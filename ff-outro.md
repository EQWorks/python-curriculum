# Outro

From Part 00 to 03, we have gone through a short (7 weeks) and a rather unconventional path to learning Python programming.

This outro serves as another background introduction for the journey onward.

## Open-source

The _open-source software movement_ started in the 80s, initially as the _free software movement_. Since then, we have enjoyed a constant improvement in how we work, live, learn, and communicate.

The immediate values of open-source software are apparent. They are usually free to use. Users can change software behaviors without waiting for the providers to do it for them. For a providing party, open-source brings benefits of open scrutiny to the quality and security measures. It demonstrates their confidence and opinions to attract a fanbase and build up ecosystems. For organizations using open-source technologies, hiring and onboarding become much simpler without expensive training and obtaining certificates from the proprietary counterparts.

In-depth, there are qualities and practices of open-source communities that impact our workplace and society in profound ways.

### Transparency by default

While open-source communities and projects present in many shapes and forms, even when they are for-profit, the one prominent trait in common is the transparency of the software source code and its timeline of changes. As a result, this usually leads to other aspects such as the issue/feedback tracking, feature discussions, peer-review, product deployment, etc., to be open to public examination. The transparency allows the software development process to be more socially inclusive, encouraging participants to contribute to the various parts of the development lifecycle.

Empowered by transparency, open-source communities often devise pragmatic and objective-focused methodologies, eliminating as many intermediaries and manual processes as possible. Contributors can infer as much as possible from available information before involving others. These methodologies evolve as fast as the open-source software projects themselves, fluidly adapt to the people who make and use the software instead of the rigid models seen from the conventional corporate world, giving such communities a considerable edge to stay agile and competitive. The transparency also generates more data that drives more opportunities to help make data-driven decisions.

### Asynchronous and Decentralized Workforce

Open-source participants jointly form a workforce that resembles an efficient network system that is asynchronous and decentralized. With an abundance of information, minimal layers of people and processes to get in each other's way, and a growingly sophisticated set of tools and automation, open-source contributors can collaborate efficiently at any time and in any location.

This asynchronous workforce model defies the conventional way practically unchanged from the First Industrial Revolution. It better embraces the Information Age, especially with the catalyst known as the internet. The model leads to realizations of how elaborate choices of where and when to work not only do not diminish productivity, but by respecting each others' time, life, and work style, we see less burnout and more innovations spark out.

The synchronous forms of communication do not entirely vanish. They become more scarce and thus more treasured by each other. When participants resolve most motions asynchronously, the calls and meetings become laser-focused on the unresolved remainders, preserving time and effort. Equally importantly, the in-person times serve a great socialization purpose to remind us that we are still humans.

### Automation and Hacking

To sustain an asynchronous and decentralized workforce with a massive amount of information exposed through transparency, open-source participants frequently make and improve automation to optimize or abstract away processes. This mindset drives people to continually lookout for new ways to adapt and improve their workflow.

But it is rare for existing tools and automation to provide a perfect fit for everyone's use-cases. People resort to hacking, or creative workarounds, to bend tools to their will.

The hacking culture is common in making open-source software itself, providing an organic counter-balance to some problems that plague many projects, such as under-documentation, lack of testing, and [leaky abstractions](https://en.wikipedia.org/wiki/Leaky_abstraction).

## git

Among many tools that support the open-source software ecosystem, `git` is the most popular one that provides efficient ways to distribute and manage source code. Its decentralized nature allows every contributor to fully access the working copy and the entire change history and derivatives.

The collaboration happens in a peer-to-peer fashion. Collaborators branch out the source code to implement new features or issue fixes. Upon concluding the implementation, the contributor requests to merge back to the mainstream working copy of the source code, attract others to review, and offer suggestions to improve. When enough contributors reach a consensus, the implementation gets merged back to the mainstream. During this entire process, automation plays a critical role in simplifying every participant's experience through automated testing and suggestions, so contributors do not waste time on trivial problems such as code-style differences and logical flaws. After the merge, it is common to see automated deployment or release of the software to a designated audience.

When unresolvable disagreements break out, one can _fork_ the project to evolve the software to another trajectory without impacting other collaborators. The practice of forking is why we have a diverse number of Linux distributions.

### GitHub

However, due to a barrier to converting from a centralized mindset to a decentralized one from its users, `git` was notoriously convoluted and hard to utilize. Toward the end of 2007, a group of software developers who enjoyed `git` but envisioned better ways to use it started building what's known as GitHub today, making `git` usages a pleasant experience even for people who are not developers. They have been building GitHub using `git` and GitHub itself, a practice known as [dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food).

The company started as profitable from day one, refrained from taking external funding until [July 2012](https://www.reuters.com/article/github-fundraising/github-raises-100-mln-from-andreessen-horowitz-idUSL2E8I9AV320120709), and stayed as a flat organization with 234+ employees until [17 July 2014](https://en.wikipedia.org/wiki/Timeline_of_GitHub).

Perhaps the root of their success is a culture that emphasizes [people's happiness instead of money](https://tom.preston-werner.com/2010/10/18/optimize-for-happiness.html). The culture reflects in their ability to [develop quality products](https://github.blog/changelog/) that embrace and encourage the best practices from open-source communities and benefit even proprietary developments. Not surprisingly, they are also a large contributor to various open-source software projects, with an adopted [Open Source (Almost) Everything](https://tom.preston-werner.com/2011/11/22/open-source-everything.html) mindset.

Such emphasis on people's happiness through their interpretation of open-source practices allows the company to attract top talents worldwide to collaborate on a service platform enjoyed by their users. By 2010 (a little over three years since inception), GitHub has claimed to be the largest host of source code in the world until today.

## EQ Works - our adaptation of open-source

A key idea behind the open-source movement is to leverage their learnings to make information and curation more transparent and efficient. This social movement coincides with the phenomenon of the internet-driven information explosion and the increasing realization of how closed platforms could [unethically profit from manipulating the information flow and shape](https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal).

As a part of the workspace meta shift, more organizations start to realize the benefits of open-source software and their community practices. Since around the beginning of 2014, our dev team has started to build products using open-source technologies and evolve our culture by adapting the open-source ways.

### Round-table wisdom

Instead of on-paper seniority, materialized merits become the only valid argument between project contributors in discussions and debates. We demonstrate cases in a verifiable way, rapidly iterate based on feedback, and make frequent releases with peer-review and automation that capture rudimentary errors through various quality-assurance measures.

The practice allows us to eliminate hierarchy and processes to boost productivity and innovation opportunities while maintaining a flat and fluid team. We eradicate conventional constraints to give everyone the freedom to pursue after their passion and the power to develop, test, and deploy their implementations through the available tools and automation without waiting for others.

### Respect Time - Work Alone, Together

The transparent and asynchronous model of information distribution allows our collaboration and communication to be in a manner that respects each other's time. With the information availed to us, each team member infers and summarizes on their own time to form most decisions without bothering or getting blocked by others. The abundance of tools and services, combined with a hacking culture, allows us to automate away conventional chores and costly events to direct our time and efforts for more valuable tasks.

We encourage the utilization of text-based communication such as shared calendars, to-do lists, group chat, and discussions. This way, we retain information as a raw and searchable form of a knowledge base. With the help of tools and automation built on top of the services we use, we distill the knowledge into well-formed documentation for future reference. Team status and technical updates are automatically organized and shared across, so we can spend our time on unresolved problems instead of waiting for a debriefing from each other.

And in the event of required synchronous communication, such as meetings, we have been [developing and evolving](https://github.com/EQWorks/common/blob/master/communications/meetings.md) our method to minimize manual processes and make such events less expensive, more valuable, and more scalable.

<!--
## Prospects

ML accelerated automation for more elimination of processes and partial or entire job functions
-->
