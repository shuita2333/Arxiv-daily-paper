# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 251. [Anytime and Difficulty-Adaptive PAC-Bayes for Constrained Density-Ratio Network with Continual Learning Guarantees](https://arxiv.org/abs/2605.17212)

**<font color=#1a73e8>作者：</font>** Paulo Akira F. Enabe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A unified framework for learning under covariate shift is presented, in which a constrained density-ratio network approximates the Radon-Nikodym derivative $r^\star = dP/dQ$ from source $Q$ to target $P$, supports an importance-weighted empirical risk, and feeds an anytime PAC-Bayes generalization certificate. A change-of-measure identity decomposes the gap between target risk and importance-weighted source risk into a ratio-bias term, controlled by the $L^2(Q)$ closeness of the learned ratio to $r^\star$, and a generalization-gap term, controlled by the variability of the weighted loss. Three structural identities of a Radon-Nikodym derivative, normalization, moment matching, and a second-moment penalty controlling the effective sample size, are imposed as hard integral constraints through an augmented-Lagrangian scheme. PAC-Bayes is then instantiated on the weighted risk in a fixed-time regime that yields Bernoulli-KL bounds, a KL-regularized objective whose minimizer is the network-weighted Gibbs posterior, and a stability statement on $L^2(Q)$ perturbations of the learned ratio, and in an anytime regime that builds a time-uniform certificate by geometric peeling across epochs. A pre-registered two-campaign protocol combining a patch test against analytic ground truth with a real-data deployment under intrinsic distribution shift validates the framework. The network produces a calibrated covariate ratio on real data, reduces the target $0/1$ loss relative to unweighted empirical risk minimization and to classical direct ratio-estimation baselines, and attains the anytime certificate as the construction promises. A single pre-registered failure of the fixed-time coverage claim is recorded, with per-split coverage aligning one-to-one with the magnitude of the label shift, confirming that the covariate-only assumption is operationally tight rather than a defect of the certificate.

---


### 252. [Integration of AI in Cybersecurity: Current Trends with a Focused Look at Intrusion Detection Applications](https://arxiv.org/abs/2605.17219)

**<font color=#1a73e8>作者：</font>** S. Tazili, A. Mansour, M. Y. Chkouri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) is widely adopted today for its ability to detect patterns, automate tasks, and reduce time and cost across various applications. Its integration into Cybersecurity has garnered significant attention, particularly in areas such as intrusion detection, malware analysis, and phishing or spam detection. As AI and cybersecurity evolve, new methods and approaches emerge regularly. Current trends include the use of Generative AI, Natural Language Processing, Federated Learning for privacy-preserving collaborative training, and eXplainable AI to ensure interpretability and trust, which are vital in cybersecurity. This paper presents an interesting review of current AI-based cybersecurity trends, focusing on intrusion detection approaches and aiming to uncover meaningful insights through comparative analysis based on the employed AI techniques and reported performance.

---


### 253. [Triple-Hoisted Baby-Step Giant-Step Linear Transformation over CKKS Homomorphic Encryption and Hardware Accelerator](https://arxiv.org/abs/2605.17222)

**<font color=#1a73e8>作者：</font>** Sajjad Akherati, Xinmiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computations can be directly carried out over ciphertexts using homomorphic encryption (HE), which is indispensable for privacy-preserving cloud computing. Linear transformation is widely used in neural networks, including large language models. However, the implementation of linear transformation over HE requires a large number of ciphertext rotations, which incur significant memory and hardware overhead despite existing simplification techniques. This paper proposes a triple-hoisted baby-step giant-step algorithm that decomposes the baby step further to substantially reduce the number of ciphertext rotations needed for the CKKS HE evaluation of linear transformation. Moreover, to reduce off-chip memory access, which contributes to the majority of the latency, a memory-optimized data path is proposed by partitioning the algorithm into multiple phases. Furthermore, an efficient FPGA-based hardware accelerator with an optimized permutation circuit for message routing is designed for the proposed scheme. For a set of typical parameters, the proposed design reduces the off-chip memory access by 2.9x compared to the best prior design. Synthesized for Xilinx Virtex UltraScale+ devices, the proposed design achieves a 5.8x reduction in computational latency compared with the baseline design.

---


### 254. [FishBack: Pullback Fisher Geometry for Optimal Activation Steering in Transformers](https://arxiv.org/abs/2605.17231)

**<font color=#1a73e8>作者：</font>** Sihan Wang, Jiayi Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering methods modify intermediate representations of language models to control output behavior, but universally assume the activation space is Euclidean. We show this assumption fails drastically: the local geometry induced by the model's own output behavior -- the Fisher information metric of the softmax layer, pulled back through the Jacobian of subsequent layers -- deviates from the Euclidean metric by over 97% in relative spectral norm on GPT-2, with an effective dimensionality of only 2--17% of the ambient space. From this pullback Fisher metric, we derive a closed-form steering equation that identifies the minimum-distortion direction for any target concept, yielding a closed-form optimal direction at each point that can be applied iteratively without manifold fitting or data-driven geometry estimation. We call the resulting framework FishBack. The metric admits a layer-wise recursive decomposition, which reveals that existing methods -- CAA, ActAdd, ITI, and others -- each implicitly adopt a particular approximate metric, and that their performance gaps are quantitatively predicted by a single spectral diagnostic: the ratio of their implicit metric's cost to the Fisher-optimal cost. On GPT-2, iterative pullback steering consistently outperforms all Euclidean baselines across three verb-morphology concepts and four layers, with off-target KL reductions of $1.3\times$--$2.5\times$ relative to Euclidean gradient ascent and $1.5\times$ relative to CAA at matched concept probability.

---


### 255. [Dimension-Free Convergence of Discrete Diffusion Models: Adjoint Equations Induce the Right Space](https://arxiv.org/abs/2605.17232)

**<font color=#1a73e8>作者：</font>** Kelvin Kan, Xingjian Li, Benjamin J. Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion has become a leading framework for generative modeling in various applications including language, vision, and biology. Existing convergence theory, however, exhibits fundamental limitations. KL-based analyses diverge under singular priors such as the masked distribution, while bounds in total variation (TV) depend on the state space size $S$ and become vacuous for modern language tasks, where vocabularies contain hundreds of thousands of tokens. We develop a unified adjoint-equation-based framework that establishes dimension-free convergence guarantees in any integral probability metric (IPM). To the best of our knowledge, our bounds are the first to be entirely free of $S$ and applicable to both masked and uniform priors. Importantly, our theory relies only on a single standard rate-matrix regularity assumption and is compatible with time-inhomogeneous schedules.
Four novel techniques drive our improvements: working in the space of observables via adjoint equations rather than directly with probability measures, a regularity analysis that yields bounds on any IPM, a coupling argument that removes $S$-dependence under uniform transitions, and a score-marginal cancellation technique that removes $S$-dependence under masked transitions. Our framework thus sharply departs from prior analyses and avoids the shortcomings of pathspace-KL and existing TV-based approaches. Beyond convergence bounds, our framework provides a versatile toolkit for further theoretical study of discrete diffusion models.

---


### 256. [Active Budget Allocation for Efficient Scaling Law Estimation via Surrogate-Guided Pruning](https://arxiv.org/abs/2605.17234)

**<font color=#1a73e8>作者：</font>** Viktoria Schram, Markus Hiller, Daniel Beck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting model performance at larger scales enables the design of training strategies and architectures tailored to specific performance targets. Empirical scaling law research identifies functional forms to aid this prediction task. These describe the relationship between loss and compute using a loss-compute frontier defined by learning curves. Due to the empirical nature of this approach, the computational burden is substantial, making strategic resource allocation essential - yet it remains surprisingly underexplored. In this work, we address this shortcoming by exploring the suitability of Successive Halving (SH) and SH combined with parametric and non-parametric surrogate models. In addition to enabling a more systematic allocation of a given compute budget, our findings show that SH paired with surrogate models yields a set of learning curves that includes one with a lower loss-compute value than what naive uniform allocation or an SH-only approach can obtain. Our experiments demonstrate mean relative improvements of up to 2.84% and 5.47% on real-world and synthetic learning curve datasets. This strategic resource allocation enables us to obtain accurate scaling laws at significantly reduced computational costs, saving up to 98.7% over the traditional exhaustive approach.

---


### 257. [Systematic Evaluation of Vision Transformers for Automated Cervical Cancer Classification: Optimization, Statistical Validation, and Clinical Interpretability](https://arxiv.org/abs/2605.17236)

**<font color=#1a73e8>作者：</font>** Nisreen Albzour, Sarah S. Lam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual Pap smear analysis for cervical cancer screening is limited by inter-observer variability, time constraints, and restricted expert availability. Although convolutional neural networks (CNNs) have automated cervical cell classification, they remain limited in modeling long-range spatial dependencies and often lack clinical interpretability. In this study, Vision Transformer (ViT) architectures were systematically optimized to enhance automated cervical cancer screening, which resulted in improved interpretability. The Herlev dataset (917 images: 242 normal, 675 abnormal) was utilized to optimize ViT-Tiny, a lightweight Vision Transformer architecture designed for reduced computational complexity, through a comprehensive evaluation of augmentation strategies, class weighting, and hyperparameters. The optimal configuration achieved 94.9%-95.2% cross-validation accuracy, in which random horizontal flipping and class weighting (0.7 x 1.3) were identified as most effective. Gradient-weighted Class Activation Mapping (Grad-CAM) analysis confirmed that model attention corresponded to clinically relevant morphological features, which include nuclear regions, cell boundaries, and chromatin texture, which align with cytopathological criteria. These findings indicate that Vision Transformers can deliver accurate and interpretable decision support for cervical cancer screening, which fulfills both clinical performance and transparency requirements essential for medical AI deployment.

---


### 258. [Learning in Position-Aware Multinomial Logit Bandits: From Multiplicative to General Position Effects](https://arxiv.org/abs/2605.17238)

**<font color=#1a73e8>作者：</font>** Xi Chen, Shibo Dai, Jiameng Lyu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the dynamic joint assortment selection and positioning problem, where the attraction of each product depends on both its intrinsic appeal and its display position under a Multinomial Logit (MNL) choice framework. Our study ranges from the multiplicative position effects model, in which each product's attraction is scaled by a position-specific factor, to a general position effects model assigning independent attraction parameters to every product--position pair to capture heterogeneous synergies. For both models, we design round-based learning algorithms that update decisions after every single feedback, and establish the first regret-optimal characterization. Besides, our round-based algorithms provide the prompt operations needed by modern platforms. For the multiplicative model, we develop a cross-position pairwise maximum likelihood estimator with a clipping mechanism, and prove that our algorithm P2MLE-UCB attains a regret of $\tilde{O}(\sqrt{NT})$, matching the lower bound and closing the $\sqrt{K}$ gap left by prior epoch-based analyses. For the general model, we establish a minimax lower bound and propose GP2-UCB with a matching upper bound. Moreover, we design an efficient subroutine for the per-round joint assortment and positioning optimization based on Dinkelbach's method and maximum-weight bipartite matching. Numerical experiments on synthetic data and the Expedia dataset show that our algorithms consistently outperform state-of-the-art benchmarks.

---


### 259. [Drift Flow Matching](https://arxiv.org/abs/2605.17244)

**<font color=#1a73e8>作者：</font>** Chenrui Ma, Xi Xiao, Lin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative generative models such as Flow Matching and Diffusion models have demonstrated strong test-time scaling behavior, where additional inference computation can improve generation quality. In contrast, Drift Models offer efficient one-step generation, but their direct generation paradigm limits such flexibility. In this work, we propose Drift Flow Matching (DFM), a framework that connects drifting generative modeling with flow-based iterative generation. DFM preserves the efficiency of direct transport maps while enabling generation to be refined through multiple inference steps when desired. This bridges the gap between one-step Drift Models and multi-step Flow Matching methods, and provides a novel generative paradigm that can adapt sampling computation to different quality--efficiency requirements. Extensive experiments across different tasks and datasets demonstrate the effectiveness and generality of the proposed framework.

---


### 260. [Towards Robust Argumentative Essay Understanding via TIDE: An Interactive Framework with Trial and Debate](https://arxiv.org/abs/2605.17247)

**<font color=#1a73e8>作者：</font>** Zheqin Yin, Yupei Ren, Yadong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Argumentative essays serve as a vital medium for assessing critical thinking and reasoning skills, yet there is limited works on accurately understanding and evaluating such texts via prompt. In this work, we propose TIDE, a novel framework designed to improve criteria-based prompt optimization for argument-related tasks by integrating TrIal and DEbate mechanism. Our method addresses key limitations of criteria-based prompt optimizing by mitigating the influence of noisy training data and enhancing optimization stability. We evaluate TIDE on three core tasks: Automated Essay Scoring, Argument Component Detection, and Argument Relation Identification. Results demonstrate that our framework improves performance across tasks. These findings underscore the potential of combining prompt-based methods for advanced argument understanding.

---


### 261. [Image-to-Video Diffusion: From Foundations to Open Frontiers](https://arxiv.org/abs/2605.17248)

**<font color=#1a73e8>作者：</font>** Xianlong Wang, Wenbo Pan, Shijia Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based \textit{image-to-video} (I2V) generation has become a central direction in generative models by turning a reference image, with optional conditions, into a temporally coherent video. Compared with broader video generation settings, this task places stricter demands on content consistency, identity preservation, and motion coherence. Although the literature grows rapidly, existing works mostly discuss I2V generation within broader topics and still lack a dedicated taxonomy together with a systematic analysis centered on this field. This work addresses that gap by treating diffusion I2V generation as a standalone subject. It first reviews the task formulation, model architectures, datasets, and evaluation metrics, and then organizes existing methods through a taxonomy based on architecture and training paradigm. It further distills four core designs, namely condition encoding, temporal modeling, noise prior design, and spatial-temporal upsampling, and discusses representative application scenarios together with major open challenges.

---


### 262. [Towards Principled Test-Time Adaptation for Time Series Forecasting](https://arxiv.org/abs/2605.17250)

**<font color=#1a73e8>作者：</font>** Haochun Wang, Ruichen Xu, Georgios Kementzidis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) has recently emerged as a promising approach for improving time series forecasting (TSF) under distribution shift. Existing TSF-TTA methods differ in how they utilize revealed targets, yet the resulting adaptation protocols remain heterogeneous and lack a clearly unified formulation. To address this issue, we revisit TSF-TTA from the perspective of protocol cleanliness and propose an adaptation protocol based solely on matured ground truth, yielding a more principled setting for adaptation. Under this protocol, we further diagnose existing adapters in the frequency domain and find that their prediction corrections often exhibit limited and weakly structured spectral modifications. Motivated by this diagnosis, we propose Frequency-Aware Calibration (FAC), a lightweight calibration method that directly parameterizes prediction corrections in the frequency domain. Across diverse datasets, forecasting horizons, and source forecasters, FAC achieves competitive and consistent performance while requiring substantially fewer trainable parameters than the compared TSF-TTA adapters.

---


### 263. [Monocular Depth Perception Enhancement Based on Joint Shading/Contrast Model and Motion Parallax (JSM)](https://arxiv.org/abs/2605.17252)

**<font color=#1a73e8>作者：</font>** Seungchul Ryu, Hyunjin Yoo, Tara Akhavan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereoscopic 3D displays adopt a binocular depth cue to provide depth perception. However, users should be equipped with expensive special devices to appreciate depth perception based on the binocular depth cues. Also, visual fatigue induced by the stereoscopic display is still a challenging open problem. In order to overcome this limitation, this paper proposes a novel framework, JSM, to enhance monocular depth perception, significantly improving both depth volume perception and depth range perception. The proposed framework can not only provide an enhanced depth perception on any conventional 2D display devices, but also it can be applicable to the 3D display devices since it is complementary to binocular depth cues. The qualitative evaluation, ablation study, and subjective user evaluation proved the advantages and practicability of the proposed framework.

---


### 264. [CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy](https://arxiv.org/abs/2605.17259)

**<font color=#1a73e8>作者：</font>** Dawei Xie, Khalil Anderson, Tochukwu Eze 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Collaboration literacy requires adapting to the evolving demands of group work within complex discussions, making it difficult to develop and assess. Traditional analytics metrics capture behavioral signals while missing the semantic dimensions of how learners approach collaboration and build on each other's ideas. We present Collaboration Literacy through Artifact Reasoning and Augmentation (CLARA), an agentic analytics system that extracts semantic representations from transcripts as analytics artifacts: concept maps representing emergent ideas and relationships, and collaboration assessment characterizing collaboration quality across seven dimensions. While users explore these artifacts through the dashboard, the same artifacts are indexed into distinct vector database collections for agent retrieval and reasoning. This architecture establishes a human-AI common ground where users and AI can operate over shared representations. Evaluation results show that CLARA produces reliable collaboration quality analysis and, owing to the artifacts serving as knowledge infrastructure, improves both retrieval performance and response quality over transcript-only baselines. Our work suggests that AI-produced artifacts may scaffold human interpretation and ground AI reasoning in learning analytics workflows.

---


### 265. [Expert Cognition Dashboard: From Learning Analytics to Cognition Intelligence in AI-Driven Education](https://arxiv.org/abs/2605.17263)

**<font color=#1a73e8>作者：</font>** Annie Yuan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current AI-driven educational systems primarily rely on behavioural analytics, performance metrics, and content-level interactions to model learning. While these approaches provide useful indicators of learner activity, they are insufficient for representing the expert cognition used to interpret learner development, identify misconceptions, and make adaptive pedagogical decisions. Existing learning analytics dashboards largely visualise learner behaviour for human instructors, rather than embody expert cognition as a reasoning infrastructure for AI-native education.
This paper introduces the Expert Cognition Dashboard (ECD), a cognition-centred reporting infrastructure for AI Twin-driven education systems. ECD models expert cognition within dashboard systems, enabling learner behaviours to be interpreted through expert-like cognitive structures rather than treated as raw behavioural signals. The proposed framework transforms student interactions into interpretable cognition structures through AI Tutor analysis and multi-level dashboard aggregation. Its architecture organises cognition across three layers: individual cognition dashboards, class cognition dashboards, and AI Twin expert dashboards for cross-group reasoning and adaptive intervention.
Building on the AI Expert Feedback Ecology framework, ECD redefines dashboards as cognitive middleware that connects learner behaviours with AI-driven expert reasoning. By modelling interpretation, identity cognition, value recognition, misconception patterns, and learning tension, ECD enables AI Twins to identify recurring learner difficulties, generate adaptive tasks, and support personalised intervention. The paper argues for a shift from learning analytics toward Cognition Intelligence, positioning dashboards as foundational cognition infrastructures that embed expert reasoning into future AI-native education systems.

---


### 266. [When Molecular Similarity Works: Property Cliffs Reveal Hidden Errors](https://arxiv.org/abs/2605.17265)

**<font color=#1a73e8>作者：</font>** Di Hu, Kun Li, Haojie Rao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of molecular properties underpins drug discovery and material design, yet even state-of-the-art models remain vulnerable to localized failure modes that aggregate metrics cannot detect. The places where molecular similarity should be most helpful are also places where standard evaluation can be most misleading. Property cliffs expose this gap: structurally similar molecules can still differ sharply in target property, so models with competitive overall performance may fail in high-risk local neighborhoods. To expose and mitigate this failure mode, CliffSplit, a cliff-aware evaluation protocol that constructs locally supported, cliff-exposed test cases, and CliffLoss, a model-agnostic train-only mitigation mechanism for cliff-sensitive errors, are introduced. Experiments on three QM9 targets and three MoleculeNet tasks across five backbones show that CliffSplit reveals at least 15% higher error in cliff-heavy QM9 regions, while CliffLoss reduces the cliff-to-smooth error gap by up to 30% on Lipophilicity and improves overall MAE by 9.7%. Together, these results turn molecular similarity failure from a descriptive anomaly into a benchmarked evaluation problem for molecular machine learning. The code is available at this https URL.

---


### 267. [Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation](https://arxiv.org/abs/2605.17268)

**<font color=#1a73e8>作者：</font>** Nicanor Mayumu, Xiaoheng Deng, Patrick Mukala  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present the first systematic study of faithfulness in Vision-Language-Action (VLA) driving models, analyzing 300 Alpamayo-R1-10B inferences across 100 diverse PhysicalAI-AV scenarios. Our main finding is that output natural-language rationales with trajectories may be significantly unfaithful: (i) overall reasoning fidelity is only 42.5%, with Chain-of-Causation matching scene reality less than half the time; (ii) 94 missed pedestrians in one-third of pedestrian-relevant scenes; (iii) 97.7% trajectory fragility under mild visual perturbations; and (iv) only 48.3% mean reasoning-action consistency, with 53.3% of inferences exhibiting low consistency, including 37.9% of stop-claimed cases where the model continues instead. We formalize faithfulness information-theoretically, define entity and action fidelity with verification criteria, and outline a four-component safety architecture aligned with these results.

---


### 268. [Calibeating for general proper losses: A Bregman divergence approach](https://arxiv.org/abs/2605.17269)

**<font color=#1a73e8>作者：</font>** Maximilian Fichtl, Cristóbal Guzmán, Nishant A. Mehta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work introduces a general framework for calibeating based on regret minimization. As compared to Foster and Hart's seminal calibeating work which had specialized treatments of Brier score (squared loss) and log loss, we consider a large family of proper losses that includes $\alpha$-Tsallis losses (for $\alpha \in [1, 2]$) and Lipschitz losses. Our results for Tsallis losses also hold for an unscaled version of Tsallis loss that recovers log loss. Our analysis is oriented around the Bregman divergence view of a proper loss. Technically, our results for the family of Tsallis losses that we consider are U-calibration results, simultaneously obtaining logarithmic regret for all losses in this family while having a weaker dependence on the dimension compared to previous results. Of potential independent interest, we also show a new regret equality for the regret of Be The Regularized Leader. This regret equality holds for general proper losses and itself is based on two results related to online updating formulas for the generalized variance, the latter being a previously introduced generalization of variance based on Bregman divergences.

---


### 269. [Beyond Detection: A Structure-Aware Framework for Scene Text Tracking](https://arxiv.org/abs/2605.17270)

**<font color=#1a73e8>作者：</font>** Chenmin Yu, Liu Yu, Daiqing Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern visual object trackers show impressive results on general targets, yet their performance drops substantially when dealing with scene text. Although currently underexplored, tracking text in videos is essential for dynamic text manipulations such as segmentation, removal, and editing. To fill this gap, this paper formalizes this specific task as Scene Text Tracking and presents the first systematic work for it. We identify three primary challenges in this task: 1) severe geometric distortions from perspective shifts, 2) high visual ambiguity across different instances, and 3) high sensitivity to fine-grained structural details. To address these issues, we propose SymTrack, a unified detection-free framework with synergistic dual-branch design. It integrates a Cross-Expert Calibration mechanism to reduce semantic bias, along with a Predictive Token Rectification mechanism to correct structural imbalances, complemented by an Adaptive Inference Engine that stabilizes predictions under motion constraints. Considering the lack of dedicated benchmarks for this task, we utilize three datasets from video text spotting to construct a benchmark with high-quality annotations. Extensive experiments demonstrate that SymTrack sets the new state-of-the-art on all three benchmarks, outperforming previous best trackers by up to 11.97\% AUC on $ \text{BOVText}_{\text{SOT}} $. Overall, our work promotes efficient and thorough text tracking, paving the way toward more generalized video text manipulation.

---


### 270. [State-of-the-Art Claims Require State-of-the-Art Evidence](https://arxiv.org/abs/2605.17273)

**<font color=#1a73e8>作者：</font>** YongKyung Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-Art (SOTA) claims pervade Artificial Intelligence (AI) and Machine Learning (ML) research. These claims rest on benchmark evaluations, where models are ranked by aggregate scores across tasks. Public benchmarks or leaderboards are the most visible instance, but the same structure appears in paper tables throughout the literature. However, such minimal evidence often cannot support these strong claims. We identify a widespread claim-evidence gap in AI benchmarking. Claiming SOTA carries implicit assumptions beyond mean score superiority, suggesting that a model meaningfully outperforms alternatives across most tasks. However, a marginal improvement in the mean score merely indicates a top average rank rather than true superiority. Analyzing ten cross-domain benchmarks from public leaderboards, we found that in more than half of top-model comparisons, at least one commonly assumed property of superiority does not hold. These properties include meaningful effect size, consistency across tasks, or robustness to dataset removal. Instead, aggregate gains are frequently driven by outlier datasets. This fragility persists even in benchmarks with many tasks. We argue that claim language should reflect the strength of the underlying evidence. This requires no additional experiments, only honest reporting of what results actually show, enabling more precise and interpretable comparisons across models.

---


### 271. [How Do Electrocardiogram Models Scale?](https://arxiv.org/abs/2605.17276)

**<font color=#1a73e8>作者：</font>** Jiawei Li, Fabio Bonassi, Ming Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While scaling laws have established a fundamental framework for foundation models in natural language processing, their applicability to electrocardiogram (ECG) models remains poorly characterized. Indeed, recent studies do not always yield consistent downstream gains as one increases the model size or pre-training dataset size of ECG models, leaving the exact roles of architectural inductive biases, pre-training paradigms, and expected improvements with size largely unanswered. In this work, we systematically investigate neural and loss-to-loss scaling laws within the ECG domain. By pre-training over $120$ models (ranging from $20$K to $200$M parameters) on the large-scale CODE dataset ($2.3$M records), we decouple the effects of model architecture (ResNet vs. Transformer) and pre-training paradigm, namely supervised learning (SL) versus self-supervised learning (SSL). We found that (i) SL models are data-bottlenecked in-distribution, whereas SSL models scale robustly across both model and data sizes; (ii) for out-of-distribution (OOD) generalization, ResNets are $1.3$ to $2.5$ times more parameter-efficient than Transformers, while SSL is up to $16$ times more data-efficient and achieves up to $7.6$ times higher transfer efficiency than SL on unseen clinical tasks; (iii) across the observed scales, ResNet-based models generally achieve the lowest OOD loss, with SSL dominating on unseen clinical tasks and self-supervised Transformers overtaking at very large model sizes. Our results suggest that the path to effective ECG foundation models lies in the strategic alignment of architecture and paradigm rather than brute-force scaling.

---


### 272. [A2RBench: An Automatic Paradigm for Formally Verifiable Abstract Reasoning Benchmark Generation](https://arxiv.org/abs/2605.17278)

**<font color=#1a73e8>作者：</font>** Qingchuan Ma, Yuexiao Ma, Yongkang Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Abstract reasoning ability reflects the intelligence and generalization capacity of LLMs to extract and apply abstract rules. However, accurately measuring this ability remains challenging: existing benchmarks either rely on expensive manual annotation, limiting their scale, or risk measuring memorization rather than genuine reasoning. To address this, we introduce an automated pipeline named A2RBench, encompassing generation, expansion, evaluation, and analysis. Specifically, in the generation stage, LLMs create diverse tasks demanding genuine reasoning; in the expansion stage, LLMs reuse validated rules and expand new input spaces to generate task variations, achieving scaling. However, such a process may cause hallucinations. To eliminate it, we further establish a theoretical framework and prove that programmatic verification--testing whether the inverse operation perfectly reverses the forward operation (cycle consistency)--guarantees a unique solution. Through extensive evaluations on mainstream LLMs, we find: (1) Current LLMs exhibit fundamental deficiencies in abstract reasoning, with top models significantly underperforming humans on a representative subset (39.8% vs. 68.5%). (2) Current LLMs fall far short of 2D and 1D in the complexity of generated 3D tasks, revealing their lack of understanding of high-dimensional tasks. (3) Counterintuitively, inputs with higher information complexity can simplify the reasoning process.

---


### 273. [CLAP: Contrastive Latent-space Prompt Optimization for End-to-end Autonomous Driving](https://arxiv.org/abs/2605.17284)

**<font color=#1a73e8>作者：</font>** Ruiyang Zhu, Yuehan He, Boyuan Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving systems powered by Vision-Language-Action (VLA) models achieve strong performance on common driving scenarios, yet remain brittle in rare but safety-critical long-tail situations such as active construction zones and complex yielding geometries. In this paper, we present a method that addresses the long-tail challenging scenes beyond data scaling and model training. We introduce CLAP (Contrastive Latent-space Prompt optimization), a location-aware adaptation framework that augments a frozen VLA driving model with per-roadblock soft prompts, optimized from crowdsourced data and retrieved on demand via Vehicle-to-Everything (V2X) communication. Our approach rests on two observations from VLAs' latent space: (i) at the VLA's hidden-state layer, scenarios from the same roadblock cluster tightly and occupy compact regions of the latent space; and (ii) within a single roadblock, long-tail and normal frames are heavily intermixed in the latent representation, making it difficult to improve one without disturbing the other. CLAP addresses this via a two-stage pipeline: supervised contrastive learning to discover a roadblock-specific hard-scene direction, followed by directionally regularized prompt optimization that selectively improves challenging frames while preserving normal frame performance. On the NAVSIM benchmark with various state-of-the-art VLA backbones, CLAP reduces challenging scenario planning error by 24% with no regression on normal frames, significantly improving planning performance.

---


### 274. [UNR-Explainer: Counterfactual Explanations for Unsupervised Node Representation Learning Models](https://arxiv.org/abs/2605.17285)

**<font color=#1a73e8>作者：</font>** Hyunju Kang, Geonhee Han, Hogun Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Node representation learning, such as Graph Neural Networks (GNNs), has emerged as a pivotal method in machine learning. The demand for reliable explanation generation surges, yet unsupervised models remain underexplored. To bridge this gap, we introduce a method for generating counterfactual (CF) explanations in unsupervised node representation learning. We identify the most important subgraphs that cause a significant change in the k-nearest neighbors of a node of interest in the learned embedding space upon perturbation. The k-nearest neighbor-based CF explanation method provides simple, yet pivotal, information for understanding unsupervised downstream tasks, such as top-k link prediction and clustering. Consequently, we introduce UNR-Explainer for generating expressive CF explanations for Unsupervised Node Representation learning methods based on a Monte Carlo Tree Search (MCTS). The proposed method demonstrates superior performance on diverse datasets for unsupervised GraphSAGE and DGI.

---


### 275. [HyperVision: A Channel-Adaptive Ground-Based Hyperspectral Vision Pre-trained Backbone](https://arxiv.org/abs/2605.17286)

**<font color=#1a73e8>作者：</font>** Guanyiman Fu, Jingtao Li, Zihang Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While hyperspectral imaging provides rich spatial-spectral information across hundreds of narrow wavelength bands for precise material identification, ground-based hyperspectral pre-trained backbones remain absent, constrained by varying spectral configurations across sensors, the scarcity and inconsistency of labels, and the limited scale and scene diversity of existing datasets. To address these challenges and enable universal perception, we propose HyperVision, the first ground-based hyperspectral pre-trained backbone. First, to handle varying spectral configurations, HyperVision adopts a channel-adaptive dynamic embedding mechanism to map heterogeneous inputs into a unified token space. Second, to address the scarcity and inconsistency of labels, we introduce a multi-source pseudo-labeling method that fuses semantic representations from both spatial structures generated by SAM2 and fine-grained spectral material information extracted by HyperFree. Third, to compensate for limited dataset scale and enrich scene diversity, a cross-modal knowledge distillation mechanism is utilized to transfer rich semantic representations from a pre-trained RGB vision model to our hyperspectral backbone. Pre-trained on a collection of 15k images from 26 diverse ground-based datasets, HyperVision demonstrates exceptional generalization. Requiring only efficient head-only adaptation without adjusting backbone parameters, it achieves state-of-the-art performance compared to task-specific methods across three downstream tasks under varying sensor configurations, yielding up to a 16.3% relative improvement in hyperspectral semantic segmentation $\mathrm{Acc}_{\mathrm{M}}$, a 2.1% relative gain in object tracking AUC, and a 35.5% reduction in salient object detection MAE. The source code and pre-trained model will be publicly available at this https URL .

---


### 276. [LISA: Language-guided Interference-aware Spatial-Frequency Attention for Driver Gaze Estimation](https://arxiv.org/abs/2605.17287)

**<font color=#1a73e8>作者：</font>** Jun Ma, Zhenye Yang, Ruichen Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driver gaze estimation serves as a fundamental metric for evaluating driver attentiveness in modern monitoring systems. Beyond being vulnerable to sudden lighting changes and sensor noise, spatial-domain models struggle to disentangle authentic gaze cues from irrelevant visual attributes. In this paper, we propose LISA, a \textbf{L}anguage-guided \textbf{I}nterference-aware \textbf{S}patial-Frequency \textbf{A}ttention framework that combines frequency-domain priors with vision-language knowledge. Observing that the amplitude spectrum remains relatively stable even under spatial perturbations, we design a dual-domain fusion mechanism. It integrates stable low-frequency semantics into high-frequency details, employing spatial attention to precisely target ocular regions. To reduce semantic ambiguity, we also introduce a training-time disentanglement strategy. Using a frozen CLIP encoder and orthogonal regularization, we explicitly separate gaze features from appearance interference. Experiments on two benchmarks show that LISA achieves state-of-the-art performance, with significantly improved robustness against occlusions and lighting variations. The code repository is available at this https URL.

---


### 277. [HierEdit: Region-Aware Hierarchical Diffusion for Efficient High-Resolution Editing](https://arxiv.org/abs/2605.17294)

**<font color=#1a73e8>作者：</font>** Yuyao Zhang, Alexander Huang-Menders, Yu-Wing Tai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution image editing is essential for professional and creative applications, yet existing multimodal diffusion-based editors remain computationally inefficient and constrained to relatively low resolutions. Current approaches redundantly process the entire image canvas or rely on large-scale high-resolution datasets, resulting in substantial training and inference costs. We introduce HierEdit, a region-aware hierarchical diffusion framework designed for efficient and scalable high-resolution image editing. Our method first performs edits on a low-resolution proxy using an off-the-shelf editing model to generate a reference and to localize the modified regions. A hierarchical local-window diffusion model (\textbf{Local-Window MMDiT}) that refines only edited regions within the original high-res image, while reusing the unaltered regions as conditioning inputs. The low-resolution proxy further provides structural guidance and intermediate denoising supervision (\textbf{Inference Acceleration}) , ensuring consistent global semantics and stable generation without the need for full-resolution attention computation. This targeted and hierarchical design enables fast, high-fidelity editing of images up to 4K resolution without any specialized high-resolution training data. Extensive experiments demonstrate that HierEdit achieves competitive visual quality on commodity-resolution datasets while significantly accelerating inference and extending seamlessly to ultra-high-resolution 4K editing. Please check our {\href{this https URL}{\textbf{Project Page}}}.

---


### 278. [LongDPM: Overlap-Aware 4D Reconstruction from Long Monocular Videos](https://arxiv.org/abs/2605.17303)

**<font color=#1a73e8>作者：</font>** Chenyi Xu, Yihao Wu, Liqi Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering a dynamic 3D scene from a long monocular video is crucial for dense geometry, camera motion, and temporal correspondence to remain consistent in a shared coordinate system. Existing methods face two key challenges: (1) feed-forward reconstruction models provide accurate local predictions but are limited to short clips, and (2) long-range trackers preserve correspondences without producing dense sequence-level reconstruction. This paper presents LongDPM, a novel overlap-aware framework for scalable long-range monocular dynamic reconstruction. First, LongDPM processes long videos in overlapping chunks, keeping inference memory bounded by the chunk length. Second, it connects chunk-local coordinate systems through confidence-weighted registration with static-aware overlap abstraction. Third, it associates dynamic identities across chunk boundaries and fuses matched trajectories to recover coherent long-range 3D motion. Experimental results demonstrate that LongDPM achieves superior long-range reconstruction and tracking performance, reducing dense tracking EPE over V-DPM on PointOdyssey, Kubric-F, and Kubric-G, while obtaining the best TUM-dynamics ATE for camera pose estimation.

---


### 279. [StyleText: A Large-Scale Dataset and Benchmark for Stylized Scene Text Inpainting](https://arxiv.org/abs/2605.17309)

**<font color=#1a73e8>作者：</font>** Aleksandr Simonyan, Nipun Jindal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present StyleText, a large-scale dataset and benchmark for localized scene-text inpainting with style preservation. StyleText contains 28,518 image-mask-prompt triplets grouped into 9,932 scene families, enabling controlled evaluation of text legibility and visual consistency under shared scene context. We construct the dataset with an automated pipeline that combines LLM prompt templating, Flux-based source generation with key-value (KV) cache injection, OCR-based semantic filtering, polygon mask extraction, and mask-conditioned FluxFill augmentation. We define a reproducible evaluation protocol using normalized OCR metrics (word accuracy and character error rate) and CLIP image-image similarity with explicit preprocessing. A FluxFill+LoRA baseline trained on StyleText improves OCR accuracy substantially over initialization while maintaining scene style consistency, establishing a strong reference point for future comparisons.

---


### 280. [SpecSem-Net: Integrating Spectral and Semantic Features for Robust AI-generated Video Detection](https://arxiv.org/abs/2605.17311)

**<font color=#1a73e8>作者：</font>** Zixi Wei, Huixuaun Zhang, Xiaojun Wan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The remarkable visual fidelity of recent commercial video generative models, such as Sora and Veo, renders robust AI-generated video detection increasingly essential to prevent synthetic content from being indistinguishable from real videos and exploited for disinformation. However, existing detectors often fail due to an over-reliance on increasingly realistic semantic features, neglecting subtle spectral artifacts. In this paper, we propose SpecSem-Net, the first framework to introduce a semantic-guided spectral denoising mechanism specifically for high-fidelity AI-generated video detection. Specifically, we design a spectral module to extract high-frequency features via Fourier-Transform based filtering. Furthermore, to reduce misjudgments arising from spectral noise, we employ a Gated Merging Mechanism to adaptively fuse semantic context, effectively mitigating spectral noise. Additionally, to evaluate detector performance on the latest top-tier generative models, we construct a comprehensive benchmark comprising 5 SOTA commercial generators. Extensive experiments demonstrate that SpecSem-Net outperforms existing methods, achieving accuracies of 87.25% and 95.59% on our benchmark and public datasets, respectively.

---


### 281. [VISTA: Triplet-Supervised Video Style Transfer with Diffusion Transformers](https://arxiv.org/abs/2605.17312)

**<font color=#1a73e8>作者：</font>** Yiren Song, Wangzi Yao, Haofan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video style transfer aims to render videos in a target artistic style while preserving content, structure, and motion. While image stylization has advanced rapidly, video stylization remains challenging due to temporal inconsistency. Most existing methods stylize frames or keyframes and enforce consistency via heuristic temporal propagation, which is brittle under occlusions, disocclusions, and long-term motion, leading to drift and flickering artifacts. We argue that a fundamental bottleneck lies in the lack of large-scale triplet data and a principled training paradigm that jointly models and disentangles style, content, and this http URL address this, we introduce VISTA-1000, a synthetic dataset with 1,000 styles and motion-aligned triplets of style reference, clean video, and stylized video, and propose a diffusion-transformer-based in-context video style transfer framework with a lightweight style adapter for robust style extraction. Extensive experiments demonstrate SOTA performance in style fidelity, temporal consistency, and content preservation.

---


### 282. [Weak-to-Strong Elicitation via Mismatched Wrong Drafts](https://arxiv.org/abs/2605.17314)

**<font color=#1a73e8>作者：</font>** Wei Deng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We consider whether off-policy experience from a smaller, weaker model can elicit capability in a stronger learner that on-policy RL fine-tuning (e.g., GRPO) does not reach. We find that injecting mathematically wrong drafts from a smaller but more domain-trained model -- mismatched to the current problem -- into a stronger learner's GRPO context consistently outperforms standard on-policy GRPO on held-out MATH-500 and out-of-distribution AIME 2025/2026. Concretely, we use Mathstral-7B as the learner, Qwen2.5-Math-1.5B as the draft model, 8.8K Level 3--5 MATH problems (with MATH-500 held out), and train with Dr. GRPO. Mismatch is an active ingredient: shuffling drafts to mismatched problems while holding everything else constant yields $+1.62$pp on MATH-500 (greedy pass@1) over the matched-wrong variant ($n=10$ seeds, $p=0.0015$, Welch's $t$). In fact, the mismatched-wrong variant leads all other variants we tested on MATH-500 across both greedy pass@1 and sampling pass@$k$. On out-of-distribution AIME 2025 and 2026, the mismatched-wrong variant uniquely lifts pass@$k$ above both Mathstral-7B (in its native [INST] format) and the Qwen2.5-Math-1.5B draft model at every sample budget from $k=1$ to $k=1024$ across 2 seeds ($+14.2$pp on 2025 and $+9.0$pp on 2026 at pass@1024 over Mathstral-7B), and at pass@1024 also leads no-draft, matched-wrong, and mismatched-correct variants on both years. All variants use the same prompt with no draft injection at test time. The recipe -- trained on a single GPU with no SFT, no reward models, no synthesized data, and no produce-critique-revise inner loop -- reaches 71.98% MATH-500 on Mathstral-7B-v0.1, the highest published result on this model to our knowledge, surpassing the heavier WizardMath pipeline at 70.9% on full MATH (SFT + PPO with process/instruction reward models).

---


### 283. [Learning Higher-Order Structure from Incomplete Spatiotemporal Data: Multi-Scale Hypergraph Laplacians with Neural Refinement](https://arxiv.org/abs/2605.17316)

**<font color=#1a73e8>作者：</font>** Keshu Wu, Sixu Li, Zihao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensor networks increasingly govern modern infrastructure, yet the data they lose are rarely missing in the uniform-random patterns assumed by standard imputation benchmarks. Loop detectors go offline during calibration, roadside cabinets silence clusters of nearby sensors, and newly installed instruments provide no history. Such failures create structured absences whose values are constrained by higher-order relations among groups of sensors, not merely by pairwise proximity. Existing low-rank and graph-based methods often miss this collective structure and can fail when missingness becomes coherent. We introduce Multi-Scale Hypergraph Laplacians (MSHL), a two-stage framework for learning higher-order structure from incomplete spatiotemporal observations. The Discovery stage builds a multi-scale hypergraph from complementary topology and residual-correlation evidence, with an observation-only selector that adapts to the supported interaction scale. The Refinement stage adds a small hypergraph-conditioned residual network that is safe by construction: it learns nonlinear corrections where informative residual features exist and defers to the linear estimate where they do not. We prove that MSHL represents group-conservation patterns inaccessible to pairwise graph priors, adapts to the best fixed scale up to a logarithmic factor, transfers this advantage to held-out imputation error, and admits a one-sided refinement guarantee. On two real traffic networks evaluated across scattered cell missingness, contiguous block outages, and whole-sensor blackouts at five rates, MSHL improves over a pairwise-graph baseline whenever higher-order structure is identifiable and otherwise matches it within sampling noise. The results point to a broader principle for reliable infrastructure learning: missing data should be treated not as isolated entries to fill, but as evidence of structure to discover.

---


### 284. [Federated Stream-Processing and Latency-Gated Response for Cross-Sector Threat Detection and Collaborative Containment](https://arxiv.org/abs/2605.17325)

**<font color=#1a73e8>作者：</font>** Namit Mohale  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Critical infrastructure defense is fundamentally bottlenecked by the operational reality that preventive controls are frequently bypassed by sophisticated supply-chain compromises and stolen administrative credentials. When prevention fails, defense relies entirely on rapid, post-ingress threat detection and automated response across sovereign sectors. We present a novel, federated, high-throughput stream-processing and correlation framework designed to detect coordinated cross-sector threat campaigns and orchestrate containment at machine speed. By utilizing a stateless Pre-Filtering Dispatcher Subsystem (PFDS), in-memory lock-sharded state workers, and a 95% statistical watermark heuristic, our system maintains detection momentum during network partitions to evacuate speculative alerts. Delayed telemetry is subsequently reconciled directly within a version-keyed columnar storage engine via deterministic time-bucket hashing, eliminating state-retraction overhead. We evaluate a prototype of our framework - implemented in Go with an instantiated production-grade columnar analytical store - against a 500,000 events per second workload. The results demonstrate an internal framework processing overhead of under 7 seconds, while achieving total end-to-end operational convergence - accounting for multi-sector detection, correlation, wide-area network (WAN) propagation, windowing stability, VLAN-level response, and hardware level mitigation commitment - within a realistic 12-20 seconds window.

---


### 285. [LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails](https://arxiv.org/abs/2605.17329)

**<font color=#1a73e8>作者：</font>** Nanxi Li, Zhengyue Zhao, Chaowei Xiao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Guardrails are a critical safety layer for modern AI systems, but their operating regime is changing. As LLMs are deployed as customized assistants, safety policies are increasingly specified at inference time by users, organizations, or regulatory contexts. This makes safety enforcement fundamentally dynamic: the guardrail should adapt to changing safety policies without retraining. Yet this requirement creates a fundamental tension: faithfully judging complex policy contexts demands reasoning capability, while practical deployment requires low-latency responses. We introduce Latent Policy Guardrail (LPG), a guardrail framework that learnssemantic latent deliberation over dynamic policies. LPG compresses the internal deliberation needed for intent interpretation and policy grounding into continuous states supervised by decision-relevant semantics. At inference time, it generates only a compact verdict anchored to the violated policy clauses, preserving auditability while avoiding the latency of explicit reasoning. Across policy guardrail benchmarks, LPG-4B reaches 84.5% average safety accuracy and 77.9% F1 by compressing deliberation into just 10 latent tokens, outperforming the strongest dynamic baseline while running roughly 11 times faster than Qwen3-4B-Thinking under the single-sample evaluation setup. Code and data are available at this https URL.

---


### 286. [Bridging the Gap between Sparse Matrix Reordering and Factorization: A Deep Learning Framework for Fill-in Reduction](https://arxiv.org/abs/2605.17339)

**<font color=#1a73e8>作者：</font>** Ziwei Li, Tao Yuan, Shuzi Niu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse matrix reordering can significantly reduce the fill-in during matrix factorization, thereby decreasing the computational and storage requirements in sparse matrix computations. Finding a minimal fill-in ordering is known to be an NP-hard problem. Moreover, there is a paradox: matrix reordering is applied before matrix factorization, but fill-ins that matrix reordering methods aim at are generated from matrix factorization. To bridge the gap between reordering and factorization, we propose a deep learning framework to minimize a fill-in surrogate function based on spectral embedding. First, we employ a multi-grid-like GNN architecture to learn to approximate the smallest eigenvectors of its graph Laplacian matrix, i.e. spectral embedding, and capture the global structural information of the matrix. Then, another multi-grid-like GNN architecture is used to minimize the potential space where fill-in can occur based on the rank distribution. Experimental results indicate that our approach achieves competitive performance compared with traditional graph-theoretic algorithms and deep learning methods.

---


### 287. [GraphMAR: Geometry-Aware Graph Learning Framework for Spatially Adaptive CT Metal Artifact Reduction](https://arxiv.org/abs/2605.17343)

**<font color=#1a73e8>作者：</font>** Zilong Li, Chenglong Ma, Yiming Lei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) metal artifact reduction (MAR) aims to reduce the severe streaking artifacts induced by metallic implants and other high-density objects. Effective MAR generally requires both accurate artifact localization and artifact removal. Sinogram-domain methods can exploit explicit geometric cues, such as metal traces, to identify metal-corrupted measurements, while requiring raw projection data, which is often unavailable in clinical and practical scenarios. Image-domain methods are more flexible and widely applicable, yet they usually lack comparable geometric guidance, limiting their ability to localize artifacts and leading to suboptimal results. To address this limitation, we propose GraphMAR, a geometry-aware learning framework for explicit artifact identification and spatially adaptive MAR in the image domain. The key idea is to introduce graph-based geometric modeling as an image-domain analogue of sinogram metal traces. Specifically, we first construct a geometric graph from the metal mask and derive a geometric density graph that coarsely localizes artifact-prone regions according to inter-implant geometry. We then design GraphMoE, a graph-routed mixture-of-experts module that builds a polar-coordinate artifact graph in feature space and adaptively routes different experts to different spatial regions for MAR. By aligning the learned routing maps with the geometric density graph, GraphMAR provides explicit and interpretable artifact localization while enabling region-adaptive artifact reduction. Experiments on both simulated and real-world datasets demonstrate that GraphMAR achieves superior MAR performance compared with existing methods. To the best of our knowledge, this is the first work to introduce graph-based modeling for CT MAR and to enable explicit artifact identification in the image domain, improving both restoration quality and interpretability.

---


### 288. [VoxShield: Protecting 3D Medical Datasets from Unauthorized Training via Frequency-Aware Inter-Slice Disruption](https://arxiv.org/abs/2605.17345)

**<font color=#1a73e8>作者：</font>** Xinyao Liu, Zhipeng Deng, Wenhan Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The release of public 3D medical image segmentation (MIS) datasets accelerates clinical research but simultaneously heightens risks of unauthorized AI model training. While Unlearnable Examples (UE) offer protection by injecting imperceptible perturbations to prevent effective model learning, existing methods primarily target 2D scenarios. They neglect the volumetric spatial correlations and inter-slice anatomical consistency inherent in 3D medical volumes, which serve as critical learning priors for 3D segmentation networks. To bridge this gap, we propose VoxShield, a UE framework that explicitly targets the volumetric inductive biases of 3D networks. Our core insight is that by systematically dismantling the cross-slice continuity that 3D architectures rely on, we can fundamentally impair their spatial aggregation process. Specifically, we introduce an Inter-Slice Frequency Consistency Disruption mechanism that maximizes the spectral divergence between adjacent slices, injecting structural incoherence along the $z$-axis. Complementing this structural attack, a Semantic Prediction Disruption module is incorporated. By maximizing the $\ell_1$ divergence between clean and perturbed logits, it forces the injected noise to penetrate the entire network and corrupt the final semantic mapping. Experiments on BraTS19 and FLARE21 demonstrate that VoxShield successfully degrades 3D segmentation performance, reducing the DSC from 80.0% to near 0.0% and from 88.6% to 6.8%, respectively. All protections are achieved with minimal perturbation ($\epsilon=4/255$) to preserve high visual fidelity. The code is available at this https URL.

---


### 289. [Taming "Zombie'' Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution](https://arxiv.org/abs/2605.17348)

**<font color=#1a73e8>作者：</font>** Taolin Zhang, Pukun Zhao, Qizhou Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in LLM-based multi-agent systems have demonstrated remarkable collaborative capabilities across complex tasks. To improve overall efficiency, existing methods often rely on aggressive graph evolution among agents (e.g., node or edge pruning), which risks prematurely discarding valuable agents due to transient issues such as hallucinations or temporary knowledge gaps. However, such hard pruning overlooks the potential for ``zombie'' agents to recover and contribute in subsequent discussion rounds. In this paper, we propose AgentRevive, a Markov state-aware framework for resilient multi-agent evolution. Our approach dynamically manages agent collaboration through soft state transitions, implemented via two key components: (1) State-Aware Policy Learning: Agent states are divided into ``Active'', ``Standby'', and ``Terminated'' states, selectively propagating messages based on agent memory. The policy employs a risk estimator to optimize agent state transitions by assessing hallucination risk, minimizing the influence of unreliable nodes while safeguarding valuable ones. (2) State-Aware Edge Optimization: Subgraph edges are pruned according to states learned from the policy, permanently removing ``Terminated'' nodes and retaining ``Standby'' nodes for subsequent rounds to assess their potential future contributions. Extensive experiments on general reasoning, domain-specific, and hallucination challenge tasks show that our method consistently outperforms strong baselines and significantly reduces token consumption through state-aware agent scheduling.

---


### 290. [GeoHand: Unlocking Prior Geometry Knowledge for Monocular 3D Hand Reconstruction](https://arxiv.org/abs/2605.17354)

**<font color=#1a73e8>作者：</font>** Weiquan Lin, Yaoqing Hu, Liangchen Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D hand reconstruction is intrinsically a geometric problem, yet RGB appearance features alone often struggle to resolve severe ambiguities caused by self-occlusions and hand-object interactions. While introducing depth can explicitly provide spatial cues, raw sensor-captured depth maps are extensively noisy and incomplete, limiting their usefulness for fine-grained hand reconstruction. To bridge this gap, we propose GeoHand, a novel framework that unlocks high-quality geometric priors from a frozen foundational monocular geometry estimator (MoGe2). Recognizing that these priors are oriented toward general scenes, we introduce a map-level GeoAdapter to recalibrate the spatial features, specifically adapting them for detailed hand reconstruction. Furthermore, to systematically integrate these adapted priors without overwhelming intrinsic RGB appearance cues, we employ a gated cross-modal token fusion strategy. Finally, to secure precise local articulation, we design a Keypoint-Queried Iterative Refiner (KQIR) that uses projected joint locations to query geometry-aware image features for spatial correction. By combining global geometric disambiguation with local refinement in a unified pipeline, GeoHand achieves state-of-the-art performance on FreiHAND, DexYCB, and HO3Dv3, especially under severe occlusions and hand-object interactions.

---


### 291. [HyperPersona: A Multi-Level Hypergraph Framework for Text-Based Automatic Personality Prediction](https://arxiv.org/abs/2605.17355)

**<font color=#1a73e8>作者：</font>** Sina Heydari, Majid Ramezani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As a modern commodity, language has become a vast repository of socially and psychologically significant traits and concepts, reflecting the ways people encode pattern of thoughts, behaviors, and emotions into words. Text-based Automatic Personality Prediction (APP), seeks to infer personality from linguistic behavior, offering a scalable alternative to traditional psychometric assessments. Although text is inherently hierarchical, with the document-level capturing global features, the sentence-level encoding local semantics, and the word-level providing fine-grained lexical information, most existing approaches rely on shallow, sequential, or single-level representations that ignore the multi-level structure of written language. To address this, we propose HyperPersona, a framework that explicitly models the hierarchical organization of text (document, sentence, and word) through hypergraph structure, where a document and its sentences are represented as hyperedges, and the words are represented as nodes, enabling joint modeling of global, local, and lexical dependencies of text. Followed by a transformer-based graph encoder that learns interactions within and across these linguistic layers, yielding context-sensitive and structurally grounded feature representations for personality prediction. Experiments on the Big Five personality dimensions show that, while relying solely on text, HyperPersona effectively integrates multi-level linguistic cues, achieving superior performance compared to state-of-the-art baselines. These findings underscore the critical role of textual hierarchy in advancing human-like personality inference from natural language.

---


### 292. [UniPPTBench: A Unified Benchmark for Presentation Generation Across Diverse Input Settings](https://arxiv.org/abs/2605.17356)

**<font color=#1a73e8>作者：</font>** Bo Zhao, Maosheng Pang, Chen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing works typically focus on presentation generation under isolated input settings, whereas real-world use cases span diverse scenarios, including vague user prompts, long documents, multimodal materials, and multiple heterogeneous sources. Moreover, current evaluations are often insufficiently scenario-specific. They mainly rely on generic presentation-quality criteria, such as visual appeal, layout quality, and overall coherence, but fail to assess the core capabilities required by different input settings, including grounded compression, visual-text alignment, and cross-source synthesis. Consequently, the field lacks a unified benchmark and a scenario-aware evaluation framework for faithfully diagnosing presentation-generation systems across diverse real-world settings. We present UniPPTBench, a unified benchmark for presentation generation across four representative input settings: vague-prompt, long-document, multimodal-document, and multi-source generation. We further introduce UniPPTEval, a scenario-aware evaluation protocol that combines shared metrics for cross-setting comparison with scenario-specific metrics tailored to the core requirements of each setting. We also provide transparent reference baselines to support reproducible comparison. Experiments on UniPPTBench reveal substantial performance variation across settings and recurring failure modes in content grounding, multimodal integration, and cross-source synthesis. In particular, strong performance on generic presentation-quality metrics does not necessarily imply strong task fulfillment in grounded scenarios. Together, UniPPTBench and UniPPTEval provide a faithful and diagnostic foundation for evaluating presentation generation across diverse real-world scenarios. Code and data will be publicly available.

---


### 293. [Loaded Dice: Solving the Non-Selection Problem for Scalable Probabilistic RowHammer Defense](https://arxiv.org/abs/2605.17358)

**<font color=#1a73e8>作者：</font>** Jeonghyun Woo, Junsu Kim, Aamer Jaleel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> DRAM scaling has exacerbated the RowHammer vulnerability. To counter this, JEDEC recently introduced Per Row Activation Counting (PRAC) with the Alert Back-Off protocol as an optional DDR5 feature. While promising, PRAC requires per-row counter cells that incur area overhead, and updating them on every activation lengthens DRAM timing parameters, degrading performance. Probabilistic mitigations such as MINT offer a lower-cost alternative by randomly selecting and mitigating rows within periodic mitigation windows. MINT is effective at higher thresholds (>= 1000), but at lower thresholds, it must raise its mitigation rate to overcome the non-selection problem, where heavily hammered rows can repeatedly escape sampling. This fixed-rate scaling reduces effective memory bandwidth even when no attack is present.
To overcome this limitation, we propose PrISM, an intersection-based probabilistic mitigation that correlates sampled rows across windows using a Sampled History Queue (SHQ). PrISM samples a few activation slots per window, stores sampled-but-unmitigated rows in the SHQ, and requests an additional mitigation through the existing Alert Back-Off protocol when a sampled row reappears in this history. This allows PrISM to increase mitigation only when persistent row activity is observed, without globally increasing the fixed mitigation rate. At the threshold of 500, PrISM incurs a negligible 0.2% average slowdown compared to 14% for PRAC, with no DRAM array changes or per-row counters and only 625B of SRAM per bank, one to two orders of magnitude less than prior secure counter-based in-DRAM defenses. Compared to MINT, PrISM provides better scalability at low thresholds, reducing average slowdown from 10.7% to 1.5% at a threshold of 250, a 7.1x reduction. PrISM is open-sourced at this https URL.

---


### 294. [Learning Fill-in Reduction Ordering via Graph Policy Optimization for Sparse Matrices](https://arxiv.org/abs/2605.17362)

**<font color=#1a73e8>作者：</font>** Ziwei Li, Shuzi Niu, Huiyuan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix reordering in large sparse solvers seeks a permutation that minimizes factorization fill-in to reduce memory and computation. Because the minimum fill-in ordering problem is NP-complete and fill-in is implicit in the sparsity pattern, graph-theoretic heuristics are used. Existing reinforcement learning methods either ignore sparsity patterns--missing the global fill-in--or lack local exact fill-in feedback. We propose a graph policy optimization method, modeling fill-ins from global and local views: both the policy and value networks use a multi-hop graph neural backbone to embed global fill-in; the policy further interacts with symbolic factorization over graphs to extract local, step-level fill-ins, and the resulting feedback is aligned with the value network via an adaptive saturation function to improve convergence. On the SuiteSparse Matrix Collection, our method achieves mean reductions of 29.3 in fill-ins and 31.3 in peak memory usage over state-of-the-art baselines.

---


### 295. [Memory-Augmented Query Intent Understanding for Efficient Chat-based Image Retrieval](https://arxiv.org/abs/2605.17365)

**<font color=#1a73e8>作者：</font>** Xianke Chen, Daizong Liu, Yushuo Lou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Different from traditional text-to-image retrieval tasks, chat-based image retrieval allows the human-interactive system to iteratively clarify and refine user intent through multi-round dialogue, thereby achieving more fine-grained retrieval results. The key challenge in this task lies in dynamically understanding and updating the user's query intent across dialogue rounds. Although existing works have achieved great performance on this new task, they simply handle history query information either by directly concatenating all previous queries into a long textual sequence or by relying on large language models to reconstruct the current query from history. Such strategies are computationally redundant and easily lead to inconsistent intent representations as the dialogue progresses. To alleviate these issues, this paper proposes a novel and efficient memory-based user intent updating framework for the chat-based image retrieval task, called Memory-Augmented Query Intent Understanding (MAQIU). It introduces a lightweight memorization module that dynamically aggregates and evolves the semantic representation of query intent across dialogues, while a memory recall mechanism is further employed to prevent intent forgetting and enhance long-term semantic integrity. In addition, MAQIU also integrates historical image retrieval results as visual guidance, allowing the model to strengthen cross-round correlations and refine current visual understanding. Extensive experiments demonstrate that MAQIU achieves substantial performance gains while maintaining high computational efficiency, reducing dialogue encoding FLOPs by 86.4\% compared with the prior baseline ChatIR. Source code is available at this https URL.

---


### 296. [Bridging Data Trials and Task Barriers: A Unified Framework for Sketch Biometric Identification](https://arxiv.org/abs/2605.17367)

**<font color=#1a73e8>作者：</font>** Decheng Liu, Bin Hu, Xinbo Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Different from existing cross-modality identification tasks (e.g., heterogeneous face recognition, sketch re-identification, etc.), we introduce a novel yet practical setting for these related identification tasks, named \textbf{sketch biometric identification}, which aims to continually train a unified model across different data domains, even diverse identification tasks. Sketch biometric identification faces challenges, including scarce real sketch data, high annotation costs, privacy risks, and insufficient generalization ability of cross-task models. Existing methods usually rely on limited real data or single-task optimization, making it difficult to effectively address the joint challenges of cross-modality and cross-task. This paper proposes a unified framework that integrates efficient synthetic sketch generation and task-sequential continual learning. First, we design an efficient pipeline to generate a large-scale and high-quality synthetic person and face sketch data, which significantly reduces costs and avoids privacy risks. Meanwhile, we enhance the model's robustness by fusing real data. Second, we construct a universal unified framework for sketch biometric identification, which adopts a task-sequential training strategy: the model first completes sketch person re-identification learning on the person dataset; subsequently, it maintains the acquired person recognition capability through a trusted sample replay technique and seamlessly performs incremental training on the face dataset. This enables a single model to simultaneously handle the cross-task capabilities of multiple sketch biometric identification tasks. To support the study of the mentioned sketch biometric identification, we built a new large-scale benchmark, SketchUnified-BioID, with several practical evaluation protocols.

---


### 297. [RadGenome-Anatomy: A Large-Scale Anatomy-Labeled Chest Radiograph Dataset via Physically Grounded Volumetric Projection](https://arxiv.org/abs/2605.17368)

**<font color=#1a73e8>作者：</font>** Shuchang Ye, Mingyuan Meng, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anatomical structure labels for chest radiographs are essential for medical image segmentation and a broad range of downstream diagnostic tasks. However, annotating anatomy directly on 2D chest radiographs is labor-intensive and intrinsically ambiguous, as 3D anatomical structures are projected onto a single 2D plane where boundaries may overlap, be occluded, or appear only partially visible. Consequently, existing anatomy-labeled chest radiograph datasets remain limited in scale, anatomy coverage, and label reliability. To address these limitations, we introduce RadGenome-Anatomy, the largest anatomy-labeled chest radiograph dataset, containing over 10 million segmentation masks across 210 anatomical structures in 25,692 studies. It is constructed by projecting large-scale 3D anatomical masks from CT volumes into 2D radiographic space through canonical radiographic geometry. This shifts annotation from directly tracing uncertain 2D boundaries to defining anatomy in volumetric space, where structures that overlap or become partially invisible in radiographs remain spatially separable. As a result, each 2D mask represents the physically grounded projected footprint of a volumetrically defined structure. The scale and broad anatomical coverage of RadGenome-Anatomy, including structures that are overlapping, partially visible, or difficult to delineate directly, enable research on geometric measurements as explicit evidence for chest radiograph interpretation. We demonstrate this by training XAnatomy to predict structure-specific masks and derive clinically relevant measurements, achieving diagnostic accuracies of 96.4%, 95.6%, and 89.2% for cardiomegaly, kyphosis, and scoliosis, respectively.

---


### 298. [FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics](https://arxiv.org/abs/2605.17373)

**<font color=#1a73e8>作者：</font>** Qiran Zou, Hou Hei Lam, Wenhao Zhao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI research agents accelerate ML research by automating hypothesis generation, experimentation, and empirical refinement. Existing agent strategies range from greedy hill-climbing to tree search and evolutionary optimization, yet which strategy choices drive performance remains unclear. Answering this question requires a benchmark that separates agent strategy (e.g., search topology) from execution infrastructure (e.g., code editor), so that performance differences are attributable to strategy rather than infrastructure, and that provides process-level metrics beyond final scores to analyze exploration behaviors. Existing benchmarks offer limited support. We propose FML-Bench, a benchmark of 18 fundamental ML research tasks across 10 domains that separates agent strategy from execution infrastructure and defines 12 process-level behavioral metrics. Evaluating six representative agents, we find that: (1) strategy complexity alone does not guarantee strong performance: a simple greedy hill-climber nearly matches the best-performing tree-search agent, both well above the remaining agents; (2) our analysis suggests this pattern relates to improvement opportunity structure: greedy search tends to be more effective when opportunities are dense, while tree-search and evolutionary strategies tend to be more effective when opportunities are sparse; an adaptive agent built on this insight switches to broader exploration upon detecting improvement stagnation and outperforms the other six agents, lending initial support to this observation; and (3) process-level analysis reveals that early convergence and directionally focused exploration are significantly associated with final performance, while solution diversity and compute cost are not. Our benchmark is available at: this https URL.

---


### 299. [Heterogeneous Information-Bottleneck Coordination Graphs for Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.17393)

**<font color=#1a73e8>作者：</font>** Wei Duan, Junyu Xuan, En Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coordination graphs are a central abstraction in cooperative multi-agent reinforcement learning (MARL), yet existing sparse-graph learners lack a theoretically grounded mechanism to decide which edges should exist and how much information each edge should carry. Current methods rely on heuristic criteria that offer no formal guarantee on the learned topology, and no principled way to allocate different communication capacities to structurally different agent relationships. To address this, we propose Heterogeneous Information-Bottleneck Coordination Graphs (HIBCG), which learns a group-aware sparse graph in which both edge existence and message capacity are theoretically justified. With the graph information bottleneck (GIB) serving as the underlying tool, HIBCG first constructs a group-aligned block-diagonal prior that provides a closed-form criterion for edge retention -- determining which edges should exist and at what density per group block -- and then controls per-agent feature bandwidth on the resulting topology, compressing messages to retain only task-relevant content. We prove that the group-aligned prior strictly tightens the variational bound on topology learning, that the objective decomposes per group block, enabling differential edge control, and that capacity allocation follows a water-filling principle.

---


### 300. [Self-Supervised Learning for Sparse Matrix Reordering](https://arxiv.org/abs/2605.17403)

**<font color=#1a73e8>作者：</font>** Ziwei Li, Tao Yuan, Fangfang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rearranging the rows or columns of a sparse matrix using an appropriate ordering can significantly reduce fill-ins, i.e., new nonzeros introduced during matrix factorization, decreasing memory usage and runtime. However, finding an ordering that minimizes fill-ins is NP-complete. Existing approaches, including graph-theoretic and deep learning methods, rely on surrogate objectives without theoretical guarantees. The Fill-Path Theorem reveals a direct and intrinsic relationship between fill-in generation and the sparse structure of the matrix as path triplet inequalities. Here we first employ a multigrid graph network to capture structural information for each vertex. We then derive a triplet sampling strategy based on inequalities. Finally, we introduce an end-max chain loss function to reduce the number of triplets whose predicted scores satisfy these inequalities. Experimental evaluations on the publicly available SuiteSparse matrix collection demonstrate the superiority of the proposed method in terms of both fill-in reduction and speedup in LU factorization time.

---


> [!TIP]
> 当前位于：**251-300**（第 6/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
