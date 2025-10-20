import java.util.*;

public class Problem355 {

    Map<Integer, User> users;
    Map<Integer, Integer> tweetTime;
    int counter;

    private class User {
        int userId;
        Set<Integer> following;
        List<Integer> tweets;

        public User(int userId) {
            this.userId = userId;
            this.following = new HashSet<>();
            this.tweets = new ArrayList<>();
        }
    }

    public Problem355() {
        users = new HashMap<>();
        tweetTime = new HashMap<>();
        counter = 0;
    }

    public void postTweet(int userId, int tweetId) {
        users.putIfAbsent(userId, new User(userId));
        users.get(userId).tweets.add(tweetId);
        tweetTime.put(tweetId, counter++);
    }

    public List<Integer> getNewsFeed(int userId) {
        if (!users.containsKey(userId)) return new ArrayList<>();

        List<Integer> news = new ArrayList<>(users.get(userId).tweets);

        for (int followee : users.get(userId).following) {
            if (users.containsKey(followee))
                news.addAll(users.get(followee).tweets);
        }

        news.sort((a, b) -> tweetTime.get(b) - tweetTime.get(a));

        return news.subList(0, Math.min(10, news.size()));
    }

    public void follow(int followerId, int followeeId) {
        users.putIfAbsent(followerId, new User(followerId));
        users.get(followerId).following.add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        users.putIfAbsent(followerId, new User(followerId));
        users.get(followerId).following.remove(followeeId);
    }

    public static void main(String[] args) {
        Problem355 twitter = new Problem355();

        twitter.postTweet(1, 5);
        System.out.println(twitter.getNewsFeed(1)); // [5]
        twitter.follow(1, 2);
        twitter.postTweet(2, 6);
        System.out.println(twitter.getNewsFeed(1)); // [6, 5]
        twitter.unfollow(1, 2);
        System.out.println(twitter.getNewsFeed(1)); // [5]
    }
}
