# This bash script uses git to synchronize changes between the local and remote GitHub repository.

# steps:
# 1. stage all changes
# 2. commit changes with message 'Updated'
# 3. pull changes from remote repository. 
# 4. push changes to remote repository on branch 'main'.


# Stage all changes
git add .

# Commit changes
git commit -m "Updated"

# Pull changes from the remote repository. This is a fetch and merge operation.
git pull origin main

# Push changes to the remote repository on branch 'main'
git push origin main

# Echo a message to the console
echo "Changes synchronized successfully!"
