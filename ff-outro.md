# Outro

From Part 00 to 03, we have gone through a short (7 weeks) and a rather unconventional path to learning Python programming.

This outro serves as another background introduction for the journey onward.

## Open-source

The _open-source software movement_ started in the 80s, initially as the _free software movement_. Since then, we have enjoyed a constant improvement in how we work, live, learn, and communicate.

The immediate values of open-source software are apparent. They are usually free to use. Users can change software behaviors without waiting for the providers to do it for them. For a providing party, open-source brings benefits of open scrutiny to the quality and security measures. It demonstrates their confidence and opinions to attract a fanbase and build up ecosystems.

In-depth, there are exciting qualities and practices of open-source communities that impact our workplace and society in profound ways.

### Transparency by default

While open-source communities and projects present in many shapes and forms, even when they are for-profit, the one prominent trait in common is the transparency of the software source code.

The transparency of the source code and its timeline of code changes lead to other aspects such as the software issue/feedback tracking, feature discussions, code peer-review, product distribution, etc., to be open to public examination. The transparency allows the software development process to be more socially inclusive, encouraging participants to contribute to the various parts of the development lifecycle.

Empowered by transparency, open-source communities often devise pragmatic and objective-focused methodologies, eliminating as many intermediaries and manual processes as possible. More importantly, these methodologies evolve as fast as the open-source software projects themselves, fluidly adapts to the people that make and use the software, instead of the rigid models seen from the conventional corporate world. The transparency generates more data that drives more opportunities to help make data-driven decisions.

### Asynchronous and Decentralized Workforce

Open-source participants jointly form a workforce that resembles an efficient network system that is asynchronous and concurrent. With an abundance of information, virtually no extra layers of people and processes to get in each other's way, and a growingly sophisticated set of tools and automation, open-source contributors can collaborate efficiently at any time and in any location.

This asynchronous workforce model defies the conventional way practically unchanged from the First Industrial Revolution. It better embraces the Information Age trend, especially with the catalyst known as the internet. The model leads to realizations of how elaborate choices of where and when to work not only do not diminish productivity, but by respecting each others' time, life, and work style, we see less burnout and more innovations spark out.

The synchronous forms of communication do not simply vanish. They become more scarce and more treasured by each other. When participants resolve most motions asynchronously, the calls and meetings become laser-focused on the unresolved remainders, preserving all relevant parties' time and effort. Equally importantly, the in-person times serve a great socialization purpose to remind us that we are still humans.

### Creativity through Automation and Hacking

To sustain an asynchronous and decentralized workforce with a massive amount of information exposed through transparency, open-source participants frequently make and improve automation to optimize or abstract away processes. This mindset drives people to continually lookout for new ways and tools to adapt to their workflow and keep themselves fresh, efficient, and innovative.

But it is rare for existing tools and automation to provide a perfect fit for everyone's use-cases. People resort to hacking, or creative workarounds, to bend tools to their will.

The hacking culture is common in making open-source software itself, providing an organic counter-balance to some problems that plague many projects, such as under-documentation, lack of testing, and [leaky abstractions](https://en.wikipedia.org/wiki/Leaky_abstraction).

## git

Among many tools that support the open-source software ecosystem, `git` is the most popular one that provides efficient ways to distribute and manage source code. Its distributive nature allows every contributor to have full access to the working copy and the entire change history and derivatives.

The collaboration presents in a peer-to-peer fashion embracing the essence of decentralization. Collaborators branch out the source code to experiment and implement new features or issue fixes. Upon concluding the implementation, the contributor requests to merge back to the mainstream working copy of the source code, attract others to peer-review, and offer suggestions to improve. When enough contributors reach a G2M (good-to-merge) consensus, the implementation gets merged back to the mainstream. During this entire process, automation plays a critical role in simplifying every participant's experience through automated testing and code suggestions, so contributors do not waste too much time on common problems such as code-style differences and regression bugs. After the merge, it is common to see automated deployment or release of the software to a designated audience.

When unresolvable disagreements break out, one can _fork_ the project to evolve the software to another trajectory without impacting other collaborators. And when the opportunity comes, forks could also consolidate back to one. The practice of forking is why we have a diverse number of distributions of Linux operating systems (OS). For a similar reason, Android OS would not enjoy its fast development and evolution if it wasn't for a DVCS (distributed version control system) like `git`.

### GitHub (the company)

However, due to a barrier to converting from a centralized mindset to a decentralized one from its users, `git` was notoriously convoluted and hard to utilize. Toward the end of 2007, a group of software developers who enjoyed `git` but envisioned better ways to use it started a company to tackle these problems.

They started building what's known as GitHub today, which makes `git` usages a pleasant experience even for people who are not software developers. They created GitHub using `git` and GitHub itself, a practice known as [dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food).

What's fascinating about this company is that it started as profitable (or with a convincing model to be so) from day one, refrained from taking external funding until [July 2012](https://www.reuters.com/article/github-fundraising/github-raises-100-mln-from-andreessen-horowitz-idUSL2E8I9AV320120709), and stayed as a flat and fluid organization with 234+ employees until [17 July 2014](https://en.wikipedia.org/wiki/Timeline_of_GitHub).

Perhaps the root of the many fascinating factors of GitHub is due to their mindset and a culture that emphasizes [people's happiness, as opposed to money](https://tom.preston-werner.com/2010/10/18/optimize-for-happiness.html).

They leverage the learnings from open-source communities with tools they use (and build) to build toward simpler and better products, without conventional management methodologies and investors getting in their way. The mindset and culture reflect in their ability to [develop quality products and features](https://github.blog/changelog/) that embrace and encourage the best practices learned from open-source communities, benefit even those that are not open-source.

Their product development is self-initiated based on one's interest and passion. Quality assurance goes through peer-reviews and automation. Error-prone and inefficient manual processes, once identified, are automated away. They work entirely as a big open-source project. Not surprisingly, they are also a large contributor to various open-source software projects, with an adopted [Open Source (Almost) Everything](https://tom.preston-werner.com/2011/11/22/open-source-everything.html) mindset.

Such emphasis on people's happiness allows the company to attract top talents worldwide, and it reflects in their products to be enjoyed by their users. By 2010 (a little over three years since inception), GitHub has claimed to be the largest host of source code in the world until today.

## EQ Works (us)

The open-source social movement's key idea is to leverage the open-source communities' learnings to make information and curation more transparent. This social movement coincides with the phenomenon of the internet-driven information explosion and the increasing realization of how closed platforms could [manipulate the information's flow and shape and unethically profit from it](https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal).

As a part of the workspace meta shift, more organizations start to realize the benefits of open-source software and their community practices. Since around the beginning of 2014, our dev team has started to embrace and evolve based on open-source communities' learnings.

### Round-table wisdom

Instead of on-paper seniority, experimental merits become the only valid argument between project contributors in discussions and debates. We employ requests to code change (pull/merge requests) to demonstrate points in a verifiable way, rapidly iterate based on feedback, and make frequent releases with the help of peer-review and automation that capture rudimentary errors through various quality-assurance measures.

The practice allowed us to eliminate hierarchy and processes to boost productivity and innovation opportunities while maintaining a flat and fluid team. We free up conventional constraints to give everyone effortless ways to write, test, release software through available tools and automation that we build.

### Respect of (Others') Time

When information did not flow as freely and quickly as the era of the internet that we live and experience today, the conventional wisdom usually dictates that one should engage in a quick meeting/call with relevant parties to help with decision making. The efficiency of the traditional way to communicate is quickly diminishing in the era of information that we live and experience. In other words, such a form of communication would not scale.

The conventional hierarchal model, which requires grunt work to sift and curate information and report up, suffers a similar scalability problem.

The norm of today's internet is more opt-in based, such as subscribing to a mailing list, follow POTUS on social media, or join group chat channels of relevant subjects. These practices have been fundamentally reshaping how people interact with each other, and the impact is [more profound in younger and upcoming generations](https://www.forbes.com/sites/larryalton/2017/05/11/how-do-millennials-prefer-to-communicate/?sh=39d85bb06d6f).

The opt-in and asynchronous model of information consumption and working leads to more practical information sifting and an interesting new mindset of not expecting immediate responses. Or, in another way of looking at it, respect of others' time. The abundance of tools and services, combined with a hacking culture, gives us ways to automate away conventional chores and time-blocking events to direct our time and efforts for more valuable tasks.
