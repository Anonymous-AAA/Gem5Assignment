from m5.objects.ReplacementPolicies import RandomRP,LRURP,FIFORP,MRURP



assocs=[2,4,8,512]   #512 for fully assoc
cache_policies=[RandomRP,LRURP,FIFORP,MRURP]



for assoc in assocs:
    for cache_policy in cache_policies:
        