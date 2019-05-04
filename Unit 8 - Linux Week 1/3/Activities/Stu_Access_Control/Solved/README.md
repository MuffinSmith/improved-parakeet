# Access Control
In this exercise, you'll review UFW by blocking HTTP and HTTPS traffic to/from your machine.

## Instructions
### Web Traffic Pt 1
> **Solution**
> ```bash
> $ sudo ufw enable
> $ sudo ufw logging on
> $ sudo ufw deny 80/tcp
> ```
### Web Traffic Pt 1
> **Solution**
> ```bash
> $ sudo ufw enable
> $ sudo ufw logging on
> $ sudo ufw deny 443/tcp
> ```

## Reinforcement

- After blocking HTTP traffic, you probably noticed you were still able to browse to several sites, but _not_ to `collegehumor.com` or `example.com`. Explain why.
  > **Solution**: This is because blocking port 80 _only_ affects HTTP traffic, _not_ HTTPS traffic. Since most sites run over HTTPS, you'll still be able to hit many of them—just not those served over HTTP.