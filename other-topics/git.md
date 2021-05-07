# Collaboration through Git

As introduced in the [Python Basics outro](../basics/ff-outro.md#git), [`git`](https://git-scm.com) is the predominant tool for decentralized code collaboration.

Platforms like GitHub fill an indispensable role in further easing the adoption and utilization of `git` and empowering the software communities to prosper.

Like Python, we will not cover _how_ to install `git`. You can find plenty of information on its [official site](https://git-scm.com).

## locussdk-collab

We will take this opportunity to initiate our [`locussdk-collab`](https://github.com/EQWorks/locussdk-collab) project to contribute ideas and recipes to help other users of LOCUS SDK/Notebook with similar needs. LOCUS SDK maintainers will also actively incorporate great ideas and recipes into the core project.

Let us begin with something trivial, and along the way, see how to use `git` to achieve version control and collaborations.

## Empty repository

We will use GitHub to host the project. At this point, the repository is empty.

![empty](https://user-images.githubusercontent.com/2837532/117354169-069d8c00-ae7f-11eb-85d4-375ae8e70e52.png)

For maintainers, the empty repository page on GitHub typically shows some useful commands that we can run from our local computer to get started. The command-line experience may vary depending on your choice of the operating system, command-line tool, and `git` client.

First, make a local directory (folder) and populate it with a `README.md` file and some content in it:

```shell
% mkdir -p locussdk-collab  # create the locussdk-collab directory if it doesn't exist
% cd locussdk-collab  # get into the directory
% # create a README.md with some content
% echo "# locussdk-collab\n\nCommunity collaboration on ideas and practical workflows using LOCUS SDK" >> README.md
```

The `.md` extension means that `README.md` interprets as a [Markdown](https://en.wikipedia.org/wiki/Markdown) file. Its content would look like this:

```md
# locussdk-collab

Community collaboration on ideas and practical workflows using LOCUS SDK
```

Next, let's `git` it up:

```shell
% git init  # initialize the directory as a local git repository
% git status  # check the status of our repository
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    README.md

nothing added to commit but untracked files present (use "git add" to track)
```

The output of `git status` offers valuable insights and suggestions. Based on the information, we should proceed to add the file to commit:

```shell
% git add README.md
% git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file:   README.md
```

We now have code changes -- the addition of the new file `README.md`, to be committed:

```shell
% git commit -m "README - init with project introduction"
[main a61f24e] README - init with project introduction
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
```

Conceptually speaking, each commit is a collection of file/code changes, along with a mandatory message conveying the objective and some signatures that `git` automatically generates or associates to it.

Whenever making change commits, try to follow [some good conventions](https://github.com/EQWorks/common/blob/master/git.md#on-commits) to have well-scoped code changes and pair them with a concise and relevant message.

We can examine all the commit history:

```shell
% git log
commit a61f24ee507f19a839686b75e166eaf574cfa3a0 (HEAD -> main)
Author: Runzhou Li (woozyking) <runzhou.li@gmail.com>
Date:   Thu May 6 17:07:14 2021 -0400

    README - init with project introduction
```

So far, there is only one commit. As mentioned, other than the commit file/code changes, `git` automatically includes a commit `hash`, its author, and a date-time, along with the author's commit message.

Now we have the change committed locally. It is time to push it up to the GitHub hosted remote repository:

```shell
% git remote add origin git@github.com:EQWorks/locussdk-collab.git
% git push -u origin main
```

The first command adds a remote (repository) named `origin` that points to the GitHub hosted repository we recently created. The second command pushes up our local `main` branch to the remote branch with a matching name, using the `-u` option as a shorthand to make the association.

After pushing up the `main` branch with the first commit, we now have:

![first commit](https://user-images.githubusercontent.com/2837532/117367661-78ca9c80-ae90-11eb-9dc2-3ba356e47e21.png)

## Branch out

Branches are another essential element of `git`. Through branching, collaborators with _write_ access to the repository can safely experiment and make new commits without impacting the `main` branch until they are confident to _merge_.

GitHub takes branching one step further through _forking_ or making a new remote clone of the original repository. Collaborators do not necessarily need to obtain _write_ access to the original repository to make commits.

Through either branching or forking, once the collaborators are confident about the commits, they can suggest the changes to be pushed back into the original repository through [_pull requests_](https://docs.github.com/en/github/getting-started-with-github/github-glossary#pull-request).

Pull requests allow the collaborators and maintainers to discuss and vet the commits' changes, sometimes with the help of automated quality assurance processes, before merging the commits into a designated staple branch (usually `main`).

Let us make our first contribution to `locussdk-collab` by adding a simple recipe function to search for matching POI lists by a single name.

Since I have the _write_ access to the repository, we will proceed with `git` native branching.

The first thing to do is to make a new local branch to introduce the changes:

```shell
% git checkout -b recipe/search-avail-poi-lists
Switched to a new branch 'recipe/search-avail-poi-lists'
```

We use a shorthand to _checkout_ a newly created branch, using the `-b` option followed by the desired branch name. Depending on the conventions, branch names may or may not carry as much significance as commit messages. However, it is generally favorable to use a succinct and relevant branch name for yourself and other collaborators.

We will proceed to create a new directory within the local repository and develop our recipe Python script in it:

```shell
% mkdir -p recipes
% touch recipes/search_poi_lists.py
```

## Contribute

Recall our objective for the recipe:

> a simple recipe function to search for matching POI lists by a single name.

After some brief research, the [`pandas.Series.str.contains()` method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html) seems to be appropriate to do the job.

```python
from locussdk import get_avail_poi_lists


def search_poi_lists(name):
    global_lists = get_avail_poi_lists(list_type='global')

    return global_lists[global_lists['name'].str.contains(name)]
```

When used:

```python
>>> search_poi_lists('pizza')
                name  poi_list_id whitelabelid customerid
67       Bostonpizza           71         None       None
113       Pizzapizza          118         None       None
175  Neworleanspizza          180         None       None
422       Royalpizza          427         None       None
450       Ginospizza          455         None       None
786      Doublepizza          791         None       None
```

Let us commit this:

```shell
% git add recipes/search_poi_lists.py
% git commit -m "recipe - search available POI lists by name"
[recipe/search-poi-lists bcc472c] recipe - search available POI lists by name
 1 file changed, 7 insertions(+)
 create mode 100644 recipes/search_poi_lists.py
```

And push it up to the matching remote branch as we did with the initial `README.md` change. But this time, it will not go into the `main` staple branch just yet:

```shell
% git push -u origin recipe/search-poi-lists
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 503 bytes | 503.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'recipe/search-poi-lists' on GitHub by visiting:
remote:      https://github.com/EQWorks/locussdk-collab/pull/new/recipe/search-poi-lists
remote:
To github.com:EQWorks/locussdk-collab.git
 * [new branch]      recipe/search-poi-lists -> recipe/search-poi-lists
Branch 'recipe/search-poi-lists' set up to track remote branch 'recipe/search-poi-lists' from 'origin'.
```

Once we have the branch pushed up, on GitHub the repository would prompt if we would like to make a pull request:

![prompt](https://user-images.githubusercontent.com/2837532/117470516-e45e4980-af24-11eb-9e13-4022cd80b0cf.png)

Let's go ahead and do that, as well as inviting some team members to review:

![pr](https://user-images.githubusercontent.com/2837532/117471163-9138c680-af25-11eb-96dc-98452fe47e16.png)

## Walk the edge

For someone who may be interested in the bleeding edge development of this recipe, they can clone the repository locally and test it out:

```shell
% git clone https://github.com/EQWorks/locussdk-collab.git
Cloning into 'locussdk-collab'...
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 7 (delta 0), reused 7 (delta 0), pack-reused 0
Receiving objects: 100% (7/7), done.
% cd locussdk-collab
% git checkout recipe/search-poi-lists
Branch 'recipe/search-poi-lists' set up to track remote branch 'recipe/search-poi-lists' from 'origin'.
Switched to a new branch 'recipe/search-poi-lists'
```

They can also fork this repository to their own GitHub account, make and commit changes, and initiate some pull requests to the original repository's `recipe/search-poi-lists` branch. Pull requests do not always have to go into the staple (usually `main`) branch. This flexibility is very empowering to groom a versatile and vibrant collaboration environment.

## Iterate

![reviews](https://user-images.githubusercontent.com/2837532/117485833-ddd8cd80-af36-11eb-9ff5-180b4ff03cc3.png)

After gathering some feedback in the [pull request](https://github.com/EQWorks/locussdk-collab/pull/1) we made for the first recipe, let us incorporate comments and suggestions to improve things.

First, let's make it possible for a case-insensitive search for broader search scope, and make it `False` by default:

```python
from locussdk import get_avail_poi_lists


def search_poi_lists(name, case=False):
    global_lists = get_avail_poi_lists(list_type='global')

    return global_lists[global_lists['name'].str.contains(name, case=case)]
```

```python
>>> search_poi_lists('pizza')
                name  poi_list_id whitelabelid customerid
67       Bostonpizza           71         None       None
113       Pizzapizza          118         None       None
116       Pizzaville          121         None       None
117     Pizzadelight          122         None       None
139        Pizzanova          144         None       None
157         Pizzahut          162         None       None
175  Neworleanspizza          180         None       None
327         241Pizza          332         None       None
422       Royalpizza          427         None       None
450       Ginospizza          455         None       None
730     Mammas Pizza          735         None       None
786      Doublepizza          791         None       None
>>> # test when case=True
>>> search_poi_lists('pizza', case=True)
                name  poi_list_id whitelabelid customerid
67       Bostonpizza           71         None       None
113       Pizzapizza          118         None       None
175  Neworleanspizza          180         None       None
422       Royalpizza          427         None       None
450       Ginospizza          455         None       None
786      Doublepizza          791         None       None
```

Let's further examine the [`pandas.Series.str.contains()` documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html). There are quite a few arguments like `case` that we can relay, using a Python mechanism known as unpacking, and a convention known as _Keyword (or Named) Arguments_. Together they are commonly expressed as `**kwargs`:

```python
from locussdk import get_avail_poi_lists


def search_poi_lists(name, **kwargs):
    global_lists = get_avail_poi_lists(list_type='global')

    return global_lists[global_lists['name'].str.contains(name, **kwargs)]
```

Conceptually, we are relaying the _Keyword Arguments_ that users of this function may optionally supply:

```python
>>> search_poi_lists('some name', case=True, regex=False)
```

What happens within the function execution is that the `pandas.Series.str.contains()` method gets them as they are supplied to the function:

```python
    return global_lists[global_lists['name'].str.contains(name, case=True, regex=True)]
```

Let's use another side example to illustrate the underlying unpacking behavior:

```python
def concat(a, b):
    return a + b
# params dict
params = {
  'a': 'leo',
  'b': 'ric',
}
# unpack dict as keyword arguments a= and b=:
concat(**params)
# conceptually equivalent to manually call as:
concat(a=params['a'], b=params['b'])
```

Effectively we allow users of the `search_poi_lists()` function to fully enjoy the power behind the Pandas mechanism by doing less. We always prefer less code if it can achieve the same or better.

Let us make a commit based on this change since its scope is now well defined:

```shell
% git status
On branch recipe/search-poi-lists
Your branch is up to date with 'origin/recipe/search-poi-lists'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
  modified:   recipes/search_poi_lists.py

% git add -u  # add updated/modified file(s)

% git status
On branch recipe/search-poi-lists
Your branch is up to date with 'origin/recipe/search-poi-lists'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
  modified:   recipes/search_poi_lists.py

% git commit -m "recipe - search_poi_lists() support pd.Series.str.contains arguments such as 'case'"

% git status
On branch recipe/search-poi-lists
Your branch is ahead of 'origin/recipe/search-poi-lists' by 1 commit.
  (use "git push" to publish your local commits)

% git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 458 bytes | 458.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:EQWorks/locussdk-collab.git
   bcc472c..d017109  recipe/search-poi-lists -> recipe/search-poi-lists
```

Knowing our change commit is all well preserved on the remote, we can move further with other suggestions, such as extending beyond searching just the "global" POI lists:

```python
from locussdk import get_avail_poi_lists


def search_poi_lists(name, **kwargs):
    # build parameters we want to pass into get_avail_poi_lists()
    params = {'list_type': 'global'}  # default search in global
    for k in ['list_type', 'whitelabel', 'customer']:
        if v := kwargs.pop(k, None):
            params[k] = v

    lists = get_avail_poi_lists(**params)

    return lists[lists['name'].str.contains(name, **kwargs)]
```

```shell
% git add -u
% git commit -m "recipe - search_poi_lists() support locussdk.get_avail_poi_lists() arguments such as 'list_type'"
[recipe/search-poi-lists 8eea16e] recipe - search_poi_lists() support locussdk.get_avail_poi_lists() arguments such as 'list_type'
 1 file changed, 13 insertions(+), 7 deletions(-)
 rewrite recipes/search_poi_lists.py (60%)
```

And adding typing, inline-documentation, and sensible defaults for both arguments and output return behaviors:

```python
from pandas import DataFrame
from locussdk import get_avail_poi_lists


def search_poi_lists(name: str = '', **kwargs) -> DataFrame:
    '''Search available POI lists based on locussdk.get_avail_poi_lists().

    Args:
        name (str): name to search in the available POI lists.
        **kwargs:
            All locussdk.get_avail_poi_lists() supported arguments.
            All pandas.Series.str.contains() supported arguments.

    Returns:
        pandas.DataFrame that contains the search resulting POI lists.

    Examples:
    >>> search_poi_lists('pizza')
                name  poi_list_id whitelabelid customerid
    67       Bostonpizza           71         None       None
    113       Pizzapizza          118         None       None
    116       Pizzaville          121         None       None
    117     Pizzadelight          122         None       None
    139        Pizzanova          144         None       None
    157         Pizzahut          162         None       None
    175  Neworleanspizza          180         None       None
    327         241Pizza          332         None       None
    422       Royalpizza          427         None       None
    450       Ginospizza          455         None       None
    730     Mammas Pizza          735         None       None
    786      Doublepizza          791         None       None
    '''
    # build parameters we want to pass into get_avail_poi_lists()
    params = {'list_type': 'global'}  # default search in global
    for k in ['list_type', 'whitelabel', 'customer']:
        if v := kwargs.pop(k, None):
            params[k] = v

    lists = get_avail_poi_lists(**params)

    # return all available POI lists if no search string given
    if not name:
        return lists

    return lists[lists['name'].str.contains(name, **kwargs)]
```

You can examine the code changes before committing using the `git diff` command:

```shell
% git diff
diff --git a/recipes/search_poi_lists.py b/recipes/search_poi_lists.py
index 122dc77..31e59ea 100644
--- a/recipes/search_poi_lists.py
+++ b/recipes/search_poi_lists.py
@@ -1,7 +1,35 @@
+from pandas import DataFrame
 from locussdk import get_avail_poi_lists


-def search_poi_lists(name, **kwargs):
+def search_poi_lists(name: str = '', **kwargs) -> DataFrame:
+    '''Search available POI lists based on locussdk.get_avail_poi_lists().
+
+    Args:
+        name (str): name to search in the available POI lists.
+        **kwargs:
+            All locussdk.get_avail_poi_lists() supported arguments.
+            All pandas.Series.str.contains() supported arguments.
+
+    Returns:
+        pandas.DataFrame that contains the search resulting POI lists.
+
+    Examples:
+    >>> search_poi_lists('pizza')
+                name  poi_list_id whitelabelid customerid
+    67       Bostonpizza           71         None       None
+    113       Pizzapizza          118         None       None
+    116       Pizzaville          121         None       None
+    117     Pizzadelight          122         None       None
+    139        Pizzanova          144         None       None
+    157         Pizzahut          162         None       None
+    175  Neworleanspizza          180         None       None
+    327         241Pizza          332         None       None
+    422       Royalpizza          427         None       None
+    450       Ginospizza          455         None       None
+    730     Mammas Pizza          735         None       None
+    786      Doublepizza          791         None       None
+    '''
     # build parameters we want to pass into get_avail_poi_lists()
     params = {'list_type': 'global'}  # default search in global
     for k in ['list_type', 'whitelabel', 'customer']:
@@ -10,4 +38,8 @@ def search_poi_lists(name, **kwargs):

     lists = get_avail_poi_lists(**params)

+    # return all available POI lists if no search string given
+    if not name:
+        return lists
+
     return lists[lists['name'].str.contains(name, **kwargs)]
```

All looks good:

```shell
% git add -u
% git commit -m "recipe - add typing, docs and defaults for search_poi_lists()"
[recipe/search-poi-lists 7c78644] recipe - add typing, docs and defaults for search_poi_lists()
 1 file changed, 33 insertions(+), 1 deletion(-)
```

We should have 2 commits await, let's push them up to our remote repository:

```shell
% git status
On branch recipe/search-poi-lists
Your branch is ahead of 'origin/recipe/search-poi-lists' by 2 commits.
  (use "git push" to publish your local commits)

% git push
<output omitted>
```

On GitHub, I can go ahead and mark all the inline comments as resolved:

![resolved](https://user-images.githubusercontent.com/2837532/117489910-26df5080-af3c-11eb-9ccd-4e4aab0351ba.png)

And once some of the reviewers get a chance to review again and possibly approve, we may have our first recipe officially merged back into the `main` branch, indicating that we are ready to share it with the world!

![merge](https://user-images.githubusercontent.com/2837532/117502536-a4f82300-af4d-11eb-9690-d2272a73b873.png)

![updated](https://user-images.githubusercontent.com/2837532/117502663-d375fe00-af4d-11eb-9aa8-e0d15f402a8f.png)

GitHub offers various other features such as [issues](https://guides.github.com/features/issues/) for feature requests and bug reports and many more.

## References

* [`git` official website](https://git-scm.com)
* [Introduction to GitHub by The GitHub Training Team](https://lab.github.com/githubtraining/introduction-to-github)
