# GitHub 个人主页回档说明

这个仓库使用普通 Git 提交和标签保留每次主页版本，不需要覆盖历史，也不需要强制推送。

## 从黑金版退回此前的白灰版

黑金版合并前的主页保存在标签 `profile-before-black-gold-20260824`。如果以后不喜欢黑金版，可以恢复这几个主页文件并创建一次普通回档提交：

```powershell
git switch main
git pull --ff-only
git restore --source profile-before-black-gold-20260824 -- README.md ROLLBACK.md
git rm .github/workflows/contribution-animation.yml
git rm assets/contribution-snake-dark.svg assets/contribution-snake-light.svg
git commit -m "revert: restore profile before black-gold redesign"
git push origin main
```

这不会删除任何历史。黑金版自身保存在标签 `profile-black-gold-20260824` 和分支 `black-gold-preview` 中，之后仍可恢复。

## 撤销某一次修改

先用 `git log --oneline` 找到需要撤销的提交，再执行：

```powershell
git switch main
git pull --ff-only
git revert <提交哈希>
git push origin main
```

这会创建一个新的撤销提交，并完整保留历史。

## 从基线重新制作

如果想把主页整体恢复到首次改版前，而不改写提交历史：

```powershell
git switch main
git pull --ff-only
git restore --source profile-baseline-20260824 -- README.md
git commit -m "revert: restore profile baseline"
git push origin main
```

## 查看已有版本

```powershell
git log --oneline --decorate
git tag --list "profile-*"
```

> 如果希望完全恢复到“没有个人主页仓库”的状态，还需要在 GitHub 中把仓库设为私有或删除仓库；这属于额外的账号级操作，不会自动执行。
