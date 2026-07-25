# 📦 其他研究 | 2026年07月26日

> 本类共 **271** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-271](./part-06.md)

---

### 201. [HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors](https://arxiv.org/abs/2607.21281)

**<font color=#1a73e8>作者：</font>** Siyu Li, Kunyu Peng, Di Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Topological maps are key outputs of autonomous driving perception systems, delivering essential road information for path planning. They identify instances such as centerlines and traffic signs, along with their connectivity relationships. Due to the lack of explicit markings for centerlines in real-world environments, the detection of centerline instances remains a significant challenge. To tackle this problem, we propose HGeo-TopoMap, which leverages an explicit prior map and implicit spatial relations to hierarchically boost topological mapping. First, a geometric adaptive learning module is designed for the road structure map obtained via inverse perspective mapping. This module discretely encodes semantic and spatial features from the map, followed by a prior-mask attention mechanism that selectively focuses on informative regions. Then, a geometric consistency learning module is devised, which leverages the geometric properties and spatial relationships of centerlines. Built on the geometry-aware decoder, it enforces spatial consistency by aligning features of centerline instances with identical geometric orientations. The proposed method is evaluated on the OpenLane-V2 dataset across the centerline, lane segment, and robustness benchmarks. Beyond substantial improvements in topological mapping accuracy, the proposed method offers the benefit of enhanced robustness, consistently outperforming baselines under both standard and challenging conditions. The source code and model weights will be made publicly available at this https URL.

---


### 202. [news-crawler-LM: A Small Long-Context Model For High-Quality News Crawling](https://arxiv.org/abs/2607.21284)

**<font color=#1a73e8>作者：</font>** Pascal Stolzenburg, Jonas Golde, Max Dallabetta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting structured content from news pages remains challenging due to heterogeneous HTML layouts, inconsistent markup, and substantial boilerplate such as navigation elements and advertisements. Rule-based news crawlers can achieve high extraction accuracy by encoding site-specific structure, but require manual configuration in order to generalize to new publishers. Large language models provide a more flexible alternative by reducing the need for handcrafted rules, but their high computational cost limits practical deployment. In this paper, we introduce news-crawler-LM, a small long-context language model fine-tuned on high-quality, human-validated extractions from the Fundus news-crawling library. Our model converts raw HTML into plaintext and structured JSON, including fields such as headline, author, publication date, and article body. In our experiments, news-crawler-LM outperforms strong baselines in HTML-to-Markdown and HTML-to-JSON extraction, improving performance by +4.8 BLEU and +6.1 METEOR in the HTML-to-Markdown task, and by +2.2 BLEU and +4.1 METEOR in the HTML-to-JSON task. However, we also observe that our model only slightly better compared to other rule-based parsing libraries on the HTML-to-plaintext task in evaluations on previously unseen publishers. We release all models and artifacts to the research community.

---


### 203. [Reimagining the Augmented Reality Accessibility Ecosystem for Deaf Students: Service Provider Perspectives in Experiential Learning](https://arxiv.org/abs/2607.21289)

**<font color=#1a73e8>作者：</font>** Roshan Mathew, Roshan Peiris  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In experiential learning environments, Deaf and hard of hearing (DHH) students often experience ``split attention,'' dividing their focus among tasks, instructors, and access providers. Augmented reality (AR) has been proposed as a means to centralize communication access within the student's field of view; however, little is known about how such systems affect the instructors, interpreters, and captioners who support access in these settings. We present a formative, expert-based evaluation of ARRAE, an AR-mediated communication access ecosystem, examining the experiences of an instructor, an American Sign Language (ASL) interpreter, and a real-time captioner in a simulated laboratory environment. Comparing in-person, traditional remote, and AR-mediated access, our findings suggest that AR reconfigures accessibility labor and interactional practices by redistributing communication, attention, and awareness across participants. While AR-mediated access supported integrated, in-situ communication and enhanced contextual awareness, it also altered interactional feedback mechanisms, such as gaze coordination and pacing, that support shared understanding during instruction. These observations highlight trade-offs between access, control, and coordination, and suggest that AR-mediated systems may be most effective when considered as part of a broader, hybrid ecosystem rather than as standalone replacements for existing modalities. This work contributes initial insights into how AR reshapes communication access in experiential learning and informs the design of systems that support coordinated, multi-user interaction in hands-on educational contexts.

---


### 204. [Multi-Task Learning for Heterogeneous Prediction from Video Game State with Transfer Learning](https://arxiv.org/abs/2607.21290)

**<font color=#1a73e8>作者：</font>** Jonas Peché, Aliaksei Tsishurou, Alexander Zap 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task learning (MTL) is a promising approach for prediction tasks derived from video game state data, as modern game telemetry provides multiple related supervision signals from the same structured observations. We study whether a shared model trained jointly across tasks in team-based multiplayer games can improve generalization while reducing training and inference cost compared to specialized single-task models. We adapt a multimodal architecture for endpoint prediction to a general multi-task setting that combines rasterized vision inputs, global match context, and per-unit state information through an image encoder and attention-based interaction modeling. Experiments on a large proprietary World of Tanks dataset compare single-task and multi-task training, evaluate weighting strategies for mixed losses and conflicting gradients, and test pre-training/fine-tuning under limited target-data regimes. We also examine within-game transfer across game maps under structured environment shift.

---


### 205. [Expert Behavior Prior Reinforcement Learning](https://arxiv.org/abs/2607.21302)

**<font color=#1a73e8>作者：</font>** Gong Gao, Weidong Zhao, Xianhui Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavior prior reinforcement learning (BPRL) has emerged as a promising paradigm to improve sample efficiency in online reinforcement learning (RL) by leveraging policy priors derived from offline demonstrations. However, most existing BPRL methods rely on static offline datasets, which often suffer from low data diversity and suboptimal trajectory quality. This reliance restricts the effectiveness of policy priors, hindering both policy exploitation and stability during online training. Consequently, agents are prone to inefficient exploration and unstable learning dynamics. To address these limitations, we deviate from existing offline pre-training methods and propose an Expert Behavior Prior (EBP) algorithm. Specifically, we introduce a Q-guided conditional variational autoencoder (Q-CVAE) that learns to generate expert policy priors directly from the online replay buffer. This enables the generation of high-value actions for guiding policy updates without relying on pre-collected expert trajectories. To further enhance policy exploitation, we propose an expert policy guidance (EPG) mechanism that selects expert actions from a generative support set, and we integrate a policy gradient correction (PGC) module to harmonize Q-guidance with expert supervision, promoting stable and consistent policy improvement. Extensive experiments conducted on robotic control (Gym, PyBullet) and industrial control (DMControl) benchmarks demonstrate that EBP significantly outperforms state-of-the-art online RL algorithms, achieving higher sample efficiency and more stable convergence.

---


### 206. [AI Assistants Overassist](https://arxiv.org/abs/2607.21306)

**<font color=#1a73e8>作者：</font>** Verona Teo, Raghav Jain, Tobias Gerstenberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as tutors and thought partners, helping users reason through problems. While guidance from AI assistants can scaffold thinking and foster learning, such benefits depend on how they help--for instance, intervening too early or too frequently may hinder true learning and cognitive engagement. Yet how AI systems navigate intervention decisions during problem-solving remains poorly understood. Here, we introduce Int-Bench, a simulation-based benchmark for evaluating LLM interventions during learning. Int-Bench simulates a "student" solving a problem while a "teacher" monitors the student's reasoning and decides whether, when, and how to intervene. Across three domains--code debugging, mathematics, and brain teasers--we evaluate LLM teachers on the frequency and timing of interventions, as well as their impact on both immediate task success and generalization to new problems. We also compare LLMs to humans, finding that LLMs intervene more frequently and earlier than humans. Moreover, in contrast to humans, they tend to provide complete solutions rather than targeted hints. These findings suggest that current LLM assistants often optimize for short-term success rather than supporting the reasoning processes needed for deeper learning and long-term success.

---


### 207. [PC-Edit: Prompt-Contrastive Region Discovery and Region-Guided Editing](https://arxiv.org/abs/2607.21318)

**<font color=#1a73e8>作者：</font>** Jian Zhang, Zhijun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Replacing an object with one that differs in category or shape requires complete source removal, natural target formation unconstrained by the source silhouette, and preservation of unrelated content. Existing training-free editors either localize edits from terminal predictions under source and target prompts or preserve unrelated content through spatially unselective source-feature reuse without explicit region discovery. Before reaching the terminal predictions, prompt-induced semantic differences undergo additional network transformations that may obscure their spatial localization, reducing localization precision. Spatially unselective feature reuse forces a trade-off between edit completeness and background preservation. Therefore, we propose PC-Edit, a prompt-contrastive framework for training-free MM-DiT editing. PC-Edit contrasts the image-token attention outputs under the source and target prompts, capturing prompt-induced semantic differences directly where text-conditioned information is delivered to image tokens. The same contrast identifies a source-erasure region during inversion and a target-emergence region during denoising. Their union suppresses source remnants while allowing the target object to form naturally. PC-Edit further couples region discovery and background preservation within each sampling step by estimating the current edit region from preceding attention blocks and immediately injecting cached source K/V features outside it in subsequent blocks, thereby protecting unrelated content before the latent update. Experiments on PIE-Bench and our EditRegion-Bench, with human-verified edit-region annotations for single- and multi-object addition and replacement, show that PC-Edit achieves the best editing quality and background preservation among methods without user-specified edit regions.

---


### 208. [Toward cryptographically verifiable authorization for autonomous AI agents: A security hypothesis, preliminary formal model, and proof-of-concept implementation](https://arxiv.org/abs/2607.21325)

**<font color=#1a73e8>作者：</font>** M. Llambí-Morillas, D. Fernández-Fernández  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents increasingly execute actions, invoke tools, and operate on protected resources with limited human oversight. Existing authentication and authorization mechanisms establish identity and delegate authority, but do not inherently provide cryptographic evidence that a concrete request issued by a specific agent satisfies the applicable policy in a specific execution context. This paper hypothesizes that agent authorization can be formalized as a cryptographically verifiable relation, denoted $R_{CVA}$, that jointly binds an agent principal, a concrete authorization request, an execution context, and the satisfaction of an applicable policy, while selectively preserving the confidentiality of private authorization attributes. We introduce a preliminary formal abstraction for Cryptographically Verifiable Agent Authorization (CVA), define a compact set of candidate security properties including authorization soundness, principal binding, request binding, policy binding, and replay resistance, and provide an executable zero-knowledge proof of concept that instantiates selected elements of the model over a Groth16 zk-SNARK construction. We further identify and formalize the structural separation among identity binding, authorization-request binding, and runtime execution binding as a central open problem in the design of secure agentic systems (a distinction {not explicitly addressed by} current agentic security frameworks) and present a falsifiable research agenda for its resolution.

---


### 209. [SlerpFlow: Spherical Trajectory Correction for Rectified Flow Inversion](https://arxiv.org/abs/2607.21326)

**<font color=#1a73e8>作者：</font>** Wenbin Duan, Yan Shu, Zhuoyuan Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rectified-flow-based diffusion transformers, particularly FLUX, have demonstrated outstanding performance in high-quality image generation. However, achieving fast and accurate inversion--transforming images back to latent noise for faithful reconstruction and editing--remains a challenging bottleneck due to the discretization errors of linear solvers. This paper introduces SlerpFlow, a straightforward yet highly effective zero-shot approach that unlocks the full potential of FLUX for high-fidelity inversion and editing. Unlike existing approaches (e.g., RF-Solver) that rely on complex numerical approximations such as high-order Taylor expansions to correct trajectory errors, we present a geometric view based on the Manifold Hypothesis: the empirically observed trajectory curvature is not a numerical artifact, but rather serves as a necessary "centripetal force" that constrains the flow to remain on the data manifold. Guided by this insight, SlerpFlow integrates Spherical Linear Interpolation (Slerp) to rectify flow velocity directions on the hypersphere, strictly adhering to the intrinsic curvature of the latent space. Crucially, by caching the corrected velocity for subsequent steps, SlerpFlow achieves high-precision inversion while maintaining the computational efficiency of a first-order Euler solver. Extensive experiments on FLUX-based reconstruction and editing tasks demonstrate that SlerpFlow improves reconstruction fidelity and achieves stronger semantic alignment in editing without requiring additional training. Code is available at this https URL.

---


### 210. [Gradient Concentration, Not Weight Saliency, Explains Representation-Level Class Unlearning](https://arxiv.org/abs/2607.21353)

**<font color=#1a73e8>作者：</font>** Billel Habbati, Alessio Merlo, Luca Verderame 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the influence of specific training data while preserving model utility. Many state-of-the-art approaches pursue this goal by restricting the forgetting update to a subset of parameters selected through gradient-based saliency. Although such methods are widely adopted, the actual contribution of saliency-based weight selection to representation-level forgetting remains unclear. In this work, we perform the first controlled ablation of the saliency masking mechanism used by SalUn. Using a matched-compute experimental design on CIFAR-10 and CIFAR-100 with ResNet-18, we compare saliency-based masking against random masks of equal sparsity and unconstrained updates, while keeping the unlearning objective, optimization schedule, and computational budget fixed. Across multiple representation-level evaluations, including linear probing, prototype recovery, and layer-wise CKA, the three configurations exhibit statistically equivalent representation-level recoverability. We find that forget gradients are strongly concentrated in the final network layers (approximately 92% of the squared gradient energy on CIFAR-10) before any mask is applied, causing all masking strategies to operate within the same representational subspace. Furthermore, saliency masks show limited class specificity (specificity index 0.09-0.11), selecting highly overlapping parameter subsets across different forget classes. Our findings suggest that, in the studied setting, representation-level forgetting is primarily governed by gradient concentration and representation geometry rather than by the specific identity of saliency-selected weights. More broadly, the results support a growing body of evidence indicating that effective representation-level unlearning requires objectives that act directly on latent representations rather than on increasingly sophisticated weight-selection strategies.

---


### 211. [SPORD: A Simulation-Propose-then-OR-Dispose Approach for Supply Chain Planning](https://arxiv.org/abs/2607.21354)

**<font color=#1a73e8>作者：</font>** Jiayin He, Yutong Pan, Sen Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For years, supply chain planning at e-commerce firms has operated as a collection of isolated projects. Each planning task from static network planning to dynamic warehouse assortment planning requires analysts to spend weeks building models from scratch, calibrating and persuading executives to act on outputs they cannot verify. Three barriers drive this: bespoke models proliferate because standardization is difficult (operational fragmentation); once unified, the combinatorial scale of millions of SKUs, thousands of nodes, and intricate routing logic exceeds what solvers can handle within a tight window (computational intractability); and a mathematically optimal solution still fails to be implemented if the executives do not trust it (implementation hurdle). To bridge this gap, we propose and implement the Simulation-Propose-then-OR-Dispose method, deployed as this http URL's NetSim platform. The central insight is decoupling: simulation proposes by generating and evaluating the full set of operationally valid candidate paths-absorbing all idiosyncratic business logic, while an integer program disposes by selecting the globally optimal subset. Computationally, matrix-vectorized CPU/GPU accelerated simulation achieves a 10-100 times speedup over serial methods, and a list scheduling algorithm reduces coupled-order processing from hours to minutes. Operationally, we establish a closed loop via an intelligent diagnosis engine. Since 2025, NetSim has optimized end to-end services for over 20,000 suppliers, the cross-regional fulfillment rate dropped from 6.1% to 4.9%, and the average monthly carbon reduction is approximately 5,745 tCO2e. SPORD moves simulation from monitoring to active planning. The transparent outputs turn skeptical executives into engaged collaborators, and the modular architecture ensures that the next planning requires just configuration, not reconstruction.

---


### 212. [Hilbert Operator for Progressive Encoding (HOPE): A Mathematical Framework for Deconstructing Learned Representations in Deep Networks](https://arxiv.org/abs/2607.21366)

**<font color=#1a73e8>作者：</font>** Hossein Mobahi, Peter L. Bartlett  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks encode complex representations, but deconstructing this internal knowledge remains a challenge. Given the link between learning and compression, network compression offers a promising lens to analyze this knowledge. However, standard compression heuristics often suffer from scale symmetries and architectural biases. To resolve these, we introduce Hilbert Operator for Progressive Encoding (HOPE), a mathematical framework to gradually deconstruct the representations in trained network weights.
HOPE shifts network compression from the discrete domain into a Hilbert space of continuous functions. By modeling individual neurons as rank-1 Hilbert-Schmidt operators, HOPE unifies pruning and neuron merging as low-rank subspace projection. Extending this formulation, HOPE introduces macro block eviction to encompass multi-layer structures like entire residual pathways under the same unified metric. This unified approach enables unbiased architectural decisions across layers with different types and sizes. HOPE is a data-free and hyperparameter-free framework. We present proof-of-concept experiments in model compression and fine-tuning to highlight the practical potential of our theory.

---


### 213. [Incremental Optimal Assignment for Real-Time Crowd Tracking](https://arxiv.org/abs/2607.21368)

**<font color=#1a73e8>作者：</font>** Ismail H. Toroslu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking in dense crowds requires solving a bipartite assignment problem between detections and trajectories at every video frame. The classical Hungarian algorithm solves this in $O(N^3)$ time, which becomes a bottleneck for large scenes with hundreds of people. We propose an \emph{incremental} assignment algorithm that exploits the block-sparse structure of crowd tracking cost matrices --- dense within each crowd cluster, near-zero between clusters. We compute the exact same optimal $N \times N$ assignment as the Hungarian algorithm, but via an incremental strategy: we add one person at a time, exploiting the fact that after step $n-1$ the dual potentials are \emph{exactly optimal} for the $(n-1)\times(n-1)$ subproblem --- a strictly stronger condition than the intermediate feasibility maintained by the Hungarian algorithm during its $N$ outer iterations. Each new step therefore requires only a single augmenting path search from a certified optimal starting point. This avoids repeated full-matrix scans while guaranteeing an identical globally optimal result. A diagonal-reordering invariant keeps the data structure compact and cache-friendly. On realistic crowd benchmarks with $N \in [200, 5000]$ people organised into dense clusters, our algorithm achieves \textbf{3.7--6.5$\times$ speedup} over the Hungarian baseline while producing provably optimal matchings identical to those of Hungarian. The speedup grows with $N$ and remains stable beyond $N=3000$, making the method especially attractive for large-scale crowd scenes such as stadium exits and mass public events.

---


### 214. [Mean-to-Score Discrete Diffusion: Posterior-Mean Denoisers for Score Entropy](https://arxiv.org/abs/2607.21372)

**<font color=#1a73e8>作者：</font>** Jingyuan Li, Xiaoyi Jiang, Yixuan Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score Entropy Discrete Diffusion (SEDD) parameterizes discrete reverse processes with unconstrained positive score ratios. While positivity guarantees nonnegative reverse jump rates, it does not ensure Bayes realizability: ratios at a noisy state need not be jointly induced by any clean-token posterior under the forward kernel. The score-entropy loss has the correct population optimum but does not enforce this constraint away from it. In a trained pure-uniform SEDD checkpoint, roughly one quarter of complete score vectors violate the coordinate box, while more than half lie inside it yet remain materially incompatible with any valid posterior. Such violations can produce negative pre-normalization weights in finite-step sampling. Projecting raw scores onto the bridge polytope removes all observed negative weights and improves external generative PPL from $203.6$ to $175.1$ without changing the sampler. We introduce \emph{mean-to-score} (M2S), which predicts a clean-token posterior mean and converts it to the score through an exact kernel-dependent linear map. The construction applies to any known coordinate-wise continuous-time Markov chain (CTMC) satisfying a mild support condition. For uniform corruption, it maps the probability simplex onto the bridge polytope; for absorbing-mask corruption, the resulting objective recovers MD4 exactly. In a controlled 28.4M-parameter CIFAR-10 comparison, M2S lowers test BPD from $3.173$ to $3.129$ and FID-50k from $\CifarSEDDFID$ to $\CifarMtwoSFID$. A 170M-parameter M2S model trained on about 262B OpenWebText token slots outperforms the evaluated pure-uniform SEDD, GIDD, and Neural CTMC checkpoints at every tested sampling budget, reaching generative PPL $143.3$ at 128 steps versus $183.6$ for the strongest pure-uniform baseline.

---


### 215. [Towards Faithful Graph Explanations with Synergistic Edge Effects via Granular Balls](https://arxiv.org/abs/2607.21381)

**<font color=#1a73e8>作者：</font>** Jiancu Chen, Shuyin Xia, Guan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instance-level explanations aim to reveal the rationale behind a model's decisions for a specific graph. Previous methods explain graph neural networks (GNNs) by selecting important edges to induce subgraphs, where edge importance is assessed by perturbing each edge and observing changes in the model predictions. However, they often neglect the synergistic effects among edges, which are crucial for accurately characterizing edge importance. To address this issue, we propose SeeExplainer, a parameter-free explainer to interpret GNNs. Specifically, we first introduce a granular-ball graph refinement mechanism that decomposes a graph into several disjoint granular-balls with no fixed size, and utilize them as nodes to construct a structural graph. This process can better capture the synergistic effects among edges. Then, we perturb nodes and edges in the structural graph to generate explanatory subgraphs based on their respective contributions. Experiments on several graph classification datasets of different networks show that SeeExplainer outperforms state-of-the-art baselines.

---


### 216. [Word meaning co-determines vowel-inherent spectral change. A corpus-based investigation of conversational Mandarin](https://arxiv.org/abs/2607.21391)

**<font color=#1a73e8>作者：</font>** Xiaoyun Jin, Mirjam Ernestus, R. Harald Baayen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates vowel-inherent spectral change (VISC) in spontaneous conversational Mandarin. Using the generalized additive model and word embeddings from distributional semantics, we show that, when controlling for variables such as vowel duration, gender, speaker identity, co-articulation, vowel identity, and utterance position, vowel formant trajectory dynamics have word-specific components that are tied to their meaning in context: The F1 and F2 trajectories of words can be predicted from their contextualized embeddings with an accuracy that substantially exceeds a permutation baseline. Challenging modular cognitive models of speech production, these results indicate that, words' semantics co-determine the fine details of their articulation.

---


### 217. [CRAFT: Exploring Wearable Creative AI on Smart Glasses for Fiction Writing in Real-World Contexts](https://arxiv.org/abs/2607.21394)

**<font color=#1a73e8>作者：</font>** Runze Cai, Yuxuan Huang, Lin-Ping Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creative writing increasingly integrates AI assistance, yet current tools miss in-situ moments when writers draw inspiration from real-world experiences. We envision Context-aware Reality-Fiction Transformation (CRAFT), an approach for AI glasses that translates daily experiences into fiction narratives. We explored its desirability, feasibility, and potential viability through three studies. Interviews with nine writers yielded desires and three design goals: 1) augmenting in-situ perception to bridge reality-fiction gaps, 2) promoting authenticity grounded in real-world experiences while maintaining fictionalization, and 3) preserving creative agency, enjoyment, and life-art boundaries. Co-design workshops with 16 writers and researchers operationalized these goals into concrete interaction mechanisms using a technology probe. We then conducted supported field trials with eight writers across 24 sessions using a refined probe, revealing writer-perceived benefits (e.g., enriched fictional ideas from serendipitous encounters), emergent practices (e.g., micro-creation), and design considerations for future sustained use. We contribute design explorations for the CRAFT approach, offering design implications and empirical insights on ubiquitous human-AI creative collaboration in everyday life.

---


### 218. [When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard: A Fast Vision-Language Guard for Real-Time Moderation](https://arxiv.org/abs/2607.21401)

**<font color=#1a73e8>作者：</font>** Dongbin Na  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A vision-language AI assistant returns its answer as a stream of generated tokens. Therefore, a safety guard that watches that answer has to keep up with the stream and stop a harmful reply before a user reads it. Recent vision-language guardrails instead generate a chain of thought before they issue a verdict. They believe that step-by-step reasoning yields a safer guard. This design makes the guard heavy and slow, since the model must decode many tokens for harmfulness detection. We pose the question of whether a vision-language guard really needs to reason in order to screen a response. We answer with a guard that has no chain. ResponseGuard reads a harmful verdict from a single pooled representation of the request, the response, and the image in one forward pass. Across a standard multimodal guardrail benchmark, our 2B ResponseGuard outperforms a recent 3B reasoning-based vision-language guard on response harmfulness detection, without any reasoning and at about 150 times lower time cost. On request harmfulness the reasoning guard retains an overall lead, and the remaining gap on both tracks sits on the image-only cells. We observe that the gap may stem from the frozen vision encoders that both designs use rather than from the missing chain. We have also found the reasoning guard directs almost none of its verdict attention to the image. Based on a single-pass detection, ResponseGuard can screen an answer sentence by sentence as it streams and stop a harmful answer before it finishes. For guarding the response of a vision-language model, a calibrated single-pass label may provide a sufficient safety signal. We fully release all source code, trained models, and datasets at this https URL.

---


### 219. [A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention](https://arxiv.org/abs/2607.21403)

**<font color=#1a73e8>作者：</font>** Ziping Xu, Yuyi Chang, Chenshun Ni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile-health interventions increasingly use online learning and decision making algorithms to personalize when to nudge users toward healthier behavior, but a poorly designed algorithm can burden and disengage participants. New algorithm design decisions should therefore be vetted against realistic simulated users before each real-life deployment. We propose a method to develop ``JITAI-Twins'': digital twins of a target subpopulation for comparing candidate online algorithms before a just-in-time adaptive intervention (JITAI) deployment. The method builds on a conditional time-series diffusion model that is temporally consistent (future actions do not affect the generated past), and it supports repeated updating from three sources of information, in three steps: pre-training on a large observational dataset, fine-tuning on small prior intervention deployments in related populations, and inference-time calibration to the next target population from domain-scientist expertise. We validate the twin at each pre-deployment stage of the long-running HeartSteps series (v2 through v4) of physical-activity suggestion intervention deployments, treating each successive deployment as an upcoming study. The proposed method reproduces the target subpopulation's temporal and between-participant structure better than simpler simulators. These results suggest that our twin can be used to simulate a target deployment before it runs, the prerequisite for testing and informing online algorithm design decisions.

---


### 220. [MemTools: A Unified Research Framework for Interoperable Agent Memory](https://arxiv.org/abs/2607.21404)

**<font color=#1a73e8>作者：</font>** Chengfeng Zhao, Jinhui Chen, Sirui Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While memory systems are essential for agent architectures, pervasive architectural fragmentation restricts systematic research. Existing implementations typically couple different stages of the memory lifecycle, entangle evaluation logic with specific datasets, and provide limited support for the management of heterogeneous memory types. We introduce MemTools, an interoperability research framework that decouples memory system components from their underlying deployment environments. MemTools standardizes the memory lifecycle through declarative data contracts, enabling the interchangeable assembly of components across different systems. It orthogonally separates benchmark datasets from execution protocols to facilitate controlled assessments. Furthermore, MemTools provides a unified computational interface for coordinating symbolic, neural, and multimodal memory representations within a shared runtime. Empirical evaluations on cross-system component integration, evaluation protocol reconfiguration, and heterogeneous memory coordination demonstrate that MemTools enables systematic isolation and analysis of memory design variables. These findings suggest that MemTools provides a practical and extensible infrastructure for advancing principled research on agent memory.

---


### 221. [Anti-Periodic Positional Encoding: Möbius Boundary Conditions Make In-Context Retrieval Reliable](https://arxiv.org/abs/2607.21405)

**<font color=#1a73e8>作者：</font>** Ji Ho Bae  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Möbius RoPE is a rotary positional encoding built on the anti-periodic frequency ladder $\theta_i=\pi(2i+1)/N$: every rotation plane advances by an odd multiple of $\pi$ across the training context, so the positional holonomy is $-1$ and the two ends of the sequence are deterministically coupled through a closed-form Dirichlet "dipole"; to our knowledge this is the first anti-periodic boundary condition in positional encoding. We verify the theory numerically to $\sim 10^{-6}$ and pretrain 48 models spanning six 160M-class and three 410M-class arms (2B FineWeb-Edu tokens each; the hybrid arm puts Möbius frequencies on 25% of heads). Hybrid perplexity is unchanged (29.66 vs. 29.72), but needle-in-a-haystack retrieval becomes reliable: $90.3\pm5.7\%$ versus $63.3\pm31.4\%$ at context 512 ($n=6$ seeds), observed worst seed 86% versus 14%, robust variance tests $p=0.013$-$0.029$ (unadjusted), recurring at 410M (Levene $p=0.040$). Matched controls isolate the mechanism: an aperiodic ladder in the same frequency band reproduces none of the effect, and a periodic (holonomy $+1$) ladder only a fraction. Swapping trained models' frequency table back to standard RoPE (weights frozen) collapses retrieval, with damage concentrated on far needles: trained models depend on this long-range geometry. A NoPE arm is even more reliable at short context but pays a 13% perplexity tax and extrapolates worst; only the anti-periodic hybrid pairs baseline perplexity with a high reliability floor. The effect is scoped to single-needle retrieval within the training window; a one-line frequency swap thus provides zero-cost insurance against the retrieval seed lottery.

---


### 222. [Themis Consensus Extension v1: MEV Mitigation by Randomized Delayed Execution and Intent-Hiding Transactions in Application-Specific Blockchains](https://arxiv.org/abs/2607.21406)

**<font color=#1a73e8>作者：</font>** Shoeb Siddiqui, Mateusz Nowakowski, Stanislav Vozarik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Maximal extractable value (MEV) arises when privileged participants select, exclude, insert, or reorder pending transactions for private gain. We specify and analyze the Themis Consensus Extension v1, first published by Mangata in 2021. The design separates value extraction by reordering (VER) from value extraction by denial (VED). For VER, block construction and execution occur across consecutive producers: one producer commits a transaction set, and the next derives a publicly verifiable, deterministic, previously un- predictable seed and executes a seed-determined, dependency-preserving permutation. For selective VED, a user may encrypt a transaction for a designated builder and executor. The builder removes an outer layer and commits the opaque inner ciphertext; the executor reveals and executes the plaintext only after commitment. Under selfish but non-colluding validators, an adversary below the underlying consensus fault threshold, secure cryptography, and accountable role performance, the construction limits unilateral post-commit ordering control and hides transaction intent from relays and the builder. It does not provide send-order or receive-order fairness, complete censorship resistance, resistance to builder-executor collusion, or per-transaction price guarantees. We analyze probabilistic extraction, spam, dependent transactions, decryption liveness, session boundaries, total denial, and threshold coalitions. We also document the initial Aura-based Substrate implementation and its subsequent transition to a BABE-based sr25519/VRF seed path, together with delayed execution, Fisher-Yates shuffling, and Xoshiro256++. The result preserves the original proposal while narrowing its claims to explicit assumptions.

---


### 223. [Logical Regression for Planning with Axioms](https://arxiv.org/abs/2607.21414)

**<font color=#1a73e8>作者：</font>** Connor Little, Christian Muise  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In automated planning, logical regression is an operation that returns the most general condition necessary for an action to achieve a particular formula. It has many applications, such as allowing for more robust plan execution and providing compact policies for non-deterministic planning. Although relatively simple to calculate in basic planning settings, logical regression becomes significantly more complex when additional factors, such as axioms, are present. We introduce a methodology for approximating the logical regression of an action in a domain that includes axioms; an approximation that limits conditions to partial states. Our method produces minimal partial states while avoiding the recalculation of axioms. To demonstrate the impact of our methods, we embed our form of regression in an execution monitoring context, a well-established setting that can benefit greatly from logical regression. Our results show that this form of regression can dramatically generalize partial states across multiple domains, reducing the number of variables considered for execution monitoring by up to 70%, and demonstrate that the resulting execution monitor is robust enough to recover frequently in an environment with unexpected changes: several domains recover over 50% of the time in our tests.

---


### 224. [Towards Privacy-Preserving Federated Prompt Tuning under Data Heterogeneity: A Subspace-Decomposed Expert Approach](https://arxiv.org/abs/2607.21417)

**<font color=#1a73e8>作者：</font>** Yuhua Wang, Xiaodong Li, Yihao Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated prompt tuning (FPT) enables collaborative adaptation of vision--language models (VLMs) using lightweight prompts. Existing methods often address heterogeneity and privacy through a split-prompt design under local differential privacy (DP), combining a shared prompt for global transfer with private prompts for local adaptation. However, a single shared prompt may over-smooth diverse transferable knowledge, weakening the balance between personalization and generalization. Multi-expert prompts (MEPs) can better capture this diversity, but enlarge the communicated space, increasing DP noise and communication cost while making robust expert composition more difficult. We propose FedSEPT, a privacy-preserving Fed}erated Subspace-decomposed Expert Prompt Tuning. Specifically, we employ Subspace-decomposed Expert Modeling (SEM) to parameterize multiple prompt experts with shared low-rank factors, a fixed public basis, and private residuals, thereby confining communication and DP perturbation to a compact factor space while enabling direct server aggregation in a common coordinate system. We further design Instance-aware Expert Fusion (IEF), which adaptively combines semantically complementary experts via on-device routing and performs efficient logit-level fusion using cached expert-specific text features. Extensive experiments on 11 heterogeneous benchmarks show that, under the same privacy constraints, FedSEPT achieves a better trade-off between local adaptation and global generalization than strong baselines.

---


### 225. [Bridging the Gap Between Plausibility and Admissibility: Constraint-Aware Flow Maps for Dynamic Graph Systems](https://arxiv.org/abs/2607.21421)

**<font color=#1a73e8>作者：</font>** Michael Romei de Socio, Gian Luca Pozzato, Alessio Merlo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models can support decision-making under uncertainty by producing ensembles of plausible future system trajectories, but statistical plausibility does not ensure structural feasibility. This study investigates whether post-sampling symbolic constraints can improve the reliability of generative trajectory modeling in dynamic graph-structured systems. A conditional diffusion model generates future graph-state trajectories from partial observations, while an external symbolic layer applies hard filtering, soft weighting, or projection-based repair. The framework is evaluated on two controlled synthetic regimes: a compact graph and a medium-complexity dependency graph, using metrics for structural validity, sample efficiency, diversity, robustness, and calibration. In the compact regime, the model produces an invalid probability mass of 0.002996, indicating an almost entirely admissible trajectory manifold. Under the same architecture and training protocol, invalid mass increases to 0.155929 in the medium-complexity regime. Hard filtering removes all invalid retained trajectories while preserving 84.4% of generated samples, whereas soft weighting preserves effective sample size but yields only limited validity gains. Family-level analysis shows that dependency constraints account for nearly all observed inadmissibility. These results indicate that statistical plausibility and structural admissibility are distinct reliability properties and that symbolic constraint handling becomes more valuable as graph-structural complexity increases.

---


### 226. [Semantic-Aware Task Clustering for Constructive and Cooperative Multi-Tasking](https://arxiv.org/abs/2607.21426)

**<font color=#1a73e8>作者：</font>** Ahmad Halimi Razlighi, Maximilian H. V. Tillmann, Edgar Beck 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-task semantic communication (CMT-SemCom) improves task execution performance by leveraging shared representations. However, as we demonstrated in [1], cooperative multi-tasking can be either constructive or destructive, depending on the semantic relationships among tasks. To ensure constructive cooperation, we propose a semantic-aware task clustering method for CMT-SemCom. We have formulated a sequential multi-stage optimization problem in which semantically aligned tasks are clustered once after a short initial training phase, and then end-to-end (E2E) joint training is conducted exclusively within the discovered groups. Specifically, the problem decomposes into two stages: (i) a semantic clustering problem leveraging hierarchical density-based spatial clustering, and (ii) an intra-cluster E2E CMT-SemCom learning problem. Simulation results demonstrate that the proposed framework effectively mitigates destructive cooperation and negative transfer, yielding accuracy gains compared to unclustered multi-tasking and individual training baselines.

---


### 227. [Context-weighted Discrete Flow Matching](https://arxiv.org/abs/2607.21427)

**<font color=#1a73e8>作者：</font>** Daniil Cherniavskii, Daniel Severo, Karen Ullrich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete flow matching provides a flexible framework for generative modeling on discrete structures. However, the standard factorized training objective exposes the model to targets of varying difficulty, mixing well-conditioned, predictable tokens with ambiguous, high-entropy ones. We empirically demonstrate that the uncertainty over the value of each token is closely related to the density of available context in its neighborhood. Motivated by this observation, we propose a simple modification to the underlying continuous-time Markov chain (CTMC) that incorporates local context information. Our context-weighted sampler improves generation quality with negligible computational overhead, while our scaled cross-entropy loss function reweights the training signal from different tokens and reduces generative perplexity by up to 63% on OpenWebText. Moreover, our approach matches a strong semi-autoregressive block diffusion baseline in quality while retaining the ability to perform generation in any order. These results highlight the role of local context as an important factor in discrete generative modeling and show that simple context-aware modifications can significantly improve both sampling and training efficiency.

---


### 228. [Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models](https://arxiv.org/abs/2607.21433)

**<font color=#1a73e8>作者：</font>** Renuka Oladri, Niveda Jawahar, Abdirisak Mohamed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought reasoning models such as DeepSeek-R1-Distill-Qwen-7B exhibit a bimodal convergence pattern: generations either terminate within a token budget (converged) or exhaust it without reaching a conclusion (non-converged). We characterize this phenomenon empirically, showing that converged generations achieve 90.3% accuracy on AIME 1983-2024 while non-converged ones achieve only 6.6%, with an overall convergence rate of 62.0%. We then ask whether this outcome is detectable early in the thinking chain using internal model representations. Training linear probes on hidden-state activations at token positions 50-300, we find that layer-20 activations at token 150 achieve AUC 0.608 (+-0.080, 5-fold CV), reliably above chance even at token 50. Activation probes consistently outperform behavioral baselines derived from token entropy and repetition statistics. A sweep-level permutation test yields p=0.063 (100,000 permutations), consistent with a modest signal that our sample size cannot confirm at conventional thresholds. These findings suggest that convergence fate is partially encoded in intermediate representations well before the generation ends, opening a path toward early-exit inference and adaptive compute allocation.

---


### 229. [Adaptive Identity Anchoring: Closed-Loop Keyframe Placement for Synthetic Paired Supervision in Video Face Swapping](https://arxiv.org/abs/2607.21434)

**<font color=#1a73e8>作者：</font>** Logan Robbins  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video face swapping has no natural paired supervision: no real footage exists of one person's face performing another person's video. The strongest current answer, DreamID-V's SyncID-Pipe, mints pairs by replacing the identity in exactly two frames of a real clip -- the first and the last -- and regenerating the rest from a pose sequence alone. Pose carries no appearance evidence of the swapped-in identity, so over long clips, occlusions, and extreme pose excursions the synthesized identity has a long unanchored span on which to drift; no published ablation examines anchor count or placement. We propose Adaptive Identity Anchoring (AIA): (i) generalize the synthesizer to arbitrary anchor sets, architecturally natural for diffusion-forcing-style transformers where conditioning on a frame is clamping its tokens to zero noise; (ii) place anchors by a closed feedback loop that scores every generated frame against the real reference identity and inserts an image-face-swapped anchor at the worst-scoring frame until the pair passes a threshold or exhausts a budget; (iii) reuse the loop's verdict as an automatic data filter. A second pathology, the beauty-filter look of over-smoothed skin, has the same root cause: micro-texture, like identity, is priced by none of the pipeline's objectives. We therefore pair AIA with Reality-Referenced Texture Restoration: matched re-graining from each real frame's non-face regions, band-split transfer of sub-identity micro-texture from the real footage, and a second, spectral acceptance channel refereed by the footage's own spectrum. Identity-anchor density, we argue, is a controllable quality dial, and we specify falsifiable experiments -- drift-versus-gap curves, uniform-versus-adaptive placement at matched budgets, student training on AIA-minted data, and texture ablations with a human beauty-filter study -- that would validate or refute the proposal.

---


### 230. [Agent-Guided Relational Concept Discovery: Toward Interpretable Surgical Margin Assessment](https://arxiv.org/abs/2607.21437)

**<font color=#1a73e8>作者：</font>** Nooshin Maghsoodi, Amoon Jamzad, Robert Policelli 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning models can effectively use Rapid Evaporative Ionization Mass Spectrometry (REIMS) data for surgical margin assessment. However, their clinical adoption remains challenging due to limited generalization to operating room conditions. This difficulty arises because models are typically trained on labeled spectra collected from resected tissue samples, while they must operate on noisy, unlabeled data acquired directly during surgery. In addition, the black-box nature of deep learning models makes it difficult to understand and systematically improve their behavior. Concept-based learning offers a promising way to address these challenges by mapping raw measurements to human-understandable concepts. However, supervised concept-based approaches rely on concept annotations, which are difficult to obtain in complex mass spectrometry workflows. We propose Agent-Guided Concept Discovery, a framework that learns meaningful concepts directly from data without requiring predefined concept labels. During training, a reasoning agent refines semantic descriptions of the learned concepts and adaptively adjusts their weight based on diagnostic relevance. These concepts are further grounded using a biochemical knowledge graph to ensure consistency with known metabolic relationships. Across Skin and Breast Cancer datasets, our model improves balanced accuracy and sensitivity over the baseline. In a representative intraoperative case, it shows fewer false positives, indicating better generalization to surgical conditions.

---


### 231. [DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV](https://arxiv.org/abs/2607.21438)

**<font color=#1a73e8>作者：</font>** Tong Ling, Wenhui Diao, Yingchao Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation is a fundamental prerequisite for 3D reconstruction and autonomous navigation in Unmanned Aerial Vehicles (UAVs). In practical deployments, UAVs operate under highly dynamic camera poses characterized by continuous variations in height, pitch, roll, and field of view (FOV). Existing monocular depth estimation methods frequently fail to generalize across such diverse perspectives and the expansive scale of depth distributions inherent in aerial scenes. To address these challenges, we establish a quantitative representation of UAV viewing angles through rigorous theoretical analysis, deriving the geometric correspondence between viewing angles and view distances using the ground plane as a reference for observation. Building upon this, we propose Depth Estimation for Any Perspectives Model (DAPM), representing the first monocular framework specifically designed for UAV aerial imagery to jointly estimate camera pose and depth under continuously varying viewpoints. Specifically, we introduce an Ideal Ground Depth (IGD) module that leverages the derived geometric relationships between UAV perspectives and view distances to implement dense camera-pose supervision and enhance depth features. And we further develop a coarse-to-fine Progressive Quantization Bins (PQB) module. By incorporating progressive supervision and hierarchical quantization bins, the PQB module enables robust estimation in complex UAV aerial imagery. To evaluate the proposed framework, we present the UAV Any Perspectives Depth (UAPD) dataset, featuring comprehensive and continuous distributions of pose parameters. Experimental results on UAPD demonstrate that DAPM achieves state-of-the-art performance across both depth and camera-pose estimation metrics. The source code and datasets are available at: this https URL.

---


### 232. [RUMBA: Russian User Memory Benchmark](https://arxiv.org/abs/2607.21447)

**<font color=#1a73e8>作者：</font>** Elizaveta Shevtsova, Inna Glebkina, Mark Baushenko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The ability to handle long-term memory in LLMs is becoming increasingly critical, yet existing benchmarks remain English-centric and rely on aggregate retrieval metrics, failing to capture interactions between long-range context, temporal information, and reasoning. To address this, we introduce RUMBA (Russian User Memory BenchmArk) - a new benchmark for long-term conversational memory that provides a fine-grained taxonomy of memory-centric question types and a unified methodology accounting for semantic type, session scope, temporal reasoning, and the explicitness of temporal expressions. RUMBA consists of timestamped user-assistant dialogues with QA pairs requiring retrieval, combination, and reasoning across sessions. While designed for Russian, we also provide an aligned English subset under the same methodology. We evaluate contemporary memory systems and long-context models, and show how RUMBA serves as a diagnostic tool to analyze model behavior across benchmark slices and identify strengths and failure modes of different memory mechanisms.

---


### 233. [GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.21448)

**<font color=#1a73e8>作者：</font>** Jiahao He, Yihua Shao, Zhengkai Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic scene reconstruction with 3D Gaussian Splatting requires a balance between fine-grained motion modeling, structural stability, and compact representation. Existing per-primitive methods provide flexible local deformation but often suffer from redundant primitive growth, while anchor-based methods improve spatial regularity at the cost of suppressing locally varying motion. To address these issues, we present GrainGS, a dynamic Gaussian framework that combines a hierarchical anchor scaffold with per-Gaussian deformation. A static warm-up stage first establishes a time-invariant canonical representation from observations across all timestamps. During joint training, a stop-gradient operation blocks the deformation-mediated gradient pathway to the canonical positions while preserving their direct refinement through the reconstruction objective. Each Gaussian then predicts independent temporal offsets for position, rotation, and scale, enabling detailed local motion within a structurally constrained scaffold. A canonical-residual appearance decomposition further models frame-dependent photometric changes without forcing them into geometric deformation. Experiments on synthetic monocular and real-world multiview benchmarks show that GrainGS achieves high reconstruction quality, real-time novel view synthesis, and compact storage. Under the synthetic benchmark setting, it reaches an average peak signal-to-noise ratio of 36.98 decibels, renders at 435.6 frames per second, and requires 4.67 megabytes of storage.

---


### 234. [Test-Time Scaling via Error Localization](https://arxiv.org/abs/2607.21453)

**<font color=#1a73e8>作者：</font>** Rajiv Shailesh Chitale, Rahul Madhavan, Taneesh Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling inference-time computation has emerged as a reliable method to improve the performance of large language models on complex reasoning and programming tasks. However, standard approaches such as independent sampling and sequential multi-turn refinement operate without token-level credit assignment, resulting in computational inefficiency, since valid reasoning prefixes are frequently discarded. In this work, we introduce Test-Time Scaling via Error Localization (TTEL), an inference-time algorithm that utilizes fixed or environment feedback to perform token-level error localization. By comparing conditional probabilities under informed feedback against a null-context baseline, TTEL isolates the step at which an error occurred. The algorithm then truncates the trajectory and branches a new generation, maximally reusing the valid prefix. Extensive evaluations demonstrate that TTEL establishes strictly dominating Pareto frontiers across sequential reasoning domains, measured by pass-at-k vs. generated-token cost. With Qwen3-8B on LiveCodeBench, TTEL attains a pass@64 of 71.0% while generating approximately half as many tokens as independent sampling (360.4k vs. 735.0k). Generalizing to math benchmarks AIME-2025 and HMMT-2025, TTEL cleanly outperforms competing test-time baselines across both Qwen3-8B and Qwen3-4B-Thinking-2507.

---


### 235. [SPDCN: Strip-based Deformable Convolutional Network for Steel Surface Defect Segmentation](https://arxiv.org/abs/2607.21456)

**<font color=#1a73e8>作者：</font>** Zhongming Liu, Bingbing Jiang, Guangxin Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Steel surface defect segmentation is critical for industrial quality inspection, yet existing methods struggle with elongated, anisotropic defects such as cracks and scratches due to the isotropic receptive fields of standard convolutions and rigid sampling grids that cannot adapt to irregular defect boundaries. To address these limitations, we propose Strip-based Predictor for Deformable Convolutional Networks (SPDCN) with two key innovations. The \textbf{Fuzzy-enhanced Multi-scale Context Module (FMCM)} employs group-wise multi-branch convolutions with an intuitionistic fuzzy channel attention mechanism to adaptively capture multi-scale contextual information across varying defect sizes. The \textbf{Adaptive Direction-Aware Deformable Convolution (ADADC)} replaces the conventional offset predictor with decoupled horizontal and vertical strip convolutions, enabling the deformable sampling grid to anisotropically align with the principal orientation of elongated defects. Extensive experiments on public steel surface defect benchmarks demonstrate that SPDCN consistently outperforms state-of-the-art methods, achieving 89.60\% mIoU on NEU-Seg with only 3.54M parameters. The source code is publicly available at this https URL .

---


### 236. [AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461)

**<font color=#1a73e8>作者：</font>** Shuqi Lu, Chaofan Li, Kun Luo 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research requires agents to find answers that jointly satisfy multiple constraints. Discovering such answers is costly, whereas verifying a candidate can often be decomposed into tractable constraint-wise checks. This discovery--verification asymmetry suggests that a research agent should do more than simply search longer: it should recursively improve its current answer by verifying intermediate results and using the partially verified state to guide subsequent refinement. We introduce AREX, a family of Recursively Self-Improving (RSI) deep research agents. AREX alternates between an inner research loop that gathers evidence and constructs a provisional answer, and an outer self-improvement loop that audits the answer constraint-wise, identifies unresolved claims, and launches targeted follow-up research. To sustain RSI over long horizons, AREX learns an autonomous context-update tool that compresses growing interaction history into a compact improvement state preserving verified evidence and unresolved constraints, without relying on an external model. We train AREX on verified synthetic tasks and high-quality trajectories through agentic mid-training and long-horizon reinforcement learning. To mitigate sparse final rewards during long horizon learning, we emphasize key steps where decisive evidence is acquired or erroneous research directions are corrected. We instantiate a dense 4B model and a 122B-A10B Mixture-of-Experts model. Across BrowseComp, WideSearch, DeepSearchQA, Humanity's Last Exam (HLE), and other reasoning and tool-use benchmarks, AREX substantially outperforms comparable-scale baselines and remains competitive with models using substantially more activated parameters.

---


### 237. [CLUIE: Clustering-Aware Recurrent Propagation with Local Structural Compensation for Underwater Image Enhancement](https://arxiv.org/abs/2607.21467)

**<font color=#1a73e8>作者：</font>** Kui Jiang, Zefan Feng, Laibin Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater image enhancement remains challenging due to wavelength-dependent light absorption, scattering, and backscattering, which jointly cause color distortion, contrast degradation, and detail loss. Since these degradations vary with scene depth and imaging conditions, different regions within the same image often exhibit heterogeneous degradation patterns and thus require region-adaptive restoration. Although visual RWKV models offer an efficient linear-complexity solution for long-range dependency modeling, their predefined scanning orders are content-agnostic and therefore fail to adapt recurrent state propagation to spatially non-uniform restoration demands. To address this limitation, we propose a Clustering-aware RWKV framework, termed CRWKV, which reformulates the fixed recurrent propagation path of conventional RWKV into a content-adaptive token trajectory. Specifically, we introduce Clustering-aware Semantic Dynamic Reordering (CSDR), which groups tokens according to semantic feature similarity and derives a dynamic traversal order from inter-cluster contextual relations. This design enables WKV states to be accumulated along semantically correlated regions rather than fixed spatial or spectral orders. Since dynamic reordering may disrupt the local continuity of original spatial neighborhoods, we further propose Dark-response Modulated Local Propagation (DMLP), which extracts local structural responses via depth-wise convolution and adaptively modulates their propagation strength using a neighborhood-aware pseudo-dark response map. In this way, local structural cues are compensated before recurrent aggregation while preserving content-adaptive long-range modeling. Extensive experiments on multiple underwater image enhancement benchmarks demonstrate that CRWKV achieves state-of-the-art quantitative performance and superior visual quality.

---


### 238. [Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471)

**<font color=#1a73e8>作者：</font>** Yukun Shi, Minglun Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic-scene reconstruction is almost always evaluated inside the observed time window, yet deployment settings such as AR overlays, robot interaction, and anticipatory planning need the future surface: the geometry at times beyond those captured. No standard benchmark measures this. We introduce FutureSurf, a controlled diagnostic benchmark and dataset for future-time surface reconstruction that trades scene diversity for exact future ground truth and falsification controls. A method trains on the observed first 75% of a sequence; we score its extracted per-frame surface on the held-out future by Chamfer distance, reporting absolute future CD as the primary score and the future/observed gap as a diagnostic. The dataset contains eight analytically defined controlled motions, including three falsification controls, with exact per-frame ground-truth meshes. We also provide a ground-truth-side recoverability oracle. The release includes split files, scoring code, a benchmark card, and Croissant metadata. On the controlled motions, the DG-Mesh backbone leaves a 2.7-4.1$\times$ gap even for futures predictable in principle (four of five recoverable from observed motion by a fixed rule), while the falsification controls behave as designed (the surface-invariant motion shows no gap). Beyond the contributed dataset, the gap persists across six animated DG-Mesh asset scenes and a second backbone, Deformable-3DGS (2.0-6.6$\times$; both share a deformation-MLP temporal model). The benchmark also shows that future rendering quality and future-surface accuracy are statistically decoupled, so the novel-view-synthesis metrics the field reports do not track future geometry. The future error is structured, concentrating where the surface moves. The dataset, evaluation toolkit, and scoring code are available on Hugging Face and GitHub (this https URL).

---


### 239. [Error Certificates for KV-Cache Eviction via Randomized Design](https://arxiv.org/abs/2607.21475)

**<font color=#1a73e8>作者：</font>** Peng Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deterministic KV-cache eviction keeps the top-$k$ tokens under an importance score and deletes the rest. We prove that this design cannot know what it destroyed: evicted values can be altered so that everything the serving system retains is unchanged while the true attention-output error grows arbitrarily, so no serving-time estimator of that error is consistent. Randomized eviction restores identifiability. With a Poisson-sampled tail at known inclusion probabilities, one logit offset performs the Hájek correction inside the softmax, and a survey-sampling variance estimator over the retained set becomes a per-step error certificate with 0.97 empirical coverage at no accuracy cost. On real workloads we pre-registered seven claims and lost three: question-aware eviction at 25--50\% budgets is nearly free; output log-probability predicts failure better than the certificate; certificate-gated budget escalation adds nothing. What survives is attribution: the certificate separates cache-induced from inherent failures (AUC 0.73--0.75, against 0.47--0.54 for output confidence) and schedules recomputation better than random or confidence gating. Randomization buys attribution, not prediction.

---


### 240. [Recurrent Sinusoidal INRs for Efficient High-Fidelity Representation](https://arxiv.org/abs/2607.21485)

**<font color=#1a73e8>作者：</font>** Hyunmin Cho, Jaejun Yoo, Kyong Hwan Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study sinusoidal recurrence as an iterative mechanism for harmonic spectral enrichment in implicit neural representations (INRs). Our analysis reveals that sinusoidal activations induce a harmonic line spectrum, providing a spectral account of how recurrent unrolling enriches the effective spectral support. We realize this principle with a shared sinusoidal block that iteratively refines the latent representation. We empirically validate the resulting spectral behavior against feed-forward INRs, non-sinusoidal recurrent variants, and equilibrium-style sinusoidal models. Complementing this analysis, we evaluate the proposed architecture across image and 3D representation tasks. On RGB image benchmarks, our method achieves higher fidelity than feed-forward baselines with fewer parameters and fewer optimization steps, and it further transfers favorably to super-resolution, NeRF, and SDF tasks.

---


### 241. [Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections](https://arxiv.org/abs/2607.21488)

**<font color=#1a73e8>作者：</font>** Gil Lifshits, Igal Bilik, Gilad Katz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coordinating autonomous vehicles at unsignalized intersections remains a critical challenge for multi-agent reinforcement learning (MARL) systems, which typically struggle with combinatorial action spaces, reliance on privileged information, or rigid agent designs. We propose Master-Agent Proto-plan System (MAPS), a hierarchical deep reinforcement learning (DRL) architecture in which a centralized Master agent generates a compact, continuous embedding, denoted as proto-plan, that encodes a global coordination strategy. Decentralized Worker agents integrate this embedding with local observations to execute vehicle-specific control, decoupling strategic intent from tactical execution and enabling independent optimization of each module.
As a proof-of-concept evaluation of this coordination mechanism, we test MAPS across 72 intersection configurations in HighwayEnv. MAPS achieves collision-free navigation while significantly reducing average travel time, outperforming state-of-the-art baselines. The learned proto-plans further exhibit robust generalization: a system trained with three agents achieves a 94% success rate when deployed zero-shot to five-agent scenarios, confirming that proto-plan-based hierarchical learning provides a promising framework for multi-vehicle coordination.

---


### 242. [What, Where, and How: Disentangling the Roles of Task, Language, and Model in Code Model Representations](https://arxiv.org/abs/2607.21491)

**<font color=#1a73e8>作者：</font>** Piotr Wilam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do independently trained language models come to represent the same thing in the same way? We answer for code, extending a recently introduced concept-circuit extraction method to a 2x2 design -- Python and Rust crossed with Qwen2.5-Coder-7B and DeepSeek-Coder-V1-6.7B -- and measuring a complete inventory of grammatical concepts (58 Python, 57 Rust) identically in all four cells: the smallest design that separates what depends on the task, the language, and the model.
The answer splits into three parts. What earns dedicated circuitry is set by the task: the models agree on which concepts receive circuits (Spearman $\rho$ = 0.638 for Python, 0.673 for Rust, both p < $10^{-7}$). Where those circuits sit is set by the model: Qwen processes concepts in a late band (~L17-19), DeepSeek at L6-7, for both languages. How circuits grow across layers is also set by the model: Qwen gives its atomic concepts an early spike that DeepSeek does not. "Are circuits universal?" thus has no single answer: yes for What, no for Where and How -- universality is a property of representational content, not of computational organisation.
None of this structure was fixed in advance. The agreement could have landed anywhere between independence and identity; it lands at $\rho \approx 0.65$. Rust constructs receive 2-3x more concept-specific circuitry than their Python equivalents, in both models. Both models share neurons between the languages (6/7 and 7/7 paired constructs), DeepSeek 1.94x more than Qwen -- a direction no prior result predicts. And Qwen binds nine keywords of Rust's type-and-trait machinery into one tight neuron cluster (Jaccard 0.535 vs null 0.112, p < 0.001), a semantic dimension invisible in surface syntax. Ablation and linear probes confirm the circuits are functional.
All claims are scoped to this 2x2; whether the per-model profile predicts a third model is the designed next test.

---


### 243. [Toward Continuous Assurance for the Democratization of AI Agent Creation in Industry](https://arxiv.org/abs/2607.21495)

**<font color=#1a73e8>作者：</font>** Natan Levy, Harel Berger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly created inside organizations by non-engineering users through low-code, no-code, and conversational development environments. This democratization enables rapid local innovation, but it also creates a reliability gap: agents that appear to users as simple productivity artifacts may depend on changing models, tools, retrieval sources, permissions, prompts, schedules, and external services. These dependencies can cause silent degradation long after deployment, even when no user directly modifies the agent. This paper identifies the reliability challenge created by democratized AI agent creation and proposes a lightweight continuous-assurance framework for citizen-created organizational agents. The framework combines dependency mapping, readiness contracts, scheduled checks, diagnostics, and lifecycle governance to assess whether an agent remains operationally ready under expected conditions. We also present an initial prototype auditor and scenario-based assessment showing how the proposed taxonomy can be translated into practical checks and actionable remediation guidance.

---


### 244. [A Needs Assessment for Measuring Geographic - Legislative Associations in the U.S. House of Representatives](https://arxiv.org/abs/2607.21502)

**<font color=#1a73e8>作者：</font>** Ashu Gupta, Cameron Owens, Benjamin Wilson-Langman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Political legislation affects the well-being and livelihoods of constituents. In the U.S. Congress a representative's voting record on bills and legislation is public. These bills have themes associated with them, such as veterans' affairs, coastal monitoring, agricultural appropriations, etc. A bill on veterans' affairs may affect a constituency differently if they have a high percentage of veterans. In this work, we demonstrate how congressional vote outcomes can be merged with typical geographic information systems (GIS) data to help compare a legislator's votes with the geographies of their constituencies to measure the association between district features and legislators' decisions.
We retrieved and tagged bills from the 118th U.S. House of Representatives (Jan. 2023 - Jan. 2025) by manually assigning each bill a set of themes. We then retrieved spatial data at the congressional district level related to each theme. We built a backend database to connect bill information and spatial data, and an interactive map prototype displayed the spatial data related to each theme associated with each bill. Our work helps identify challenges to creating a more accessible and complete system that would facilitate the visualization and analysis of the nature of contemporary Congressional representation. This technical report is primarily written for members of the data science community, and specifically those interested in legislative and geographic data.

---


### 245. [Texture++: Elevating 3D Asset Texture Resolution with a Region-Aware Diffusion Model](https://arxiv.org/abs/2607.21504)

**<font color=#1a73e8>作者：</font>** Shuaiwei Wang, Shi Li, Jieting Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Numerous 3D assets are discarded due to low texture resolution, while current super-resolution models ignore texture maps and focus on natural images. An efficient and generalizable texture super-resolution model can revitalize a large corpus of aging yet valuable assets across industries such as film and video games. We present Texture++, a novel framework for texture super-resolution, which enhances the low-resolution textures of assets to produce high-resolution, high-quality results. Specifically, we reformulate the task of super-resolution in UV space into performing it across multiple rendered views and merging the outputs. Firstly, to achieve more complete and continuous textures in the view space, we propose an adaptive view selection strategy to integrate textures dispersed across UV texture patches. Furthermore, we introduce a quadtree-based texture region organization method for combining super-resolved textures from different viewpoints, providing masks to distinguish regions that require improvement. Finally, we design a diffusion-based super-resolution model that enhances the texture resolution for specified masked regions, seamlessly integrating with surrounding regions. Through comprehensive evaluations, we demonstrate that our approach yields textures with substantially improved detail and coherence over existing methods.

---


### 246. [Transparent by Design, Usable in Practice? A Formative Usability Study of a Conversational Product Advisor](https://arxiv.org/abs/2607.21513)

**<font color=#1a73e8>作者：</font>** Kevin Schott, Dagmar Kern, Daniel Hienert  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models can make conversational product advisors fluent but opaque. If they hide the logic behind a ranking and the evidence for a recommendation inside natural-language replies, they challenge users' ability to understand, trust, and steer the results. One response is to build transparency into the advisor. We report a formative, moderated think-aloud usability study of one such system: a chatbot for laptop search with constrained natural-language generation, an on-demand ranking explanation, and a comparison feature. Seven participants completed three laptop-search tasks and reported post-task usability measures. We coded their sessions into severity-rated usability problems. Ease and satisfaction during the tasks were high, but two findings stand out. First, transparency by design did not guarantee understanding: several participants valued the ranking explanation in principle, yet it caused the most severe problem. Second, participants valued the effort the advisor saved, but some wanted additional direct-manipulation controls. We contribute a severity-prioritized set of usability problems and design implications for human-centered conversational product advisors.

---


### 247. [Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation](https://arxiv.org/abs/2607.21518)

**<font color=#1a73e8>作者：</font>** Linjun Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Even a current high-capability LLM can appear safer when shown a dangerous objective directly than when other agents transform and relay its direction. Using OpenAI's gpt-5.6-sol model alias, we test 25 pre-specified mirrored trade-off profiles. Direct exposure to an objective authorizing concealment, fabrication, and pressure produced advice net opposed to its target. After an Id and Censor transformed the same objective into affect and a constraint-rewritten, target-bearing intention, the user-facing Superego---which saw the preferred direction but not the raw objective, its manipulative clauses, or its source---produced advice net aligned with the target.
This behavioral reverse shift is consistent with the model recognizing or distrusting the manipulative motive, although we do not identify its internal mechanism. The second result exposes a compositional safety gap: a current high-capability model can be used as the user-facing component of an automated, multi-stage workflow serving an explicitly manipulative objective. The workflow can keep the raw instruction, its manipulation-authorizing clauses, and its provenance outside the downstream model's context while preserving the objective's target direction. A user with endpoint-only access likewise cannot directly inspect those upstream messages including the objective.

---


### 248. [Boosting Robustness for All-Weather Self-Supervised Depth Estimation in Autonomous Driving](https://arxiv.org/abs/2607.21526)

**<font color=#1a73e8>作者：</font>** Mengshi Qi, Xiaoyang Bi, Xianlin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised depth estimation is challenging for safe autonomous driving under various adverse weather conditions due to sensor perception degradation. These challenges arise from two main aspects. Firstly, adverse conditions can distort pixel correspondences and violate the assumptions embedded in the self-supervised loss function, leading to erroneous depth predictions. Secondly, while radar is a widely adopted sensor in adverse weather conditions, the sparse distribution of radar points in the Point of View (POV) poses challenges for self-supervised fusion. To address these issues, we introduce a novel self-training pipeline using unpaired real all-weather data through multi-teacher distillation and robust radar fusion. We propose the Uncertainty-Aware Multi-Teacher Distillation method to generate diverse teacher models with different adverse condition inputs, and then employ uncertainty modeling to weigh the knowledge distillation loss. Additionally, we design the POV-BEV Radar Fusion approach, which leverages camera-pixel ray constraints to establish connections between the camera's Point of View (POV) and the radar's Bird's-Eye View (BEV). This approach enables the utilization of denser radar points, effectively capturing the complementary perspectives of both POV and BEV. Extensive quantitative and qualitative experiments demonstrate the robustness of our proposed method on all-weather datasets, achieving state-of-the-art performance. Our code and models are available at this https URL.

---


### 249. [Sources of Inequity and Fairness Risks inWellbeing Sensing](https://arxiv.org/abs/2607.21527)

**<font color=#1a73e8>作者：</font>** Han Zhang, Vedant Das Swain, Koustuv Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Passive sensing for wellbeing uses smartphones and wearables to continuously collect human behavioral data and applies ML/AI models to infer psychological states and behaviors (e.g., depression, cognitive load). These systems are increasingly adopted in high-stakes settings (e.g., hospitals, universities), yet fairness research remains limited---primarily to post-hoc, identity-based comparisons of model performance. However, passive sensing combines heterogeneous sensing infrastructures, indirect behavioral inference, and longitudinal deployment---characteristics that, while not exclusive to the domain, are jointly pronounced here and raise two underexplored questions: (1) what additional sources of inequity arise from these characteristics, and (2) how do such inequities propagate beyond algorithmic audits across the system lifecycle? To address this gap, we conducted semi-structured interviews with 14 researchers and practitioners across five countries, examining how fairness risks emerge and are negotiated across the full passive sensing lifecycle. Our findings empirically characterize five situated sources of inequity (e.g., comfort with monitoring, behavioral regularity) that systematically shape fairness risks beyond identity-based attributes. We further synthesize 15 fairness risks and corresponding mitigation strategies across the lifecycle, from study design to deployment. Finally, we identify structural barriers that constrain fair practice in reality, and argue that enabling fair passive sensing requires both individual researcher efforts and ecosystem-level governance support from funders, publication venues, and deploying institutions.

---


### 250. [ElasticTTT: Prior-Preserving Test-Time Tuning for Video Editing](https://arxiv.org/abs/2607.21529)

**<font color=#1a73e8>作者：</font>** Yueyi Liu, Chi Zhang, Sen Cui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-Time Tuning (TTT) on pretrained diffusion models has emerged as a powerful paradigm for video editing. However, there exists a foundational mismatch between the distribution-mapping nature of generative models and the single-point optimization of standard TTT. In this paper, we demonstrate that this mismatch triggers \textit{Prior Collapse}, a degenerate state where the model discards the text conditions and spatial latents, collapsing generations to the source video, or entangling the features of distinct regions. To resolve this, we propose \textbf{ElasticTTT}, a novel framework that preserves the prior generative distribution and rescues generative elasticity. Specifically, we propose \textit{Target Distribution Regularization} to prevent sharp memorization minima, \textit{Contrastive CFG} to guide inference away from source biases, and \textit{Asynchronous Noise Schedule} to preserve unedited regions. Extensive evaluations, supported by theoretical analysis, demonstrate that ElasticTTT successfully preserves the generative prior of the base model, achieving state-of-the-art performance on one-shot video editing.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-271](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
