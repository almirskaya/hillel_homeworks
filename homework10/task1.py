from animal.cold_blooded.fish.guppy import Guppy
from animal.cold_blooded.fish.salmon import Salmon
from animal.warm_blooded.mammals.bear import Bear
from animal.warm_blooded.mammals.whale import Whale
from animal.warm_blooded.birds.eagle import Eagle
from animal.warm_blooded.birds.peacock import Peacock


if __name__ == "__main__":
    bear = Bear('Panda', 'Asia', 'Warm-blooded', 'Fur', False)
    bear.is_predator()
    bear.eat()
    bear.feed_offspring()
    bear.sleep()
    print('-' * 10)
    whale_blue = Whale('Blue Whale', 'Pacific Ocean', 'Warm-blooded', 'blubber', 1000)
    whale_fin = Whale('Fin Whale', 'Pacific Ocean', 'Warm-blooded', 'blubber', 1100)
    whale_blue.socialize(whale_fin.name)
    whale_fin.sing()
    print('-' * 10)
    eagle = Eagle('Golden Eagle', 'North America', 'Warm-blooded', 'grey', 1.5)
    salmon = Salmon('Pink salmon', 'North America', 'Cold-blooded', 'pink', False)
    eagle.hunt(salmon.name)
    print('-' * 10)
