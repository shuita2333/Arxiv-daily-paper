# 📦 其他研究 | 2026年10月28日

> 本类共 **446** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

---

### 101. [CADonatello: Towards Real-World Multi-Part 3D CAD Reconstruction](https://arxiv.org/abs/2610.33575)

**<font color=#1a73e8>作者：</font>** Ahmet Serdar Karadeniz, Dimitrios Mallis, Parsa Akbari Chianeh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing methods for CAD reconstruction from 3D scans achieve strong performance on standard benchmarks, yet their effectiveness often degrades in real-world scenarios where objects consist of multiple parts and scan artifacts such as noise. A key reason is that current CAD reconstruction datasets predominantly contain single-part models and clean geometric inputs, limiting the ability of learned models to generalize to realistic settings. In this work, we introduce CADonatello, a part-aware framework for reconstructing parametric CAD models from real-world 3D scans. Our approach first decomposes the input geometry into structurally meaningful components using a foundation-scale 3D part segmentation model, and then reconstructs each component independently through a cross-section-driven pipeline that performs sketch parameterization followed by an extrusion. To improve the robustness of sketch parameterization to scan-derived cross-sections, we further introduce CC3D Cross-Sections, a dataset of paired rasterized cross-section images from realistic scans and their corresponding parametric sketches derived from aligned CAD models. This dataset enables effective domain adaptation from clean CAD sketch images to scan-derived cross-section images. Extensive experiments demonstrate that the proposed approach improves generalization to noisy scans and enables reliable reconstruction of complex multi-part objects across multiple real-world CAD reverse engineering benchmarks.

---


### 102. [Variational Atlas Autoencoders and Self-Supervised Chart Selection](https://arxiv.org/abs/2610.33577)

**<font color=#1a73e8>作者：</font>** Arno Coomans, Merlin Nimier-David, Eugene d'Eon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex, high-dimensional data lie on manifolds that a single global latent coordinate system cannot represent without distortion. We introduce Variational Atlas Autoencoders, a mixture-of-charts framework that learns an atlas of local latent representations, each responsible for one region of the data manifold. The central difficulty in learning an atlas is deciding which chart should be responsible for which data point without labels. We show that this decision need not be a heuristic. By treating the chart index as a latent variable, the evidence lower bound yields the training objective and casts chart assignment as posterior inference, valid for any routing distribution. Within this framework, we propose latent-evidence routing, which assigns a point to a chart in proportion to the evidence of its encoding under that chart's latent prior. This has a simple interpretation: the closer a point lands to the center of a chart's latent space, and the more confidently it is placed there, the more likely it is to belong to that chart. Chart assignment thus emerges as posterior inference, depends on the encoder alone, and is fully self-supervised, so the charts discover structure in the data on their own, separating classes and subclasses such as distinct types of shoes or faces without access to labels. We further recover an atlas from the trained charts by identifying their overlaps and transition maps, enabling continuous interpolation within and across charts that stays close to the data manifold rather than traversing unsupported regions of latent space. Compared to capacity-matched baselines, Variational Atlas Autoencoders yields better-structured latent spaces and higher sample quality on image datasets including CelebA, while sampling requires evaluating only a single chart's decoder.

---


### 103. [ZoomSEM: accelerating large-scale brain connectomics with intelligent SEM super-resolution](https://arxiv.org/abs/2610.33580)

**<font color=#1a73e8>作者：</font>** Jiateng Shou, Zhiwei Xiong, Ruikang Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Serial electron microscopy (EM) is essential for large-volume biological imaging and connectomics, yet its throughput remains a major bottleneck, with cubic-millimeter-scale brain imaging requiring months or years. Existing deep learning-based EM super-resolution methods are limited to small upscaling factors or rely on synthetic data, offering modest acceleration and limited practical impact. We introduce ZoomSEM, a deep learning-based super-resolution method to dramatically accelerate SEM imaging. Trained on real low- and high-resolution scanning electron microscopy (SEM) pairs, ZoomSEM enables reliable recovery of 4$\times$, 8$\times$, and up to 16$\times$ higher-resolution images from fast low-resolution scans while preserving fine neuronal structures critical for connectomic analysis, achieving up to 30-fold effective acceleration. Extensive experiments across datasets of diverse biological samples demonstrate robust generalization under realistic low-resolution acquisition. This advance enables high-resolution, large-volume serial EM imaging at unprecedented speed, poised to transform connectomics and related fields.

---


### 104. [UltraFlash: Accelerating Megapixel Visual Synthesis](https://arxiv.org/abs/2610.33581)

**<font color=#1a73e8>作者：</font>** Phuc Lai, Anh Nguyen, Phong Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Megapixel visual synthesis with latent diffusion models requires operating far beyond the resolutions at which these models are typically trained. Cascade refinement is a leading strategy for this setting: it starts from a base image at a native resolution and progressively upsamples it to the target resolution through multiple refinement stages. Each stage typically performs a pixel-space resolution transition followed by latent-space denoising. While prior acceleration efforts mainly focus on reducing denoising cost, we identify a complementary and underexplored bottleneck: the repeated movement of representations through the VAE. We call these operations pixel-space transitions. In cascade pipelines, intermediate latents are often decoded to RGB, resized, and re-encoded before refinement, while final latents are decoded patch by patch with dense overlap to suppress boundary artifacts. We propose UltraFlash, a transition-efficient approach that accelerates these VAE-heavy operations. UltraFlash has two components. Latent Hyperloop replaces intermediate RGB round trips with a learned latent-space shortcut that approximates the decode-resize-encode transformation without repeated VAE decoding and encoding. Sparse Patch-based Decoding accelerates final reconstruction by addressing patch seams caused by inconsistent GroupNorm statistics and reusing cached statistics across patches, enabling sparse VAE decoding with much smaller overlap. Integrated into a state-of-the-art cascade baseline, UltraFlash reduces 4K generation latency by approximately 2x while improving image quality. These results show that optimizing pixel-space transitions can improve both efficiency and fidelity, offering an effective route toward fast, high-quality megapixel visual synthesis.

---


### 105. [When the Weakest Language Keeps Moving: ARMOR-DP for Multilingual BabyLM](https://arxiv.org/abs/2610.33583)

**<font color=#1a73e8>作者：</font>** Hanyu Liao, Yijing Chen, Tao Ji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual BabyLM systems usually fix language sampling proportions even though the weakest language can change during training. We present ARMOR-DP, a modular framework that diagnoses imbalance arising from representation, exposure, capacity, and objective pressure, and uses per-language validation loss to update sampling. Controlled experiments show that equal character budgets create a severe representation artifact for Chinese; byte-level encoding removes much of it, while static Chinese protection can subsequently make English the weakest language. The dynamic controller tracks these transitions and achieves a better score--balance tradeoff than fixed protection. On official evaluation, curriculum-dynamic checkpoints outperform a matched static Chinese-protective baseline while using fewer Chinese epochs; scaling capacity yields the strongest internal ARMOR-DP system. These results support a simple conclusion: multilingual weakness is a training-time state rather than a fixed property of a language. ARMOR-DP therefore separates diagnosis from intervention, allowing protection to follow the current bottleneck instead of a predetermined language label.

---


### 106. [Mix Forcing: Causal Pre-Training via Mixture Attention for Interactive World Models](https://arxiv.org/abs/2610.33589)

**<font color=#1a73e8>作者：</font>** Zelin Gao, Hao Ouyang, Jiapeng Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While interactive video world models require autoregressive generation, directly adapting pretrained bidirectional video diffusion models into autoregressive ones with teacher forcing can disrupt their visual priors and degrade autoregressive generation quality. In this paper, we introduce Mix Forcing, a causal pre-training paradigm for interactive video world models, implemented with the Mixture-of-Bidirectional-and-Autoregressive (MoBA) attention. Mix Forcing jointly trains a video diffusion model with both teacher forcing and bidirectional training, yielding a strong causal initialization for few-step post-training. In self-attention, Mix Forcing leverages teacher forcing to learn causal next-chunk prediction for autoregressive rollout, while using bidirectional attention to preserve pretrained visual priors. To support online text interaction, Mix Forcing further adopts a chunk-wise cross-attention design that conditions each video chunk on a shared environment prompt and its own local prompt, without exposing future instructions to the current chunk. Following causal pre-training on a 14B image-to-video model, we apply consistency and distribution matching distillation to obtain a four-step autoregressive generator. Experiments on our internal benchmark and public benchmarks, including WBench and SANA-WM-Bench, show that our model achieves state-of-the-art visual quality and timely event following with precise camera control. Notably, our model supports high-fidelity long-horizon generation without quality degradation even over one-hour rollouts. Project page is here: this https URL

---


### 107. [Counterfactual Model Testing Under Distribution Shift](https://arxiv.org/abs/2610.33594)

**<font color=#1a73e8>作者：</font>** Joran Leest, Ilias Gerostathopoulos, Claudia Raibulet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deployed machine learning (ML) models can degrade as the distribution of their input data shifts. Such shifts can result from changes in the population or from data integrity issues in the pipeline that materializes model features, two sources that operate through different mechanisms. Because labels are often absent or delayed, it is common practice to track shifts in the data instead, but a detected shift does not indicate how it affects the model. We formulate this problem as online model testing under distribution shift. Testing requires reproducing the shift on a controlled baseline with known labels. Since the same shift can come from either source, doing so requires knowing which mechanism changed. We propose a methodology that reproduces observed changes in both mechanisms to estimate current performance and the potential gain from repairing observed data integrity issues. Experiments on real-world datasets with simulated faults show that separating the two sources generally improves both estimates, supporting this formulation. A churn prediction case illustrates how these tests can support monitoring and repair prioritization

---


### 108. [H-GLow: Accelerating Graph Generation via Hazard-Guided Discrete Flow Matching](https://arxiv.org/abs/2610.33599)

**<font color=#1a73e8>作者：</font>** Sirine Ayadi, Stephan Günnemann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete flow matching (DFM) offers a promising approach to graph generation; however, generating high-quality graphs with few steps remains challenging due to the strong dependencies between nodes and edges. Although DFM decouples training from sampling, enabling flexible sampling strategies without retraining, existing graph DFM samplers often rely on task-specific heuristics, substantially expanding the hyperparameter space. Moreover, graph DFM models still require sampling budgets comparable to those of diffusion-based approaches, leaving their potential for accelerating graph generation only partially realized. In this work, we introduce H-Glow, a hazard-guided framework for accelerating graph generation built on the decomposition of Continuous-Time Markov chain (CTMC) generators into hazards and conditional jump distributions. H-Glow leverages these quantities to plan graph edits and dynamically adjust the sampling time to graph activity. H-Glow can be adapted to pretrained graph DFM models, substantially improving the generation quality with fewer steps. We further introduce a novel graph DFM model based on the conditional generator matching framework, which directly predicts hazards and conditional jumps, and show that its training objective decomposes exactly into hazard matching and hazard-weighted jump prediction. Experiments on molecular and synthetic graph benchmarks demonstrate improved generation quality with substantially fewer sampling steps.

---


### 109. [Satellite-derived bathymetry of Arabian Gulf ports under leakage-free validation: a multi-site benchmark of empirical, machine-learning and deep-learning models against 285,000 multibeam soundings, with an outlook for UAE waters](https://arxiv.org/abs/2610.33609)

**<font color=#1a73e8>作者：</font>** Muhammad Saeed, Fatema Al Hajri, Mohamed H. Alhosani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Satellite-derived bathymetry (SDB) is often proposed as a low-cost complement to multibeam surveys of ports, but its accuracy is seldom measured on an area the model has never seen. We test SDB in the turbid, shallow and tidal waters of the Abu Dhabi coast against 285,619 multibeam soundings from twelve surveys at six port areas, reduced to Lowest Astronomical Tide. The Stumpf ratio, the Lyzenga transform, a monotonic gradient-boosted tree model (LightGBM) and a U-Net ensemble were trained on 72 Sentinel-2 images and tested in transfer to an unseen site and with local control (about 20% of a site's soundings, spatial blocks beyond a 225 m buffer). The validation design changed the result more than the model: the same LightGBM model gave 0.57 m RMSE under a random pixel split, 1.30 m under spatial blocks and 1.66 m at an unseen site. In transfer the Stumpf ratio (1.45 m) was not beaten by LightGBM, the U-Net or Lyzenga. With local control a hybrid of the tree output and the band ratio reached 1.11 m over 0-11 m, 67% of pixels within the IHO S-44 Order 2 tolerance and a conformal 95% interval with 95% observed coverage; in clear water it reached 0.29-0.53 m. The seabed could not be read beyond 11 m, and summer images were five to six times more turbid than winter ones. ICESat-2 ATL24 agreed with the surveys to 0.25 m after a depth-dependent offset was removed. A 60 m reconnaissance mosaic of 17,200 km2 of the UAE coast, calibrated cell by cell on ICESat-2 without any vessel survey, reached 1.42 m RMSE on held-out blocks over half of the product. Sentinel-2 SDB with about a hundred control depths per image is a usable reconnaissance and change-monitoring tool in these waters to about 10 m; it does not meet S-44 Order 1 without local control, and accuracies from random splits should not be taken as operational accuracy.

---


### 110. [Geodesic-SVDD Latent Mixup for One-Shot Distributed Tabular Learning](https://arxiv.org/abs/2610.33619)

**<font color=#1a73e8>作者：</font>** Andrea Moleri, Christian Internò, Markus Olhofer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed Learning on structured data is a key and widely adopted approach in privacy-sensitive sectors, ranging from financial fraud prevention to federated healthcare diagnostics. While Gradient Boosted Decision Trees are widely used in centralized settings due to their efficiency, they are incompatible with standard gradient-based federated learning protocols because of their non-differentiability. Conversely, standard deep classifiers that are amenable to federated optimization often suffer from catastrophic forgetting under label distribution skew. In this work, to address these gaps we propose Geodesic-SVDD, a framework for Distributed Spherical Prototype Learning that recasts each client's task as one-class density estimation on the hypersphere, so that local models can be aggregated as probabilistic manifolds in a single round. Specifically, for each client, we employ a Residual Spherical Encoder and Geodesic Latent Mixup that enforces strict hyperspherical constraints ($\|\phi(x)\| \equiv 1$), preventing the manifold collapse observed in linear approximations. Furthermore, leveraging this insight, we propose a novel One-Shot "Product of Experts" protocol that enables privacy-preserving aggregation without iterative synchronization. Finally, we mechanistically analyze the trade-off between interpolation strategies, demonstrating that while linear mixup offers an enticing computational shortcut, it destabilizes optimization gradients by orders of magnitude ($10^9\times$). Across five tabular benchmarks and four levels of label skew, Geodesic-SVDD attains the highest mean AUROC among seven federated methods, outperforms federated tree ensembles by up to 21 AUROC points on Covertype, and its One-Shot variant matches centralized Deep SVDD under IID and mild skew with a single communication round.

---


### 111. [Graph-dependent pooling: adaptive granularity in hierarchical graph neural networks](https://arxiv.org/abs/2610.33623)

**<font color=#1a73e8>作者：</font>** Bohan Yoon, Hyejin Jang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks are widely used to learn structural representations of relational data. Hierarchical graph pooling learns multi-level representations by progressively coarsening graphs; however, prior methods rely on predefined cluster numbers or fixed pooling ratios, limiting adaptability to individual graphs. We propose Graph-Dependent Pooling (GDPool), which dynamically determines pooling granularity for each graph. We analyze optimization conflicts among layer-wise objectives through gradient alignment, showing that independently supervised pooling levels can send conflicting gradients to shared parameters. GDPool uses self-attention to select graph-specific anchors representing structurally important nodes and constructs coarse graphs through soft node assignment. Experiments on metal-organic framework and molecular graph benchmarks show that GDPool consistently achieves the best predictive performance across all benchmarks. Evaluations using modularity and the effective number of clusters show that GDPool achieves consistently higher modularity than existing methods while the number of active clusters decreases monotonically with depth. Sensitivity analyses confirm stable behavior across hyperparameter and architectural choices.

---


### 112. [Allocation Before the Clock: Graph, Set and Game Theory of Professional League of Legends Objective Setups](https://arxiv.org/abs/2610.33626)

**<font color=#1a73e8>作者：</font>** Zheng Gao, Zhenyu Liu, Yifan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Before every neutral objective in professional League of Legends, each team decides which of its five players walk to the pit, which hold a lane, and when to commit. The leading analysis of such setups, TAGNet for Counter-Strike 2, clusters graph-network embeddings of player positions and reads cluster win rates as tactical quality. We treat a setup as an allocation on a walled map: formations are set partitions on the lattice $\Pi_5$, control is a geodesic Voronoi split of a navigation graph, and commitment is an allocation game solved as a quantal response equilibrium priced in win probability. On all 164 games of MSI and Worlds 2025 (2,994 team-setups, minimap tracks validated against Riot positions), trailing teams leave the pit empty far more often than leading teams, by +34.8 percentage points at the first baron and +30.4 percentage points at Atakhan. Our model, HASSE-QRE, finds six setup patterns that whole-model series-bootstrap refits reproduce (ARI 0.819, comparable to 0.813 for TAGNet's $K$-Means step alone) and indicates that teams price fights, travel and committed players, not the objective itself (weight 0.018; fixing it to one costs 59.9 log-likelihood points). The equilibrium reproduces a quarter of the commitment gap, almost all of it through state variables rather than its strategic channels. Weighting a team-level contrast by exposure moves it across $p=0.05$ (0.046 against 0.052). We release the tracks, setups and code.

---


### 113. [ONOT/TONO-Print: A Paired Benchmark for Identity-Document Portrait Quality under Document Production Shift](https://arxiv.org/abs/2610.33627)

**<font color=#1a73e8>作者：</font>** Alexander Vinogradov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-document portraits are modified during document production by printing, engraving, and integration into the document template. These transformations may change image texture, contrast, colour, and other visual properties without necessarily changing the underlying biometric or presentation information. In this work, we introduce ONOT/TONO-Print, a small paired benchmark for evaluating face-image quality models under identity-document production shift. The benchmark is based on ONOT and TONO portraits and contains synthetic variants representing five common production techniques: toner, inkjet, dye sublimation, laser engraving, and thermal transfer. A smaller physical subset contains portraits printed and scanned using inkjet and toner devices. The benchmark is used to compare the behaviour of biometric and ICAO-related face-quality components before and after production. Results show that production can introduce substantial domain shift for some quality estimators, while other models remain comparatively stable.

---


### 114. [DROA-CLIPSeg: Prompt-Guided Thin Crack Segmentation in Low-Light Conditions](https://arxiv.org/abs/2610.33635)

**<font color=#1a73e8>作者：</font>** Vinita Shukla, Partibha Jangra, Vinayak Pathak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pavement crack segmentation under low light is degraded by reduced contrast, shadows, headlight glare, joints, stains, and wet seams. Existing crack segmentation methods mostly assume good illumination. Low-light enhancement methods improve visual quality, but they do not explicitly preserve crack topology. To address these limitations, we formulate low-light crack segmentation as a degradation-aware, prompt-grounded structural defect segmentation problem and propose DROA-CLIPSeg, a parameter-efficient framework that adapts a frozen CLIPSeg vision language backbone using two lightweight modules. QKV Low-Rank Adaptation is injected into the Q/K/V projections of the vision and text encoders to improve crack-specific image text alignment without backbone fine-tuning. The proposed Domain Residual Orthogonal Adapter (DROA) decomposes intermediate features into a dominant crack-domain branch, which captures recurring low-light crack patterns, and an orthogonal residual branch, which preserves faint, thin, and fragmented evidence usually suppressed by noise, shadow, or over-smoothing. We also introduce CrackLingo-9K and CrackLingo-12K, text augmented versions of Crack9k and Crack12k with crack-aware prompts. Training only approximately 1.93 M parameters, corresponding to 1.3% of the full model, DROA-CLIPSeg outperforms 9 zero-shot and 4 fine-tuned vision language baselines on both splits, generalises zero-shot to MVTec AD across textures and defect morphologies, and is supported by extensive ablations. Our source code is publicly available at this https URL

---


### 115. [UniQuery: Unifying Vision Models with a Joint Query Head for Cross-Domain Pedestrian Attribute Recognition](https://arxiv.org/abs/2610.33639)

**<font color=#1a73e8>作者：</font>** Nguyen Dang Duy Tan, Linh T. T. Tran, Huynh Nguyen Phat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian Attribute Recognition (PAR) predicts semantic attributes of individuals, such as gender, age, clothing and accessories, and its descriptions support attribute-based person retrieval and person re-identification. However, accurately recognizing fine-grained attributes across domains remains challenging due to occlusion, appearance variations, and shifts in image distributions. Ensembles of independently trained foundation encoders combine their logits with fixed fusion weights, so every attribute uses the same mix and the encoders are never trained together. We propose UniQuery, which instead jointly fine-tunes DINOv3 and CLIP for attribute-specific fusion. It combines two query heads, one for each encoder, with a joint query head whose attribute queries attend to tokens from both encoders, and the prediction is the average of the logits of the three query heads. We evaluate UniQuery on the benchmark of the UPAR Challenge 2027 at the WACV 2027 Real-World Surveillance workshop, where models are trained on PA100k, PETA and Market-1501 with a shared set of attributes. In leave-one-dataset-out experiments, UniQuery outperforms the independent ensemble in Challenge_Avg on both held-out datasets. Ablations show that learning fusion over independently trained encoders does not improve upon logit averaging in the mean over the two held-out datasets, while freezing the encoders lowers the Challenge_Avg of UniQuery. On the hidden test set of the benchmark, UniQuery achieves a Challenge_Avg of 0.8001.

---


### 116. [LENS: Likelihood Evaluation and Neighbor Smoothing for Attribute-Based Person Retrieval on Unseen Cameras](https://arxiv.org/abs/2610.33641)

**<font color=#1a73e8>作者：</font>** Nguyen Dang Duy Tan, Vo Thanh Nguyen, Linh T. T. Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attribute-based person retrieval ranks surveillance images from a binary query of semantic attributes, but mean Average Attribute Degree of Match (mADM) drops on unseen cameras as predicted probabilities shift. Common pipelines rank gallery images by their L1 distance to the query, which penalizes a confident single-attribute mismatch no more than small uncertainties across many attributes, while post-hoc recalibration fitted on source validation data fails to transfer because the per-attribute maps fitted on source data do not match those of new cameras. We propose LENS (Likelihood Evaluation and Neighbor Smoothing), combining fine-tuned DINOv3 and CLIP models with a distilled student. LENS regularizes mutually exclusive attribute groups with group cross-entropy in training, scores gallery images by the log-likelihood of the exact query, and smooths gallery logits over nearest neighbors using DINOv3 appearance features from the same forward pass. On held-out datasets, all three changes raise mADM: the likelihood score improves all six retrieval metrics for the main ensemble and mADM for all 48 development models, and training-free kNN smoothing improves all 46 tested development models. On the hidden test set of the UPAR 2027 benchmark, LENS reaches 68.17 mADM.

---


### 117. [Physics-Informed Graph-Based Safe RL with Constraint-Specific Critics for Community Battery Coordination in Distribution Network](https://arxiv.org/abs/2610.33654)

**<font color=#1a73e8>作者：</font>** Chenghao Huang, Yue Yang, Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High penetrations of distributed energy resources (DERs) and fast-varying electric vehicle (EV) charging intensify voltage and line-limit violations in distribution networks (DNs), making safe, low-cost operation increasingly challenging. This paper proposes a physics-informed safe deep reinforcement learning (DRL) framework for coordinating community battery energy storage systems to mitigate constraint violations while minimizing operating cost. To represent nonlocal spatiotemporal interactions, we develop a dual-level physics-informed graph representation in which line impedance and capacity shape spatial information propagation, while power-balance, voltage-profile, and flow-reconstruction losses regularize the latent state toward control-relevant physical consistency. Building on this representation, we develop Lagrangian Dedicated-Critic PPO (LDCPPO), which implements constraint-specific value decomposition: independent reward and cost critics preserve heterogeneous voltage- and line-loading-related learning signals and combine their advantages only during the Lagrangian policy update. Case studies on DNs with high rooftop photovoltaic penetration and EV charging demonstrate that the proposed method reduces the key voltage-violation degree by up to 80.5% compared with the tested baselines, while also achieving the lowest voltage-violation count and line-overload degree with competitive operating cost.

---


### 118. [FreeView: Robust 3D Reconstruction from Uncurated Views](https://arxiv.org/abs/2610.33656)

**<font color=#1a73e8>作者：</font>** Junho Kim, Hyunyoung Choi, Seongwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing a coherent 3D scene from uncurated image collections remains challenging due to the presence of irrelevant or non-overlapping views. Recent work has shown that feed-forward reconstruction models contain internal view-consistency signals that support distractor rejection. However, reference-conditioned filtering relies on a curated clean reference, which is not guaranteed in practical image collections. To address this limitation, we introduce FreeView, a training-free framework that jointly selects a filtering reference and rejects distractor views from an uncurated collection. FreeView leverages collection-level consensus to identify a representative view that serves as a reliable reference for filtering. It then adapts view rejection to each input collection by combining complementary visual and geometric evidence. This approach preserves useful views under substantial appearance and viewpoint variations while rejecting distractors. FreeView integrates with both VGGT and pi^3, removing the need for a manually curated reference or manual calibration of view rejection. Extensive experiments across multiple datasets demonstrate high clean-view retention and distractor rejection rates, leading to reliable 3D reconstruction from uncurated views.

---


### 119. [Tracking Is Not Sensing: Artifact-Aware Thermal Video Respiration Estimation in Head-Free Marmosets](https://arxiv.org/abs/2610.33661)

**<font color=#1a73e8>作者：</font>** Penghao Wang, Sen Yang, Fenghua Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous physiological monitoring is essential for linking behavior, internal state, and neural activity in neuroscience and translational research. In common marmosets, a key nonhuman primate model for social neuroscience, respiratory rate provides a basic readout of arousal, stress, and physiological regulation. Contact sensors can provide accurate measurements, but they add preparation burden and may interfere with head-free behavioral protocols. Thermal video offers a noncontact alternative by capturing breathing-related temperature changes around the nose and mouth. However, in head-free marmosets, these cues are weak, localized, and easily corrupted by head motion, pose changes, and fur. Here we show that this setting exposes a broader challenge in video-based physiological sensing: visually reliable tracking does not necessarily imply physiologically valid measurement. Using synchronized thermal video and contact respiration recordings, we show that marmoset respiration is recoverable from thermal video but strongly ROI-sensitive. Under head-free motion, visually plausible nasal tracking can still produce traces inconsistent with contact respiration, demonstrating that tracking is not sensing. We therefore estimate respiratory rate from learned temporal signals extracted from thermal clips and introduce Selective Temporal Attenuation Regularization (STAR). STAR selectively attenuates high-motion thermal discontinuities through local temporal imputation during training, regularizing models toward respiration-consistent dynamics while leaving inference unchanged on raw video. Across multiple deep-learning backbones, STAR improves head-free estimation, reaching 2.23 bpm MAE compared with 20.76 bpm for tracked ROI analysis.

---


### 120. [Beyond Affine Reconstruction: Multi-Resolution Transformer DeepONets for the Radiative Transfer Equation](https://arxiv.org/abs/2610.33668)

**<font color=#1a73e8>作者：</font>** Tanguy Azéma, Marc Bocquet, Fatiha Nmira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radiative heat transfer plays a dominant role in fire simulations, where solving the radiative transfer equation (RTE) is a computational bottleneck. Neural operators can accelerate these computations by learning solution operators from offline simulation data. However, conventional DeepONet surrogates rely on fixed-grid inputs and affine reconstruction, limiting their flexibility across resolutions and their approximation accuracy at a fixed latent dimension. In this paper, we develop a transformer-based DeepONet for multi-resolution RTE surrogate modelling. The proposed approach combines a Perceiver encoder, which maps temperature and absorption coefficient fields at different spatial resolutions into a fixed-size latent representation, with a cross-attention decoder that enables non-affine reconstruction of the radiative intensity. This architecture allows a single model to process inputs at varying resolutions without resampling them onto a common grid. We formulate a computable empirical version of a previously derived theoretical lower bound for affine reconstruction, enabling direct comparison with model errors on the same dataset. Experiments on a two-dimensional pool-fire dataset demonstrate that the proposed approach outperforms autoencoder-based DeepONets in predicting both radiative intensity and incident radiation, with fewer trainable parameters. Power spectral density analysis shows improved preservation of small-scale structures. Both affine baselines remain above the corresponding lower bound at all evaluated ranks, whereas the proposed model achieves a training error below it at one matched latent dimension, demonstrating the potential of non-affine reconstruction to overcome this representational limitation. Experiments on a dataset combining three spatial resolutions confirm the accuracy advantage of the approach at each input resolution.

---


### 121. [Extraction meets Distillation - cryptanalytic techniques to recover parameters from a Deep Neural Network](https://arxiv.org/abs/2610.33671)

**<font color=#1a73e8>作者：</font>** Biprarshi Biswas, Arya Anshuman Ojha, Yubaraj Das 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study fully connected neural-network reconstruction by combining cryptanalytic weight-direction extraction with learning from predicted labels. We adapt a ReLU extraction implementation to Leaky ReLU, compare sign-search methods, and estimate biases and output layers. We prove conditional bounds for direction recovery with approximate prefixes, preservation of local distance votes, prediction changes from aligned parameter errors, and sign selection with independent scoring data. We also specify exact row restoration and distinguish its guarantee from that of gradient masking. The experiments evaluate assisted extraction, with privileged access to gradients, hidden activations, and victim parameters, followed by label-based reconstruction. Across eight search seeds on the largest synthetic architecture, Leaky ReLU recovers 51--57 neurons in the deepest hidden layer, while ReLU recovers none. This advantage does not hold uniformly across architectures and layers. Removing victim-weight access from the sign walk gives less accurate signs, despite high final prediction agreement. Across 40 seeded runs on the two smallest synthetic victims, agreement on 5,000 inputs excluded from fitting and selection ranges from $0.9890$ to $0.9992$. On two CIFAR-10 victims, the reconstructed models achieve $56.40\%$ and $58.29\%$ agreement and exceed the distillation baseline on three functional metrics. We report label requests separately from privileged access and explain why prediction agreement does not identify network parameters.

---


### 122. [Meta-CLIP: Metadata-Conditioned Contrastive Learning for Zero-Shot Disease Inference](https://arxiv.org/abs/2610.33674)

**<font color=#1a73e8>作者：</font>** Haozhe Luo, Nirosh Sivanesan, Shelley Zixin Shu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical vision--language pretraining learns transferable representations from paired images and radiology reports, yet differences in scanners and acquisition protocols can impair transfer. Existing approaches primarily enrich clinical semantics, leaving structured acquisition information in DICOM headers underused. We introduce Meta-CLIP, a metadata-conditioned contrastive framework that uses acquisition similarity to reweight cross-modal negatives during pretraining. A kernel over numerical and categorical DICOM fields defines a bounded pairwise margin. This margin increases the contribution of acquisition-similar negatives, emphasizing distinctions among studies that share imaging conditions. The kernel remains fixed during image--text optimization, and inference follows the standard dual-encoder architecture without requiring metadata. We evaluate Meta-CLIP on chest radiography and volumetric chest CT through zero-shot classification, appearance perturbations, grounding, and representation analyses. On CT-RATE, Meta-CLIP improves macro-AUROC over CT-CLIP by 1.41 points, with a 95\% paired bootstrap confidence interval of 0.96--1.85 points. It also achieves the highest macro-AUROC on four of five CXR benchmarks. An exploratory BrgSA evaluation extends the analysis to another CT backbone. These findings support acquisition metadata as a practical training-time prior for medical vision--language learning. Code will be made publicly available upon publication.

---


### 123. [PACE: Research Proving Agent for Adaptive Conjecture Exploration](https://arxiv.org/abs/2610.33690)

**<font color=#1a73e8>作者：</font>** Shu Miao, Feiming Wang, Wentao Long 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many mathematical research agents focus on solving problems with fixed statements. However, conjecture research, especially in applied mathematics, may require revising candidate questions or conclusions as investigation proceeds, coupling problem formulation with proof development. We present PACE, a research-proof agent that supports this process through a structured research loop that selects mathematical objectives and develops or challenges candidate mechanisms. The whole prover constructs proofs from these mechanisms, and an independent verifier checks them against the original target. Evidence-tracking memory stores assumptions and dependencies arising during research and marks evidence for revalidation when a candidate or condition changes. This memory supports task-specific context composition that keeps checked premises, exploratory material and unresolved obligations distinct. To evaluate proof construction and conjecture research, we introduce ResearchProofBench, an applied-mathematics benchmark focused on optimization, comprising 51 known-proof tasks with 331 hidden checkpoints under historical abstract access and six open-problem cases. The known-proof tasks assess reconstruction of published results, while the open-problem cases assess mathematical investigation and proof development. On the 51 known-proof tasks, PACE achieves an aggregate Proof Score of 75.16 and completes 20 proofs. In conjecture research, PACE develops conditional results, with its submissions receiving higher review scores than the compared baselines.

---


### 124. [Embedding-Based Educational Taxonomies](https://arxiv.org/abs/2610.33694)

**<font color=#1a73e8>作者：</font>** Kia Karbasi, Kaveh Karbasi, Gregory Pottie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Educational taxonomies organize educational content, such as exercise problems, into concepts, which are also called skills or knowledge components. These taxonomies define learning objectives in educational applications such as intelligent tutoring systems. Developed through human expertise and iterative refinement, they also provide fundamental structure for curricula, assessment, and models of student learning. Recent advances in semantic text embeddings make it possible to construct alternative educational taxonomies computationally from the content itself. In this paper, we investigate this possibility by clustering embeddings of math questions to construct embedding-based educational taxonomies. We compare these taxonomies with the existing Common Core State Standards (CCSS)-based knowledge-component taxonomies in two ASSISTments datasets and evaluate their utility in Deep Knowledge Tracing, a downstream task that relies on taxonomic mappings of questions to knowledge components. The embedding-based taxonomies exhibit substantial but incomplete correspondence with the existing taxonomies, revealing both preserved and alternative organizations of educational content. When used for knowledge tracing, they improve predictive performance by approximately 3-5 AUC percentage points. These results demonstrate the potential of semantic embeddings for automatically constructing educational taxonomies that both recover structure present in human-developed taxonomies and provide useful alternative representations for downstream educational modeling.

---


### 125. [Scalable Unrolled Chains for MRI Reconstruction](https://arxiv.org/abs/2610.33695)

**<font color=#1a73e8>作者：</font>** Emiljo Mëhillaj, Ender Konukoglu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unrolled variational networks achieve state-of-the-art performance for accelerated MRI reconstruction, but standard end-to-end training becomes prohibitively memory intensive as the number and width of cascades increase. We propose a memory-efficient training framework that updates a randomly sampled cascade while retaining supervision from the final reconstruction loss. The error signal is propagated from the end of the chain to the sampled cascade using an activation-light backward pass that avoids storing full chain activations, thereby decoupling training memory from chain length. A time-conditioned network shared across cascades further keeps the parameter count independent of chain length. The backward pass is approximate only through frozen normalization statistics, and a trained exact gradient control shows the approximation leaves reconstruction quality unchanged. The framework remains trainable at chain lengths and cascade widths where standard end-to-end backpropagation exhausts GPU memory. On fastMRI single-coil knee and multi-coil brain reconstruction, our method consistently outperforms other local training approaches. On high-SNR knee slices, our method surpasses E2E-VarNet at $8\times$ and matches it at $4\times$, while on the complete brain validation set it surpasses E2E-VarNet at $8\times$ and achieves comparable performance at $4\times$, with fewer parameters, lower peak memory, and faster per-iteration training. Code is available at this https URL.

---


### 126. [E3tereo: Improving Stereo Matching at Depth Boundaries with Learned Geometric Edges](https://arxiv.org/abs/2610.33704)

**<font color=#1a73e8>作者：</font>** Qi Xiong, Qinghua Zhao, Yongqiang Xi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth boundaries remain a major source of error in stereo matching. For IGEV on Scene Flow, geometric edge pixels account for only 6% of evaluated pixels but about half of the total absolute disparity error. Photometric edges can respond to texture changes without corresponding depth discontinuities, making them unreliable cues for boundary refinement. We propose E3Stereo, which learns geometric edges from disparity supervision and combines these boundary cues with the backbone disparity and image details to predict full-resolution disparity corrections. The same edge map also emphasizes boundary errors during training, while joint optimization allows the edge predictor to adapt to disparity refinement. On the Scene Flow dataset, E3Stereo reduces end-point error (EPE) at depth boundaries by 9.5%-14.3% across RAFT-Stereo, IGEV, and MonSter, while also reducing overall EPE. After fine-tuning, our IGEV-based model improves upon IGEV on all eleven reported metrics across ETH3D, KITTI 2012, and KITTI 2015. The source code will be made publicly available upon acceptance.

---


### 127. [Traffic-Context-Aware Driver Emotion Recognition with Expectation-Deviation-Driven Inference](https://arxiv.org/abs/2610.33713)

**<font color=#1a73e8>作者：</font>** Longhao Yan, Jinhao Liang, Kaidi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driver emotion provides an important indication of how drivers perceive and evaluate ongoing traffic situations, making reliable emotion recognition an important capability for effective human-vehicle interaction. Yet, most existing driver emotion recognition approaches rely primarily on in-cabin images and overlook how surrounding traffic interactions shape driver emotional responses. To address this limitation, we propose a traffic-context-aware driver emotion recognition (TADER) framework that integrates in-cabin signals with out-of-cabin traffic scenarios, modeling driver emotions as arising from expectation deviation represented by the discrepancy between predicted and observed vehicle trajectories. The proposed framework comprises two key components: (1) a vision-based base recognizer that extracts spatiotemporal representations from in-cabin facial images to infer driver emotions, and (2) a traffic-context-aware fusion module that quantifies expectation deviation from external traffic scenarios and integrates it into the base recognizer via attention-based embedding fusion. To overcome the scarcity of paired in-cabin and out-of-cabin data, we introduce a transfer learning strategy that transfers a trajectory prediction model trained on large-scale naturalistic datasets to smaller paired datasets. Extensive experiments demonstrate that TADER consistently outperforms state-of-the-art methods across both naturalistic and simulated driving environments by incorporating traffic context information into emotion recognition, resulting in improvements of 5% in accuracy on the AIDE and manD datasets.

---


### 128. [Latent dynamics for reconstructing fine-scale PDE trajectories from coarse observations](https://arxiv.org/abs/2610.33722)

**<font color=#1a73e8>作者：</font>** Chenhao Si, Zishan Qian, Shing-Tung Yau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coarse PDE observations omit spatial detail and intermediate states of evolving fields. We present Structured Latent Dynamics (SLD), a framework that reconstructs high-resolution trajectories from spatially and temporally downsampled simulations. SLD interpolates the input in time, adds a learned temporal correction and uses the resulting sequence to guide a hidden state on the coarse grid. Each update of the latent state combines a learned gated response with horizontal and vertical central differences and a five-point Laplacian of the state. The three spatial terms have learned channel-wise coefficients. Two Haar wavelet synthesis branches map the hidden state and refined coarse input to the high-resolution field. We evaluate SLD on two-dimensional Gray--Scott, complex Ginzburg--Landau and viscous Burgers systems, reconstructing 100 output frames from 25 input frames with eightfold refinement in each spatial direction. SLD achieves lower mean relative $L_2$ error and mean absolute error than unstructured latent dynamics and ConvLSTM baselines with comparable parameter counts, both on held-out trajectories and on later windows of trajectories used during training. SLD also reduces errors in regions with large reference gradients and across most or all of the evaluated later time intervals. A representative Gray--Scott comparison shows lower spectral error over most intermediate and high wavenumbers. Removing the fixed spatial response increased reconstruction error, supporting its contribution to the SLD architecture.

---


### 129. [Human-Feedback-Guided Multi-Agent Inverse Reinforcement Learning for Interactive Driving Behavior Modeling](https://arxiv.org/abs/2610.33726)

**<font color=#1a73e8>作者：</font>** Longhao Yan, Jinhao Liang, Kaidi Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modeling human driving behavior is fundamental to understanding driver decision-making and supporting autonomous vehicles (AVs) in mixed traffic. Reward learning offers a principled way to infer the latent objectives behind driving behaviors, yet most existing methods are formulated in single-agent settings and treat surrounding vehicles as dynamic obstacles. Directly extending reward learning to multi-agent scenarios is difficult because the joint action space grows exponentially with the number of interacting vehicles. In addition, existing approaches mainly rely on physical demonstrations and rarely exploit human feedback during reward recovery. To address these limitations, this paper proposes a Human-Feedback-Guided Multi-Agent Inverse Reinforcement Learning (HFG-MAIRL) framework for interactive driving behavior modeling. First, we develop a multi-agent maximum-entropy inverse reinforcement learning module that explicitly models each vehicle and its directly interacting neighbors in a localized Markov game, while using aggregated traffic states to capture the influence of the broader traffic environment. The resulting coupled multi-vehicle responses are approximated through finite marginal-response iterations over factorized vehicle-level policies, avoiding explicit enumeration of the full joint action space. Second, we incorporate human feedback as ordinal preference supervision through a Bradley-Terry likelihood. In our experiments, driver emotion labels are used as one instantiation of such feedback and converted into pairwise ordinal preference constraints. Experiments on the AIDE dataset show that HFG-MAIRL outperforms representative IRL baselines in decision modeling and produces interpretable feedback-aligned reward patterns.

---


### 130. [How Geometry Shapes Generative Model Evaluation on Riemannian Manifolds](https://arxiv.org/abs/2610.33731)

**<font color=#1a73e8>作者：</font>** Misha Oberski, Valentijn Oldenburg, Xanthos Kekkos 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On Riemannian manifolds, generative-model evaluation is geometry-dependent since curvature and dimension jointly determine distances and volume growth. Our framework systematically compares geodesic, ambient, and tangent-space versions of Wasserstein and MMD across different geometries. Using controlled-noise perturbations and Riemannian Flow Matching samples, we study metric agreement, noise sensitivity, and their relation to geometry-induced volume scaling. We find that no metric is uniformly reliable: evaluation distance can affect both measured discrepancies and noise sensitivity, varying across curvature and dimension. Our analysis leads to practical recommendations for reporting evaluation distances, comparing metric types, and calibrating metrics to the geometry of the samples.

---


### 131. [A SegFormer-based model for spatial Daylight Factor prediction with comprehensive obstruction encoding and regulatory validation](https://arxiv.org/abs/2610.33737)

**<font color=#1a73e8>作者：</font>** Stanislava Fedorova, Alejandro Pacheco Diéguez, Christoph Berkmiller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Daylight compliance assessment in residential buildings requires time-consuming raytracing simulations and specialist model preparation, limiting its integration into iterative architectural design. We present a machine learning-based methodology for predicting the spatial distribution of the Daylight Factor (DF) directly within Building Information Modelling (BIM) environments, delivering results in seconds without model export or manual curation. The approach addresses five gaps not jointly covered by any existing model: external obstruction encoding including balconies, own building height, variable material reflectances, non-orthogonal room geometries, and regulatory validation. Two models are developed: a default-materials model with fixed reflectances for preliminary design checks, and a custom-materials model with variable project-specific reflectances. Both are trained on about 20,000 synthetic Radiance-simulated rooms and validated on a held-out synthetic dataset and 102 rooms from 18 real building models. The default-materials model achieves $\delta_1$ = 83.4% and MAE = 0.11% DF on synthetic data, and on real buildings predicts BBR (Swedish) compliance area within 4.85 pp MAE (bias +2.31 pp) and TEK17 (Norwegian) mean room DF within 0.304% DF MAE (bias +0.287% DF). The custom-materials variant shows 1.7-2.4$\times$ higher error across all metrics. Both models concentrate accuracy in the BBR compliance-critical zone (DF < 1%), achieving a sub-1% DF MAE of 0.105% DF and Compliance IoU of 0.883 on real buildings. All cases where compliance is overestimated are borderline, within 10.7 pp of the BBR threshold (median 3.2 pp) and 0.36% DF of the TEK17 threshold (median 0.10% DF). The default-materials model is recommended as a replacement for preliminary daylight simulations; the custom-materials variant requires further development before use in final compliance verification.

---


### 132. [Polynomial Residual Networks are Generically Identifiable](https://arxiv.org/abs/2610.33738)

**<font color=#1a73e8>作者：</font>** Isabel Dahlgren, Giovanni Luca Marchetti, Kathlén Kohn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove identifiability results for constant-width residual networks with polynomial activations and bias terms. For activations of degree at least five with generic coefficients, the fiber over a generic parameter is a singleton. For activations of degree at least three with no linear term after a suitable translation of the input, the generic fiber is given by translating biases and then scaling weights and translated biases by real roots of unity. These results specialize to networks without bias terms. With the same proof technique, we further derive necessary conditions for critical points of the ResNet parametrization, that are central in singular learning theory.

---


### 133. [A quantum k-nearest neighbors implementation using magnitude-aware comparisons](https://arxiv.org/abs/2610.33739)

**<font color=#1a73e8>作者：</font>** Christopher Rector, Jiangwen Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Much attention has recently been devoted to the k-nearest neighbors (KNN) algorithm as a case study for quantum computing algorithms. Several algorithms have devised methods to compute a similarity metric to solve Quantum KNN (QKNN). This paper presents a practical quantum encoding technique that enables Euclidean distance calculation between vectors with different L2 norms by appending a single component to each vector, then uses it in the QKNN problem. It is arguably simpler to understand and implement than comparable methods and uses fewer qubits. Further, an implementation of this algorithm is provided and is used to benchmark it against a recent Euclidean-distance QKNN method on standard labeled datasets. In addition to demonstrating proper formulation, the results show marked improvement over similar implementations during simulation with realistic noise due to the use of fewer qubits and thus more coherent circuits.

---


### 134. [Refined Assessment for Translation Evaluation: Rethinking Machine Translation Evaluation in the Era of Human-Level Systems](https://arxiv.org/abs/2610.33749)

**<font color=#1a73e8>作者：</font>** Dmitry Popov, Vladislav Negodin, Ekaterina Enikeeva 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As machine translation systems approach human-level quality, traditional evaluation methodologies struggle to detect subtle translation errors. We critically examine limitations in current gold-standard approaches (MQM and ESA), including inconsistencies from variable annotator expertise, excessive categorization complexity, coarse severity granularity, accuracy bias over fluency, and time constraints. To address this issue, we introduce a high-quality dataset consisting of human evaluations for English-Russian translations from WMT24, created by professional linguists. We show that expert assessments without time pressure yield substantially different results from standard evaluations. To enable consistent and rich annotation by these experts, we developed the RATE (Refined Assessment for Translation Evaluation) protocol. RATE provides a streamlined error taxonomy, expanded severity ratings, and multidimensional scoring balancing accuracy and fluency, facilitating deeper analysis of MT outputs. Our analysis, powered by this expert dataset, reveals that state-of-the-art MT systems may have surpassed human translations in accuracy while still lagging in fluency - a critical distinction obscured by existing accuracy-biased metrics. Our findings highlight that advancing MT evaluation requires not only better protocols but crucially, high-quality annotations from skilled linguists.

---


### 135. [Computer Vision Navigation for an Autonomous Vehicle Model Using Reinforcement Learning](https://arxiv.org/abs/2610.33755)

**<font color=#1a73e8>作者：</font>** Dinis Fernandes, Tiago Ribeiro, António Ribeiro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work aims to assess the capabilities of the reinforcement learning algorithm, Proximal Policy Optimization (PPO), in developing a policy capable of controlling the speed and steering angle of a vehicle model to navigate within simulated road lines.
The control system's input is a camera, and its outputs are the rotational speed of the rear wheels and the steering angle of the front wheels, controlling the vehicle's speed and direction, respectively. The algorithm is trained and tested in a simulated environment, where it receives image frames from the vehicle's camera, processes them through a feature extraction algorithm, and feeds them into the policy. For each frame, the policy outputs speed and direction commands for the vehicle. The policy is iteratively updated to enhance its performance.
The reinforcement learning algorithm successfully generates a policy capable of navigating the vehicle in a simplified environment. Potential improvements are suggested to enhance the system's robustness in more complex scenarios.
Creating a simulation environment suitable for testing an advanced reinforcement learning algorithm is a complex task. This project offers a framework for other developers to test different approaches and algorithms. The tested algorithm, PPO, uses proximity intervals - an innovative approach in reinforcement learning. In some scenarios, the algorithm achieved better performance than predecessor algorithms, which are typically harder to implement and require tuning more hyperparameters.

---


### 136. [Road Infrastructure Perception for Autonomous Driving: Taxonomy, Representations, Tasks, and Challenges](https://arxiv.org/abs/2610.33758)

**<font color=#1a73e8>作者：</font>** Guoyang Zhao, Weiqing Qi, Kai Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road infrastructure perception is a fundamental component of autonomous driving, as it recovers the structured road elements that define roadway geometry, delimit operational space, and encode traffic regulations. Although individual tasks such as lane detection, drivable-space estimation, traffic-sign recognition, and online map construction have been extensively studied, the field remains fragmented across task definitions, sensing assumptions, output representations, datasets, and evaluation protocols. This survey provides a function-oriented synthesis of road infrastructure perception. We first clarify its scope and organize existing studies into three complementary categories: geometric-structural, functional-spatial, and regulatory-semantic infrastructure. Based on this taxonomy, we review sensing modalities, scene representations, representative methods, benchmarks, and evaluation protocols, emphasizing the field's evolution from image-space recognition toward metric, vectorized, topology-aware, occupancy-based, and rule-grounded scene modeling. We further examine how representation choices affect evaluation and downstream usability, revealing limitations of current benchmarks in relation reasoning, temporal consistency, robustness, and planning-oriented assessment. Finally, we discuss open challenges and future directions toward unified infrastructure representation, open-environment generalization, relation- and rule-aware reasoning, and downstream-oriented evaluation. By connecting tasks, representations, and evaluation under a common functional framework, this survey aims to establish road infrastructure perception as a coherent foundation for map-compatible and behavior-relevant autonomous-driving scene understanding.

---


### 137. [C-DFF: Concept-Level Diagnostics for Mechanism Parity in Simulation-Based Validation of Autonomous Driving Perception](https://arxiv.org/abs/2610.33760)

**<font color=#1a73e8>作者：</font>** Danial Safaei, Siddartha Khastgir, Matthew Higgins 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simulation is widely used in autonomous-driving validation, but matching task outputs between real and synthetic images does not guarantee that a system relies on the same visual evidence. This creates a validation gap for transfer, especially in safety-critical perception functions. We present Concept-Decisive Feature Fidelity (C-DFF), a concept-level mechanism-parity diagnostic for paired real-synthetic evaluation. Starting from decisive evidence extracted from a frozen system-under-test (SUT), C-DFF projects that evidence into a shared semantic concept space using off-the-shelf segmentation and compares real and synthetic concept-importance vectors. The result is not only a scalar mechanism-parity score, but also a concept-shift diagnostic that identifies which scene concepts become more or less decisive in simulation. We evaluate C-DFF on KITTI $\leftrightarrow$ Virtual KITTI 2 with 2126 matched pairs across three frozen SUTs (steering regression, YOLOP drivable-area, YOLOP lane-line). Across these tasks, C-DFF is SUT-discriminative and yields interpretable concept-level summaries that support validation triage and simulator debugging. When reported alongside task-specific output-value context metrics, C-DFF shows that output agreement does not by itself establish mechanism parity. These results position C-DFF as a practical semantic diagnostic layer for validation and verification workflows in simulation-based AV testing.

---


### 138. [CFL-aware edge design for graph neural solvers of hyperbolic transport](https://arxiv.org/abs/2610.33769)

**<font color=#1a73e8>作者：</font>** Jinyoung Jeong, Joseph B. Choi, Xinlun Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic partial differential equations (PDEs) transport information at finite speed along characteristics, often producing shocks and discontinuities that are challenging to capture numerically. Graph neural networks (GNNs) offer learned update rules, but neighbor aggregation alone does not tell a GNN how far information must travel and along which edge. As a result, when a GNN model takes a time step larger than what was used in training, shock fronts smear and oscillations grow. In this work, we ask whether making the scale of transport explicit as an edge-local Courant-Friedrichs-Lewy (CFL) signal can enhance GNNs' ability to model hyperbolic PDEs. Holding the architecture fixed, we vary only the information given to each edge, from a raw edge form to forms that progressively expose the edge-local transport interaction through direction, length, and wave speed. Because all of these are computed from the same ingredients, what changes is not the amount of information but its form. The results show a consistent pattern, in which feature count is not the limiting factor, and appending CFL directly to a raw edge form produces almost no benefit. The CFL conditioning proves most effective when the edge information already exposes the transport interaction, reducing final-step error by 10.4-14.4%, and the improvement widens as the step size grows larger. Notably, this improvement arises not from smearing the solution but from suppressing oscillations near shocks. These results point to a specific design principle that CFL conditioning is most effective when the edge representation already separates the direction of interaction from spatial scale, so that the CFL value has a well-defined quantity to modulate.

---


### 139. [Greedy Orthogonal Polynomial Manifolds with Lipschitz Control for Dimensionality Reduction and Reduced Modeling](https://arxiv.org/abs/2610.33784)

**<font color=#1a73e8>作者：</font>** Tomoki Koike, Benjamin Peherstorfer, Elizabeth Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Polynomial manifolds provide nonlinear low-dimensional representations through polynomial decoders. We propose to represent the polynomial terms of the decoder using features that are orthonormal on the training data. This empirical orthogonality enables a greedy algorithm, Greedy-OPM, which jointly selects encoder modes and polynomial features while minimizing the reconstruction error under a prescribed bound on the decoder's Lipschitz constant. Numerical experiments show that this Lipschitz constraint improves generalization away from the training data while retaining high reconstruction accuracy.

---


### 140. [Segmentation of Moving Objects During Camera Motion Using the OWL Function](https://arxiv.org/abs/2610.33789)

**<font color=#1a73e8>作者：</font>** Daniel Raviv, Juan D. Yepes  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a principled, analytical framework for segmenting multiple independently moving rigid objects during single camera motion, built directly upon the OWL perception function. OWL encodes two fundamental visual motion cues, perceived looming $L$ and perceived rotation $\omega$, into a single closed-form representation of relative 3D structure. A key consequence of this structure is that the unit direction of relative translation $\hat{t}$ is analytically recoverable per image point from $L$ and $\omega$ alone. All points belonging to a non-rotating rigid body share the same $\hat{t}$, whereas points on different rigid bodies generally yield distinct values. This furnishes a natural segmentation criterion: clustering per-point $\hat{t}$ estimates partitions the visible scene into independently moving rigid bodies. Building on the 2D complex form of OWL, we derive the framework in 3D using quaternions, for a single moving camera. The approach is parallel, camera rotation-invariant, and requires no training data, no depth information, and no semantic priors.

---


### 141. [Whispers from the Neighbors: Rethinking Caption Consensus as Inference-Time Evidence for Vision-Language Retrieval](https://arxiv.org/abs/2610.33798)

**<font color=#1a73e8>作者：</font>** Khang Nhat Hoang Vo, Belal Shoer, Abhirama Subramanyam Penamakuri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An image is rarely described only once. Retrieval benchmarks and many collections attach several captions to each picture, yet dual encoders still judge every image-caption pair in isolation. We ask what these neighboring captions contribute when a frozen encoder consults them at inference time. Fusing image similarity with similarity to an image's own captions improves text-to-image R@1 by 3.4 to 16.8 points across nine frozen encoders when the captions come from the same annotators as the queries. The gain falls to 1.9 to 7.2 points when an off-the-shelf captioner writes them, and to at most one point when they come from a different annotation source; a paraphrase-trained text encoder strengthens the text side further. A natural refinement, scoring the part of the image that the captions leave unexplained, appears to add much more under a leave-one-out evaluation. We show that this advantage arises because the correct candidate's supports are built differently from those of the negative candidates, with set size and query removal each contributing about half, and that under a fixed support index the residual reduces to a reweighting of what the captions already provide. On compositional benchmarks, the captions help by matching candidates to human descriptions of the image, without improving image-text grounding. The code is available at: this https URL

---


### 142. [Beyond Static Structures: Linking Protein Dynamics to Function via DynaReason-Pro](https://arxiv.org/abs/2610.33804)

**<font color=#1a73e8>作者：</font>** Zhaokang Liang, Mingze Yuan, Quanzheng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intrinsically disordered proteins (IDPs) carry out their functions through heterogeneous conformational ensembles that reflect their dynamics, yet most protein function prediction methods rely on sequence or a single static structure. To this end, we introduce DynaReason-Pro, the first framework to jointly predict GO terms from conformational ensembles and generate natural-language functional rationales. We evaluate DynaReason-Pro on a curated IDP benchmark from the Protein Ensemble Database (PED), with sequence- and structure-cluster-disjoint splits to prevent data leakage. Variability-stratified evaluation shows the clearest gains in the high-conformational-variability regime.

---


### 143. [Grounded Exploration for Open-Ended Image Editing](https://arxiv.org/abs/2610.33810)

**<font color=#1a73e8>作者：</font>** Jieyu Zhou, Mehdi Ben Ayed, Shubham Gupta 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-ended image-editing requests, such as ``decorate this room,'' admit multiple valid realizations. Direct sampling may produce ungrounded variation, whereas explicit diversity prompting often produces superficial differences. We study how to ground these requests without prematurely eliminating their legitimate ambiguity. We introduce a two-stage framework that first identifies diverse, feasible edit scopes and then realizes them as executable edit instructions. Across 300 open-ended image-editing tasks, our approach achieves 24.6% higher mean semantic dispersion and 17.1% higher mean groundedness than direct diversity prompting, while producing more valid and distinct realizations. These results show that structuring feasible edit directions before realization supports more useful grounded exploration.

---


### 144. [Memory or a Clock? Auditing a Memory Advantage in XLand-MiniGrid with Seeds, Maps and Evaluation Noise Apart](https://arxiv.org/abs/2610.33816)

**<font color=#1a73e8>作者：</font>** Rodrigo Reveron-Fonseca  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On a partially observable XLand-MiniGrid task, an LSTM agent beats a memory-free MLP by 25 percentage points. The gap looks like a clear case of memory. We ask two questions about it. First, how much of a measured gap is noise? Separating training seed, map and evaluation randomness in 60 runs, each re-evaluated three times, we find that about ten paired seeds detect a 10-point gap in final success. The binary "task acquired" verdict, a common summary of learning curves, is 76% evaluation noise and would need about a hundred seeds for the same gap. Second, is the gap memory? On a sealed panel of new maps, opened once, a memory-free MLP of the LSTM's size comes within 3.3 points of the LSTM when it is given the time step, and gains no measurable benefit from its width without it. With the time step, an MLP a quarter of the LSTM's size, and the LSTM with its state erased at every step, also come within about 5 points. A linear probe reads the time step from the trained LSTM's state. On this task, most of the apparent memory advantage is an advantage of knowing the time, which matters because episodes are cut at a fixed limit and the reward shrinks with time. We recommend giving memory-free baselines the time step, and we release the protocol, the event-driven tooling and every checkpoint.

---


### 145. [EEGBiFormer: Real-Time EEG Attention Classification via Hybrid CNN-Transformer with EEG-Informed Auditory Protocol Validation](https://arxiv.org/abs/2610.33832)

**<font color=#1a73e8>作者：</font>** Isabella Guan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sustained attention is critical for academic performance, yet existing auditory support tools are static and not grounded in real-time neural evidence. This paper presents EEGBiFormer, a hybrid CNN-Transformer model for realtime binary classification of attention states, focus versus nonfocus, from 16-channel EEG signals. A custom analog front-end acquisition board was designed and built to collect a task-based EEG dataset. Before model training, spectral and connectivity analysis, using Power Spectral Density and Phase Locking Value, confirmed distinct neural signatures between attention states, providing physiological grounding for the classification approach. EEGBiFormer achieved 91.3 percent window-level validation accuracy with an F1 score of 94.5 percent, and 88.2 percent recording-level accuracy across 17 independent sessions. End-to-end system latency was measured below 100 ms, supporting real-time responsiveness. The trained model was further used to objectively rank auditory stimuli by focus-state confidence, yielding EEG-informed audio protocols. In a paired within-subject behavioral study with 37 participants, these protocols produced a statistically significant 20 percent improvement in composite attention scores over silent controls, with a medium-to-large effect size. This work demonstrates a complete pipeline from custom EEG hardware through neural signal analysis, deep learning classification, and evidence-based auditory protocol design.

---


### 146. [Hessian-Similar Optimization with Capped Participation: Lower Bounds and Virtual Masters](https://arxiv.org/abs/2610.33835)

**<font color=#1a73e8>作者：</font>** Rui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What is the round complexity of Hessian-similar optimization when each round can contact at most $s$ of $m$ clients? Prior rates permit a free master or full participation and do not characterize strict caps. We count every one-vector query and reply. A hidden-client chain gives a lower bound for zero-respecting local algorithms with adaptive cohorts and random stopping: on strongly convex quadratics, the required rounds are $\Omega((m/s)\sqrt{\min\{\delta_a,\bar\delta/\sqrt m\}/\mu}\,\log(1/\epsilon))$ for $s\leq(m-2)/2$ in the high-accuracy, high-dissimilarity regime. Here $\mu$ is strong convexity, while $\delta_a$ and $\bar\delta$ bound anchor and average Hessian variation. To remove dependence on a poor anchor, virtual-master SVRS uses independent estimator and proximal cohorts and averages the proximal replies. With Catalyst, it reaches relative gap $\epsilon$ in $\tilde O(m/s+(\sqrt{m/s}+m^{3/4}/s)\sqrt{\bar\delta/\mu})$ expected rounds on quadratics with strongly convex clients, independent of $\delta_a$. Combining this method with charged analyses of existing algorithms matches the lower bound's polynomial dependence for $s\leq\sqrt m$ and $s=\Omega(m)$; the worst gap is $O(m^{1/8})$. A held-out 12-seed synthetic study finds fewer rounds than tuned SVRP in nine of ten dip-family incomplete-cohort cells, versus two of 30 other cells. The lower bounds concern zero-respecting algorithms and do not cover unrestricted messages.

---


### 147. [Approximate Universal Prediction under Interaction](https://arxiv.org/abs/2610.33842)

**<font color=#1a73e8>作者：</font>** Richard Cornelius Suwandi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian mixtures, and Solomonoff induction in particular, provide an idealized model of prediction learned by minimizing population log loss, and they underlie universal agents such as AIXI. An agent that plans with an approximation of such a predictor decides where that predictor is evaluated, and a planner can be drawn toward branches on which its model is optimistic. We study which approximation guarantees survive this feedback. For normalized finite-horizon causal mixtures, the transfer coefficient factors into a policy likelihood ratio and task evidence available before each prediction, so task rarity and action-branch rarity can compound. Within one fixed universal mixture, infinitely many computable environments admit excess prediction error of order $\kappa\eta\,2^{K(\mu)}$, where $\eta$ is the training KL budget and $\kappa$ measures policy coverage. This order is sharp, and for each target a computable predictor attains it at a suitable finite horizon, so computability alone does not remove the penalty. For bounded returns, value error is controlled by the probability of entering a poorly covered branch plus a square-root term in $\eta$. Both terms are necessary, and finite maximum coverage ratios are not required. Motivated by the mentor override of Golden Handcuffs, we derive margins for preserving deferral decisions and conditional KL budgets with an unavoidable inverse-history-probability penalty, and a counterexample separates agreement of deferral decisions from task-wise event avoidance. The guarantees apply to any predictor architecture that meets explicit population approximation and coverage conditions, which gives concrete targets for implementing idealized universal agents.

---


### 148. [When is early stopping beneficial under label noise? A phase diagram for kernel gradient flow](https://arxiv.org/abs/2610.33846)

**<font color=#1a73e8>作者：</font>** Fabrizio Boncoraglio, Lenka Zdeborová  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early stopping is commonly used to prevent fitting label noise from degrading generalization. Does this mean that, when a positive fraction of the training labels is intrinsically unpredictable, the best test error must occur before interpolation? Experiments on a CIFAR10 classification task with randomly labeled examples motivate the opposite possibility: although fixed-feature and shallow models exhibit late-time deterioration of the test error, the need for early stopping essentially disappears in larger, deeper convolutional networks even after the random labels have all been classified correctly. We determine when late-time deterioration disappears entirely in a solvable setting. For kernel gradient flow on a synthetic noisy classification task, we derive sharp high-dimensional learning curves and obtain a phase diagram controlled by the balance between the linear kernel component that learns the shared relation between inputs and labels and the higher-order components that enable fitting the label noise. In one regime, generalization is optimized at finite time and early stopping is necessary. In another, generalization improves until interpolation, but the endpoint is suboptimal across kernels. At the boundary, the interpolating endpoint attains the lowest generalization error across the considered kernel family and all training times. Thus, even with extensive irreducible label noise, interpolation can outperform early stopping. The neural-network experiments leave open how learned representations acquire an analogous favorable geometry.

---


### 149. [TrackTok: Object-Centric Video Tokenization with Semantically Persistent Tokens](https://arxiv.org/abs/2610.33857)

**<font color=#1a73e8>作者：</font>** Nhi Pham, Christopher Wewer, Bernt Schiele 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce TrackTok, an efficient video tokenization framework that produces object-centric tokens, i.e., tokens that consistently encode the same semantic objects across time, even as it moves, deforms, or undergoes partial occlusion. Conventional patch-based or existing holistic tokenizers produce token identities often tied to fixed image locations. In contrast, our approach learns temporally persistent object-centric representations that bind visual features across frames into stable semantic units. This enables substantially more compact, continuous latent video representations, reducing the number of tokens required for downstream generative modeling with state-of-the-art flow models, while preserving the semantic structure needed for high-quality synthesis. Our tokenizer offers a favorable quality-efficiency trade-off. TrackTok achieves comparable class-conditional generative FVD on UCF-101 dataset at 8 times fewer latent tokens and better latency, and outperforms existing 1D tokenization baselines on frame prediction task on Kinetics-600 across low token budgets. These results suggest that object-aligned and temporally persistent tokenization is a promising direction for scalable video generation, where reducing latent token counts is critical for efficient modeling. Our code for this work is available at this https URL.

---


### 150. [Numina Fuse: Interactive Autoformalization in Lean 4](https://arxiv.org/abs/2610.33860)

**<font color=#1a73e8>作者：</font>** Justin Asher, Yichuan Cao, Ruichen Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Numina Fuse is an agent-native application for formalizing mathematics in Lean 4. Since Lean can compile while not representing its intended informal meaning, and agents now write Lean faster than people can read it, we built Fuse around human supervision of agent work. A user works with an AI orchestrator on a Lean project and supervises it through views of the blueprint, the dependency graph, and the Lean code, while the backend keeps the project's derived state and runs agents for hours without the user present. We describe the development of Fuse throughout 2026, as it moved from a prescribed pipeline of agents paced by human review to an orchestrator that dispatches specialists, provers, and parallel children on its own. We designed for this shift, keeping project state, tooling, and interface design separate from orchestration so that agents could take over more of the work as models improved. We report Fuse's use in a formalization of the three-dimensional Kakeya conjecture and a study of prover models. We close with lessons for the next generation of autoformalization systems. Fuse Desktop, an open-source local version, is available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
