#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main(project_list, worktree_list=None, **kwargs):
    """Main function invoked directly by repo.
    We must use the name "main" as that is what repo requires.
    Args:
      project_list: List of projects to run on.
      worktree_list: A list of directories.  It should be the same length as
          project_list, so that each entry in project_list matches with a
          directory in worktree_list.  If None, we will attempt to calculate
          the directories automatically.
      kwargs: Leave this here for forward-compatibility.
    """
    for project in project_list:
      print("Would run pre-upload-hook for project '%s'" % project)

    if worktree_list:
      for worktree in worktree_list:
        print("would run pre=upload-hook for worktree '%s'" % worktree)
    

