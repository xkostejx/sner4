import string
import random
import unittest

from django.forms.models import model_to_dict
from django.urls import reverse
from django.test import Client
from .models import Net


class NetMapTest(unittest.TestCase):
    def get_random_Net(self):
	ip, cidr, ip_first, ip_last, organization, \
	description, note = (None, None, None, None, None, None, None)

	if random.randint(0,100) % 2 == 0:
	    ip = '.'.join('%s' % random.randint(0, 255) for i in range(3))
	    cidr = "%s.0/24" % (ip)
	    ip_first = "%s.1" % (ip)
	    ip_last = "%s.255" % (ip)
	else:
	    ip = "2001:db8:%s" % \
                (":".join(("%x" % random.randint(0, 16**4) for i in range(2))))
	    cidr = "%s::/112" % (ip)
	    ip_first = "%s::1" % (ip)
	    ip_last = "%s::ffff" % (ip)
	
        organization = ''.join( \
                         random.choice(string.lowercase) for x in range \
                         (Net._meta.get_field('organization').max_length))
        description = ''.join(  \
                            random.choice(string.lowercase) for x in range \
                            (Net._meta.get_field('description').max_length))
        note = ''.join( \
                            random.choice(string.lowercase) for x in range \
                            (Net._meta.get_field('note').max_length))

        return Net( cidr=cidr, ip_first=ip_first, ip_last=ip_last, \
                    organization=organization, description=description, \
                    note=note)
    
    def setUp(self):
        self.client = Client()

    def test_list(self):
        response = self.client.get(reverse('net_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_nets_exists(self):
        net = self.get_random_Net()
        net.save()
        response = self.client.get(reverse('net_edit', args=[net.id]))
        self.assertEqual(response.status_code, 200)
   
    def test_net_add(self):
        net = self.get_random_Net()
        response = self.client.post(reverse('net_add'), model_to_dict(net))
        self.assertEquals(response.status_code, 302)

        net_db = Net.objects.last()
        self.assertEquals(net.cidr, net_db.cidr )

    def test_net_edit(self):
        net = self.get_random_Net()
        net.save()
        response =  self.client.get(reverse('net_edit', args=[net.id]))
        form = response.context['form']
        data = form.initial
       
        net_edit = self.get_random_Net()
       
        data['cidr'] = net_edit.cidr
        data['ip_first'] = net_edit.ip_first
        data['ip_last'] = net_edit.ip_last
        data['description'] = net_edit.description
        data['note'] = net_edit.note

        response = self.client.post(reverse('net_edit', args=[net.id]),data)
        self.assertEquals(response.status_code, 302)

        net_db = Net.objects.get(id=net.id)
        self.assertEquals(net_db.cidr, net_edit.cidr)
        self.assertEquals(net_db.ip_first, net_edit.ip_first)
        self.assertEquals(net_db.description, net_edit.description)
        self.assertEquals(net_db.note, net_edit.note)

