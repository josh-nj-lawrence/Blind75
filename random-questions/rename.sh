for file in ./**; do
    if [[ $file == *"leetcode"* ]]; then
        newname=${file//[^0-9]/}
        ext=${file##*.}
        echo "Renaming $file to $newname.$ext"
        mv "$file" "$newname.$ext"
    else
        echo "$file is correctly formatted"
    fi  
done