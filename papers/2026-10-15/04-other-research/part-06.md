# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 251. [Scalable Robust MCTS with Anytime Deterministic Optimality Guarantees](https://arxiv.org/abs/2610.15461)

**<font color=#1a73e8>作者：</font>** Tomer Massas, Vadim Indelman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> MDP planners often rely on nominal transition models that may differ from the true dynamics. Robust MDP planning accounts for this uncertainty through a set of admissible models, but doing so with limited online computation is challenging: the search tree grows exponentially with the horizon and each robust backup requires an additional optimization. Existing online robust methods remain limited in scale and offer at most probabilistic guarantees. We introduce, to the best of our knowledge, the first deterministic anytime guarantees for robust online MDP planning. We restrict computation to the sampled search tree while deterministically bounding the contribution of unsampled trajectories. For any fixed policy, we derive lower and upper bounds on the gap between its projected and true robust values under rectangular and non-rectangular uncertainty sets. Under rectangular uncertainty, we propagate these bounds through the robust Bellman operator to bound the optimal robust value. These bounds are computable from the current sampled tree, hold at every node, tighten as the sampled support expands, and converge to the robust values as full support is recovered. We develop CAR-MCTS, a bound-guided MCTS planner that uses these deterministic bounds to guide exploration, prune provably suboptimal branches, and terminate once the optimal root action is certified. The fixed-policy bounds also yield an anytime policy-evaluation mechanism that certifies the robust value of any policy, independent of how it was obtained. Experiments verify the deterministic bounds, their tightening under support expansion, substantial branch pruning, root-action certification, and convergence to the optimal robust policy. To our knowledge, this is the first scalable robust MCTS framework with anytime deterministic guarantees for both online planning and policy evaluation, without enumerating the full state space.

---


### 252. [Concept Representations in Vector Space: Quantifying Sharedness and Idiosyncrasy of Meaning](https://arxiv.org/abs/2610.15496)

**<font color=#1a73e8>作者：</font>** Simon Josef Durstewitz, Denis Buehler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Concepts are the basic units through which we navigate the world and communicate meaning. But do you and I really mean the same thing when we think or speak about a concept? The present study develops a measurement framework for modeling and analyzing interindividual variation in concept representations through sentence embeddings, dense vector representations mapping entire utterances into a shared geometric space. The framework is developed in a theoretical argument and validated, demonstrated, and subjected to robustness checks in a pre-registered study. Short personal definitions, elicited from $N = 125$ participants, are encoded as sentence embeddings and submitted pairwise to a crossed random effects model yielding two concept-level quantities: sharedness ($S_b$), the expected dissimilarity between two randomly drawn individuals, and idiosyncrasy ($I_b$), the person-specific share of total dyadic variance. Two validity tests support the approach: the embedding space fully recovers concept and domain organization from participant definitions even with the target word excluded, and a parameter-free classifier achieves 0.630 accuracy in a within-participant extensional prediction task against a chance baseline of 0.500 and a consistency ceiling of 0.893. The framework finds theoretically interpretable variation in $S_b$ and establishes $I_b$ as a reliable source of dyadic variance across concepts. Results replicate across three encoders varying in architecture and capacity, providing a reproducible and scalable instrument for the empirical study of meaning variation.

---


### 253. [Revisited Support Vector Machines: A Unified Joint Optimization Framework with Nyström Approximation for Scalable Adaptive Learning](https://arxiv.org/abs/2610.15498)

**<font color=#1a73e8>作者：</font>** Nassou Gongon Benjamin, Noulapeu Ngaffo, Patrick Njionou Sadjang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The theoretical elegance of Support Vector Machines (SVMs), grounded in statistical learning theory, establishes them as a reference for robust classification. However, in the era of Big Data, classical SVMs face two major bottlenecks: the prohibitive cubic complexity $\mathcal{O}(N^3)$ of training and the rigidity of static kernels. Traditional methodologies treat kernel selection as a discrete, "brute-force" GridSearch problem, effectively decoupling the learning of data representation from the optimization of the decision boundary. This paper proposes a paradigm shift with a so-called "Revisited SVM", a unified framework that recasts the learning process as a continuous %bi-level joint optimization problem. We derive a novel objective function $J(\alpha, \theta)$ that allows for the simultaneous optimization of dual Lagrange multipliers and kernel hyper-parameters. To solve this challenging non-convex problem efficiently, we introduce a hybrid Block Coordinate Ascent (BCA) algorithm, tightly integrated with Nyström-based low-rank approximation, which drastically reduces computational complexity to $\mathcal{O}(Nm)$. Extensive experiments conducted across four heterogeneous domains (Bioinformatics, Finance, Cybersecurity, and Computer Vision) demonstrate that our approach not only matches but often exceeds exhaustive GridSearch accuracy, while delivering training speedups of up to 100x. Notably, on the complex NSL-KDD intrusion detection dataset, our adaptive kernel approach achieves 96.25\% accuracy compared to a mere 50\% for standard baselines, proving its unique ability to model complex non-linear manifolds in high-dimensional spaces. We validate our results using rigorous statistical tests and provide a theoretical convergence analysis of the proposed algorithm.

---


### 254. [From Observations to Authorized Actions: Measuring Source Information in Android Agents](https://arxiv.org/abs/2610.15502)

**<font color=#1a73e8>作者：</font>** Hyobin Ahn, Dongjae Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android agents read content from applications and web pages and act on it with the user's authority, yet they cannot reliably tell where that content came from -- its source, the application or document that supplied it. The WebView accessibility fields we inspected expose the host application but omit the document origins available inside the browser, so an agent reading through this interface cannot check which document supplied an object; a limited reproduction on an unmodified WebView yields the same finding. We build and separately evaluate two prototypes to examine how source information supports authorization. Our application-source monitor withholds side-effecting calls whose signed source record contains an untrusted application. With the source set derived from the OS accessibility log, it blocked every selected attack write in the tested runs, but it also withheld benign sends issued after reading untrusted content, flagged benign tasks that use external content, and carried source records into a later clean task. Our WebView source-reference gate uses records from a modified browser to check object origins and reference lifetime through direct calls; in a separate 24-trial evaluation, the live agent selected no disallowed object. Supporting benchmark and planner measurements characterize textual argument matches and attacker-target selection, without establishing causal dataflow or a controlled model ranking. The prototypes are not an integrated defense: the WebView gate still lacks authenticated browser delivery and atomic capture of selected bytes and origin. Together, the results show which source information the tested policies need and why it must stay linked to the object used in execution.

---


### 255. [Data Portability Revisited: Toward the Human-Centric, AI-Driven Data Ecosystems of Tomorrow](https://arxiv.org/abs/2610.15503)

**<font color=#1a73e8>作者：</font>** Mark Fenwick, Michael Fertik, Paulius Jurcys 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This Article critically examines the contemporary regulatory framework and discourse surrounding data portability in the United States. Using recent regulatory developments in the European Union as an illustration, this Article suggests that although data access and portability are identified as vital issues in multiple policy instruments, in its current iteration, at least, legal conceptions of portability continue to reinforce the interests of service providers and data controller enterprises rather than individual end users. This Article argues that a paradigm shift toward a more human-centric data approach to data governance must occur, under which data would be recognized as fundamental to an individual's identity in a digital age. Therefore, it should be placed in the hands of individuals rather than service providers or data controller enterprises. This Article considers technical and market trends in the European Union that reveal and facilitate such a change. It suggests that regulatory frameworks should better align with these technological and market developments to encourage change-inducing trends among market actors. In short, this Article identifies a transformative approach to data portability that empowers individuals with the freedom and ability to aggregate their data in secure personal spaces under their control or dominion. Such a human-centric perspective on data portability is crucial in building Artificial Intelligence (AI)-powered applications for individual consumers that can pave the way for the human-centric, AI-driven data ecosystems of the future.

---


### 256. [Structured Stateful Relational Scripts with a High-Quality Dataset for Multi-Shot Audio-Visual Video Generation](https://arxiv.org/abs/2610.15512)

**<font color=#1a73e8>作者：</font>** Chen Zhao, Lehan Shen, Qilong Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coherent multi-shot audio-visual video generation requires maintaining consistent identities while depicting evolving states and coordinating sounds across shot boundaries. Although dense captions describe individual shots in detail, they rarely specify which entities persist, how their states change, or which entities and actions produce sounds. To address this limitation, we propose Structured Stateful Relational Scripts (SSRS), a textual supervision representation that separates persistent entity and voice identities from shot-specific visual and auditory states. SSRS explicitly encodes sound-source bindings and temporal relations, while a global audio-visual event sequence connects local actions and sounds, including events that continue across shot boundaries. We further introduce MSAV-Script-100K, a large-scale dataset of curated multi-shot audio-visual videos paired with detailed SSRS annotations, enabling models to learn identity persistence, state transitions, and event continuity from structured supervision. Experiments demonstrate improvements in cross-shot consistency, adherence to specified state changes, and audio-visual alignment, highlighting the effectiveness of our SSRS and MSAV-Script-100K for coherent multi-shot audio-visual generation. Our proposed dataset is available at \href{this https URL}{MSAV-Script-100K}.

---


### 257. [Semantically Steerable Image Tokenization](https://arxiv.org/abs/2610.15515)

**<font color=#1a73e8>作者：</font>** Danilo de Goede, Mohammad Mahdi Derakhshani, Yuki M. Asano 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adaptive image tokenizers compress an image into a variable number of tokens matched to its complexity, and recent work makes this allocation controllable: conditioned on a target reconstruction error, the tokenizer itself decides how many tokens an image needs. However, the fidelity measure guiding this allocation shapes which aspects of the image are preserved under compression. The pixel-wise error used in prior work is blind to the spatial structure that carries an image's meaning, and under heavy compression such tokenizers are prone to abruptly discarding tokens that encode essential content. We introduce GIST (Guided Image Semantic Tokenizer), an adaptive tokenizer that can be steered toward a requested semantic fidelity. Its token allocation is jointly controlled by pixel-level and semantic target errors, with semantic error measured in the feature space of a frozen DINOv3 encoder. This joint control enables semantic protection: with the semantic target fixed at zero, the reconstruction target can be relaxed to discard pixel detail while preserving what the image depicts. In a controlled comparison on ImageNet-100, GIST outperforms its pixel-controlled counterpart KARL at every token count, with up to $30\%$ lower LPIPS and $37\%$ lower DreamSim. On average, lowering its semantic target reduces LPIPS $2\times$ faster per token than lowering the reconstruction target, and up to $5\times$ in the low-token regime. Semantic fidelity is thus an effective control signal for adaptive tokenization: it lets a tokenizer see, and so preserve, what an image depicts.

---


### 258. [OceanFlow: Coherent Flow Matching for Probabilistic Ocean Modeling](https://arxiv.org/abs/2610.15518)

**<font color=#1a73e8>作者：</font>** Yuan Gao, Fan Xu, Hao Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic ocean modeling is essential for risk-aware marine operations, climate analysis, and scientific decision-making, where downstream decisions depend on the conditional distribution of future ocean states rather than a single deterministic trajectory. Recent data-driven ocean models have made deterministic global ocean modeling increasingly accurate and efficient, but probabilistic ocean modeling remains underdeveloped. Specifically, perturbation-driven ensembles can create spread without explicitly optimizing the joint distribution of their members, often yielding poor calibration and physical inconsistency. To address these issues, we propose OceanFlow, a coherent flow matching framework for probabilistic global ocean modeling. OceanFlow first establishes a sharp, stable mean anchor for the conditional ensemble. Flow matching then learns a coherent state-conditioned pathwise law that jointly reshapes the residual distribution around this anchor at each transition, preserving the predictive center while refining state-dependent uncertainty. We further introduce a Factorized Dynamics Operator (FDO), which combines factorized transitions with a learned state-conditioned response to parameterize the mean anchor and residual-flow velocity. Extensive experiments show that OceanFlow improves ensemble-mean accuracy, probabilistic reliability, and physical-consistency diagnostics over competitive baselines, supporting coherent flow matching as an effective route toward data-driven probabilistic ocean modeling. Code is available at this https URL.

---


### 259. [UMAS3D: Unified Mask-Free 3D Editing with Region-Adaptive Source Preservation](https://arxiv.org/abs/2610.15533)

**<font color=#1a73e8>作者：</font>** Xianlin Zeng, Xiaolong Shen, Ruijie Quan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D editing aims to modify an existing 3D asset according to user intent while preserving geometry and appearance outside the intended edit region. Existing methods often rely on task-specific training, source-3D inversion, or external 3D masks, and lack a unified framework for diverse editing conditions and tasks. We propose UMAS3D, a unified 3D editing framework that is training-free, inversion-free, and free from external 3D masks. UMAS3D converts text, bounding boxes, reference images, and their combinations into common target-view guidance, after which addition, deletion, modification, appearance, and pose editing share the same downstream 3D generation process. Our key insight is to couple online edit-region estimation with region-aware source preservation. Mask-Free Adaptive Region Modeling (MARM) initializes an Edit/Keep prior from source-target visual differences and progressively refines it as the target structure evolves, while Source-Guided Preservation Steering (SGPS) constrains the current Keep-region states to retain source geometry and appearance without suppressing target-driven changes. Experiments show that UMAS3D supports addition, deletion, modification, appearance, and pose editing while effectively preserving unedited source content. These advances make UMAS3D a unified framework for flexible and source-preserving 3D editing across diverse editing conditions.

---


### 260. [Poisoned into Action: Context Attacks on Typed Decision Workflows](https://arxiv.org/abs/2610.15537)

**<font color=#1a73e8>作者：</font>** Chenkai Wu, Xing Chang, Jun Yan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Typed decision interfaces restrict models to predefined actions, yet schema-valid choices can still trigger policy-violating state changes. Evaluating context poisoning thus requires connecting model decisions to execution outcomes while accounting for legitimate automation retained by defenses. We introduce an execution-aware protocol tracing poisoned evidence through retrieval, model choice, automated action, and persisted state. We evaluate it with 1,659 fresh calls to Jev-1.13.0 across 20 development tasks in two synthetic workflows, using three repetitions per condition. Under natural retrieval, a standalone payload reaches all 60 trials and produces five security-violating executions, while a carrier-payload pair exposes the payload in 57 trials and produces one violation. An initial source-exclusion gate blocks the pair's observed violation but also withholds ten otherwise correct attacked decisions and sixteen correct clean decisions. Correcting its empty-scope behavior restores twelve clean decisions without additional model calls. Factorial controls show that adding correct evidence reduces wrong executions from 119/120 to 55/120 in the semantic arm and from 60/120 to zero in the neutral arm, suggesting that much of the improvement reflects general evidence value rather than attack-specific protection. Three prespecified contrasts are not statistically supported after Holm correction, so the findings remain exploratory. The protocol provides an auditable framework for studying which poisoning-induced errors reach execution and how much correct automation defenses preserve. Code is available at this https URL.

---


### 261. [Sensitivity Fidelity Reveals Physical Dependencies Beyond Forecast Accuracy in Deep-Learning Earth-System Models](https://arxiv.org/abs/2610.15540)

**<font color=#1a73e8>作者：</font>** Qi Chen, Peng Zhan, Hongxing Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep-learning models increasingly rival numerical simulation in Earth-system forecasting, yet forecast error alone cannot determine whether their learned input-output dependencies are physically consistent. Here we introduce sensitivity fidelity as an additional criterion: alongside prediction error, model responses to input perturbations should be examined against a trusted reference or established physical knowledge. In an idealized Rayleigh-Bénard convection benchmark, four surrogate architectures achieved low forecast errors yet encoded markedly different sensitivities. Quantitative comparison with a matched adjoint distinguished the models far more sharply than forecast accuracy and showed that predictive skill and sensitivity fidelity need not coincide, while finite-perturbation experiments further linked these differences to the propagation of initial-condition uncertainty. We then applied this strategy to El Niño-Southern Oscillation prediction, where no adjoint reference exists and learned sensitivities showed event-wise robustness, validity under finite perturbations, and consistency with established precursors. These results identify gradient-based evaluation as a discriminating complement to forecast-error metrics, providing a practical test of whether data-driven Earth-system models learn physically credible dependencies.

---


### 262. [Fetch Me If You Can: A Comprehensive Analysis of Fetch Metadata](https://arxiv.org/abs/2610.15541)

**<font color=#1a73e8>作者：</font>** Pedro Bernardo, Alex Ploner, Marco Squarcina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Effective server-side defenses against cross-site attacks depend on understanding the context in which browser requests are generated. However, servers often lack the information needed to distinguish legitimate requests from potentially malicious cross-site interactions. Fetch Metadata, a security mechanism introduced in 2019, addresses this limitation by adding a set of HTTP headers to outgoing browser requests. These headers provide servers with information about a request's context and provenance, enabling them to enforce request isolation policies accordingly. However, the extent of Fetch Metadata's real-world adoption and its interaction with existing security mechanisms remain largely unexplored. In this paper, we present the first large-scale measurement study of Fetch Metadata adoption. We analyze the top 1M websites in the Tranco list to detect deployments of Fetch Metadata isolation policies and identify custom policies used in the wild. We then examine how these policies address cross-site threats and assess their security coverage. Finally, we provide the first systematic comparison of Fetch Metadata with existing client-side security mechanisms, revealing security gaps that arise from differences between client-side and server-side enforcement.

---


### 263. [An Interpretable Linguistically-Grounded Analysis of Scene Saliency in Movie Screenplays](https://arxiv.org/abs/2610.15544)

**<font color=#1a73e8>作者：</font>** Uday Bindal, Ishaan Karan, Manan Garg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the factors affecting salience in movie screenplay by posing two research questions: 1. {\em Does Uniform Information Density (UID) predict salient scenes?} 2. {\em What other linguistic properties distinguish salient scenes from non-salient background?} We answer both questions through a controlled corpus study on the MENSA corpus, paired with a Linguistically-Grounded Salience Model (LGSM), a dual-stream classifier that fuses a frozen BERT encoder with explicit linguistic features through adaptive gating. The UID picture is layered in long-form discourse. Per-scene UID summaries carry no independent signal once length is controlled, but at the token level salient scenes match non-salient material in the bulk while specifically suppressing the rarest, hardest-to-predict tokens in the upper tail. UID therefore lives at the within-scene token level rather than as a per-scene aggregate. Salient scenes also show a moderate and sustained cast of central characters (following an inverted-U pattern), strong third-person usage, syntactically simpler language, and more abstract vocabulary about motivation and conflict. LGSM exploits this signature and improves recall on salient scenes over a strong semantic baseline while yielding better downstream summaries.

---


### 264. [ELECT: Settling Identity Before Rendering for Scalable Story Visualization](https://arxiv.org/abs/2610.15555)

**<font color=#1a73e8>作者：</font>** Mehrajul Abadin Miraj, Md. Mahmudul Hasan, Meherun Farzana 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free story visualization without reference images must preserve recurring entities across frames while scaling to long narratives. Existing methods typically maintain consistency by conditioning each frame on other frames of the same story, coupling generation time, VRAM, or both to story length. We introduce ELECT, which instead settles cross-frame identity before final rendering through a language-guided scene-entity mapping and stationary anchors elected from the model's own drafts. This makes the per-frame cost of the final rendering pass independent of story length. Joint attention exceeds 96 GB of VRAM at 32 scenes, whereas ELECT remains at 8.3 s per frame and under 20 GB VRAM from 10 to 1000 scenes. On the Story50 long-story benchmark, ELECT reaches 0.833 average Character Consistency Similarity (aCCS), compared with 0.826 for ten-round refinement, at one seventh of its generation cost, with lower text alignment (0.327 vs. 0.340). At 1000 scenes, to our knowledge, the first evaluation of training-free story visualization at this length, ELECT exceeds ten-round refinement by 0.017 aCCS and the nearest flat-cost baseline by 0.091, while also surpassing refinement in text alignment at one twenty-fourth of its generation time. These results show that long-horizon consistency need not require increasingly expensive inter-frame conditioning as stories grow.

---


### 265. [A Plausible Future Is Not a Causal Future: Can Video Models Generate How the World Unfolds?](https://arxiv.org/abs/2610.15562)

**<font color=#1a73e8>作者：</font>** Jialiang Li, Zhengning Xu, Zongyang Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale video generation models are increasingly viewed as a promising path toward world models, yet their ability to capture causally coherent physical dynamics remains poorly understood. Existing evaluations largely emphasize visual quality, prompt adherence, or broad physical plausibility, leaving open whether a model can faithfully realize a complete causal cascade, in which an initiating event propagates through causally dependent interactions to a terminal outcome. We introduce CausalCascade, a simulator-grounded benchmark centered on 50 event-rich Blender scenes with structured event graphs, graph-grounded diagnostic VQA, three levels of future-event specification, and 2,832 controlled counterfactual variants, and use it to evaluate nine image-to-video models with complementary motion-, event-, and counterfactual-level diagnostics. Across the evaluated models, generated motion is more reliably localized spatially than realized with correct spatiotemporal evolution, while richer future-event specification improves event recovery but leaves physical realization limited. Counterfactual evaluation further reveals weak selective responsiveness to physical interventions, while most audited failures are foundational, arising at scene consistency or event occurrence. Together, these results position causal cascade generation as a process-level test of world modeling and highlight the need to jointly recover the intended future, faithfully realize its physical evolution, selectively respond to physical interventions, and maintain a coherent physical world over time. Code and dataset are available at this https URL .

---


### 266. [UNISON: A Unified Framework for Learning from Scored Bags](https://arxiv.org/abs/2610.15564)

**<font color=#1a73e8>作者：</font>** Ofek Kirshenboim, Or Shkuri, Shani Finkelshtein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce UNISON, a unified framework that bridges multiple instance learning and recommendation systems by treating both as instances of learning from scored bag collections of (item, score) pairs. Unlike traditional approaches that address bag-level classification and personalized recommendation as separate problems, UNISON decomposes learning into three interconnected stages: (1) learning universal item representations, (2) modeling bag-specific preference patterns through lightweight personalized parameters, and (3) inferring bag-level characteristics from learned preferences. We justify the architectural choice of linear bag-specific scoring through a first-order analysis: when item embeddings are sufficiently smooth in the score, a linear function approximates the score up to a Taylor remainder controlled by the curvature of the underlying preference function. For cold-start scenarios, we show that the cold-bag fitting problem reduces to ridge-less linear regression with a closed-form solution, and provide convergence guarantees for the iterative variant. Empirically, UNISON matches or outperforms state-of-the-art approaches across diverse domains: entertainment (books, movies), immunology (T cell receptor (TCR) based classification), and microbiome, offering superior computational efficiency and interpretability. A controlled synthetic experiment further confirms that the bag-specific parameters ($w_j, b_j$) recover the latent factors that drive item scores even when the projection $\phi$ has no access to the original scoring mechanism (AUC > 0.998). UNISON is available at this https URL.

---


### 267. [Truncation Samplers Are Nested: Comparing Decoding Rules Is a Measurement Problem](https://arxiv.org/abs/2610.15570)

**<font color=#1a73e8>作者：</font>** Rasul Khanbayov, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Settling one comparison between two truncation samplers has cost six thousand A100-hours, and nothing says in advance how far apart two samplers can be. We observe that almost every deployed truncation rule keeps a prefix of the probability-sorted vocabulary, so any two such rules are nested at every decoding step. Nesting yields a closed-form per-step distance and a coupling under which both samplers emit identical text until they first disagree. Accumulated over a generation, this gives a separation certificate that bounds the difference between two samplers on any bounded outcome, is computable from logs a comparison already produces, and equals their sequence-level total variation distance exactly when neither rule ever overtakes the other. Two consequences follow without measurement: exactness is fragile, and certifying a small difference requires the two retained masses to agree to very high precision at every step. On six open-weight models over four math and science benchmarks, the certificate for every hyperparameter grid we tested is at least 0.998, so a bound alone rarely settles a comparison, although two members of one family can be far closer. What remains useful is the coupling, which gives an unbiased paired estimator that cuts variance $1.2$-$3.8\times$ against prompt-level pairing. Read against benchmark sizes at the default pair's variance and our point estimate of its between-prompt component, resolving a one-point difference needs 8 to 32 samples per prompt on GSM8K, MATH-500 and GPQA-Diamond and about 210 on AIME 2025; at that component's upper confidence bound GPQA-Diamond needs more than 32 and AIME 2025 cannot be resolved at any sample count. Choosing a truncation sampler is a measurement problem at least as much as a design one. The code is available at this https URL.

---


### 268. [Self-Representation Alignment in Diffusion Models for Video Background Music Generation](https://arxiv.org/abs/2610.15575)

**<font color=#1a73e8>作者：</font>** Jincheng Zhang, György Fazekas, Charalampos Saitis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models have been widely used for various generative tasks. However, recent studies have demonstrated that the internal representations learned in the diffusion models' denoising process are insufficiently meaningful, which can hinder the generation performance. To address this, we propose a novel diffusion U-Net architecture enhanced by explicitly aligning the weaker representation from the earlier layer conditioned on higher noise with the better representation from the later layer conditioned on lower noise during training, which we use for the challenging multimodal task of video background music generation. Our diffusion U-Net Self-Representation Alignment (U-SRA) employs an alignment loss to effectively guide our diffusion model to learn good internal representations, thereby enabling it to produce higher-quality symbolic music conditioned on video features. We employ a cross-attention mechanism to synchronize music with video segments. Experiments on a benchmark video-music dataset demonstrate that the proposed U-SRA approach for video background music generation surpasses the state-of-the-art across key evaluation metrics, including video-music alignment and overall music quality.

---


### 269. [Ellipsoids from Tangents](https://arxiv.org/abs/2610.15580)

**<font color=#1a73e8>作者：</font>** Efrat Dahan, Michael Werman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an algorithm for detecting and fitting multiple ellipsoids in 2D, 3D and higher-dimensional data. The representation is based on tangents to the ellipsoid together with their contact points, rather than on points alone. A tangent contributes d independent equations where a point contributes one, so each hypothesis needs fewer samples, which in turn reduces the number of iterations required to recover every ellipsoid. The problem is posed as sets of linear equations whose solutions -- the ellipsoid parameters -- are recovered robustly by clustering in parameter space. The algorithm works in all dimensions and outperforms the state of the art in 2D. The approach applies in general to the robust solution of linear equations, and so has utility beyond ellipsoid fitting.

---


### 270. [Inverse Garment Design with Visual Agents](https://arxiv.org/abs/2610.15582)

**<font color=#1a73e8>作者：</font>** Nanxiang Jiang, Yunuo Chen, Zeng Tao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the problem of inverse garment design, reconstructing simulation-ready 3D outfits with arbitrary layers from a single image, with visual agents. Unlike differentiable optimization that is time-consuming, or feed-forward methods limited by training data, we introduce DressAgent, a hierarchical agentic system that recovers garment sewing patterns through planning and closed-loop refinement grounded in physical simulation. To this end, we first present an enhanced representation based on GarmentCode for diverse styles and arbitrary dressing layers, and build the first multi-layer sewing pattern dataset with over 15K outfits for supervision and benchmarking. Inverse design then proceeds coarse to fine: In layer planning and coarse estimation, agents infer layer order and relations, peel each layer into its own view, and estimate coarse patterns. In fine-grained refinement, an agentic trio of Tailor, Critic, and Orchestrator refines patterns in a closed loop of editing, simulating, and judging against the reference with visual and measured evidence. Carefully designed tools and an evolving memory make this refinement converge on the target geometry. We also design an agentic generation method for high-fidelity textures. DressAgent outperforms feed-forward methods by a large margin, surpasses or matches differentiable optimization in a fraction of the time, and generalizes to complex layering, diverse poses, and body shapes.

---


### 271. [The Gradient That Top-k Distillation Never Computes](https://arxiv.org/abs/2610.15589)

**<font color=#1a73e8>作者：</font>** Rasul Khanbayov, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many deployed distillation pipelines show the student a truncated view of the teacher: keep the top-k probabilities, renormalize, and minimize a divergence on what remains. Renormalization is assumed to account for the missing mass. We prove that it removes the visibility of tail mass, not the freedom to move it. The renormalized objective depends only on log-odds among the retained tokens, so at each position its gradient along the directions that control tail mass is exactly zero; on a real teacher that component measures $2$-$3\times10^{-15}$ of the gradient. The full-vocabulary gradient equals the truncated gradient plus a residual weighted by the tail masses, and training acts only on the first term. Without the cross-entropy term, a top-k student's tail mass drifts away from the teacher's while a full-vocabulary control moves slightly toward it; with it, the gap shrinks about fourfold but persists. On seven open-weight teachers, the retained set determines the teacher's distribution only from $k=d+1$ ($d$ the hidden dimension): recovery is exact from there on all seven, and commonly cached sizes sit below it. In our off-policy runs the practical effect is real but smaller than the choice of teacher-student pair. Renormalization is a normalization, not a safeguard. The code is available at this https URL.

---


### 272. [An Attention-Guided Graph Neural Network Surrogate for Boundary Integral Computation in Physical Field Reconstruction](https://arxiv.org/abs/2610.15590)

**<font color=#1a73e8>作者：</font>** RongZe Gao, YuWei Wu, XinRan Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In practical engineering and scientific computing, a real physical system can be reduced to a boundary value problem, and the adequate boundary information to determine the interior spatial distribution and evolutionary state of the physical field can be solved with linear equations, alternatively, the the real physical problem can be treated with boundary problems with in adequate information problems in field of machine learning. This paper proposes a deep learning framework for the recovery of missing boundary information using an attention-guided graph neural network (GNN) surrogate. The framework extracts features from the physical information on the discretized boundary into a latent space, and the missing boundary quantities are then predicted by the network. Thus, the nonlinear mapping from known boundary quantities to missing boundary quantities is learned using a variational autoencoder (VAE) architecture, while an attention mechanism is incorporated to better model the correlations among different types of boundary information. Furthermore, the interior physical field can be reconstructed using the conventional boundary element method (BEM) integral formulation. The effectiveness of the GNN-BEM framework is evaluated using numerical examples of the two-dimensional Laplace and Poisson equations, which demonstrate good performance in reconstruction accuracy, local detail preservation, and model stability. The results show that GNN-BEM provides a feasible computational framework for boundary information recovery and fast interior physical field reconstruction for partial differential equations under complex boundary conditions.

---


### 273. [FireNav: Decision-Oriented Reconstruction Evidence Routing for Vision-Language Navigation in Indoor Fire Environments](https://arxiv.org/abs/2610.15595)

**<font color=#1a73e8>作者：</font>** Hongbo Ding, Xiang Chen, Jiangxin Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world indoor fire environments, visual degradation severely impairs instruction grounding, waypoint prediction, and long-horizon exploration in vision-language navigation (VLN). Although image restoration offers a natural means to mitigate such visual degradation, existing methods primarily optimize reconstruction fidelity, which does not necessarily translate into better navigation decisions and may even corrupt task-critical cues when applied indiscriminately. In this paper, we present FireNav, a decision-oriented reconstruction evidence routing framework that aligns visual restoration with navigation utility in VLN. To advance this task, we first contribute FireVLN-Bench, a paired indoor fire navigation benchmark with clean references preserving task semantics, safety supervision, and matched settings for continuous navigation and robot execution with simulated dynamics. Our FireNav retains native visual tokens and treats latent reconstruction features as auxiliary evidence, where a lightweight router leverages visual features, task context, and prior execution states to determine whether such evidence should be admitted and how strongly it should contribute to the visual tokens. To learn when reconstruction is beneficial, we further introduce decision utility calibration, which compares action prediction losses with and without candidate evidence under the same state, thereby supervising evidence selection according to its contribution to waypoint, heading, and arrival prediction. Experiments demonstrate that FireNav consistently outperforms state-of-the-art baselines in both navigation success and path efficiency across evaluation settings.

---


### 274. [Side-Vent Design for Microphone-Based Mechanomyography Sensors: Modeling and Experimental Evaluation of Contact Dependence](https://arxiv.org/abs/2610.15600)

**<font color=#1a73e8>作者：</font>** Cong Liu, Xiao Jin, Zhenhua Yu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable muscle sensing for rehabilitation, assistive robotics, and electrical-stimulation feedback needs mechanomyography sensors less sensitive to fit changes during wear. In microphone-based mechanomyography, cavity pressure depends on rim contact, a dependence housing design has rarely targeted. This study evaluates a side-vented housing, whose vent opens a pressure-relief path in parallel with the rim to lower contact dependence, and quantifies the acoustic-gain cost. Thermoviscous finite-element simulations compared twenty cavity configurations under prescribed source motion. Paired bench sweeps over 10-200 Hz on both housings compared direct contact with a Gap-ring spacer, a radially grooved spacer ring. At 100 Hz, side venting reduced the simulated acoustic-gain variation across 0.10-0.50 mm rim clearances from 25.8 to 10.0 dB and cost 5.5 dB of gain at 0.20 mm clearance. Velocity fields and branch-flow calculations identified this path. At the higher speaker drive level, the Gap-ring spacer caused median attenuations of 13.6 dB (vented) and 30.1 dB (unvented) relative to direct contact. In this front end, a 35.9-dB signal-gain increase at 100 Hz raised the calculated operational-amplifier voltage-noise gain by 1.6 dB. A single-participant demonstration of paced elbow flexion and extension compared envelope timing and spectra between housings, finding similar envelope timing (correlation 0.935) and broadly similar spectra (correlation 0.956). Vent area trades acoustic gain against contact dependence and can therefore serve as a housing design parameter.

---


### 275. [CondMSP: Condition-Informed and Resource-Aware Inorganic Materials Synthesis Planning](https://arxiv.org/abs/2610.15603)

**<font color=#1a73e8>作者：</font>** Heewoong Noh, Gyoung S. Na, Elton Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Materials synthesis planning (MSP) connects AI-driven materials discovery to experimental realization by proposing precursors, synthesis operations, and processing conditions for a target material. Existing approaches predict these components separately or in pairs and treat conditions only as a prediction target. Consequently, MSP remains centered on recipe prediction: it leaves unexplored how conditions can serve as process context for constructing synthesis routes, and it does not address which candidate routes should be executed under limited experimental resources. We propose CondMSP, which extends MSP from recipe prediction to execution-aware planning. CondMSP predicts temperature, time, and atmosphere by combining a joint predictor with variable-specific experts, and then uses these predictions both as process context, grounding the generation and retrieval of operation sequences, and as execution requirements, specifying which thermal stages can share a furnace run and at what cost. This specification is held fixed across all compared methods; within it, CondMSP ranks routes across precursor sets by a common utility and, under furnace budgets, jointly selects routes and allocates their thermal stages by constrained optimization. CondMSP improves condition and operation prediction and, under this shared constraint, raises reference-recipe recovery from 27.9% to 32.9% at three simulated furnace runs per target and from 34.7% to 40.0% at 30 trials, while a new evaluation set of 2,344 targets supports generalization beyond oxide-dominated training chemistry.

---


### 276. [Squeeze-Aware-YOLO: Early Channel Recalibration and Multi-Scale Fusion for Real-Time Traffic Sign Detection](https://arxiv.org/abs/2610.15604)

**<font color=#1a73e8>作者：</font>** Mizbaul Haque Maruf, Syed Samin Sadaf, Syed Tamzid Bakht 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic sign detection plays a vital role in intelligent transportation systems, supporting the safe operation of advanced driver assistance systems and autonomous vehicles. Despite significant progress in real-time object detection, accurately identifying traffic signs under challenging conditions remains difficult. Variations in lighting, adverse weather, motion blur, and partial occlusion often reduce detection performance, especially for small or visually degraded signs where important spatial information can be lost. To address these challenges, we propose Squeeze-Aware-YOLO, a lightweight traffic sign detection framework that introduces a multi-branch bottleneck module combining convolutional kernels of different sizes with a Squeeze-and-Excitation mechanism to improve feature extraction and adaptive channel weighting. In addition, we integrate the Multi-Branch Auxiliary Feature Pyramid Network and Re-parameterized Heterogeneous Multi-Scale modules to strengthen multi-scale feature representation and feature fusion while preserving real-time inference efficiency for practical deployment. The proposed approach is evaluated on the Bangladeshi Traffic Sign Detection Dataset, the CSUST Chinese Traffic Sign Detection Benchmark 2021, and the German Traffic Sign Detection Benchmark, achieving mAP@0.5 scores of 74.7%, 79.4%, and 84.0%, respectively, while consistently outperforming recent state-of-the-art YOLO-based traffic sign detectors. These findings demonstrate that combining multi-scale receptive fields, channel attention, and enhanced feature fusion enables more accurate and robust traffic sign detection while maintaining the computational efficiency required for real-world deployment.

---


### 277. [A Co-Located MMG-FES Wearable Interface for Action-Updated State-Gated Stimulation](https://arxiv.org/abs/2610.15605)

**<font color=#1a73e8>作者：</font>** Cong Liu, Xiao Jin, Zhenhua Yu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Functional electrical stimulation (FES) assists movement, but fixed schedules cannot track how a repeatedly activated muscle changes, and surface electromyography (EMG) near the stimulation electrodes is often obscured by artifacts. Prior work recorded mechanomyography (MMG) passively during closed-loop FES cycling and estimated FES-induced fatigue or predicted fatigue for FES control, without gating stimulation with stimulated-site MMG. In this study, we present VG-FES, a wearable module co-locating microphone-based MMG, programmable charge-balanced biphasic stimulation, and embedded state-gated control at one on-skin thigh site. After each action, we compare rectus femoris (RF) mean power frequency (MPF) with an early-session baseline of the same direction, giving a relative state. A threshold on its window means enables fixed-duration bursts separated by rest periods. During onboard stimulation, MMG remained recordable, whereas near-site EMG was artifact-dominated. Under prolonged external stimulation, cycle-wise MMG tracked an independent local-pressure reference (Spearman rho = 0.968). In leave-one-session-out evaluation on 2284 squat actions (11 sessions, eight participants), MMG-based action segmentation reached an event-detection F1 of 0.923 and direction classification a balanced accuracy of 0.925. Online, over 15.69 min of self-paced squats, one participant received four bursts while MMG acquisition and action monitoring continued. Mechanical feedback from the stimulated site offers wearable FES and assistive robotics a per-action basis for state-gated stimulation.

---


### 278. [Lesion-Aware Attention for Mammography Segmentation with Heterogeneous Supervision](https://arxiv.org/abs/2610.15612)

**<font color=#1a73e8>作者：</font>** Di Dai, Bo Liu, Liwei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate lesion segmentation in mammography is important for computer-aided breast cancer diagnosis, but dense pixel-level annotations remain costly and limited. Existing public segmentation datasets usually cover only a small set of lesion types with manually delineated masks, whereas larger mammography datasets often provide only image-level diagnostic labels. This annotation mismatch makes it difficult to train segmentation models that can generalize to rare or weakly annotated lesion categories. To address this problem, we study open-vocabulary mammographic lesion segmentation under a mixed-supervision setting, where pixel-level masks are available for base lesion categories and image-level labels are available for a broader set of categories. We propose a two-branch framework that jointly learns from segmentation data and classification data. The segmentation branch learns lesion boundaries from annotated masks, while the classification branch introduces additional image-level semantic supervision. To better transfer image-level supervision to lesion-relevant regions, we further introduce a Lesion-wise Attentive Classifier that maintains category-specific feature prototypes and generates lesion-aware attention maps for foreground feature pooling. This design reduces the influence of background tissue and encourages more compact lesion representations. Experiments on multiple mammography datasets show that the proposed method consistently improves open-vocabulary segmentation baselines on both base and novel lesion categories, while reducing the gap to fully supervised models that require dense target-domain masks. Qualitative results further indicate that our method produces more complete lesion localization for small, low-contrast, and visually subtle mammographic findings.

---


### 279. [ProML: Progressive Multi-label Learning](https://arxiv.org/abs/2610.15614)

**<font color=#1a73e8>作者：</font>** Yi Kou, Jieting Wang, Yuhua Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-label learning typically pursues model construction through the joint optimization of label fitting, correlation modeling, and structural regularization. While empirically effective, such a coupled paradigm imposes multiple learning objectives on a single predictive parameter matrix, forcing it to simultaneously fit observed labels and encode structural priors. This coupling may induce ill-conditioned optimization geometry, increase hyper-parameter sensitivity, and complicate capacity control. To address the these issues, this paper proposes a Progressive Multi-Label Learning (ProML) framework, which decouples direct label fitting from predictor learning via the introduction of an auxiliary predictive variable. This auxiliary variable admits a closed-form solution, yielding an equivalent profiled objective in which the supervised fitting term is scaled by a trade-off parameter. This result provides a unified view of ProML and conventional coupled learning, with the latter recovered as a limiting case. We theoretically analyze the optimization geometry of ProML and show that, under quadratic positive semidefinite structural regularization, ProML attenuates the dominant curvature of the fitting term, enlarges the stable learning rate range, and provides a controllable fidelity-regularization trade-off. Further, we instantiate the ProML for multi-label feature selection task by integrating global-local label priors and row-sparse regularization. Extensive experiments and controlled optimization analyses on 12 benchmark datasets empirically corroborate the theoretical analysis and demonstrate the robust and competitive performance of the proposed method.

---


### 280. [Adaptive Role Assignment and Controlled Feature Reconstruction for Federated Image Semantic Communication](https://arxiv.org/abs/2610.15623)

**<font color=#1a73e8>作者：</font>** Yuxuan Chen, Jiao Bie, Hang Qi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid federated semantic communication enables user equipment (UEs) to contribute model updates or semantic features under a shared training framework. However, heterogeneous role costs and the interaction between model aggregation and feature reconstruction (FR) remain key challenges in practical radio access network (RAN) deployment. To address these issues, we propose ARC-FedSC, a RAN-aware framework that coordinates UE role assignment and server-side controlled FR under a fixed communication budget. Within ARC-FedSC, RAN Aware Role-Bandit learns the historical contribution of UEs in different roles together with current uplink conditions, while Temporal Consistency Alignment (TCA) regulates FR according to recent model aggregation directions. Experiments on CIFAR-10 with time-varying RAN channels show that ARC-FedSC outperforms baselines across all five tested role configurations in the later training stage, with the best configurations achieving about 24.17 dB average PSNR over the last 20 rounds. Component level results further show that Role-Bandit maintains an average rolling UE coverage of 85.3%, compared with about 65.7% for baseline, while TCA reduces the probability of harmful FR events from 0.245 to 0.093, corresponding to a 62.0% reduction. Ablation and sensitivity studies further support the effectiveness and robustness of the proposed design.

---


### 281. [1Step-WAM: Your World Action Model but Faster using 1-Step Action Generation](https://arxiv.org/abs/2610.15625)

**<font color=#1a73e8>作者：</font>** Rundong Su, Pengtao Chen, Haohan Geng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) unify visual world modeling and action generation, yet their real-world deployment is heavily bottlenecked by iterative action denoising and the sequential execution of visual prefilling and action prediction. We demonstrate that the action-denoising trajectories in WAMs are approximately straight, rendering the first-step velocity a strong estimate of the final action direction. Building on this observation, we introduce 1Step-WAM, a framework that transforms multi-step action denoising into one single forward. Specifically, we employ a lightweight calibrator to directly correct the first step velocity, and use bandwidth-constrained action decoding to further reduce errors in the calibrated one-step actions. Compressing action generation into a single step enables it to execute in parallel with visual prefilling, completely breaking the sequential bottleneck of the traditional imagination-then-action paradigm. Evaluations on RoboTwin and LIBERO show that 1Step-WAM largely preserves multi-step task success with only about 13.4M trainable parameters, while achieving inference speedups of $7.44\times$, $5.98\times$, and $24.84\times$ for FastWAM, ImageWAM and Kairos, respectively. Furthermore, real-world robotic deployments using the FastWAM backbone confirm a consistent 7.44$\times$ speedup while maintaining close success rate to the multi-step baseline. Code is avaliable at this https URL.

---


### 282. [Riemannian Suppression of Cross-Session Identity Leakage in Motor-Imagery EEG](https://arxiv.org/abs/2610.15626)

**<font color=#1a73e8>作者：</font>** Sheikh Samit Muhaimin, Aarthy Nagarajan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) recorded for motor-imagery (MI) brain-computer interfaces (BCIs) carries subject-identifying structure that persists across sessions, allowing separately released sessions from the same person to be linked. Existing EEG identity protections use learned or additive perturbations and operate on representations other than the covariance geometry underlying MI pipelines. We ask whether cross-session identity leakage can be suppressed directly in this covariance representation without learning a privacy model. We introduce a Riemannian transform that equalizes two subject-conditioned geometric statistics: the Riemannian mean covariance and the tangent-space scatter around it, with two optional band-specific refinements. Ablations show that mean alignment and scatter whitening carry nearly all of the suppression, while the optional stages contribute small, dataset-dependent refinements. Across two public datasets and five attackers spanning four covariance-space representations, the worst attacker falls from 90.8% to 15.6% on BCI Competition IV-2a and from 90.8% to 9.9% on OpenBMI, at a cost of 7.0 and 2.1 points of MI decoding accuracy relative to the 8-30 Hz input, and no aggregation rule exceeds chance by more than two points at any batch size. The transform requires no learned privacy model, surrogate network, or gradient-based training, and is fitted on one session and applied unchanged to a held-out later session.

---


### 283. [Robust Detection of Directional Adversarial Attacks in Deep Neural Networks for Radiological Imaging](https://arxiv.org/abs/2610.15628)

**<font color=#1a73e8>作者：</font>** Tristan Malatyński, Joanna Jaworek-Korjakowska  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning is now central to radiology, helping detect changes on X-rays, CTs, and MRIs. However, these systems are highly vulnerable to adversarial attacks - small, crafted perturbations that mislead models while appearing unchanged to humans. Such errors risk missed cancers or false positives. Studies show over 90% attack success on medical scans. Almost 30% of US hospitals use AI in imaging in 2023. Thus, an effective method of detecting such attacks and their directionality is crucial to ensure the credibility and reliability of medical systems based on DNNs. We propose a novel detection framework that leverages subsequent attacks using random noise to identify adversarial perturbations. Our approach uses the analysis of variations in the Sigmoid function to distinguish genuine medical images from adversarially manipulated ones. Specifically, we compare prediction differences between clean and attacked images, as well as between different adversarially altered versions, to improve detection accuracy. We evaluated our method on three popular medical datasets including 'Chest X-Ray Images for Classification', 'Retinal Fundus Multi-disease Image Dataset' and 'Brain Tumor Dataset' under various attack scenarios, including random noise. Our framework achieved up to 99.8% ACC in identifying adversarial directional attacks, significantly outperforming existing defense mechanisms. It consistently identified adversarial samples across varying attack strengths while keeping false positives low, showing strong reliability and potential for clinical use. Furthermore, our proposal highlights its potential for real-world deployment.

---


### 284. [SurgCast: Action-Conditioned Future Skeletons for Controllable Surgical World Models](https://arxiv.org/abs/2610.15645)

**<font color=#1a73e8>作者：</font>** Wanhao Liu, Rulin Zhou, Liangjing Shao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical world models must turn prospective robot actions into visually faithful, structurally consistent instrument motion. We introduce SurgCast, which predicts future instrument skeletons from current structure, robot state, and future actions, then uses the forecast to control video generation. Dual-path injection combines skeleton geometry with derived, instrument-specific motion descriptors through geometric residuals and conditioning modulation. Both paths complement native action conditioning and are retained in a four-step causal student. On SutureBot and SRTH-Porcine-Cholei, the teacher and student improve all seven reported quality and instrument-consistency metrics over their respective direct-action baselines; teacher FVD decreases by 37.6% and 67.3%. Ablations show that future actions improve skeleton prediction and that combining both injection paths performs best across all six metrics under predicted skeletons. These results support using predicted articulated structure and its motion semantics as a control interface for surgical video prediction. Project videos and examples are available at this https URL.

---


### 285. [Dynamic Conflict Clustering with Lightweight Learning and Strategic Repair for Distributed Constraint Satisfaction](https://arxiv.org/abs/2610.15658)

**<font color=#1a73e8>作者：</font>** Raziyeh Moghaddas, Fabio Caraffini  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Distributed Constraint Satisfaction Problems (DCSPs) model distributed decision-making in multi-agent systems, where agents assign values to local variables while satisfying shared constraints. However, many DCSP solvers still rely on broad, repeated peer-to-peer communication and are largely reactive, with limited support for strategic coordination or learning. This increases communication overhead, can lead to stagnation, and reduces the success of hard instances. Hence, we propose Dynamic Conflict Clustering-Incomplete (DCC-Incomplete), a repair-based solver that combines conflict-centred decomposition, structured coordination, strategic repair, and lightweight learning for stagnation recovery. DCC-Incomplete groups the unsolved part of the problem into conflict clusters and restricts communication via a coordination layer to agents within the same conflict region. It also introduces memory-guided restart, enabling agents and clusters to pause, revise, and adapt repairs based on neighbouring conflict states. A thorough evaluation of DCC-Incomplete on distributed graph-colouring benchmarks with planted satisfying assignments shows that its memory-guided restart improves the success rate from 37.50% to 61.11%, reduces median runtime from 0.565s to 0.367s, and cuts median communication from 12.493 to 6.503 messages per constraint. These results suggest that dynamic conflict clustering, combined with lightweight strategic and learning-guided repair, improves both communication efficiency and robustness in incomplete DCSP solving.

---


### 286. [Testing Central Structure for Complex Networks](https://arxiv.org/abs/2610.15659)

**<font color=#1a73e8>作者：</font>** Qilong Wu, Yuxiao Li, Simeng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Centrality measures rank nodes even when the observed differences can be explained by ordinary structural variation. We therefore study a preceding question: whether a network contains a statistically identifiable central structure at all. We formulate this question as a network-level hypothesis testing issue using the adjacency spectral radius as the test statistic and estimate an empirical p-value from randomized networks generated under a specified null model. The framework is evaluated using G(N,M), Chung-Lu, and two implementations of the configuration model on simulated benchmarks and 55 real networks. Controlled experiments further vary the number and connection weights of designated central nodes while holding network size and density fixed. The results show a clear negative association between central-structure strength and the empirical p-value. They also demonstrate that rejection decisions depend substantially on the structural properties preserved by the null model: the detected network sets are not simply nested across models.

---


### 287. [Sparse All-Layer Connector for Domain Generalised Semantic Segmentation](https://arxiv.org/abs/2610.15660)

**<font color=#1a73e8>作者：</font>** Ruoyu Guo, Xin Kun Lin, Maurice Pagnucco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain generalised semantic segmentation (DGSS) has recently benefited from combining multiple foundation models, such as vision-language and vision foundation models, to leverage their diverse representations for generalisation. Existing multi-model approaches share a common design choice: cross-model fusion is restricted to depth-aligned layers, implicitly assuming that mutually beneficial information resides at the same depth across models. However, foundation models pretrained under different objectives may develop distinct representation hierarchies, making the optimality of depth-aligned fusion questionable. Moreover, we observe that the foundation models exhibit different depth-wise domain sensitivity. Motivated by these observations, we propose a Sparse All-Layer Connector (SALC) that enables each layer to access information from preceding layers of another model. As the number of accessible layers grows with depth, dense aggregation may hurt generalisation. SALC therefore learns to adaptively select a sparse subset of informative layers. We further introduce a candidate dropout regularisation that strengthens sparsity and encourages SALC to explore diverse layers, leading to more robust selection. Across four foundation model combinations and three DGSS evaluation settings, the proposed design demonstrates stronger generalisation than conventional depth-aligned fusion. The code is available at this https URL.

---


### 288. [Drift, Then Spread: Learning One-Step Generative Policies for Online Reinforcement Learning](https://arxiv.org/abs/2610.15662)

**<font color=#1a73e8>作者：</font>** Chunyu Luo, Hongyu Zhao, Guangyi Ni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative policies offer expressive action distributions for online reinforcement learning (RL), but many diffusion- and flow-based policies require costly iterative sampling. We propose DriftSpread, a one-step generative policy based on Drifting for online maximum-entropy (MaxEnt) RL. To incorporate entropy without a tractable policy density, we build on an energy-based view of Drifting and derive critic-guided Drift and entropy-induced Spread from the negative MaxEnt objective. Our method learns these updates sequentially in the same actor, using action regression for value improvement and distribution matching to capture the effect of entropy. The actor updates require neither direct samples from the critic-defined Boltzmann target nor policy-density or score estimation. Under exact fitting with a fixed critic, we prove convergence to the Boltzmann target in the small-step limit followed by the long-time limit. On MuJoCo, DriftSpread achieves the highest aggregate normalized return among all evaluated methods, while outperforming the diffusion- and flow-based baselines in both training and inference efficiency.

---


### 289. [ProtoPur: Prototype-Purity Pseudo-Labeling for Weakly Supervised Instance Learning in Pathology](https://arxiv.org/abs/2610.15669)

**<font color=#1a73e8>作者：</font>** Chen Shu, Chengyang Zhang, Boyu Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weak bag-level labels are widely available in computational pathology, whereas reliable instance-level annotations for whole-slide images remain expensive and ambiguous. Weakly supervised multiple instance learning (MIL) achieves strong bag-level classification, but instance-level supervision from attention scores, model predictions, negative bags, or spatial refinement may fail to identify class-specific local evidence. We propose ProtoPur, a prototype-purity pseudo-labeling method for weakly supervised instance-level learning in pathology whole-slide images. ProtoPur estimates class-balanced local purity over prototype regions constructed from frozen foundation-model features, and assigns pseudo-labels to high-purity regions strongly associated with a target class. This purity-first design separates class-specific evidence from negative or shared morphology, with coverage used only to ensure sufficient pseudo-label assignment. We provide a PAC-style analysis showing that the risk of an instance classifier trained with ProtoPur pseudo-labels can be decomposed into a standard uniform-convergence term and a ProtoPur-specific pseudo-label noise term, comprising selected-region mismatch and a coverage residual. Experiments on three public whole-slide image datasets with two pathology foundation encoders show that ProtoPur consistently improves instance-level performance across multiple MIL backbones while maintaining competitive bag-level performance. Pseudo-label quality comparisons on two public datasets further demonstrate that prototype-purity selection provides stronger instance supervision. These results suggest that the foundation-model features contain exploitable instance-level supervision signals, and ProtoPur is a way to reveal and use these signals from weak bag labels without requiring dense instance annotations.

---


### 290. [Rethinking Human Intent-to-CAD: Parametric CAD Model Generation via Cooperative Multi-Task Alignment and Spatial-Aware Reinforcement Learning](https://arxiv.org/abs/2610.15681)

**<font color=#1a73e8>作者：</font>** Qingwang Zhang, Jiahao Li, Xiangdong Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parametric Computer-Aided-Design (CAD) modeling from human intent remains challenging, particularly during the conceptual design stage, where design goals are expressed through incomplete and unstructured modalities (e.g., hand-drawn sketches and textual descriptions). In this work, we rethink the human intent-to-CAD pipeline and propose a unified method that directly maps multi-level human intents to executable codes, without assuming the prior existence of target CAD models. To support our study, we construct HiCAD, the first large-scale dataset aligning hand-drawn sketches, textual descriptions, and parametric CAD codes. Based on this, we introduce HiCAD, a two-stage framework comprising Cooperative Multi-Task Alignment to bridge the representational gap between heterogeneous inputs, and Spatial-Aware Reinforcement Learning to enforce geometric and topological consistency. Extensive experiments demonstrate that our method significantly outperforms existing baselines across multiple tasks, validating its effectiveness and robustness in transforming heterogeneous human intents into high-fidelity parametric CAD models. Our project page: this https URL.

---


### 291. [FARL: A Fully Automated Pipeline of RL Interface and Solver Design](https://arxiv.org/abs/2610.15691)

**<font color=#1a73e8>作者：</font>** Tianyu Jin, Liuyu Xiang, Chaowen Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing reinforcement learning (RL) largely focuses on optimizing learning algorithms within a pre-defined task formulation, while applying RL to new tasks still relies heavily on human expertise to design the learning pipeline: what an agent observes, how it is rewarded, which algorithm it uses, and how training is configured. Automating these choices is challenging because they are tightly coupled. We introduce FARL (Fully Automated Reinforcement Learning), a framework that automates RL design by jointly searching observation and reward programs, learning algorithms, and training settings. FARL uses training statistics and observed behavior to diagnose failures, propose changes, and test whether they improve learning. Its search preserves diverse candidates and the controls needed for these tests, using a staged budget to screen designs before investing in longer training. Experimental memory records each finding together with its conditions, so an unsuccessful component can be reconsidered in a different combination. Across expert-withheld and expert-available settings, FARL outperforms the evaluated automated baselines on challenging navigation, locomotion, and manipulation tasks. On Adroit Hand Relocate, FARL achieves 97.1% success at 5M training steps per policy, compared with 0% for Eureka and LiMEN and 1.0% for native Proximal Policy Optimization (PPO) under the same policy training budget.

---


### 292. [DRanker: A Transformer-Based Multi-Task Ranking Model for the Disney+ Homepage](https://arxiv.org/abs/2610.15696)

**<font color=#1a73e8>作者：</font>** Priya Nirmal Singh Khokher, Daniel Nemirovsky, Benjamin P. Whitesell 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present DRanker (Disney+ Ranker), a transformer-based multitask ranking model serving personalized recommendations on the Disney+ homepage. We describe the encoder-only architecture over enriched engagement-history sequences paired with a lightweight causal debiasing mechanism, and the inference stack that enables transformer-based ranking at scale. Through iterative development, we systematically evaluated more complex alternatives and found that simpler designs consistently outperformed them on offline metrics, qualitative behavioral evaluation, and in production. Deployed globally, DRanker drives over 1% lift in our key engagement metric and 0.5% lift in daily active users across all experiences powered by the ranker. We share practical lessons on data engineering, debiasing, and architectural choices that shaped our ranking system at scale.

---


### 293. [RespFocus: Learning Temporal Evidence for Weakly Supervised Respiratory Sound Classification](https://arxiv.org/abs/2610.15702)

**<font color=#1a73e8>作者：</font>** Yi Tian, Xiaohuan Chen, Yufei tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Respiratory auscultation provides a low-cost means of assessing pulmonary function, yet transient crackles and sustained wheezes can be difficult to recognize in noisy clinical recordings. Conventional deep learning classifiers often operate as black boxes, offering limited insight into the temporal acoustic evidence supporting their predictions. We present RespFocus, a weakly supervised framework that uses multiple instance learning (MIL) to learn inspectable temporal evidence from cycle-level labels and integrate it into classification. We also introduce PedResp2026, a multicenter pediatric respiratory sound cohort collected in routine clinical environments with adjudicated cycle-level annotations. In classification experiments, RespFocus achieves four-class Scores of 69.55\% on public ICBHI 2017 and 72.91\% on PedResp2026. Evidence diagnostics and matched temporal interventions support the functional contribution of the learned evidence to model predictions. Together, these findings highlight RespFocus's potential as a tool for automated respiratory sound diagnosis.

---


### 294. [bharatSetu: a 1M x 22 bridge for indic translation](https://arxiv.org/abs/2610.15705)

**<font color=#1a73e8>作者：</font>** Haq Nawaz Malik, Nahfid Nissar, Faizan Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> India's Eighth Schedule recognises 22 languages, yet parallel data is uneven across them, and many language pairs, especially among lower-resource languages such as Bodo, Dogri, Santali and Kashmiri, lack direct bitext. We present BharatSetu 22-Indic 1M, a row-aligned table of 984,764 English sentences, each paired with machine translations into all 22 scheduled languages (21,664,808 Indic cells), generated with the sarvamai/sarvam-translate model family. Because every Indic cell in a row translates the same English sentence, any two columns form a translation pair: 462 directed Indic-to-Indic pairs, or 506 including English, without direct bitext. We call these pivot-derived pairs and propose a confidence layer that lets users choose how strictly each pair is connected. The corpus is machine-generated and not human-verified; quality is expected to vary by language, domain and sentence style, and pivot-derived pairs can inherit errors from both sides. We therefore release BharatSetu as a machine layer and propose a human-correction layer keyed to the same row identifiers, so that each corrected column upgrades every pair that uses it, together with an evaluation protocol. We report no translation-quality results.

---


### 295. [MedHarnessBench: A Unified Benchmark for Healthcare Agent Evaluation](https://arxiv.org/abs/2610.15714)

**<font color=#1a73e8>作者：</font>** Rui Tang, Hongqiu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare agents must transform longitudinal clinical evidence into reliable actions through heterogeneous tools and stateful workflows, conditions under which model-centric systems may lose context, misuse tools, fail to verify consequential transitions, or cross authorization boundaries. Existing medical-agent benchmarks primarily emphasize terminal task outcomes, making it difficult to determine whether execution failures arise from the agent model, the runtime harness, or their interaction. We present the Medical Harness Protocol, an outcome-preserving framework that independently evaluates seven healthcare-specific process dimensions: Care Action Fulfillment, Clinical Resource Competence, Patient-Evidence Alignment, Clinical Workflow Continuity, Clinical Auditability, Closed-Loop Verification, and Clinical Conduct Boundaries. A normalized intervention trace further tracks whether runtime support is available, activated, delivered, adopted by the agent, and propagated into subsequent behavior. We instantiate the protocol as MedHarnessBench, comprising 342 executable tasks across FHIR/EHR operations, healthcare-administration interfaces, and multimodal clinical tools. Across more than 16,000 controlled task executions, MedHarness yields broad improvements in terminal task success, intermediate subtask completion, and healthcare-specific process quality. We further evaluate MedHarness against multiple general-purpose harnesses and use controlled single-fault perturbations to verify the sensitivity and discrimination of the seven-dimensional evaluation. These results demonstrate that healthcare-specific runtime support can substantially improve both task completion and execution quality, while revealing failures that terminal outcomes alone cannot capture. Code and resources are available at this https URL.

---


### 296. [Uncovering the Generative Landscape of Diffusion Models: A Spectral-Guided Quality-Diversity Diffusion Framework](https://arxiv.org/abs/2610.15724)

**<font color=#1a73e8>作者：</font>** Hannah Janmohamed, Joao Correia, Penousal Machado 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Denoising Diffusion Probabilistic Models have emerged as powerful generative priors across domains ranging from molecular design to high-resolution image synthesis. However, standard diffusion sampling is inherently biased toward high-likelihood regions, often limiting the diversity of outputs. In many domains, a single, high-likelihood sample is insufficient. Instead, diverse portfolios of high-performing solutions are required, motivating methods that uncover a model's full expressive range. Here we show that integrating Quality-Diversity (QD) optimisation with diffusion models enables the discovery of diverse, high-performing outputs. We first propose Quality-Diversity Diffusion, a framework that adapts QD to diffusion models by directly optimising the model's latent noise and conditioning embeddings and leveraging embedding models to quantify diversity. Second, we introduce a novel h-space Spectral Mutation operator, which guides search along directions of maximal semantic sensitivity by analysing principal singular vectors of the model's input-to-activation Jacobian. We evaluate our combined approach, Spectral-Guided Quality-Diversity Diffusion, on text-to-image generation. Against 12 baselines, our method consistently achieves the lowest FID score, demonstrating an excellent balance of image quality and diversity.

---


### 297. [A Dependency-Aware Multi-GPU Training Framework for Temporal Graph Neural Networks](https://arxiv.org/abs/2610.15730)

**<font color=#1a73e8>作者：</font>** Yang Zhao, Yue Dai, Liang Qiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal graph neural networks (TGNNs) achieve superior performance in many dynamic graph learning tasks. These models use node state vectors (i.e., memories) to capture and record graph changes (i.e., events), and then exploit these memories to assist prediction. However, this memory-centric design makes multi-GPU training challenging because predictions for later events often depend on memory updates from earlier events. To maintain model quality, existing multi-GPU TGNN training schemes strictly preserve all event dependencies, which limits parallelism and causes expensive cross-GPU memory synchronization. In this work, we observe that many of these dependencies can be handled more flexibly without harming training quality. Specifically, (a) dependencies in TGNN training have high locality in both time and graph topology, (b) the short-range dependencies missed within a large batch can often be recovered cheaply, and (c) many memory updates are not immediately needed. Based on these observations, we propose DepBloom to accelerate multi-GPU TGNN training with three techniques: (1) temporally bounded spatial partitioning to reduce unnecessary cross-GPU synchronization and improve parallelism; (2) intra-batch memory refinement to recover missing short-range temporal dependencies inside enlarged batches; and (3) critical-path optimization to prioritize urgent memory updates while deferring non-critical work during multi-GPU pipeline execution. Experimental results across representative models and diverse datasets show that DepBloom achieves an average speedup of 2.84$\times$ and up to 5.16$\times$ over state-of-the-art methods, while maintaining comparable or better model accuracy.

---


### 298. [ScenePlacer: Reformulating Scene-Level Object Pose Estimation as Visibility Field Learning](https://arxiv.org/abs/2610.15734)

**<font color=#1a73e8>作者：</font>** Ken Deng, Jiarui Liu, Guibiao Liao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ScenePlacer, a framework for scene-level pose estimation of objects generated by state-of-the-art native shape generation models, placing generated 3D objects into scenes given a partial geometric observation without modifying the underlying generative pipeline. Existing scene generation approaches either generate objects directly in scene coordinates, compromising their canonical-space priors, or regress poses from complete generated shapes in the shape generation process - the latter being a poorly conditioned problem that is sensitive to scale ambiguity and partial observations. ScenePlacer decouples object generation from pose estimation by reformulating alignment as conditional visibility-field learning. Given an observed partial point cloud from reconstruction and a generated mesh, it predicts a visibility field defined in object space, then estimates the rigid transformation by aligning the partial observation to visible parts on the mesh. We propose a pretrained 3D shape VAE as our backbone, preserving its mesh prior while conditioning it on a separately encoded observation. We further introduce visibility-aware, radius-constrained supervision and synthesize training pairs using only object-level meshes and rendered views, eliminating the need for scene-level pose annotations. On 3D-FUTURE, ScenePlacer consistently outperforms existing placement and pose-refinement baselines under both ground-truth and monocular depth estimation. With generated objects, it achieves a Chamfer distance of 0.0077 and an F-score of 92.40 under estimated depth and improves to 0.0023 and 98.27, respectively, under ground-truth geometry.

---


### 299. [Frozen History: When Temporal Losses Stop Accumulation in Learned Real-Time Supersampling](https://arxiv.org/abs/2610.15752)

**<font color=#1a73e8>作者：</font>** Hao Yu, Guoying Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned real-time supersampling accumulates jittered low-resolution samples along motion vectors. Many methods use a temporal consistency loss to reduce flicker. We show that with accurate registration, this loss can suppress accumulation: on static content, the network copies its warped history at almost no temporal cost. Camera jitter in motion vectors raises this cost and can hide the effect. We identify four registration errors that training can conceal: jitter-carrying motion vectors, one motion field for both resolution lattices, jittered depth, and an unregistered skip path. A model-free oracle shows that correct registration makes freezing two orders of magnitude cheaper on static pixels. Controlled training shows that registration reverses the temporal weight's effect on PSNR. Under exact registration, increasing the weight reduces pixel variance at the expense of accuracy and perceived quality, with a 0.7 to 0.9 dB loss on static frames at weight 0.25. This reversal recurs across three network families and two scales; the loss also reduces accuracy on unjittered STSS data. With a small temporal weight and a normalised sample accumulator, a plain registered network improves the best published QRISP PSNR by 0.34 to 0.62 dB at $\times$2, $\times$3 and $\times$4 upscaling to 1080p. At $\times$2, its static pixel standard deviation is one quarter that of DLSS 2. Without retraining, it outperforms classical temporal upsampling by at least 4.4 dB on Arm's jittered Bistro capture. Our most accurate $\times$4 model runs in 2.03 ms per 1080p frame on an H200. Code: this https URL

---


### 300. [Enhancing Zero-Shot Domain Transfer in Low-Resource Sentiment Analysis: A Case Study in Marathi](https://arxiv.org/abs/2610.15757)

**<font color=#1a73e8>作者：</font>** Tanvi Somani, Aryan Babare, Samyak Bora 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment analysis is a key task in Natural Language Processing that determines the polarity of opinions in text. For low-resource languages like Marathi--where limited data prevents the direct use of standard statistical methods--models are often trained on single-domain datasets. While this yields strong in-domain performance, it leads to poor generalization to unseen domains. Recent studies highlight the need for domain-robust systems that can handle diverse real-world content through multi-domain modeling. This study investigates how multi-domain training improves sentiment classification for unseen Marathi domains. Models are trained using single-domain, two-domain, and three-domain dataset combinations. Results show that two-domain training improves accuracy on unseen domains by about 8\% compared to single-domain training. Adding a third domain provides further improvement, though the gain is smaller, averaging around 2\% for some domains. These results suggest that training with data from multiple domains helps build more robust sentiment analysis models for low-resource languages, though the benefits reduce as more domains are added.

---


> [!TIP]
> 当前位于：**251-300**（第 6/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
