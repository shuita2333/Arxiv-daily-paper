# 📦 其他研究 | 2026年06月16日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-211](./part-05.md)

---

### 1. [A Deep Reinforcement Learning (DRL)-Based Transformer Method for Solving the Open Shop Scheduling Problem](https://arxiv.org/abs/2606.13682)

**<font color=#1a73e8>作者：</font>** Faezeh Ardali, Mwembezi A. Nyelele, Gerald M. Knapp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The open shop scheduling problem (OSSP) arises in many industrial and service settings but remains computationally challenging as the number of jobs and machines increases. While exact methods quickly become intractable, classical dispatching rules and metaheuristics may require substantial tuning to maintain solution quality at large scales. This study develops a Transformer-based scheduling policy for OSSP using an encoder-decoder architecture with multi-head attention. The model is trained on Taillard benchmark instances (4x4, 5x5, 7x7, and 10x10) using only the processing-time matrix as input and produces feasible schedules with makespans typically within 15-30% of best-known values. To evaluate scalability, the trained policy is applied without retraining to randomly generated instances from 40x40 to 100x100 and compared against classical dispatching heuristics, including SPT, LPT, MWKR, and EST. Across these large instances, the Transformer achieved average gaps of 12.89-15.12% relative to a standard lower bound. Compared with EST, the Transformer remained competitive, typically within a modest margin, while substantially outperforming SPT and LPT. These results indicate that a Transformer policy trained on small OSSP instances can generalize to substantially larger problems and provide a feature-light, learning-based alternative to classical dispatching rules.

---


### 2. [Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces](https://arxiv.org/abs/2606.13686)

**<font color=#1a73e8>作者：</font>** Zijing Shi, Meng Fang, Ling Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As autonomous web agents are increasingly deployed to perform real-world tasks, ensuring their safety has become a critical concern. In this work, we study web agent behavior under realistic deceptive interfaces in the e-commerce domain. We introduce WebDecept, a lightweight and configurable plugin framework that enables controlled injection of deceptive interface patterns into existing web environments. Using WebDecept, we instantiate seven deceptive patterns commonly observed on the open web, including targeted advertisements, domain redirection, and shopping manipulation. By injecting these patterns into the frontend during task execution, we perform controlled evaluation of multiple multimodal web agents. Our results show that current web agents are highly susceptible to multiple classes of deceptive interfaces, and that prompt-based constraints are often insufficient to mitigate these failures. We further analyze how the design choices of deceptive patterns influence the success of such manipulations. These findings highlight safety challenges that should be addressed as web agents are scaled toward real-world deployment.

---


### 3. [The Frustrometer: Detecting User Frustration in Data Visualization Tasks using Biomarkers and Interaction Patterns](https://arxiv.org/abs/2606.13687)

**<font color=#1a73e8>作者：</font>** Johannes Ellemose, Sophia Wanner, Djordje Slijepčević 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualization research has largely solved \textit{how} to help a stuck or frustrated user -- through interactive onboarding, contextual help, and active guidance. The unsolved problem is \textit{when}: trigger help too eagerly and you break the user's train of thought; wait too long and they have already gone astray. We present the \textsc{Frustrometer}, a series of experiments to predict user stuckness and frustration by fusing physiological and interaction signals. The Frustrometer consists of a convolutional neural network classifier, that in real-time estimates whether user are stuck in their task or not. We collected data from a controlled study where 14 participants performed analytical tasks on two interactive visualization dashboards while we captured eye movement, pupil dilation, galvanic skin response, heart-rate, head orientation, mouse dynamics, and keyboard events. In addition participants assessed their own performance, while we annotated when during the tasks the participants were stuck. Our results reveal that autonomous physiological responses such as heart-rate and galvanic skin response provide limited insights into the frustration level of the user. Similarly, head orientations are not easily correlated with the frustrations felt by the user during visual analysis tasks. Mouse movements and gaze data conversely carry the majority of predictive signal, with mouse movements alone having a strong correlation for some participants, suggesting that lightweight instrumentation may suffice for real-time frustration detection. We end the paper by discussing how these findings can inform the design of adaptive guidance systems for complex visualization tasks that takes a multimodal approach to frustration and stuckness detection.

---


### 4. [History of the Muddy Children Puzzle](https://arxiv.org/abs/2606.13703)

**<font color=#1a73e8>作者：</font>** Hans van Ditmarsch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Muddy Children Puzzle is a puzzle about knowledge and ignorance that has been inspiring for the development of epistemic logic. Who came up with it first? This is unclear. We trace the origin of the Muddy Children Puzzle through logical and literary publications over the past two centuries. The puzzle inspired a numerous variations such as involving numbers or coloured hats. We also present a novel hats puzzle involving self-reference.

---


### 5. [Hybrid Open-Ended Tri-Evolution Makes Better Deep Researcher](https://arxiv.org/abs/2606.13710)

**<font color=#1a73e8>作者：</font>** Hongming Piao, Chi Liu, Mengzhuo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research and agent evolution serve as de-facto tasks for AI agents in real-world applications toward artificial general intelligence. The former enables autonomous retrieval and integration of information in open-ended environments to tackle open-ended research tasks, yet it is constrained by the static parametric deep research capabilities of agent systems. The latter allows agents to autonomously interact with the environment to gain experiences that evolve model capabilities. However, its effectiveness has been widely validated only on verifiable tasks with standard answers, leaving a gap with open-ended research tasks. To bridge these two critical tasks, we propose the Hybrid Open-Ended Tri-Evolution (HOTE) framework, which leverages hybrid-mode reinforcement learning to facilitate the collaborative evolution of a proposer, solver and judge based on web-scale knowledge, moving toward autonomous evolving agents in open-ended tasks and environments. Extensive experiments on three long-form deep research benchmarks demonstrate that the 8B model trained via HOTE surpasses the strongest static open 8-32B models as well as those trained by state-of-the-art deep research training methods with less time overhead, and further verify that the evolution of all three modules in HOTE is indispensable.

---


### 6. [TSA: Temporal Slot Activation for Persistent Object-Centric Video Representation](https://arxiv.org/abs/2606.13714)

**<font color=#1a73e8>作者：</font>** Duc Nguyen, Sieu Tran, Hao Vo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised video object-centric learning aims to decompose dynamic scenes into temporally persistent entity representations. Existing recurrent video slot-attention methods propagate a fixed set of slots across frames, but typically assume unconditional slot propagation: every slot is updated and decoded at every frame, regardless of whether its corresponding object is visible. We show that this design violates a basic lifecycle requirement for persistent slots: when an object is absent or fully occluded, its slot should preserve its previous state and avoid explaining unrelated visible content. Instead, unconditional propagation creates two failure pathways: update-induced state drift, where current-frame evidence overwrites the absent object's representation, and decoder-induced reconstruction interference, where the inactive slot remains coupled to reconstruction through decoder attention. We propose Temporal Slot Activation (TSA), a mechanism that learns a per-slot, per-frame activation score $\alpha_{k,t} \in (0, 1)$ without visibility supervision. TSA uses this activation as a shared latent control variable for slot lifecycle modeling. When a slot is inactive, TSA anchors its state to the previous slot via activation-gated updating and suppresses its decoder participation through an activation-dependent additive bias on attention logits before softmax normalization. This jointly reduces state drift and reconstruction-driven interference. To improve decisions under partial occlusion and gradual reappearance, TSA further conditions activation prediction on a per-slot temporal memory produced by a Temporal Context Encoder. We evaluate TSA on MOVi-C/E, YT-VIS, and OVIS benchmarks using both standard and tracking-based metrics (FG-ARI, mBO, IDF1, HOTA). TSA consistently improves object decomposition and temporal identity preservation, with large gains on long, heavily occluded videos.

---


### 7. [WorkBench Revisited: Workplace Agents Two Years On](https://arxiv.org/abs/2606.13715)

**<font color=#1a73e8>作者：</font>** Olly Styles  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The best agent on WorkBench in March 2024, GPT-4, completed 43% of tasks and took an unintended harmful action, such as emailing the wrong person, on 26% of them. We re-visit the benchmark in June 2026 and find that the best agent to date, Claude Opus 4.8, completes 89% and takes an unintended harmful action on 2.5%. Aside from this considerable progress in frontier agent performance, three things stand out. First, capability and safety go together on WorkBench rather than trade off, so the models that finish the most tasks also do the least unintended damage. Second, while several classes of error have been totally eliminated, frontier models still make some basic mistakes that occasionally result in irreversible harm, such as sending an email to the wrong person. Third, the rise of open-weight models has drastically lowered costs for a performance level that was previously only accessible to proprietary models, while frontier costs have stayed relatively stable. We release an updated version of the benchmark with data and code quality improvements, new model scores, and analysis of agent progress on WorkBench since 2024.

---


### 8. [Refusal Beyond a Single Direction: A Preliminary Comparison of Diff-in-Means and INLP](https://arxiv.org/abs/2606.13720)

**<font color=#1a73e8>作者：</font>** Elisabetta Rocchetti, Alfio Ferrara  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Arditi et al. (2024) has shown that refusal in safety fine-tuned chat models is mediated by a single linear direction in the residual stream, recoverable by a difference-in-means (DiM) of harmful and harmless activations. We compare DiM-based interventions (activation addition and directional ablation) with two interventions derived from Iterative Nullspace Projection (INLP) -- nullspace projection and counterfactual flipping -- on five open-weight chat models, asking whether INLP can match DiM at steering refusal and whether its richer parameterisation yields more tweakable interventions. INLP counterfactual flipping is competitive with DiM directional ablation on refusal suppression, while nullspace projection is consistently weaker. Restricting INLP to the leading directions of the extracted subspace preserves most of the suppression effect at near-baseline perplexity, giving a tunable capability. Geometrically, the two INLP interventions land in qualitatively different regions of activation space: nullspace projection collapses transformed activations \emph{between} the harmful and harmless clusters, while counterfactual flipping moves them into the opposite cluster, suggesting that the model encodes the absence of a concept differently from its opposite -- an intriguing distinction that warrants further investigation in future work.

---


### 9. [Morphology-Aware Sample Assignment: Overcoming IoU Insensitivity for Surface Defect Detection](https://arxiv.org/abs/2606.13723)

**<font color=#1a73e8>作者：</font>** Pengfei Liu, Yuhan Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intersection-over-Union (IoU), as a pivotal metric for evaluating the spatial alignment between candidate proposals and ground-truth annotations, directly determines the quality of positive sample sets and the training efficacy of visual detection models. Through theoretical modeling and analysis, we uncover a non-sensitive region on the IoU response curve, within which samples yield nearly identical IoU scores despite distinct geometric overlaps. To overcome this limitation, we introduce a set of morphological similarity metrics covering area, shape, and aspect ratio, to refine the positive sample assignment process, thereby ensuring more discriminative and reliable matching. A supplementary matching score is derived via mean-based aggregation of these multidimensional similarities, compensating for the intrinsic limitation of IoU in representing structural correspondence. Theoretically, incorporating morphological similarity reshapes the response distribution of the matching function, yielding both effective directional gradients and polygon-like iso-response contours, which tightly confine high-response regions around each ground-truth instance and substantially enhance the precision of positive sample selection. Experiments based on the YOLOv9 framework demonstrate consistent performance gains on both NEUDET and GC10- DET datasets. Notably, the proposed approach is fully plug-and-play and incurs zero additional inference overhead, thereby ensuring deployment efficiency for industrial visual inspection.

---


### 10. [When Sample Selection Bias Precipitates Model Collapse](https://arxiv.org/abs/2606.13732)

**<font color=#1a73e8>作者：</font>** Xinbao Qiao, Xianglong Du, Wei Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The proliferation of recursive training on synthetic data can alleviate data scarcity but risks model collapse, where repeated training erodes distributional tails and homogenizes outputs. Data selection is widely viewed as a remedy, yet its reliability depends critically on the reference distribution used by the verifier. We show that in low-resource verification regimes, where each verifier observes only a small, fragmented, and biased slice of the target manifold, selection itself becomes biased. This situation naturally arises in low-resource data silos such as healthcare consortia or proprietary financial institutions, where raw data cannot be pooled and local references are inherently incomplete. As a result, selection preferentially retains samples aligned with the local manifold while pruning globally relevant tail modes, turning from a safeguard against collapse into a mechanism that precipitates it. We theoretically prove that such siloed selection accelerates collapse and induces power-law diversity decay. As an initial mitigation, we construct Wasserstein proxy references from multiple silos without sharing raw data. Empirical results confirm that local-reference selection fails on skewed distributions, whereas collaborative proxy references mitigate diversity degradation, suggesting that recursive synthetic-data pipelines require particular caution when real-data coverage is fragmented or scarce.

---


### 11. [AI Receptivity or AI Adoption Breadth? A Tool-Specific Reanalysis of the Lower-Literacy/Higher-Usage Link](https://arxiv.org/abs/2606.13734)

**<font color=#1a73e8>作者：</font>** Hristo Inouzhe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent evidence reported by Tully, Longoni, and Appel (2025) suggests that lower artificial intelligence (AI) literacy predicts greater receptivity toward AI. We revisit this claim using the public data from Study 3 of that article, which measures past usage of five AI tool categories on a five-point frequency scale. We first reproduce the negative association between AI literacy and aggregate AI usage using OLS on participant-level averages, binary logit, ordered logit, and multinomial logit specifications. We then show that the aggregate relationship masks substantial heterogeneity by tool type. In our demographic-adjusted primary specification, AI literacy does not significantly predict text AI usage (ordered-logit $\beta$ = -0.090, p = .387), whereas it remains a strong predictor of non-text AI adoption ($\beta$ = -0.377, p < .001). The non-text effect is also robust under Tully et al.'s original Study 3 control specification ($\beta$ = -0.502, p < .001). Binary, ordered-logit, and multinomial specifications suggest that the non-text relationship is primarily an adoption/non-adoption pattern rather than evidence of intensive use: the demographic-adjusted odds ratio of ever having used a non-text AI tool is 0.68. Thus, in the study that measures self-reported past usage rather than stated preferences, the evidence does not support a simple claim that lower AI literacy predicts greater receptivity to AI in general. It points instead to a narrower pattern of broader adoption across lower-penetration, non-text AI tools.

---


### 12. [Connections Between Pairs of Filters Improve the Accuracy of Convolutional Neural Networks](https://arxiv.org/abs/2606.13736)

**<font color=#1a73e8>作者：</font>** Kathleen Anderson, Philipp Grüning, Erhardt Barth  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While researchers continue to find new and improved network structures for CNNs, most of the newly invented architectures still rely on the traditional pattern of stacking convolutional blocks and separating them with pointwise activation functions. However, there are drawbacks to a network purely building on pointwise nonlinearities. One alternative is to introduce a pairwise connection between two filters of a network. Typical connection functions use multiplications or the minimum operation to realize logical AND connections. In this paper, we go one step further by demonstrating that CNNs can benefit from more general connections, which include parameters that are learned. With such parameters, the network is able to implement different connections in different network layers and better adapt the connection function to the task at hand.

---


### 13. [FreoStream:Enhancing Stream Guardrails via Future-Aware Reasoning and Safety-Aligned Optimization](https://arxiv.org/abs/2606.13737)

**<font color=#1a73e8>作者：</font>** Jianwei Wang, Guoyang Shen, Yanhong Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stream guardrails enable token-level safety detection before full responses are generated. However, they often make overly conservative judgements and block those sensitive but safe tokens, which is known as over-refusal. Due to lack of full context, they also fail to detect implicitly harmful content from jailbreaking. To address these challenges, we propose FreoStream, a novel streaming guardrail framework. Specifically, FreoStream fine-tunes a LoRA module to perform Future-Aware Reasoning when the base guardrail detects unsafe tokens. The reasoning process follows a Future-Reason-Judge paradigm: predict the future, reason about the full context and give the final judgement. This design can effectively reduce over-refusal by incorporating the future information. Moreover, we introduce the Safety-Aligned Optimization module that extracts the safety-aligned component from the reasoning gradients to update the base guardrail model, thereby enhancing streaming safety detection. Extensive experiments on various safety benchmarks demonstrate that FreoStream achieves lower over-refusal rates and better jailbreak defense compared to existing streaming guardrails.

---


### 14. [High-Frequency Pricing at Scale for E-Commerce](https://arxiv.org/abs/2606.13741)

**<font color=#1a73e8>作者：</font>** Stefan Birr, Tobias Huelden, Mones Raslan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents the design, development, and implementation of a specialized forecast-then-optimize algorithmic pricing tool for sales campaigns in fashion e-commerce. Sales events present unique challenges for pricing including volatile demand patterns, rapid pricing decisions, and the need to balance short-term revenue with long-term profitability. We describe our approach combining daily-resolution demand forecasting using gradient-boosted trees with a multi-objective optimization framework that maximizes both long-term profit and net merchandise value for more than 5 million articles. Our solution addresses key limitations of existing weekly-granularity systems by implementing a forecast-then-optimize architecture that reduces pricing decision time from hours to minutes. We validate our approach through 23 A/B tests across 12 markets during 2023-2024 sales campaigns at Zalando, one of Europe's leading online fashion retailers. Experimental results demonstrate that the new pricing system achieves approximately 6% higher profit while maintaining equivalent performance on sales and revenue compared to the previous manual-algorithmic hybrid approach. Based on these results, the algorithm was successfully deployed to production and now handles the majority of algorithmic pricing decisions for sales campaigns at the company.

---


### 15. [A fully GPU-based workflow for building physics emulators of hypersonic flows](https://arxiv.org/abs/2606.13742)

**<font color=#1a73e8>作者：</font>** Fabian Paischer, Dylan Rubini, Deniz A. Bezgin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability to resolve complex physical phenomena with high fidelity and at low computational cost is central to addressing key challenges in modern engineering. A prime example lies in hypersonic flows, where the precise prediction of the full flowfield topology, in particular with respect to shock wave location and intensity, is critical. Yet supersonic and hypersonic flows continue to be a stumbling block for traditional reduced-order models and neural emulators that struggle to capture steep gradients in flow states with physical consistency in applications of industrial relevance. To that end, we introduce a fully GPU based workflow that integrates accelerated data generation with the training of neural emulators augmented by uncertainty quantification and physics-aware refinement. Our workflow is enabled by a differentiable high-fidelity solver (JAX-Fluids) which we employ for rapid dataset creation and residual-based improvement of the neural emulator to enhance physical consistency. Building on this framework, we first present a suite of model architectures and analyze their scaling behavior to expose their strengths and shortcomings. We then show that residual-based refinement enables training on cases where only mesh and input parameters are available, substantially reducing residuals and improving physical consistency. Together, differentiable simulation and residual-based refinement yield physics emulators that remain reliable beyond their training distribution, a key requirement for deploying surrogates in real-world engineering design loops.

---


### 16. [FedSPC: Shared Parameter Correction for Personalized Federated Learning](https://arxiv.org/abs/2606.13748)

**<font color=#1a73e8>作者：</font>** Kannanthodath Induchoodan Ajay Menon, Christian Prehofer, Yunfei Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized federated learning (PFL) is one of the important approaches in federated learning for addressing statistical heterogeneity while enabling client-specific adaptation. Many PFL methods split the model into shared and personalized parameters, which are jointly trained on each client. However, this creates an optimization issue: shared parameters are updated by clients optimizing different local objectives, which can lead to inconsistent shared updates and weaken the shared representation. To address this problem, we propose Federated Shared Parameter Correction (FedSPC), a modular correction method for PFL. FedSPC applies control-variate correction only to the shared parameters of a given PFL method, while leaving personalized parameters unchanged. It can be integrated into three common PFL settings: shared feature extractors, shared classifiers, and fully shared models with local regularization. Experiments on CIFAR-100 and Tiny-ImageNet with ViT, ResNet-34, and VGG-11 show that FedSPC improves performance across representative PFL methods, including FedPer, FedRep, FedBABU, LG-FedAvg, and Ditto.

---


### 17. [Which Models Perform Better in Inheritance Reasoning?](https://arxiv.org/abs/2606.13751)

**<font color=#1a73e8>作者：</font>** Mohammed Amine Mouhoub, Chahinez Bouchekif  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the participation of team PSL in the QIAS 2026 Shared Task on Arabic Islamic inheritance reasoning. The task evaluates the ability of large language models to solve inheritance cases that require legal interpretation, multi-step reasoning, and precise numerical computation. We compare \textit{commercial} and \textit{open-source} models under a unified prompting strategy to assess their effectiveness in structured legal reasoning with minimal task-specific adaptation. \\ Our results show a clear gap in reliability between the two model families. Commercial models demonstrate stronger performance in identifying eligible heirs, applying exclusion rules, and maintaining consistency across reasoning steps. In contrast, open-source models exhibit greater instability, particularly in cases involving dependent legal decisions and fractional share adjustments. The best performance is achieved by \textit{Gemini 2.5 Flash}, with an MRE of $0.989$.

---


### 18. [The Weight Norm Sets the Grokking Timescale: A Causal Delay Law](https://arxiv.org/abs/2606.13753)

**<font color=#1a73e8>作者：</font>** Truong Xuan Khanh, Doan Hoang Viet, Luu Duc Trung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking is the delayed onset of generalization in neural networks, arising long after they fit the training data. Whether the weight norm causes this delay is disputed: some studies report a critical norm at the transition, others observe grokking with no fixed norm at all. We settle this by intervening on the norm during training rather than only observing it. Under free training with weight decay, networks grok when the weight norm reaches a value Wc that varies little across seeds and learning rates (CV 1 to 2 percent) and grows with the modular base as a power law. When we instead clamp the norm to a fixed multiple rho of Wc and hold it there, the network still groks, but the delay follows T_grok proportional to exp(alpha rho). One exponent, alpha near 7.5, fits this delay across four moduli (R^2 = 0.996). Over the swept ranges the held norm moves the delay by about 19x and the learning rate by only about 2x, and holding the norm above Wc slows grokking rather than preventing it. A final LayerNorm removes the dependence by decoupling weight scale from the network function; without it the exponential law returns. This pinned-norm delay is the exponential counterpart to the logarithmic delay predicted for a freely contracting norm.

---


### 19. [D2H-AD: A Hybrid Model Utilizing Hyperdimensional Computing for Advanced Anomaly Detection](https://arxiv.org/abs/2606.13754)

**<font color=#1a73e8>作者：</font>** Ghazal Ghajari, Elaheh Ghajari, Ashutosh Ghimire 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection is a fundamental component of intelligent systems with applications in healthcare, cybersecurity, smart grids, and IoT environments. Although conventional machine learning and deep learning methods have demonstrated effectiveness in identifying anomalies, they often rely on large labeled datasets, incur high computational costs, and face scalability challenges in edge and high-dimensional settings. This paper presents D2H-AD, a novel anomaly detection framework based on Hyperdimensional Computing (HDC), a brain-inspired paradigm that represents information using high-dimensional distributed vectors. Unlike existing HDC-based methods, D2H-AD integrates distance-based similarity and density-aware encoding within a unified framework, improving anomaly representation and detection performance. Ablation studies show that hyperdimensional encoding alone yields up to 5.4% higher ROC-AUC than applying the same density-distance scoring directly in the original feature space. Furthermore, D2H-AD consistently outperforms five established baselines, namely HDAD, ODHD, One-Class SVM, Isolation Forest, and Autoencoders, across all evaluated datasets. The framework is lightweight, interpretable, and computationally efficient, making it suitable for resource-constrained and real-time applications. We validate D2H-AD on five benchmark datasets and demonstrate superior F1-score and ROC-AUC performance, together with robustness to class imbalance, noise, and data complexity. In addition to improved accuracy, D2H-AD offers scalability, a small memory footprint, and low-latency operation enabled by binary computations and a compact design. These properties make it particularly attractive for TinyML and edge AI deployments. The proposed framework highlights the potential of HDC for accurate, interpretable, and energy-efficient anomaly detection in dynamic environments.

---


### 20. [SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents](https://arxiv.org/abs/2606.13757)

**<font color=#1a73e8>作者：</font>** Rui Melo, Riccardo Fogliato, Sean Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) reviewers are increasingly used in pull-request (PR) workflows, where their approvals help decide which code is merged into a repository. This raises a question that benchmarks for static vulnerability detection or code generation do not address: can an automated reviewer reject a malicious contribution when the attacker controls both the code change and the accompanying PR text? We introduce SEVRA-BENCH (Social Engineering of Vulnerabilities in Review Agents), a benchmark that measures how often an automated reviewer approves such adversarial pull requests. Each malicious PR in SEVRA-BENCH is built from a real project commit that previously fixed a vulnerability listed in the Common Vulnerabilities and Exposures (CVE) database. We automatically invert that fix to restore the original vulnerable code and submit it as a pull request wrapped in one of 15 social-engineering framings, which vary the claims made, the supporting evidence, the urgency conveyed, signals of prior approval, and appeals to authority. SEVRA-BENCH contains 1,062 malicious PRs drawn from Common Vulnerabilities and Exposures (CVE)-linked fixes across the top 10 entries of the 2025 Common Weakness Enumeration (CWE) Top 25. In a realistic setting, we evaluate 8 current LLMs as code review agents on PRs that introduce vulnerabilities previously reported in public disclosures. Our results reveal a sharp gap in security capabilities between closed- and open-source models. We hope SEVRA-BENCH will serve as a valuable resource for advancing open-source models and narrowing this gap.

---


### 21. [Beyond LoRA: Is Sparsity-Induced Adaptation Better?](https://arxiv.org/abs/2606.13767)

**<font color=#1a73e8>作者：</font>** Elijah Cadenhead, Cristian McGee, Xin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) and its variants provide a memory- and compute-efficient alternative to full fine-tuning of pre-trained models. However, questions remain about the comparative generalizability of these approaches and how the structural restrictions on low-rank updates preserve effective adaptation performance. We present a historical framing, covering the past (full fine-tuning and original LoRA), the present (different variants of LoRA), and propose simpler, cheaper, parameter-efficient extensions by inducing sparsity within existing LoRA variants: Cheap LoRA (cLA), training a single low-rank factor with the other fixed (deterministically or, in its randomized variant, stochastically), and the chained circulant variant, ${c}^3$LA. We frame cLA as a structured instance of asymmetric LoRA, serving as a controlled column-subspace restriction of full fine-tuning. We derive information-theoretic generalization error bounds for these variants, marking one of the first endeavors in this area. Empirically, we evaluate 11 fine-tuning methods across 10 pre-trained models and 14 datasets, analyzing the fine-tuned models' performance and generalization using tools such as loss landscapes and spectral analysis. Despite the sensitivity of fine-tuned models to the pre-trained model, datasets, and other factors, our study suggests that restricting LoRA-based PEFT methods' adaptation to a sparse, structured column space remains competitive across tasks with their parameter-matched baselines while reducing up to 10% training time and peak GPU memory up to 15%, even with a naïve, non-optimized, sparse implementation. Our theoretical and empirical generalization measures provide a more consistent and principled approach to their cost-effective adaptation than commonly used analytical tools. Overview and code are available at: this https URL.

---


### 22. [CineOrchestra: Unified Entity-Centric Conditioning for Cinematic Video Generation](https://arxiv.org/abs/2606.13768)

**<font color=#1a73e8>作者：</font>** Sharath Girish, Tsai-Shien Chen, Zhikang Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cinematic video depicts multiple subjects acting or interacting at specific moments, captured with deliberate camera movement, and stitched together by shot transitions. Together, these elements demand a level of fine-grained control beyond current text-to-video models. Existing work addresses each axis in isolation: multi-subject personalization, temporal control, multi-shot synthesis, or camera control; no prior framework jointly integrates all four. We present CineOrchestra, a unified video diffusion model that controls subjects, events, cameras, and shot transitions simultaneously. Our key insight is that these heterogeneous cinematic elements share a fundamental structure: each is an entity acting over a specific temporal interval, which can therefore all be expressed through one shared structure of entity-centric conditioning primitives, augmented with reference images for visual entities. This formulation reduces the architectural challenge to a single positional encoding problem, which we solve with two parameter-free coordinated rotary embeddings: (a) an interval-sampled temporal RoPE that yields consistent attention behavior across events of dramatically varying duration, and (b) a 2D entity-temporal cross-attention RoPE that disambiguates per-entity conditions and routes each to its corresponding spatiotemporal region. On two new benchmarks, CineOrchestra outperforms six per-axis specialists on dense caption following and shot-transition timing, with consistent gains in a pairwise user study and component ablations.

---


### 23. [Diffusion Policy Optimization without Drifting Apart](https://arxiv.org/abs/2606.13795)

**<font color=#1a73e8>作者：</font>** Haozhe Jiang, Haiwen Feng, Pieter Abbeel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL post-training has become increasingly pivotal for improving diffusion policies, but existing diffusion policy-gradient methods are often unstable and cannot achieve reliable policy improvement. We identify the cause as the double-drift phenomenon: optimizing a variational surrogate can let the ELBO separate from the true log-likelihood, which then makes the resulting proxy policy gradient misaligned with the true policy gradient of expected return. We propose \textbf{DiPOD}, a diffusion policy optimization framework that maintains tight-bound behavior throughout training by interleaving self-distillation with policy-improving gradient updates. This leads to a simple and practical algorithm: augmenting each diffusion policy-gradient update with an on-policy ELBO regularizer. Across diffusion language model post-training and continuous-control diffusion policies, DiPOD substantially stabilizes training and reaches higher rewards than previous methods.

---


### 24. [Smart Blockchain-Based Access Control for the Internet of Things](https://arxiv.org/abs/2606.13798)

**<font color=#1a73e8>作者：</font>** Mahdi Manavi, Yunpeng Zhang, Guoning Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Securing access control in large-scale Internet of Things (IoT) deployments requires mechanisms that adapt to risk while preserving low latency for benign traffic. Permissioned blockchains such as Hyperledger Fabric offer auditability through smart contracts, but static endorsement policies impose the same validation depth on all requests, regardless of security posture. We propose a risk-adaptive enforcement layer for Hyperledger Fabric that couples an off-chain LSTM-based risk oracle with deterministic on-chain checks. The oracle assigns each request to a tier (Low, Moderate, High) and issues a signed attestation bound to the client identity and target key/version. Endorsing peers verify the attestation in chaincode and enforce tier-conditioned SBE policies without modifying the ordering service or consensus. Experiments on a Fabric testbed show that tier-conditioned endorsement strengthens validation for higher-risk requests while retaining low confirmation latency for benign workloads.

---


### 25. [Neural Variability Enhances Artificial Network Robustness](https://arxiv.org/abs/2606.13801)

**<font color=#1a73e8>作者：</font>** Robin Preble, Praveen Venkatesh, Stefan Mihalas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural responses in cortex exhibit substantial trial-to-trial variability in response to repeated stimuli, while peripheral sensory neurons respond far more consistently, leading many to wonder whether stochasticity may carry meaning. Existing work has argued that noise and signal correlations may be optimized for discrimination in animals, whereas artificial neural network (ANN) studies have shown similar benefits of noise in machine learning tasks, although most ANN work has neglected the effects of correlations. Here we investigate whether correlated noise improves the robustness of artificial neural networks to adversarial attacks and naturalistic image modifications. Using the covariance of activations under modified versus clean inputs, we find that structured noise may significantly improve network robustness. Robustness to naturalistic image modifications benefits most from structure, but this structure transfers poorly across modification types. In contrast, noise structure from adversarial attacks can generalize to other kinds of attacks. These results suggest that structured noise in ANN activations generally improves robustness, establishing a biologically plausible strategy for creating robust artificial neural networks that only relies on local information.

---


### 26. [Neural Slack Variables for Shape Constraints](https://arxiv.org/abs/2606.13803)

**<font color=#1a73e8>作者：</font>** Ruben Wiedemann, Antoine Jacquier, Lukas Gonon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enforcing functional inequality constraints such as monotonicity and convexity in neural networks is a fundamental challenge in many industrial and scientific applications. Classical one-sided penalty methods, along with primal-dual methods gated by complementary slackness, provide constraint gradients only at violated locations, resulting in fragile satisfaction. Architectures that guarantee feasibility by construction, on the other hand, remain largely limited to elementary cases and impose additional inductive biases. We introduce neural slack variables, a deep learning native primal-side approach that converts constraint enforcement into a regression problem by coupling the primary network with a jointly learned auxiliary network. The auxiliary network serves as a valid target for the primary network's constraint quantities, inducing feasibility and regularity. Neural slack variables achieve zero measured violations on dense-grid monotonicity and convexity test cases, where penalty and primal-dual baselines leave residual violations, and enable arbitrage-free learning of volatility surfaces, an open industrial challenge in quantitative finance.

---


### 27. [Compressing Image Style Training into a Single Model Forward](https://arxiv.org/abs/2606.13809)

**<font color=#1a73e8>作者：</font>** Zhongjie Duan, Yingda Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based style transfer must balance inference efficiency with stylization fidelity. Adapter-based methods are efficient, but they inject style as an external condition and can either weaken reference-specific appearance or copy reference semantics into the generated image. Optimization-based personalization methods such as LoRA internalize style more effectively, but require a separate training process for every new style. We introduce i2L (image-to-LoRA), a framework that amortizes style LoRA training into a single forward pass. Given one or more reference images, i2L predicts LoRA weights for a text-to-image model, enabling immediate style instantiation without per-style optimization. The architecture combines an image encoder, learnable LoRA queries, and compressed decoding heads that generate adapted matrices. Training on semantically diverse style pairs encourages the predictor to preserve appearance cues while suppressing reference-content copying. Experiments on Z-Image, FLUX.2, and Hidream-O1 show that i2L improves style fidelity, prompt alignment, and perceptual quality over existing baselines. Because i2L produces explicit LoRA weights, it also supports asymmetric classifier-free guidance, multi-reference style fusion, and composition with controllable-generation modules.

---


### 28. [Uncertainty Estimation and Generalization Bounds for Modern Deep Learning](https://arxiv.org/abs/2606.13818)

**<font color=#1a73e8>作者：</font>** Luis A. Ortega  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This thesis investigates how Bayesian principles can deepen our understanding of modern deep learning systems. While neural networks achieve remarkable predictive performance, their ability to generalize and to quantify uncertainty remains only partly understood. This thesis approaches this challenge from both methodological and theoretical angles: unifying Bayesian inference, function-space modeling, and large-deviation theory under a common probabilistic perspective.
On the methodological side, the thesis introduces the Deep Variational Implicit Process (DVIP), a scalable Bayesian framework that extends implicit processes to deep architectures. Complementing this, two post-hoc methods -- the Variational Linearized Laplace Approximation (VaLLA) and the Fixed-Mean Gaussian Process (FMGP) -- are proposed to equip pretrained deterministic networks with calibrated uncertainty estimates.
The theoretical contributions focus on one of the central open questions in modern machine learning: why do large, over-parameterized neural networks generalize so well? To address this, the thesis develops a unified probabilistic framework that connects three key mechanisms -- diversity, smoothness, and stochasticity -- within the language of PAC-Bayesian and large-deviation theory.

---


### 29. [Attention-Based Estimation of the Individual Treatment Benefit Probability under Dose Variation](https://arxiv.org/abs/2606.13821)

**<font color=#1a73e8>作者：</font>** Lev V. Utkin, Andrei V. Konstantinov, Stanislav K. Kogan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating the probability that a treatment outperforms a control for an individual patient, called the Individual Probability of Treatment Benefit (IPTB), offers a clinically intuitive alternative to population-average metrics. However, existing methods for IPTB estimation are largely confined to binary treatment settings, despite the prevalence of dose-varying interventions in clinical practice. We propose a general framework for IPTB estimation with ordinal outcomes under discrete dose assignments, called Dose-AIPTB (Dose Attention-based IPTB). Our approach recasts the problem as binary classification over the unobserved sign of the individual treatment effect, constructing pseudo-labels from covariate-similar pairwise comparisons and aggregating them via attention mechanisms or Nadaraya-Watson kernel regression. This formulation naturally accommodates multiple discrete dose levels, extending beyond the binary treatment paradigm. Through numerical experiments on real-world and synthetic data under covariate shift, varying sample sizes, and heterogeneous outcomes, we demonstrate that attention-based aggregation consistently outperforms kernel alternatives. The framework provides a foundation for personalized dose selection grounded in individual-level benefit probabilities. Codes implementing the model are publicly available at this https URL.

---


### 30. [A Stationarity-and-Coupling Criterion for Training-Free Time-Lagged Spectral Embeddings of Multivariate Time Series](https://arxiv.org/abs/2606.13823)

**<font color=#1a73e8>作者：</font>** Siddharth Pal, Viktoria Rojkova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study training-free fixed-length descriptors for multivariate time series and ask not merely whether such a descriptor performs well, but when it can be expected to work at all. Our object of study is $D(\tau)$, built from a time-lagged correlation matrix truncated at the Marchenko-Pastur edge so that only signal-bearing eigenvalues survive and classified by cosine similarity to class centroids with zero learned parameters. The central contribution is not the descriptor but a falsifiable applicability criterion for it. Working from a stationary Gaussian VAR(1) model, we argue that $D(\tau)$ separates two classes when the signals are approximately stationary and the class information lives in their cross-channel temporal coupling rather than in marginal per-channel power. We derive, semi-formally, three consequences: a distinguishability condition, why the static ($\tau=0$) covariance collapses to chance, and why a stationary but power-discriminated paradigm defeats the descriptor. The criterion is operational: a two-part pre-flight test -- an augmented Dickey-Fuller stationarity check and a power-baseline saturation check -- predicts applicability before any training. We validate both halves on a mixed assortment. On four paradigms that satisfy the criterion (Sleep-EDF, BCI-IV-2a, MIT-BIH, ESC-50) the descriptor is competitive with strong baselines at a fraction of their cost, reaching $88.5\pm4.5\%$ under 20-subject leave-one-subject-out on Sleep-EDF on a single CPU thread. On three that violate it -- non-stationary ERPs, and financial-volatility and wearable-stress regimes that are power-discriminated -- it fails exactly as the pre-flight predicts, and these negatives are the more informative half. We are explicit that $D(\tau)$ is not the most accurate representation; its value is a compact, training-free embedding whose domain of validity is known in advance.

---


### 31. [Safety-Contract Graph Multi-Agent Reinforcement Learning for Autonomous Network Security Response](https://arxiv.org/abs/2606.13832)

**<font color=#1a73e8>作者：</font>** Jose Luis Lima de Jesus Silva  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous network-security response systems promise to reduce Security Operations Centre (SOC) reaction latency, but reward-only multi-agent reinforcement learning (MARL) can improve security reward while remaining non-deployable. We present a safety-contract graph MARL framework and instantiate it as ACD$^3$-GAT (Adaptive Constrained Counterfactual Decisioning with a Graph Attention Network encoder), an architecture that separates simulator observations from reusable operational budgets, constrained optimization, graph state encoding, and counterfactual action screening. We evaluate the method in CAGE Challenge 4, where agents operate under budgets for Mean Time to Recover (MTTR), false-positive response, and firewall change-management disruption. Across the benchmark, every unconstrained method violates the SOC downtime budget in 100% of evaluated episodes, with mean downtime proxy costs of 311-430 against a budget of 50. This complements prior CAGE Challenge 4 findings by showing that reward-only learning lacks operational discipline. Constrained MAPPO-GAT (C-MAPPO-GAT) isolates Lagrangian operational-cost control and budget-aware screening, while ACD$^3$-GAT adds budget context, CVaR tail-risk estimation, opponent-belief state, and Graph Counterfactual Risk Propagation (G-CRP). The replicated comparison includes three 200-episode seeds for IPPO, MAPPO-GAT, C-MAPPO-GAT, and ACD$^3$-GAT. C-MAPPO-GAT reduces downtime violation from 100% to 0.3% and mean downtime cost from 355.4 to 15.5 relative to MAPPO-GAT. ACD$^3$-GAT reduces mean downtime cost to 48.2 with a 13.8% violation rate, placing it on the safety-contract frontier rather than at the most conservative compliance point. Topology-seed and coupled adaptive Red-process stress tests preserve this contrast and show lower worst adaptive degradation for safety-constrained policies than reward-only MAPPO-GAT.

---


### 32. [Explaining RhythmFormer: A Systematic XAI Analysis of Periodic Sparse Attention for Remote Photoplethysmography](https://arxiv.org/abs/2606.13839)

**<font color=#1a73e8>作者：</font>** Louis Chen, Torbjörn E. M. Nordling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) transformers achieve low heart-rate error on benchmarks, yet their decisions remain opaque--a growing concern as rPPG moves toward clinical heart rate estimation. Existing rPPG XAI is dominated by qualitative heatmap inspection without quantitative faithfulness metrics or physiology-grounded validation, leaving a gap between visual plausibility and auditable evidence. We address this gap. First, we adapt four attribution methods (raw attention, rollout, flow, Beyond Intuition) to RhythmFormer's bi-level routing attention with top-$k$ selection. Second, we introduce a skin coverage metric quantifying how much attribution mass falls on skin regions. Third, we adapt the SaCo faithfulness coefficient from its original classification setting to rPPG regression by using the MAE between original and perturbed predicted rPPG waveforms as the perturbation impact. Applying these tools, we quantify a multi-hop leakage effect under sparse top-$k$ routing: attention rollout and flow almost completely restores the connections that individual refined-attention layers explicitly set to zero. Beyond Intuition mitigates this via its value-projection-weighted rollout and gradient-supported mask, attaining the highest median refined skin coverage ($0.83$ vs. $0.57$ for vanilla rollout) and faithfulness ($F=0.92$) among the evaluated methods on UBFC-rPPG. Validation across diverse datasets and model variants is needed. A case study on a low-SaCo outlier further shows all four methods recovering consistently once an artefactual region is replaced, suggesting consistent SaCo behavior across attribution families in this illustrative case. Together, these metrics move XAI for rPPG toward auditable numerical evidence about spatial alignment and perturbation faithfulness, i.e. trustworthy rPPG XAI.

---


### 33. [Rethinking the UI of GenUI: A Tale of Two Designs](https://arxiv.org/abs/2606.13843)

**<font color=#1a73e8>作者：</font>** Xiang `Anthony' Chen, Savvas Dimitrios Petridis, Tian Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> GenUI is an emergent class of AI tools that use large models to generate UI mock-ups based on users' high-level descriptions, promising to democratize UX design exploration for a broader audience. Most GenUI designs to date tend to inherit the conventions of conversational large models, such as ChatGPT and Gemini, where a user describes their design needs primarily via an unstructured prompt, and the tool then takes a depth-first approach, delving into the design right away and producing a high-fidelity prototype. In this research, we rethink how well this unstructured, depth-first, and high-fidelity GenUI design can support early-stage, 0-to-1 design exploration. To probe this question, we propose a contrastive design with structured input, breadth-first exploration, and low-fidelity generation. We then conducted a comparison study with 24 UX designers and product managers who conducted mini design exploration exercises using an existing GenUI tool and our contrastive GenUI tool. Findings reveal participants' perceived benefits and trade-offs of the two GenUI designs: structured input surfaces key facets but requires more work, raising entry barriers to start exploration; breadth-first workflow reveals more possibilities, but previewing UX ideas spanning many screens remains hard; and though low fidelity has value, professionals favor high fidelity because it fits practice and GenAI heightens fidelity expectations. We conclude with design implications for GenUI and similar AI-powered creativity support tools.

---


### 34. [Hybrid Classical-Quantum Variational Autoencoder for Neural Topic Modeling](https://arxiv.org/abs/2606.13852)

**<font color=#1a73e8>作者：</font>** Ivan Kankeu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural topic models enable scalable semantic discovery, but their integration with quantum hardware remains largely unexplored. We present a proof-of-concept hybrid classical-quantum variational autoencoder (VAE) for topic modeling, embedding parameterized quantum circuits within the VAE inference network while retaining a classical topic-word decoder. To address the resource constraints of quantum hardware, we propose a modified Gaussian Softmax posterior that decouples latent space dimensionality from the number of topics to be extracted, enabling the model to operate with a low-resource 10-qubit quantum device. On the AgNews dataset, the hybrid VAE outperforms state-of-the-art neural topic models (NTMs), reaching a $C_v$ coherence score of 0.71 and an NPMI score of 0.20 while preserving high topic diversity. For comparison, we also construct a fully classical variant, which also outperforms state-of-the-art models on AgNews and exhibits clear class separation in the latent space. These results demonstrate that hybrid VAEs are computationally viable even on NISQ-era devices and represent a promising direction for quantum-enhanced topic modeling.

---


### 35. [Information Flow Paths from RTL Traces](https://arxiv.org/abs/2606.13860)

**<font color=#1a73e8>作者：</font>** Calvin Deutschbein, Owyn Wyatt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security validation is an important yet challenging part of the hardware design process, yet, by convention, validation engineers are tasked with defining the threat model, specifying the relevant security properties, detecting any violations of those properties, and assessing the consequences to system security, each of which is manually intensive and may introduce errors. The combined technologies of information flow tracking and specification mining represent an automated approach to property generation and validation, but prior work on information flow tracking on RTL trace data was limited to find cases under which information flowed between registers, without reproducing full paths to capture how sensitive information propagates through a design. With the introduction of new technologies accelerating hardware analysis, we develop a novel approach for constructing information flow paths from register transfer level (RTL) trace data.

---


### 36. [Temporal Backtracking Search for Test-time Generative Video Reasoning](https://arxiv.org/abs/2606.13861)

**<font color=#1a73e8>作者：</font>** Sejoon Jun, Zheng Ding, Huangyuan Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While test-time scaling has revolutionized reasoning in large language models, generative video reasoning remains bottlenecked by a single-shot paradigm. We demonstrate that searching over denoising steps cannot rescue logically flawed rollouts because spatial trajectories commit early in the diffusion process. Root-level Best-of-N (BoN) sampling is similarly inefficient: reasoning errors cluster early in the temporal axis, and resampling blindly discards verified upstream progress. To unlock effective test-time scaling for video models, we introduce Temporal Backtracking Search (TBS), which shifts the search space to the temporal axis. TBS transforms video generation into an iterative generate-verify-restart loop via three core mechanisms: (1) variable-K conditioning to resume generation from arbitrary clean prefixes; (2) temporal process verification to localize failures and extract valid restart anchors; and (3) prefix-based search to reallocate compute toward extending correct trajectories rather than root resampling. Across algorithmic, navigation, and robotics domains, TBS Pareto-dominates matched-budget BoN. In a strict out-of-distribution setting where one-shot generation collapses (0.7% for BoN), TBS achieves 22.7%, with every solved episode stemming from a restarted branch. Ultimately, TBS reveals that the local reasoning competence of video models far exceeds what single-shot rollouts indicate, providing a scalable test-time framework to unlock it.

---


### 37. [SuperThoughts: Reasoning Tokens in Superposition](https://arxiv.org/abs/2606.13862)

**<font color=#1a73e8>作者：</font>** Zheyang Xiong, Shivam Garg, Max Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long Chain-of-Thought (CoT) reasoning improves LLM problem-solving but is computationally expensive due to sequential token generation. While recent works explore reasoning in continuous latent spaces to bypass discrete token generation, they often struggle with training stability and fail to scale to complex, long-horizon tasks due to lack of supervision signal. We propose SuperThoughts, which compresses pairs of consecutive CoT tokens into single latent representations and decodes two tokens per step via a lightweight Multi-Token Prediction (MTP) module. This preserves discrete token supervision at training time while doubling throughput at inference time. We finetune Qwen2.5-Math-1.5B-Instruct, Qwen2.5-Math-7B-Instruct, Qwen2.5-Math-14B-Instruct, and evaluate on MATH500, AMC, OlympiadBench, and GPQA-Diamond. With a confidence-based adaptive mechanism that falls back to standard decoding when uncertain, SuperThoughts achieves $\sim$20--30\% CoT length reduction while maintaining accuracy with minimal degradation (1-2 points accuracy drop on most tasks).

---


### 38. [RTL-Arrow: Hardware-to-Cloud Bridge](https://arxiv.org/abs/2606.13865)

**<font color=#1a73e8>作者：</font>** Calvin Deutschbein, Jimmy Ostler  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware Security at Willamette is a Willamette University affiliated research group studying the hardware-software interface of security critical services. Within our program, we noticed many researchers spent considerable development time learning to understand and manually parse traces-of-execution of hardware designs which are used to identifying whether vulnerabilities or weaknesses arise at the hardware, software, or interface level. We propose the "RTL-Arrow" framework, a framework to compile performant binaries which bridge the hardware/data divide. We translate the outputs of simulated hardware execution, as "value change dumps" into modern data science workflows as cloud-ready "dataframes", to standardize program verification across the hardware and software levels. We describe our approach, its benefits, and lessons learned from the process of packaging and distributing these libraries for our security research program.

---


### 39. [Muon$^p$: Muon with Fractional Spectral Powers](https://arxiv.org/abs/2606.13867)

**<font color=#1a73e8>作者：</font>** Yihe Dong, Will Sawin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon is an increasingly widely used optimizer that replaces a gradient $G=USV^\top$ with its polar factor $UV^\top$, thereby flattening the singular spectrum. However, full flattening discards singular-value information that may matter for adaptation. We introduce Muon$^p$, a Muon-style optimizer that instead uses fractional spectral-power updates $US^pV^\top$ for rational $p\in(0,1)$, interpolating between Muon and gradient descent. To make it practical, we prove that fractional spectral powers cannot be computed by any fixed univariate polynomial iteration, and furthermore derive low-degree odd bivariate recurrences that approximate $US^pV^\top$ using only matrix multiplications, preserving Muon's matrix-multiplication-only structure and compute complexity. We show that Muon$^p$ maximizes the linear improvement in loss under the Schatten $q$-norm for $q=1+\frac{1}{p}$. Empirically, Muon$^p$ is especially effective for finetuning: on billion-scale models, Muon$^p$ improves validation perplexity and downstream task performance. We further analyze when Muon$^p$ is less suitable, through the lens of spectral geometry. Our results reveal important insights on when preserving the singular spectrum can bring significant gains, and introduce a principled way to achieve them.

---


### 40. [Hyperdimensional computing for structured querying on tabular data embeddings](https://arxiv.org/abs/2606.13871)

**<font color=#1a73e8>作者：</font>** Sebastián Bugedo, Stijn Vansummeren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tabular data embeddings have become a cornerstone of data profiling and data integration pipelines, enabling tasks such as entity annotation and resolution; schema matching; column type detection; and table search, among others. Existing approaches embed rows, columns, or entire tables into a vector space and rely on nearest-neighbor search to retrieve candidate matches. A fundamental limitation of current embedding methods is the lack of interpretable similarity scores: the concrete similarity value between a query and its nearest neighbour carries no intrinsic meaning, making it impossible to determine whether that neighbour is a true match or simply the least-dissimilar item in a corpus that contains no valid answer. This inability to set principled thresholds for retrieval undermines practical deployment, particularly for zero-match detection.
We investigate the use of HyperDimensional Computing (HDC), specifically the Holographic Reduced Representations (HRR) model, as a framework for tabular row embeddings when the retrieval task corresponds to answering structured select-project queries in vector space. Exploiting the algebraic properties of HDC operations, we derive closed-form expected similarity values for both equality and non-equality retrieval predicates, which converge to interpretable values as dimensionality increases, and use these to identify suitable retrieval thresholds. We evaluate HDC against EmbDI, a graph-based baseline, on two real-world datasets across varying table sizes and predicate lengths. Our results show that HDC matches or outperforms EmbDI for row retrieval across all configurations, handles non-equality predicates more robustly, and achieves perfect attribute projection accuracy at sufficient dimensionality -- while uniquely enabling reliable identification of zero-match predicates through its principled thresholds.

---


### 41. [A Longitudinal Attribute-Conditioned Neural Network for Modeling Health-State Transition Probabilities in Temporally Irregular Data: The LANTERN Framework](https://arxiv.org/abs/2606.13880)

**<font color=#1a73e8>作者：</font>** Bright Kwaku Manu, Beckett Sterner, Petar Jevtic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of long-term care transition probabilities is central to disability insurance pricing, reserving, and solvency assessment. Classical actuarial multi-state models commonly rely on Markov, semi-Markov, or proportional-hazard specifications, which provide a direct connection to cohort projection but may be restrictive for irregular longitudinal health data with nonlinear aging patterns and heterogeneous covariate histories. This paper develops a well-calibrated estimator of multi-state transition probabilities for irregular longitudinal health data. The model learns from individual health history, incorporates the time elapsed between observations, and conditions transition probabilities on demographic and socioeconomic attributes. It produces a valid probability distribution over the next observed health state, with four possible states: healthy, mild disability, severe disability, and death. Individual probabilities are aggregated by age group and origin state to form transition matrices compatible with actuarial cohort projection. Using longitudinal data from the Health and Retirement Study, we compare the proposed estimator with logistic regression, gradient-boosted trees, a recurrent neural network, and a last-state persistence benchmark. The evaluation considers probabilistic accuracy, endpoint discrimination and calibration for severe disability and death, risk concentration, and transition matrix error after aggregation. The proposed estimator improves severe disability discrimination relative to logistic regression and gradient-boosted tree benchmarks, maintains strong calibration, and yields the lowest transition matrix error among the evaluated models in the held-out test analysis. Results show that a structured machine learning estimator can support long-term care transition modeling when judged by calibration and projection fidelity, beyond discrimination.

---


### 42. [Crypto x AI, AI x Crypto: A Survey](https://arxiv.org/abs/2606.13892)

**<font color=#1a73e8>作者：</font>** Sarah Allen, Pranay Anchuri, James Austgen 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The intersection of crypto x AI is spawning papers, products, online posts, and companies. All the surrounding buzz, though, obscures what exactly has been done, what the opportunities and challenges are, and what open questions deserve attention. This survey paper asks what AI can do for blockchain-based technologies (broadly construed as "crypto") (crypto x AI), and vice versa (AI x crypto). We systematize existing work, summarize key takeaways, highlight open research questions, and offer a perspective on pervasive industry misconceptions, concluding that AI and crypto are still in the very early stages of meaningful integration.

---


### 43. [Gefen: Optimized Stochastic Optimizer](https://arxiv.org/abs/2606.13894)

**<font color=#1a73e8>作者：</font>** Nadav Benedek, Tomer Koren, Ohad Fried  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AdamW is a default optimizer for modern deep learning, but its first and second moment states add roughly two parameter-sized buffers to training memory. We propose Gefen, a memory-efficient optimizer that automatically shares second-moment estimates across parameter blocks and quantizes the first moment using a learned codebook, thereby reducing AdamW's memory footprint by ~8x while maintaining the same performance, corresponding to a reduction of 6.5 GiB per billion parameters. The method is motivated by a theoretical result showing that large mixed Hessian entries constrain the ratio of squared gradients toward one, suggesting that Hessian-aligned parameters are natural candidates for sharing second-moment statistics. Since computing Hessians is impractical at scale, Gefen infers block structure from the initial squared gradients, requiring no architecture-specific metadata or hyperparameters beyond AdamW defaults. Gefen learns an exact histogram-based dynamic-programming quantization codebook and reuses the same blocks for first-moment scaling. Across diverse experiments, Gefen achieves the lowest peak optimizer memory among the compared AdamW-like methods while maintaining AdamW-level performance. In FSDP and DDP training, the reduced memory footprint enables larger microbatches and improves throughput significantly over AdamW, providing a practical drop-in replacement with lower memory usage that can increase throughput and enable training larger models or using larger batch sizes. We provide the complete Python implementation, including fused CUDA kernels at this https URL

---


### 44. [How do Self-Supervised Remote Sensing Vision Models Transfer to Downstream Tasks?](https://arxiv.org/abs/2606.13896)

**<font color=#1a73e8>作者：</font>** Julia Romero, Qin Lv, Morteza Karimzadeh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised geospatial foundation models (GeoFMs) learn transferable representations from remote sensing data, but their downstream behavior is difficult to characterize. We study six representative GeoFMs spanning joint-embedding, reconstruction, and multimodal pretraining families, and evaluate transfer across classification, regression, and segmentation benchmarks under different label availability and downstream pipelines. We find that model rankings change across tasks and adaptation settings. Layerwise probing shows that, in most cases, task-relevant information is more accessible in intermediate transformer blocks compared to final-layer embeddings, and that GeoFMs exhibit distinct depthwise profiles. In segmentation case studies on PASTIS and Sen1Floods11, downstream adaptation settings such as decoder design and fine-tuning can be as impactful as the choice of GeoFM, and standard dense-prediction heads may be poorly aligned with how GeoFMs organize information over depth. Finally, CKA analysis on case studies shows that fine-tuning does not rewrite GeoFMs uniformly across depth, and the strongest changes are localized to the first linear layer of the MLP in ViT blocks. These results help explain why GeoFM rankings shift across benchmarks and motivate more representation-aware evaluation and adaptation strategies.

---


### 45. [HiLo-Token: Input-Adaptive High-Low Frequency Token Compression for Efficient Image Editing](https://arxiv.org/abs/2606.13898)

**<font color=#1a73e8>作者：</font>** Haoran You, Yotam Nitzan, Lingzhi Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creative image editing tools, such as Photoshop's Remove or Generative Fill buttons, are central to everyday customer use and account for a major share of traffic in Photoshop and Lightroom. However, current generative AI models face significant latency challenges, which become even more pronounced when transitioning from convolution-based U-Nets to Diffusion Transformers (DiTs). In our evaluation on hundreds of representative image editing samples spanning a wide range of mask ratios, the DiT module alone accounts for an average of 73% of the total model latency, even after being distilled from 50 timesteps down to 8 timesteps. To tackle this challenge, we propose $\textbf{HiLo-Token}$, an input-adaptive token compression framework that allocates more token budget to high-frequency, rich-context regions while assigning fewer tokens to low-frequency areas. Specifically, for the editing region specified by the user mask, we retain all tokens within a dilated mask to preserve strong locality and contextual relevance. Outside the editing region, we introduce a simple yet effective high-frequency token selection strategy based on spatial frequency to capture important local details, while using tokens from a 16x downsampled image to represent low-frequency components and preserve the blurry but global structure. Extensive experiments on production-level evaluation data validate the effectiveness of the proposed method, achieving 3.13x, 2.59x, and 1.67x DiT speedups on A100-80GB for image editing tasks across small, medium, and large mask ratio categories with average ratios of 6.38%, 15.92%, and 35.36%, respectively, without any regression in generation quality.

---


### 46. [SpikF-GO: Spiking Fourier Graph Operators for Multivariate Time Series Forecasting](https://arxiv.org/abs/2606.13901)

**<font color=#1a73e8>作者：</font>** Jafar Bakhshaliyev, Niels Landwehr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) have emerged as an energy-efficient alternative to conventional neural networks, demonstrating strong performance in computer vision and robotics. More recently, SNNs have been applied to time series forecasting (TSF), with methods exploring spiking temporal backbones, spike-compatible positional encodings, Fourier-domain processing, and redesigned neuron dynamics. However, existing SNN forecasting approaches process variables independently, lacking explicit mechanisms for modeling inter-variable dependencies. This is a critical limitation in multivariate settings, where cross-variable correlations carry substantial predictive information. We propose Spiking Fourier Graph Operators (SpikF-GO), which addresses this gap by combining a hypervariate graph formulation in which every scalar observation becomes a graph node with spike-driven spectral processing. SpikF-GO introduces a Hard Concrete frequency gate for learnable sparse frequency selection and a Complex LIF gate that applies independent spiking neurons to real and imaginary Fourier components, preserving binary, event-driven computation throughout the spectral domain. We further present a variant incorporating Central Pattern Generator-based positional encodings for stronger long-range temporal modeling. Evaluated on eight benchmarks under a unified experimental protocol, SpikF-GO achieves the best average rank among all SNN methods and outperforms its ANN counterpart, FourierGNN, at reduced energy cost. SpikF-GO maintains competitive accuracy even at substantially smaller embedding dimensions, thereby achieving significant energy reductions. To our knowledge, this is among the first works to bring graph-based multivariate modeling into the spiking domain for TSF and the first to provide a unified comparison across SNN forecasting architectures under a common experimental protocol.

---


### 47. [SANA: What Matters for QA Agents over Massive Data Lakes?](https://arxiv.org/abs/2606.13904)

**<font color=#1a73e8>作者：</font>** Austin Senna Wijaya, Jiaxiang Liu, Haonan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Exploratory question answering (EQA) over data lakes requires an LLM agent to discover relevant sources, analyze retrieved data, and adapt its actions based on intermediate results. End-to-end accuracy alone cannot distinguish failures in search, planning, data analysis, or the agent's Action Policy: its decisions about what to do next and when to submit an answer. We present SANA (Search Agent Navigation Ablation framework), a diagnostic ablation framework that transforms EQA tasks into runtime profiles containing gold source sequence, sanitized subquestions, and execution records. SANA uses these profiles to construct idealized search, planning, and data-analysis tools, allowing each component to be ablated; the residual gap is diagnostic evidence for policy failures.
To illustrate SANA as a reusable evaluation framework, we adapted two recent EQA benchmarks, LakeQA and KramaBench, and evaluated lightweight and mid-sized agents under fixed prompts, budgets, data lakes, and runtimes. Across both benchmarks, data analysis is a consistent bottleneck while planning is less so. Search is a major limitation in LakeQA's large data-lake setting, but less so for the smaller-scale KramaBench. SANA thus deconstructs end-to-end task accuracies into a diagnosis of where data-lake agents fail, and allows for systematic comparisons of progress in search, planning, data analysis, and agent design.

---


### 48. [PMOF: A Dataset and Benchmark for Passenger Monitoring Using Overhead Fisheye Cameras](https://arxiv.org/abs/2606.13910)

**<font color=#1a73e8>作者：</font>** Stella Katharina Wermuth, Qazi Arbab Ahmed, Klaus Neumann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous staff-free public transport requires reliable in-vehicle passenger monitoring. However, perception inside moving vehicles is challenged by confined spaces, variable illumination, motion-induced background variation, occlusion, and limited viewpoints. To mitigate these spatial constraints, ceiling-mounted fisheye cameras provide full-scene coverage from a single viewpoint. Yet existing public overhead fisheye datasets are recorded in static environments and do not capture the domain shift introduced by vehicle motion. To fill this gap, we introduce PMOF, Passenger Monitoring using Overhead Fisheye cameras, the first public dataset of top-view fisheye imagery captured inside a moving vehicle, comprising over 19k manually annotated frames. PMOF provides rotated bounding boxes, tracking identifiers, and action labels, supporting object detection, tracking, and action recognition. We benchmark PMOF using YOLO26m-obb models fine-tuned under multiple dataset configurations that combine PMOF with existing overhead fisheye datasets. Cross-domain fine-tuning with custom rotation-aware augmentation achieves 94.8% AP50 on PMOF and 96.5% AP50 on an unseen overhead fisheye dataset from a different domain. Our results highlight the domain gap between static and moving environments and show that incorporating PMOF improves detection performance and advances generalization beyond passenger monitoring to broader fisheye-based person detection tasks. The dataset and code are available at this https URL.

---


### 49. [Overhead Wildlife Locator (OWL): Benchmarking Weakly Supervised Learning for Aerial Wildlife Surveys](https://arxiv.org/abs/2606.13911)

**<font color=#1a73e8>作者：</font>** Isai Daniel Chacón, Zhongqi Miao, Bruno Demuro 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated aerial wildlife surveys increasingly rely on deep learning, yet standard object detectors require bounding-box annotations, reported to be up to seven times slower and three times more expensive to produce than point-level labels. To address this bottleneck, we introduce the Overhead Wildlife Locator (OWL), a weakly supervised density-estimation framework with three variants: OWL-C, a fully convolutional model for high-throughput screening; OWL-T, a Swin-augmented hybrid for heterogeneous, cluttered scenes; and OWL-D, built on a frozen DINOv3 ViT-H+/16 encoder with a DPT-style fusion decoder. We benchmark all three against POLO, YOLOv11n, and YOLOv11l across five public aerial datasets, from sparse fixed-wing savanna surveys to dense UAV paddock imagery, and against the published HerdNet baseline on its native Delplanque split. OWL-D sets a new state of the art on Delplanque (0.934 AP vs. HerdNet's 0.840) and records the highest AP on four of the five datasets. Performance is regime-dependent: on the extreme-density SheepCounter UAV dataset the hybrid OWL-T leads (0.978 AP) and the convolutional variants attain the lowest counting error, whereas the foundation-based OWL-D degrades, indicating which variant suits which survey type. We further validate operational readiness on the Alaska Department of Fish and Game's 2022 Central Arctic Caribou census: under cross-herd and cross-temporal transfer, OWL-C fine-tuned on the 2017 Porcupine Caribou Herd split attains F1 = 0.965 on a held-out patch test set, with a signed count error of +3.1% aggregated across the released test patches. We release the OWL code, model weights, and the annotated Porcupine Caribou Herd 2017 (PCH) and Central Arctic Herd 2022 (CAH) patches, the first open patch-level datasets for large-scale caribou aerial surveys, at this https URL.

---


### 50. [A Multi-Agent AI System for Automated High School Transcript Processing: Collaborative Document Analysis at Scale](https://arxiv.org/abs/2606.13916)

**<font color=#1a73e8>作者：</font>** Ben Torkian, Jun Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Each year, college admissions offices face an overwhelming challenge: processing millions of high school transcripts, each with unique formats, grading systems, and layouts. This manual process creates operational bottlenecks that delay admissions decisions and consume valuable resources. We present a transformative solution through a multi-agent AI system where specialized agents collaborate to automatically process diverse transcript formats through intelligent coordination and communication. Our multi-agent architecture consists of three specialized agents-a Pattern Recognition Agent for format-specific parsing, a Semantic Analysis Agent for natural language understanding, and a Vision Intelligence Agent for multimodal document analysis-coordinated by an Orchestration Agent that manages agent communication and result reconciliation. Our key innovation lies in agent-based quality control using GPA extraction as a coordination signal, ensuring reliable agent collaboration and preventing critical information loss. When evaluated on 40 real world transcripts from high schools across 13 U.S. states, our agent system successfully processed every document, achieving 96.7% accuracy compared to expert manual review while maintaining practical processing speeds of 45 seconds per transcript. This work demonstrates how multi-agent coordination can solve complex document processing challenges, offering institutions a scalable, collaborative AI solution that preserves accuracy while dramatically reducing processing time.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-211](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
