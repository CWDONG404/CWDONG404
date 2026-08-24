# GitHub 个人主页回档说明

这个仓库使用普通 Git 提交和标签保留每次主页版本，不需要覆盖历史，也不需要强制推送。

## 撤销极简白灰主页

在仓库目录执行：

```powershell
git switch main
git pull --ff-only
git revert profile-v1-minimal-20260824
git push origin main
```

这会创建一个新的撤销提交，把 `README.md` 恢复到改版前的基线状态，并完整保留历史。

## 从基线重新制作

如果只想取回改版前的 `README.md`，而不撤销其他文件：

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
