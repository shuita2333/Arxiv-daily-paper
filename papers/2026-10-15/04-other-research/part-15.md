# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**701-750**（第 15/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | **701-750** | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 701. [Random Probing for Structural Self-Interactions in Graph Neural Networks](https://arxiv.org/abs/2610.18164)

**<font color=#1a73e8>作者：</font>** Saku Peltonen, H. Çağrı Bilgi, Kubilay Atasu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) fundamentally lack the ability to capture structural properties defined by node self-interactions, such as cycle counts, subgraph centrality, and heat kernel signatures. Existing solutions often rely on computationally expensive higher-order architectures or hand-crafted features. In this work, we introduce DIAL, a message-passing layer that gives nodes access to graph structure through the diagonal of graph-derived operators. Our approach uses randomized probing to provide nodes with learnable, permutation equivariant access to diagonal entries. We prove that our approach can express important structural features, including cycle counts, subgraph centrality, and heat kernel signatures. The proposed method can be integrated directly into message passing layers. Experiments on molecular property prediction, cycle counting, and pattern detection demonstrate the effectiveness of DIAL across a range of graph learning tasks.

---


### 702. [Back to the Future: Reverse-Consequence Modeling for Long-Horizon Particle Dynamics](https://arxiv.org/abs/2610.18168)

**<font color=#1a73e8>作者：</font>** Leyan Zhang, Nantian He, Jiajun Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of object trajectories is fundamental to mechanical understanding and robotic control. However, autoregressive models inherently suffer from cumulative errors, leading to severe drift in long-horizon rollouts. Observing that in many physical systems with dissipative or convergence-to-rest behavior, the final states are often more predictable than transient dynamics (e.g., a sliding object resting under friction or a pendulum stabilizing at equilibrium), we propose ReStep, a cascaded approach that reverses the conventional forward-prediction paradigm. ReStep first employs a stochastic model to directly predict the final state, then leverages Anchored Diffusion to generate goal-conditioned intermediate trajectories. By conditioning on both ''boundary states'', it effectively constrains dynamics and reduces uncertainty, producing physically plausible and temporally coherent transitions. We further integrate ReStep dynamics as the physical engine within a 3D Gaussian Splatting pipeline, enabling a unified physical-visual framework for intuitive inference from images. Extensive experiments on diverse rigid and non-rigid collision datasets show that ReStep achieves superior long-term accuracy, substantially mitigating error accumulation via reverse-consequence modeling.

---


### 703. [Neuro-Symbolic Graph Transformers for Hierarchical Intention Recognition from Multimodal Human Activity Sequences](https://arxiv.org/abs/2610.18176)

**<font color=#1a73e8>作者：</font>** Farnaz Soleimani, Abdelghani Chibani, Yacine Amirat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive human-robot collaboration requires autonomous systems to infer not only immediate actions but also the underlying hierarchical intentions governing human behavior. Current deep learning approaches predominantly focus on flat action classification, failing to capture the structural dependencies connecting kinematic motion to high-level goals. A Neuro-Symbolic Graph Transformer (NSGT) is proposed within this multimodal framework, a Human Reasoning Graph (HR-G) is integrated into the self-attention mechanism via learnable topological biases. Furthermore, the architecture is augmented with a differentiable First-Order Logic (FOL) loss, acting as a structural regularizer by which ontological consistency is enforced across four levels: atomic actions, composite activities, Low-Level Intentions, and High-Level Intentions. Evaluation is performed on the synthesized NTU-Hierarchy dataset, a four-level ontological extension of NTU RGB+D 120, wherein existing sequences were mapped into 119,383 complex hierarchical episodes (85 actions, 16 activities, 8 LLIs, 4 HLIs). To prevent circular supervision, strict isolation between label generation and FOL constraints was maintained. In the base configuration, 91.65% top-1 action accuracy is achieved by the NSGT. When the FOL loss is incorporated into the baseline, logic consistency is improved by 3.26 percentage points to 96.67%. Through the HR-G biases, a tunable trade-off between accuracy and structural coherence is established. In the primary consistency-maximizing configuration ($\lambda$ = 0.5), a logic consistency of 94.59% is reached and ontological contradictions are reduced by 33%, while a robust 89.90% top-1 action accuracy is retained. Finally, interpretable reasoning evidence is provided by the learned HR-G weights, wherein transition edges are strongly exploited ($\beta$ trans $\approx$ +2.6) without explicit supervision.

---


### 704. [Exploring Object Recall in an Object-Rich AR Office Scene](https://arxiv.org/abs/2610.18183)

**<font color=#1a73e8>作者：</font>** Sangita Kunapuli, Shane Dirksen, Radha Kumaran 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented reality (AR) changes how users perceive and attend to their surroundings. Prior work suggests AR can reduce attention to the physical world, but it remains unclear whether this holds in environments dense with both virtual and physical objects, and which factors most affect object recall. This study examines recall in a mixed-reality office scene after an object-selection task, testing object-level factors (virtuality, size), context-level factors (semantic congruency, saliency), and user-level factors (cueing, dual tasking). Cueing informed participants of a later recall test, while dual tasking added cognitive load through a secondary audio task. Virtual objects were recalled more accurately than physical ones. Cueing produced a modest improvement in recall of present objects. Using playback software to reconstruct each participant's view throughout the trials, we computed object-level saliency and found a weak positive correlation with recall, slightly stronger than the effects of virtuality, but not reaching statistical significance. These findings have implications for AR interface design and for building mixed-reality environments that better support cognition during real-world tasks.

---


### 705. [Reinforcement Learning for Large-Scale Lifelong Multi-Agent Path Finding with Shared Spatial Fields](https://arxiv.org/abs/2610.18186)

**<font color=#1a73e8>作者：</font>** Jean Seong Bjorn Choe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale applications of lifelong multi-agent path finding (LMAPF) call for computationally inexpensive movement decisions under changing traffic conditions and across varied layouts. We propose a navigation policy in which a convolutional network computes a shared spatial field over the map once per timestep and a compact goal-conditioned operator derives agents' movement preferences. The complete policy is trained end-to-end using average-reward reinforcement learning with throughput as the reward, without planner demonstrations or a separate online path planner. For structured and unstructured layouts, we train one policy per class on mixtures of small maps and deploy each without retraining on larger, unseen layouts and agent populations. Across six layouts with 10000 agents, our policies achieve throughput comparable to or higher than the strongest evaluated baselines. The proposed method has an average execution time below 10 ms per step, more than an order of magnitude faster than several established planners.

---


### 706. [VARI: Robust Text-to-Video Generation via Group-Structured Intent Alignment](https://arxiv.org/abs/2610.18189)

**<font color=#1a73e8>作者：</font>** Mingxuan Zhu, Hohei Chan, Shiyuan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-video (T2V) models generate visually compelling videos, yet meaning-preserving changes in prompt wording can substantially alter semantic realization and overall quality. Existing prompt rewriting modifies the inference input, whereas conventional post-training constructs supervision from one prompt formulation at a time; neither explicitly optimizes reliability across equivalent forms. We introduce VARI (Verified Alignment over Representations of Intent), a group-structured framework that treats automatically verified formulations of the same visual intent as a shared supervision unit. VARI builds matched form-seed rollout pools, cross-scores each video against all forms, and applies a wording-independent structured intent audit to identify valid realizations and hard semantic failures. Group-Consistent Distillation (GCD) aligns every verified form with interchangeable valid realizations, while Form-Contrastive Flow-DPO (FC-DPO) learns group-level preferences from audited positive-negative pairs, prioritizing same-seed, different-form contrasts. On HunyuanVideo-1.5, VARI attains the highest T2V-CompBench, VBench, and StoryEval scores among the evaluated methods. On prompt-form extensions of T2V-CompBench and VBench, it improves weakest-form alignment over the strongest prompt-level baselines by 2.45 and 3.55 points and reduces cross-form drop by 30.5% and 32.2%, respectively, while preserving visual quality. Human evaluation, natural-caption controls, prompt-enhancement experiments, diversity analyses, and transfer to LTX-2.3 further support the robustness and transferability of these gains, while VARI requires no additional inference-time module.

---


### 707. [QORH: Learning Query-Specific Ordered Rule Hypergraphs for Inductive Knowledge Graph Link Prediction](https://arxiv.org/abs/2610.18198)

**<font color=#1a73e8>作者：</font>** Naixing Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graph link prediction involving unseen entities and relations requires learning transferable reasoning patterns from observed graph structure. Existing methods based on relation graphs primarily capture pairwise dependencies, limiting their ability to preserve the compositional semantics, relation ordering, and role information of complete path rules. To address this limitation, we propose QORH (Query-specific Ordered Rule Hypergraph), which jointly encodes rule heads and ordered rule bodies as hyperedges conditioned on the query relation, explicitly modeling joint dependencies among multiple relations. QORH performs learnable rule selection using statistical evidence, such as rule confidence and coverage, and enhances relation representations through role-aware hypergraph message passing to guide entity-level reasoning. The model's shared parameters are independent of specific entity or relation identifiers, enabling inductive prediction for unseen entities and relations. Extensive experiments on entity-inductive and fully inductive benchmarks demonstrate that QORH significantly outperforms the state-of-the-art baselines included in our evaluation, validating the effectiveness of rule hypergraph modeling for inductive link prediction.

---


### 708. [Closing the Estimation Gap: Training-Free Transductive Inference for Cross-Domain Few-Shot Action Recognition](https://arxiv.org/abs/2610.18209)

**<font color=#1a73e8>作者：</font>** Changyi Li, Zeyu Yang, Yu Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-domain few-shot action recognition (CD-FSAR) aims to recognise unseen action classes in a target domain from a handful of labelled videos. Despite advances in representation learning, CD-FSAR inference still relies on prototypes estimated from extremely limited support examples. To assess this bottleneck, we perform an oracle analysis with the representation fixed. Constructing oracle prototypes and decision boundaries from ground-truth query labels improves 5-way 1-shot accuracy by 7--20 percentage points across five target datasets. This reveals a substantial estimation gap: the representation contains useful discriminative information, but prototypes and boundaries estimated from scarce supports fail to capture each episode's true class structure. Motivated by this, we propose TRACE, a training-free transductive inference framework that improves episode-level estimation without modifying the backbone. TRACE comprises two complementary stages. Confidence-Thresholded Transductive Prototype Refinement (CTPR) refines support-based prototypes using confidently predicted queries. The refined prototypes initialise a lightweight per-episode classifier, which Transductive Classifier Refinement (TCR) further adapts by encouraging confident, class-balanced predictions over all queries. Together, the two stages improve prototype and boundary estimation, enabling better use of information in the unlabelled queries. Across five target datasets (HMDB51, UCF101, SSv2, Diving48, and RareAct) in both 1-shot and 5-shot settings, TRACE consistently improves a strong CD-FSAR baseline, including gains of more than six percentage points on HMDB51 1-shot, while recovering much of the oracle-estimated gap. These results suggest that improving test-time estimation is a powerful, broadly applicable complement to representation learning for CD-FSAR under extreme support scarcity.

---


### 709. [Operator Surrogates](https://arxiv.org/abs/2610.18210)

**<font color=#1a73e8>作者：</font>** Christoph Schwab, Josephine Westermann, Jakob Zech  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This chapter provides a mathematical introduction to operator surrogates, which are finite-parametric maps approximating complex (typically nonlinear) operators between infinite-dimensional (function) spaces.
A typical approach to constructing operator surrogates is the encoder-approximator-decoder paradigm, whereby infinite-dimensional inputs are mapped to a finite-dimensional latent space, processed, and then mapped back to the infinite-dimensional output space. We discuss various methods for creating efficient representation systems, including stable linear frameworks like Banach frames and data-driven techniques such as Principal Component Analysis (PCA), Active Subspaces, and nonlinear autoencoders. Subsequently, we survey key surrogate architectures, contrasting spectral methods, based on polynomial chaos expansions and related technologies, with more recent neural network approaches. We further discuss architectures that do not rely on representation systems, such as Fourier Neural Operators and transformers. We elaborate on their relationship and how they relate to other neural network operator surrogates, particularly those obtained by so-called "algorithm-unrolling".
Additionally, we provide an introduction to the theoretical analysis of approximation and generalization errors. We explain how underlying low-dimensional structures, provided for example by holomorphy, are essential to overcome the so-called "curse of dimensionality": this refers to the fact that the complexity of numerical algorithms tends to increase exponentially in the problem dimensionality. We present convergence rate bounds for holomorphic operators that depend on the number of trainable parameters and the regularity of the input and output data. Throughout, we prioritize intuition over detailed technical proofs and provide precise pointers to the literature for detailed arguments.

---


### 710. [A Controlled Evaluation of Curvature Inspired Scalar Feature Scaling for Domain Generalization](https://arxiv.org/abs/2610.18227)

**<font color=#1a73e8>作者：</font>** Sunny Gupta, Amit Sethi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain-specific curvature is an appealing idea for domain generalization (DG), but curvature learning can denote substantially different computations. This paper evaluates one deliberately narrow implementation: the code calls it HyperDG, but it rescales Euclidean encoder features during training by learned positive scalars and uses an ordinary linear classifier on unscaled Euclidean features at inference. It does not implement a Lorentz or Poincaré representation, geodesic prediction, or a Sharpness-Aware Minimization inner loop. We audit the executed objective and evaluate six conditions on PACS, VLCS, Office Home, and TerraIncognita. The completed design contains 384 runs: six conditions, four held-out targets, and four run seeds per dataset. Checkpoints are selected using only the three source-validation environments. Inference first averages paired seed differences within each held-out target; targets, rather than 16 seed-by-target observations, are the per-dataset clusters. The full implementation's equal-dataset macro point estimate is 1.61 percentage points below native DomainBed ERM (95% clustered CI [-3.17, -0.04]). All four dataset point estimates favor ERM, but an exact four-dataset sign-flip test gives p = .125 and Holm-adjusted p = .250; we therefore claim no adjusted evidence of a difference. The cleaner domain-specificity contrast, separate learned source scales without their variance penalty versus one shared learned source scale, is -0.13 pp (95% CI [-0.53, 0.27]). Its 90% CI lies within a revision-stage $\pm 1$ pp smallest effect of practical interest (TOST p = .003), supporting equivalence only for the source-selected suite macro, not every dataset, target, or final-step endpoint. The study thus supplies a bounded negative result for this scalar training package; it does not test or refute genuine hyperbolic representation learning.

---


### 711. [Consider, Then Choose: Order-Invariant Decisions in System One Models](https://arxiv.org/abs/2610.18233)

**<font color=#1a73e8>作者：</font>** Jianguo Huang, Yao Long Teng, Yanchen Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System One models answer typed questions in a single forward pass and promise the same answer for the same input. For choice questions, this promise fails: the answer depends on the order of the options, increasingly so as they grow in number, and averaging over their cyclic shifts reduces this dependence without removing it. Scoring each option alone, which the order cannot affect, shows that the order changes the answer mostly when the model is unsure among its top few options, even though the listwise answer looks confident. We therefore propose $\textbf{Runoff}$, which considers, then chooses: it scores each option alone to keep a few candidates, then compares them in listings where each candidate takes every position. It needs no training and can run in two forward passes, and its answer does not depend on the option order by construction. On two open models and five datasets, it changes no answer under shuffling, against 9.3% for cyclic averaging, and with 20 options it is about as accurate and three to four times faster. Wrapped around eight System One models, it removes the order dependence of the five benchmarks, while cyclic averaging changes up to 15.4%.

---


### 712. [LiFUSE: Frequency-Spatial Unified Self-Supervised Pretraining for Liver Disease Analysis on Non-contrast CT](https://arxiv.org/abs/2610.18243)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Yi Huang, Wei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given the growing global burden of liver tumors and diffuse liver diseases, non-contrast computed tomography (NCCT) is increasingly used for opportunistic screening because of its low cost and favorable safety profile. However, downstream tasks such as tumor detection and fine-grained disease diagnosis remain challenging due to NCCT's inherently low tissue contrast, lack of hemodynamic enhancement, and complex anatomical background. These limitations make subtle, heterogeneous, and multifocal hepatic lesions difficult to identify. Although large-scale self-supervised pretraining can learn robust representations from unlabeled NCCT scans, conventional voxel-wise reconstruction does not fully exploit the complementary information available in NCCT. Under weak NCCT contrast, low-level intensity patterns become less informative for pathology recognition, limiting the capture of lesion-specific discriminative features. In this paper, we propose the Liver Frequency-Spatial Unified Self-Supervised Pretraining (LiFUSE). The frequency branch applies random band-stop masking and spectrum reconstruction to encourage the model to capture subtle differences between lesions and surrounding tissues, while the spatial branch performs hybrid-granularity masked volumetric reconstruction to accommodate lesions of diverse sizes and morphologies. Finally, a cross-domain consistency scheme couples the spatial and frequency branches, yielding more discriminative representations for hepatic structures and lesions. Extensive experiments on three clinically relevant tasks across internal cohorts and a public target-domain transfer setting show that LiFUSE consistently outperforms strong baselines. These results suggest that unified frequency-spatial learning can improve liver disease analysis on NCCT, highlighting its potential for large-scale screening.

---


### 713. [Optimal Online Regret for Context-Lumpable Bandits](https://arxiv.org/abs/2610.18258)

**<font color=#1a73e8>作者：</font>** Chenyu Lu, Zihan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic contextual bandits with an unknown context-lumpable structure. The $S$ contexts are partitioned into $r$ blocks, and every arm has the same mean reward across contexts in the same block. Under arbitrary context distributions and without separation assumptions, we design an algorithm with expected regret $\widetilde{O}(\sqrt{r(S+K)T})$, matching the lower bound of Lee et al. (2023) up to logarithmic factors and improving their previous upper bound by a factor of $r$.
The algorithm operates over dyadic accuracy levels, using a baseline policy and confidence-based early stopping to control exploration. It then performs cross-context elimination: since rewards are identical within a block, one selected arm eliminates all surviving records from that block, requiring at most $r$ selections at each level. Multi-scale exploration assigns finer accuracies to frequent blocks and coarser accuracies to rare blocks, yielding a near-optimal arm for every block while keeping the weighted policy error small.

---


### 714. [FALLNEST: Dual-Domain Dataset Condensation of Imbalanced IMU Data for Wearable Fall Detection](https://arxiv.org/abs/2610.18260)

**<font color=#1a73e8>作者：</font>** Rashi Niyas P, Ritika Jain, Hitika Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wearable fall detection is hampered by rare fall events, scarce labeled IMU data, and the cost of training deep models on large, imbalanced corpora. Existing methods either rely on hand-crafted features with shallow classifiers, which limits learning from raw signals, or train deep networks on full datasets that require re-sampling to counter class skew and demand substantial data and compute. To address this, we propose a novel Fall detection framework via Normalized-gradient and Embedding matched Synthetic Time-frequency condensation, dubbed FALLNEST, a data-centric approach that distills large, imbalanced IMU datasets into tiny, class-balanced synthetic training sets. Building on dual-domain time-series condensation (CondTSC), FALLNEST introduces a fall-specific 7-channel input with accelerometer vector magnitude, class-balanced K-Means initialization, and normalized gradient matching with gradient clipping, combined with MMD-based embedding alignment and multi-view Fourier-domain augmentation, so that class balance arises from the condensed set itself rather than from re-sampling. We evaluate on SisFall, KFall, and MobiFall using strict subject-wise splits and naturally imbalanced test sets, reporting accuracy, Macro-F1, and PR-AUC over five seeds. A 102K-parameter TinyCNN trained on only 32 to 146 synthetic windows (about only 1% of the training windows) reaches 93.5-95.8% mean accuracy and 0.89-0.98 PR-AUC, with standard deviations of 1.0-1.7% in accuracy, demonstrating the efficacy of our approach.

---


### 715. [JevGPT: Thinking Fast and Slow in Autonomous Research](https://arxiv.org/abs/2610.18272)

**<font color=#1a73e8>作者：</font>** Yasheng Sun, Yanning Dai, Yimeng Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents must acquire and reason over evidence within a limited budget. Yet relevant sources can remain uninspected or unused, leaving a gap between retrieval coverage and the evidence that informs research. The challenge is to align fast local judgments with changing evidence needs and feed their findings back into research decisions. We introduce JevGPT, a dual-system architecture for autonomous research that couples fast evidence processing with deliberative research planning. System Two sets evidence objectives and integrates findings, while System One locates support, assesses relevance, and guides further inspection. Independent source judgments run in parallel; selected original passages inform the next research step. Experiments on fixed-corpus question answering and document ranking show that JevGPT achieves leading task performance, with faster completion and lower cost than comparably effective research agents. Evidence analysis shows broader source inspection and greater coverage of supporting documents in the research loop, highlighting efficient evidence processing as a route to more capable autonomous research.

---


### 716. [Traditional and Recent Approaches for Infrared Small Target Detection : Overview, Challenges and Perspectives (Part 1)](https://arxiv.org/abs/2610.18276)

**<font color=#1a73e8>作者：</font>** Thierry Bouwmans, Anastasia Zakharova, Belmar Garcia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection is often used in different civilian and military applications to detect static or moving targets in scenes like in ground, air and sea surveillance. First valuable research has emerged since 30 years ago and the two last decades witnessed very significant publications in this field following the rise of low-rank and sparse decomposition (model-based methods) and deep learning models (data-based methods). Furthermore, several surveys can be found in the literature but none of them addresses an overall review in this field. In this context, the aim of this paper is to provide a complete survey of the traditional and recent approaches in infrared small target detection. First, we categorize the different approaches found in the literature in terms of the modeling models, i.e mathematical models, machine learning models and signal processing models. Then, we have discussed them in terms of the critical situations that they claim to handle. Furthermore, we present the available resources, datasets and libraries. Then, we conclude with several promising directions for future research. For the sake of reading, this survey is divided into two parts: 1) "Traditional and Recent Approaches for Infrared Small Target Detection : Overview, Challenges and Perspectives (Part 1)" about conventional and low-rank and sparse decomposition (model-based methods), and 2) "Traditional and Recent Approaches for Infrared Small Target Detection : Overview, Challenges and Perspectives (Part 2)" about deep learning models (data-based methods).

---


### 717. [PING: physics informed graph neural network for advection-diffusion processes with applications to solar power forecasting](https://arxiv.org/abs/2610.18280)

**<font color=#1a73e8>作者：</font>** Jelena Simeunović, Baptiste Schubnel, Pierre-Jean Alet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advection-diffusion plays an essential role in transport phenomena such as atmospheric and cloud dynamics. Improved forecasting of cloud motion, in turn, enhances solar power production forecasts and facilitates the integration of additional photovoltaic (PV) sources into the power grid. However, both classical numerical models and emerging deep learning approaches face challenges when applied to spatially irregular sensor networks such as those formed by weather stations. In this work, we adopt a graph signal processing perspective and model advection-diffusion particles as signals on a graph to capture the dynamics of these processes. We introduce a Physics-Informed Graph Neural Network (PING) for forecasting future advection-diffusion particle concentrations on irregular grids. The model incorporates a discretized advection-diffusion equation as a soft constraint in the loss function to guide learning toward physically consistent solutions. This model is on par with state of the art models on synthetic and real transport phenomena datasets, including sea surface temperature and cloud index datasets. Furthermore, the PING model is successfully coupled with models for forecasting PV power production. This hybrid approach leverages data fusion from ground-based sensors at PV stations and satellite images with cloud concentration to improve the accuracy of intra-day PV power production.

---


### 718. [Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation](https://arxiv.org/abs/2610.18284)

**<font color=#1a73e8>作者：</font>** Yaoli Liu, Guo-Hua Wang, Yiyang Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generated images often have coherent layouts and visual content, yet local errors in small text and complex characters still limit their readability and practical use. Scene-text refinement requires accuracy, preservation, and efficiency. Existing methods based on variational autoencoders (VAEs) can lose fine strokes during reconstruction, while full-image editing can shift background colors. In this work, we introduce PixText, a model that formulates local text refinement as grouped image generation in pixel space. Conditioned on the original image, PixText generates only the target regions, preserves unedited content, and uses MeanFlow for four-step generation. We further introduce Text Refinement Bench to evaluate text correction and image preservation in generated images. On this benchmark, PixText achieves 83.06% glyph pass and 94.66% exact target-character OCR accuracy, versus 36.77% and 52.31% for the strongest baseline. Its four-step MeanFlow variant retains an 81.84% pass rate with less than one GPU-second of amortized generation cost per image.

---


### 719. [LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](https://arxiv.org/abs/2610.18289)

**<font color=#1a73e8>作者：</font>** Ziyu Zhu, Zhaoxu Sun, Fan Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models have emerged as a foundation for long-horizon world rollout. However, when extended far beyond their training windows, these models suffer from progressive drift: visual quality deteriorates, motion becomes inconsistent, and object identity gradually collapses as generated frames are recursively reused as context. We study a supervision-horizon gap: short-horizon distillation leaves later rollout states without direct supervision. We show that matching short-window marginals need not determine long-horizon behavior, while longer on-policy trajectories expose delayed failures to training. This motivates temporal manifold matching at scale for long-horizon world models. Building on this insight, we introduce LongForcing, a distillation approach that scales teacher supervision to long student self-rollouts. LongForcing preserves the short-horizon teacher-forcing and causal ODE-distillation stages, while replacing the realscore teacher in the final distribution-matching stage with an extended-horizon bidirectional teacher. The long-horizon teacher supervises extended student self-rollouts using the standard distribution-matching formulation, without modifying the student architecture or increasing inference cost. We evaluate LongForcing on text-to-video generation and interactive action-conditioned world models, achieving a VBench Quality score of 85.52 and improving WorldRoamBench 60s action score by 23.9 points in first-person ablations. Qualitative stress tests further sample interactive rollouts up to 24 hours, far beyond the training horizon. These results suggest that scaling supervision along the temporal axis is a practical step toward long-horizon world models. The project website and code are at this https URL.

---


### 720. [Reliable Risk Estimation with Kernel Mean Matching under Dependent Sampling](https://arxiv.org/abs/2610.18292)

**<font color=#1a73e8>作者：</font>** Alexey Zaytsev, Diana Koldasbayeva, Egor Serov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel Mean Matching (KMM) estimates risk under covariate shift by reweighting labelled source samples so that their kernel mean embedding matches that of unlabeled target samples. Existing finite-sample guarantees are usually stated for independent samples, although many applications involve temporal, spatial, or clustered dependence. We give a finite-sample KMM analysis under dependent sampling by replacing nominal sample sizes with effective sample sizes in the concentration steps used by the classical proof. The approach uses Bernstein inequalities for geometrically strongly mixing processes and derives a model-based effective sample size. The resulting bound separates overlap, dependence, and smoothness effects with specific constants derived under a Gaussian process assumption. This analysis yields an additional tradeoff: smoother losses preserve more input dependence and therefore reduce effective sample size, while also reducing function complexity and empirical-to-population risk gaps. Applying the result to prediction yields confidence intervals that achieve near-nominal coverage in synthetic experiments and substantially reduce undercoverage on real monitoring data.

---


### 721. [Which Optimizer Leaks Most? Optimizer Implicit Bias as a Training-Data Privacy Controller](https://arxiv.org/abs/2610.18294)

**<font color=#1a73e8>作者：</font>** Sagi Habani, Yehonathan Refael, Ofir Lindenbaum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Releasing a neural network checkpoint can leak information about its training data, and existing reconstruction results rely on gradient-descent training. We ask whether the choice of optimizer affects the ability to recover the training data. Extending work connecting Karush--Kuhn--Tucker conditions to training-data reconstruction, we show that the implicit biases of popular optimizers (SGD, Adam, Muon) leave very different fingerprints of the training data. We argue that the key distinction is the \emph{weight-specificity} of these implicit biases, namely how much continuous information about the final weights the optimizer-dependent target of the stationarity conditions encodes. The limiting stationarity conditions for models trained with SGD and Muon retain enough weight-specific information to reconstruct training examples in practice. For Adam in the $\ell_\infty$ implicit-bias regime, the optimizer-dependent part of these conditions encodes only a discrete pattern of maximal coordinates and their signs, and at nondegenerate KKT points the conditions are too few to identify the training set to first order. Experiments on MNIST and CIFAR-10 support these claims: models trained with Muon can yield stronger reconstructions at much lower training cost than models trained with SGD, although this advantage depends on the training regime and architecture, and models trained with Adam appear consistently more resistant to the evaluated attacks.

---


### 722. [LegalRewardBench: Benchmarking Reward Models for Legal Preference Evaluation](https://arxiv.org/abs/2610.18299)

**<font color=#1a73e8>作者：</font>** Hui Huang, Jie Zhou, Hongli Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reward models are central to preference alignment for legal tasks, yet existing reward model benchmarks are still primarily centered on general-domain preferences. In this work, we introduce LegalRewardBench, the first human-verified benchmark for evaluating reward models in the legal domain. The benchmark organizes legal preference evaluation into five capability levels: knowledge, understanding, analysis, decision, and writing, and preference examples are constructed through rubric-guided automatic judging combined with human verification. We evaluate three families of judges, covering both general and fine-tuned models, and generative and discriminative architectures. Experimental results show that strong general-purpose generative models are currently the most robust legal reward models, while existing fine-tuned reward models transfer less reliably to legal preference evaluation. We also conduct detailed comparisons of input organizations and training strategies.

---


### 723. [A dataset of formalised theorem statements from the Annals of Mathematics](https://arxiv.org/abs/2610.18301)

**<font color=#1a73e8>作者：</font>** Thomas Browning, Katerina Hristova, David Ledvinka 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress in autoformalisation of mathematics using AI has been impressive. Measuring this progress requires datasets of formal statements that are both hard and trustworthy. We present AnnalsChallenge: 50 formalised theorem statements written by hand in Lean 4 using Mathlib. Each is the main result of a paper published in the Annals of Mathematics since 2020. Every formalisation was manually reviewed and then audited by AI. We release them without formalised proofs.

---


### 724. [Bayesian Optimization of CVaR with Unknown Hyperparameters](https://arxiv.org/abs/2610.18306)

**<font color=#1a73e8>作者：</font>** Valentin Margraf, Jonas Hanselle, Viktor Bengs 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Bayesian optimization of the Conditional Value-at-Risk (CVaR) of an expensive black-box function that depends on a decision and an environmental variable. Existing no-regret algorithms assume that the correct Gaussian process (GP) kernel and its hyperparameters are known. In practice, however, they must be estimated from limited data, often yielding a misspecified surrogate. This is especially damaging for CVaR because misspecification can distort the estimated tail-risk and thus lead to catastrophic decisions. We propose HE-CV-UCB, the first no-regret algorithm for CVaR Bayesian optimization with unknown GP hyperparameters. Given a finite candidate set containing a well-specified model, HE-CV-UCB adaptively eliminates those inconsistent with the observed data, actively queries where the survivors disagree, and returns a design that is robust across the surviving candidates. We prove that it attains cumulative regret matching the oracle rate of CV-UCB up to a factor depending only on the candidate set's size. Across synthetic benchmarks and three real-world applications, HE-CV-UCB achieves competitive performance and frequently outperforms existing CVaR Bayesian optimization methods.

---


### 725. [BALLAST: Physics-Aware Moving Target Defense for Industrial Control Systems Using a Digital Twin Safety Oracle](https://arxiv.org/abs/2610.18311)

**<font color=#1a73e8>作者：</font>** Oscar Mogollon-Gutierrez, Mohammadhossein Homaei, Alberto Lopez-Trigo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial Control Systems run on static network configurations, which leaves an attacker unlimited time to map the plant. Moving Target Defense answers this by shuffling addresses, but almost every published scheme never checks whether the reconfiguration will itself disturb the physical process it protects, so the defense can destabilise a control loop or trip an actuator. We present BALLAST, which places a learned Digital Twin between the security policy and the plant as a safety oracle. A physics-informed LSTM surrogate forecasts the physical effect of a candidate network change, a reinforcement learning agent trades security entropy against process stability, and a connection-draining handover lets in-flight Modbus transactions complete before the old mapping is withdrawn. An explicit shield rejects any action whose predicted trajectory would leave the safe operating envelope. On the SWaT water treatment testbed, Ballast cut the success rate of an adversary's reconnaissance sweep by 85 percent and recorded no safety violation across 50 runs, a 95 percent upper bound of 5.8 percent on the violation rate, against five violations and a tracking error 19 times larger for RL-MTD, the closest published analogue to our design. Measured against the strongest baseline on the physical metrics, a threshold-triggered scheme that itself records one violation rather than RL-MTD's five, Ballast still improves the tracking error by a factor of 2.5 and removes that remaining violation. The gain costs a small and deliberate concession in raw deterrence. Twin inference meets the 50 ms budget on a workstation core and an embedded GPU, and is projected to meet it on both edge CPUs when the three envelope stages are evaluated in a single batched call; the complete decision-to-enforcement path was measured only on the workstation.

---


### 726. [Complex materials engineering via Provenance Action Graphs: potential, structure and demonstration](https://arxiv.org/abs/2610.18314)

**<font color=#1a73e8>作者：</font>** Yevgeny Rakita, Paul Todd, James R. Neilson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work discusses and tests the potential of reaction graphs for material synthesis, in which events consist of reaction steps (actions) and their outputs (observations). The importance comes from the requirement to synthesize technologically useful materials, especially those that are kinetically stabilized. Often, it is a science that follows years of trial and error, culminating in (published) successful recipes, but is truly driven by far more (unpublished) failures. The entry into the era of AI provides an opportunity to use learning algorithms to encode rules from multi-dimensional synthesis pathways, regardless of their technological usefulness, and to decode both forward prediction and inverse learning modes. The main incentive is to accelerate material discovery by generating a global knowledge base that can be shared among data agents and contributed to by them. We will focus on several scenarios in the common synthesis process during solid-state synthesis, primarily because these reactions are kinetic in nature and require closer monitoring and control of the reaction history.

---


### 727. [Over-parameterization Is Neither Robust nor Fragile in Matrix Sensing: A Geometric Theory of Solution Robustness](https://arxiv.org/abs/2610.18318)

**<font color=#1a73e8>作者：</font>** Runze Shi, Ziye Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over-parameterization is ubiquitous in modern machine learning, yet its effect on robustness remains poorly understood. We study this question in matrix sensing, a canonical non-convex problem that can also be viewed, under an appropriate parameterization, as training a two-layer quadratic neural network. We develop a rank-aware robustness theory for the Burer-Monteiro factorization when the search rank k may exceed the target rank r_star, thereby capturing over-parameterization. Our analysis shows that robustness depends jointly on the degree of over-parameterization and the local geometry of the attained second-order stationary point: increasing k generally worsens sensitivity, but stationary points with the same search rank can exhibit substantially different robustness. Motivated by this observation, we propose a trajectory-aware algorithm that uses spectral balancing and randomized sketching to steer optimization toward less sensitive solutions. In matrix-sensing experiments, the method reduces paired sensitivity by 18-29 percent for isotropic operators and 87-89 percent for weak-tail operators, without degrading reconstruction accuracy. These results demonstrate that parameter count alone does not determine robustness and identify solution geometry and the optimization trajectory as important levers for improving it.

---


### 728. [ShoeFit: A New Dataset and Dual-image-stream DiT Framework for Virtual Footwear Try-On](https://arxiv.org/abs/2610.18325)

**<font color=#1a73e8>作者：</font>** Yuhan Li, Zhiyu Jin, Yifan Tong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual footwear try-on (VFTON), a critical yet underexplored area in virtual try-on (VTON), aims to synthesize faithful try-on results given diverse footwear and model images while maintaining 3D consistency and texture authenticity. Unlike conventional garment-focused VTON methods, VFTON presents unique challenges due to (1) Data Scarcity, which arises from the difficulty of perfectly matching product shoes with models wearing the identical ones, (2) Viewpoint Misalignment, where the target foot pose and source shoe views are always misaligned, leading to incomplete texture information and detail distortion, and (3) Background-induced Color Distortion, where complex material of footwear interacts with environmental lighting, causing unintended color contamination. To address these challenges, we introduce MVShoes, a multi-view shoe try-on dataset consisting of 7305 well-annotated image triplets, covering diverse footwear categories and challenging try-on scenarios. Furthermore, we propose a dual-stream DiT architecture, ShoeFit, designed to mitigate viewpoint misalignment through Multi-View Conditioning with 3D Rotary Position Embedding, and alleviate background-induced distortion using the LayeredRefAttention which leverages background features to modulate footwear latents. The proposed framework effectively decouples shoe appearance from environmental interferences while preserving high-quality texture detail through decoupled denoising and conditioning branches. Extensive quantitative and qualitative experiments demonstrate that our method substantially improves rendering fidelity and robustness under challenging real-world product shoes, establishing a new benchmark in high-fidelity footwear try-on synthesis.

---


### 729. [Strategic Multi-Agent Resource Allocation via Statistical Contracts](https://arxiv.org/abs/2610.18336)

**<font color=#1a73e8>作者：</font>** Ben Chugg, Michael I. Jordan, Aaditya Ramdas  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study a class of strategic hypothesis testing problems in which a principal aims to allocate resources among competing agents who possess data or data-generating mechanisms that may be relevant to the principal's goals. Each agent can pay a participation cost to opt into a statistical contract, in which case they generate data from a private distribution and receive an allocation based on a predetermined (and publicly known) mechanism. Each agent is either "null" or "non-null" and the principal's goal is to design the contract to limit the allocation to the former while maximizing transactions with the latter. Using e-values, we define a "continuous-closure," a set of allocations which prevents null agents from profiting in expectation and provides post-hoc risk control for general loss functions under arbitrary dependence. When the loss is the fraction of resources allocated to null agents, the region admits polynomial-time linear optimization. We also give explicit, interpretable closed-form approximations, and we analyze participation from a non-null agent's perspective, giving conditions under which entry into the contract is profitable. Finally, we extend the framework to support online arrival of the agents, in which case the principal has to make irrevocable on-the-fly decisions, and provide a method which gives time-uniform error-control in this setting.

---


### 730. [CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations](https://arxiv.org/abs/2610.18342)

**<font color=#1a73e8>作者：</font>** Jiahui Sun, Ran Bi, Yifei Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban spatial intelligence calls for 3D cities that agents can measure, interpret, and modify across successive tasks. Maintaining such cities as persistent, code-based states requires lightweight acquisition and support for consistent state updates without repeated dense reconstruction. We therefore formulate a new setting for grounded urban world construction: generating large-scale, instance-level parameterized 3D cities from one low-altitude aerial RGB image per region and known camera parameters, while recovering metrically scaled buildings and explicit road geometry and connectivity. We introduce CityCode, an agent-operable representation that unifies metric geometry, urban topology, visual semantics, and 3D assets through persistent entity identities, with dependency-aware versioned execution for validated updates and historical restoration. We further develop Air2Code to construct this representation by combining visual structure extraction with adapted metric depth estimation. To address occlusion and incomplete coverage, recovered structure and observed appearance guide generative completion and subsequent structure-aware 3D generation for buildings and backgrounds. Experiments on CitySample-Aerial and UrbanScene3D demonstrate substantially more accurate metric structure recovery and superior visual fidelity to the target cities compared with the evaluated baselines. Across 50 task chains of 50 steps each, CityCode supports continued querying, editing, planning, and historical restoration over evolving city states. Together, CityCode and Air2Code turn sparse aerial observations into persistent, agent-operable urban worlds for long-horizon urban spatial intelligence.

---


### 731. [ABot-ER: Unified Embodied Reasoning through Agentic Data-Model Co-Evolution](https://arxiv.org/abs/2610.18355)

**<font color=#1a73e8>作者：</font>** Qiuyu Ding, Heng-Da Xu, Changda Xia 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce \textbf{ABot Embodied Reasoning (ABot-ER)}, a unified embodied reasoning foundation model that breaks the tension between breadth and depth in embodied reasoning. Embodied intelligence demands the joint mastery of perception, planning, and execution, yet reconciling generality with specialization across this spectrum remains an open challenge. Within a single unified model, ABot-ER commands specialist-level depth across all three competencies, spanning spatial, scene, and temporal reasoning in perception; long-horizon action organization in planning; and point grounding and affordance in execution. The \textbf{Agentic Data-Model Self-Evolution Engine} continuously adapts data strategies to the model's evolving capability state. The \textbf{Task-Conditioned Adaptive Training Strategy} uses task tokens to activate lightweight low-rank residuals over a shared backbone, separating updates from heterogeneous output formats while retaining shared embodied knowledge. Across a systematic evaluation on twelve benchmarks covering three core competencies and five capability dimensions, ABot-ER achieves \textbf{state-of-the-art overall performance} across perception, planning, and execution within a unified parametric framework, demonstrating that breadth and depth can coexist in unified embodied reasoning.

---


### 732. [Understanding the "Why": Investigating the Design of Privacy Support Tools (PSTs) through the Lens of Psychological Needs](https://arxiv.org/abs/2610.18366)

**<font color=#1a73e8>作者：</font>** Sara Hahn, Verena Zimmermann, Simon Althaus 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Privacy Support Tools (PSTs) help users control their digital data, but face low adoption due to resignation and overwhelm. While current regulations aim to enhance privacy control, users still struggle to manage their privacy. To address this, we explore how PSTs can be designed for long-term adoption by applying the theoretical lens of psychological needs, as their fulfillment motivates users to use a digital product. We conducted in-depth interviews with 15 users and identified Security, Autonomy, and Competence as key psychological needs. From our results, we derive implications and recommendations for the need-sensitive design of PSTs.

---


### 733. [SchemaPose: RGB-Based Category-Level Pose Estimation with Parametric Category Schema](https://arxiv.org/abs/2610.18374)

**<font color=#1a73e8>作者：</font>** Shuang Wu, Jiude Wei, Cewu Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-based category-level 9D pose estimation remains highly challenging because a monocular system must generalize across unseen object instances while jointly inferring 3D translation, 3D rotation, and 3D size. Unlike instance-level pose estimation, the category-level setting requires the network to learn both what is shared across objects within a category and how individual instances vary in structure. This challenge is amplified in the RGB-only setting, where pose cues, category-level commonality, and instance-specific variation are entangled in appearance without direct geometric constraints, making it difficult for existing frameworks to learn a representation that is truly aligned with the category-level estimation objective. To address this problem, we propose SchemaPose, a schema-guided framework for RGB-based category-level pose estimation. SchemaPose equips the estimation pipeline with an explicit parametric schema for modeling category-level regularities together with structured instance variation, and uses the inferred schema variables to guide pose-related prediction in an end-to-end query-based framework. The same formulation also supports template instantiation, synthetic annotation, and pose learning within a unified framework. Experiments on synthetic and real data show that SchemaPose achieves state-of-the-art performance among RGB-based methods for category-level 9D pose estimation.

---


### 734. [Beyond Task Success: A Theory of Representation Reuse](https://arxiv.org/abs/2610.18375)

**<font color=#1a73e8>作者：</font>** Zibo Meng, Andrew C. M. Austin, Alin Achim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learned representation is useful beyond its source task only if later tasks can make use of what the encoder has already learned. Source-task performance, however, gives no guarantee that the representation itself will remain useful once the original head is removed. We study representation reuse with respect to a specified family of future tasks. For such a family, we define the task-relevant state as the coarsest deterministic state sufficient for all of its tasks. A larger task family can require a finer state, and losing a required distinction makes at least one future task unrecoverable on a target support containing that conflict. Exact reuse also depends on how the retained information is presented to the downstream rule. We separate this into structural accessibility, which concerns whether the required distinctions remain recoverable, and coordinate consistency, which concerns whether those distinctions can be interpreted by the same downstream rule across samples. Both failure modes appear separately in the experiments. Reuse improves as task-relevant distinctions become more accessible. Reversible sample-dependent coordinate changes can sharply reduce reuse even when the representation remains recoverable, and inverting the applicable coordinate change restores performance. The same accessibility-reuse ordering appears in prospectively specified CIFAR-100 experiments with both ResNet-18 and DenseNet-121. Finally, preserving a candidate state that contains the distinctions needed by the anticipated task family improves reuse on compatible held-out tasks, with the clearest benefit when target supervision is limited. Representation reuse is therefore relative to the tasks that follow source learning: a useful representation must retain the distinctions those tasks need and make them available in a form that a shared downstream rule can use.

---


### 735. [Noise2Match: Self-Supervised Low-Dose CT Denoising via Adaptive Inter-Slice Matching](https://arxiv.org/abs/2610.18379)

**<font color=#1a73e8>作者：</font>** Langrui Zhou, Guang Li, Xinyu Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid development of deep learning, supervised convolutional neural network methods have greatly improved the performance of low-dose computed tomography (CT) denoising. However, they require paired noisy-clean training data, which is difficult to obtain in practice. Some classic self-supervised denoising methods rely on the assumption of pixel-wise independent noise, making them ineffective for correlated noise in low-dose CT (LDCT) images. Considering the high similarity and weaker noise correlation between adjacent CT slices, several recently proposed self-supervised methods use adjacent LDCT slices for training. Nevertheless, these approaches fail to effectively account for the non-rigid misalignment between slices caused by anatomical variation, hindering them from satisfying the equal-mean condition required by the classic Noise2Noise framework. In this paper, we propose Noise2Match, a self-supervised LDCT denoising method based on adaptive inter-slice matching. Noise2Match introduces an inter-slice matching network to model the label transition process between adjacent slices, and then applies correction to the denoiser's outputs to better satisfy the equal-mean condition. We theoretically prove that, under idealized conditions, training Noise2Match using adjacent LDCT slices is equivalent to supervised training with paired noisy-clean images. We further find that Noise2Match can also effectively perform low-dose conebeam CT (CBCT) denoising, which could be attributed to its correction operation that reduces inter-slice noise correlation. To the best of our knowledge, Noise2Match is the first effective image-domain self-supervised method for low-dose CBCT. Extensive experiments demonstrate that Noise2Match outperforms existing image-domain selfsupervised methods, offering broader applicability and higher practical value.

---


### 736. [HULK: An Efficient Algorithm for Enabling Fast Bulk Bitwise Operations on Homomorphically Encrypted Data](https://arxiv.org/abs/2610.18391)

**<font color=#1a73e8>作者：</font>** Mayank Kabra, Phillip Widdowson, Harshita Gupta 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A wide range of important cloud applications, e.g., database analytics, graph analytics, and genome analysis, spend a considerable amount of time performing bulk bitwise operations (e.g., AND, OR, XOR). These applications often operate on highly sensitive data, making data privacy a critical concern. Homomorphic encryption (HE) enables secure computation on encrypted data without requiring decryption, ensuring privacy in untrusted and shared environments. We analyze 13 end-to-end applications across three domains (healthcare, graph, and database analytics) and observe that bulk bitwise operations take 62-100% of the execution time of the healthcare and graph workloads. The key problem is that existing HE approaches perform them with high-latency homomorphic operations (e.g., multiplication or lookup tables) and significantly increase the data size. Our goal is to enable fast bulk bitwise operations on homomorphically encrypted data by designing an efficient HE algorithm that reduces the use of these costly operations. To this end, we propose HULK, which performs two key steps: (1) it constructs bulk bitwise operations using low-cost homomorphic additions, which compute the Hamming weight of the encrypted operand bits in every slot of a packed ciphertext without any homomorphic multiplication, and (2) it decodes the result of an AND, OR, or XOR from the Hamming weight with a single indicator polynomial, keeping the result in the standard encoding. Across 13 end-to-end applications in healthcare, graph, and database analytics, HULK improves performance over the arithmetic approach used by prior works by up to 7.26x (CPU) and 6.65x (GPU), and on average by 2.32x/1.78x/1.45x (CPU) and 2.08x/1.70x/1.51x (GPU) for healthcare/graph/database analytics. When we increase the reduction depth in a representative application, HULK's speedup grows to 10.10x over the state-of-the-art GPU baseline.

---


### 737. [Resource-Efficient 3D Shape and Orientation Estimation of Road Users using Roadside RGB Camera and 3D Radar](https://arxiv.org/abs/2610.18417)

**<font color=#1a73e8>作者：</font>** Shiva Agrawal, Savankumar Bhanderi, Gordon Elger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end deep learning pipelines for camera-radar 3D object detection are well established in driver assistance systems and autonomous vehicles; however, adapting them to roadside-mounted infrastructure presents significant challenges. On vehicles, sensor heights, pitch angles, and relative geometries remain largely uniform, allowing end-to-end models to generalize effectively. On the contrary, roadside sensor installations vary drastically in height, tilt, and field of view across locations, rendering end-to-end models prone to failure and difficult to adapt without massive location-specific datasets. Hence, instead of designing a complex end-to-end pipeline for direct 3D bounding box estimation, a low-cost, resource-efficient two-stage approach is proposed for real-time 3D shape and orientation estimation. The first stage utilizes any off-the-shelf, state-of-the-art method to extract 2D camera bounding boxes and associated 3D radar points for each road user. The proposed second stage then processes these inputs to construct 3D oriented bounding boxes where radar data determines 3D position, predefined templates define size for each road user, and a tiny neural network predicts a site-specific and optimized yaw angle. The algorithm is successfully validated at a curved road with a junction for pedestrians, bicycles, and cars, where it achieves 25 frames per second on an NVIDIA Jetson ORIN for real-time applications.

---


### 738. [The Singularity Has a Distribution: Exact Timing Laws and Detection Limits for a Stochastic Intelligence Explosion](https://arxiv.org/abs/2610.18445)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Zheng Gao, Chiwun Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating AI research creates a positive feedback loop between software capability and research effort. We study a stochastic realisation of this loop in which independent, positive, multiplicative improvements arrive at a rate proportional to a power of current capability. Within this model, randomness leaves the deterministic explosion threshold unchanged but replaces the blow-up date by an explicit distribution. For equal-sized improvements the explosion time is a geometrically weighted sum of independent exponentials; its $q$-series representation gives its transforms, moments and tail behaviour, including a two-term small-time asymptotic. For Lomax-distributed improvement sizes the explosion time is exactly Gamma distributed. Self-similarity implies that, with parameters known, the relative uncertainty about the remaining time does not vanish as explosion approaches. We formulate a fixed-sample test between constant and geometrically increasing idea-arrival rates. If the baseline rate and the alternative log-rate increment $\ell$ are known, the minimum sample size at error level $\alpha$ is asymptotic to $(12z_\alpha^2)^{1/3}\ell^{-2/3}$, where $z_\alpha$ is the upper-$\alpha$ standard normal quantile. Uncertainty about the growth exponent near its critical value produces a $1/t$ tail with an explicit constant, and hence an infinite conditional mean waiting time, although explosion is certain given a positive exponent. Separate extensions show that a fixed deployment delay prevents explosion in the specified delayed-feedback models, that power-law diversion of effort shifts the growth threshold, and that in a deterministic oversight race a fixed allocation share does not change the asymptotic regime, except at a critical equality of exponents. Numerical illustrations, which are not empirical forecasts, show how timing and detectability depend on the granularity of improvements.

---


### 739. [CoTL: Compact Token Learning for 3D Scene Representation](https://arxiv.org/abs/2610.18446)

**<font color=#1a73e8>作者：</font>** Han Liang, Sibo Wu, Anpei Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present CoTL, a framework that learns a compact set of tokens that preserves scene geometry and appearance from unposed multi-view images. Our encoder compresses the input images into small per-view sets of latent tokens that aggregate information across views to form a view-consistent scene representation. Each additional view expands the representation with only a small, resolution-independent set of tokens, allowing its capacity to grow with the available observations. To force this compact bottleneck to retain sufficient scene information, a query-based Gaussian decoder uses scene-independent queries to attend to the learned tokens and recover an explicit, renderable set of 3D Gaussian primitives. Novel-view rendering supervision trains the compact representation end to end through the reconstructed Gaussian scene. Experiments on \retenk{} and ACID show that the resulting compact, unstructured token set supports competitive novel-view synthesis and can serve as the latent space of a generative model for 3D Gaussian scene generation. Together, these results show that 3D Gaussian reconstruction is an effective objective for compact scene representation learning and the learned token space provides a basis for broader downstream tasks in 3D vision.

---


### 740. [Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence](https://arxiv.org/abs/2610.18447)

**<font color=#1a73e8>作者：</font>** Thinker Team Ubtech, Peng Gao, Jichao Jiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support. In particular, visual dynamics, geometric structure, and executable action are commonly coupled through separate interfaces or downstream modules rather than being jointly represented and evolved within a shared dynamics model. In this work, we present Thinker-WM, a unified multimodal world model that jointly models and generates RGB, metric depth, and robot action through a shared intermediate Unified Dynamics Transformer with modality-specific encoders and decoders. The model performs multimodal unification at the representation level: appearance, geometry, and action are transformed into a common dynamic representation and jointly evolved by shared parameters, while their distinct output structures are preserved. The same parameterization supports multiple functions, including joint video-action generation, world prediction, policy inference, action-conditioned generation, video-to-action generation, and inverse dynamics. To examine whether the shared representation captures action-related information, we introduce a lightweight motion probe that shows the frozen visual representation contains recoverable motion information. Thinker-WM is trained on a heterogeneous corpus comprising approximately 20K hours of egocentric video, 10K hours of real-robot data, and 1K hours of simulation data, including approximately 4K hours of real-robot data with aligned depth supervision. Extensive experiments demonstrate strong performance across embodied world-model evaluations. Thinker-WM ranks first on EWMBench, WorldOlympiad and WorldArena, while controlled studies further demonstrate the benefits of action conditioning, geometric interaction, and multi-function training within the shared representation.

---


### 741. [Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2610.18449)

**<font color=#1a73e8>作者：</font>** Yibo Wen, Han Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents for autonomous scientific discovery must decide which experiments to run under a limited budget. Most benchmarks for science agents provide fixed datasets, while others that support active experimentation largely rely on simulation. We introduce Autonomous Science Bench, an initial release comprising six budgeted design-build-test-learn campaigns grounded in published experiments across biology, chemistry, and materials science. Agents select batches of designs, receive measurements from a lab service, and use the results to guide subsequent experiments before delivering a predictive model. Success requires passing two calibrated gates: a discovery gate, which evaluates the designs the agent measured, and a learning gate, which evaluates its model's ranking of held-out designs. In a pilot evaluation of eight agent-model configurations and 144 trials, the best configuration succeeds in 67% of trials, while the hardest campaign is solved in only three of 24 attempts. The two gates reveal different weaknesses: some agents build accurate rankings but find too few promising designs, while others find promising designs but fail to predict which unseen designs will perform well. These differences are obscured by overall success rates alone. We release version 0.1 of the campaigns, lab runtime, and public leaderboard at this https URL.

---


### 742. [Learning Perturbation-Specific Representations through Conditional Energy Prior for Cellular Response Prediction](https://arxiv.org/abs/2610.18456)

**<font color=#1a73e8>作者：</font>** Yuchen Yan, Yatao Bian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-based cellular perturbation prediction is essential to accelerate drug discovery and therapeutic identification. However, perturbation-specific signals are generally obscured by cellular complexity, making it difficult for existing methods to correctly capture perturbation effects. To address this problem, we propose PerturbEnergy, which introduces a conditional energy-based prior over perturbation representations. It assigns lower energy (higher probability) to representations compatible with the given perturbation and higher energy to others, thereby explicitly tilting the latent space toward perturbation-preferred regions. Besides, PerturbEnergy can be integrated into autoencoder architectures as we find its Evidence Lower Bound (ELBO) is equivalent to the ELBO of the complete autoencoder. We further prove that optimizing PerturbEnergy increases the lower bound on the conditional mutual information between representation and perturbation. Extensive experiments on four benchmark datasets demonstrate the effectiveness of our PerturbEnergy: it improves perturbation recognition especially in latent space with improvement of up to 83.2\%; It also achieves state-of-the-art performance for predicting top-50/100/200 differentially expressed gene(DEG) response and remaining competitive on highly variable gene(HVG) prediction. The code is provided: this https URL

---


### 743. [$\mathrm{S}^3$-PnP: Plug-and-Play Denoising for Scientific Imaging with Self-Supervised Score Priors](https://arxiv.org/abs/2610.18458)

**<font color=#1a73e8>作者：</font>** Yukun Cui, Jiangshe Zhang, Shuang Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image restoration methods increasingly rely on large-scale supervised training, yet clean targets are often prohibitively difficult to obtain in scientific imaging modalities such as hyperspectral imaging (HSI) and magnetic resonance imaging (MRI). Plug-and-play ADMM (PnP-ADMM) with pretrained diffusion priors offers a promising alternative, but the learned prior distribution can mismatch both the target scientific image distribution and the distribution of ADMM denoiser inputs induced by dual feedback. To mitigate these mismatches, we propose $\mathrm{S}^3$-PnP, a self-supervised plug-and-play restoration framework that learns a score prior directly from observation-derived ADMM intermediate states, without clean training targets or externally pretrained weights. Specifically, the learned score corrects the input to the analytical prior update, combining observation-driven corrections with analytical regularization. We further analyze the convergence and reconstruction error of the corrected ADMM algorithm assuming an ideal score and quadratic data fidelity. Experiments on reference-guided HSI restoration, single-image HSI denoising, and MRI denoising demonstrate consistent improvements over competing methods.

---


### 744. [MFVSR: A Multi-Style and Fine-Grained Benchmark for Video Subtitle Removal](https://arxiv.org/abs/2610.18461)

**<font color=#1a73e8>作者：</font>** Xiyan Huang, Qingdong He, Peng Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video subtitle removal (VSR) is an important video restoration task, yet existing evaluation remains limited by low-resolution datasets, fragmented test sets, and generic video-inpainting protocols that fail to adequately capture localized restoration errors, unintended modifications, temporal instability, and incomplete outputs. In this paper, we introduce MFVSR, a large-scale multi-style benchmark for fine-grained and reliability-aware video subtitle removal evaluation. MFVSR distinguishes itself through three key features: (1) Large-scale and diverse data, comprising 3,000 paired videos from Real-HQ, Real-LQ, and AI-Generated sources, with an auxiliary set of 953 in-the-wild real videos for real-world coverage analysis; (2) Controlled subtitle diversity, spanning 16 languages and four factors covering spatial layout, temporal behavior, visual style, and language mode; (3) Fine-grained evaluation, introducing an information-conditioned, spatially decoupled protocol that separates blind from mask-guided removal and measures Restoration Fidelity, Preservation Fidelity, Temporal Fidelity, coverage, and failures. Experiments on six representative methods reveal substantial discrepancies between local restoration, outside-region preservation, temporal consistency, and full-set reliability that are obscured by conventional full-frame metrics. MFVSR therefore provides a more comprehensive and diagnostic foundation for evaluating and advancing video subtitle removal methods.

---


### 745. [Physics-Aware Deepfake Detection via Distance-Speech Consistency](https://arxiv.org/abs/2610.18485)

**<font color=#1a73e8>作者：</font>** Kyeongrae Kim, Kim Sung-Bin, Oh Hyun-Bin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in generative models has made talking-head deepfakes highly realistic and easy to create, jeopardizing public trust. However, most audio-visual deepfake detectors rely on lip-speech synchronization and are designed for static, frontal videos, limiting their reliability in dynamic, in-the-wild recordings where the speaker moves and lip cues are degraded or missing. As an alternative, we propose a physics-aware detector for dynamic speaking videos that leverages an acoustic constraint: in real recordings, speech energy varies predictably with speaker-to-camera distance, whereas deepfake generation can break this coupling. Our method combines distance estimates from video with distance-dependent acoustic measures from speech to detect deepfakes. Experiments on in-the-wild benchmarks show that the proposed physical cue is effective in dynamic scenarios, and that it complements lip-sync-based detectors, with a simple ensemble achieving consistent gains across datasets. Codes are available at this https URL.

---


### 746. [SoK: Rethinking Membership Inference in Tabular Machine Learning](https://arxiv.org/abs/2610.18486)

**<font color=#1a73e8>作者：</font>** Cristina Pêra, Tânia Carvalho, Maxime Cordy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Membership Inference Attacks (MIAs) are currently the dominant approach to evaluating privacy in machine learning applications. Despite their significance, several concerns remain unexplored, particularly with regard to tabular data. Existing evaluations focus predominantly on high-dimensional datasets, leaving the privacy behavior of small-to-medium datasets unexplored. In this paper, we present a new taxonomy for MIAs and conduct a comprehensive study of the factors influencing vulnerability. We evaluate four distinct state-of-the-art attacks across diverse tabular datasets and model architectures. Our results show that datasets with higher class granularity and majority class percentage are more susceptible to MIAs. We further demonstrate that advanced MIAs are highly dependent on adversarial knowledge of the target model, while reference model-free attacks often achieve statistically comparable results. Most importantly, we show that records with unique signatures (single-outs) remain highly vulnerable, even when common defenses are applied. These findings indicate that current defenses reduce average leakage, but fail to adequately protect the most sensitive individuals.

---


### 747. [Recalibrating Many Questions with Few Labels: Minimax Rates and Identification Limits](https://arxiv.org/abs/2610.18488)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Chiwun Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many related prediction problems, which we call questions, come with few labels each. What information can be shared across them, and what is actually necessary for good decisions? We answer both for recalibration, motivated by decision models such as Jev (TypeSafe AI, 2026) that return a probability for any yes/no question a developer writes. A predictor reports a probability $P$ with output law $\mu$ on $m$ questions, each with $n$ labels and a nondecreasing map $g_j(p)=\mathbb{P}(Y=1\mid P=p)$; the compound risk is the excess Brier score over the true maps, averaged over questions. Over maps within sup-distance $\tau\le 1$ and total variation $V\le 2$ of one nondecreasing shape (fixed effects), the minimax compound risk is $(mn)^{-2/3}+\min\{\tau^2,1/n\}+\min\{\tau^2,V^2,(V/n)^{2/3}\}$ up to universal constants, for every non-atomic $\mu$. A pooled isotonic fit with a per-question correction sized once, on held-out labels of all questions, attains it without knowing $\tau$, $V$ or $\mu$ ($n\ge 2$, $m\ge 3$); tuning each question on its own labels loses a factor of order $\min\{n,\log(m^2/n)\}$ when the maps differ by constants and $m^2/n$ is large. When the maps are drawn from an unknown prior (random effects), other questions need not identify the Bayes rule. The loss, the identification regret, is at most $2^{-n}$ once the law of a question's data is known, extending a bound of Skibinsky (1968) for coins, and in the worst case at least $\beta_\star^{-n}/(72\sqrt{n})$ at every finite $m$, where $\beta_\star\approx 3.583$. Beyond a few labels per question, what cannot be learned is nearly unnecessary. For constant maps (an uninformative predictor) and constant-map priors, the exponential base is exactly $\beta_\star$, not the 4 suggested by the moment range; for monotone maps it lies in $[2,\beta_\star]$.

---


### 748. [Approximating Optimal Policies in Heterogeneous Asynchronous Multi-player Bandits](https://arxiv.org/abs/2610.18514)

**<font color=#1a73e8>作者：</font>** Sacha Arroues-Paykin, Etienne Boursier, Vianney Perchet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by applications to cognitive radio networks, multi-player multi-armed bandits (MMAB) have attracted considerable attention in recent years. The asynchronous variant, in which players are active only at a fraction of timesteps, better reflects real-world decentralized networks, where devices are not permanently active. Despite its practical relevance, this setting remains relatively understudied. Existing work on asynchronous MMAB has focused on homogeneous players, who share the same activation probability, a setting in which the optimal centralized allocation can be easily characterized. In contrast, efficiently computing the optimal allocation in the heterogeneous setting, where players have different activation probabilities, has remained an open problem. In this work, we investigate this problem and first establish its NP-hardness. We then turn to the greedy algorithm, which runs in polynomial time, and prove that it achieves a $\frac{1}{e}$-approximation of the optimal allocation. Furthermore, when players are processed in decreasing order of their activation probabilities, the approximation guarantee improves to $\frac{1}{\sqrt{e}}$. Overall, our results establish the greedy algorithm as an efficient approximation to the optimal allocation, providing a practical oracle baseline for the design of online algorithms for heterogeneous asynchronous multi-player bandits.

---


### 749. [Imprinting: Knowledge Distillation Can Shift Student Behavior](https://arxiv.org/abs/2610.18517)

**<font color=#1a73e8>作者：</font>** Yu-Chien Tang, An-Zi Yen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation trains student models on teacher-generated responses to transfer task capability, but those responses may also carry behavioral tendencies of their source. We investigate whether the source teacher can shape student behavior beyond the capability that distillation is intended to transfer. We construct harm-accepting and harm-avoiding variants of the same base teacher, use them to generate responses to ordinary reasoning and knowledge questions unrelated to safety, and distill those responses into students with different base models. Students generally acquire task capability while their downstream decisions shift toward the source teacher's safety-pragmatism disposition, a phenomenon we call imprinting. Distillation from the harm-accepting teacher reduces harm avoidance, whereas distillation from the harm-avoiding teacher increases it. Imprinting varies across teacher-student pairs and does not extend uniformly across different forms of safety behavior. Excluding a sparse set of divergence tokens reduces imprinting, whereas response rewriting preserves the source-dependent effect and can introduce additional rewriter-dependent shifts. Post-distillation preference optimization raises harm avoidance but does not eliminate the source-dependent difference. These results show that behavioral tendencies can be intentionally imprinted through the source teacher, even with ordinary task supervision.

---


### 750. [Dual-Domain Sparse-View 4D CBCT Reconstruction with Spatial-Temporal Consistency Learning](https://arxiv.org/abs/2610.18518)

**<font color=#1a73e8>作者：</font>** Qi Lai, YuTong He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Four-dimensional cone-beam computed tomography (4D CBCT) provides phase-resolved volumetric images for image-guided radiotherapy. Yet good reconstruction quality usually needs many projections. This increases scan time and radiation dose. We propose STCNet, a sparse-view 4D CBCT reconstruction framework that uses spatial-temporal consistency learning. STCNet reconstructs high-quality images from only 16 projections in each respiratory phase. STCNet integrates physics-driven positional encoding to enforce geometric consistency in the projection domain and introduces temporal encoding in latent space to capture respiratory motion dynamics across phases to capture dynamic respiratory motion across phases. A dual-domain collaborative strategy jointly optimizes both projection and image domains, enhancing structural fidelity and temporal coherence. We tested STCNet on the TCIA-LUNG dataset and a CIRS thorax phantom dataset. STCNet performed better than conventional methods and recent deep learning baselines in image quality, artifact reduction, and structural preservation. On TCIA-LUNG, STCNet reached PSNR values of 33.311, 32.695, and 32.658 dB at phases 2, 5, and 8. The corresponding SSIM values were 0.845, 0.823, and 0.825. On CIRS, STCNet achieved PSNR values up to 36.497 dB and SSIM values up to 0.877. These results support STCNet as a promising framework for low-dose, phase-resolved 4D CBCT reconstruction in image-guided radiotherapy.

---


> [!TIP]
> 当前位于：**701-750**（第 15/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | **701-750** | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
