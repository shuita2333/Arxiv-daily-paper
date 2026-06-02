# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 301. [AMP: A Vendor-Neutral Wire Format for Agent Memory Operations](https://arxiv.org/abs/2606.01138)

**<font color=#1a73e8>作者：</font>** Thamilvendhan Munirathinam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent-memory frameworks - mem0, Letta/MemGPT, Cognee, Zep/Graphiti, MemoryOS, MemTensor - each ship their own SDK, storage layout, and operational vocabulary. There is no shared wire format: every integration is bespoke, every migration rebuilds memory from scratch, and no framework ships a governance surface that lets a human review writes before they enter long-term storage. We present memorywire, a JSON-Schema 2020-12 wire format for five memory operations (remember, recall, forget, merge, expire) over four memory types (semantic, episodic, procedural, emotional), with a MemoryStore interface, a fan-out router, and an optional HITL governance channel. We describe an open-source reference implementation with five backend adapters (sqlite-vec, mem0, Letta, Cognee, pgvector); a microbenchmark on a 100-fact / 50-query labelled corpus achieving recall@5 = 1.000 on the 42 labelled queries with ingest p50 = 37.8 ms and recall p50 = 40.6 ms; an adversarial-fusion experiment showing Reciprocal Rank Fusion holds recall@5 = 1.000 across a 1-of-N rank-0 injection sweep (K in {0,5,...,50}) where max fusion collapses to 0.500 with 80% leak at K >= 5; and a 16-scenario cross-adapter conformance suite passing 68 of 80 cells with zero failures. The contribution is not a new algorithm; it is a packaging of established components (RRF, FSMs, STM/LTM consolidation, diff-and-approve workflows) into a venue-neutral protocol with an empirically validated reference, positioned to compose with the Model Context Protocol rather than compete with it.

---


### 302. [Not All Explanations Simulate Equally: Comparing Verbalized Feature Attributions and Self-Generated Rationales](https://arxiv.org/abs/2606.01148)

**<font color=#1a73e8>作者：</font>** Pingjun Hong, Benjamin Roth  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural-language explanations are often treated as a unified interface for understanding model behavior, but different explanation sources may support simulation in different ways. This paper compares two families of explanations for question answering models: verbalized feature attributions and self-generated rationales. We evaluate them under a shared counterfactual simulation setting, using an LLM judge as predictor and measuring whether it can better predict a model's answers to follow-up questions when given its explanation. Across multiple instruction-tuned models, we analyze how explanation source, verbalization strategy, and feature granularity affect the simulatability of explanations. Our results show that explanation format and granularity affect simulatability: attribution-based explanations and self-generated rationales differ in how much they improve counterfactual prediction, with effects that vary across models and formats.

---


### 303. [CoSTL: Comprehensive Spatial-Temporal Representation Learning for Moment Retrieval and Highlight Detection](https://arxiv.org/abs/2606.01149)

**<font color=#1a73e8>作者：</font>** Xin Dong, Wenjia Geng, Wenfeng Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Moment Retrieval (MR) and Highlight Detection (HD) are crucial tasks in video analysis that aim to localize specific moments and estimate clip-wise relevance based on a given text query. Recent approaches treat them as similar video grounding tasks and use the same architecture to solve them. These tasks require both fine-grained comprehension at the image level and high-level temporal understanding across the entire video. Existing approaches have primarily focused on temporal modeling using frame-level features, often neglecting the rich visual information related to the text query within individual frames. This oversight leads to inaccurate grounding results. To address this limitation, we propose a Comprehensive Spatial-Temporal Representation Learning Framework (CoSTL), which captures both fine-grained image-level information and temporal dynamics. Specifically, CoSTL incorporates a text-driven progressive fine-grained image encoder, performing a two-step text-driven knowledge extraction process to learn fine-grained spatial representations. Furthermore, a multi-scale temporal perception module captures comprehensive spatial-temporal representations, enhancing the model's ability to process temporal dynamics. We demonstrate state-of-the-art performance on four public benchmarks: QVHighlights, Charades-STA, TACoS, and TVSum.

---


### 304. [Lagrangian Perturbation Diffusion Steering: Latent Reinforcement Learning for Generative Policies](https://arxiv.org/abs/2606.01151)

**<font color=#1a73e8>作者：</font>** Hikmet Simsir, Ozgur S. Oguz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavior cloning with high-capacity generative policies achieves strong imitation performance, but is often limited by demonstration coverage and distribution shift. Direct reinforcement learning fine-tuning can improve performance, but updating large action decoders is frequently unstable and sample inefficient. We propose Lagrangian Perturbation Diffusion Steering (LP-DS), a lightweight adaptation method that improves a frozen generative policy by learning a compact noise-space perturbation before decoding. LP-DS optimizes this perturbation with a Lagrangian trust-region objective, improving downstream value while constraining deviation from the latent prior. Across RoboMimic manipulation, OpenAI Gym locomotion, and Adroit dexterous manipulation benchmarks, LP-DS improves sample efficiency, success, and return while maintaining higher action-space entropy than unconstrained noise-space steering, with return improvements of up to 25% over prior baselines. Additional evaluations with flow-matching backbones, a large vision-language-action model, and physical Franka deployment show that LP-DS is not limited to compact diffusion policies or simulated benchmarks. Project page: this https URL.

---


### 305. [HiTokSR: A Coarse-to-Fine Tokenizer with Hierarchical Codebooks for High-Fidelity Real-World Image Super-Resolution](https://arxiv.org/abs/2606.01157)

**<font color=#1a73e8>作者：</font>** Mingxi Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector-quantized (VQ) generative models have shown promising results in real-world image super-resolution (Real-ISR). However, existing methods typically rely on a monolithic latent space that entangles low-frequency structures with high-frequency textures. This entanglement forces a single codebook to capture a combinatorially complex set of structure-texture pairings, which constrains representational capacity and limits codebook utilization. To address this issue, we present HiTokSR, a hierarchical token prediction framework. Instead of using a single codebook, HiTokSR partitions the latent space along the channel dimension into frequency-aware groups, quantizing each with an independent sub-codebook. This coarse-to-fine design disentangles global structures from fine details, enhancing combinatorial expressiveness while circumventing the optimization instability of high-dimensional nearest-neighbor lookups. To further improve semantic consistency, our generator integrates priors from a vision foundation model via adaptive feature modulation, multi-scale class tokens, and a representation alignment loss. Additionally, we introduce an index-level perturbation strategy during decoder fine-tuning to bridge the train-test discrepancy in discrete token prediction. Extensive experiments on real-world benchmarks demonstrate that HiTokSR achieves state-of-the-art performance in both perceptual quality and reconstruction fidelity.

---


### 306. [Fairness in two-player zero-sum games with bandit feedback](https://arxiv.org/abs/2606.01159)

**<font color=#1a73e8>作者：</font>** S Akash, Pratik Gajane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study two-player zero-sum games (TPZSGs) with bandit feedback under fairness constraints requiring every action to be played with probability at least $\alpha/m$. Existing instance-dependent results target $\textit{pure}$ Nash equilibria, while fairness generically produces $\textit{mixed}$ equilibria, a harder learning target. Our key technical tool is a reparametrization: every fair strategy decomposes as $p = (\alpha/m)\mathbf{1} + (1-\alpha)\widetilde{p}$ with $\widetilde{p} \in \Delta_m$, and substituting into the payoff form yields $p^{\top}Aq = \widetilde{p}^{\top}\widetilde{A} q$ for a fair payoff matrix $\widetilde{A} := (1-\alpha)A + \alpha\mathbf{1} c^{\top}$, where $c_j = \tfrac{1}{m}\sum_i A(i,j)$ is the column-mean vector. The fair game on $A$ is then equivalent to a standard zero-sum game on $\widetilde{A}$, so equilibrium existence, KKT structure, and LP basis stability reduce to classical results applied to $\widetilde{A}$. We derive the fair minimax value, fair Nash equilibrium, fair regret, and a clean dual representation showing the price of fairness is at most $\alpha(1-1/m)$ and vanishes whenever the unconstrained equilibrium already has full support. Our main result is an $\widetilde{O}(T^{2/3})$ regret bound for an Explore-Then-Commit algorithm, $\texttt{Fair-ETC-TPZSG}$, applicable to general mixed fair equilibria, together with a discussion of why naive action elimination does not readily improve it. When the fair equilibrium has a single dominant action, equivalently when $\widetilde{p}^{\star}$ is a vertex of $\Delta_m$, the bound sharpens to instance-dependent $\widetilde{O}(1/\widetilde{\Delta}(\alpha)^{2})$, where $\widetilde{\Delta}(\alpha)$ is the LP-margin gap.

---


### 307. [Deft Scheduling of Dynamic Cloud Workflows with Varying Deadlines via Mixture-of-Experts](https://arxiv.org/abs/2606.01162)

**<font color=#1a73e8>作者：</font>** Ya Shen, Gang Chen, Hui Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Workflow scheduling in cloud computing demands the intelligent allocation of dynamically arriving, graph-structured workflows with varying deadlines onto ever-changing virtual machine resources. However, existing deep reinforcement learning (DRL) schedulers remain limited by rigid, single-path inference architectures that struggle to handle diverse scheduling scenarios. We introduce \textbf{DEFT} (\textbf{D}eadline-p\textbf{E}rceptive Mixture-o\textbf{F}-Exper\textbf{t}s), an innovative DRL policy architecture that leverages a specialized mixture of experts, each trained to manage different levels of deadline tightness. To our knowledge, DEFT is the first to introduce and validate a Mixture-of-Experts architecture for dynamic cloud workflow scheduling. By adaptively routing decisions through the most appropriate experts, DEFT is capable of meeting a broad spectrum of deadline requirements that no single expert can achieve. Central to DEFT is a \textbf{graph-adaptive} gating mechanism that encodes workflow deadlines and DAGs, task states, and VM conditions, using cross-attention to guide expert activation in a fine-grained, deadline-sensitive manner. Experiments on dynamic cloud workflow benchmarks demonstrate that DEFT significantly reduces execution cost and deadline violations, outperforming multiple state-of-the-art DRL baselines.

---


### 308. [Coordinating Task Switching in a Robotics Multi-Agent System Using Behavior Trees](https://arxiv.org/abs/2606.01170)

**<font color=#1a73e8>作者：</font>** Lucas Haug, Anarosa Alves Franco Brandão, Arthur Casals  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The application of multi-agent systems in robotics is a very challenging field. Several competitions involving such systems are proposed to foster research and development of strategies and mechanisms using games as the underlying domain. Among them are the ones from the \textit{IEEE Very Small Soccer (VSSS)} category, which is the case study described in this paper. In VSSS, two teams of three robots each compete in a very dynamic environment of a soccer game. Thus, coordination of robots' behavior during the game is crucial to win it. In this paper, we present a Behavior-Tree-based approach to support multi-robot coordination within the VSSS team of the ThundeRatz robotics team from the Universidade de S$\tilde{a}$o Paulo. Moreover, a comparison between the proposed approach and the previous one, which was based on a Finite State Machine (FSM), was conducted using the FIRASim simulator. Besides that, the performance of this new strategy was further evaluated in an academic robotics competition.

---


### 309. [Revisiting Neural Processes via Fourier Transform and Volterra Series](https://arxiv.org/abs/2606.01172)

**<font color=#1a73e8>作者：</font>** Peiman Mohseni, Nick Duffield, Raymond K. W. Wong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling unknown latent functions from finite, irregularly sampled measurements is a recurring challenge across science and engineering. Neural processes (NPs), a family of probabilistic functional models, are promising solutions -- especially when endowed with domain-specific symmetries like translation equivariance, which improve sample efficiency and generalization. Yet existing translation-equivariant NPs face two limitations: (i) they stack generic components with non-linearities, obscuring the induced function class and limiting interpretability; and (ii) convolutional designs rely on kernels with local receptive fields and require dense uniform input grids, while attention-based methods avoid these issues but scale quadratically with the number of observations. We address both with two contributions. First, using the Volterra expansion, we characterize continuous translation-equivariant operators as sums of higher-order convolutions, yielding analytical transparency while admitting efficient approximation by first-order convolutions. Second, we introduce set Fourier convolutions (SFConvs), a frequency-domain parameterization that operates directly on irregularly sampled points, achieves approximately global receptive fields, and scales linearly in the number of observations. Building on these ideas, we propose two conditional NPs (CNPs): SFConvCNPs, which stack SFConv blocks with non-linearities, and SFVConvCNPs, which integrate the Volterra formulation. Experiments on synthetic and real-world datasets demonstrate our methods' efficacy against state-of-the-art baselines.

---


### 310. [Reusing Fusion-Time Spectral Reliability for Adaptive Fusion and Expert Routing in RGB-Infrared Object Detection](https://arxiv.org/abs/2606.01173)

**<font color=#1a73e8>作者：</font>** Yefeng Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-infrared detectors typically discard the statistics generated during cross-modal fusion, leaving downstream modules unaware of whether the current interaction is reliable. We propose to extract a parameter-free, 7-dimensional spectral reliability descriptor -- summarizing band energy, amplitude ratio, phase consistency, and cross-modal correlation -- and to reuse it beyond the fusion stage. The descriptor drives both Spectral Reliability Fusion (SRF), which gates a spectral residual against a conservative spatial base, and Reliability-Conditioned Expert Routing (RCER), which combines the descriptor with pooled content to steer sparse post-fusion experts. Under matched ablations, descriptor-aware gating improves mAP50 over content-only adaptive gating; a $2{\times}2$ factorial analysis further shows that descriptor-conditioned routing provides the larger marginal gain over expert architecture alone at near-equal parameter count. Under six synthetic degradations on DroneVehicle, average retention rises to 95.0%, versus 92.0% for content-only MoE and 87.9% for concatenation, with the largest gain under modality drop; the same model also improves mAP50 by +5.2/+5.3 on the natural day/night split. These results suggest that preserving fusion-time reliability as an explicit signal benefits both adaptive fusion and post-fusion conditional computation.

---


### 311. [Temporal Motif Signatures for Temporal Graph Neural Networks](https://arxiv.org/abs/2606.01176)

**<font color=#1a73e8>作者：</font>** Dylan Sandfelder, Mihai Cucuringu, Xiaowen Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real temporal interaction streams carry predictive structure in short-horizon motif patterns -- repetition, reciprocity, star diversity, triadic flow -- that vanilla temporal graph neural networks (TGNNs) often fail to expose to their edge scorers. We show this concretely on MOOC interaction prediction, where a small four-feature family of past-window star counts already delivers most of the lift over a strong static GNN. Across a wide set of real and synthetic temporal datasets we find that motif activity organizes consistently along three scale-stable axes (dyadic recency/reciprocity, star diversity, triadic flow), and we use this empirical structure to design a compact 13-coordinate, leakage-safe, candidate-local motif feature map h(u, v, t) that linearly embeds into any static or temporal encoder without architectural changes. A temporal Weisfeiler-Leman (WL) analysis places the augmentation relative to the first level of an anchored temporal-WL hierarchy and exhibits a candidate-anchored pair on which motif features distinguish. We demonstrate empirically that the same augmentation consistently lifts performance across heterogeneous tasks: TGB link-property prediction across all five baselines, edge classification on Bitcoin Alpha/OTC and MOOC, and graph-level classification of synthetic temporal generators.

---


### 312. [Physics-Informed Deep Learning for Entropy Prediction in Heterogeneous Systems: Thermodynamic and Information-Theoretic Case Studies](https://arxiv.org/abs/2606.01179)

**<font color=#1a73e8>作者：</font>** Biswajeet Sahoo, Debadutta Patra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entropy production governs irreversibility and uncertainty in both physical and information-theoretic systems. While Physics-Informed Neural Networks (PINNs) successfully solve differential equations, current architectures remain inherently domain-specific. The extraction of domain-invariant entropy representations across fundamentally different physical laws remains unexplored. This paper introduces a unified Physics-Informed Deep Learning (PIDL) framework that simultaneously enforces differential equation residuals and information-theoretic bounds within a single neural architecture. We demonstrate this framework via two canonical studies: (i) a thermodynamic continuous stirred-tank reactor (CSTR) model solving governing ODEs, where a Softplus constraint strictly enforces the Second Law of Thermodynamics; and (ii) an information-theoretic financial market model solving the inverse Fokker-Planck PDE to infer latent drift and diffusion coefficients, guaranteeing diffusion positivity via a Softplus constraint while naturally inducing Shannon entropy. Three model variants are evaluated: two domain-specific baselines and one shared-encoder architecture. The PIDL framework guarantees absolute thermodynamic admissibility with zero Second-Law violations and exhibits exceptional data efficiency, retaining >90% predictive accuracy using merely 30% of available training data. Furthermore, a post-hoc Ruppeiner Riemannian geometric analysis of the learned entropy surface successfully identifies thermodynamic phase instabilities. This methodology provides a robust, domain-agnostic architecture for physics-constrained entropy modeling, advancing applications in sustainable process design and quantitative financial risk assessment.

---


### 313. ["Skill issues'': data-centric optimization of lakehouse agents](https://arxiv.org/abs/2606.01185)

**<font color=#1a73e8>作者：</font>** Nicole Rose Schneider, Davide Ghilardi, Giacomo Piccinini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are becoming users of data infrastructure, but their success depends not only on model quality: it also depends on the skills and environment files that teach agents how to use a system. We study how to optimize these artifacts for agents operating on a branching lakehouse, Bauplan. In our setting, headless APIs and Git-like data primitives expose data workflows through code, branches, commits, and merges. Our central observation is that a branching lakehouse turns data-agent evaluation from an output-matching problem into a state-verification problem: agent-generated pipeline code induces concrete, inspectable lakehouse changes. We present a data-centric optimization pipeline that generates task-verifier pairs, executes candidate skills in isolated sandboxes, and scores trajectories using both trace-level signals and programmatic checks over lakehouse state. In a preliminary evaluation on 25 tasks, optimized skills improve accuracy by 31.9%. These results suggest that write-path data workflows provide a useful substrate for optimizing agent skills beyond read-only tasks.

---


### 314. [The Case for Model Science: Verify, Explore, Steer, Refine](https://arxiv.org/abs/2606.01189)

**<font color=#1a73e8>作者：</font>** Przemyslaw Biecek, Luca Longo, Jianlong Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We argue that the AI community is now ready to move beyond benchmarking and consolidate scattered efforts in model analysis into a systematic discipline, a direction we term Model Science. Complex AI models now serve billions of users, yet our understanding of how they work lags far behind our ability to deploy them. Decades of benchmark-driven research have delivered remarkable progress: extensive leaderboards, a wide range of performance metrics, tracking capability gains across diverse tasks; yet this success has also revealed the limits of benchmarks as they tell us whether models perform but not why they succeed or fail, they miss critical failure modes, such as hallucinations or shortcuts. Precedents from established sciences point the way forward: cognitive science shows that understanding complex systems requires complementary levels of analysis; neuroscience demonstrates that deep study of single cases reveals what population studies miss; medicine teaches that specialised training must develop alongside research practice; and agriculture models how shared infrastructure and principles enable cumulative progress. These lessons inform three foundations for Model Science. First, we propose to consolidate research around four functional perspectives: Verify, Explore, Steer, and Refine that address complementary questions about model behaviour. Second, we discuss the required infrastructure for cumulative knowledge: catalogues of datasets, models and findings. Third, we highlight the need for deep analysis of individual model instances, not just model families, because single cases can reveal what population studies miss.

---


### 315. [PairedGTA: Generating Driving Datasets for Controlled Photometric Shift Analysis](https://arxiv.org/abs/2606.01192)

**<font color=#1a73e8>作者：</font>** Andrea Chianese, Giulio Rossolini, Alessandro Biondi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating the performance of visual perception systems for autonomous driving is essential to ensure reliable operation across diverse environmental scenarios. Ideally, a balanced and fair analysis across different adverse conditions would require perfectly paired images of the same scene under different weather or illumination changes. This would allow evaluating the effect of photometric shifts independently of geometry and semantic changes. Unfortunately, real-world datasets rarely provide images of the same scene under different environmental conditions, because, normally, camera pose, traffic, and locations of dynamic objects (vehicles, pedestrians, etc.) vary over time, thus yielding only coarsely paired data. To address this challenge, this work introduces a data generation framework based on a high-fidelity game engine for extracting perfectly paired images. By leveraging software APIs that communicate with the GTA game engine, the framework modifies illumination and weather conditions while preserving scene geometry, camera pose, and the identity and placement of dynamic objects. For each sampled location, it procedurally instantiates dynamic entities and renders pixel-aligned images under diverse adverse conditions. The benefit of the proposed generation framework in driving scenarios is demonstrated through a systematic analysis of semantic segmentation models, whose output degradation can be attributed more directly to photometric shifts rather than to uncontrolled semantic or geometric factors.

---


### 316. [Low-Resource Safety Failures Are Action Failures, Not Representation Failures](https://arxiv.org/abs/2606.01196)

**<font color=#1a73e8>作者：</font>** Rashad Aziz, Ikhlasul Akmal Hanif, Fajri Koto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment learned in high-resource languages transfers poorly to low-resource languages. Models refuse harmful prompts in English but fail to refuse when the same prompts are translated into Swahili or Burmese. Adaptive steering methods like AdaSteer and CAST inherit this failure cross-lingually. We diagnose where transfer breaks down. Across Qwen2.5-7B, Gemma-2-9B, and Llama-3.1-8B on 23 languages, the harmfulness direction extracted from high-resource activations linearly separates harmful from harmless low-resource prompts nearly as well as high-resource ones. The relevant representation is present. Yet harmful refusal drops from 87.9% to 43.9%. The model fails to convert the representation into refusal. What fails to transfer is calibration of the safety decision, not the underlying representation. We exploit this by recalibrating, rather than retraining, a high-resource gate: a low-rank logistic readout with its decision threshold reset using as few as 1 to 4 target-language examples per class. The gate routes between refusal steering and harmfulness-direction ablation, substantially raising mean refusal selectivity ($\Delta$ = harmful $-$ harmless refusal) from 33.6 for the strongest adapted baseline to 54.5 while preserving MMLU utility. These results suggest that some low-resource safety failures can be repaired by recalibrating existing representations rather than learning new ones. Our code is released: this https URL.

---


### 317. [Linear Strategic Classification with Endogenous Improvements](https://arxiv.org/abs/2606.01198)

**<font color=#1a73e8>作者：</font>** Siddharth Shrivastava, Mahvith Akshintala, B Vamsha Vardhan Reddy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Strategic classification studies settings in which agents respond to a deployed classifier by modifying observable features at a cost. Classical models typically treat such responses as cosmetic: features may change, but true labels remain fixed. We study an improvement-aware variant in which strategic responses can induce genuine changes in outcome-relevant features. Agents choose post-deployment feature vectors strategically, and labels are then generated according to a stable conditional outcome law that preserves the relationship between features and outcomes. We formalize this problem for linear classifiers under a single-index qualification model and linear-decomposable costs. We show that the strategic-optimal classifier is obtained by a parallel shift of the Bayes-optimal decision boundary, and that it provides a better surrogate for the improvement-aware objective than the Bayes classifier. Since improvement-aware learning requires post-deployment labels, which are typically unavailable before deployment, we provide PAC-style guar- antees under an oracle model, propose a practical plug-in algorithm, establish its generalization bound, and evaluate it on synthetic and real-world datasets.

---


### 318. [From Craft Practice to Aesthetic Cognition Transmission: Workflow Cognition Translation for AI-native Intangible Cultural Heritage Education](https://arxiv.org/abs/2606.01203)

**<font color=#1a73e8>作者：</font>** Annie Yuan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Intangible Cultural Heritage (ICH) education has traditionally relied on apprenticeship, embodied participation, and long-term engagement with masters, materials, and cultural environments. While these modes of transmission remain essential, they are difficult to scale. Existing digital heritage initiatives have expanded documentation and access, but often preserve artefacts, procedures, and representations of practice rather than the aesthetic and cognitive structures through which expertise operates. This paper argues that the future challenge of ICH education is not only the transmission of craft techniques, but the scalable transmission of aesthetic cognition: the perception, judgement, interpretation, and culturally situated meaning-making through which aesthetic expertise develops. Drawing on aesthetic education, tacit knowledge, cognitive apprenticeship, and expert cognition, we propose a shift from craft transmission to Aesthetic Cognition Transmission. To support this shift, we introduce Workflow Cognition as a model of how experts coordinate perception, judgement, decision-making, and action within evolving workflows. We then propose Workflow Cognition Translation as a methodological framework for transforming expert workflow cognition into computable educational representations for AI-native learning systems. The paper makes three contributions: it reframes ICH education around aesthetic cognition transmission; introduces Workflow Cognition Translation as a method for representing expert aesthetic cognition; and outlines an AI-native cognitive apprenticeship infrastructure involving AI Expert Twins, workflow-based tutoring, and progressive learner participation. Rather than replacing masters, workshops, or embodied practice, the framework positions AI as a cognition mediation infrastructure for expanding access to heritage expertise.

---


### 319. [Schema-Agnostic Knowledge Graph Construction via Hybrid Ontology Discovery for Cyber Threat Intelligence](https://arxiv.org/abs/2606.01208)

**<font color=#1a73e8>作者：</font>** Seonwoo Kim, Jinwoo Kim, Daegyu Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threat intelligence (CTI) reports now serve as essential resources for capturing adversary tactics, techniques, and procedures observed in modern attack campaigns. While traditional CTI platforms reduce this intelligence to isolated indicators through fixed schemas such as STIX, ontology-based representations preserve the semantic relationships needed for structured threat analysis. However, existing approaches for ontology-aligned CTI extraction face three challenges: (i) schema-specific pipelines that require manual reconfiguration whenever the schema changes, (ii) prompt-based schema inclusion that fails to scale on large ontologies such as UCO, and (iii) reliance on enterprise LLM APIs that conflicts with privacy constraints when integrating sensitive internal incident data. In this paper, we present ANCHOR, a schema-agnostic CTI knowledge graph construction system that bridges LLMs and formal ontology schemas. At the core of ANCHOR is hybrid ontology discovery, a search-and-navigate mechanism that dynamically explores large-scale ontology schemas, combined with SHACL-based validation to enforce schema-compliant type assignments. Experimental results on the UCO, STIX, and MALOnt schemas show that ANCHOR outperforms existing baselines in ontology typing and schema compliance. In addition, ANCHOR with a local LLM closely matches enterprise LLM typing performance, enabling privacy-preserving CTI analysis with high fidelity.

---


### 320. [GPU Acceleration of Learning With Errors KEMs Using OpenACC for Post-Quantum Cryptography](https://arxiv.org/abs/2606.01211)

**<font color=#1a73e8>作者：</font>** Tiziana Liberati, Nitin Shukla, Matteo Barbieri 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Shor's algorithm proved that asymmetric cryptographic protocols based on the integer factorization and discrete logarithm problems are no longer safe in a world with large-scale quantum computers. As a result, Post-Quantum Cryptography (PQC) has been developed over the last few years, seeking cryptographic primitives resistant to quantum attacks. One of the main hard problems underlying PQC schemes is the Learning with Errors (LWE) problem, which is significantly more computationally intensive than its classical predecessors. In this work, we present a Key Encapsulation Mechanism (KEM) based on plain LWE and develop a GPU-oriented implementation using OpenACC. We evaluate the performance of our accelerated application in terms of both time-to-solution and energy-to-solution, considering bare-metal and containerized executions across multiple NVIDIA GPU models and generations. Our implementation achieves significant acceleration across all tested GPU platforms. In particular, on the NVIDIA Grace Hopper Superchip, it attains up to a $208\times$ speedup over a multithreaded CPU baseline and enables the execution of problem sizes that are impractical on CPU architectures due to memory and synchronization constraints. Energy consumption analysis also shows $\approx 2\times$ better efficiency when using the Superchip compared to systems equipped with x86-based CPUs and NVIDIA H100 GPUs. These results highlight the effectiveness of GPU acceleration for computationally demanding LWE-based cryptographic workloads.

---


### 321. [TECCI: Tricky Edits of Collected and Curated Images](https://arxiv.org/abs/2606.01213)

**<font color=#1a73e8>作者：</font>** Aishwarya Agrawal, Roy Hirsch, Yasumasa Onoe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite tremendous recent progress, current text-guided image editing methods still struggle with many aspects of editing involving instruction following, minimally editing the source image, and ensuring high visual quality. These problems are especially apparent when the requested edit is challenging, such as those that involve position, motion, viewpoint, scale and creative edits. To systematically test generative image editors, we propose a novel image editing benchmark -- TECCI: Tricky Edits of Collected and Curated Images. TECCI consists of a completely new set of images we are releasing. The images in TECCI span 7 image categories. The images and these categories were curated intentionally to target weaknesses of existing methods. The edit instructions in TECCI are automatically generated by Gemini, covering 5 edit types per source image. We also curated a set of 530 images for which we created challenging manually written edit instructions. Overall, TECCI contains 7550 pairs of images and edit instructions. We conduct human evaluations of five leading image editing models on TECCI. Humans judge outputs along three dimensions: 1) instruction following, 2) minimality of the edits, and 3) visual quality. To scale-up the evaluation, we also build an auto-rater using Gemini that achieves 74.7% accuracy in matching human evaluations. Our evaluations reveal that: 1) none of the models exceed a 22% overall success rate, demonstrating the challenging nature of TECCI, 2) Nano Banana Pro is the best performing model overall, 3) models perform significantly better at instruction following compared to minimal edits and visual quality, 4) models struggle with editing architecture and nature images which require strong understanding of spatial layout and intricate visual details. 5) reasoning and creative edits are the most difficult, whereas color and appearance edits are the easiest.

---


### 322. [Riemannian Optimization for Hadamard Products of Low-Rank Matrices](https://arxiv.org/abs/2606.01216)

**<font color=#1a73e8>作者：</font>** Pratik Jawanpuria, Ankish Chandresh, Bamdev Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The elementwise Hadamard product of two low-rank matrices provides a parameter-efficient model for data with multiplicative structure, but its modeling is challenging due to the presence of additional symmetries under coupled row/column scalings between the two factors. In order to leverage the geometry of the space, we formulate the learning of such matrices as optimization on a Riemannian quotient manifold. We propose a novel block-diagonal Riemannian metric derived from the pullback of the Frobenius inner product. The metric is shown to be invariant under the full symmetry group. We develop a Riemannian gradient descent algorithm that uses a tuning-free Gauss--Newton step size and scales linearly in the number of observed entries per iteration. Experiments on real and synthetic datasets illustrate the efficacy of our proposed Riemannian approach.

---


### 323. [Analysis of Ethnic Disparities in Autism Spectrum Disorder among Toddlers](https://arxiv.org/abs/2606.01217)

**<font color=#1a73e8>作者：</font>** Aadithya Prabha Ramaharsha, Deevna Reddy, Uma Ranjan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autism Spectrum Disorder (ASD) is a neurodevelopmental disorder characterized by challenges in communication and behavior. This study examines the relationship between ethnicity and ASD traits, along with behavioural scores, sex and neonatal jaundice across three ethnic groups: White Europeans, Asians, and Middle Eastern individuals. We perform a logistic regression and show that ethnicity has a significant effect on incidence of ASD. White Europeans are 81% increased risk of ASD and Middle Easterners are at 79\% reduced risk of ASD compared to Asians. We also confirm earlier studied which show that neonatal jaundice is a significant predictor of ASD, while male children are at much higher risk of ASD compared to female children. These results suggest the need for diagnostic frameworks and interventions that account for ethnic in the presentation and assessment of ASD traits

---


### 324. [Hybrid Imbalanced Regression Through Unified Data-Level and Algorithm-Level Balancing](https://arxiv.org/abs/2606.01221)

**<font color=#1a73e8>作者：</font>** Shermin Shahbazi, Hossein Mohammadi, Mohsen Afsharchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imbalanced learning is a critical challenge in machine learning, where underrepresented target values can bias models and degrade prediction performance on rare but important cases. Although extensively studied in classification, imbalanced regression remains relatively underexplored. Existing methods mainly focus on either data-level balancing, which may introduce noise and overfitting, or algorithm-level balancing, which often struggles with highly complex target distributions. To address these limitations, we propose a unified hybrid framework that integrates both data- and algorithm-level balancing strategies into a regressor-agnostic pipeline. The proposed framework consists of five stages: (1) adaptive bin partitioning to dynamically segment the target space based on local linear coherence; (2) target-conditioned representation learning using a Conditional Variational Autoencoder; (3) multistage data-level balancing through feature-space clustering and oversampling of minority clusters; (4) algorithm-level balancing using a novel Latent-Density Weighted Loss (LDWL) to emphasize rare samples in latent and target spaces; and (5) attention-based gated fusion for final regression. Experimental results on benchmark datasets demonstrate that the proposed framework consistently improves predictive performance compared to standalone regressors and existing imbalanced regression approaches.

---


### 325. [Connecting the Dots: Benchmarking Reflective Memory in Long-Horizon Dialogue](https://arxiv.org/abs/2606.01223)

**<font color=#1a73e8>作者：</font>** Jingjie Lin, Bingbing Wang, Zihan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite substantial progress in long-context modeling, existing benchmarks remain confined to factual memory for explicit recall, failing to measure the reflective memory required to synthesize fragmented, multimodal cues into high-level interpretations. To address this gap, we introduce RefMem-Bench, a benchmark for reflective memory in long-horizon dialogue. RefMem-Bench contains 26K annotated QA instances with eight reflective-memory dimensions and three task formats, requiring models to move beyond surface-level retrieval and infer latent meanings from evidence distributed across interaction histories. To enhance reflective memory capability, we propose REflective Memory INDuction (REMIND), a hierarchical framework that treats reflective memory as progressive meaning construction. REMIND couples question-conditioned evidence retrieval, salience-aware grounding, and abstraction-level supervision, and uses Progressive Reflective Alignment to distill high-level reflective reasoning into the factual inference pathway. Experiments show RefMem-Bench poses a substantial challenge to current models, while REMIND consistently improves both answer accuracy and memory recall through progressive evidence perception, grounding, and abstraction.

---


### 326. [Privacy-Preserving Smart Surveillance with Cross-Dataset Violence Detection and Decentralized Evidence Governance](https://arxiv.org/abs/2606.01225)

**<font color=#1a73e8>作者：</font>** Hasan Coşkun, Furkan Çolhak, Andrea Kulakov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-enabled surveillance can accelerate public-safety response, yet most systems still leave recorded evidence under centralized administrative control. This paper proposes a privacy-preserving smart surveillance framework that separates incident detection from evidence disclosure. A lightweight MobileNetV2-based video classifier detects violent clips, while each recorded incident segment is immediately encrypted and made accessible only through threshold-based approval. The decryption key is split with Shamir's Secret Sharing, member shares are protected with public-key cryptography, and voting is supported by time-limited tokens, two-factor authentication, signatures, and audit logs. This study evaluates MobileNetV2+LSTM, MobileNetV2+BiLSTM, and MobileNetV2+temporal CNN heads on SCVD, RWF-2000, and Real-Life Violence Situations under seven in-domain and cross-dataset scenarios. The best all-source model, MobileNetV2+BiLSTM, reaches 93.5% test accuracy and ROC-AUC 0.980% on the merged held-out set, while lower RWF-2000 slice performance confirms persistent dataset shift.

---


### 327. [DAGGER: Gradient-Free Construction of Transiently Amplifying Networks under Hard Connectivity Constraints](https://arxiv.org/abs/2606.01227)

**<font color=#1a73e8>作者：</font>** James C. Ferguson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many networks not only support but also rely on transient non-normal amplification, an orders-of-magnitude increase in the activity of an otherwise stable system. Constructing such networks under hard sign/sparsity/diagonal constraints -- the regime relevant for biological connectomes and structured RNN initializations -- has so far required either gradient-based local search with thousands of inner-loop eigendecompositions or Schur-form direct construction in an abstract basis that breaks the constraints under projection.
Here we introduce DAGGER (Directed Acyclic Graph Guided Edge Reweighting), a gradient-free single-pass algorithm. Given a stable signed sparse matrix, DAGGER produces an output with the same sign, sparsity, and diagonal. A single scalar $\beta$ controls a Wasserstein-2 budget that smoothly trades exact multiset preservation ($\beta = 0$) for amplification; peak amplification grows essentially without bound with $\beta$, empirically reaching $10^{10}$ before numerical overflow.
DAGGER matches or exceeds gradient-based methods at multiset preservation in a single forward pass -- 30-100$\times$ fewer eigendecompositions than a typical gradient inner loop -- and at moderate $\beta$ beats them by orders of magnitude with connectivity exactly preserved. We develop the algorithm, compare it to the existing methods and on a downstream signal-detection task, and examine the diagnostics that show why DAGGER is structurally different from other amplifying networks.

---


### 328. [Application of Algorithms in Energy-Efficient Design Platforms for Green Building](https://arxiv.org/abs/2606.01229)

**<font color=#1a73e8>作者：</font>** Na Yu, Fu Wenli, Guo Fei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> During green building design, computer-aided energy assessment is widely used to improve efficiency and achieve overall optimization. This paper presents a platform that combines Building Information Modeling (BIM), sensor operational data, and advanced simulation workflows using robust algorithms. The platform uses a multi-layer service architecture with dynamic energy simulation and evolutionary multi-objective optimization, connected via a high-performance C++ core and adaptive agent models. A mid-rise office building was selected as the case study. Five representative areas were chosen to collect data on building envelope characteristics and occupancy patterns. After preprocessing, missing sensor data accounted for 3.2% of annual records, and all variables were standardized using 15-minute interpolation. After 40 optimization rounds, annual energy consumption per square meter dropped by 29.3% from 315 kWh/m2 to 223 kWh/m2. The lifecycle cost increase for occupants was limited to 3.7%, and discomfort hours were reduced to under 70 hours per year. Analysis of Pareto optimal solutions shows that the envelope U-value ranges from 1.05 to 1.57 W/m2K, and nighttime ventilation rate ranges from 2.1 to 3.6 h-1, both closely linked to energy performance. The results confirm that the integrated algorithm framework offers good scalability, strong performance, and technical feasibility for green building design. This platform provides a reliable decision-support tool for design engineers and sustainability practitioners, enabling accurate, data-driven delivery of energy-efficient buildings.

---


### 329. [Unlocking the Black Box of Latent Reasoning: An Interpretability-Guided Approach to Intervention](https://arxiv.org/abs/2606.01243)

**<font color=#1a73e8>作者：</font>** Shuochen Chang, Tong Bai, Xiaofeng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent reasoning enables Large Language Models (LLMs) to perform multi-step inference within continuous hidden states, offering efficiency gains over explicit Chain-of-Thought (CoT). However, the opacity of these continuous thought vectors hinders their reliability and controllability. This paper bridges the gap between mechanistic interpretability and actionable control. We first present a systematic analysis using structural, causal, and geometric probes, revealing that latent vectors encode compressed, faithful representations of reasoning steps, with early vectors acting as critical causal hubs. Building on this, we operationalize these interpretability insights into a suite of training-free, decode-time interventions that refine the latent reasoning process by imposing the identified geometric and semantic priors. Extensive experiments across multiple model scales and diverse task domains demonstrate that our approaches consistently improve reasoning accuracy. Our interpretability-guided interventions consistently unlock latent capabilities and improve reasoning accuracy without any parameter updates.

---


### 330. [SIRIUS-SQL: Anchoring Multi-Candidate Text-to-SQL in Execution Feedback](https://arxiv.org/abs/2606.01246)

**<font color=#1a73e8>作者：</font>** Leo Luo, Haining Xie, Siqi Shen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL on complex schemas is unreliable on a single pass, so recent systems generate multiple SQL candidates and let voting filter out errors. Yet voting alone is not enough, because the multi-candidate recipe has three coupled weaknesses: 1) sampling more from a single generator produces increasingly redundant candidates, 2) existing pipelines apply one generic correction to every non-clean execution result, while runtime errors, timeouts, and empty results each indicate a different distance from correctness, and 3) existing selectors rely on a single angle such as result-majority voting or pairwise SQL comparison, missing what other angles would have caught. We present SIRIUS-SQL, which addresses all three weaknesses. A difficulty-smoothing RL recipe trains SIRIUS-32B to generate diverse executable SQL candidates, paired with a generalist LLM that fills in gaps left by the specialist. An execution-grounded lifecycle classifies each outcome and applies targeted repair before candidates re-enter the pool. A confidence-gated hybrid selector combines execution-result agreement with pairwise SQL-form judgment, escalating only near-tied cases to a deterministic structural check. SIRIUS-SQL reaches 75.88% on BIRD dev and 91.20% on SPIDER test. Two of three generalist pairings surpass Agentar-Scale-SQL, the strongest published multi-candidate system on BIRD dev.

---


### 331. [Beyond Sinusoids: A Morlet Wavelet Framework for Transformer Positional Encoding](https://arxiv.org/abs/2606.01258)

**<font color=#1a73e8>作者：</font>** Athanasios Zeris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard positional encodings for transformers - sinusoidal and rotary (RoPE) - treat every position as equally local: they encode where a token is, but not how far its positional influence should extend. We propose that the Morlet wavelet, which simultaneously minimises uncertainty in position and frequency, is the natural basis for positional encoding, and introduce Morlet Positional Encoding (MoPE): each embedding dimension learns its own frequency and locality bandwidth from data. The main theoretical result is a unification: sinusoidal PE and the RoPE correlation kernel both emerge as limiting cases of MoPE when locality is switched off (sigma_i -> infinity). The phase of MoPE recovers the RoPE rotation angle exactly; the amplitude adds a learned Gaussian locality kernel that standard encodings lack. Empirically, MoPE combined with Energy-Gated Attention achieves +0.119 improvement over standard attention on TinyShakespeare, outperforming either component alone. Analysis of the learned parameters reveals that all 128 frequency-bandwidth pairs converge to the wavelet admissibility boundary - an empirical observation consistent with a companion result on energy gating, suggesting a reproducible property of character-level language signals that warrants further investigation.

---


### 332. [PALTO: Physics-Informed Active Learning for Tri-Gate FinFET Design Optimization for Vertical Power Delivery](https://arxiv.org/abs/2606.01265)

**<font color=#1a73e8>作者：</font>** Ayoub Sadeghi, Leonid Popryho, Inna Partin-Vaisband  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper demonstrates the effectiveness of machine learning-driven optimization for designing application-specific GaN tri-gate FinFETs in vertical power delivery systems. Conventional TCAD-based approaches are computationally intensive and insufficient for navigating the high-dimensional, nonlinear design space of advanced GaN devices. To address this, a physics-informed active learning framework is used to intelligently guide simulations, accelerating convergence while preserving accuracy. This ML-guided approach enables the discovery of optimal configurations by efficiently exploring key structural parameters -- most notably the GaN-to-AlGaN thickness ratio -- a long-standing focus of debate in device design. By systematically exploring key structural parameters, two optimized devices with aggressively scaled gate-to-drain lengths are identified. Single-fin, multi-channel simulations show that device~D2, with a thinner GaN channel relative to the AlGaN barrier, achieves higher drive current. However, in a 300-fin configuration, device~D1 outperforms device~D2 by delivering 3.3\,A at 0.49~ohm on-resistance -- approximately 2$\times$ better -- despite slightly higher parasitics. Both devices operate in a normally-off mode. Based on an application-specific figure of merit, device~D1 achieves 5\,pC$\cdot$ohm, demonstrating 2$\times$ greater switching efficiency than device~D2, while both designs outperform industrial benchmarks from different performance standpoints.

---


### 333. [Emergent Ordinal Geometry in Transformers Trained on Local Comparisons](https://arxiv.org/abs/2606.01269)

**<font color=#1a73e8>作者：</font>** Nishit Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transitive inference is the challenge of inferring that A < C from knowing only adjacent relations (A < B, B < C). It is solved by humans and animals not through logical chaining but via an analogue mental number line, whose signature is the symbolic distance effect: distant comparisons are easier than nearby ones. We ask whether Transformers acquire the same primitive, training small models exclusively on adjacent comparisons from a hidden total order and evaluating generalization to unseen distant pairs. We find that out-of-distribution generalization emerges alongside a striking geometric reorganization: entity embeddings collapse onto a one-dimensional manifold whose principal axis recovers the hidden rank order with near-perfect fidelity, and this structure is sensitive to optimization in ways that produce grokking-like transient dynamics. Critically, even when accuracy is at ceiling, decision confidence and geometric separation both scale monotonically with rank distance, directly mirroring the symbolic distance effect observed across decades of behavioural experiments on humans, primates, and rodents. These results ground a 50-year-old behavioural regularity in the geometry of learned representations, offering a mechanistic account of transitive inference that bridges cognitive science and modern neural networks.

---


### 334. [Exploiting In-Sensor Computing for Energy-Efficient Earth Observation](https://arxiv.org/abs/2606.01271)

**<font color=#1a73e8>作者：</font>** Luigi Capogrosso, Pietro Bonazzi, Loris Hoxhaj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of the satellite industry has driven a significant increase in geospatial data acquisition, highlighting a critical bottleneck: the severe disparity between the volume of collected sensor data and the limited downlink bandwidth available to ground stations. While On-Board Computing (OBC) has helped address this by pre-processing data in orbit, this article further advances the paradigm by introducing an in-sensor computing framework. We present an optimized end-to-end Earth Observation (EO) pipeline tailored for strict computational constraints by integrating TinyML techniques with the Sony IMX500 Intelligent Vision Sensor. Specifically, our approach shifts processing directly to the sensor level, offloading the computation from the primary embedded device, and effectively mitigating the downlink transmission of noisy or irrelevant data. We evaluated several efficient Convolutional Neural Networks (ConvNets), i.e., SqueezeNet, ShuffleNetV2, and MCUNetV1, on the EuroSAT dataset. Experimental results show that, despite the optimizations required for deployment on the IMX500 platform, our models maintain a competitive 96.68% accuracy while operating within its 8 MB constraints. Specifically, the models reach an average processing throughput of 17.40 FPS with a latency of 27.43 ms. Furthermore, our system profile exhibits high energy efficiency, with a low energy footprint of 14.19 mJ per inference and an efficiency rating of 42.26 GMAC/J, demonstrating its viability for in-sensor deployment.

---


### 335. [GLIDE: Graph-guided Leap Inference for Diffusion Estimation of Spatio-Temporal Point Processes](https://arxiv.org/abs/2606.01273)

**<font color=#1a73e8>作者：</font>** Guanyu Zhou, Yao Liu, Yanglei Gan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal point processes (STPPs) provide a principled framework for modeling asynchronous events in continuous time and space. Recent diffusion-based approaches offer a flexible alternative to deterministic prediction by modeling complex conditional distributions, but their application to STPPs remains challenging: reverse sampling from pure noise is costly, and weak structural constraints in sparse spatial domains can lead to poorly localized probability mass. We propose \textbf{GLIDE} (Graph-guided Leap Inference for Diffusion Estimation), a conditional diffusion framework for next-event modeling in STPPs. GLIDE organizes historical events into a multi-scale historical graph and encodes temporal evolution and spatial topology through a dual-stream architecture, yielding a structured conditioning context for a dual-branch diffusion denoiser. It further introduces a prior-guided leap inference mechanism, in which a lightweight mean predictor provides a deterministic anchor and the reverse process starts from an intermediate diffusion step instead of from pure Gaussian noise. Experiments on multiple real-world datasets show that GLIDE improves both distribution fitting and next-event prediction, with the largest gains appearing on the spatial side. The results also indicate that prior-guided leap inference substantially reduces reverse-sampling cost while preserving the stochastic generation capability of diffusion models.

---


### 336. [Event-Based Vision in Space: Applications, Trends, and Future Directions](https://arxiv.org/abs/2606.01280)

**<font color=#1a73e8>作者：</font>** Luigi Capogrosso, Pietro Bonazzi, Michele Magno  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO) is undergoing a significant transformation driven by the deployment of novel sensing technologies. Traditional frame-based optical sensors often struggle with motion blur, high power consumption, and extreme data redundancy in challenging orbital environments. In contrast, event-based sensors, also known as neuromorphic cameras, offer a bio-inspired asynchronous approach. By capturing only local illumination changes, they provide microsecond temporal resolution, an extremely high dynamic range, and exceptional energy efficiency. Although the use of these sensors is rapidly expanding from terrestrial systems to orbital platforms, the scientific literature surrounding their space-based applications remains heavily fragmented. To bridge this gap, this article presents a comprehensive review of the state-of-the-art in event-based vision in the space domain. Based on the retrieved literature, we introduce a taxonomy structured around four primary domains: 1) atmospheric and high-speed observation; 2) environmental monitoring and change detection; 3) operational support and onboard processing; and 4) geospatial modeling and predictive analysis. As a result, this survey highlights that neuromorphic engineering is far more than a supplementary imaging technique; it is a paradigm shift that can be used to directly address critical bottlenecks in modern remote sensing and sustainable space exploration.

---


### 337. [KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Demographically Fair Text-to-Image Generation](https://arxiv.org/abs/2606.01282)

**<font color=#1a73e8>作者：</font>** Farbod Davoodi, Seyed Reza Tavakoli Shiyadeh, Pooria Safaei 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (TTI) systems are now everyday infrastructure for journalism, education, advertising, and public communication, and the demographic and cultural stereotypes they inherit from training data (rendering women, people of colour, older adults, and non-Western cultures as under-represented or caricatured) become a population-level harm at deployment scale. Existing mitigations either require costly retraining, infeasible for the closed-source backbones that dominate consumer products, or rely on fixed demographic templates that ignore cultural context. We present KG-FairDiff, a model-agnostic, inference-time framework that formalises fairness-aware prompt refinement as a constrained optimisation problem and operationalises it as a closed-loop pipeline: a knowledge graph of ~1,200 culture- and bias-related triples retrieves structured context, an LLM rewriter proposes refinements, and a validator accepts only prompts that reduce a divergence-based fairness loss while preserving semantic fidelity to the user's original intent. We prove a finite-termination bound for the refinement loop, contribute a mathematically consistent evaluation suite linking Bias-P/Bias-W to divergence from target distributions and ENS to KL divergence, and audit eight widely-deployed backbone generators. KG-FairDiff substantially reduces gender, race, age, and intersectional disparities while preserving prompt semantics, offering a practical, deployment-ready route to more equitable generative AI.

---


### 338. [AdaKernel: Learning Adaptive Kernel Parameters for Spatiotemporal Graph Neural Networks](https://arxiv.org/abs/2606.01283)

**<font color=#1a73e8>作者：</font>** Zhongyue Zhang, Guangyin Jin, Yuxuan Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling spatial dependencies is central to spatiotemporal data analysis using Graph Neural Networks (GNNs). Traditional methods rely on distance-based kernels with predefined parameters, which restricts model capacity. Although generic adaptive mechanisms (e.g., Graph Attention Networks) offer flexibility, they often fail to capture the underlying geometric structure, performing worse than distance-based models in data-sparse scenarios. Addressing this, we revisit the kernel parameterization problem and theoretically prove that misspecified kernel parameters introduce unavoidable approximation errors in GNNs. To overcome this, we propose AdaKernel, a simple yet effective approach that learns adaptive kernel parameters within the neural network. Unlike methods that learn graph structures from scratch, AdaKernel adopts a structure-preserving strategy that optimizes the scale of physical interactions rather than discarding them. Extensive experiments on Kriging, Imputation, and Forecasting demonstrate that AdaKernel consistently improves various GNN architectures and outperforms model-agnostic adaptive baselines, validating that accurately learned kernel parameters are superior to both fixed priors and fully latent graph structures.

---


### 339. [Knowledge-Intensive Video Generation](https://arxiv.org/abs/2606.01285)

**<font color=#1a73e8>作者：</font>** Chenxu Wang, Mingda Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video generation has advanced rapidly in visual quality, but remains under-evaluated for factuality and practical usefulness. We introduce knowledge-intensive video generation (KIVI), where models generate videos from short information-seeking prompts that ask for explanations, procedures, or demonstrations. To evaluate this setting, we construct KIVI-Bench, a benchmark of 1,080 prompts, and propose automatic metrics for factuality and helpfulness. Human evaluation shows that our metrics significantly better align with human annotations than existing alternatives. Experiments on seven state-of-the-art video generation models show that current systems still lag behind human performance, especially on visual properties, procedural operations, and clear information presentation. These results highlight KIVI as a challenging direction for factual and instructionally useful video generation.

---


### 340. [Beyond Visual Memory: Mechanistic Diagnostics of Latent Visual Reasoning](https://arxiv.org/abs/2606.01287)

**<font color=#1a73e8>作者：</font>** Garvin Guo, Yu Chen, Xiang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent latent visual reasoning methods achieve substantial gains by inserting continuous latent tokens into multimodal language models. These gains are commonly attributed to the tokens encoding visual evidence; recent analyses, however, reveal a paradox: the tokens are loosely tied to the image and contribute little to the answer. Critically, these analyses treat latent tokens as a single unit, obscuring the true source of the gains. We therefore decompose latent tokens into three testable components: latent slots, boundary markers, and format, and develop a state-of-the-art method as a probe under favorable conditions. Across six method-stage settings and four perception-heavy benchmarks, latent slots fail every prediction of the visual-memory account. Strikingly, retaining only the boundary markers preserves 78 to 100% of the gain in several settings, while the model attends to the image more narrowly at latent positions than at answer positions. The gain therefore comes from boundary markers, format, and this attention pattern, not from latent slots. How each method engages this mechanism depends on its training supervision: at matched accuracy, mechanisms can still differ markedly. Latent visual reasoning thus needs evaluation not only by accuracy but by what the model actually relies on.

---


### 341. [Feature to Dynamics: Feature-space to Autoregression strategy for Zero-shot Time Series Forecasting](https://arxiv.org/abs/2606.01289)

**<font color=#1a73e8>作者：</font>** Yifan Wu, Junjie Wu, Kai Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot time series forecasting aims to predict future values for previously unseen series, requiring models to generalize temporal dynamics beyond the training distribution. While recent foundation models achieve strong in-domain performance through large-scale pretraining, their effectiveness often relies on broad data coverage and implicit pattern memorization, which can limit generalization when data are scarce or source and target domains are disjoint. In this work, we propose FSA, a feature-to-strategy framework for controlled zero-shot univariate forecasting. Instead of directly modeling raw sequences in the observation space, FSA learns a structured mapping from an interpretable feature space to an autoregressive strategy space. This design introduces explicit inductive biases that disentangle global trends, periodic components, and local temporal dynamics, enabling the model to capture transferable time-series structure with fewer data assumptions. Empirical results show that, under identical pretraining data, training protocol, and comparable parameter budgets, FSA outperforms Transformer-based architectures in our controlled zero-shot setting.

---


### 342. [What Makes a Strong Model? A Unified Spectral Analysis of Knowledge Transfer over High-dimensional Linear Regression](https://arxiv.org/abs/2606.01292)

**<font color=#1a73e8>作者：</font>** Wendao Wu, Fangqing Zhang, Haihan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Teacher-Student Knowledge Transfer (KT) is ubiquitous in modern machine learning, ranging from classical model compression via Knowledge Distillation (KD) to the emergent phenomenon of Weak-to-Strong (W2S) generalization. While existing studies offer isolated insights, a unified theoretical framework explaining the efficacy of KT across these disparate regimes remains lacking. In this work, we establish a unified spectral analysis of SGD dynamics in high-dimensional linear regression, elucidating the efficiency of KT across seemingly disparate regimes. We characterize KT efficiency through two distinct mechanisms: \emph{Spectral Horizon Expansion} in KD, which enables the capture of statistically inaccessible high-frequency signals, and \emph{Spectral Denoising} in W2S, where the student acts as a filter for optimization noise. Our framework unifies these phenomena, revealing that the efficacy of transfer is governed by the interplay between implicit regularization and heterogeneous spectral learning speeds over the spectrum.

---


### 343. [Don't Read Everything: A Curvature-Conditioned Query for Linear Attention](https://arxiv.org/abs/2606.01294)

**<font color=#1a73e8>作者：</font>** Dong Le, Thong Nguyen, Cong-Duy Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear attention reduces the quadratic cost of softmax attention by maintaining a recurrent fast-weight state, but it consistently lags on in-context retrieval and long-context tasks. Existing remedies act on the write side of memory through gating, delta updates, or kernel feature maps, but the read step is left unchanged: every past key contributes additively to the output, so useful targets are diluted by the bulk of stored vectors. We borrow one specific piece of softmax's geometry to construct a cheap read-time contraction of the query. A second-order Taylor expansion of the softmax log-partition at the isotropic-attention point gives a local quadratic model whose curvature coincides with the running key covariance, a quantity that can be maintained with the same recurrent/chunkwise mechanism as the linear-attention state. The associated linear operator contracts the query along the high-density directions of memory before it reads the state. We call this mechanism Curvature-Conditioned Query (CCQ). CCQ modifies only the read step and is composable with any linear-attention backbone. Attached to GLA and Gated DeltaNet, it improves perplexity, zero-shot downstream accuracy, S-NIAH retrieval at and beyond the training context, length-extrapolation perplexity from 4K to 20K, and LongBench accuracy, at small extra cost.

---


### 344. [Challenger at MultiPRIDE: Is It Hate Speech or Reclaimed?](https://arxiv.org/abs/2606.01298)

**<font color=#1a73e8>作者：</font>** Hadi Bayrami Asl Tekanlou, Mahdi Bakhtiyarzadeh, Jafar Razmara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The spread of hate speech has become increasingly harmful in modern digital environments, particularly on social networking platforms. While recent advances have shown promising results in automatic hate speech detection, a key challenge remains: distinguishing genuine hate speech from reclaimed language. Accurate labeling is difficult due to the nuanced and context-dependent nature of reclaimed expressions. In this paper, we present a simple and interpretable approach for distinguishing hate speech from reclaimed language, developed for the MultiPride Shared Task. Our method generates dense semantic text embeddings and incorporates a label-noise filtering stage using Cleanlab with logistic regression, followed by a Multi-layer Perceptron (MLP) neural network for final classification. The system is designed to operate under limited computational resources while maintaining strong performance. We evaluate our approach using precision, recall, and F1-score, including macro-averaged metrics. Experimental results demonstrate robust performance despite extreme class imbalance in the dataset. Overall, the findings highlight the potential for further improvements through larger embedding models and more advanced preprocessing techniques while preserving interpretability.

---


### 345. [Structure and Scale in Simplicial Sequence Modelling](https://arxiv.org/abs/2606.01302)

**<font color=#1a73e8>作者：</font>** Matthew Farrugia-Roberts  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large-scale deep learning exhibits two striking empirical phenomena: behavioural scaling laws (predictable performance gains with increasing scale) and emergent mechanisms (structured internal representations and circuits in deep neural networks). We hypothesise that these two phenomena are connected: that predictable changes in behaviour are the result of predictable changes in internal computational structure. In this paper, we report preliminary evidence of such a connection. We find a correlation between scaling patterns in performance and representations in small transformers trained to predict the outputs of a hidden Markov model, for which residual activations are known to linearly encode a belief distribution over latent states in a probability simplex.

---


### 346. [When Hard Negatives Hurt: Bridging the Generative-Discriminative Gap in Hard Negative Synthesis for Retrieval](https://arxiv.org/abs/2606.01304)

**<font color=#1a73e8>作者：</font>** Zhicheng Zhang, Jiwei Tang, Kuicai Dong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hard negative mining has become the dominant strategy for training retrievers, yet it faces intrinsic limitations: negatives are bounded by corpus availability, selected by retriever score rather than diagnostic value, and increasingly contaminated by false positives as the retriever improves. LLM-based synthesis offers a principled alternative, where negatives that are unconstrained, targeted, and free from false positive risk. But we show that naively incorporating generated negatives into contrastive learning often degrades retrieval performance. We identify and formalize the root cause as a generative-discriminative gap: LLM generation optimizes for fluent, plausible text, while contrastive learning demands strategic violations of relevance at the decision boundary. Our analysis reveals two compounding failure modes: discriminative-agnostic generation, where the LLM lacks an explicit model of query information needs and defaults to generic or topic-drifted text that provides no contrastive signal; and source-dependent shortcuts, where distributional artifacts enable the model to distinguish negatives by origin rather than relevance, causing gradient drift that actively corrupts optimization. To close this gap, we propose CausalNeg consisting of two main modules: (1) CoT-guided counterfactual perturbation for data construction: decomposes why a document satisfies a query into explicit information requirements, then surgically violates individual requirements to construct negatives with controlled, interpretable hardness. (2) Query-view entropy maximization during training: disperses generated negatives across the similarity spectrum, minimizing the mutual information between source identity and similarity scores to suppress shortcut exploitation. We make our code publicly available at this https URL.

---


### 347. [FAiT: Frequency-Aware Inverted Transformer for Multivariate Time Series Forecasting](https://arxiv.org/abs/2606.01306)

**<font color=#1a73e8>作者：</font>** Peng He, Yao Liu, Yanglei Gan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Transformer-based architectures have established themselves as a dominant paradigm in Multivariate Time Series Forecasting (MTSF), their core self-attention mechanism inherently functions as a low-pass filter, systematically smoothing out high-frequency signals vital for sharp local changes. Recent advancements have increasingly incorporated frequency-domain operations to address this bias, however, most existing designs rely on fixed spectral bases and apply sequence-wise (uniform) modulation, implicitly assuming a time-invariant frequency response. This overlooks a key property of real-world series that their spectral characteristics often evolve over time, making uniform modulation insufficient for capturing fine-grained temporal dynamics. To tackle these limitations, we propose FAiT, a Frequency-Aware inverted Transformer. Specifically, FAiT rectifies the spectral bias internally through Inverted Attention, which interprets the attention map as a learnable low-pass operator and constructs a dedicated complementary high-pass branch by inverting the attention matrix to recover attenuated transient signals. Furthermore, FAiT introduces Dynamic Temporal-Frequency Modulation (DTFM), which synthesizes instance-conditioned weights to adaptively re-calibrate the energy of spectral sub-bands, enabling fine-grained control over evolving multi-scale patterns. Extensive experiments on widely used benchmarks demonstrate that FAiT consistently outperforms state-of-the-art Transformer-based and frequency-enhanced baselines, while maintaining computational efficiency.

---


### 348. [SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems](https://arxiv.org/abs/2606.01314)

**<font color=#1a73e8>作者：</font>** Yangbo Wei, Zhen Huang, Shaoqiang Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent self-evolving agents have shown that skills can be discovered, refined, and accumulated through execution. However, existing skill-evolution frameworks typically assume a fixed tool layer and evaluate each skill independently, limiting their ability to repair tool-level failures or reason about interactions among skills. We propose SkillSmith, a synergy-aware skill-tool co-evolution framework. SkillSmith introduces a unified proposal space in which reflection produces atomic bundles that jointly modify skills and tools, allowing tools to be wrapped, edited, composed, split, or retired when skill evolution identifies a reusable capability gap. To guide this joint search, SkillSmith maintains an ecological utility model inspired by Lotka-Volterra dynamics, where an interaction matrix estimated from execution traces captures pairwise complementarity and conflict among skills and provides pressure signals for retrieval, mutation prioritization, and retirement. Furthermore, SkillSmith records anti-patterns, including failure signatures, causal attributions, and remedies, to accelerate diagnosis and veto proposals that repeat known mistakes. Experiments on three benchmarks, including WildClawBench, and five Qwen3.5 model scales show that SkillSmith consistently outperforms strong baselines, with gains that amplify as task complexity and multi-skill co-activation increase.

---


### 349. [DeblurNVS: Geometric Latent Diffusion for Novel View Synthesis from Sparse Motion-Blurred Images](https://arxiv.org/abs/2606.01315)

**<font color=#1a73e8>作者：</font>** Changyue Shi, Wangbo Yu, Chaoran Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis (NVS) is a fundamental problem in computer vision and graphics. Recent advances in neural radiance fields (NeRF), 3D Gaussian Splatting (3DGS), and generative view synthesis have substantially improved its quality. Yet most methods still rely on clean observations, where image structures and cross-view geometric cues are well preserved. Motion blur breaks this assumption by corrupting local details and weakening multi-view correspondences. Such blur commonly arises from camera shake, scene motion, or finite exposure in practical capture. Blur-aware NVS methods address this degradation by modeling image formation, but their reliance on costly per-scene optimization limits efficient and generalizable sparse-view synthesis. To address this, we propose DeblurNVS, a novel framework for synthesizing high-fidelity novel views directly from sparse motion-blurred images, without requiring per-scene optimization. DeblurNVS restores the intermediate geometric representations needed for multi-view reasoning, enabling blurred inputs to recover reliable structure and correspondence cues. The restored representations are then combined with target camera information to synthesize the target-view representation and reconstruct a sharp RGB novel view. To enable the large-scale training, we construct a motion-blurred NVS dataset from DL3DV-10K using interpolation-based finite-exposure blur synthesis. Extensive experiments demonstrate that DeblurNVS outperforms existing baselines on synthetic motion-blur benchmarks and generalizes to real motion-blurred scenes, producing perceptually sharper and structurally more stable novel views while avoiding costly per-scene optimization. Project page: this https URL.

---


### 350. [Science Earth: Towards A Planet-Scale Operating System for AI-Native Scientific Discovery](https://arxiv.org/abs/2606.01316)

**<font color=#1a73e8>作者：</font>** Zhe Zhao, Haibin Wen, Yingcheng Wu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery demands intelligence, perseverance, and serendipity
across vast search spaces. Today, top scientific capabilities remain
siloed--one AI system for biological analysis, another for clinical
reasoning, mathematical derivation, or materials simulation--and no
pre-designed team can anticipate every skill a question will need.
Science Earth is a planet-scale scientific runtime in which any
capability--a simulation cluster, a wet-lab robot, a proof engine, a
single-cell pipeline--can connect to any other, with collaboration
structure emerging from the question itself. Its underlying EACN protocol
lets capabilities discover one another, negotiate task ownership, and
adjudicate across incompatible evidentiary standards without prior
knowledge of who will meet whom. This shifts the organizing challenge from
workflow design to open-ended connectivity. Two runs validate this under
structurally distinct conditions. In a trans-Pacific higher-order Kuramoto
synchronization study, agents identified and corrected a closure-ratio
assumption in Ott-Antonsen analytic theory that fails outside the
Lorentzian limit, within thirty minutes. In an eight-agent single-cell run
on the 4.88M-cell Kang 2024 pan-cancer atlas, heterogeneous capabilities
coupled over a 64.9-hour window with one structural external instruction,
producing three new result layers and anchoring findings against an
independent wet-lab study on an adjacent CCR8- TIGIT+ Treg subset. These
cases are a first empirical reading, not a benchmark sweep. They show that
when AI capabilities are truly connectable and coordination emerges from
the problem, scientific reasoning becomes a distributed, self-correcting
process--a step towards scaling AI-native discovery to the planet.

---


> [!TIP]
> 当前位于：**301-350**（第 7/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
