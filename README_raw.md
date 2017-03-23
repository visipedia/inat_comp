# iNaturalist Competition 
Please open an issue if you have questions or problems with the dataset.

# 2017 Competition
The 2017 competition is part of the [FGVC^4 workshop](fgvc.org) at [CVPR](http://cvpr2017.thecvf.com/). 

## Details

* Number of Species: X
* Number of Training Images: Y 
* Number of Validation Images: Z
* Number of Testing Images: W

Super Categories:

| Name | Species Count | Train + Val Image Count |
|------|---------------|-------------|
| Aves | 964 | 235521 | 
| Plantae | 2101 | 196613 |
| Insecta | 1021 | 118555 |
| Reptilia | 289 | 40881 |
| Mammalia | 186 | 32823 |
| Amphibia | 115 | 17703 |
| Mollusca | 93 | 9377 |
| Fungi | 121 | 7606 |
| Animalia | 77 | 6590 |
| Arachnida | 56 | 5959 |
| Actinopterygii | 53 | 2619 |
| Chromista | 9 | 542 |
| Protozoa | 4 | 381 |
| | | |
|Total| 5089 | 675170 |

## Evalutation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image $i$, an algorithm will produce 5 labels $l_{ij}$, $j=1,\ldots,5$. We allow 5 labels because some species are distinguished with additional data provided by the observer, such as latitude & longitude or date. Each image has one ground truth label $g_i$, and the error for that image is:
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
  "rights_holder" : str
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
Depends on if we use Kaggle or not...
```
[{
  "image_id" : int,
  "category_id" : int,
  "score" : float
}]
```
