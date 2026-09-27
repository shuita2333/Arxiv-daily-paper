# 📦 其他研究 | 2026年09月28日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 101. [IronViT: Toward Efficient Generalist Visual Representation Learning](https://arxiv.org/abs/2609.29252)

**<font color=#1a73e8>作者：</font>** Jiaxi Huang, Yueqi Hu, Xin Zhu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A generalist vision encoder must capture semantic, spatial, language-aligned, and action-relevant cues within a unified representation, yet softmax attention underlying today's most capable visual backbones becomes prohibitively expensive at high resolution. A natural attempt to address both challenges is to distill multiple specialist teachers directly into an efficient architecture. We find that directly coupling these objectives degrades representation quality, as the student must simultaneously reconcile heterogeneous capabilities and adapt them to a different token-mixing architecture. We introduce IronViT, built on a simple principle: consolidate capabilities before constraining computation. IronViT first distills complementary specialists into a softmax attention capability bridge, then progressively transfers the consolidated representation to a hybrid softmax-linear attention encoder. A purpose-built data pipeline further curates the distillation corpus for higher information density and broader domain coverage. Across recognition, retrieval, dense prediction, multimodal understanding, and robotic learning, IronViT is competitive with leading specialist and generalist vision encoders. The softmax bridge achieves the strongest aggregate performance in multimodal understanding and robotic learning among the evaluated backbones, while the hybrid encoder retains broad transfer performance with an efficiency advantage that grows with input resolution. Together, these results show that consolidating capabilities before architectural conversion can yield a generalist visual encoder without inheriting the prohibitive high-resolution cost of conventional softmax attention.

---


### 102. [Deep learning of longitudinal visual fields predicts glaucoma progression rate and identifies fast progressors](https://arxiv.org/abs/2609.29256)

**<font color=#1a73e8>作者：</font>** Taiabur Rahman, Siddiqur Rahman, Muhammad Moniruzzaman 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glaucoma is the leading cause of irreversible blindness, and timely identification of fast progressors is essential to prevent disability. Current practice estimates progression by ordinary least-squares regression of mean deviation (MD) on time, requiring 6--10 visual field (VF) tests over several years to obtain a reliable slope. We present GLAM (Glaucoma Longitudinal Analysis Model), a deep learning framework that ingests longitudinal Humphrey 24-2 total deviation sequences with five clinical features and predicts MD and visual field index progression rates using attention-based fusion and aleatoric uncertainty. On the open-access University of Washington Humphrey Visual Field dataset (4,276 patient-eyes), GLAM achieved an MD-rate mean absolute error of 0.139 dB yr$^{-1}$ ($R^2 = 0.927$; 73.5% reduction over a ridge baseline) and an AUC of 0.990 for fast-progressor detection. VF-only deep learning can match multimodal pipelines for progression prognostication using routinely collected perimetry alone.

---


### 103. [TP-CRIV: A Framework for Third-Party Challenge-Response Identity Verification of AI Models](https://arxiv.org/abs/2609.29264)

**<font color=#1a73e8>作者：</font>** Teruki Sano, Minoru Kuribayashi, Masao Sakai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) models are increasingly deployed through remote services, making model misappropriation a growing concern. Existing approaches, including watermarking, fingerprinting, and model similarity analysis, primarily rely on predefined evidence or direct behavioral comparison and do not explicitly evaluate whether the claimant currently possesses and can utilize model-dependent information relevant to the claimed model identity.
In this paper, we propose Third-Party Challenge-Response Identity Verification (TP-CRIV) for AI models. TP-CRIV targets a third-party verification setting in which the verifier has neither white-box nor API access to the claimant's model, can interact with the suspicious deployed service only through its ordinary black-box inference interface, and does not require protocol-specific cooperation from the service provider. Under these constraints, the framework enables the verifier to obtain empirical evidence as to whether the claimant locally possesses a model satisfying a predeclared identity relative to the deployed model. Verification is conducted under fresh, previously undisclosed requirements and network isolation, so that the demonstrated capability cannot rely on online external assistance after challenge disclosure. The resulting evidence is interpreted relative to independently specified and calibrated matching and non-matching operating situations and is statistical rather than cryptographic. We instantiate TP-CRIV for CNN image classifiers using probability-control-based witness generation. Experiments on ten ImageNet-pretrained TorchVision models demonstrate clear same/cross-model separation and finite-challenge verification using independently calibrated thresholds.

---


### 104. [Baszta: Data-Centric Fine-Tuning of a Polish Multi-Label Safety Classifier](https://arxiv.org/abs/2609.29266)

**<font color=#1a73e8>作者：</font>** Adam Górski, Mateusz Jąkalak, Rafał Jakubowski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We develop a multi-label Polish content-safety classifier by fine-tuning allegro/herbert-base-cased (124M) across five categories (hate, vulgarity, sexual content, crime, self-harm) using a Focal + R-Drop objective, and evaluate the resulting model against Bielik Guard (Sójka) on the shared out-of-distribution Gadzi Język benchmark. Both systems are given per-category threshold tuning on the same calibration split. Under that matched protocol our model holds a small but statistically significant lead in micro F1, while an apparent macro-F1 lead does not survive: it was an artifact of comparing a tuned model against an untuned one. We also report what that micro figure is worth. Because Gadzi Język is 97% crime-positive, a classifier that flags crime on every input and nothing else already scores 0.910 micro F1 on the same test split, so micro separates neither system from a degenerate strategy and macro is the column that does. Per-category and per-protocol figures are reported in Section 4.
The residual out-of-distribution gap is one of calibration rather than discrimination. Ranking quality stays high while positive probabilities collapse, and per-category temperature scaling recovers the loss where Platt scaling and isotonic regression do not. That recovery turns out to be conditional on the calibration set containing safe text. Gadzi Język contains almost none, so thresholds fitted on it flag crime on every safe input, and a balanced refit buys a deployable operating point at the cost of adversarial recall. We report both operating points rather than only the flattering one.
Two changes that are standard practice, per-class cost-sensitive weighting and mean pooling, each raise in-distribution macro F1 while lowering the out-of-distribution figure, which indicates that robustness has to be selected for directly rather than inherited from in-distribution accuracy.

---


### 105. [BridgeMem: Causal Dyadic Transition Residuals for Temporal Knowledge Graph Forecasting](https://arxiv.org/abs/2609.29268)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Libing Chen, Shengda Zhuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal knowledge graph forecasting aims to infer future relational facts from the temporal structure of observed events. Existing forecasters mainly summarize history through entity states, relation states, paths, or exact recurrence. These views often miss pair-specific transition evidence, that is, the way prior relations between the query actor and a candidate change the odds of the target relation. We introduce BridgeMem, which estimates this quantity as a residual added to the log scores of a frozen full-vocabulary forecaster. For each candidate, BridgeMem retrieves the pair's events that strictly precede t, encodes their relations, directions, and lags, and converts them into a likelihood-ratio correction. A support-adaptive empirical-Bayes reader trusts exact transition counts where they are abundant and backs off to a learned attention estimator where they are sparse. The backbone's own uncertainty gates the correction, so confident queries and candidates without dyadic history are left unchanged. On five benchmarks, BridgeMem improves on the strongest of nine baselines from 2021--2026 in all 20 filtered MRR and Hits@{1,3,10} comparisons, with MRR gains of 0.0213, 0.0164, 0.0216, 0.0112, and 0.0028 over the best prior result. These results show the value of explicit dyadic transition modeling.

---


### 106. [ALOE: Semantically Addressed Low-Rank Operators for Knowledge Editing](https://arxiv.org/abs/2609.29269)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Hu Xu, Jianfeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge editing changes what a model knows by modifying parameters so that a requested fact updates while unrelated behavior is preserved. This is usually treated as a write problem, but editing also involves an address problem: deciding which hidden states should receive the new residual. An update that activates too narrowly memorizes one prompt, while one that activates too broadly disrupts neighboring knowledge. Parametric editors encode this scope implicitly, whereas memory-based editors make the selection explicit but keep it outside the edited model. We propose ALOE (Addressed Low-rank Operator for Editing), which learns semantic addresses from paraphrases and hard same-subject negatives, aligns them with autoregressive hidden states through rollout refinement and gate calibration, and embeds the resulting gated low-rank operator within one MLP layer, so that the deployed model runs in a single forward pass with no external retriever or auxiliary router. Evaluated on CounterFact, ZSRE, and KnowEdit across three 7--8B model families, ALOE achieves efficacy between 0.955 and 0.999 and locality between 0.981 and 1.000; mechanistic analyses confirm that the learned geometry separates competing edits and that calibration suppresses out-of-scope activation. The remaining errors concentrate in paraphrase coverage and write fitting.

---


### 107. [Learnable Time-Frequency Masks for Explaining Time-Series Classifiers](https://arxiv.org/abs/2609.29270)

**<font color=#1a73e8>作者：</font>** Theresa Dahl Frehr, Francisco Pelayo, Lukas Raad 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series explainability remains challenging because discriminative information is often encoded in latent frequency or time-frequency features rather than in the raw signal itself. Existing attribution methods typically operate either in the time domain or in a fixed transform domain, limiting their ability to capture salient information across different representations. We propose XACT, a general framework that learns sparse attribution masks over coefficients from arbitrary invertible time-frequency transforms. We evaluate the framework on the STFT, the continuous wavelet transform, and the discrete wavelet transform. In addition, we extend the virtual inspection layer approach from the STFT to both wavelet transforms, enabling LRP to generate explanations in these representations. On a synthetic dataset, XACT produces precise explanations and is less prone to highlighting spurious features than the tested baselines. Across two real-world datasets, XACT produces sparse and structured explanations, although no method performs best across all quantitative evaluation criteria. These results demonstrate that learning explanations directly in time-frequency representations offers a flexible approach to interpreting deep-learning models for time series data.

---


### 108. [Online Task Adaptation via Self-Organisation](https://arxiv.org/abs/2609.29281)

**<font color=#1a73e8>作者：</font>** Krsto Proroković  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are typically adapted by computing gradients and updating model parameters. We investigate whether task-specific adaptation can instead emerge from a meta-learned self-organising process that requires no gradients at adaptation time. We instantiate this idea with a Neural Cellular Automaton in which locally interacting recurrent cells maintain both a recurrent state and a fast associative memory. During meta-training, backpropagation is used to learn the recurrent dynamics together with how the memory is read and written. Once training is complete, the slow model parameters remain fixed, and online adaptation occurs only through cellwise memory updates driven by local prediction errors and a delta rule.
We evaluate whether the learned mechanism can adapt to semantically distinct held-out classification tasks. A single pass over the support data produces substantial improvements in held-out performance without gradient computation or parameter updates during adaptation, and the mechanism remains effective across large changes in the number of examples processed jointly. These results show that task-specific adaptation can be achieved through explicit fast-memory updates while keeping the slow model parameters fixed.

---


### 109. [PHOSA: Photorealistic 3D Sign Avatar Modeling and Benchmark](https://arxiv.org/abs/2609.29292)

**<font color=#1a73e8>作者：</font>** Haodong Wang, Hezhen Hu, Wengang Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we focus on photorealistic sign avatar modeling, which is crucial for effective communication with the Deaf community and is characterized by complex hand gestures and nuanced facial expressions. To this end, we introduce MVSign, the first multi-view Chinese sign language dataset co-designed with Deaf experts, featuring diverse gestures and rich annotations. For precise SMPL-X annotation, we develop a hybrid fitting pipeline that produces accurate body, hand, and facial parameters and can also be applied to the monocular setting. Building on MVSign, we propose a decoupled sign avatar representation that isolates body, head, and hand components to capture complex articulations, together with a motion-aware sampling strategy to handle motion blur and balance gesture diversity. Extensive experiments demonstrate that our method achieves high-fidelity visual results on MVSign, particularly in detailed hand and facial regions, and generalizes well to in-the-wild monocular sign language videos. Project page: this https URL.

---


### 110. [Beyond Feature Reliability: Repeat-Informed Multifractal Curve Regression for Brain-Age Prediction](https://arxiv.org/abs/2609.29307)

**<font color=#1a73e8>作者：</font>** Yu Chang, Anzhe Cheng, Jiahao Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain-age prediction from resting-state fMRI provides a quantitative framework for characterizing age-related changes in spontaneous brain dynamics and for identifying functional signatures. Existing studies have linked fractal and multifractal scaling to age and examined the reliability of individual features. However, prediction repeatability depends on how features fluctuate jointly and how a predictor combines them, which feature-wise reliability assessments do not capture.
To address this problem, we propose Repeat-informed Multifractal Curve Regression (RMCR), a structured framework for learning stable age-predictive patterns from multifractal curves. By jointly modeling curve structure and repeat-scan variability, RMCR learns predictive combinations of fluctuation orders that target both accuracy and within-subject consistency.
Relative to a matched run-level ridge baseline, RMCR reduces single-run MAE by 6.1% on HCP-A and 7.9% on an external Cam-CAN cohort, and within-visit repeat absolute difference by 18.5% on HCP-A, using a single scan at inference.

---


### 111. [Beyond Centralized Policy Decision Points: Decentralized Sticky Policy Authorization through Evidence Quorums](https://arxiv.org/abs/2609.29308)

**<font color=#1a73e8>作者：</font>** Aleena Nazir, Mubashir Husain Rehmani, Bernard Butler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sticky policies remain attached to protected data so that access restrictions can persist across systems, yet request-time authorization often still depends on a centralized Trusted Authority or Policy Decision Point (PDP). This paper presents SPEAR-Q, a decentralized framework in which independent Policy Authority Nodes (PANs) evaluate the active sticky policy using local context, consent, and risk information and generate signed authorization evidence. A strict-majority Evidence quorum determines the global Permit or Deny decision, while a committed policy becomes active only after the required PAN majority applies it. SPEAR-Q was deployed across physically separated hosts in the Airbus Cyber Security Simulation Platform and evaluated using a healthcare workload derived from MIMIC-IV. Across 9,000 performance requests, all requests completed without execution failure or timeout. Latency increased and throughput saturated as cluster size and concurrency grew, with PAN evidence waiting and PAN-local processing dominating under load and credential validation forming the main PAN-side cost. Policy-activation experiments confirmed majority-based activation. Quorum experiments showed that correctly signed false-Permit evidence from fewer compromised PANs than the required quorum could not produce a global Permit or resource release, while authorization remained fail-closed when reachable PANs fell below the required quorum. Compared with prior approaches that decentralize policy management, credential authority, or threshold-based release separately, SPEAR-Q integrates persistent sticky policy enforcement, independent request-time evidence, majority-based policy activation, and explicit quorum-bounded authorization within one decentralized framework. Under the evaluated conditions, SPEAR-Q supports decentralized sticky-policy authorization without relying on a centralized decision authority.

---


### 112. [DocuTeam: Mixed-Initiative Multi-Agent Discussions around Evolving Documents](https://arxiv.org/abs/2609.29309)

**<font color=#1a73e8>作者：</font>** Heechan Lee, Juhyeon Choi, Tae Soo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In open-ended problem solving, collaborators often rely on discussion to surface concerns, challenge perspectives, and refine shared work as it evolves. While AI agents are increasingly used as discussion partners, existing multi-agent systems place a heavy burden on users to initiate and carefully orchestrate the discussions. We present DocuTeam, a mixed-initiative multi-agent discussion system in which both users and agents can initiate and steer conversations. Agents monitor document changes to proactively start and redirect discussions as the work evolves, while users can flexibly shape the conversation or adopt agent ideas. In a within-subjects study (N=20), participants using DocuTeam produced outcomes rated significantly more novel, relevant, and specific than with a baseline without any increase in cognitive load. Rather than using agents for one-off idea sourcing, participants engaged in an iterative refinement loop in which document changes prompted agent reactions, which led users to revisit and further develop their work.

---


### 113. [When No One Owns the Judgment: Accountability Under Contribution Dissolution in Human-AI Collaboration](https://arxiv.org/abs/2609.29312)

**<font color=#1a73e8>作者：</font>** Hengzhi Ye  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Communities often respond to potentially AI-assisted work by asking three questions: Was AI used? Was that use disclosed? Can hidden use be detected? These questions place AI use itself at the center of accountability while overlooking a deeper problem: unowned judgment. Evaluations, claims, decisions, and creative directions can be shaped by AI with no accountable human or institution prepared to stand behind them. We develop this argument through two illustrative cases: AI-assisted peer review and concealed AI use in creative work. The first shows how contribution dissolution can weaken responsibility while the second shows how the fear of losing credit can discourage honest disclosure. The cases expose the limits of disclosure rules and provenance records as responses to AI-mediated collaboration. We offer three directions for discussion: distinguishing the roles AI plays, identifying judgments that require clear human ownership, and creating conditions in which AI involvement can be disclosed without default penalty. The broader aim is to make AI-shaped contributions discussable, creditable, contestable, and repairable.

---


### 114. [Neuralized Multi-Wavelet Decomposition for Time Series Classification and Forecasting](https://arxiv.org/abs/2609.29317)

**<font color=#1a73e8>作者：</font>** Xiaohan Jiang, Jingyuan Wang, Jiahao Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series analysis is fundamental in domains such as finance, healthcare, and meteorology. Real-world time series often exhibit multiscale characteristics shaped by diverse latent factors, resulting in intricate temporal patterns and rich frequency structures. However, existing approaches typically focus on either frequency-domain decomposition or time-domain pattern extraction in isolation, neglecting their joint structure. This decoupled modeling limits representation expressiveness and undermines performance in tasks requiring simultaneous temporal and spectral reasoning. To address this gap, we propose m-WCN, a novel end-to-end deep learning framework that neuralizes multi-wavelet decomposition for joint extraction of temporal patterns and frequency components. By approximating the classical GHM multi-wavelet transform with trainable convolutional operators and enforcing orthogonality constraints, m-WCN produces interpretable multi-resolution representations. Built on this foundation, we introduce two task-specific architectures: TFBC for time series classification, which boosts discriminative features across frequency scales, and FTB for forecasting, which ensembles frequency-aware predictors. Extensive experiments on 64 UCR datasets and seven public forecasting benchmarks demonstrate the effectiveness of our approach. Built on the neuralized m-WCN, our TFBC and FTB outperform various baseline models across diverse datasets, achieving average improvements of 19.97% in classification and 19.92% in forecasting tasks.

---


### 115. [TinyCardioUNet: IMU-to-ECG Translation with Graph-Encoded Inter-Axis Dependencies and Tensor Decomposition-Based Parameter Reduction](https://arxiv.org/abs/2609.29322)

**<font color=#1a73e8>作者：</font>** Seungwoo Han, Ingon Chanpornpakdi, Motoi Noda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating electrocardiography (ECG) from a chest-worn inertial measurement unit (IMU) enables continuous heart rate (HR) monitoring without the discomfort of electrodes. We propose TinyCardioUNet, a lightweight UNet that uses all six IMU axes without prior channel selection, refines its bottleneck with a graph neural network that encodes inter-axis dependencies, and employs tensor decomposition with automatic variational Bayesian rank selection for parameter reduction. On a public dataset, TinyCardioUNet achieves an RMSE of $0.098$ and a Pearson correlation coefficient of $0.677$ with only $36.0$k parameters and remains comparatively robust to additive noise, demonstrating accurate ECG reconstruction with a compact model.

---


### 116. [Hyperbolic Multimodal Continual Learning: A Closest-Admissible Solution](https://arxiv.org/abs/2609.29329)

**<font color=#1a73e8>作者：</font>** Jiahong Liu, Ming Shen, Xiaohao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing continual-learning methods protect parameters, replayed examples, or Euclidean feature subspaces. When applied to hyperbolic multimodal models, they do not explicitly preserve the Lorentz geometry that jointly encodes within-modality similarity, cross-modal correspondence, and semantic hierarchy; sequential updates can therefore retain task scores while still distorting previously learned relations. We address this gap with Hyperbolic Multimodal Continual Learning (HMCL). We show that preserving the old multimodal geometry amounts to restricting all modalities to one shared hyperbolic isometry, which induces a family of admissible first-order parameter changes. We formulate a joint closest-admissible (CA) correction that retains the shared rotation best matching the candidate modal updates; its minimal-rotation (MR) special case fixes this rotation to zero. Both variants correct the displacement realized by AdamW, and task anchoring bounds within-task accumulation while preserving learning freedom. Across a unified 16-task classification-retrieval stream with three hyperbolic backbones, HMCL improves final performance and backward transfer over sequential fine-tuning and four continual-learning baselines; HMCL-CA gives the highest Overall score on every backbone. A modality-extended stream confirms the retrieval gains. Representation analyses find 81.2 to 95.5 percent less radial, angular, cross-modal, and paired-distance drift; ImageNet-WordNet results show better semantic ancestry and radial hierarchy.

---


### 117. [FlowAtom: Atom-Based Evidence Aggregation for Multi-Label Website Fingerprinting](https://arxiv.org/abs/2609.29330)

**<font color=#1a73e8>作者：</font>** Chongru Fan, Wentao Huang, Wei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying the set of monitored websites in mixed encrypted traffic is challenging because an individual flow often provides only partial evidence of website identity. To address this challenge, we propose FlowAtom, which constructs shared prototypes, called Atoms, from flow representations without website labels. Specifically, FlowAtom pretrains a flow encoder on external unlabeled traffic and aggregates Atom responses across flows within each observation window into a fixed-dimensional, permutation-invariant representation for monitored website-set prediction. Across Direct HTTPS, Trojan, and VMess, FlowAtom achieves micro-F1 scores of 97.82%, 94.43%, and 93.92% in closed-world evaluation, respectively, and consistently outperforms the evaluated baselines in open-world evaluation on windows containing monitored visits. The code is available at this https URL.

---


### 118. [A Study of the Limits of Collaborative DCT-Based Image Denoising via Interpretable Neural Networks](https://arxiv.org/abs/2609.29334)

**<font color=#1a73e8>作者：</font>** Cristian Comellas, Julia Navarro, Antoni Buades  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image denoising remains a fundamental problem in image restoration, with applications in photography, biomedical, and scientific imaging. Modern deep neural networks achieve strong performance by learning powerful image priors, but often rely on large black-box models with limited interpretability. In contrast, DCT-based sliding-window and collaborative filtering methods such as BM3D offer clear algorithmic structure, but depend on handcrafted and non-differentiable operations. This work studies how far such structured collaborative filtering principles can be pushed when reformulated as trainable models. We introduce DeepBM3D, a compact fully differentiable architecture that combines non-local patch grouping, DCT-domain filtering, and multi-stage refinement within a BM3D-inspired pipeline. Lightweight convolutional feature extractors guide patch grouping, while filtering is performed through learned Wiener weights in the DCT domain. Experiments show that DeepBM3D improves over classical and hybrid baselines, remains competitive with FFDNet at low and moderate noise levels, and performs particularly well on repetitive textures.

---


### 119. [SEE Challenge 2026: Event-Guided Brightness Adjustment Across a Broad Illumination Range](https://arxiv.org/abs/2609.29347)

**<font color=#1a73e8>作者：</font>** Yunfan Lu, Mingchao Xu, Hanyu Zhou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras provide a high dynamic range and preserve brightness-change cues in lighting conditions where conventional RGB frames may be noisy or saturated. To benchmark event-guided restoration across a broad illumination range, we organized the SEE Challenge 2026 with the Event-Based Multimodal Vision Workshop at ECCV 2026. The task conditions restoration on one or more RGB frames, synchronized events, and a scalar target-brightness statistic provided by the organizers. It uses SEE-600K, which contains 610,126 image-event observations from 202 real-world scenes spanning low-light, normal-light, and high-light conditions with illumination variations of up to 1,000$\times$. The challenge follows an open-system protocol: participants may use different temporal contexts, architectures, pretrained weights, test-time augmentation, and post-processing strategies. PSNR determines the ranking, and SSIM is reported as a secondary metric. Around 70 teams registered interest and 15 valid CodaBench submissions were received. Six distinct teams completed organizer-side identity and technical verification, provided method descriptions, checkpoints, inference code, and instructions, and are included in the verified open-system ranking reported here. Beyond the ranking, this report analyzes exposure subsets, semantically distinct test cases, a shared failure pattern, system design choices, and inference strategies. The top systems obtain closely spaced average scores, while the best-performing method varies across cases and metrics; under severe underexposure, all verified systems retain visible local errors.

---


### 120. [Learning a Flow to Self-Supervised Representations](https://arxiv.org/abs/2609.29350)

**<font color=#1a73e8>作者：</font>** Yuling Jiao, Wensen Ma, Houduo Qi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explicit geometric references offer a direct way to structure self-supervised representations. Existing adversarial distribution-matching formulations, however, require costly encoder-critic optimization. We introduce Flow-Based Distribution Matching (FBDM), a non-adversarial framework that learns this reference-directed geometry through spherical conditional velocity regression. An ETF-inspired reference allows its number of components K' to exceed the auxiliary flow dimension d* while retaining structured geometric separation. We assign both augmented views of each image to the same target, while limiting how many images each reference center can receive. An explicit alignment loss further pulls the two views' representations closer together. Experiments across benchmarks ranging from CIFAR to ImageNet show that FBDM achieves performance nearly on par with DM and remains competitive with existing SSL methods. Matched training-cost comparisons show a 1.48- to 1.83-fold speedup over DM with a negligible increase in GPU memory usage. We also provide a theoretical explanation for the usefulness of the learned representations: under stated conditions, we bound the downstream misclassification rate in terms of the FBDM pretraining loss.

---


### 121. [Beyond Simple Input-Output Assessment Tasks: Leveraging Automated Programming Assessment for Non-Trivial Courses](https://arxiv.org/abs/2609.29363)

**<font color=#1a73e8>作者：</font>** Artur Jordao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The public visibility of Artificial Intelligence (AI) is growing rapidly, driven by the positive impact of its applications across diverse fields of knowledge. In this new chapter, courses that cover the foundations of AI and machine learning become essential for understanding their role and potential in contemporary society. Therefore, understanding fundamental concepts and elementary algorithms through the close integration of theory with practice is essential in AI courses. In this essay, we report our experience designing machine learning exercises for automated assessment tools in programming. It is worth mentioning that we are not developing a novel form of automated grading system. Instead, we propose a perspective that frames machine learning problems as input-output assessment tasks. From this perspective, each exercise admits a unique and deterministic answer and enables automated programming assessment tools (e.g., VPL for Moodle, Codeforces, and MOJ) to effectively support AI education. We believe this essay can encourage instructors to foster educational innovation by adopting more dynamic and interactive approaches to AI courses that integrate theory and practice. Importantly, this essay does not introduce an innovation in the use of AI for education; rather, it introduces an innovative approach to improving the learning of AI, particularly, machine learning.

---


### 122. [Shadow Reduction in Ultrasound Imaging Using Differentiable Simulation and Radiance Field Decomposition](https://arxiv.org/abs/2609.29373)

**<font color=#1a73e8>作者：</font>** Valentin Bacher, Pak Hei Yeung, Bernhard Kainz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acoustic shadows from bone and other highly attenuating tissues obscure clinically important structures in ultrasound. In fetal brain imaging, skull-induced artefacts disproportionately degrade the hemisphere closer to the transducer (proximal), limiting symmetric assessment of the two hemispheres. Existing correction methods require raw scanner data, impose restrictive assumptions on tissue properties, or rely on generative models that may hallucinate anatomy. We present RFlash, a physics-informed post-processing method that decomposes beamformed ultrasound images into explicit attenuation and scatter-intensity maps using a differentiable radiance-field formulation of image formation. Attenuation-adaptive re-rendering then removes the dependence of the signal at each depth on the intervening tissue, equivalent to virtually advancing the transducer into the tissue. Across 1,261 3D fetal brain volumes, 143 real 2D curvilinear abdominal scans, and 1,200 simulated 2D linear-probe liver scans, RFlash reduces shadow-related intensity differences more effectively than classical Hughes-Duck attenuation correction. For a gestational-age model trained on the distal hemisphere (further from the transducer) and applied to the proximal hemisphere, prediction error decreases by 5.1 days (40%) relative to the original images. The estimated attenuation maps also yield shadow-confidence maps that improve random-forest bone-shadow segmentation over the image alone and receive greater SHAP importance than an existing neural confidence-map baseline, suggesting greater physical consistency. RFlash requires neither hardware modification nor access to raw scanner data and supports 2D and 3D acquisitions with linear and curvilinear probes, making it widely applicable allowing clinicians to use our method on their already acquired scanners and images.

---


### 123. [A Hybrid CNN--State-Space--Attention Backbone with Joint-Embedding Predictive Pretraining for 12-Lead ECG Classification](https://arxiv.org/abs/2609.29376)

**<font color=#1a73e8>作者：</font>** Yakoub Bazi, Sarah Aljuhani, Mohamad M. Al Rahhal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic 12-lead electrocardiogram (ECG) classification requires representations that jointly capture local waveform morphology, long-range temporal dynamics, and cross-lead dependencies, yet integrating these properties within a single efficient architecture remains challenging. This paper introduces a hybrid CNN-SSM-Attention backbone for 12-lead ECG classification. A convolutional stem performs early waveform tokenization and temporal reduction, mixed state-space and depthwise-convolutional blocks model temporal dynamics and local morphology, and a late self-attention stage enables global token interaction at reduced resolution. To improve transfer from unlabeled data, we further develop an ECG-oriented Joint-Embedding Predictive Pretraining (JEPA) framework. Unlike ViT-based JEPA methods that mask patch tokens before the encoder, the proposed method samples span masks at the latent temporal resolution and projects them back to the waveform domain, then predicts clean latent targets from a momentum encoder without waveform reconstruction. Experiments on CPSC2018, Chapman-Shaoxing, and PTB-XL, with pretraining on approximately 350K unlabeled CODE-15 recordings, show that the proposed backbone provides strong supervised baselines under a compact parameter budget. JEPA pretraining further improves transfer, particularly in reduced-label settings and under both full fine-tuning and LoRA-based adaptation. Code: this https URL

---


### 124. [On the second-order optimization for spiking neural networks](https://arxiv.org/abs/2609.29379)

**<font color=#1a73e8>作者：</font>** Ngoc Phu Doan, Ihsen Alouani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) offer an energy-efficient alternative to conventional neural networks by exploiting sparse, binary spikes, and event-driven computation. However, the training of SNNs remains challenging, as spiking activations create a sharp loss landscape that hinders training, and diagonal-curvature optimizers such as the Adam family may fail to capture this geometry. The extension of curvature-based optimization methods to SNNs is further complicated by the sparse, discrete, and temporally recurrent nature of their underlying dynamics. To address these limitations, we propose SpiKFAX, a second-order optimization method that formulates a computationally tractable, Kronecker-factored approximation of the Fisher information matrix specifically adapted to the structure of SNNs. Empirical evaluation across five architectures and seven datasets demonstrates that SpiKFAX consistently yields improvements in test accuracy and training stability relative to other popular optimizers.

---


### 125. [An auditable conditional-strategy framework for open-ended decision-making in complex lung cancer](https://arxiv.org/abs/2609.29381)

**<font color=#1a73e8>作者：</font>** Daoyun Wang, Zhicheng Huang, Huaiyuan Sun 等 42 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex lung cancer decisions can involve several defensible pathways whose eligibility, sequencing and safety depend on unresolved information. Effective support must make explicit how patient conditions govern pathway eligibility, deferral and redirection. MedGPT Clinical Explorer (MCE) organizes alternatives, decision-changing unknowns, safety constraints and fallback into a conditional strategy for clinician review. To evaluate this representation in physician-authored strategies, multidisciplinary experts established case-specific references for 40 cases within a purposive 100-case corpus, and 250 physicians from 98 institutions produced 2,250 strategies under unaided, retrieval-reference and MCE-assisted conditions.
MCE-assisted strategies expressed more applicable clinical requirements, measured by the Admissible Pathway Attainment Score (APAS; 0-100), than unaided strategies (adjusted difference, 12.87; 95% CI, 11.18-14.55) and retrieval-reference strategies (5.22; 3.52-6.93). With the same knowledge base available in the retrieval-reference and MCE-assisted conditions, the additional content centered on candidate pathways, decision-critical information and safety constraints. Physicians' whole-strategy acceptability judgments correlated with APAS (Spearman's rho = 0.671), while a complementary relationship audit assessed whether candidates, conditions and subsequent actions were coherently connected.
Together, these findings identify two complementary dimensions of open-ended decision support: coverage of clinically relevant content and coherent links among pathways, conditions and subsequent actions. MCE provides a shared decision object that makes consequential omissions and pathway contingencies visible before action; prospective studies should evaluate its effects on clinical workflow and patient outcomes.

---


### 126. [Lightweight Probabilistic Downscaling from a Deterministic Base Model](https://arxiv.org/abs/2609.29383)

**<font color=#1a73e8>作者：</font>** Joseph McLean, Tiffany Vlaar, Sigrid Passano Hellan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Climate data downscaling is the task of increasing the spatial resolution of climate data, typically by generating fine-resolution regional climate data from coarse global model output. Recent machine learning (ML) work in the related task of weather forecasting has seen significant improvements due to newly devised training methods and architectural components, but these have not yet benefited downscaling. We adapt two of these methods to create a family of lightweight probabilistic ML downscaling models built on a modified U-Net backbone and evaluate them on the CORDEX-ML-Bench suite for daily maximum temperature and precipitation across three geographic regions: the Alps, New Zealand and South Africa. We find that a two-stage training curriculum, combining deterministic pretraining with probabilistic tuning, transfers well to downscaling, beating the state-of-the-art for RMSE. Our work provides an advancement towards lightweight, probabilistic downscaling models, reducing the current trade-off between computational intensity and distributional fit.

---


### 127. [Segment-Level Risk Discovery in Online Handwriting for Alzheimer's Disease Detection](https://arxiv.org/abs/2609.29384)

**<font color=#1a73e8>作者：</font>** Changqing Gong, Huafeng Qin, Mounîm A. El-Yacoubi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online handwriting provides a non-invasive and low-cost behavioral biomarker for Alzheimer's disease (AD) detection, as it reflects both cognitive planning and fine motor control. Existing handwriting-based AD detection methods usually rely on global trajectory features or whole-sample representations, which can be strongly affected by individual writing style, task-specific variation, and acquisition noise. In this paper, we propose NormPaST-Risk, a healthy-normative Paper-Air selective trajectory state-space risk network for interpretable AD detection from online handwriting. Instead of treating the entire trajectory as a single holistic representation, our method reformulates AD handwriting detection as local disease-relevant segment discovery. Specifically, a multi-scale temporal encoder captures stroke dynamics at different temporal resolutions, while a selective Paper-Air state-space encoder models long-range handwriting progression and distinguishes on-paper motor execution from in-air planning and transition behaviors. To explicitly characterize abnormal deviations, a healthy normative branch learns normal handwriting dynamics from healthy controls, and a task-aware multi-expert segment-risk module estimates segment-level AD risk calibrated by hidden-state changes and normative deviations. A weakly supervised segment-level objective further enables high-risk segment discovery without manual segment annotations. Experiments on the DARWIN benchmark demonstrate that the proposed framework achieves superior AD/HC classification performance compared with existing methods. Moreover, the discovered high-risk segments can be projected back to the original handwriting trajectory, providing interpretable evidence associated with AD-related handwriting variations.

---


### 128. [MORE-PLR: multi-output regression employed for partial label ranking](https://arxiv.org/abs/2609.29386)

**<font color=#1a73e8>作者：</font>** Santo M. A. R. Thies, Juan C. Alfaro, Viktor Bengs  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The partial label ranking problem is a supervised learning scenario that aims to fit a preference model that predicts a bucket order defined over a set of labels for a given input instance. This problem generalizes the well-known label ranking problem, which, in practice, is limited to outputting total orders of labels. Existing partial label ranking methods have primarily extended label ranking approaches to handle ties in predictions. This paper proposes using multi-output regression to address the partial label ranking problem, introducing an encoder that, during the learning phase, transforms the (possibly incomplete) rankings with ties of labels to multivariate regression targets, an underexplored perspective in both label ranking and partial label ranking. Moreover, during the inference phase, we introduce several post-hoc layers that convert the multi-output regression results into the output bucket order to effectively implement this approach. This framework provides learning strategies that are competitive with the current state-of-the-art partial label ranking methods, as demonstrated through experimental evaluations.

---


### 129. [When Misalignment Becomes Supervision: Structured Label Noise in Supervised Synthetic CT Generation](https://arxiv.org/abs/2609.29387)

**<font color=#1a73e8>作者：</font>** Valentin Boussot, Cedric Hemon, Caroline Lafond 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised synthetic CT (sCT) generation is commonly trained and evaluated as voxel-wise regression against registered reference CT images. In practice, MRI-CT and CBCT-CT pairs are aligned through registration procedures that leave residual misalignments. These residuals are not independent intensity noise but spatially coherent geometric discrepancies that act as structured label noise. We investigate how this registration-induced bias affects supervised MRI-to-CT and CBCT-to-CT synthesis on 1,784 paired patients covering five anatomical regions. Voxel-wise scores strongly depend on the consistency between the registration used to build the training targets and the one used for evaluation: models score best when both conventions match, showing that networks partly learn the geometric convention of the registration pipeline and that standard metrics reward it. Training on more anatomically consistent registrations reduces prediction variability and improves out-of-distribution robustness, and CT-only controls show that registration alone produces metric errors in the range of top challenge submissions. To mitigate the limits of voxel-wise supervision, we introduce a perceptual loss computed in the feature space of a pretrained Segment Anything encoder. Compared with MAE-only and VGG-based objectives, it improves downstream segmentation and yields sharper, more structurally coherent sCT. Perceptual and voxel-wise metrics disagree under imperfect alignment and agree when the evaluation geometry is reliable. These results identify registration-induced bias as a central confounder in supervised sCT generation and argue for complementing voxel-wise agreement with anatomy-oriented evaluation criteria.

---


### 130. [Wearable ECG Quality Assessment: A Deep Learning and Ambulatory Context-Awareness Approach](https://arxiv.org/abs/2609.29396)

**<font color=#1a73e8>作者：</font>** Xiaopeng Mao, Marike Weisbjerg, Sadasivan Puthusserypady  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents and evaluates a Deep Learning-based (DL-based) Signal Quality Assessment (SQA) model to distinguish between clean and noisy ambulatory Electrocardiograms (ECG). The model is trained on Copenhagen Center for Health Technology-Contextualized Arrhythmia Database (CACHET-CADB), which, to the best of our knowledge, is the first ambulatory ECG database with both physical and patient-reported contextual data. The model shows stable performance on different databases such as MIT-databases and the latest PyhsioNet/Cinc Challenge 2021 databases. Subsequently, the paper demonstrates how complicated ECG noise can be investigated by the SQA model and the physical contextual data.

---


### 131. [RD-JEPA: Predictive latent pretraining for few-trajectory transfer across reaction--diffusion equations](https://arxiv.org/abs/2609.29403)

**<font color=#1a73e8>作者：</font>** Chenhao Si, Ming Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning surrogates for time-dependent partial differential equations often requires a new simulation corpus when the governing operator changes. We introduce RD-JEPA, a joint-embedding predictive architecture for self-supervised pretraining on reaction-diffusion trajectories. A single model is pretrained on five parameterized systems and then adapted to three held-out systems whose reaction operators and trajectories are excluded from pretraining. Using one, five, or ten complete trajectories from a held-out system, RD-JEPA achieves lower mean relative discrete $\ell^2$ field error and mean absolute spatial first-difference error than five supervised surrogate baselines, an independently trained control that removes the trajectory-dependent predictive latent pathway, and an architecture-matched model trained from scratch. Within the evaluated equations, output resolution, forecast horizons, and choices of adaptation trajectories, the results indicate that prediction of future-state representations can support data-efficient adaptation across related reaction-diffusion systems.

---


### 132. [Neural Transport Nested Sampling](https://arxiv.org/abs/2609.29413)

**<font color=#1a73e8>作者：</font>** David Yallup, Will Handley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from Boltzmann distributions of molecular systems is an inference problem that has seen significant recent developments fuelled by advances in neural density estimation. We develop a novel sampling algorithm, Neural Transport Nested Sampling (NTNS), which combines the classical strengths of nested sampling with modern neural flow-based methods. NTNS uses a flow matching velocity as the drift in a Metropolis--Hastings corrected Langevin kernel inside a nested sampling outer loop, requiring only evaluations of the target energy function and providing scalable estimation of the full partition function of high-dimensional particle systems. We benchmark NTNS on challenging molecular sampling benchmarks, scaling up to Lennard--Jones clusters of 55 interacting particles, where it reduces both interatomic distance and energy Wasserstein errors to reference MCMC by over an order of magnitude relative to the strongest neural baselines at lower wall-clock cost. To our knowledge, NTNS is also the first neural sampler to return a calibrated, temperature resolved partition function estimate at this scale, recovering the phase structure across temperature from a single run.

---


### 133. [Controlling Backchannels in Streamable Full-duplex Models](https://arxiv.org/abs/2609.29418)

**<font color=#1a73e8>作者：</font>** Maike Züfle, Peter Polák, Sefik Emre Eskimez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Backchannels, brief acknowledgements like "uh-huh" produced while the other party may still be talking, are central to natural conversation, but full-duplex spoken dialogue models rarely model them explicitly. We introduce a lightweight backchannel head that predicts, from a full-duplex model's own hidden states, when a backchannel should begin. Once this probability crosses a tunable threshold, a backchannel is force-decoded. Attached to both a 7B (PersonaPlex) and a 1B (F-Actor) model, it generalizes across scale. Probing confirms the hidden states anticipate real human timing, and generation evaluation shows more frequent, better-timed backchannels. Human raters judge the resulting backchannels on par with real ones.

---


### 134. [Detecting Glaucoma Across Multi-ethnic Myopic and Non-Myopic Populations Using an Uncertainty-Aware Vision Transformer: A Multicentre Model Development and Validation Study](https://arxiv.org/abs/2609.29433)

**<font color=#1a73e8>作者：</font>** Raghavan Lavanya, Yangqin Feng, Ten Cheer Quek 等 39 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Artificial intelligence (AI)-based glaucoma detection from colour fundus photographs (CFP) offers scalable screening, but performance may decline on external datasets because of differences in ground-truth definitions, populations, and coexisting conditions such as high myopia (HM). We developed and validated a Vision Transformer-based deep learning (DL) model for glaucoma detection across multi-ethnic cohorts with and without HM. Methods: A ViT-B/16 model with predictive uncertainty estimation was developed using 56,483 CFPs (57.1% with myopia; 14.4% with HM). Glaucoma labels were standardised using clinical, imaging, and perimetry data. The model was validated on 16 independent datasets across three continents, including four datasets with explicit HM labels. Findings: Internal AUROC was 98.7% (95% CI 98.2-99.1%), with sensitivity 94.5% and specificity 97.3%. Across 16 external datasets from eight countries, AUROCs ranged from 86.4% to 99.6%. In HM eyes, internal AUROC was 97.8% (95% CI 96.1-99.2%), with sensitivity 94.8% and specificity 93.7%. External HM AUROCs were 86.5% in the Beijing Eye Study and 93.3%, 91.8%, and 85.5% in hospital-based datasets from Taiwan, Thailand, and South Korea. In an exploratory HM clinical evaluation, the model had higher CFP-only diagnostic accuracy than ophthalmologists and trained graders (92.0% vs 70.0%; p=0.008) and performed comparably to glaucoma specialists using full clinical information. Interpretation: The model showed robust glaucoma detection across myopic and non-myopic multi-ethnic populations and may support AI-assisted screening in settings with high HM prevalence.

---


### 135. [Pose Adaptive Dynamic FiLM Modulation for Visual Speech Recognition](https://arxiv.org/abs/2609.29443)

**<font color=#1a73e8>作者：</font>** Matthew Kit Khinn Teng, Haibo Zhang, Takeshi Saitoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Head-pose variation introduces substantial appearance transformations in visual speech recognition (VSR), making pose-aware feature modulation desirable. However, performance degradation and unwanted feature interactions may result from using numerous Feature-wise Linear Modulation (FiLM) circuits with fixed modulation intensity. We propose a Pose Adaptive Dynamic FiLM framework with a Dynamic Residual FiLM (DR-FiLM) modulator that predicts input-dependent weights to adaptively control the strength of pose-conditioned modulation. Experiments on LRS2 and LRS3 demonstrate that unweighted multi-pathway modulation substantially degrades phoneme recognition, increasing PER to 20.33% and 29.42%, respectively, compared with 16.20% and 20.96% for the single ResFiLM configuration. In contrast, the proposed DR-FiLM with dynamic Deep-Res weighting reduces PER to 15.74% on LRS2 and 23.91% on LRS3, substantially mitigating the adverse effects of unweighted modulation. The analysis of the learned weights further reveals a consistent tendency to assign greater weight to the deeper FiLM pathway as head-pose variation increases. These results show that merging pose-conditioned FiLM circuits is more efficient when the modulation strength is dynamically controlled.

---


### 136. [SPADE-DFL: Communication-Efficient Decentralized Federated Learning via Derivative-Free Linearized ADMM](https://arxiv.org/abs/2609.29446)

**<font color=#1a73e8>作者：</font>** Mengli Wei, Mengkai Zhu, Jiawen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reducing communication in derivative-free decentralized learning requires controlling the disagreement accumulated over multiple local updates. This paper develops SPADE-DFL, a primal--dual method that allows the number of local function-value updates between neighbor exchanges to grow with the computation budget while preserving the nonprivate convergence order. For smooth nonconvex objectives under uniform query-moment bounds, the prescribed nonprivate schedule achieves a time-averaged stationarity and consensus bound of $\mathcal{O}(T^{-1/3})$ using only $\Theta(T^{2/3})$ communication rounds, where $T$ is the number of local updates per client. For private training, the accumulated data-dependent increment is isolated from the graph correction, allowing one protected state per client and round to generate all outgoing messages. We prove client-level differential privacy for the full interactive transcript and quantify the resulting optimization error over a finite horizon. Experiments on four classification tasks show that SPADE-DFL achieves higher mean test accuracy than existing decentralized learning methods.

---


### 137. [Frame-to-Panorama Localization and Context-Aware Sampling for Scene-Specific Ship Detection in a Smart Marina Testbed](https://arxiv.org/abs/2609.29447)

**<font color=#1a73e8>作者：</font>** Ignat Romanov, Andreas Hadjipieris, Neofytos Dimitriou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Smart maritime infrastructures provide continuous access to heterogeneous sensing streams, enabling repeated experimentation, digital-twin development, and AI-based maritime services. However, sensing hardware alone is not sufficient for scene-specific model development: historical video streams must also be spatially indexed, contextualized, and reduced to informative subsets for annotation. This paper presents a frame-to-panorama localization and context-aware sampling pipeline for ship detection in historical PTZ maritime video lacking reliable pan, tilt, and zoom metadata. The main contribution is an end-to-end data-curation approach that recovers camera-view information from historical PTZ video and combines it with environmental context and visual diversity to construct compact, scene-specific training sets. Specifically, frames are localized on a reference panorama using SuperPoint and LightGlue, enriched with weather and solar-state metadata, and selected through diversity sampling to preserve variation across camera view and environmental conditions. A second context-aware stage targets under-represented distant-vessel cases near the horizon using tile-level visual embeddings and Gaussian Mixture Model clustering. Applied within the CMMI MDigi-I Smart Marina testbed, the proposed pipeline reduces 40,718 candidate frames to 220 images for annotation, corresponding to a 99.5% reduction. A YOLO26-m detector fine-tuned on this subset achieves a mean AP50 of 94.78% $\pm$ 0.51% and a mean AP50-95 of 75.10% $\pm$ 1.73% under sequence-grouped five-fold cross-validation. These results demonstrate that highly redundant infrastructure video streams can be transformed into compact, spatially and contextually diverse training sets for scene-specific detector adaptation while substantially reducing annotation effort.

---


### 138. [YODAS v3: Over 1 Million Hours of High-Bandwidth, Stereophonic, Multilingual Speech](https://arxiv.org/abs/2609.29448)

**<font color=#1a73e8>作者：</font>** William Chen, Shinnosuke Takamichi, Sayaka Shiota 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present YODAS v3, a weakly-labeled speech corpus containing over 1.1 million hours of 48kHz multi-channel audio in 147 languages, released under a CC BY 3.0 license. YODAS v3 is not only the largest open speech dataset to date, but also the first truly large-scale speech corpus with high-fidelity stereo audio. We first provide the collection methodology for the corpus, where we introduce new techniques for gathering language-balanced speech data. The effectiveness of our approach is shown by the language distribution of the crawled data: 22 languages in YODAS v3 have over 10K hours and 73 languages have over 5K hours of data. We then conduct extensive analyses on the composition of the data, such as the distribution of languages, audio quality, and transcription quality. Finally, we train baseline speech recognition and neural codec models to show the effectiveness of the dataset. Download at this https URL.

---


### 139. [Decoupled Learning and Selection in Slate Recommendation for Privacy and Stability Under Noisy Scores](https://arxiv.org/abs/2609.29453)

**<font color=#1a73e8>作者：</font>** Sam Urmian, Qinyi Liu, Mohammad Khalil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formalize slate recommendation as a randomized score learner followed by deterministic selection. First, an appropriately scoped differential-privacy guarantee passes through selection and its audit trace by post-processing. End-to-end privacy holds only when selector inputs are public or independent, previous private outputs, or separately privacy-accounted; fixing raw state or candidate information instead yields only a conditional guarantee. Second, we derive a logged margin certificate: bounded score-induced objective movement below half the smallest greedy decision margin guarantees that the ordered slate is unchanged.
Controlled fixed-margin tests show near-linear exponent scaling, with an empirical slope of $-0.220$ (95% CI $[-0.231,-0.210]$) against the independent-noise reference $-1/4$. Real-anchor experiments on OULAD, MovieLens-25M, and Amazon Musical Instruments show that greater anchor weight reduces score-noise-induced ranking churn. OULAD and EdNet certificate checks validate the implementation of the logged inequality, while closed-loop simulations show bounded target drift and setting-dependent downstream utility. The contribution is therefore a privacy-scope contract and a certifiable score-to-slate stability mechanism, not a universal utility claim.

---


### 140. [Dense Coverage, Sparse Refinement: Byte-Constrained Cooperative Perception](https://arxiv.org/abs/2609.29456)

**<font color=#1a73e8>作者：</font>** Melih Yazgan, Timon Müller, J. Marius Zöllner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception improves autonomous perception by sharing intermediate Bird's-Eye-View (BEV) features across connected agents, but dense feature exchange is difficult to deploy under strict Vehicle-to-Everything (V2X) bandwidth limits. Existing efficient methods typically either compress the full feature map uniformly, spending bits on low-value background, or sparsify communication, risking the loss of useful context. We propose a coverage-refinement design for byte-constrained cooperative perception: each agent transmits a highly compressed coarse layer over the full BEV map and allocates the remaining budget to selected high-resolution patches. A Task-Aware Benefit Selector ranks cells by estimated downstream utility, enabling deterministic budgeted refinement and zero-retraining adaptation to changing bandwidth. The receiver reconstructs a dense BEV tensor compatible with standard fusion modules. Experiments on DAIR-V2X and OPV2V show strong accuracy-payload trade-offs at kilobyte-scale budgets. On DAIR-V2X, our method reaches 0.60 AP@0.7 at only 1.87 KB per non-ego agent, compared with 0.52 at 4.61 KB for uniform SimVQ compression. Controlled diagnostics further show that the gain arises from coverage-refinement allocation rather than quantization alone. Code will be published.

---


### 141. [Precise Convergence Speed of Clipped SGD](https://arxiv.org/abs/2609.29458)

**<font color=#1a73e8>作者：</font>** David A. R. Robin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a tightened convergence analysis of clipped gradient descent on $(L_0, L_1)$-smooth functions, with quantitative constants. Building on the ideas of Koloskova et al (2023), we refactor several case disjunctions to reveal the central role of a control of the bias derived from fundamental properties of $\ell_2$-projection, simplifying proofs. We also extend the domain of validity from $\eta \leq 1 / (9 \beta)$ to $\eta < 1 /\beta$ where $\beta = L_0 + c L_1$ for clipping constant $c$, which matches the more traditional analysis of smooth functions. We strengthen the convergence criterion from $\left( \min_{t < T} \mathbb{E}[\lVert \nabla f(x_t) \rVert_2] \right)$ to $\left( \frac{1}{T} \sum_{t < T} \mathbb{E}[\lVert \nabla f(x_t) \rVert_2] \right)$ with matching speed, and lower the final achievable loss from $\mathcal{O}(\min(\sigma^2/c, \sigma))$ to the more precise $6 \min(\sigma^2 /c, 3 \sigma)$.

---


### 142. [AgriCountDINO: Parameter-Efficient Exemplar-Guided Counting and Localization in Agriculture](https://arxiv.org/abs/2609.29460)

**<font color=#1a73e8>作者：</font>** Shengjie Guo, Xin Li, Borjana Arsova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate counting and localization of plants and their organs support phenotyping and yield estimation, yet target appearance, scale, and density vary widely across species and imaging conditions. Exemplar boxes specify the target without category-specific retraining, and point predictions identify the individual instances contributing to the count. We introduce AgriCountDINO, a parameter-efficient exemplar-guided framework for joint counting and localization. It conditions frozen multiscale DINOv3 features on exemplar appearance and size, then progressively decodes them into target points. Missed-object recovery extends supervision to targets overlooked by initial matching, and exemplar-adaptive point NMS filters duplicate predictions according to exemplar scale. With 8.4M trainable parameters, approximately one-tenth of TasselNetV4's, AgriCountDINO achieves a three-shot MAE of 11.92 on the TPC-268 benchmark, reducing counting error by 9.7\% while providing individual target locations. Trained only on TPC-268, it achieves a zero-shot MAE of 14.25 on unseen generic object categories in FSC-147, improving upon the best compared zero-shot method by 6.0\% without target-domain training or fine-tuning.

---


### 143. [Direct Message Approximation (DMA): A Consistency-Based Framework for Tractable Approximate Inference on Factor Graphs](https://arxiv.org/abs/2609.29466)

**<font color=#1a73e8>作者：</font>** Ralf Herbrich, Rainer Schlosser, Jan Lemcke 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Approximate message passing on factor graphs underlies two dominant families of probabilistic inference algorithms: expectation propagation (EP) and variational message passing (VMP). Both methods approximate the marginal at each factor edge, forcing an iterative round-robin schedule, risking negative-precision messages, and, for VMP, collapsing to point estimates at Dirac-delta factors. We introduce Direct Message Approximation (DMA), which approximates factor-to-variable messages directly rather than the marginal. For normalisable factors, we define a consistency condition (requiring exactness when all other incoming messages are Dirac deltas) to guide message construction. We prove a master theorem (proper messages, any graph) bounding marginal KL from message KL, with three structural corollaries: Dirac-input consistency, no EP-style inner-loop iteration, and no negative-precision messages. Further, we prove a complementary $O(1/r^2)$ guarantee for the inherently improper backward message of the product factor, whose closed-form treatment has resisted prior work. As a concrete instantiation, we derive explicit DMA messages for the product and leaky-ReLU factors and assemble a Bayesian neural network (BNN) inference algorithm with one forward/backward sweep per training example and no gradient learning-rate hyperparameter, validating that the structural guarantees translate to predictive uncertainty that widens in data-sparse regions, including under model mismatch.

---


### 144. [Clinical Intent Extraction: A FHIR-Aligned Representation and the CIRCA Benchmark](https://arxiv.org/abs/2609.29479)

**<font color=#1a73e8>作者：</font>** Alexander Apartsin, Yehudit Aperstein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prospective clinical actions, the follow-ups, orders, referrals, and instructions that deter-mine what happens to a patient next, are annotated today in thin fragments across incom-patible corpora: each records a text span and one coarse category. We introduce Clinical Intent Extraction (CIE), the task of recovering these actions as complete structured rec-ords, and the Clinical Intent Representation (CIR), which decomposes each action into its verb, type, coded target, timing, and condition, and adds two axes prior datasets do not jointly represent: request-intent, the authority behind the action (proposal, plan, order, or option, aligned to HL7 FHIR), and modality, a seven-valued scale of clinical strength. Re-expressing five heterogeneous corpora (CLIP, MedDec, ap_parsing, PaniniQA, SIMORD) in the CIR yields CIRCA: 10,011 harmonized intents spanning two note distributions, with a human-validated subset, source-to-CIR crosswalks, and a deterministic FHIR R4 mapper. CIRCA is built by three-model consensus that auto-accepts high-agreement in-tents and routes the rest to human review; the audited agreement stratum matches human decisions 88.4% of the time. Benchmarking five existing models without task-specific training exposes the gap CIRCA targets: given the span, they label type well (85 to 91%) but get all four closed fields right only 18 to 35% of the time. All artifacts are released, with MIMIC-derived layers shared as stand-off annotations under PhysioNet credentialed access.

---


### 145. [A Graph-Based Stackelberg Security Game for Trustworthy 6G Disaggregated Architecture](https://arxiv.org/abs/2609.29500)

**<font color=#1a73e8>作者：</font>** Lav R. Varshney, Xinbo Wu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open, cloud-native, and AI-enabled 6G architectures make network functions easier to deploy, observe, and replace, often implemented with separate software modules. However, each explicit interface can also create an entry point, trust transition, and lateral-movement route from a cybersecurity perspective. This paper formulates architectural disaggregation as a graph-based Stackelberg design game for 6G system security. A deployment graph specifies candidate 6G system seams, while an architecture-dependent directed attack graph specifies externally reachable functions and multistage paths. The defender commits to seams and allocates hardening and monitoring; an informed attacker then chooses a path and effort. Because edge traversal and evasion factors compose multiplicatively, the attacker's path response becomes a shortest-path problem after a logarithmic transformation. Convex effort costs admit a conjugate representation, and, for each fixed architecture, the defender's control problem is a convex exponential-epigraph program solvable by path generation. We derive an architecture-comparison criterion, a threshold for AI transducers within 6G systems that jointly add visibility and exposure, and comparative statics for attacker entry and bypass innovation. Experiments with stylized standards-anchored O-RAN/6G systems over RAN, RIC, core, cloud, and edge-AI functions show that neither full integration nor maximal disaggregation is generally best. Uncontrolled seams can increase risk, whereas selectively monitored and hardened seams can improve the Stackelberg objective. We find a boundary is worthwhile only when its detection and containment gains exceed its added attack opportunities and coordination cost.

---


### 146. [Spectral-Guided Diffusion: Accelerating Inference via Static Spectral Layer Scheduling](https://arxiv.org/abs/2609.29505)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion inference repeatedly evaluates the same large network. We ask whether pretrained weights alone can identify residual branches that need not be recomputed throughout the trajectory. Our \textbf{Spectral Concentration Ratio (SCR)} measures leading-versus-tail singular-value energy. Combined with Frobenius magnitude, it yields an offline sensitivity proxy and a deterministic lifetime for each scheduled unit. A frozen unit reuses its cached residual-branch update while the current residual stream and all external conditioning continue to propagate. The method needs no router, calibration prompts, or input-dependent search. At matched layer-step budgets, SCR/Frobenius preserves quality better than random, depth, norm, stable-rank, and Frobenius--stable-rank schedules on LLaDA-8B, DiT-XL/2, U-ViT-L, and SDXL. Broader LLaDA tests cover retrieval, reasoning, code, summarization, and open-ended generation; matched-horizon controls retain the ranking down to ten denoising steps. The complete captured-graph system reaches $2.8\times$--$3.0\times$ wall-clock speedup over eager inference. This is a systems-level number: on LLaDA, padded graph execution already gives $2.7\times$, while eliminating inactive branch work raises it to $3.0\times$. The perturbation analysis motivates pre-norm attention and MLP components under explicit local assumptions; results on AdaLN, U-shaped, convolutional, and cross-attention blocks are empirical transfer, not certified guarantees.

---


### 147. [What a Cross-Model Fixed-Point Census Can and Cannot Arbitrate About Repetition](https://arxiv.org/abs/2609.29507)

**<font color=#1a73e8>作者：</font>** Nicolás Vera Zúñiga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Two accounts of neural text degeneration coexist. One locates the cause in the training data -- repetition in the corpus produces repetition in the output, established by training on repetition-sorted data -- the other in the trained network, in copying circuits and repetition features. Neither has been arbitrated across a broad cohort of pretrained models: the causal work trains its own. We report an observational measurement in a different currency: the fixed-point structure of a model's own short-window argmax map, censused from 96 random two-token starts over 17 off-the-shelf models, always unprompted -- a companion paper shows nine tokens of conditioning move this readout across most of its range. The four-way class is stable across census seeds on 17 of 17. Three exhibits. At fixed corpus (The Pile), fixed scale and that fixed domain, the class is not determined: across two size-matched tiers, pythia is a funnel while RWKV, Mamba and a second transformer family are not, and both hold their class across an order of magnitude of scale. Six of seven models in that ladder reach the same endpoint token, and those concentrating on it most strongly are among those that never stay there -- what varies is not where trajectories go but whether the destination self-continues. The deduplicated Pythia suite does not change the class. And the corpus-side inflow term proposed for this phenomenon does not select our endpoints once frequency is controlled, in English and three other languages. This is observational and cannot refute a training intervention. Funnels are common: eight of seventeen models, seven families, five corpora -- so the limit is not that the phenomenon is one model's peculiarity, but that within the one corpus where training data can be held fixed only one available family funnels; that subset cannot show the split is corpus-independent.

---


### 148. [AdaPilot: Towards Scene-Adaptive Policy Learning for Cross-Generator Text-to-Image Quality Optimization](https://arxiv.org/abs/2609.29517)

**<font color=#1a73e8>作者：</font>** Wenjin Liu, Fayuan Ke, Yue Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing methods for improving text-to-image generation quality have progressed from generator fine-tuning and prompt optimization to reinforcement learning with multi-turn visual feedback. However, existing strategies are deeply coupled with specific generators and tasks, and the learned capabilities are difficult to generalize into a universal quality optimization policy. Therefore, we propose AdaPilot, which learns a scene-adaptive, cross-generator transferable quality optimization policy by formulating multi-turn image generation as a Markov Decision Process (MDP) and optimizing it via end-to-end reinforcement learning. Specifically, AdaPilot decouples the policy from generator internals to enable cross-generator transfer, introduces scene-aware rewards that adaptively align quality assessment dimensions with task semantics, and employs process-level rewards to model the evolution trajectory of image quality. Experimental results show AdaPilot outperforms baselines in generation quality and generalization. Separate cross-generator evaluations further show that a single policy transfers zero-shot to unseen generators while maintaining positive average gains across all evaluated generators. Our project is available at this https URL.

---


### 149. [Sample-Weighted End-to-End Trace-Norm Geometry for Multitask Learning](https://arxiv.org/abs/2609.29520)

**<font color=#1a73e8>作者：</font>** Mahdi Mohammadigohari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multitask models combine a shared representation with task-specific outputs, but generalization bounds often control the two components separately. Such products can discard relative orientation and cancellation and can change under equivalent transformations of intermediate coordinates even when the represented predictors are unchanged. We study instead the sample-size-weighted trace norm of the end-to-end map from task coefficients to input-space predictors. For its fixed-radius class, we derive the exact empirical Rademacher complexity. The same quantity is characterized by eliminating a positive-definite task covariance after the representation acts and, in finite-dimensional intermediate spaces, by optimizing the separated product over all equivalent invertible refactorizations. Explicit constructions show unbounded orientation and factorization gaps and an exponential depth gap for cancelling linear layers. As a geometric application, finite-to-one Lipschitz shared maps yield an exact Sobolev task Gram matrix determined by multiplicity and local directional distortion. We evaluate the corresponding convex regularizer in two protocol-locked unseen suites. Across 252 paired held-out comparisons, weighted joint nuclear regularization improves average population excess over unweighted nuclear regularization by 0.00764, with a stratified-bootstrap 95% interval [0.00465, 0.01110]. Correct task counts improve average and least-sampled-quartile excess over shifted counts by 0.01072 and 0.02847; all 15 imbalanced rank-suite cells are positive and the balanced effect is zero. Weighted joint nuclear also outperforms weighted Frobenius and independent ridge. The least-sampled-quartile comparison with unweighted nuclear remains unresolved, delimiting rather than contradicting the average advantage. All seven predeclared gates pass.

---


### 150. [Common Covariance Geometry and Certification for Brownian Kernel Ladders](https://arxiv.org/abs/2609.29525)

**<font color=#1a73e8>作者：</font>** Mahdi Mohammadigohari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A representation-adaptive kernel class produces, on a fixed sample, a union of reproducing-kernel Hilbert-space ellipsoids rather than one ellipsoid. We introduce the minimum-trace common covariance that dominates the unrestricted empirical union generated by Brownian kernel ladders and develop its statistical, approximation-theoretic, and computational consequences. The covariance value admits exact formulations through absolutely two-summing operators and covariance-dominated multipliers, and it yields a universal Gaussian-complexity bound. A closed last-layer Dirac-trace reduction and a signed Brownian threshold representation convert the generic covariance problem into threshold, graph-coarea, and effective-resistance geometry. These tools give deterministic depth laws, conditional Gaussian reverses, random-design and perturbation transfers, and an exact empirical Kolmogorov-width formula whose leading covariance eigenspaces approximate the complete adaptive ball simultaneously. Finite contact, active semidefinite programs, verified separation, and a convex resistance-design relaxation provide complementary lower and upper certificates. A finite covariance-indexed Brownian path on frozen representations illustrates the distinction between successful covariance certification and predictive selection: all reported path certificates succeed, whereas the locked predictive study misses one predeclared aggregate criterion. The paper thereby identifies one finite-dimensional covariance object linking unrestricted kernel adaptation, Gaussian geometry, common subspaces, and certifiable computation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
