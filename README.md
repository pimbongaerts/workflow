## Reference manager (Zotero/Zotfile/Dropbox)
Using [zotero](https://www.zotero.org/) with [ZotFile](http://zotfile.com/). Keeping synchronized across devices through Dropbox following [these instructions](http://islamicate-dh.github.io/2016-05-27-set-up-zotero-between-multiple-computers/). Basically, by using an identical path (`/Users/pimbongaerts/Dropbox/Zotero`) to store attachments on all devices, and by using this path in *Custom Location* of the *General Settings* of Zotfile, and as *Base directory* in the *Files and Folders* settings of the *Advanced* Zotero preferences. Additional settings include changing *automatically rename new attachments* to *always* in the Zotfile settings and unchecking the two options under *File Syncing* in the Zotero preferences (to avoid using Zotero's storage to sync attachments.

## Window management (Spectacle)
[Spectacle](https://github.com/eczarny/spectacle) provides easy window management on the Mac, with customizable shorcuts to neatly organize windows across screen(s).

## Terminal
Zsh / Oh my Zsh / Antigen install:
```
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
curl -L git.io/antigen > antigen.zsh
mkdir .antigen
mv antigen.zsh .antigen
ln -s ~/Github/workflow/dotfiles/zsh/.zshrc ~/.zshrc
```

Oh My Zsh - configuration manager for zsh: https://github.com/robbyrussell/oh-my-zsh
Antigen - plug-in manager for zsh: https://github.com/zsh-users/antigen
Vundle - plug-in manager for vim: https://github.com/VundleVim/Vundle.vim

Created symlink for sublime:
sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/sb

Use CAPSLOCK as ESCAPE through System Preferences > Keyboard > Modified Keys

```shell
ln -s ~/Github/workflow/dotfiles/zsh/.zshrc ~/.zshrc
```

## Permits

Retrieve updated list of (facultatively) zooxanthellate scleractinian genera for particular oceanic region from coraltraits.org (in this example "Indian Ocean"):

```shell
> join -t , <(curl -s https://coraltraits.org/traits/35.csv\?taxonomy\=on | grep -v "observation_id" | cut -d, -f4,5,7,8,22 | sort) <(curl -s https://coraltraits.org/traits/41.csv\?taxonomy\=on | grep -v "observation_id" | cut -d, -f4,5,22 | sort) | grep -v "azooxanthellate" | grep "Indian Ocean" | awk -F'[, ]' '{print "Family " $4 "," $2 " spp."}' | sort | uniq
```

### Compile updated list of co-authors

Retrieve a list of co-authors from Google Scholar (usingthe scholarly module - https://pypi.org/project/scholarly/)  based on publications from a certain time range. 

```shell
# Install scholarly
$ pip install scholarly
# Usage example: get all co-authors of Steven A Cholewiak (developer of scholarly) for articles published between 2020 and 2021, but ignoring publications with more than 10 co-authors (-m 10), and including those without a publication year (-i)
$ python3 scholar_get_coauthors.py 'Steven A Cholewiak' 2020 2021 -m 10 -i
```

