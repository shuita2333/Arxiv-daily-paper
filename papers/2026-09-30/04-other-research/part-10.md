# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 451. [Printability-Constrained Adversarial Decals for Near-Nadir Aerial Perception: Measured Ink Gamuts, Nested Realism Constraints, and a Physical-World Bound](https://arxiv.org/abs/2609.33513)

**<font color=#1a73e8>作者：</font>** Sandesh Shrestha, K. T. Yasas Mahima, Asanka G. Perera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial patches for aerial perception are typically evaluated as digital composites, with printing left as an implementation detail. This study imposes three physical constraints during optimization rather than after it: the color range a particular printer can reproduce, the size of the flat panel a vehicle offers, and the loss of fine detail incurred when the patch is imaged from altitude. The principal comparison isolates the ink set. Two patches share all seventeen recorded optimization settings and differ only in the colors available to them. One is constrained to a uniform color cube; the other to a gamut measured by printing and scanning a 216-patch chart. Each was optimized at three seeds and evaluated against thirteen victim conditions, with every rate reported against a size-matched optimized control. The effect of the measured gamut is victim-dependent rather than uniform. Net attack success rises on three of six closed-set segmentation victims, and for these the seed ranges of the two ink sets are disjoint: $+0.120$ on DeepLabv3-R101 and $+0.041$ on SegFormer-B0. The color-cube patch is consistently stronger on the open-vocabulary segmenter and on two of four detectors, though no detector exceeds a net of $+0.026$ under either ink set. The natural explanation is that a printable palette is simply less chromatic and lower in frequency than a digital one. Eleven further patches test this account and it does not hold. Once cardinality is matched, a palette as chromatic as the cube attacks equally well. Cardinality itself shows no trend from three inks to thirty-two. Palettes matched on cardinality, lightness and chroma, and differing only in hue placement, span $0.035$ to $0.136$. A physical evaluation with printed decals did not detect transfer; it bounds the transferred rate at $0.133$, which does not exclude the simulated value of $0.121$.

---


### 452. [SLP-ProbHard: Probabilistic Hard-Constrained Learning via Structural Latent Parameterization](https://arxiv.org/abs/2609.33515)

**<font color=#1a73e8>作者：</font>** Wondesen Teshome Bekele, Marco D'Oria  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many probabilistic predictors must satisfy exact structure in every stochastic realization, yet common hard-constraint approaches form predictions in ambient coordinates and then correct or project them. We introduce SLP-ProbHard, a cross-family, representation-centered framework for probabilistic hard-constrained learning when explicit structural parameterizations are available. Its core object, a Structural Feasible Latent Parameterization (SFLP), combines a structural latent law $Z \sim P^Z_\theta(\cdot\mid x)$ with a feasible map $Y=h_\phi(x,Z)$ that satisfies the constraint for every latent realization. Together these components define the predictive law itself, including its support and boundary probabilities, rather than serving as a final feasibility wrapper. We study how feasible coordinates and maps affect stochastic dimension, dependence, calibration, expressiveness, and computation. Experiments use Gaussian latent laws and fixed geometry-derived maps across affine equalities, ordering and simplex constraints, nonlinear manifolds, and three structural representations of seven-basin hydrological flow-duration-curve (FDC) data. In an official-source affine comparison with ProbHardE2E/DPPL, both methods achieve zero practical constraint violations. SLP-ProbHard uses 8 instead of 11 stochastic coordinates and improves MSE/MAE, while DPPL yields better marginal CRPS and closer-to-nominal coverage; a paired test detects no Energy Score difference across ten seeds. Real-world affine and nonlinear FDC representations reduce 13 to 7 and 14 to 8 ambient versus computational coordinates, respectively. Exact feasibility alone thus does not determine a predictive law, motivating direct structural generation when meaningful feasible coordinates are available.

---


### 453. [Anatomy-Structured Hierarchical MIL for Weakly-Supervised Thoracic Disease Detection in Chest X-rays](https://arxiv.org/abs/2609.33520)

**<font color=#1a73e8>作者：</font>** Jeongin Kim, Sohyun Ahn, Seo Young Kang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly-supervised thoracic disease detection in chest X-rays (CXR) is challenging due to subtle appearances and complex anatomical overlap, motivating anatomy-aware modeling for improved localization. However, prior anatomy-aware methods typically rely on coarse region proxies or static spatial priors, which may restrict dynamic instance discovery and limit precise localization of small abnormalities. We propose Anatomy-Structured Hierarchical Multiple Instance Learning (ASH-MIL), a framework that introduces parallel anatomy-structured observation branches (cardiac, pulmonary, and agnostic) combined with hierarchical MIL aggregation. Anatomical priors are injected as soft spatial biases into decoder cross-attention, enabling anatomically grounded evidence maps without disease bounding-box supervision. Instance localization is derived directly from MIL-weighted cross-attention maps without bounding box supervision. Experiments on CXR8 and cross-domain MIMIC-CXR held-out sets demonstrate consistent improvements over prior weakly-supervised and anatomy-aware approaches, particularly under stricter localization criteria. Our code is available at this https URL.

---


### 454. [In-Token Learning for High-Fidelity Image Restoration via Diffusion Transformers](https://arxiv.org/abs/2609.33523)

**<font color=#1a73e8>作者：</font>** Xingfu Yi, Xiaoxue Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present In-Token Learning, an image restoration framework that adapts a pretrained diffusion transformer using conditional rectified flow matching. Clean targets paired with degraded inputs supervise transport from Gaussian noise to restored images. Spatially aligned degraded-image tokens are fused with evolving latent tokens along the channel dimension, preserving the image-token count at a given resolution. Direct Low-Quality Guidance (DLG) combines frozen degraded-image embeddings with a fixed task prompt through the native conditioning pathway, without a trainable ControlNet-style branch or image captioning. We evaluate super-resolution and denoising on DIV2K, LSDIR, FFHQ, RealLQ250, and RealPhoto60, and automatic colorization on DIV2K and LSDIR. The tasks use separately trained checkpoints under the same framework. Results show competitive fidelity and perceptual quality under the evaluated protocols, with weaker generalization on RealLQ250. We report full-image QHD ($2560{\times}1440$) inference and a tiled $12$K restoration demonstration of Along the River During the Qingming Festival. Attention cost still increases with resolution. This technical report preserves the early broader study underlying Fill2SR, which subsequently developed the real-world super-resolution direction.

---


### 455. [EverMine: Dissecting the Self-Evolution of Research Capabilities in Long-Horizon Alpha Research](https://arxiv.org/abs/2609.33524)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Jiangfeng Zhang, Rui Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents aim to turn research feedback into reusable skills, tools, and research rules. Whether these accumulated capabilities continue to improve later research requires controlled evaluation. Long-horizon alpha discovery provides a state-dependent setting: once a new factor enters the portfolio, the predictive information already covered changes, so the value of the same candidate or experience may change over time. We introduce EverMine, an empirical framework for studying self-evolving research capabilities in long-horizon alpha discovery. EverMine decomposes the research state into history (Hist), the current factor portfolio (Frontier), and reusable capabilities (Cap). Under matched resource limits, we compare complete runs with fixed or evolving Cap, and replace Cap while holding Hist and Frontier fixed to estimate the conditional value of accumulated capabilities. We also combine full trajectories with historical-state replay to examine how experience-based decisions affect candidate selection and portfolio outcomes. Across 18 long-horizon trajectories, end-to-end comparisons show no consistent gain from Cap evolution. Across 48 continuation branches from shared Hist and Frontier states, accumulated Cap also does not consistently outperform the initial Cap. Parameter tuning of existing factor structures can still improve the portfolio. In an exploratory replay of two screening batches from one Evolving trajectory, some screened-out candidates have positive marginal value at the original state, yet submitting all screened-out candidates sequentially slightly lowers final portfolio IC in both batches. These results show that candidate value depends on the evolving portfolio and submission order, and motivate evaluating self-evolving research capabilities through end-to-end outcomes, conditional capability value, and the consequences of experience-based decisions.

---


### 456. [Discovering Symmetries in Neural Network Parameter Spaces](https://arxiv.org/abs/2609.33527)

**<font color=#1a73e8>作者：</font>** Bo Zhao, Nima Dehmamy, Robin Walters 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter space symmetries are important for understanding neural networks' loss landscape, training dynamics, and generalization. However, systematically identifying these symmetries remains a challenge. In this paper, we formalize data-dependent parameter symmetries and characterize loss invariance and the group-action axioms through infinitesimal conditions, which provide objectives for jointly learning group generators and nonlinear action maps. Our framework systematically uncovers parameter symmetries, including previously unknown ones. To study larger networks, we establish conditions under which subnetwork symmetries extend to the full model. The same construction gives an explicit family of finite-batch symmetries, providing both analytical examples and a foundation for discovery through small subnetworks. Using the infinitesimal characterization and subnetwork construction, we implement a framework for automated discovery of parameter symmetries, and successfully uncovered symmetries in various architectures, including pretrained transformer models.

---


### 457. [Where the Numbers Come From: Auditing Evaluation in Provenance-Based Intrusion Detection](https://arxiv.org/abs/2609.33532)

**<font color=#1a73e8>作者：</font>** Jihwan Moon, Gunhee Kim, Myeongjang Pyeon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reproducing a provenance-based intrusion detector's score does not establish what that score says about its emitted alarms or the information its encoder uses. We audit nine released implementations, execute four detectors using their own code, and isolate three measurement effects. First, a fixed-alert comparison separates label choice from neighbourhood credit: ThreaTrace reports precision 0.938 with neighbourhood credit, although only seven of its 994 alarms carry its own attack label. Second, removing test-label checkpoint selection lowers attack detection precision (ADP) by 0.16 to 0.33 across four forty-member word2vec configurations without changing detector order. Third, a buffer-reuse defect gives a linear encoder unintended degree-dependent inputs. Correcting it lowers type-only ADP in every identical-input initialization pair on two hosts, while historical word2vec effects depend on the host. These findings qualify claims from the inspected implementations about alarm precision, performance magnitude and static-attribute sufficiency. STRICT connects them to six checkable reporting requirements. Because the comparisons condition on benchmark targets, they neither validate those labels nor establish a universal detector ranking.

---


### 458. [PGL-3D: Towards Progressive Geometric Learning for 3D Visual Query Localization](https://arxiv.org/abs/2609.33558)

**<font color=#1a73e8>作者：</font>** Liang Peng, Shizhuo Mu, Bohan Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Visual Query Localization (3DVQL) retrieves the latest contiguous occurrence of a queried object in an RGB--point-cloud sequence and predicts a 9-DoF cuboid for every response frame. The query is captured independently of the search sequence, so its annotated pose may differ from how the object appears in the search frames. The benchmark baseline predicts cuboids after feature modeling, leaving their geometry unused for subsequent feature refinement. We investigate whether complete intermediate cuboids can improve query and proposal representations before final decoding. We introduce Progressive Geometric Learning for 3DVQL (PGL-3D), a predict--select--refine--re-predict framework that uses intermediate cuboids to guide the aggregation of search evidence and update query and proposal representations. A shared head first predicts a complete cuboid for every proposal. Query--Tube--Memory (QTM) then selects reference observations by combining proposal association, cuboid quality, frame response, and target absence, since association confidence alone establishes neither target presence nor geometric accuracy. The center, size, and orientation of each selected cuboid define soft pooling weights over query-conditioned proposal features. The pooled memory updates the query and proposal representations, and the head re-predicts from the updated features. A training-only objective, ST-D9O, supervises cuboid geometry at every stage by adding boundary, signed-distance, and soft-overlap terms to parameter regression. PGL-3D achieves a mean stAP of $0.270 \pm 0.004$ on 3DVQL, compared with $0.044$ reported for LaF. Ablations support the benefits of geometry-guided feature updates, while stage-wise analyses show improved cuboid accuracy. Replacing the geometry objective in our PROT3D reproduction with ST-D9O improves mAO on GSOT3D from $21.63\%$ to $25.78\%$. Our code and models will be released.

---


### 459. [GraphSelect for Budgeted Representation Selection in Multimodal Graph Inference](https://arxiv.org/abs/2609.33561)

**<font color=#1a73e8>作者：</font>** Xu Wang, Xunkai Li, Yinlin Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal graph predictors combine text, images, and relations to classify connected entities. How much of this input is needed to preserve their predictions? We study budgeted representation selection, which chooses a subset of candidate text and image vectors under a separate capacity for each modality. Predictions from the complete candidate input define the classes to preserve. The challenge is that a representation's contribution depends on the other selected inputs, while graph propagation extends its effects across nodes. Our empirical study shows that candidate rankings change with the selected input, while predicted probabilities remain informative after the class stops changing. Updating scores improves selection, and exchanging inputs can improve a subset whose capacity is already filled. These findings lead to GraphSelect, which starts from individual candidate gains and refines the subset through jointly evaluated exchanges. It screens promising removals and additions, accepts an exchange when it reduces the prediction loss, and updates the scores. Experiments on six graphs show higher mean objective recovery than six attribution and explanation methods adapted to the selection task. Across nine trained architectures on two graphs, retaining 20% of the candidate representations per modality gives a mean accuracy drop of 0.10 percentage points relative to full candidate input, preserving classification performance with substantially fewer text and image representations.

---


### 460. [OOD Generalization as a Bifurcation Problem](https://arxiv.org/abs/2609.33562)

**<font color=#1a73e8>作者：</font>** Nguyen-Thanh-Luong Doan, Quang-Vu Nguyen, Tang-Phu-Quy Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Systematic out-of-distribution (OOD) generation remains a critical bottleneck for continuous-time generative models. While standard joint classifier-free guidance (CFG) routinely fails to synthesize unobserved concept combinations, exact decomposed scoring generalizes robustly at the cost of severe computational overhead. In this work, we reveal that compositional binding is not a uniform process but a highly localized phase transition. We identify the semantic bifurcation window - the precise temporal interval where joint and decomposed vector fields meaningfully diverge. Exploiting this dynamic, we propose surgical guidance, a hybrid sampling strategy that restricts exact multi-pass scoring strictly to this critical window. On an OOD bi-digit MNIST testbed, surgical guidance achieves state-of-the-art compositional fidelity at a fraction of the inference cost, yielding a +5.3% absolute improvement in pairwise accuracy over the joint baseline by intervening during just the first 15% of the diffusion trajectory. Furthermore, our empirical analysis uncovers a fundamental topological divide: diffusion models (SDEs) force conceptual resolution immediately at peak noise, whereas Conditional Flow Matching (ODEs) delays structural binding until intermediate features emerge, establishing a new temporal framework for accelerating large-scale generative decoding.

---


### 461. [MA-JEPA: Joint-Embedding World Models for Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.33563)

**<font color=#1a73e8>作者：</font>** Brandon Gary Kaplowitz, Osaze James Obahor, Christian Schroeder de Witt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models improve sample efficiency by training policies on imagined trajectories, but their usefulness depends on learning representations that capture the information needed for future control. We study whether self-supervised joint-embedding prediction (JEPA) can provide this learning signal for multi-agent reinforcement learning. We introduce MA-JEPA, a stochastic world model that replaces observation reconstruction with prediction of target representations, enabling model-based multi-agent reinforcement learning with centralized training and decentralized execution. A categorical latent state and a causal Transformer are trained with posterior and action-conditioned dynamics prediction objectives and are then used for actor-critic learning from latent imagination. A training-only joint predictor conditions on all agents' local states and actions to predict each agent's next local observation embedding. These predictions are passed through the same local posterior used during real interaction with a centralized critic that is used only for value learning, with execution remaining decentralized. Our experiments show that this architecture performs strongly on SMAC, matching or exceeding the strongest reported comparator mean win rate on four of eight evaluated maps.

---


### 462. [Dr. Free: You Don't Need Difficulty Rewards for Self-Evolving Search Agents](https://arxiv.org/abs/2609.33565)

**<font color=#1a73e8>作者：</font>** Zhipeng Qian, Zihan Liang, Yufei Ma 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central limitation of current data-free self-evolution methods for training search agents is their reliance on difficulty-based proposer rewards. These methods reward a proposer for generating questions that challenge a co-evolving solver, using solver difficulty as a proxy for question quality. Yet difficulty alone is insufficient to distinguish questions that require cross-passage evidence from those that are answerable via simpler shortcuts. In addition, measuring difficulty demands repeated solver rollouts for every candidate question, leading to substantial computational costs. In this paper, we introduce \methodname, the first self-evolving search framework that eliminates difficulty-based proposer rewards and directly optimizes for evidence necessity relative to shortcut contexts. Dr. Free samples relational chains from a knowledge graph and pairs them with aligned passages, giving question generation an explicit multi-hop structure. A generated question receives a positive information-gain reward only when the likelihood of the target answer under the complete evidence passages exceeds the maximum likelihood under all evaluated shortcut contexts. Because this signal is computed from teacher-forced likelihoods, it removes the need for pass-rate estimation and reduces proposer training time by over $7\times$. Experiments on seven open-domain QA benchmarks show that Dr. Free outperforms prior data-free search agents and the supervised baseline, with large improvements on multi-hop QA benchmarks.

---


### 463. [Correct then Forecast: Observer State-Space Models for Time Series Forecasting](https://arxiv.org/abs/2609.33566)

**<font color=#1a73e8>作者：</font>** Alexis-Raja Brachet, Guillaume Clavier--Frémond, Abdelhakim Ziani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting requires extrapolating the dynamics of an observed process beyond the last available measurement. Yet recurrent forecasting models typically treat observations as inputs that directly control their latent dynamics. It leads to a regime change when these observations become unavailable at prediction time. Following a state-estimation perspective, we introduce Observer State-Space Models (OSSMs), a class of recurrent models that interprets the observed input time series as measurements of an underlying autonomous dynamical system. OSSMs explicitly separate latent-state propagation from measurement assimilation: a single transition governs the dynamics across both context and forecasting intervals, while available observations correct the estimated state through an observer. This formulation naturally exposes classical control-theoretic properties, including observability and convergence of the state estimation error. We further show that conventional and recent SSMs can be recovered as particular instances of our OSSM framework, thereby providing a unified interpretation of their recurrent dynamics and revealing modeling inconsistencies. We perform experiments across several benchmarks showing that OSSM achieves substantial improvements while maintaining the same parameter count and training setup as the corresponding SSM baseline. These results support a simple principle for recurrent forecasting: observations should correct the estimated latent state, rather than control the dynamics used to propagate it.

---


### 464. [Information Blackhole: Exploring Backdoor Mechanism in 3D Point Cloud Reconstruction](https://arxiv.org/abs/2609.33569)

**<font color=#1a73e8>作者：</font>** Zhifei Yang, Xiuping Liu, Kuofeng Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Point cloud autoencoders are fundamental components for 3D world representation and support many safety-critical downstream applications. Existing studies have extensively investigated backdoor attacks on point cloud classification, whereas backdoor attacks against point cloud autoencoders remain largely unexplored. However, their backdoor behaviors differ substantially due to the intrinsic structural gap between discriminative and generative models. Specifically, a classifier is a discriminative model that separately fits the marginal distributions of benign and malicious data. In contrast, the generative nature of an autoencoder entangles the two within a unified latent distribution, leading to information crosstalk and reduced attack controllability. In this setting, residual source geometric information in malicious data may leak into the clean inference branch, causing the reconstruction to collapse toward the source data. We then propose the Information Blackhole principle, which introduces Gaussian distribution constraints to disentangle latent representations and block interfering information. Building on this principle, we further propose Adaptive Gaussian Matching (AGM), which explicitly regularizes the latent distribution of poisoned samples. By suppressing the propagation of source geometric information from poisoned features to the attacker-specified reconstruction target, AGM improves attack controllability. Extensive quantitative and qualitative experiments on ModelNet and ShapeNetPart demonstrate that the proposed framework improves the attack performance of several standard triggers and reveals the unique operating mechanisms of backdoor attacks against point cloud autoencoders.

---


### 465. [Compressing Value Predictions for Learning-Augmented Metrical Task Systems](https://arxiv.org/abs/2609.33580)

**<font color=#1a73e8>作者：</font>** Sizhe Li, Yecheng Li, Kun He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-augmented algorithms for metrical task systems (MTS) can exploit predictions of canonical dual values, but existing formulations typically require a prediction for every state. We study whether these predictions can be compressed to a small set of representative states while retaining their algorithmic value. We introduce landmark-compressed value predictions, in which the predictor reports predicted dual values only at $m$ landmarks and the remaining values are reconstructed by a Lipschitz extension. Our algorithm achieves additive excess cost $O(T\,r(L) + \sum_t \delta_t)$, where $r(L)$ is the covering radius of the landmarks and $\delta_t$ measures prediction error up to additive shifts; local and value-dependent bounds refine this guarantee. For sparse landmark sets on unit-spaced finite lines, we prove a matching $\Omega(T r_m)$ lower bound for every randomized algorithm using fixed landmarks, even with advance access to their entire exact absolute-value table. The prediction interface also matters: on two states with one landmark, exact absolute values permit horizon-independent excess, whereas exact relative values force worst-case expected excess linear in $T$. We give PAC guarantees for learning compressed prediction tables, with efficient empirical-risk minimization for fixed landmarks. Our results connect metric coverage, prediction interfaces, and learning guarantees for compressed predictions in online MTS.

---


### 466. [ForeFly: A Dual-Horizon World Action Model for Aerial Vision-Language Navigation](https://arxiv.org/abs/2609.33581)

**<font color=#1a73e8>作者：</font>** Kunhui Wang, Xintong Zhang, Junyu Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial Vision-Language Navigation (AVLN) requires UAVs to maintain reliable instruction following over long trajectories in complex 3D environments. However, existing AVLN approaches are predominantly reactive or limited to single-horizon prediction, overlooking complementary future cues across different temporal horizons. To address this limitation, we propose ForeFly, a dual-horizon latent world action model that predicts both a proximal future for local continuity and an adaptive route-critical future for long-range guidance. Horizon-specific foresight queries are primed with recent and route-critical visual memories, providing history-aware context for future prediction. To exploit their distinct roles in action generation, we introduce Foresight-Guided Action Refinement (FGAR), which asymmetrically exploits proximal foresight for local action enhancement and route-critical foresight for feature-wise correction and route-level guidance. Experiments on the TravelUAV and UAV-ON benchmarks show that ForeFly consistently outperforms strong baselines across seen and unseen settings, validating the effectiveness of dual-horizon foresight and FGAR learning. The code is available at: this https URL

---


### 467. [Fill2SR: Repurposing Inpainting Diffusion Transformers for Real-World Super-Resolution](https://arxiv.org/abs/2609.33582)

**<font color=#1a73e8>作者：</font>** Xingfu Yi, Xiaoxue Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent real-world image super-resolution (SR) methods often adapt text-to-image (T2I) backbones with ControlNet-style branches or spatial conditioning tokens, which increases memory and computes with resolution and often constrains training to a fixed scale. We propose Fill2SR, which repurposes a masked-inpainting Diffusion Transformer for SR without extra spatial branches. Our Inpainting-Interface Evidence Adapter (IIEA) writes the low-quality (LQ) observation into the native masked-image slot under a full-image mask, turning inpainting into a reverse-degradation conditional rectified flow trained with LoRA-only tuning. We further introduce RCDT, an offline pipeline that distills degradation descriptors from unpaired real images and transfers them onto clean targets using frozen open-source models. Fill2SR supports mixed-resolution training up to QHD and yields stable performance across $512/1024/2048$ outputs. On synthetic benchmarks, our base model with IIEA achieves the best LPIPS on DIV2K and LSDIR; adding RCDT trades a small LPIPS drop for consistently stronger no-reference quality on RealLQ250 and RealPhoto60. Fill2SR remains memory-predictable, running $1536^2$ inference on a single 32GB GPU and extending to multi-megapixel outputs via tiled restoration.

---


### 468. [Pretraining Transformers with Quantized Softmax in Attention](https://arxiv.org/abs/2609.33591)

**<font color=#1a73e8>作者：</font>** Shangzhen Zhu, Muyan Hu, Tomasz Kozlowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision Transformer systems increasingly quantize attention matrix multiplications, while softmax often remains at higher precision. During pretraining, an approximate softmax changes the gradients that train the model as well as its forward computation. We study this interaction with K-interval attention, which approximates the exponential using K+1 grid values. We vary per-row grid calibration, interpolation versus hard rounding, and the placement of a straight-through surrogate relative to normalization. We derive the corresponding backward rules, including calibration derivatives, and compare these choices in pretraining experiments matched on model, data, and optimizer. Detaching the row extrema leaves the forward computation unchanged but produces a delayed increase in validation loss. With hard rounding at K=4, min-max calibration and a pre-normalization surrogate incur a large loss gap; changing either choice substantially reduces it. At 124M parameters and 2.5B training tokens, fixed-window calibration with a post-normalization surrogate yields a validation loss gap of +0.019 nats relative to softmax at K=4, and with a pre-normalization surrogate yields +0.004 nats at K=16.

---


### 469. [LoopLUT: 3D Lookup Tables with Progressive Region Refinement for Real-Time 4K Image Enhancement](https://arxiv.org/abs/2609.33593)

**<font color=#1a73e8>作者：</font>** Yang Ye, Jiajun Ma, Chen Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color enhancement of 4K images must meet a quality target under a tight compute budget. Three-dimensional lookup tables (3D LUTs) dominate real-time enhancement because they decide at low resolution and apply a per-pixel lookup at full resolution. A single global LUT, however, is spatially invariant, so an underexposed shadow and a well-exposed region that share a pixel value receive identical corrections. Spatially heterogeneous demands cannot be expressed by such a mapping. We propose LoopLUT, a region-cascaded 3D LUT with progressive refinement. A global LUT performs the overall correction, followed by K-1 loop iterations. In each iteration a gating head predicts at low resolution the region that still needs correction, then builds a residual LUT from the color statistics of that region alone. The cascaded gates form a partition of unity, so the output is a per-pixel convex combination of the K lookup results. Fusion is therefore performed by the gates themselves, with no separate fusion module and no interpolation error accumulating across rounds. The decision stage runs at a fixed 256x256 resolution, independent of output resolution, so a 4K image costs only K pure lookups. Extensive experiments across four benchmarks show that LoopLUT improves PSNR by up to 2.81 dB over the strongest prior method, while keeping real-time throughput at 4K. The same decomposition also generalizes well to underwater enhancement datasets.

---


### 470. [The Price of Peeking: Anytime-Valid Leakage Detection on ML-KEM EM Traces](https://arxiv.org/abs/2609.33597)

**<font color=#1a73e8>作者：</font>** Georgios Feretzakis, Alexandros Papaspyridis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Side-channel evaluators routinely inspect leakage tests while acquisition is still running, and extend or stop the campaign based on what they see. Fixed-horizon screening such as the Welch $t$-test with threshold $|t|>4.5$ gives no error guarantee for this monitored decision rule. We study anytime-valid leakage detection based on testing by betting: SKIT-type swap-pair e-processes whose false-alarm probability is controlled uniformly over time under an explicit conditional symmetry null. In matched comparisons that share the frozen witness, rows and payoff, first-crossing detection needed 1.68-2.00$\times$ the traces of a fixed-horizon randomization test at 80% detection on synthetic streams, and 1.68-2.38$\times$ on degraded recordings from an open ML-KEM electromagnetic dataset with the primary Ridge witness at $\alpha=0.05$. With the same primary witness and level, on undegraded reference and pqm4 recordings the monitored procedure stopped early: its median stopping point was 62-72 and 146-316 evaluation traces, i.e. 2-8% of a conservative 4096-trace budget. Under exact designed nulls on the recorded backgrounds, repeated-look $|t|>4.5$ screening over all 13000-20000 samples raised a false alarm in 2.7-12.9% of replicates, against 0.0-4.7% for terminal-only screening and no rejection by a sample-wise e-Bonferroni process, which in a prespecified follow-up detected natural-label associations in 4 of 4 backgrounds after 840-3288 traces. All recordings come from one device, and natural-label results are descriptive; we state the assumptions each claim requires.

---


### 471. [Short-Length Code Designs for Integrated Sensing and Communications: A Deep Learning Approach](https://arxiv.org/abs/2609.33605)

**<font color=#1a73e8>作者：</font>** Muah Kim, Shuangyang Li, Tayyebeh Jahani-Nezhad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrated sensing and communication (ISAC) enables joint communication and sensing using a shared waveform, but its signal design is challenging due to the inherent trade-off between the two objectives, particularly in the short blocklength regime. This paper proposes an autoencoder (AE)-based framework for ISAC waveform design in noncoherent settings.
We derive a modified Cramér-Rao bound for multi-target delay estimation and analyze the maximum-likelihood decoding rule for noncoherent communication under correlated fading. These results reveal structural connections and trade-offs between communication and sensing objectives in waveform design.
Based on this analysis, the AE learns waveform representations that jointly optimize both functionalities, with a tunable parameter controlling the trade-off. Simulation results show that the proposed design outperforms conventional schemes in both communication reliability and sensing accuracy, especially under short blocklength and fading conditions.

---


### 472. [Hierarchical Response Preservation for Continual Adaptation of Zero-Shot Graph-Text Models](https://arxiv.org/abs/2609.33607)

**<font color=#1a73e8>作者：</font>** Haopeng Zhang, Yuhan Wang, Yubing Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained graph-text models align graph representations with textual semantics, enabling recognition of unseen classes and transfer across graph domains. However, as graph data and classes continually arrive, models should learn from new supervision while retaining their zero-shot transfer capabilities and historical task knowledge. Two challenges arise: (i) new classes can overturn historical predictions despite preserved distinctions among historical classes, and (ii) overly strict response preservation can stall learning of new classes. To address these challenges, we propose Hierarchical Response Preservation (HiRP). HiRP represents this competition through a hierarchical response that keeps each historical-class probability and sums new-class probabilities, preserving historical distinctions and aggregate competition while allowing distinctions within the new class group to adapt. It further uses the geometry induced by this response to guide constrained updates, retaining useful adaptation directions while controlling response drift. Across three class-incremental settings, HiRP achieves absolute gains of 1.84-7.95 percentage points in average accuracy over the strongest compared baseline in each setting, while mitigating zero-shot transfer degradation.

---


### 473. [Supervision Recovery for Time Series Anomaly Detection via Context-Anchored Pairing](https://arxiv.org/abs/2609.33610)

**<font color=#1a73e8>作者：</font>** Yifei Gao, Tian Lan, Yimeng Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series anomaly detection (TSAD) remains challenging not only because anomaly labels are scarce, but also because temporal anomalies are highly context-dependent. Existing methods often rely on unsupervised objectives or surrogate abnormal patterns, providing limited supervision for context-dependent normal--anomalous distinctions. We propose Context-Anchored Pair Supervision (CAPS), a supervision-recovery framework for TSAD. CAPS views ideal anomaly supervision as a matched comparison between normal and anomalous outcomes under the same temporal context, and seeks to recover such supervision without target-domain anomaly labels. Using simulated normal--anomalous pairs, CAPS learns structure and anomaly-semantic representations through reconstruction, background consistency, and within-pair counterfactual recombination. The resulting anomaly representations form a continuous semantic space with coarse modes and induce a sampleable multimodal prior. CAPS conditionally realizes sampled semantics as residual-form effects on target reference trajectories. The resulting context-anchored normal--anomalous counterparts provide temporal supervision for discriminative detector learning. Experiments on nine datasets show that CAPS achieves the strongest aggregate performance across all four evaluation metrics among the compared methods, while complementary ablations and transfer analyses support the roles of context anchoring, semantic disentanglement, and conditional realization.

---


### 474. [Anguinus Sculpturae: Compositional Synthesis of Peak-Enhancement Breast DCE-MRI Scans](https://arxiv.org/abs/2609.33611)

**<font color=#1a73e8>作者：</font>** Benjamin Hamm, Nico Albert Disch, Maximilian Rokuss 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic contrast-enhanced breast MRI (DCE-MRI) is rich in anatomical and perfusion information, but its reliance on gadolinium-based contrast agents raises safety concerns and adds cost. Virtual contrast enhancement, synthesizing post-contrast from pre-contrast images, is a promising alternative. We address the MAMA-SYNTH challenge task of predicting peak-enhancement breast MRI. Rather than adopting the full machinery of diffusion or flow matching, we observe that under a rectified, straight-line path the generative process collapses to a single difference prediction: the synthetic peak image is the pre-contrast image plus a predicted enhancement map, recovered in one forward pass. Around this we build Anguinus Sculpturae, a compositional pipeline in which nnU-Net segmentations of lesion, foreground and breast region guide two generators - one optimized for global fidelity, one for lesion structure through an asymmetric Tversky term routed via a frozen segmenter - composited region-wise with Gaussian-weighted blending. On the held-out Duke subset of MAMA-MIA our model achieves the best FRD and Dice among all evaluated variants, showing that single-step difference prediction with segmentation guidance suffices to recover both global fidelity and lesion structure. Code is available at this https URL.

---


### 475. [StoryEngine: A State-Grounded Agentic Framework for Video Storytelling](https://arxiv.org/abs/2609.33627)

**<font color=#1a73e8>作者：</font>** Yingrui Wang, Zeqing Wang, Yeying Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in agentic multi-shot video generation, producing coherent and consistent long-form stories remains challenging. Existing agentic pipelines typically rely on textual shot plans or previously generated pixels, yet lack an explicit mechanism for propagating the consequences of story events and maintaining the video world state across shots. As a result, missing visual details may be reconstructed inaccurately, while visual drift may propagate across subsequent shots, undermining both narrative coherence and visual consistency. To address these challenges, we propose StoryEngine, a state-grounded agentic framework for video storytelling. StoryEngine establishes a separation between authoritative semantic plans and unreliable visual observations. Specifically, StoryEngine maintains a structured representation of entity placement and story-relevant states, and propagates event-induced changes to define the intended start and end states of each shot. To visually realize these states, StoryEngine constructs canonical references for recurring entities and environments, and compiles state and visual constraints into executable render plans. Meanwhile, to realize these states correctly, a bounded evaluation-guided repair loop further corrects local state inconsistencies. Together, these mechanisms preserve causal story progression and prevent local visual errors from propagating across shots. To comprehensively evaluate long-form storytelling, we construct a benchmark across diverse scenarios and visual styles, with metrics assessing storytelling quality, narrative coherence, and visual consistency. Experimental results demonstrate that StoryEngine consistently outperforms state-of-the-art methods across all evaluation dimensions, validating its effectiveness for coherent and consistent video storytelling.

---


### 476. [Scalable and Data-Driven Decision Support in the Maintenance, Repair, and Overhaul Process](https://arxiv.org/abs/2609.33641)

**<font color=#1a73e8>作者：</font>** Houkun Zhu, Helena Ebel, Dominik Scheinert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Several businesses apply maintenance, repair, and overhaul (MRO) principles to the life-cycle of their existing products. In cases like casted gas turbine component Product Lifecycle Management (PLM), repairing components in frequent intervals can extend the lifetime expectation of the product, provide higher cost efficiency compared to newly produced components, and even improve the part design during the repair cycle. Another aspect of repair concerns sustainability, as products often contain rare materials. The emissions produced by the repair process are usually smaller than mining materials and casting new components.
To optimize the repair process further, we propose the Smart Expert System (SES), which assists engineering experts with machine learning-based decision support throughout the repair process. We elaborate on its IT architecture and present machine learning models employed for representative MRO use cases. The SES is evaluated using actual industry data from a leading gas turbine company and demonstrably fulfills formulated requirements concerning the suitability of the overall decision support and the stability of the enclosing IT architecture.

---


### 477. [From Distributions to Stochastic Processes: Neural Approximation of Measure-Valued Maps](https://arxiv.org/abs/2609.33649)

**<font color=#1a73e8>作者：</font>** Yichen Wang, Ziyi Wang, Wenlian Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning mappings between probability distributions arises naturally when inputs and outputs are represented by populations of samples rather than individual observations. We develop an approximation-theoretic framework for distribution-to-distribution learning and extend it to mappings between stochastic processes. For continuous operators on $W_2$-compact families of finite-dimensional probability laws, we establish uniform neural approximation in the 2-Wasserstein metric using finite law statistics, a simplex-valued neural map, and a shared atomic output support that guarantees valid probability measures. We further extend this principle to probability laws on separable Hilbert spaces through finite-rank orthogonal projections. These results establish the representational feasibility of learning transformations between probability laws rather than deterministic vectors or functions.
To demonstrate practical relevance, we study two problems naturally defined at the distribution level: prediction of first-passage-time distributions for an Ornstein--Uhlenbeck process and nonlinear response-path laws of a Duffing oscillator. Because the theory is model-agnostic and broader than any single practical architecture, the experiments use task-adapted neural models rather than reproducing the theoretical construction exactly. In both problems, the proposed models outperform a fixed-feature MLP baseline and distribution-space kernel regression. These experiments complement the theory by demonstrating the practical learnability of distribution-to-distribution transformations in random systems.

---


### 478. [FuseAlign: Forced Alignment in the Wild](https://arxiv.org/abs/2609.33650)

**<font color=#1a73e8>作者：</font>** Mithilesh Vaidya, Stephen Bailey, Sumukh Badam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Word-level forced alignment estimates when each transcript word occurs in an audio recording. It underpins text-based media editing, subtitling, speech-data curation, and phonetic analysis. Existing evaluations understate the difficulty of forced alignment by relying on short, clean speech, perfect transcripts, and metrics that obscure consequential alignment errors. In contrast, real-world media and data-processing pipelines operate on long and diverse recordings. Additionally, forced aligners often operate on error-prone automatic speech recognition (ASR) output. We address these gaps with improved evaluation metrics, a scoring protocol for real ASR transcripts, and AlignBench, a benchmark spanning diverse speaker, acoustic, and text conditions. We further introduce FuseAlign, a transformer-based aligner trained on large-scale pseudo-labeled speech with online label correction. FuseAlign performs joint contextualization of audio and text for the localization of coarse words. The model then refines boundaries at millisecond resolution and detects missing transcript words in the audio without lexicon-based or Viterbi decoding. On AlignBench, FuseAlign substantially outperforms all baselines and remains robust under real ASR transcripts. Ablations show that convolutional upsampling and EMA-snapshot label correction matter more than model properties such as parameter count.

---


### 479. [Tsubame: Tree Replay for Diffusion-Based Speculative Decoding](https://arxiv.org/abs/2609.33652)

**<font color=#1a73e8>作者：</font>** Yepeng Weng, Qiao Hu, Takehisa Yairi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context-aware dynamic trees allocate the speculative decoding budget according to draft path probabilities, adapting their depth and branching to the current context. Under stochastic decoding, however, we find that this structural advantage does not always compensate for the acceptance gains of random sampling paired with advanced verification, and such dynamic trees can fall behind sampled chains in some settings. These trees grow their topology from the candidates themselves, so the tokens submitted for verification are typically the deterministic high-score tokens selected during construction. This coupling is not inherent: once the topology is fixed, its nodes can be repopulated by sampling, allowing dynamic trees to retain their structural advantage while also benefiting from random sampling and advanced verification. Diffusion-based drafters make this practical, as their parallel outputs or lightweight conditional corrections allow candidates to be regenerated cheaply after the complete topology is known. We introduce Tsubame, a two-pass tree speculative decoding framework for diffusion-based drafters. The first pass plans and freezes a context-aware topology using draft path scores; the second replays the fixed topology, sampling the tokens that populate its nodes to form the candidate tree for verification. We prove that Tsubame is lossless under compatible sampling and verification strategies. Experiments across three diffusion-based drafters, six datasets, and multiple candidate budgets show that Tsubame improves acceptance length and throughput over deterministic trees, including settings where it reverses their disadvantage against sampled chains.

---


### 480. [Towards Eliminating Catastrophic Forgetting in the Curriculum Learning of Math Reasoning Tasks](https://arxiv.org/abs/2609.33655)

**<font color=#1a73e8>作者：</font>** Zengyan Yang, Yangyang Wu, Kai Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Curriculum learning has found broad application across numerous domains. Nevertheless, its effectiveness is intrinsically curtailed by catastrophic forgetting, driven by the shifts in model parameter distributions between curriculum tasks. In this paper, we investigate the phenomenon of catastrophic forgetting in this training paradigm, building on the established efficacy of curriculum learning. Our theoretical analyses of parameter update dynamics demonstrate that catastrophic forgetting in curriculum learning stems from the divergence of task optima, which is generally essential to the faster convergence of curriculum learning; therefore, forgetting cannot be completely eliminated. Based on this finding, we augment the training process and propose IV-EWC, which incorporates Elastic Weight Consolidation (EWC) into the curriculum learning objective to curb catastrophic forgetting in mathematical reasoning, a prototypical curriculum learning scenario. IV-EWC employs the influence function to construct a representative validation set from the curriculum's training data, which is used to drive dynamic regularization during training. We further present an extended theoretical analysis to show that EWC-based regularization methods mitigate catastrophic forgetting in curriculum learning, thereby providing theoretical support for IV-EWC. Empirical evaluations on three backbone models and three benchmarks indicate that curriculum learning exhibits catastrophic forgetting. IV-EWC alleviates this issue, reducing forgetting by 162% on average relative to vanilla curriculum learning and yielding positive backward transfer, as evidenced by improved performance on easier tasks after subsequent training on challenging tasks.

---


### 481. [When Noise Meets Long-Tail: Feature-Threshold Dual Calibration for Robust Pseudo-Labeling](https://arxiv.org/abs/2609.33668)

**<font color=#1a73e8>作者：</font>** Ping Guo, Zhiqi Huang, Xinran Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pseudo-labeling has become a cornerstone of learning from unlabeled data in semantic segmentation. Yet its effectiveness drops sharply in real-world scenarios where strong imaging noise and long-tailed class distributions occur together. We trace this failure to a vicious cycle of pseudo-label degradation. Imaging noise entangles foreground and background features, lowering prediction confidence across all classes, while long-tailed distributions leave tail classes with far fewer training samples and inherently lower confidence. Under fixed high-threshold filtering, these tail-class predictions are systematically filtered out, so they receive no supervision from unlabeled data and thus features keep degrading in subsequent iterations. Critically, noise and long-tail are not independent obstacles but mutually amplifying ones, and addressing either alone is insufficient. To break this cycle, we propose FTC-Seg, a Feature-Threshold dual-Calibration framework built on a standard teacher-student framework. At the feature level, Orthogonal Prototype Reconstruction (OPR) uses a set of learnable orthogonal prototypes to residually purify pixel-wise features, widening the margin between weak foreground targets and noisy backgrounds. At the threshold level, Adaptive Threshold Calibration (ATC) dynamically adjusts class-specific thresholds based on learning difficulty and prediction-distribution bias, rescuing low-confidence pseudo-labels of tail classes from systematic exclusion. Extensive experiments on four public benchmarks spanning three distinct noise modalities show that FTC-Seg achieves strong performance against state-of-the-art methods, with particularly substantial gains on tail classes. Our results establish that jointly calibrating features and thresholds is essential for robust pseudo-labeling under compounded noise and class imbalance.

---


### 482. [RSD-Poker: Structure-Adaptive and Shift-Robust Risk-Utility Certification for Residual Policies in Imperfect-Information Games](https://arxiv.org/abs/2609.33669)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Residual policy adaptation provides a lightweight way to modify a strong reference policy, but a shared scale and a fixed subgroup partition can hide heterogeneous degradation and become fragile when the deployment mixture of information states changes. We introduce RSD-Poker, a structure-adaptive and shift-robust certification framework that freezes a bank of residual families and scales, learns a policy-visible partition on an independent structure split, and freezes that partition before calibration labels are joined. Each candidate-group pair receives a weighted simultaneous upper certificate for anchor-relative risk and a lower certificate for weak-response utility. A robust group-to-candidate map is then selected over a predeclared uncertainty set of deployment group proportions. Under independent calibration units drawn from each frozen group's law, a candidate bank and partition fixed before calibration, and invariant within-group conditionals, the selected map satisfies its declared mixture-robust risk budget and utility certificate with probability at least $1-\zeta_{risk}-\zeta_{util}$. The information contract supports both a teacher-backed transform and a teacher-free observation-only student. The retained deterministic 24-state audit remains an exact replay diagnostic: empirical-zero selects $\alpha=0.08$, raising the weak-response proxy from 4.2082 to 4.2889 with $0/12$ held-out threshold crossings. On stratified held-out states, the learned-partition dual selector raises weak utility from 4.4074 under global dual certification to 4.4936 and lowers held-out violation from 0.0215 to 0.0078; its mixture-robust variant reaches violation 0.0059. Across five observation-only checkpoints, risk-calibrated residuals attain weak utility $4.3659\pm0.0177$ and violation rate $0.0178\pm0.0057$.

---


### 483. [Reachability is not enough: Diagnosing long-range behavior in GNNs](https://arxiv.org/abs/2609.33674)

**<font color=#1a73e8>作者：</font>** Filippo Maria Bianchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are often called long-range because their architecture can connect distant nodes, but this does not show whether they use distant information correctly. We introduce a framework that measures how strongly inputs at each graph distance affect predictions and separates limitations due to architecture, finite approximation, training, and numerical execution. Our analysis shows that local message-passing can spread influence slowly, so a finite implementation may rely mainly on nearby inputs even when the ideal computation uses the whole graph. We also explain why mathematically equivalent filters can differ in how easily they are learned and how reliably they run. Across controlled tasks, models with similar architectural reach use distant information very differently, while low average error can hide failures on distant interactions. Together, these results show that long-range capability depends on learning to use information at the distances required by the task and preserving that use during computation.

---


### 484. [Benign Overfitting for General Norms and Distributions](https://arxiv.org/abs/2609.33675)

**<font color=#1a73e8>作者：</font>** Daniel Barzilai, Ohad Shamir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding why predictors can generalize despite interpolating noisy training data is a central puzzle in machine learning. Most work on such "benign overfitting" studies minimum-2-norm linear regression, reflecting the inductive bias of gradient descent. However, modern optimizers such as Adam and Muon use non-Euclidean update geometries, favoring solutions associated with other norms. Analyzing regression for non-Euclidean norms is substantially more difficult, with known results essentially limited to Gaussians. In this paper, we develop a method to analyze benign overfitting in linear regression for general norms and general (sub-Gaussian) distributions. As a special case, we prove that minimum-p-norm interpolation with p>1 can benignly overfit even for non-Gaussian distributions, under suitable conditions. Perhaps surprisingly, for the 1-norm, benign overfitting does not hold in general for well-behaved (but non-Gaussian) distributions, showing that existing positive 1-norm results rely crucially on Gaussianity. Our proof analyzes the geometry of the dual optimization problem, using concentration and central limit tools to show it is approximately Euclidean in many high-dimensional cases.

---


### 485. [T-MoXAI: A Hierarchical Explainability Framework for Temporal Multimodal Data](https://arxiv.org/abs/2609.33685)

**<font color=#1a73e8>作者：</font>** Ali Inha, Mo Vali, Saaliha Vali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) models for temporal multimodal data have potential in healthcare and agriculture, but their opacity can limit trust and adoption. We introduce T-MoXAI (Temporal Multimodal eXplainable AI), a hierarchical framework explaining (1) when timepoints influence predictions, using temporal Shapley values; (2) which modalities contribute at those moments, using attention analysis; and (3) what features or image regions drive decisions, using gradient based attribution. A transformer based architecture handles irregular temporal sequences and heterogeneous data, generating all three explanation levels in under one second for interactive decision support. We evaluate the framework on two real world tasks: predicting IVF treatment outcomes from ultrasound sequences and clinical measurements (AUC 0.660 despite significant class imbalance), and forecasting wheat yield from temporal RGB imagery and phenotypic traits ($R^2$ 0.265 amid substantial environmental variability). Ablation studies indicate that temporal modelling is critical in both domains: removing it reduces performance to the equivalent of random guessing. Temporal ROAR experiments provide evidence that the explanations reflect the model's reasoning process. With a unified, domain agnostic architecture and open source implementation, T-MoXAI provides a baseline for temporal multimodal XAI, addressing fragmentation in the field and supporting applications where understanding decisions is as important as predictive accuracy.

---


### 486. [Resource-Aware Parameter-Efficient Model Adaptation for Onboard High-Dimensional Data](https://arxiv.org/abs/2609.33687)

**<font color=#1a73e8>作者：</font>** Qiyang Zhang, Xinhao Li, Lei Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Onboard satellite models often require frequent updates, but the weights adapted to earlier data distributions can quickly become outdated. However, updating large-scale model parameters in orbit presents significant challenges due to the limited uplink bandwidth of Low Earth Orbit (LEO) satellite systems, particularly for hyperspectral satellite imagery, where high-dimensional spectral-spatial inputs lead to increased model size and update costs. Existing full fine-tuning methods are thus expensive to retrain and difficult to deploy under strict communication constraints. To address this challenge, we propose NE-LoRA, a parameter-efficient adaptation framework for bandwidth-constrained onboard hyperspectral model updates. NE-LoRA combines a primary low-rank branch with a nonlinear auxiliary branch to capture both global update trends and complex spectral-spatial variations. Additionally, we introduce a differentiated training strategy for multi-matrix adapters, motivated by the asymmetric initialization and gradient dynamics of different adapter matrices. Experiments on four hyperspectral datasets and three representative backbone models demonstrate that NE-LoRA consistently outperforms LoRA-based baselines and remains competitive with, and in several cases superior to, full fine-tuning. Across the evaluated settings, NE-LoRA updates only a small fraction of the total parameters on average while preserving low deployment overhead, offering a favorable accuracy-communication trade-off for onboard hyperspectral adaptation.

---


### 487. [TopoMamba: A Load-Support Relation-Guided Multi-Directional State-Space Model for Topology Optimization](https://arxiv.org/abs/2609.33688)

**<font color=#1a73e8>作者：</font>** Bin Lou, Yuxuan Cheng, Huaizhi Zong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning has emerged as an efficient alternative for predicting high-performance material distributions in topology optimization. Existing methods struggle to accurately capture load-transfer information, limiting out-of-distribution generalization, while their model architectures often incur high computational costs. To address these challenges, this paper proposes TopoMamba, a topology prediction framework incorporating a load-support relation-guided multi-directional state-space model. Coupling physical fields with load-support relations enables more effective modeling of mechanical dependencies. A load-support relation-guided spatially adaptive fusion mechanism dynamically adjusts multi-directional scan features according to spatial conditions. Mamba is coupled with the solid isotropic material with penalty method to enhance structural mechanical performance while maintaining computational efficiency. Results on two-dimensional topology optimization benchmarks demonstrate that TopoMamba achieves superior topology prediction accuracy, out-of-distribution generalization, and computational efficiency over state-of-the-art models. The proposed load-support physics-guided framework enables efficient optimization of more complex structural systems.

---


### 488. [Dynamic Kuramoto-Hodge Operators for PDEs on Complex Geometries and Topologies](https://arxiv.org/abs/2609.33693)

**<font color=#1a73e8>作者：</font>** Xiang Li, Yue Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning PDE operators on complex domains requires capturing interactions among fields on vertices, edges, and faces, alongside global responses shaped by topology. Existing neural operators accommodate irregular geometries but often overlook these distinct field supports or their condition-dependent coupling. We introduce the Dynamic Kuramoto--Hodge Operator (DKHO), which combines topology-constrained interactions with learned coordination. DKHO encodes conditions on their native cochain supports, evolves Kuramoto-inspired relation states through the boundary and coboundary operators that compose the Dirac operator, and decodes non-harmonic and harmonic responses in orthogonal Hodge subspaces. Topology thus determines where information can flow, while learned dynamics adapts how it is exchanged to each PDE instance. Across porous-medium Darcy flow, torus transport--diffusion, and cavity magnetostatics, DKHO-large reduces prediction error by approximately 61% on average over leading baselines, while DKHO-small remains competitive using only 11.5--24.3% as many parameters. These results suggest that coupling topological structure with adaptive dynamics provides an effective inductive bias for accurate and parameter-efficient PDE operator learning on complex geometries and topologies.

---


### 489. [Geometric Inductive Biases for Semi-Supervised Equalization: The Constellation-Aware Transformer](https://arxiv.org/abs/2609.33695)

**<font color=#1a73e8>作者：</font>** Avi Caciularu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding signals over unknown channels with minimal pilot overhead is a critical challenge in next-generation communications. Existing deep learning approaches typically rely on generic encoders that struggle to model long-range temporal dependencies or efficiently capture the channel's physical properties from scarce data. We argue that standard architectures suffer from agnostic estimation gaps, as they must implicitly learn the constellation geometry that is already known. We introduce the Constellation-Aware Transformer (CAT), a novel architecture that explicitly injects geometric inductive biases into the equalization process. CAT is composed of a stack of custom TransFIRmer blocks, which use an "early interaction" paradigm to co-process received signals and ideal constellation symbols. Each block features a split Feed-Forward Network that applies a Finite Impulse Response (FIR)-inspired filter for deconvolution and a parallel MLP for geometric refinement. We show that this design is structurally aligned with the optimal linear (MIMO Wiener) receiver: its attention can implement a matched-filter bank, and its bidirectional FIR branch provides the non-causal filtering that block MMSE equalization requires. In the semi-supervised setting, CAT needs fewer pilots than VAE and standard Transformer baselines: on two of our three ISI channels, it reaches a lower SER with 64 pilots than they do with 128.

---


### 490. [A Spectral Theory of Compositional Learning](https://arxiv.org/abs/2609.33708)

**<font color=#1a73e8>作者：</font>** Hugo Rydel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How does compositional reasoning emerge during learning? We address this question by mathematically analyzing the learning dynamics of deep linear networks. We train these networks in structured synthetic environments and derive a theory linking the structure of experience to compositional learning. Our theory predicts when compositional inferences emerge, whether they are identifiable from the available evidence, and how new linking evidence can rapidly unlock previously unavailable inferences. These results provide a qualitative explanation for several phenomena observed in human cognition. They account for why a composition can fail despite knowing its premises, why similar compositions can emerge at different times, and how a single linking fact can suddenly enable many new inferences. Taken together, these findings establish a mathematical link between the statistical structure of experience and the development of compositional reasoning.

---


### 491. [Theory Guided and Interpretable Neural Operator Design for Partial Differential Equation Learning](https://arxiv.org/abs/2609.33715)

**<font color=#1a73e8>作者：</font>** Zeyuan Song, Zheyu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate numerical solutions of partial differential equations (PDEs) are crucial in numerous science and engineering applications. In this work, we introduce a novel neural PDE solver named AFDONet, which incorporates neural operator learning and adaptive Fourier decomposition (AFD) theory for the first time into a specifically designed variational autoencoder (VAE) structure, to solve a general class of nonlinear PDEs on smooth manifolds. AFDONet is the first neural PDE solver whose architectural and component design is fully guided by an established mathematical framework (in this case, AFD theory), turning neural operator design from an art to a science. Thus, AFDONet also exhibits exceptional mathematical explainability and groundness, and enjoys several desired properties. Furthermore, AFDONet achieves outstanding solution accuracy and competitive computational efficiency in several benchmark problems. In particular, thanks to its deep connections with AFD theory, AFDONet shows superior performance in solving PDEs on i) arbitrary (Riemannian) manifolds, and ii) datasets with sharp gradients. Overall, this work presents a new paradigm for designing explainable neural operator frameworks.

---


### 492. [Revisiting Diffusion Fine-Tuning for Unsupervised Domain Adaptation](https://arxiv.org/abs/2609.33716)

**<font color=#1a73e8>作者：</font>** Xuan Qi, Yi Wei, Daniele Berardini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based unsupervised domain adaptation (UDA) improves cross-domain transfer by generating target-specific synthetic data for downstream adaptation. Existing methods are largely designed for single-target adaptation: when a model trained on one labeled source domain must be adapted to multiple unlabeled target domains, they typically require separate diffusion fine-tuning for each source--target pair, causing training, storage, and deployment costs to grow with the number of targets. In this paper, we study multi-target data generation for diffusion-based UDA, where a single source-guided diffusion fine-tuning process is reused to generate target-specific synthetic data for multiple target domains. We propose MUSE (Multi-target UDA-oriented Synthesis with Efficient diffusion fine-tuning), a decoupled adaptation framework that separates source-supervised semantic adaptation from target-specific style adaptation. MUSE uses a shared semantic branch updated by labeled source data and target-private style branches specialized to individual target domains, enabling target-specific generation while avoiding repeated source-guided fine-tuning for each target. Experiments on standard UDA benchmarks show that MUSE achieves a stronger accuracy--efficiency trade-off than repeated per-target diffusion adaptation, reducing diffusion fine-tuning cost while improving average target-domain accuracy. The project page is available at this https URL.

---


### 493. [GeoShrink: Accelerating Diffusion Transformers with Two Lines of Code](https://arxiv.org/abs/2609.33723)

**<font color=#1a73e8>作者：</font>** Haosen Li, Wenshuo Chen, Shaofeng Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers incur substantial inference cost through repeated model evaluations along a sampling trajectory. We introduce GeoShrink, a training-free acceleration method that retains the original solver grid while evaluating the model only at a prescribed set of anchors. At skipped stages, GeoShrink predicts the solver-facing output by adding a geometrically retained fraction of the latest observed innovation to the most recent exact output. We derive this rule from chordal tangent transport and round-trip line projection, and establish a geometric anchor-spacing principle that minimizes the largest adjacent gap expansion under fixed coverage and first span. The analysis characterizes the geometric closure and propagation of prediction errors without assuming access to future model outputs. Experiments cover image, video, motion, and audio generation, together with adapted 3D backends. At approximately $5\times$ acceleration, GeoShrink improves FLUX PSNR by 3.10 dB over the strongest listed baseline. On HunyuanVideo, it achieves a reported $4.99\times$ speedup and improves ChronoMagic-Bench-150 PSNR by 5.44 dB over the strongest listed fidelity baseline. Comparisons at fixed evaluation budgets further show substantial gains on motion, audio, music, and 3D generation.

---


### 494. [Robust Biomolecular Complex Design Across Protein Conformational Landscapes](https://arxiv.org/abs/2609.33726)

**<font color=#1a73e8>作者：</font>** Qingyuan Zeng, Zongqi Xu, Anglin Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proteins populate conformational ensembles, yet structure-based biomolecular design typically optimizes candidates against a single target conformation. Consequently, a candidate that fits one state can lose favorable interactions or develop steric clashes when the target adopts another. We introduce FlexEvo, a model-agnostic evolutionary framework that adapts candidates once at inference time from a single target conformation to improve compatibility with alternative natural conformations unseen during adaptation, without retraining the source model or requiring a conformational ensemble. FlexEvo casts cross-state adaptation as geometry-constrained bi-objective optimization, balancing preservation of input-state interactions against robustness to plausible conformational perturbations. To limit the search space and reduce invalid structural edits, geometry-derived FlexBoxes define protected anchor regions, adaptable regions for local exploration, and forbidden regions for clash avoidance. A unified all-atom representation supports topology-preserving adaptation across diverse binder categories, while Pareto selection preserves nondominated candidates across the two objectives. We evaluate FlexEvo across multiple generation baselines and nine representative binder categories spanning diverse molecular sizes and structural topologies. FlexEvo reduces the category-balanced mean relative performance degradation from 47.8% to 4.4%, while adding only 1.4--3.1 minutes of adaptation per sample. These results establish single-state inference-time adaptation as a practical route toward robust biomolecular complex design across protein conformational landscapes.

---


### 495. [ALDER: Discovering the Laws of a World by Acting in It](https://arxiv.org/abs/2609.33728)

**<font color=#1a73e8>作者：</font>** Teng Cao, Yu Deng, Quentin Delfosse 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable world models should not only predict future states but express how actions change the world in an explicit, transparent and testable form, such as equations. Yet methods that rely on a fixed set of trajectories cannot distinguish equally good competing hypotheses, while searches over a fixed set of predefined candidates cannot discover equations outside the initial hypothesis space. We introduce ALDER (Action-guided Law Discovery, Evaluation, and Revision), a method that actively proposes novel experiments to test and revise models. Specifically, ALDER proposes parametric equations; a numerical optimizer fits their coefficients; an independent verifier tests these candidates on held-out data. To distinguish between competing valid hypotheses, a cost- and safety-aware selector queries interventions, in the form of novel experiments. The resulting counterexamples update the evidence ledger and guide the next structural revision, while incompatible laws are discarded. Across an in-house benchmark, ODE equation discovery tasks, and robotic experiments, ALDER discovers laws beyond its initial formula set, repairs failed model proposals, distinguishes fixed candidate models with fewer interactions, and improves out-of-distribution prediction. Furthermore, given a current state and a target, ALDER selects control actions by solving the inverse problem defined by its validated world model. Together, these results show that explicit equation-based world models can be tested and revised through interaction, then naturally used to guide goal-directed control.

---


### 496. [Yorùbá in Unicode: An Overview of a Problem](https://arxiv.org/abs/2609.33734)

**<font color=#1a73e8>作者：</font>** Kólá Túbòsún  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is a recurrent problem in the writing of Yorùbá on the internet and on the computer that has proven intractable over the years. The language, along with other African languages that depend on diacritics for disambiguation, requires a small set of precomposed characters that Unicode does not encode. This has forced writers and digital systems to rely on combining character sequences that behave inconsistently across platforms, corrupt under font substitution, and fail in search. This paper documents that failure across a range of real world contexts, from published books to web platforms to mobile keyboards, using personal and empirical evidence. It identifies Unicode's NFC normalization stability policy as the structural constraint that prevents a straightforward fix, arguing for direct intervention of the Consortium in solving the active problem, proposing a formal encoding request for the four core Yorùbá characters as the most durable path to resolution.

---


### 497. [Constrained Edit Fields for Training-Free Flow Editing](https://arxiv.org/abs/2609.33735)

**<font color=#1a73e8>作者：</font>** Jingxuan Kang, Yinsong Wang, Che Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image editing aims to perform a desired edit while preserving source content unrelated to it. Pretrained rectified-flow models enable training-free editing of real images through modifications to their sampling trajectories. However, responses at locations unrelated to the desired edit can still accumulate along the editing trajectory and become visible in the final result. To overcome this, we propose Constrained Edit Fields (CEF), which assigns each spatial location a continuous edit responsibility that quantifies its relevance to the desired edit. CEF estimates edit responsibility directly from the source image when the relevant content is present. For edits whose target content is absent from the source, CEF first generates an unconstrained proposal to reveal its realized spatial support and then estimates responsibility from that proposal. At each editing step, CEF decomposes the base edit field into prompt-induced and trajectory-induced components, enabling edit responsibility to preserve instruction-relevant updates while suppressing unintended trajectory-induced changes. Evaluated on all 700 PIE-Bench examples, CEF achieves state-of-the-art Structure Distance, background LPIPS, and background MSE with both Stable Diffusion 3.5 Medium and FLUX, while retaining competitive instruction alignment. On Stable Diffusion 3.5 Medium, it reduces these metrics over the previous best results by 10.2%, 21.2%, and 48.0%, respectively.

---


### 498. [Task-Aware Discretization of Differentiable Logic Gate Networks](https://arxiv.org/abs/2609.33747)

**<font color=#1a73e8>作者：</font>** Thore Gerlach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiable logic gate networks (DLGNs) enable gradient-based training of highly efficient Boolean networks by relaxing discrete logic gates during training and discretizing them for inference. Standard approaches make this discretization decision locally, typically through argmax selection and confidence- or entropy-based convergence criteria. We show that local discretization can be task-suboptimal even for globally optimal relaxed solutions, with high gate confidence providing no general guarantee, and derive bounds relating task-aware gate selection to tractable interventions in the relaxed network. Motivated by these results, we study first-order downstream task information for progressive discretization and characterize when this local approximation is reliable. Experiments on convolutional DLGNs reveal a strong locality dependence: first-order scores become unreliable when directly optimized over nonlocal interventions, but accurately assess local argmax decisions for progressive freezing.

---


### 499. [ResDiffFRG: Residual Diffusion for Multiple Appropriate Facial Reaction Generation](https://arxiv.org/abs/2609.33749)

**<font color=#1a73e8>作者：</font>** Shizhe Liu, Jiayan Gu, Xiangyu Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In dyadic human speaker-listener conversations, the listener's facial reactions allows the speaker to accurately perceive the listener's emotional states. Since human facial reactions are non-deterministic, the ability to generate multiple appropriate human-like facial reactions is crucial for realistic human-agent interactions. Although diffusion models are naturally suited to such one-to-many generation, existing diffusion-based Multiple Appropriate Facial Reaction Generation (MAFRG) methods attempt to denoise random Gaussian initialisations directly into multiple appropriate facial reactions (AFRs). These random initialisations are usually not well-aligned with the target listener facial reaction, which requires complex denoising trajectories from these initialisations, and subsequently creates substantial opportunities for deviations away from the range of trajectories leading to appropriate AFRs. Given the inherent mimicry between the human listener's and speaker's facial behaviours, we address the above denoising trajectory issue by leveraging this strong prior. Specifically, we propose ResDiffFRG, a novel diffusion-based MAFRG framework that explicitly anchors the diffusion process to the speaker behaviour by defining its diffusion target as the residual between the speaker anchor and an AFR. The denoiser only needs to model the comparatively small, reaction-specific residual needed to transform this anchor into an AFR, rather than reconstructing the complete reaction from an unstructured state. Extensive experiments show that ResDiffFRG achieves large improvements in correlation-based appropriateness over existing methods. Our denoising trajectory analysis showed that even at the start of the denoising trajectory, ResDiffFRG already achieves a higher facial-reaction correlation score than the Gaussian Diffusion baseline does after completing 60% of its denoising trajectory.

---


### 500. [Collaborative Synthetic Data for Privacy-Preserving Financial Fraud Detection Across Organizational Silos](https://arxiv.org/abs/2609.33754)

**<font color=#1a73e8>作者：</font>** Simeon Allmendinger, Domenique Zipperling, Burhanettin Bahadir Kibar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Organizations seek analytical value from AI, yet relevant data are often fragmented across organizations and constrained by privacy. This is acute in financial fraud detection, where rare fraud cases and imbalanced local datasets limit decision-relevant analytics. Federated learning enables collaboration without direct data sharing but does not resolve minority-class scarcity. Synthetic data generation can help, yet lightweight methods are interpolation-bound, while generative models require substantial data and computation. Existing collaborative generative approaches often rely on federated learning, imposing considerable organization-side training burdens. In this paper, we examine CollaFuse as a collaborative diffusion-based alternative for fraud detection and evaluate it across five fraud datasets. Compared with classical oversampling, local generative baselines, and centralized diffusion benchmarks, CollaFuse does not achieve the highest local fidelity but improves downstream fraud detection more consistently across most datasets. These findings suggest that synthetic data create analytical value less through local realism than through transferable cross-organizational structure.

---


> [!TIP]
> 当前位于：**451-500**（第 10/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
