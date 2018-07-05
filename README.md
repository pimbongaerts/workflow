## Reference manager (Zotero/Zotfile/Dropbox)
Using [zotero](https://www.zotero.org/) with [ZotFile](http://zotfile.com/). Keeping synchronized across devices through Dropbox following [these instructions](http://islamicate-dh.github.io/2016-05-27-set-up-zotero-between-multiple-computers/). Basically, by using an identical path (`/Users/pimbongaerts/Dropbox/Zotero`) to store attachments on all devices, and by using this path in *Custom Location* of the *General Settings* of Zotfile, and as *Base directory* in the *Files and Folders* settings of the *Advanced* Zotero preferences. Additional settings include changing *automatically rename new attachments* to *always* in the Zotfile settings and unchecking the two options under *File Syncing* in the Zotero preferences (to avoid using Zotero's storage to sync attachments.

## Window management (Spectacle)
[Spectacle](https://github.com/eczarny/spectacle) provides easy window management on the Mac, with customizable shorcuts to neatly organize windows across screen(s).

## Terminal
Oh My Zsh - configuration manager for zsh: https://github.com/robbyrussell/oh-my-zsh
Antigen - plug-in manager for zsh: https://github.com/zsh-users/antigen


Created symlink for sublime:
sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/sb

Use CAPSLOCK as ESCAPE through System Preferences > Keyboard > Modified Keys

Created a symlink for .zshrc file:
ln -s ~/Github/workflow/dotfiles/zsh/.zshrc ~/.zshrc
