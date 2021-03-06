# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import pytest

from django.core.management import call_command


@pytest.mark.cmd
@pytest.mark.django_db
def test_list_projects_tutorial(capfd):
    """List site wide projects"""
    call_command('list_projects')
    out, err = capfd.readouterr()
    assert 'project0' in out
    assert 'project1' in out


@pytest.mark.cmd
@pytest.mark.django_db
def test_list_projects_modified_since(capfd):
    """Projects modified since a revision"""
    call_command('list_projects', '--modified-since=5')
    out, err = capfd.readouterr()
    assert 'project0' in out
    assert 'project1' in out
