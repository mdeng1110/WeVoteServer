# apis_v1/views_docs.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from documentation_source import device_id_generate_doc, organization_count_doc, organization_retrieve_doc, \
    voter_address_retrieve_doc, voter_address_save_doc, voter_count_doc, voter_create_doc, voter_retrieve_doc

LOCALHOST_URL_ROOT = 'http://localhost:8000'


def apis_index_doc_view(request):
    """
    Show a list of available APIs
    """
    template_values = {
        # 'key': value,
    }
    return render(request, 'apis_v1/apis_index.html', template_values)


def device_id_generate_doc_view(request):
    """
    Show documentation about deviceIdGenerate
    """
    url_root = LOCALHOST_URL_ROOT
    template_values = device_id_generate_doc.device_id_generate_doc_template_values(url_root)
    return render(request, 'apis_v1/api_doc_page.html', template_values)


def organization_count_doc_view(request):
    """
    Show documentation about organizationCount
    """
    url_root = LOCALHOST_URL_ROOT
    template_values = organization_count_doc.organization_count_doc_template_values(url_root)
    return render(request, 'apis_v1/api_doc_page.html', template_values)


def organization_retrieve_doc_view(request):
    """
    Show documentation about organizationRetrieve
    """
    url_root = LOCALHOST_URL_ROOT
    template_values = organization_retrieve_doc.organization_retrieve_doc_template_values(url_root)
    return render(request, 'apis_v1/api_doc_page.html', template_values)


def voter_address_retrieve_doc_view(request):
    """
    Show documentation about voterAddressRetrieve
    """
    url_root = LOCALHOST_URL_ROOT
    template_values = voter_address_retrieve_doc.voter_address_retrieve_doc_template_values(url_root)
    return render(request, 'apis_v1/api_doc_page.html', template_values)


def voter_address_save_doc_view(request):
    """
    Show documentation about voterSaveRetrieve
    """
    url_root = LOCALHOST_URL_ROOT
    template_values = voter_address_save_doc.voter_address_save_doc_template_values(url_root)
    return render(request, 'apis_v1/api_doc_page.html', template_values)


def voter_count_doc_view(request):
    """
    Show documentation about voterCount
    """
    url_root = LOCALHOST_URL_ROOT
    template_values = voter_count_doc.voter_count_doc_template_values(url_root)
    return render(request, 'apis_v1/api_doc_page.html', template_values)


def voter_create_doc_view(request):
    """
    Show documentation about voterCreate
    """
    url_root = LOCALHOST_URL_ROOT
    template_values = voter_create_doc.voter_create_doc_template_values(url_root)
    return render(request, 'apis_v1/api_doc_page.html', template_values)


def voter_retrieve_doc_view(request):
    """
    Show documentation about voterRetrieve
    """
    url_root = LOCALHOST_URL_ROOT
    template_values = voter_retrieve_doc.voter_retrieve_doc_template_values(url_root)
    return render(request, 'apis_v1/api_doc_page.html', template_values)