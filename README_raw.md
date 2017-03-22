# inat_comp
iNaturalist competition details

# 2017 Competition
The 2017 competition is part of the [FGVC^4 workshop]() at [CVPR](http://cvpr2017.thecvf.com/). 

## Details

Number of Species: 
Number of Training Images: 
Number of Validation Images:

## Evalutation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image $i$, an algorithm will produce 5 labels $l_{ij}$, $j=1,\ldots,5$. Each image has one ground truth label $g_i$, and the error for that image is:
$$
e_i = \min_{j}d(l_{ij}, g_i)
$$
Where
$$
d(x, y) = 
\begin{cases}
    0       & \quad \text{if } x = y \\
    1  & \quad \text{otherwise}\\
\end{cases}
$$

The overall error score for an algorithm is the average error over all $N$ test images:
$$
\text{score} = \frac{1}{N} \sum_{i} e_{i}
$$

## Annotation Format
We closely follow the annotation format of the [COCO dataset](http://mscoco.org/dataset/#download). The annotations are stored in the [JSON format](http://www.json.org/) and are organized as follows:
```
{
  "info" : info,
  "images" : [image],
  "categories" : [category],
  "annotations" : [annotation],
  "licenses" : [license]
}  

info{
  "year" : int,
  "version" : str,
  "description" : str,
  "contributor" : str,
  "url" : str,
  "date_created" : datetime,
}

image{
  "id" : int,
  "width" : int,
  "height" : int,
  "file_name" : str,
  "license" : int,
  "rights_holder" : str,
  "date_captured" : datetime
}

category{
  "id" : int,
  "name" : str,
  "supercategory" : str,
}

annotation{
  "id" : int,
  "image_id" : int,
  "category_id" : int
}

license{
  "id" : int,
  "name" : str,
  "url" : str
}
```

## Submission Format

```
[{
  "image_id" : int,
  "category_id" : int,
  "score" : float
}]
```
