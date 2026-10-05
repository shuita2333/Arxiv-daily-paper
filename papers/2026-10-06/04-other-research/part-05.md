# 📦 其他研究 | 2026年10月06日

> 本类共 **260** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-260](./part-06.md)

---

### 201. [AIBL: Augmented Instance-Based Learning with Structured Memory and Neural Embeddings](https://arxiv.org/abs/2610.03413)

**<font color=#1a73e8>作者：</font>** Radha Poovendran, Andrea Stocco, Linda Bushnell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential learning systems often make decisions from accumulated experience while receiving high-dimensional inputs whose distribution may change over time. Instance-Based Learning Theory (IBLT) provides a principled case-based framework for such settings through stored situation-decision-utility instances, partial matching, activation, and blending. IBLT relies on symbolic knowledge representation in dictionary-like formats, but text, images, transaction vectors, and user-item histories often require learned similarity rather than hand-specified matching rules. In this paper, we introduce AIBL (Augmented Instance-Based Learning), an instance-learning model formulated in a learned vector space for high- dimensional sequential data. AIBL generalizes symbolic situation matching to neural embedding similarity while retaining instance storage, activation- weighted retrieval, and utility blending. The AIBL model organizes memory into active, forgotten, and surprise stores. Surprise memory separates weakly matched, possible out-of-distribution, or corner-case observations from active memory, reducing forced fitting to the nearest available cases. An observation-driven graduation algorithm promotes recurring surprise instances to active memory, allowing the memory to incorporate repeated novel patterns that may arise under concept drift. We evaluate the same implementation on five machine learning tasks and three controlled simulation tasks, comparing AIBL with classical IBLT variants and task-specific baselines where appropriate. AIBL improves accuracy by 6 to 17 percentage points. The results show where vector-space retrieval improves over symbolic matching and how the added memory mechanisms govern novelty detection, cold-start handling, drift adaptation, and reward learning under the tested protocols.

---


### 202. [Rethinking Epistemic Uncertainty in Node Classification through Information Growth](https://arxiv.org/abs/2610.03418)

**<font color=#1a73e8>作者：</font>** Emma Meneghini, Francesco Ferrini, Bruno Lepri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Epistemic uncertainty should decrease as additional information about the data-generating process (DGP) becomes available to the predictor. Yet, existing graph evidential deep learning (EDL) methods for node classification typically construct epistemic uncertainty from graph-specific properties and evaluate it on downstream tasks such as out-of-distribution detection, which do not test its reducibility as information about the DGP increases. To make reducibility directly testable, we introduce a statistical framework for studying epistemic uncertainty under information growth. Our framework specifies an information-growth experimental protocol and a consistency criterion for epistemic predictors, while using projective graph DGPs to ensure that growing graphs, which in general need not provide increasing information about the same DGP, constitute coherent observations of the same underlying process. We show that EDL methods do not explicitly estimate data uncertainty arising from a single finite graph observation and instead regulate epistemic uncertainty through model hyperparameters, precluding consistency, as corroborated by controlled information-growth experiments. As an alternative, we propose graph bootstrap ensembles, capturing both data and procedural uncertainty through graph resampling and randomized training. Under the same experimental protocol, these ensembles exhibit epistemic uncertainty reduction beyond standard deep ensembles. These findings support bootstrap ensembles as candidate consistent epistemic predictors under information growth.

---


### 203. [Deep Bayesian REFoCUS](https://arxiv.org/abs/2610.03419)

**<font color=#1a73e8>作者：</font>** Simon Penninga, Ruud van Sloun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work we formulate ultrasound multistatic recovery from arbitrary transmit sequences as a Bayesian inference problem. To that end, we train a deep generative prior on multistatic data sets to tackle the rank-deficient regime in which classical linear REFoCUS decoders fail. This appproach, which we term Deep Bayesian REFoCUS, outperforms the linear baselines for all regimes of rank-deficiency and noise levels, and regresses to linear decoding when inversion is exact. The model also expresses uncertainty in the null space of the acquisitions, whereas the linear REFoCUS decoders only provide point estimates. Finally, we analyze the impact of distribution shift between simulation and in-vivo acquisitions, showing remarkable generalization ability without any fine-tuning or adaptation.

---


### 204. [OuroReward: Sequential Reward Scheduling for Reinforcement Learning in Text-to-3D Generation](https://arxiv.org/abs/2610.03423)

**<font color=#1a73e8>作者：</font>** Bingyang Cui, Yujie Zhang, Yiling Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for Text-to-3D (T23D) generation requires optimization across multiple quality dimensions such as semantic alignment and texture clarity. Existing methods typically optimize these dimensions simultaneously through multiple reward aggregation, without explicitly modeling inter-dimension dependencies. This can cause imbalanced optimization and persistent interference among conflicting dimensions. To address this limitation, we propose OuroReward, an interference-aware sequential reward scheduling strategy for T23D RL. OuroReward first estimates pairwise dependencies among dimensions and constructs a cyclic optimization path that minimizes cumulative interference. By incorporating the tail-to-head dependency, the cycle captures global compatibility across the entire schedule. Then, OuroReward converts the cycle into a one-pass sequence, and starts optimization from the dimension with the lowest aggregate interference. Rather than assigning a fixed optimization budget to each dimension-wise reward, training adaptively determines when to advance to the next reward according to the remaining optimization headroom of the current one. We further introduce AdaSelect, an adaptive prompt selection strategy that identifies reliable and informative prompts aligned with the model's current capability. By focusing policy updates on these prompts, AdaSelect effectively improves training stability. Extensive experiments across different T23D models and RL algorithms demonstrate that our framework consistently improves generation quality across multiple dimensions.

---


### 205. [Becoming Suspicious Across Borders: Algorithmic Extraterritoriality and AI-Driven Financial Surveillance](https://arxiv.org/abs/2610.03425)

**<font color=#1a73e8>作者：</font>** Georgios Pavlidis, Savvas Chatzichristofis, Eleni Gavriil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Suspicion is an important, yet elusive concept in anti-money laundering and counter-terrorist financing (AML/CFT), which allows for intervention below the threshold of proof. In its traditional form, suspicion can be understood as a situated legal judgement by human actors within identifiable jurisdictions. It is argued that this understanding is no longer adequate. As artificial intelligence (AI) becomes an integral part of financial surveillance, suspicion is increasingly produced through data-driven processes. This transformation is epistemic, but also spatial. Since AI-driven financial surveillance operates through transnational data infrastructures, regulatory reach is less a matter of where conduct occurs than a question of whether such conduct becomes visible within data systems. This article develops the concept of algorithmic extraterritoriality, understood as a form of regulatory power mediated by data infrastructures rather than formal assertions of jurisdiction. Moreover, since individuals are increasingly constituted as datafied subjects of suspicion, they are rendered governable through dispersed and opaque processes of evaluation. This constitutes a challenge for accountability and contestability because suspicion becomes more difficult to locate, explain or contest.

---


### 206. [Depth Hypothesis Guided Iterative Refinement for Event-Image Monocular Depth Estimation](https://arxiv.org/abs/2610.03439)

**<font color=#1a73e8>作者：</font>** Daikun Liu, Teng Wang, Changyin Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras hold excellent dynamic properties, showing great potential for monocular depth estimation (MDE). However, existing methods mainly improve performance by optimizing contextual features, but still struggle with the ill-posed and nonlinear nature of direct full-depth regression. In this paper, we propose HypoDepth, the first event-image monocular depth iterative refinement framework. By introducing a discrete Depth Hypothesis Volume (DHV), we transform the depth regression problem into a constrained depth search task. Specifically, we construct a 3D cost volume between the DHV features and contextual features and perform a multi-scale correlation search to guide stable residual optimization. This lightweight cost volume enables efficient global-to-local refinement across multi-resolution. Our method outperforms existing approaches on DSEC and MVSEC with state-of-the-art results and strong zero-shot generalization. Meanwhile, our tiny model achieves an excellent balance between accuracy and efficiency, enabling real-time performance on resource-limited devices.

---


### 207. [ChromaGS: Text-Driven Semantic Editing of 4D Gaussian Avatars](https://arxiv.org/abs/2610.03441)

**<font color=#1a73e8>作者：</font>** Antonio Canela, Jordi Sànchez-Riera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ChromaGS, a method for real-time, language-guided color editing of animatable 3D Gaussian head avatars. Given a trained animatable avatar, users can instantly modify the color of semantic regions through natural language, with edits applied at render time and no retraining required. Our key insight is to augment each Gaussian primitive with learned soft assignments to semantic regions and decompose colors into region-level base colors and Gaussian-level residuals. This decomposition enables coherent color transfer: modifying a region's base color propagates naturally through all associated Gaussians while preserving fine appearance details encoded in residuals. A two-stage language pipeline translates text instructions into target colors, supporting both absolute specifications and relative adjustments. Unlike generative editing methods that may introduce unintended modifications, our approach provides deterministic, precisely localized semantic control. Experiments demonstrate faithful appearance preservation and intuitive interaction across diverse subjects. Project page and code are available at: this https URL

---


### 208. [Causal Representation Learning with Instantaneous and Lagged Relations via Nonstationarity](https://arxiv.org/abs/2610.03452)

**<font color=#1a73e8>作者：</font>** Tatsuya Yamada, Hiroshi Morioka, Yoshinobu Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal representation learning for time-series data aims to identify latent states and their causal relations from observations. In this setting, an important challenge is to model both lagged causal relations across observation intervals and faster causal effects that appear as instantaneous relations within an interval, while accounting for nonstationarity in time-series data. However, methods that jointly handle these causal relations and nonstationarity remain limited. To address this gap, we establish sufficient conditions for identifying latent states up to component permutation and component-wise invertible transformations, and their instantaneous and lagged causal structures up to the same permutation, using an observed auxiliary variable, such as time or a condition label, associated with changes in transition-noise distributions. Based on these results, we propose iCReN, a framework that uses contrastive learning with discrete or continuous auxiliary variables to learn latent representations and estimate their instantaneous and lagged causal structures. Experiments demonstrate accurate recovery of latent states and both instantaneous and lagged causal structures on synthetic data and the utility of the learned representations for downstream forecasting on real-world data.

---


### 209. [Measure Less, Know More: Self-Supervised Test-Time Feature Acquisition](https://arxiv.org/abs/2610.03454)

**<font color=#1a73e8>作者：</font>** Eeshaan Jain, Linus Bleistein, Bart Deplancke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in multimodal, high-dimensional learning has enabled foundation models to process heterogeneous, large-scale data. However, at test time, acquiring all features or modalities can be prohibitively costly and often redundant. Sequentially selecting informative modalities is therefore critical, yet challenging when the downstream task or prediction target is unknown. To this end, we introduce ECHO-$k$, a task-agnostic and self-supervised learning principle for modality acquisition: we use a deep model's internal pretrained representations (e.g., from a foundation model) as proxy targets that summarize cross-modal information. We provide theoretical guarantees in a stylized linear setting that motivate a reinforcement learning (RL) policy for sequential modality selection. Across task-agnostic and label-free acquisition baselines, ECHO-$k$ consistently improves budgeted downstream performance across diverse foundation-model backends. Our method provides a principled route to cost-aware test-time deployment, with implications for any multimodal system where measurements are expensive or time-constrained, and downstream tasks unknown a priori.

---


### 210. [Beyond Random Splits: Evaluating Drug-Target Affinity Models Under Chemically and Biologically Motivated Distribution Shifts Copy](https://arxiv.org/abs/2610.03456)

**<font color=#1a73e8>作者：</font>** Minjae Chung, Clara Li, Malar Paavai Muthukumaran 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug-target affinity (DTA) prediction is widely used to prioritize candidate compounds before costly experimental screening. DTA models are often compared under a single data split, even though deployment may require extrapolation to new chemical series, new protein targets, or both. We ask whether the distribution shift used for evaluation changes which architecture appears best. We curate 718,800 unique drug-protein pairs from the ChEMBL and BindingDB datasets. We compare a Morgan-fingerprint + protein-CNN baseline with 12 controlled architectures that combine four drug representations with three ESM-2 interaction modes. Mean validation RMSE increases from 0.950 and 0.945 under scaffold and fingerprint-cluster OOD to 1.299 and 1.321 under protein-cluster and dual OOD. Model rankings are similar across the two chemical shifts (tau = 0.79), but agreement with scaffold OOD falls under protein OOD (tau = 0.39) and reverses under dual OOD (tau = -0.55). Held-out evaluation, repeated seeds, group-aware bootstrap analysis, and a size-matched control support the same conclusion: architecture selection depends on the form of extrapolation, not only on average error or training-set size. DTA benchmarks should therefore match the chemical and target shifts expected at deployment.

---


### 211. [A Near-Zero Monitor Readout Is Not Evidence of Behavioral Control](https://arxiv.org/abs/2610.03458)

**<font color=#1a73e8>作者：</font>** Zhe Zhou, Tianhua Tao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training with verifiable rewards can induce reward hacking, motivating the use of monitors within the training objective rather than solely for offline auditing. We show that a low monitor readout does not identify whether such an intervention controls behavior. In a code-generation environment whose dominant exploit is available at the start of the reasoning trace, we train policies against three monitors that pass the same offline gate: an in-domain activation probe and two penalties conditioned on how early the policy commits to its own final answer. The probe score is at its numerical floor from the first recorded training step, and the trained-score median is zero for every prefix-trained run at the endpoint. These readouts estimate different quantities, and we do not compare their scales; within each monitor family, however, low values do not establish behavioral control. Within one fixed configuration, prefix-trained runs with the same zero-median trained score range, by seed alone, from a mixed regime with a low hacking share to near-pure reward hacking. All probe runs reach the hacking regime, but their floor-level readout reflects a mismatch between the position where the probe was validated and the position where it was read during training, not a second instance of this ambiguity. Text-level analysis identifies a prefix failure mode: generic planning and filler shells postpone the exploit past the cut without eliminating it from the final output. Low measured commitment therefore does not distinguish a low hacking share from delayed commitment to the exploit. Offline discrimination and low monitor-aligned readouts are insufficient evidence of behavioral control; an out-of-band behavioral check is required. We characterize the endpoint readout, not its evolution. Code is available at this https URL.

---


### 212. [Preserving Anatomical Continuity: Three-Stage Pipeline for Colon Segmentation in 3D Abdominal CT Scans](https://arxiv.org/abs/2610.03467)

**<font color=#1a73e8>作者：</font>** Deshan Kalupahana, Sonit Singh, Praveen Ravindran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate colon segmentation from CT images is essential for colorectal disease analysis, yet deep learning based methods often produce disconnected predictions due to complex anatomy. This study introduces a three-stage, topology-preserving segmentation pipeline to address this issue. The first stage performs initial deep learning-based segmentation, followed by centreline bridging to reconnect disjoint regions and a reconstruction stage to refine continuity. Evaluations on TotalSegmentator and RAOS datasets using overlap, distance and topology-based metrics demonstrate improved structural consistency while maintaining segmentation accuracy. The proposed method enhances topological integrity, enabling more reliable colon segmentation for clinical and research applications.

---


### 213. [UniDynamics: Event-RGB Fusion for Unified Future 4D Dynamic Scene Generation](https://arxiv.org/abs/2610.03473)

**<font color=#1a73e8>作者：</font>** Daikun Liu, Xin Zhan, Teng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose UniDynamics, a diffusion-based framework for future 4D dynamic scenes (RGB, depth, and optical flow) generation from a single event-RGB pair, without requiring long histories or control priors as in existing methods, while explicitly modeling future motion fields. The core idea is to leverage event streams to offer an alternative motion prior for single-RGB extrapolation, and to enforce geometric and motion constraints throughout generation via multimodal modeling. Specifically, we design an Event Latent Enhancement (ELE) module to align and enhance event latents into diffusion-injectable conditioning features, providing robust initial motion priors and reliable texture/structure cues. We further introduce a Perceptual Dynamics Space (PDS) embedded in the multi-scale U-Net, which decouples and adaptively interacts depth and flow while continuously feeding back constraints to appearance features, improving geometric-motion consistency for physically plausible and spatiotemporally coherent prediction. Experiments on VKitti2 and DSEC demonstrate state-of-the-art performance, producing high-quality, temporally coherent, and 4D-consistent future predictions, especially under challenging high-speed motion blur.

---


### 214. [Fed-ADApt: Federated Anytime Depth Adaptation for Resource-Aware Medical Image Segmentation](https://arxiv.org/abs/2610.03474)

**<font color=#1a73e8>作者：</font>** Abhijeet Parida, Zhifan Jiang, Pooneh Roshanitabrizi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative training of medical image segmentation models without sharing raw patient data, yet existing approaches assume a homogeneous compute budget across institutions, limiting participation of low-resource sites. We propose Fed-ADApt, a depth-adaptive federated framework for UNet-based segmentation that jointly addresses low-compute training and inference. Fed-ADApt integrates multi-depth supervision with hierarchical depth-wise aggregation, allowing each site to train according to its local compute budget while contributing to a global model that supports dynamic depth selection at deployment. We evaluated Fed-ADApt on multi-site 2D retinal fundus disc segmentation and 3D brain tumor segmentation. Across both tasks, federated collaboration substantially improves robustness under domain shift. Fed-ADApt matched the full-resource FedAvg performance in 3D and achieved competitive 2D performance with a 4.7% average Dice reduction, while reducing average inference cost by 19.5% in 3D and 34.5% in 2D and substantially reducing training cost by 98% at the most constrained sites. Importantly, Fed-ADApt enables low-resource institutions that cannot train full-capacity models to participate in federations while maintaining competitive global performance under a favorable accuracy to efficiency trade-off. By considering training and inference compute budgets, Fed-ADApt provides a practical and equitable solution for federated medical image segmentation across heterogeneous clinical and edge-enabled imaging environments.

---


### 215. [Single or Multiple Policies for Phase-Structured Reinforcement Learning?](https://arxiv.org/abs/2610.03475)

**<font color=#1a73e8>作者：</font>** Guilhem Loussouarn, Nancy Nayak, Kin K. Leung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many reinforcement-learning (RL) problems are non-stationary yet structured and can be decomposed into phases, each with its own transition probabilities and reward functions. When the phase sequence is known, the common solution augments the state with information to satisfy the Markovian property and applies standard RL techniques. However, prior work finds that the multi-policy approach for different phases can outperform a single state-augmented policy shared among the phases, for reasons that remain unclear. In this work, we first show that the shared policy can theoretically achieve performance of any multi-policy solution. However, whether a multi-policy solution can perform better than the corresponding single shared policy in practice depends on function approximation, learning and optimization processes, as well as, for multi-policy solutions, the sample efficiency and loss of continuity from one policy to another. We propose a regime-based phase decomposition method to identify which policy can provide better performance. The method is based on consideration of the duration of transient system dynamics relative to the duration of the quasi-stationary period. Numerical experiments are conducted with different non-stationary RL problems to validate our four major hypotheses: (a) longer phase durations favor multi-policies, (b) the heterogeneity between phases increases the burden on single policy, (c) multi-policies need sufficient data for each phase, and (d) environment-specific transition dynamics between phases can affect which policy is preferable.

---


### 216. [Dual-Context Analog Retrieval for Time Series Forecasting](https://arxiv.org/abs/2610.03491)

**<font color=#1a73e8>作者：</font>** Jung Min Choi, Ngoc Son Le, Ibram Abdelmalak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most long-term time-series forecasting models map the look-back window directly to the full horizon in a single pass. While efficient, this design does not explicitly identify which historical states are most relevant to different future segments or exploit what followed those states. Analog forecasting addresses this by retrieving past states similar to the present and using their observed continuations, but single nearest matches can be unreliable and overlapping patches may produce redundant candidates. We propose DuoTS, a Dual-Context Time Series forecasting model that uses retrieved evidence without relying on it exclusively. DuoTS first produces a base forecast with a parallel patch encoder and linear prediction head, then progressively refines it one future patch at a time. Each refinement combines two views: a current context that attends to recent tokens and captures the latest dynamics, and a detail context that provides distinct retrieved analogs together with their subsequent trajectories. Patch-wise refinement allows the model to balance these views across the forecast horizon and associate each future segment with evidence appropriate to its temporal distance from the present. Experiments on multiple real-world datasets show that DuoTS achieves state-of-the-art performance, while ablations confirm the contribution of each context. The refinement mechanism is also model-agnostic, requiring only an encoded look-back window and the future-patch position, and can therefore be integrated into existing forecasting models.

---


### 217. [Most-Recent Anchoring with Recurrent Ordering for Time Series Forecasting](https://arxiv.org/abs/2610.03494)

**<font color=#1a73e8>作者：</font>** Jung Min Choi, Ngoc Son Le, Ibram Abdelmalak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term forecasting models commonly process all patches in a look-back window using the same fixed stack. Older contextual patches and recent evidence therefore receive the same computational depth. Yet the information closest to the forecast and the more distant context do not contribute equally. Uniform processing leaves this distinction unexpressed in the architecture. We propose MARO, a Most-Recent Anchoring with Recurrent Ordering model that processes the look-back window from the most recent patch to the oldest. The most recent patch serves as the anchor. It initializes the latent state and conditions each subsequent step, so older patches are folded into a representation that remains centered on recent evidence. A single shared module is reused at every step, so extending the scan further into the past introduces no additional parameters. Intermediate states retained during the scan allow the forecast head to weigh short and long portions of the history separately. This expresses recency through the order of recurrent refinement. Extensive experiments across multiple real-world time series datasets show that MARO achieves state-of-the-art performance on both long-term and short-term forecasting this http URL studies examine the contribution of the main architectural components.

---


### 218. [Below what training size do deep tabular generators stop beating trivial baselines? A preregistered benchmark on a size ladder of clinical and standard datasets](https://arxiv.org/abs/2610.03500)

**<font color=#1a73e8>作者：</font>** Shivam Shrivastava  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep tabular generative models are benchmarked on datasets with tens of thousands of rows; clinical datasets have hundreds. We preregistered and ran a size-ladder benchmark to find where the two regimes diverge: 8 public datasets subsampled from 200 to 20,000 training rows, seven generators (independent marginals, Gaussian copula, SMOTE, unconditional SMOTE, CTGAN, TVAE, TabDDPM) with a fixed 20-trial tuning budget and 5 evaluation seeds, plus 4 natively small clinical datasets at true size, for 2,220 committed runs in total. The primary metric is the AUROC of fixed classifiers trained on synthetic and tested on real data. In 23 of 24 (dataset, deep model) pairs no deep model ever beats the best trivial baseline by more than seed noise, at any training size we measured. The best baseline wins 40 of 49 (dataset, size) cells. Our preregistered prediction that the deep models' ranking would be unstable at small sizes is falsified: mean Kendall tau between adjacent rungs below 5,000 rows is 0.806, above our 0.8 threshold, and stability is highest at the smallest sizes rather than lowest. One caveat bounds all of this: in 81% of cells the gap between the top two methods is smaller than the variation between seeds. Finally, method rankings on natively small clinical datasets agree only moderately with rankings on subsampled large ones (mean tau 0.57 to 0.64), which questions whether a subsampled large dataset can stand in for a small one. All 2,220 result files, the preregistration and its hash, and the code that regenerates every figure and number from those files are public.

---


### 219. [Certified Mechanistic Edits: Behavioral Guarantees for Skill Removal and Preservation](https://arxiv.org/abs/2610.03502)

**<font color=#1a73e8>作者：</font>** Md Sazid Uddin, Md. Khairul Alam Mazumder, M. F. Mridha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic edits (ablations, weight edits, activation steering) are the standard tools for unlearning a harmful capability from a neural network while preserving useful ones. Current approaches validate their effects only by testing, which can never cover an entire continuous region of inputs. Prior work at the interpretability-verification boundary certifies descriptions of a model: what a circuit computes, or whether it faithfully explains the whole. We instead certify the behavioral effect of an edit: that disabling a circuit removes one skill and provably preserves another, for every input in a region; a feature non-interference guarantee in the information-flow-security sense. We demonstrate such certified edits from toy ReLU networks up to a standard softmax + LayerNorm transformer, proving removal and preservation over continuous embedding-space regions and reaching roughly 9x the input-perturbation dimension an exact solver can handle by switching to sound bound propagation. Furthermore, we prove that no finite deterministic black-box test can certify removal, exhibiting an edit that passes exhaustive testing yet provably fails on a survivor pocket that can be made arbitrarily small. Guarantees hold on small, standard-architecture networks and, like any removal claim, presuppose that the target skill admits a decidable specification, a property which real-world harms may not have.

---


### 220. [Getting Your Guidance Weights Right in diffusion and flow-matching posterior sampling](https://arxiv.org/abs/2610.03503)

**<font color=#1a73e8>作者：</font>** Liam Moroy, Jean-François Giovannelli, Yoann Altmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-free posterior sampling methods, also known as Plug-and-Play methods, leverage pretrained unconditional diffusion or flow-matching models to solve inverse problems. Most existing approaches rely on guidance weights to balance, at each time step, prior information from the unconditional score or velocity network with measurement consistency, yet the tuning of these weights is often not discussed and is largely left to heuristics. We introduce a simple and principled offline strategy for automatically tuning these guidance weights. Our key observation is that, at each time step, the conditional denoising score-matching objective for diffusion models, or the conditional flow-matching objective for flow-matching models, is a least-squares objective. Therefore, when the conditional prediction is expressed as a weighted sum of the unconditional network output and a measurement-guidance term, optimizing over these weights reduces to a two-dimensional linear least-squares problem. The resulting time-dependent guidance weights can be optimized offline for a given measurement operator, noise level and sampler at the cost of a single minibatch of sampling trajectories, without retraining or fine-tuning the pretrained generative model. Instantiated with the standard Tweedie-based measurement-consistency term, our approach improves posterior sampling and achieves state-of-the-art reconstruction performance across diffusion- and flow-matching-based methods. Moreover, the optimized guidance weights enable diffusion samplers to reduce the number of sampling steps from 1000 to 50 with no significant degradation in reconstruction quality. Code will be made available.

---


### 221. [An Automated and Reproducible Workflow for Crack Identification and Damage Assessment of Fusion Materials](https://arxiv.org/abs/2610.03505)

**<font color=#1a73e8>作者：</font>** Rinkle Juneja, Viktor Reshniak, Richard K. Archibald 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-exposure microscopy is central to qualification of fusion materials. However, manual analysis does not scale to the volume, heterogeneity, and multiresolution character of modern fusion-materials campaigns. To address this challenge, we present a reproducible workflow, implemented in the Galaxy scientific workflow environment, for automated crack identification and quantitative damage assessment from scanning electron microscopy images. The workflow processes SEM images and experimental metadata to identify cracks, quantify damage, and retain the intermediate products and processing history needed for reproducibility. Outputs include crack masks, skeletonized crack networks, quality-control visualizations, and scalar damage descriptors. The method is designed to operate without image-specific parameter tuning across tungsten grades, microstructures, magnifications, and damage states. We demonstrate the workflow on a sparse electron-beam thermal-shock dataset containing 418 images from 114 experiments spanning five tungsten grades and three microstructural states. We define a crack-density descriptor, which provides standardized inputs for downstream machine-learning prediction and physics-based crack simulation. These predictive components are exposed in the same Galaxy environment and are intentionally treated here as extensible workflow modules. The principal contribution is therefore an end-to-end, shareable, and computationally portable workflow that links experimental characterization, automated image analysis, preliminary damage prediction, and simulation-guided data acquisition for fusion-materials research.

---


### 222. [Interactive Machine Learning Interfaces for Disease Risk Prediction: Effects on Risk Perception and Behaviour](https://arxiv.org/abs/2610.03511)

**<font color=#1a73e8>作者：</font>** Tiffany Ngai, Max Homm, Matthew Bradbury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Machine learning risk models are increasingly being used in patient-facing health tools, but it remains unclear how well users understand the information these systems present. In this work, we study how people interpret an interactive Type 2 Diabetes (T2D) risk interface and whether interacting with it influences their attitudes toward behavioural change. Through an exploratory mixed-methods study with 15 participants, we compare participants' perceived understanding with their actual understanding and identify key themes from qualitative interviews. We find that participants often understood the interface better than they initially believed, but still faced important barriers related to unclear terminology, ambiguous risk framing, and limited explanations of model inputs. Finally, we propose relevant design guidelines and discuss broader issues surrounding trust and fairness. Our findings highlight the importance of intuitive visual design, familiar presentation, and clear explanations in patient-facing ML interfaces.

---


### 223. [ProgressNet: Sketching and Prompting with a Frozen Text-to-Image Model](https://arxiv.org/abs/2610.03512)

**<font color=#1a73e8>作者：</font>** Arkaprabha Basu, Chaitat Utintu, Yi-Zhe Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans draw progressively: a few strokes, a look at the result, a stroke erased, a prompt revised. Image generators do not work this way. They typically take a finished sketch and produce the image in a single pass, so every edit starts the picture again, and the models that do keep state across turns are driven by text, cannot take a stroke, and are too slow to draw with. We present ProgressNet, a training-free framework that lets a frozen text-to-image model follow a drawing session as it unfolds: strokes are added and erased, the prompt is revised, and the image keeps up at about a second per turn. It needs no new parameters because the frozen model already has what a progressive generator needs, a pathway through which the previous turn can be remembered, layers that can carry appearance forward without freezing structure, and an internal signal of how far to trust an unfinished sketch; three inference-time mechanisms (Previous-Concept Memory, Layer-Selective K/V Injection and Banded Adaptive Control) use each in turn. As a sketch fills in, every existing method degrades, the FID of the FLUX+ControlNet baseline doubling between 10% and 100% completion on FS-COCO, while ProgressNet's barely moves; it maintains strong fidelity and progressive coherence across three sketch domains and is preferred by users over five competitors, most widely on erasure.

---


### 224. [Feedforward Novel View Synthesis for Heterogeneous Cameras](https://arxiv.org/abs/2610.03522)

**<font color=#1a73e8>作者：</font>** Meng Wei, Cheng Zhang, Boying Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward novel view synthesis has recently shown promising results from sparse posed images, but most existing methods assume that context and target views share a fixed camera family. This homogeneous-camera assumption breaks in practical multi-sensor systems, where perspective, fisheye, and panoramic cameras may coexist and where the target projection may be unseen during training. We study feed-forward NVS across heterogeneous central cameras and identify a key ambiguity introduced by tokenization: a visual token aggregates a projection-dependent bundle of pixel rays, while existing camera encodings mainly expose absolute rays or token-center relations. To address this, we combine token-center relative Camera Positional Encodings and proposed local raymaps, a token-level representation that explicitly describes the intra-patch ray distribution summarized by each token. We further propose projection-aware 2D RoPE, which replaces raw image-grid coordinates with ray-induced angular coordinates so that relative positional reasoning is aligned across camera projections. Together, these components treat diverse cameras as calibrated samplings of a shared ray space rather than separate visual domains. On ScanNet++ with heterogeneous-camera system, our method improves over camera-conditioned baselines under mixed-camera evaluation and demonstrates zero-shot generalization to panoramic views.

---


### 225. [Beyond Trained Models: Compiling GNNs for a Sound Explainer Benchmark](https://arxiv.org/abs/2610.03526)

**<font color=#1a73e8>作者：</font>** Steve Azzolin, Francesco Paolo Nerini, Stefano Teso 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainers for Graph Neural Networks (GNNs) are commonly evaluated by their plausibility, i.e., how well their explanations recover a predefined ground truth, such as a motif planted in the data. This protocol implicitly assumes that a GNN trained on such data relies on the intended motif. Although prior work has questioned this assumption, plausibility remains widespread. First, we show that the assumption is violated on several widely used benchmarks, where, e.g., degree statistics alone suffice to solve the task. Then, we remove this confounder by replacing training with compilation. We achieve this by introducing $\mathsf{Gracr}$, the first compiler translating graded modal logic formulas into GNN weights, yielding models that replicate the behaviour of the corresponding formulas. Since the behaviour of the model is now known by construction, we can define its ground truth explanation formally and compute it exactly. Building on this, we introduce $\mathsf{Gracr}\mathsf{Bench}$, a benchmark of compiled GNNs for the evaluation of explainers against this exact ground truth. Experiments on eleven explainers across six tasks show its effectiveness for fine-grained diagnostic evaluation: notably, we discover that most explainers are not robust to indirect influences or alternative implementations of the same formula. These results position $\mathsf{Gracr}\mathsf{Bench}$ as a novel, rigorous evaluation setting for graph post-hoc explainability.

---


### 226. [DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation](https://arxiv.org/abs/2610.03543)

**<font color=#1a73e8>作者：</font>** Jiahao Zhan, Yan Wang, Yongrui Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video generation has benefited from distribution matching distillation (DMD), which matches the joint distribution of video frames to a video teacher's approximation of the real video distribution. Although this joint matching mitigates drift during autoregressive rollouts, limitations remain in visual quality and semantic alignment. To address these limitations, we propose DuoMatching, a distribution matching framework that approximates the real video distribution through a unified joint-marginal formulation. On top of existing joint matching formulations, the additional marginal matching objective provides dedicated frame-level supervision from an image generator, transferring complementary visual and semantic priors from it. To apply this frame-level supervision in video generation, we introduce LatentBridge to resolve the latent representation mismatch between the video student and the image teacher. Latent Variation Sampling further distributes such frame-level supervision across distinct temporal segments, reducing redundancy. Experiments demonstrate that DuoMatching improves visual quality, composition, and semantic alignment while largely preserving motion dynamics. Human evaluations show overall preference rates above 80% against all evaluated baselines. The project page is available at this https URL.

---


### 227. [Get a GRIP, this will be a long TRIP: A Quantifiable Long-Range Framework for Verifying Over-squashing](https://arxiv.org/abs/2610.03556)

**<font color=#1a73e8>作者：</font>** Ferran Hernandez Caralt, Simon Heilig, Adrián Bazaga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Empirical claims about the connection between over-squashing and long-range interactions in GNNs, can only be trusted if the benchmarks used to validate them genuinely require long-range interactions. The de-facto standard, the Long Range Graph Benchmark, has been repeatedly shown to be saturated by tuned short-range models, with existing synthetic alternatives being tied to specific topologies. As such, there is a lack of principled certificate of long-rangedness on arbitrary graphs. This state reflects the absence of a precise characterization of long-ranged benchmarks. We address this fundamental gap by introducing four verifiable axioms: Predictability, Tightness, Strictly $k$-Range, and Topology-Invariance, that any task claiming to test $k$-hop interactions must satisfy. We formally prove that violating any one of them admits failure modes that undermine conclusions drawn from the task. Based on these axioms, we introduce TRIP (Truly Ranged Interactions Problem) and its generalisation GRIP (Generally Ranged Interactions Problem), constructive procedures that turn any graph into a provably long-ranged task by drawing features from stable distributions. Moreover, by construction, GRIP admits a closed-form, per-range Maximum-Likelihood oracle that yields the first a priori per-range lower bound on test error available on any benchmark. Using our framework, we: (i) audit 4 common long-range benchmarks and identify their failures modes with respect to our axioms; (ii) on TRIP-instantiated topologies, we find a popular notion of curvature is uncorrelated with GNN performance, supporting topological-vs-computational bottleneck distinction; and (iii) we show that a novel benchmark's over-squashing measures factors beyond pure long-rangedness. Code to use the framework and reproduce experiments is released this https URL.

---


### 228. [Cephalonauts One: A deep fMRI dataset for decoding naturalistic speech in the human brain](https://arxiv.org/abs/2610.03558)

**<font color=#1a73e8>作者：</font>** Antoine Collas, Louis Jalouzot, Géraud Ilinca 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cephalonauts One is a whole-brain 3 Tesla (3T) functional magnetic resonance imaging (fMRI) dataset recorded while subjects listened to audio podcasts. Three healthy subjects underwent multiple scanning sessions, each consisting of five 15-minute runs, while listening to podcasts in their native language. With 30 hours of fMRI data per subject, the current release is the deepest available fMRI dataset using naturalistic speech stimuli. The dataset pairs brain activity with the corresponding podcast audio, transcript annotations, and derived stimulus embeddings. Furthermore, we introduce a brain decoding benchmark formulated as audio segment retrieval: given fMRI activity from a held-out session, the decoder must identify the corresponding time-aligned podcast audio segment among candidate segments. We provide standardized splits, evaluation metrics, and baseline decoders for this task. Finally, a scaling analysis shows that decoding performance improves continuously with the amount of training data per subject.

---


### 229. [A Secure dToF LiDAR SoC with Dual-Domain Fingerprinting and Event-Driven AFE Circuit Achieving Sensor-Level Attack Resilience](https://arxiv.org/abs/2610.03562)

**<font color=#1a73e8>作者：</font>** Risa Nonaka, Ryoya Matsuno, Shota Nagai 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that most commercial direct time-of-flight (dToF) LiDARs can be spoofed by injecting high-frequency laser pulses into the receiver, which can erase pedestrians from the point cloud. This paper presents the first dToF LiDAR system-on-chip (SoC) with integrated sensor-level hardware security against spoofing attacks. We propose Dual-Domain Fingerprinting (DDF), which emits laser pulse pairs whose time interval and amplitude ratio are both randomized and authenticates received echoes in this two-dimensional space, so that spoofed signals are rejected before they corrupt the ranging result. An Event-Driven AFE (ED-AFE) activates the ADC only around pulse peaks: it digitizes three samples around each peak with a triggered ADC at 1-GHz sampling and applies parabolic interpolation, achieving 1-cm distance resolution with a 99% reduction in ADC power. A time-modulated laser driver controls the laser amplitude from 10% to 100% by modulating the charge time of a laser capacitor, providing the microsecond-order amplitude modulation required by DDF. A LiDAR system with a 16-channel 65-nm CMOS prototype SoC demonstrates up to 120-m ranging and an AFE power of 3.1 mW per channel, 60% lower than prior art. In a proof-of-concept experiment in which the dual-domain authentication is applied to measured sensor data, 73% of the point cloud is protected under spoofing attack, compared with 0% without DDF.

---


### 230. [Knowledge or Calculator? Decomposing the Skill Premium in Verifiable Financial Agent Workflows](https://arxiv.org/abs/2610.03564)

**<font color=#1a73e8>作者：</font>** Jermyn Zhen Yong Bek, Zhuang Qiang Bok, Zhongtian Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial AI agents must do more than retrieve facts: investment workflows require correct quantitative execution, reliable use of procedural resources, and auditable structured outputs. We introduce FinSkillBench, an evaluation suite of 2,603 point in time episodes across 12 subtasks in portfolio construction, risk management, and fundamental analysis, with hidden regenerable ground truth and task specific deterministic verifiers. Executing 17,820 episodes across 9 models and 3 resource conditions, the paired analysis across 8 models shows that curated skill packages raise mean scores by +16.2 points (0.366 to 0.528), whereas skills generated within a single episode add only +0.5 points while consuming more tokens and turns. We then decompose the curated premium by granting human authored procedural documents and executable domain tools separately: documents alone add +5.6 points, tools alone add +19.5 points, and their combination is subadditive. The premium is strongly workflow dependent: executable tools dominate numerically intensive workflows, documentation matters more when procedural or output schema guidance is the bottleneck, and interpretive tasks benefit from both. The effects are sign stable across 10 scoring variants and cluster bootstrap analyses, and an independently implemented second harness reproduces the directional pattern while showing that effect magnitudes depend on how tools and data are exposed. Overall, a measured "skill premium" is a property of the full model, resource, and harness system rather than of the underlying model alone.

---


### 231. [Learning to Assess Heartbeat Observability for mmWave Heart-Rate Sensing](https://arxiv.org/abs/2610.03570)

**<font color=#1a73e8>作者：</font>** Yuxuan Hu, Shilin Shan, Jianfei Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contactless heart-rate sensing with millimeter-wave (mmWave) radar requires assessing whether individual measurements support reliable estimation. We study learning to assess heartbeat observability, defined as the readability of the heartbeat component in an acquired phase spectrum, for selective heart-rate estimation. Coherent superposition of scatterer returns can suppress this component even under similar macroscopic observation geometry, motivating assessment directly from acquired measurements. To obtain training supervision across different observability conditions, we develop a controllable multi-scatterer frequency-modulated continuous-wave (FMCW) simulator. Agreement between the dominant heartbeat-band peak and the known heart rate provides an automatic observability label for each simulated measurement. We propose HEAR (Heartbeat Estimation with Assessed Reliability), a compact dual-task Transformer that jointly predicts an observability score and heart rate. Its input combines spectral magnitudes with frequencies relative to the respiration fundamental, providing context for respiratory harmonics. Trained solely on simulated observations, HEAR transfers zero-shot to two public real-world datasets collected at 60 and 120 GHz from 134 subjects. The same learned score supports selective prediction with both HEAR's own heart-rate head and multiple existing estimators. On the 120 GHz dataset, score-based selection reduces the HR head's mean absolute error from 17.9 BPM at full coverage to 1.6 BPM at 50% coverage. The complete pipeline achieves an end-to-end processing latency of 50.8 ms on an edge device. Project page: this https URL.

---


### 232. [HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents](https://arxiv.org/abs/2610.03574)

**<font color=#1a73e8>作者：</font>** Alham Fikri Aji, Faiz Rizki Ramadhan, Zayd M. K. Zuhri 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce HyperBrowseComp, a multilingual and multimodal browsing benchmark comprising 423 manually authored and human-validated questions across 13 languages, written by native or highly proficient speakers. Questions are designed to be extremely challenging. Each question targets a concise, publicly verifiable answer whose discovery requires locating obscure evidence, following multi-step clue chains, or inspecting heterogeneous sources such as videos, scanned documents, images, or maps. Easier questions are filtered out by evaluating them with models without internet access to reduce the likelihood that they can be answered with parametric knowledge alone. We evaluate several models using provider-native search and a shared external retrieval harness under a common agent protocol. To contextualize model performance and effort, we also conduct a human evaluation on a sample of the questions. HyperBrowseComp provides a challenging testbed for persistent information seeking across languages and evidence modalities, with difficulty arising from discovering and connecting evidence on the open web.

---


### 233. [Rethinking What to Cache in Few-Step Diffusion Transformers: Solver-Aware Target Selection](https://arxiv.org/abs/2610.03577)

**<font color=#1a73e8>作者：</font>** Shuo Yang, Lihao Fang, Yi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) can generate high-quality images and videos, but generating each sample requires multiple costly DiT forward passes. Two common ways to accelerate DiT sampling are step distillation, which reduces the number of sampling steps, and caching, which skips some DiT evaluations by reusing a tensor computed at an earlier step. Most caching methods decide in advance which tensor to reuse. After distillation, adjacent sampling steps are farther apart. Reusing a tensor across this larger gap introduces more error, so choosing what to cache becomes especially important. We therefore introduce AutoTarget, a method that chooses the cached tensor for a given model, solver, and reuse schedule. AutoTarget uses a small set of runs without cache reuse to measure the error caused by reusing each candidate tensor, then selects the candidate with the lowest error. We also analyze how an error at one reuse step affects the final sample. For Euler sampling, we identify cache targets that produce the same trajectory and show why a stored solver update may not. Experiments on distilled image and video DiTs show that the best cache target changes with the model, image resolution, and solver. AutoTarget reduces DiT evaluations and retained cache storage. Generation quality remains close to the corresponding uncached run. On the tested PixArt-LCM and FLUX.1-schnell settings, its calibration ranking matches the ranking from held-out cached runs. To help others reproduce the method, we provide its core implementation on GitHub at this https URL.

---


### 234. [Constant-Rate Certified Deletion](https://arxiv.org/abs/2610.03590)

**<font color=#1a73e8>作者：</font>** Kai-Min Chung, Tzu-Hsiang Huang, Wei-Hsiang Hung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a unified framework for upgrading a broad class of cryptographic primitives to support constant-rate certified deletion. Previous constructions require a linear number of qubits per encrypted bit of certified-deletable plaintext. In contrast, we obtain the first constant-rate constructions in the plain model that achieve certified deletion while preserving everlasting security.
Our approach applies to a wide range of "all-or-nothing"-type primitives based on BB84-style encodings, including commitment schemes, public-key encryption, attribute-based encryption, and fully homomorphic encryption. Beyond this class, we also obtain constant-rate certified deletion for primitives built from subspace coset states, such as blind delegation, secure software leasing, functional encryption, and differing-inputs iO, and CCA-PKE. Importantly, our framework does not introduce any additional assumptions beyond those required by the underlying certified deletion primitives.
Finally, under the hardness of SIS, we show that public verifiability can be incorporated into BB84- and coset-based certified deletion. In combination with our constant-rate constructions, this yields publicly verifiable certified deletion schemes with constant rate.

---


### 235. [A Path Integral Surrogate for Multi-Step Gradient Inversion in Federated Learning](https://arxiv.org/abs/2610.03597)

**<font color=#1a73e8>作者：</font>** Agnivo Ghosh, Saumik Bhattacharya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning lets many clients train a shared model together without ever sending their private data to a central server. Each client shares only a model update, and this update should reveal far less about the client than its raw training examples would. This premise is what protects the privacy of the clients. Gradient inversion attacks challenge it directly by trying to reconstruct a client's private input images from the single update it shared. Under FedAvg, a client's update accumulates several local training steps, so the server sees only the two endpoints of a hidden weight trajectory. Recent gradient inversion attacks fit a surrogate model along the path between these two endpoints but they still read its gradient at a single point. We propose the Path-Integral Surrogate Model Extension (PI-SME) which treats the accumulated update as a path integral of the gradient field and approximates it by Gauss--Legendre quadrature over several nodes along a learnable Bézier path. On CIFAR-100 and FEMNIST images across a range of trajectory lengths and class-restricted batches PI-SME reconstructs the private inputs more faithfully than the strongest surrogate baseline on several inversion metrics and the matching loss.

---


### 236. [ManifoldSplat: Language-Guided Semantic Shape Editing of 3D Gaussian Head Avatars](https://arxiv.org/abs/2610.03599)

**<font color=#1a73e8>作者：</font>** Antonio Canela, Jordi Sànchez-Riera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity 3D head avatars have reached near-photorealistic quality. While recent methods enable text-driven manipulation, they struggle to provide fine-grained localized control, often entangling features or lacking geometric consistency. Modifying geometry through natural language currently requires slow per-prompt optimization or compromises identity and rigging. We present ManifoldSplat, the first end-toend framework for language-guided semantic shape editing of animatable 3D Gaussian Splatting avatars reconstructed from monocular videos. By performing edits within the structured FLAME manifold rather than directly optimizing an unstructured Gaussian cloud, we strictly preserve identity and animation. We introduce DeltaRegion, a per-region disentangled Conditional Variational Autoencoder (CVAE) delivering feedforward shape deltas, alongside a refining stage to recover view-consistent details. ManifoldSplat reconstructs and edits an avatar in ~90 seconds on a consumer GPU, rendering at ~800 FPS. Extensive evaluations demonstrate our approach sets a new state-of-the-art in localized prompt alignment, geometric coherence, and identity preservation. Project page and code: this https URL

---


### 237. [Mastering Atari 2600 Games with Discovered Options](https://arxiv.org/abs/2610.03604)

**<font color=#1a73e8>作者：</font>** Erik M. Lintunen, Marlos C. Machado  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal abstractions, often instantiated as options, have long been regarded as a mechanism for accelerating credit assignment, facilitating exploration, and enabling generalisation in reinforcement learning (RL). However, developing general option discovery methods that are effective in large-scale, high-dimensional domains remains a fundamental challenge. Existing option discovery methods are either confined to relatively simple domains, depend on handcrafted or quasi-symbolic representations, or offer little improvement over learning without options. We present Wayfarer, a general, domain-agnostic, online deep RL agent that discovers options through Laplacian representation learning from high-dimensional observations and leverages them for control. We show that the resulting options simultaneously improve exploration, accelerate credit assignment, and generalise effectively to unseen settings, enabling substantially faster learning of complex policies. Wayfarer achieves state-of-the-art performance among single-stream agents on the most challenging Atari 2600 games, with the largest gains in games that require long-horizon exploration and strategic behaviour, such as Montezuma's Revenge and Private Eye.

---


### 238. [Low-Cost Video--Time Priors as a Strong Baseline for EEG--fNIRS Emotion Regression on Familiar Videos](https://arxiv.org/abs/2610.03618)

**<font color=#1a73e8>作者：</font>** Minghao Kong, Jiurun Chen, Ying Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous emotion regression estimates moment-to-moment valence and arousal while a viewer watches a video. In familiar-video deployment, responses fron training participant-specific estimate, and prior-dominating fixed fusion tests whether physiology adds residual correction. In five-fold subject-held-out evaluation on 24was within 0.05 and 0.32 MAE of fusion in the internal and external evaluations, respectively. Source-explicit ablations showed that video identity and within-video tine accounted for most of the reduction, while EG-FNIRS gains were smaller and varied across participants and videos. These results identify the video-time prior as a strong, low-cost baseline and position EEG-fNIRS as an optional residual signal for familiar-video emotion regression.

---


### 239. [UniIntervene++: An Adaptive Intervention Agent for Efficient Real-World Reinforcement Learning](https://arxiv.org/abs/2610.03620)

**<font color=#1a73e8>作者：</font>** Yudong Lin, Haoyuan Deng, Zhuoxuan Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning (RL) enables robot policies to improve through physical interaction, but the assistance they require changes as their competence evolves. Existing intervention strategies based on offline estimates or fixed decision rules can therefore become mismatched to the current policy. To address this, we propose UniIntervene++, an adaptive intervention agent that learns to allocate control between autonomous execution and heterogeneous assisted behaviors during online RL. Specifically, UniIntervene++ first formulates the evolving RL policy, trajectory correction, and a task-structured CodePolicy as Options in a unified semi-Markov decision process and learns their relative values online. Building on this, competence-adaptive intervention periodically probes the RL policy through unassisted execution, keeping control allocation responsive to its evolving capability. Finally, coupled experience learning allows assisted behaviors to improve the RL policy, whose evolving outcomes in turn reshape future intervention decisions. In this way, UniIntervene++ jointly determines when to intervene, how to intervene, and when to return control as the RL policy improves. Across five real-world manipulation tasks, UniIntervene++ achieves an average success rate of 89.67%, outperforming all baselines by at least 6 percentage points, while reducing human intervention to 0.77%, a relative reduction of at least 94.6% from the best baseline. Code is available in our \href{this https URL}{GitHub repository}.

---


### 240. [FALCON: A Model and Dataset Agnostic Framework for Synthetic Data Generation for NL2SQL Pairs](https://arxiv.org/abs/2610.03625)

**<font color=#1a73e8>作者：</font>** Darian Lee, Shannon Rumsey, Jack St. Clair 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Relational databases are among the most widely deployed forms of structured knowledge, and natural language access to them requires grounding language onto schema entities and relations while handling the ambiguity inherent in how people phrase requests. Existing synthetic NL-to-SQL data generation methods largely ignore this ambiguity and produce oversimplified queries that fail to prepare models for the complexity of real-world structured knowledge access. We present FALCON, a framework that generates realistic, ambiguity-aware NL-to-SQL data matching the complexity of challenging real-world benchmarks, at low cost using compact open models. Our approach combines reserved-word SQL seeding and persona-based prompting to generate structurally complex queries, while alignment-based filtering preserves difficulty by distinguishing genuinely incorrect examples from complex but valid queries. Human evaluation confirms consistent high quality across model sizes, and our generated data exceeds existing benchmarks in both SQL complexity and natural language richness. Difficulty-stratified analysis shows models trained on FALCON data increasingly outperform baseline-trained models as query complexity increases, validating our pipeline's success in generating challenging training data. When combined with a small proportion of existing benchmark data, mixed training recovers performance on simpler queries while preserving these advantages on complex ones. The model- and database-agnostic design enables organizations to generate high-complexity NL-to-SQL training data locally without external APIs.

---


### 241. [Depth as Time in One-Step Generative Models](https://arxiv.org/abs/2610.03626)

**<font color=#1a73e8>作者：</font>** Arnold Caleb Asiimwe, William Yang, Sanghyuk Chun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The recent wave of one-step generative models, which compress the multi-step trajectory of diffusion via either distillation or learned flow maps, has reached an inflection point where they can generate high-quality images. Here, we ask a natural question that follows from these advances: what happens to the denoising trajectory of multi-step diffusion when generation is compressed into a single forward pass? We offer an empirical observation we call \textit{depth as time}: the denoising computation that multi-step diffusion performs across sampling steps appears to unfold across the depth of a single forward pass, and can be recovered by decoding intermediate layers with the model's own output head. Most interestingly, we show that this depthwise computation depends on the transport task a flow map is trained to solve. The most surprising case is MeanFlow, where probing shorter transport intervals reveals both denoising and renoising within a single network evaluation. In contrast, generators trained without a time-indexed transport task, such as drifting models, do not exhibit the same depthwise denoising. Consequently, we show that models that exhibit the depthwise denoising phenomenon are more compressible across the layerwise computation: a MeanFlow \texttt{SiT-L/2} model can be compressed by $16.6\times$ in parameters into a single time-conditioned block. We offer an explanation for this denoise-then-renoise behavior and show that, when we treat the layerwise computation explicitly as a flow, a single time-conditioned block can be trained to denoise across layers, compressing a MeanFlow \texttt{SiT-L/2} model by $16.6\times$ in parameters. Together, these results suggest that the temporal computation of diffusion is not eliminated by one-step generation, but reorganized across network depth.

---


### 242. [Credit Where It Matters: Dependency-Aware Policy Optimization for Terminal Agents](https://arxiv.org/abs/2610.03634)

**<font color=#1a73e8>作者：</font>** Yu Li, Guangfeng Cai, Long-Fei Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Terminal-using agents benefit from reinforcement learning (RL) in coding, debugging, and other multi-step terminal tasks. In these tasks, later commands often depend on information or intermediate results produced by earlier commands. However, existing trajectory-level and step-level credit assignment methods do not explicitly trace the read-write dependencies through which commands affect the final outcome. Consequently, training signals could still be assigned to irrelevant operations, weakening learning from relevant steps. In this paper, we propose Dependency-Aware Group Policy Optimization (DepGPO), which uses execution dependencies between commands to guide credit assignment for terminal agents. Specifically, we construct a command dependency graph from execution traces and trace backward from the resources inspected by the task verifier. We then assign credit to relevant writes and their supporting reads along these paths, and use it to redistribute trajectory advantages across steps. Extensive comparative experiments and ablation studies demonstrate that DepGPO improves task performance and training stability on complex terminal tasks.

---


### 243. [LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation](https://arxiv.org/abs/2610.03636)

**<font color=#1a73e8>作者：</font>** Ziqi Ma, Shreya Sharma, Mohamed El Banani 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-controlled video models are rapidly advancing toward long generation horizons and complex camera control. A key failure mode is 3D inconsistency: as the camera moves, objects lose permanence and scene structures shift. Existing post-training techniques, which assign a single scalar reward to the entire generation, are poorly suited to correcting these inconsistencies over long horizons. We introduce LoGo, which blends global and spatially localized rewards for camera-controlled video models. The local reward provides fine-grained credit assignment, which substantially improves 3D consistency, while the global reward preserves camera following and video quality. Across three base models, LoGo shows a clear advantage on DL3DV and TrajectoryBench, a new benchmark for long-horizon, complex-camera-control generation that current evaluations lack. LoGo effectively reduces local object shifts, artifacts, and global scene changes, illustrating the importance of credit assignment in post-training video models. Project website: this https URL

---


### 244. [Broken scale symmetries in undercomplete linear autoencoders](https://arxiv.org/abs/2610.03640)

**<font color=#1a73e8>作者：</font>** Farhad Pashakhanloo, Jacob A. Zavatone-Veth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network loss landscapes have many symmetries, which are preserved by gradient flow but broken by finite-stepsize stochastic gradient descent (SGD). A canonical example of such a symmetry is scale in homogeneous networks: one can scale up the parameters in one layer and down in the next without changing the network output. Previous work has documented cases in which SGD breaks this symmetry in favor of balancing gradient noise or minimizing fluctuations. Here, we show that the solution geometry of undercomplete linear autoencoders instead selects a preferred sign for scale drift: on the PCA solution manifold, SGD favors large decoder weights. This directed scale drift occurs on a slow timescale, and its dynamics admit an analytically-tractable effective description. However, it cannot continue indefinitely: increasing scale eventually drives the dynamics towards a finite-stepsize stability boundary. The resulting solutions are sharper than a balanced baseline in the sense of the maximum eigenvalue of the loss Hessian, but different sharpness measures can move in opposing directions. Thus, undercomplete autoencoders give a concrete illustration of how loss geometry can convert residual gradient noise into directed motion along a manifold of functionally-equivalent solutions.

---


### 245. [IDRF: Inverse-Distilled Reward Fine-tuning of Masked Discrete Diffusion Models](https://arxiv.org/abs/2610.03641)

**<font color=#1a73e8>作者：</font>** Vladislav Gromadskii, David Li, Samson Gourevitch 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked discrete diffusion models offer a promising alternative to autoregressive generation, but iterative sampling can be costly, and intractable sequence likelihoods complicate reward fine-tuning. We introduce IDRF, a framework for reward fine-tuning of few-step masked discrete diffusion generators. Starting from a standard reverse-KL-regularized objective, IDRF replaces the intractable sequence-level KL penalty with inverse-distillation regularization. With an optimal auxiliary denoiser, we prove that the population inverse-distillation loss upper-bounds the sequence-level KL divergence to the reference distribution. IDRF optimizes a trajectory-based surrogate of this loss without reference-model rollouts, so the student keeps its own few-step sampler. We view few-step generation as a finite-horizon Markov decision process and optimize reward with a clipped policy-gradient objective over the student's trajectories. Across DNA, image, and text generation, IDRF achieves high reward with up to $32\times$ fewer denoising steps than the reference while mitigating reward hacking and preserving sample quality.

---


### 246. [On the Convergence of Success Conditioning for Policy Optimization](https://arxiv.org/abs/2610.03642)

**<font color=#1a73e8>作者：</font>** Matthew Brun, Xu Andy Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Success conditioning is a strategy for improving decision-making policies in stochastic environments; it updates a policy by increasing the probability of taking actions that yield successful outcomes. Success conditioning is common to many reinforcement learning applications, yet its limiting behavior and convergence rates are not well understood. In this work, we demonstrate that success conditioning converges to an optimal policy on a broad class of Markov decision processes (MDPs). We also derive convergence rates in some common settings. For discounted MDPs, we prove convergence within $\mathcal{O}(1/\varepsilon^p)$ iterations to an $\varepsilon$-optimal policy, where the exponent $p$ depends on problem data. For single-period MDPs, such a policy is obtained within $\mathcal{O}(\log(1/\varepsilon))$ iterations.

---


### 247. [When May a Bandit Leave Its Anchor? E-Process-Authorized Thompson Sampling under Non-stationarity](https://arxiv.org/abs/2610.03646)

**<font color=#1a73e8>作者：</font>** Mayand Gulati, Kerong Wang, WeiChen Au  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stationarity rewards memory, but after a change the same history can mislead. We ask when forgetting should be permitted. E-process-authorized Thompson sampling (e-ATS) gives each arm full-history and discounted Beta states. An anytime-valid e-process first authorizes the discounted state, then a reversible relevance score controls its influence. Before authorization, e-ATS exactly follows optimistic Thompson sampling (OTS). Under a Beta-Bernoulli prior-predictive stationary model, e-ATS's probability of ever departing from OTS is at most the chosen $\alpha_E$, without fitted thresholds. Relative to e-ATS, removing authorization increased mean normalized dynamic pseudo-regret by $38.4\%$ on the registered suite but reduced it by $7.5\%$ on the literature-derived replay suite. Therefore, evidence controls when adaptation begins, not whether it always helps.

---


### 248. [On-Board Anomaly Detection for Efficient Marine Environmental Monitoring](https://arxiv.org/abs/2610.03649)

**<font color=#1a73e8>作者：</font>** Thomas Goudemant, Clotilde Szywala, Benjamin Francesconi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Marine ecosystems are impacted by various threats such as oil spills, algal blooms, and sediment floods, which disrupt habitats, wildlife, and human activities. Advances in satellite imagery and Artificial Intelligence (AI) have enhanced our capabilities for early detection and mitigation of such hazards. In this paper, we propose a marine event detection pipeline for Earth observation satellites equipped with multi- or hyperspectral sensors. Our approach includes a self-supervised neural network encoder that compresses satellite images into a reduced latent space, enabling efficient onboard processing. A machine learning anomaly detection model identifies deviations from normal sea patterns to detect environmental anomalies. We compare its performance against traditional algorithms such as Isolation Forest, One-Class Support Vector Machine and Local Outlier Factors. Our lightweight, resource-efficient pipeline is optimized for deployment on satellites with limited computational resources, ranging from embedded CPUs to AI hardware accelerators. By prioritizing the transmission of critical information, our solution enhances system responsiveness and optimizes satellite communication bandwidth. Demonstrated through current integration across multiple missions, including European Space Agency's (ESA) Phisat-2 mission and Microsoft/Thales Alenia Space IMAGIN-e mission, our pipeline aims to improve marine environmental monitoring by providing timely alerts and efficient data reduction.

---


### 249. [PoCoFL: POlicy-COmpliant Federated Learning](https://arxiv.org/abs/2610.03650)

**<font color=#1a73e8>作者：</font>** Dominik Roy George, Varesh Mishra, Aysajan Abidin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) is a privacy-oriented learning paradigm that enables collaborative model training while keeping training data local to participating clients. However, it does not guarantee that clients submit policy-compliant contributions or that aggregators process admitted contributions correctly. Existing verifiable FL systems tailor validation rules to specific FL settings, learning workflows, and cryptographic constructions, limiting their applicability across network topologies, participant roles, and aggregation semantics. In this paper, we present PoCoFL, a policy-compliant federated learning framework that separates three aspects: (i) FL type, (ii) policy semantics, and (iii) cryptographic realisation. We provide a formalisation that captures client and aggregation requirements as policy-dependent relations. Clients prove compliance of their contributions using commitments and non-interactive zero-knowledge proofs, while aggregators prove that the recorded set of admitted contributions was processed according to the selected aggregation policy. We demonstrate PoCoFL through four formal instantiations: (i) vanilla, (ii) continual, (iii) personalised, and (iv) threshold-encrypted federated learning. We evaluate the effects of policy enforcement on the learning objectives of vanilla, personalised, and continual FL. We further implement proof-of-concept realisations of all four instantiations, demonstrating the versatility and practical feasibility of PoCoFL. Overall, these results show that PoCoFL can capture complex policy representations while remaining network-topology agnostic.

---


### 250. [MRVQ: One Resident Index for Dimension- and Rate-Elastic Vector Search](https://arxiv.org/abs/2610.03651)

**<font color=#1a73e8>作者：</font>** Sean Culatana, Shang-En Huang, Kang Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dense-retrieval services must switch among embedding-prefix dimensions and index bit rates as latency, quality, and memory budgets change. Tuning a quantizer separately for each rate gives the best quality, but the retrieval tier then holds several code streams and quantizer states at once. We introduce Matryoshka Residual Vector Quantization (MRVQ), a post-hoc residual quantizer for frozen embeddings. Its maximum-rate code can be truncated two ways: dropping residual stages lowers the rate, and dropping embedding coordinates lowers the dimension. One resident artifact therefore serves every (dimension, rate) pair we evaluate. Across FiQA and NFCorpus, four embedding families, and {4, 8, 16}-byte codes, MRVQ is the lowest-RAM design we evaluate. It uses 17.8-22.0x less memory than three separately trained QINCo2 indices, and 1.89-2.02x less than a lean shared-model steelman. The saving is not free: per-rate QINCo2 is 0.026-0.107 nDCG@10 better on FiQA. But MRVQ beats PQ, OPQ, and AdANNS-OPQ at matched code size. We also evaluate a low-build-cost PCA-scalar design that attains quality comparable to RaBitQ and its extension while fitting 420x faster at the median. Finally, we report two negative results: QINCo2 collapses when trained at high rates, and a ranking-bound hypothesis misses its pre-specified acceptance criteria. MRVQ is therefore a low-memory operating point for elastic retrieval, not a universal quality winner.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-260](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
