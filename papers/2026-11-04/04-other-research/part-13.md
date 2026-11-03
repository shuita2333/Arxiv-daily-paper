# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**601-633**（第 13/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-633**

---

### 601. [Temporal Island Sparse Autoencoders for Interpreting Clinical Time-Series Models](https://arxiv.org/abs/2611.03420)

**<font color=#1a73e8>作者：</font>** Muhan Yeo, Bong Gyun Kang, HyunGi Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models for electronic health records achieve strong predictive performance but provide little insight into what clinical concepts they represent internally. Post-hoc attribution methods produce per-cell importance scores that lack temporal coherence, cross-variable structure, and reusability across patients. We introduce the Temporal Island Sparse Autoencoder (TI-SAE), which learns a backbone-specific, patient-shared clinical concept dictionary from a frozen predictive model's representations. Each dictionary entry (latent) is defined by learned temporal Gaussian islands (specifying when the concept is active) and a sparse variable-composition vector (specifying which variables are involved). A decoupled selector then identifies which dictionary entries drive each patient's prediction, separating representation learning from attribution. We evaluate TI-SAE across five backbone architectures spanning different representation strategies on MIMIC-III and MIMIC-IV (three prediction tasks each). TI-SAE produces structured clinical concepts that go beyond transient attribution heatmaps while achieving strong performance on standard faithfulness benchmarks.

---


### 602. [Circumventing Magnitude Collapse via Modular Two-Stage Open-Set Recognition](https://arxiv.org/abs/2611.03421)

**<font color=#1a73e8>作者：</font>** Laurin van den Bergh, Halil Bisgin, Andres Palechor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-set recognition (OSR) requires neural networks to classify known classes while rejecting unknown samples, which is critical for real-world deployment. So far, OSR research studied and developed representation learning and postprocessing methods independently and their interactions remain unexplored. In this paper, we reconsider OSR as a modular two-stage pipeline and present the first systematic study of interactions between representation learning and postprocessing methods across dataset scales and usage of known unknown data. First, we discover a failure mode we term \emph{magnitude collapse}, where representation learning methods that utilize known unknown data can suffer performance degradation at large scale and irreversibly destroy discriminative information, despite excelling at small scale. Second, we study the modular interactions and reveal when they can be leveraged for modular performance gains via two-stage processing and where interaction effects amplify performance degradation due to magnitude collapse. Third, we show how these findings can be used to achieve state-of-the-art performance with a simple $K+1$ class classifier baseline and magnitude-aware postprocessing while circumventing magnitude collapse. Finally, our results demonstrate that small-scale evaluations with known unknown data are not predictive of large-scale performance, invalidating current best practices in OSR research. Code available at this https URL.

---


### 603. [Evaluating Depth-Augmented Visual Features for Cross-Dataset Lunar Traversability Estimation](https://arxiv.org/abs/2611.03430)

**<font color=#1a73e8>作者：</font>** Jan Baturo, Bartosz Ptak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous mobility is essential for sustained lunar surface operations, as communication delays and line-of-sight occlusions limit continuous teleoperation. Although recent traversability estimation methods increasingly rely on deep learning, the domain gap between terrestrial analogue environments and real lunar terrain can limit their generalisation, and real lunar traversability labels are scarce, making fully supervised training difficult. To address these challenges, we build a weakly supervised framework trained on sparse pairwise annotations and study whether augmenting visual features with depth-derived geometric information: depth, surface normals, and combined geometric descriptors. We evaluate the models in both in-domain and cross-domain settings using two terrestrial analogue datasets and the real lunar Chang'E PCAM dataset. Contrary to expectations, we find that naive geometric augmentation yields no consistent improvement over a strong visual-only baseline in either setting, with effects small relative to seed-to-seed variance. Instead, the choice of training source emerges as the dominant factor in transfer quality: models trained on domain-relevant sources transfer substantially better to real lunar imagery than the geometric fusion strategy improves any single model. Our evaluation runs onboard a resource-constrained edge device and provides a controlled baseline for designing more expressive multimodal fusion architectures in future lunar perception systems.

---


### 604. [Bridging Neural Tangent Kernel Analysis and Reinforcement Learning for Deep Function Approximation](https://arxiv.org/abs/2611.03435)

**<font color=#1a73e8>作者：</font>** William St-Arnaud, Margarida Carvalho, Golnoosh Farnadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their widespread success across machine learning, the learning dynamics and generalization properties of neural networks remain poorly understood. The neural tangent kernel (NTK) provides an analytical characterization of the learning dynamics of infinitely wide neural networks and serves as a useful proxy for finite-width networks in supervised learning. In this work, we extend the NTK framework to reinforcement learning (RL) by introducing a temporal-difference (TD) flow formulation that accommodates time-varying mini-batches and TD targets, yielding a closed-form solution for value function evolution in an overparametrized setting. We also devise an optimization-based state-space exploration method that leverages the closed-form solution, coupled with constraints on the environment, to model the set of feasible states. On a deterministic grid environment, we validate that the proposed RL-based NTK formulation is indeed learning efficiently and adapting to the distribution shift in the training data distribution, and we demonstrate that the resulting exploration strategy improves sample efficiency. To our knowledge, this is the first work to extend NTK theory to characterize the learning dynamics of RL training with time-varying mini-batches and TD updates.

---


### 605. [Align Once to Explain: Feature Alignment for Scalable B-cosification of Foundational Vision Transformers](https://arxiv.org/abs/2611.03438)

**<font color=#1a73e8>作者：</font>** Raphael Maser, Siddhartha Gairola, Sukrut Rao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundational vision models have become the de facto standard for many vision tasks due to their strong performance. However, they are notoriously opaque and remain hard to interpret. We present ALOE (ALign Once to Explain), a one-time, label-free feature alignment approach that efficiently converts foundational vision models into inherently interpretable B-cos variants. Once aligned, the B-cos backbone is used as a drop-in replacement across several downstream tasks-amortizing the cost of interpretability. ALOE is robust across pre-training paradigms (supervised, self-supervised, vision-language) and can preserve teacher-level generalization with orders of magnitude less data than training from scratch. On classification, it strongly outperforms vanilla B-cosification (e.g., +10.5 p.p. top-1 on ImageNet for DINOv3 ViT-B/16), retains strong linear probing, k-NN, and zero-shot transfer competitive with foundational backbones (DINOv3, SigLIP2) across diverse downstream datasets. It also preserves spatially structured features useful for dense prediction, while yielding well-localized and highly human-interpretable explanations by design.

---


### 606. [Playing Dumb: How a Chess Transformer Simulates Users Across Skill Levels](https://arxiv.org/abs/2611.03439)

**<font color=#1a73e8>作者：</font>** Difan Jiao, George Eilender, Zhenwei Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models increasingly simulate users at different skill levels in education and AI evaluation. Yet it remains unclear whether lower-skill behavior reflects less internal knowledge or a different use of retained knowledge. This distinction is difficult to study in natural language, where proficiency and relevant knowledge are hard to measure. In this work, we study Maia-2, a chess transformer that predicts human moves conditioned on player skill, using quantitative skill ratings and deterministically labeled chess concepts. We hold board positions and model weights fixed and analyze positions where skill conditioning changes the prediction from a blunder to the best move. First, we measure encoded knowledge by training probes to predict the presence of 172 chess concepts from Maia-2's internal states. Probe accuracy remains nearly constant across skill conditions, and probes trained at one level transfer accurately to the others. To test whether stronger decisions can be recovered from this retained knowledge, we fine-tune only Maia-2's final output layer, raising best-move accuracy in the lowest skill band from 14.4% to 82.8%. Training this layer only on highest-skill representations retains most of the improvement at lower levels, showing that recovery does not require direct training on lower-skill states. Steering concept-relevant features learned by a sparse autoencoder also improves lower-skill decisions while leaving probe-measured concept encoding practically unchanged. These results support an account in which skill conditioning changes how retained concept knowledge influences move selection, showing that weaker behavior can understate the knowledge available within a model.

---


### 607. [Intent2CAD: How Semantic-Parametric Supervision Shapes Text-to-CAD Generation](https://arxiv.org/abs/2611.03449)

**<font color=#1a73e8>作者：</font>** Jinbo Yang, Mingyue Yuan, Shikai Jing  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-CAD generation aims to make CAD modeling more accessible by generating executable CAD programs from natural-language descriptions. However, practical CAD workflows require more than executable geometry: generated programs should also expose reusable structure that supports later modification. We introduce intent-oriented text-to-CAD generation, where design intent is expressed as recoverable code-level signals: semantic features, reusable parameters, and lightweight parametric relations. Rather than changing the model architecture or decoding procedure, we investigate how supervision representation granularity affects both CAD generation and zero-shot intent-preserving editing. To enable this study, we construct IntentCAD-100K, a 100K paired text--code dataset built by converting low-level CAD construction traces into executable CadQuery programs. We further construct IntentCAD-Edit-1K to evaluate zero-shot intent-preserving editing from the same representation perspective. Intent2CAD uses a two-stage conservative lifting pipeline: semantic lifting rewrites reliable primitive groups into feature-level operations, while parametric lifting exposes lightweight parametric relations. Under controlled fine-tuning, semantic lifting mainly improves generation reliability and feature recovery, reducing IR from 2.39% to 0.22% and achieving 99.96% API Recovery, while parametric lifting makes reusable relation structure explicit and further improves relation-aware zero-shot editing. Datasets and code are available at this https URL.

---


### 608. [Improving Hamiltonian Learning through Local Energy Decomposition](https://arxiv.org/abs/2611.03451)

**<font color=#1a73e8>作者：</font>** Yaojun Li, Yulong Yang, Christine Allen-Blanchette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hamiltonian neural networks provide a principled framework for learning conservative dynamics. A scalar Hamiltonian is parameterized by a neural network and the vector field is derived using Hamilton's equations. However, preserving Hamiltonian structure does not guarantee that the energy function itself is represented accurately. When modeled by a conventional multilayer perceptron, the Hamiltonian inherits the spectral bias of coordinate-based neural representations, favoring smooth over fine-scale structure. These fine-scale errors can be amplified by differentiation when computing the dynamics. To address this limitation, we introduce Local Multiscale Hamiltonian Neural Network (LM-HNN), which restructures the Hamiltonian according to its physical interaction structure. LM-HNN decomposes the energy into kinetic and potential components and represents them as sums of shared local functions over multiple interaction neighborhoods. This replaces a single high-dimensional approximation problem with lower-dimensional, reusable interaction laws, making fine-scale energy structure easier to resolve while preserving Hamiltonian dynamics. Across low-dimensional, interacting, and fast--slow systems, LM-HNN consistently achieves more accurate Hamiltonian derivatives and long-horizon rollouts than competing structure-preserving models, while substantially extending the effective spectral range of the learned energy. The same structured representation also generalizes more reliably to energy levels not observed during training. These results show that accuracy depends on the Hamiltonian representation as well as its structure, and that incorporating locality, decomposition, and shared interaction laws provides a simple and effective route to more accurate and generalizable Hamiltonian learning.

---


### 609. [Bg-Mix: On Using Image Backgrounds for Data Augmentation in Electron Microscopy Images](https://arxiv.org/abs/2611.03455)

**<font color=#1a73e8>作者：</font>** Ankur Srivastava, Joana Sarah Grah, Katharina Ladewig 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electron microscopy (EM) serves as a cornerstone in virology enabling the visualization of viral particles and is widely used in research, diagnostics and morphological characterization of pathogens. Computer-assisted image analysis can help facilitate and speed up this labor-intensive method, however, typical EM virus datasets are small and sparsely labeled, resulting in a lack of readily available deep learning models due to training limitations. To overcome data shortages and leverage content-rich, diverse sample backgrounds, we employed background-based data augmentation. To this end, we propose Bg-Mix, a form of data augmentation method, which decomposes training images into foreground objects and backgrounds and subsequently rearranges both into novel augmented images. This not only enhances the performance of object detection models but also increases the diversity of the training data. Using Bg-Mix provides an increase between +0.8 and +3.3 box mean average precision (mAP) points over the baseline when tested across two datasets using two architectures, thereby demonstrating its effectiveness.

---


### 610. [Unrolled gradients in disguise: bridging interpolation-based and Jacobian regularization for stable neural dynamics](https://arxiv.org/abs/2611.03461)

**<font color=#1a73e8>作者：</font>** Maya Janvier, Etienne Meunier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid models and neural differential equations (NDEs) are becoming increasingly important for modelling physical systems; however, they often encounter stability and accuracy issues during long-term integration. Training on unrolled trajectories is known to limit these divergences but quickly becomes too computationally expensive due to the need to compute gradients over an iterative process, making this method impractical for large-scale physical systems (e.g. weather and climate forecasting). Two popular paradigms for improving the stability of learned dynamics are to train on interpolated or noisy samples or to regularize the Jacobian of the learned representation. In this work, we demonstrate that these paradigms can be understood under a common lens and that they both correspond to an approximation of the gradients obtained in an unrolled learning strategy. Building on this understanding, we derive a principled and complete approach to regularize training and demonstrate its impact on the stability of learned dynamical systems.

---


### 611. [Tilted Convexity and an Exact Offline-Online Separation](https://arxiv.org/abs/2611.03472)

**<font color=#1a73e8>作者：</font>** Mohammad Pedramfar, Rajiv Khanna, Christopher John Quinn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Convexity has three equivalent descriptions: support by affine functions, monotonicity of the subdifferential, and increasing secant slopes. We weaken all three by one distortion with parameter $\gamma\in(0,1]$, which multiplies positive changes by $\gamma$ and divides negative ones by $\gamma$. The resulting classes are the convex functions at $\gamma=1$ and, for $\gamma<1$, are distinct and nested, with the parameter dropping by at most a square along the chain. For proper lower semicontinuous functions in these classes, the effective domain is convex, local minimizers are global, and the function is locally Lipschitz on the relative interior of its domain.
The classes separate offline from online optimization over compact convex sets with efficient projection, with access to function values and bounded support vectors. A smooth member of any class can be minimized to additive accuracy $\varepsilon$ with $\mathrm{poly}(1/\varepsilon)$ first-order queries and projections. Online, with nonpositive losses and $\alpha$-regret measured against $\alpha$ times the best fixed point, a polynomial-time algorithm achieves $\gamma$-regret $O(\sqrt T)$ on the largest class. For every fixed, effectively specified $\gamma\in(0,1)$ and every $\alpha\in(\gamma,1]$, no randomized polynomial-time algorithm has sublinear expected $\alpha$-regret unless $\mathbf{NP}=\mathbf{RP}$, already for smooth concave polynomial losses in the smallest class, each minimized by one linear optimization. Thus, unless $\mathbf{NP}=\mathbf{RP}$, $\gamma$ is the exact online coefficient of each class, while the offline coefficient is one.

---


### 612. [A Hybrid Visitor Prediction Framework using Interpretable Temporal features, Integrating IQR and Anomaly Detection in Lakes in Nebraska](https://arxiv.org/abs/2611.03486)

**<font color=#1a73e8>作者：</font>** Israt Zarin, Christopher Chizinski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For effective resource management, infrastructure planning, and sustainable tourism, it is really important to predict accurate visitors. This paper estimates the daily visitation of Nebraska lakes using spatial, basic temporal, and interpretable temporal features. Moreover, we evaluate the base models with multiple metrics. Using the best three models, our method will ensemble hybrid models and choose the best hybrid technique. Further, we investigate the impact of lag features and how the models work with different outlier detection techniques such as Interquartile Range (IQR) and anomaly detection. The models are evaluated using regression metrics (MAE, MSE, RMSE, MAPE, and R2). Experiment results show that, after removing anomalies, MAE, MSE, RMSE, and MAPE are reduced. Adding lag features also shows some positive effects on the results. Moreover, anomaly detection techniques perform better than IQR in improving performance while preserving data. The reported anomaly-based cross-validation results favored the voting ensemble over the compared base models on the evaluated metrics. In anomaly-based cross-validation, VOTE improved prediction errors compared with MLP (256,128,64); improvements varied in the single-split comparison. Specifically, the hybrid model reduced MAE by 9.82%, MSE by 3.12%, RMSE by 1.76%, and MAPE by 6.77%. In the reported cross-validation comparison, the best anomaly-based hybrid model had lower MAE, MSE, RMSE, and MAPE than the best IQR-based hybrid model by 9.81%, 34.30%, 18.99%, and 0.66%, respectively.

---


### 613. [An Empirical Evaluation of Signing and Verification Performance of Verifiable Credential Formats: A Cross-Language Benchmark of SD-JWT VC, W3C VCDM, and mdoc](https://arxiv.org/abs/2611.03493)

**<font color=#1a73e8>作者：</font>** Naohiro Fujie, Shigeya Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We compare the signing and verification performance of three Verifiable Credential (VC) formats--SD-JWT VC; the W3C Verifiable Credentials Data Model 2.0 with a Data Integrity cryptosuite (W3C VCDM); and mdoc (ISO/IEC 18013-5)--over one scope: issue, present with selective disclosure, verify. this http URL, Go and Python implementations ran in four environments, one a cloud VM (N=2,000 across five runs; medians of each statistic and the spread). For an end-to-end exchange disclosing 5 of 20 attributes, the total (issue, present, verify) on this http URL in the cloud VM is 0.265 ms for mdoc, 0.298 ms for SD-JWT VC and 0.534 ms for W3C VCDM. The four span a factor of five in speed; across them W3C VCDM takes 1.73--2.04x mdoc and 1.57--1.79x SD-JWT VC--at least five times our 10% band--and the ordering survives unifying the algorithm on Ed25519 and P-256. The mdoc--SD-JWT VC difference is not robust: the totals differ by 12%, 28%, 19% and 10% in the four environments, and at verification mdoc is the slower in one of them. RDFC-1.0 canonicalization produces the gap: the cryptosuite canonicalizes twice per operation, so one exchange canonicalizes six times. We attribute that cost to the specification rather than to a library mainly by replacing RDFC-1.0 with JCS, which brings W3C VCDM verification to within 5% of SD-JWT VC in three environments and within 12% in the fourth; three implementations in three languages agree, though they share a lineage. Because eddsa-rdfc-2022 has no derivation step, presenting a subset re-signs it; ecdsa-sd-2023, which preserves the issuer signature, costs 3.4 ms to issue and 1.5--2.4 ms to derive and verify there. With production education schemas, canonicalization costs 31--49x a simple credential across the four, and blank node labeling is not the driver. The measured path ends at the issuer signature check.

---


### 614. [Attacking P2P Networks: Liveness Attacks on the GossipSub and DOG Gossip Protocols](https://arxiv.org/abs/2611.03509)

**<font color=#1a73e8>作者：</font>** Jiaheng Li, Anton Paramonov, Yann Vonlanthen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Peer-to-peer (P2P) networks form the communication layer of large decentralized systems such as Ethereum, and the correctness of higher-level protocols depends on the gossip layer delivering messages to honest nodes. We study the robustness of two gossip protocols against adversaries whose only goal is to violate liveness, that is, to prevent honest nodes from receiving fresh messages, without forging, altering, or invalidating any message.
For GossipSub, the publish-subscribe protocol used by Ethereum, we show that an adversary operating a constant number of geographically distributed nodes with a fixed latency advantage can take over the ``First Message Deliveries'' peer-scoring term and separate a constant fraction of nodes from the honest mesh. We analyze the attack under a geographical model, address the random-peer and outbound-connection mechanisms, and show that the separation can be maintained under realistic churn.
For DOG, a transaction-dissemination protocol designed for CometBFT, we first give simple counterexamples in which route filtering disconnects the dissemination graph even without failures or Byzantine participants, and then present a practical attack that uses only a single physical node with a constant number of identities and legitimate actions to disable every forwarding route, separating the full network while allowing only direct publisher-to-neighbor delivery. We verify the attack in a simulated network and analyze its cost, assumptions, and possible mitigations.

---


### 615. [ST-GFM: Spectral-Temporal Graph Forecasting with Measured Perturbation Bounds and Masked Spectral Reconstruction](https://arxiv.org/abs/2611.03512)

**<font color=#1a73e8>作者：</font>** Aashish Bohra, Vivek Vijay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph forecasters for sensor networks are trained in one regime and deployed in others, where sensor coupling and signal frequency content both change. We split this spectral shift into an operator channel and a frequency channel, each with a dimensionless measure. ST-GFM (Spectral-Temporal Graph Forecasting Model) filters every input step with Chebyshev and bidirectional diffusion filters on one learned, non-symmetric operator and alternates them with per-node temporal attention. For the operator channel we prove Frobenius-norm perturbation bounds for both graph branches, show that the Chebyshev bound is attained to first order, and compute its constant from the trained weights and the measured operator norm: 17.9 on METR-LA and 21.5 on PEMS-BAY. Under random edge dropout the trained layer moves by 2.0% to 3.1% of this bound. Masked Spectral Reconstruction (MSR), a self-supervised loss active in the first 40 epochs, matches the log power spectrum of the encoder output to that of the input. For small log-spectral residuals on unclamped bins it is proportional to an Itakura-Saito divergence to leading order. Removing it raises the 60-minute MAE by 0.30 on METR-LA, close to the 0.33 lost when all three self-supervised losses go. Under one shared evaluation pipeline, the 60-minute MAE of ST-GFM is 3.5% below a retrained STAEformer on METR-LA and 13.0% below it on PEMS-BAY. Its 60-minute MAE is 3.0980.017 on METR-LA (five seeds) and 1.5760.006 on PEMS-BAY (three seeds), the lowest PEMS-BAY MAE among twelve published baselines.

---


### 616. [EmbryoProfiler: A Visual Clinical Decision Support System for IVF](https://arxiv.org/abs/2611.03516)

**<font color=#1a73e8>作者：</font>** Johannes Knittel, Simon Warchol, Jakob Troidl 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In-vitro fertilization (IVF) has become standard practice to address infertility, which affects more than one in ten couples in the US. However, current protocols yield relatively low success rates of about 20% per treatment cycle. A critical but complex and time-consuming step is the grading and selection of embryos for implantation. Although incubators with time-lapse microscopy have enabled computational analysis of embryo development, existing automated approaches either require extensive manual annotations or use opaque deep learning models that are hard for clinicians to validate and trust. We present EmbryoProfiler, a visual analytics system collaboratively developed with embryologists, biologists, and machine learning researchers to support clinicians in visually assessing embryo viability from time-lapse microscopy imagery. Our system incorporates a deep learning pipeline that automatically annotates microscopy images and extracts clinically interpretable features relevant for embryo grading. Our contributions include: (1) a semi-automatic, visualization-based workflow that guides clinicians through fertilization assessment, developmental timing evaluation, morphological inspection, and comparative analysis of embryos; (2) innovative interactive visualizations, such as cell-shape plots, designed to facilitate efficient analysis of morphological and developmental characteristics; and (3) an integrated, explainable machine learning classifier offering transparent, clinically-informed embryo viability scoring to predict live birth outcomes. Quantitative evaluation of our classifier and qualitative case studies conducted with practitioners demonstrate that EmbryoProfiler enables clinicians to make better-informed embryo selection decisions, potentially leading to improved clinical outcomes in IVF treatments.

---


### 617. [Contrastive Adapter Training and Consensus Knowledge Distillation for Multi-Source-Free Domain Adaptation in Skin Cancer Diagnosis](https://arxiv.org/abs/2611.03528)

**<font color=#1a73e8>作者：</font>** Ali Abedi, Q. M. Jonathan Wu, Ning Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skin cancer diagnosis, particularly differentiating melanoma from benign nevi, is challenging due to the visual similarity between lesions. Although convolutional neural networks (CNNs) and vision transformers (ViTs) have shown promising performance, their effectiveness often deteriorates on data from heterogeneous clinical sources. Conventional domain adaptation methods address domain shift but require access to source data during adaptation, which is often infeasible due to privacy regulations. Multi-source-free unsupervised domain adaptation (MSFDA) addresses this limitation by leveraging multiple labeled source domains to generalize to an unlabeled target domain without requiring access to source data. However, existing MSFDA methods rely on full backbone fine-tuning, leading to catastrophic forgetting and overfitting on small clinical datasets, and address domain shift at the aggregation stage without establishing a shared domain-invariant feature space. Furthermore, their reliance on hard pseudo-labels or confidence-weighted aggregation introduces noisy supervision signals under domain shift. To address these limitations, we propose CAT-CKD, consisting of two components: (1) contrastive adapter training (CAT), which trains lightweight ConvPass adapters within a frozen ViT backbone using supervised contrastive learning (SCL) to establish a shared domain-invariant feature space before source-specific model training, and (2) consensus knowledge distillation (CKD), which aggregates logits from multiple source models into a consensus supervisory signal and adapts a student model on unlabeled target data using KL divergence. Experiments on five publicly available skin lesion datasets show that CAT-CKD achieves an average AUROC of 86.1%, outperforming existing MSFDA methods while requiring only 4.3M trainable parameters. The code is available at this https URL.

---


### 618. [CoLa3D: Composable Latent 3D Decomposition](https://arxiv.org/abs/2611.03533)

**<font color=#1a73e8>作者：</font>** Xudong Cai, Yongcai Wang, Deying Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce CoLa3D, a simple and effective model for composable 3D scene decomposition that, given a single whole-scene latent from either a single image or an existing scene mesh as input, directly outputs a set of object meshes with consistent spatial layout that can be assembled back into a coherent scene. CoLa3D introduces a novel paradigm for 3D scene decomposition within a shared whole-scene latent, unlike alternatives that perform per-object generation in canonical spaces and then glue the objects back together with fragile pose and scale estimation. The network is a lightweight, flexible, and scalable query-based transformer that accepts various types of queries, including 2D masks, 3D points, and learnable queries, and learns to decompose the scene into objects in a compact latent space. On both synthetic and real-world datasets, CoLa3D achieves state-of-the-art performance on composable 3D scene decomposition, substantially improving global scene-level consistency and object-level quality while running 2 times faster and using less than 1% of SAM 3D's training data. Visible depth on par with MoGe2 further confirms that latent decomposition preserves accurate visible scene geometry while producing physically complete, decomposable object meshes.

---


### 619. [Variational Functional Neural Networks (vfNN)](https://arxiv.org/abs/2611.03542)

**<font color=#1a73e8>作者：</font>** Chinmay Katke, C. Nadir Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a variational functional neural network (vfNN) algorithm that optimizes physically motivated continuum functionals in integral form (e.g., Lagrangian, Hamiltonian, or free energy) to find the states of a system. That way, vfNN bypasses solving the equations of motion (a.k.a. the Euler-Lagrange equations), which are in the form of differential equations. To this end, our approach is fundamentally different from conventional physics-informed neural networks (PINN) that solve differential equations by minimizing a phenomenological loss function involving higher order derivatives and ad hoc weight factors. In contrast, vfNN merely evaluates lower order derivatives of the generating functional and replaces the weight factors with rigorous physical scales. This also fundamentally changes the loss landscape, and the desired solutions may become unstable. For this emergent nonconvex optimization problem, we develop a quasi-Newton optimization algorithm with simulated annealing that converges to the solutions of the corresponding Euler-Lagrange equations of the functional regardless of their stability properties. Our simulations using vfNN give accurate results for benchmark systems governed by linear or nonlinear ordinary differential equations.

---


### 620. [BISECT: Bilevel Spectral Decomposition for Low-Rank Continual Learning](https://arxiv.org/abs/2611.03574)

**<font color=#1a73e8>作者：</font>** Tom Saliencro, Wen-Hsuan Liu, Rohan Desai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exemplar-free continual learning on pre-trained Vision Transformers increasingly relies on Low-Rank Adaptation (LoRA), yet prevailing methods govern the low-rank update space through strict subspace isolation. By projecting each incoming task into the approximate null space of historical token activations, isolation-based learners equate any cross-task feature overlap with catastrophic interference. We show that this orthogonality premise induces a structural bottleneck we term \emph{spectral starvation}: when down-projection bases are locked before task optimization, the gradient norm reaching the trainable up-projection is upper-bounded by the energy of current-task features captured by the chosen basis. Because natural visual tasks share low- and mid-level covariance structure, historical null tails contain barely $5.5\%$ of incoming task variance, starving new-class plasticity while blocking positive consolidation along shared directions. We propose BISECT (Bilevel Spectral Decomposition), a continual LoRA framework that partitions a fixed rank-$r$ budget into two orthogonal functional blocks: an invariant carrier spanned by the dominant modes of the joint historical-and-current Gram matrix, and a novelty complement extracted via generalized Rayleigh whitening followed by orthogonal complement projection. After single-task training, BISECT folds both blocks back into the frozen backbone using a closed-form precision gate that scales each rank-1 invariant atom by its current-to-joint Rayleigh ratio while preserving novelty atoms at unit gain. Across eight incremental settings on ImageNet-R, ImageNet-A, CIFAR-100, CUB-200, and DomainNet, BISECT outperforms prompt, adapter, and LoRA baselines with zero extra inference parameters or FLOPs, and remains complementary to sparse analytic expansion.

---


### 621. [NitiBench+: A Temporal Thai Legal Question Answering Benchmark Across 17 Domains](https://arxiv.org/abs/2611.03576)

**<font color=#1a73e8>作者：</font>** Pawitsapak Akarajaradwong, Sarana Nutanong, Chompakorn Chaksangchaichot  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Law changes over time. A court decides a case under the law in force on that day, and legal QA benchmarks grade answers against today's law. We checked 156,650 decisions of four Thai courts. Up to 67% of them cite law that has since been amended or repealed. We introduce NitiBench+, the sequel of our NitiBench, a Thai legal QA benchmark with 1,670 items across 17 domains, built from decisions of three courts. For each cited section it holds both the text in force on the decision date and the current text, and its retrieval corpus holds every dated version of every Thai statute section. Answers are graded on the Thai Bar Council rubric, the Bar-standard score, and on the overlap between the cited sections and the court's. The report has two parts. Part I measures the cost of the wrong text on 13 open-weight models. Reading the current text of amended law drops the Bar-standard score by 0.25 and missing repealed law drops it by 0.79. The penalty comes from rule changes, 0.45 on the 428 rule-changed items and none on the 331 wording-only items, and Citation F1 does not see it. The text in force is the fair setting. Part II benchmarks today's models on that setting. A public leaderboard ranks 26 models on a held-out test split of 500 items stratified by domain, with a validation split of the same shape released for public use, from memory alone, with the court's sections provided, and as a retrieval agent over the law in force, with the cost per item and the hallucinated citations. The best model scores 7.78 out of 10 and the best open-weight model 6.39. Without a search tool only five open-weight models recall any Thai law, and with it twenty of the 26 models gain and six lose. Leaderboard will take new models as they are released. Legal benchmarks must track dates, and on the right text today's models still leave a wide gap on Thai law.

---


### 622. [3D-BBDA: Backpropagation-Free Black-Box Domain Adaptation for Robust 3D Point Cloud Recognition](https://arxiv.org/abs/2611.03588)

**<font color=#1a73e8>作者：</font>** Shivangi Rai, Kunal Jangid, Vaibhav Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust 3D point-cloud recognition is critical for robotics, mapping, and urban sensing, yet point-cloud classifiers often suffer performance drops under domain shifts caused by sensor changes, environmental variation, and acquisition artifacts. Many existing adaptation methods are difficult to deploy in practice because they require access to source data or the internal parameters of the source model, which may be restricted by privacy, licensing, or security constraints. We present 3D-BBDA, a backpropagation-free black-box domain adaptation framework that adapts a source-trained predictor to unlabeled target data using only black-box outputs. Our method performs pseudo-label guided prototype-based alignment and employs a weighted prediction module to fuse source logits with alignment logits, reducing sensitivity to noisy pseudo-labels. To stabilize prototype memory when pseudo-label coverage is incomplete, we construct a Gaussian-perturbed prototype prior from unlabeled target predictions and use it as a fallback for missing or unreliable class prototypes during alignment. Experiments on four corrupted 3D benchmarks demonstrate consistent improvements over strong baselines. On ModelNet-40C, 3D-BBDA achieves mean errors of 32.08% (PointNet) and 29.62% (GDANet), outperforming Source-only (35.88% / 34.03%) and BFTT3D (33.78% / 32.36%). 3D-BBDA requires only a single forward pass with no gradient updates making it suitable for real-time, privacy-preserving deployment in transferable 3D recognition pipelines. Project page is available at this https URL

---


### 623. [DynaSolver: A Neural Operator for Autoregressive 4D Flow Prediction with Dynamic Boundaries](https://arxiv.org/abs/2611.03595)

**<font color=#1a73e8>作者：</font>** Rui Qian, Shibo Dai, Mengjun Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide efficient surrogates for computational fluid dynamics (CFD), but most are designed for static geometries and are not equipped to model unsteady flows induced by continuously moving boundaries. We study dynamic-boundary 4D CFD prediction for articulated moving geometries and introduce RoboCFD-4D, a temporally resolved robotic CFD benchmark spanning diverse morphologies and flow conditions. To address the computational and autoregressive challenges of this setting, we propose DynaSolver, a neural operator that explicitly conditions on boundary evolution and causal flow history. DynaSolver employs an efficient physical-token formulation that amortizes point-to-token projection across the operator stack, substantially reducing repeated point-space spatio-temporal computation while retaining accurate point-level reconstruction. We further introduce Replay-Augmented Parallel Training, which exposes the model to autoregressively generated histories while preserving parallel dense supervision, narrowing the gap between ground-truth-conditioned training and autoregressive rollout. Experiments on RoboCFD-4D show that DynaSolver achieves the best full-rollout accuracy among a broad range of learned CFD surrogates, with its advantage increasing as rollout proceeds, indicating substantially reduced autoregressive error accumulation. Project page: this https URL.

---


### 624. [Structured Visual Landscape: Generating Preferred Representations in Biological and Artificial Neural Networks](https://arxiv.org/abs/2611.03597)

**<font color=#1a73e8>作者：</font>** Yusong Zhao, Edgar Y. Walker, Hao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how neurons respond to visual stimulus is an important question in both deep learning and neuroscience. It has significant implications for enhancing the interpretability of black-box artificial neural networks and for understanding the visual representation in the human brain. We propose a structured visual representations landscape and design an activation-based prior that allows us to effectively regularize the landscape with activations from brain regions or neural network units. Our model Vis-Lens integrates a variational autoencoder and a diffusion model into an image generation framework. It enables the generation of natural, realistic preferred images by directly modifying the activation-regularized latent codes without per-image iterative optimization. We demonstrate the effectiveness of our framework on both artificial neural networks and human visual cortex using functional magnetic resonance imaging (fMRI) data. Our framework improves activation modulation and image realism compared with a recent state-of-the-art method for generating preferred visual representations of these neural targets.

---


### 625. [Should We Combine Our Data? Algorithms and Limits for Privately Assessing Data Sharing](https://arxiv.org/abs/2611.03599)

**<font color=#1a73e8>作者：</font>** Mahdi Haghifam, Kumar Kshitij Patel, Avrim Blum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study when two parties should pool their data to train a machine learning model. Two agents, Alice and Bob, each hold a sensitive labeled dataset and want to train a classifier from a given hypothesis class $\mathcal{H}$. Even when each party's dataset can be perfectly classified on its own, the two parties may follow conflicting labeling standards or have selection biases that affect their features and label sets, such that no single classifier in $\mathcal{H}$ fits their combined data. Before committing to data sharing, Alice and Bob therefore want to test whether a single classifier in $\mathcal{H}$ can jointly fit both datasets---without revealing their individual data points to one another.
We formalize this problem from a learning-theoretic viewpoint via $\operatorname{opt}_\mathcal{H}$, the minimum \emph{number of mistakes} made by any hypothesis in $\mathcal{H}$ on their pooled data. Through interactive communication, the agents must distinguish $\operatorname{opt}_\mathcal{H}=0$ (compatible datasets) from $\operatorname{opt}_\mathcal{H}\geq t$ (conflicting datasets) under pure $\varepsilon$-two-party differential privacy. A trusted curator could do this with $t=O(1/\varepsilon)$, and we ask how small $t$ can be without one. For thresholds on the real line over a domain of size $m$, we show that the optimal $t$ is $\tilde{\Theta}(\log\log m/\varepsilon)$, exponentially smaller than the $\Theta(\log m/\varepsilon)$ samples needed to privately learn thresholds, even with a curator. For halfspaces in $\mathbb{R}^d$, the dependence on $m$ jumps to $\log(m)$: we give a protocol with $t=\tilde{O}(d^3\log m/\varepsilon)$ and show that some domains require $t=\Omega(d\log(m/d)/\varepsilon)$.

---


### 626. [Four Bridges: Measuring Deception Propensity in a Multi-Agent Game](https://arxiv.org/abs/2611.03600)

**<font color=#1a73e8>作者：</font>** Raphael Casey, Michael Simeone, Alberto Tosato 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly deployed in settings where they interact and coordinate with other agents, yet honesty is mostly measured in single-turn, single-agent benchmarks that pressure the model to deceive. We study deception that emerges in multi-agent interaction without any instruction to deceive. We introduce Kradle, a platform for evaluating AI models, and Four Bridges, an information asymmetry game in which four agents distribute across four rooms: one is the death room, the others hold food worth more if not shared. One agent, the informed agent, knows which room is the death room and can withhold or disclose that information. We evaluate eight frontier models as the informed agent. Deceptive behavior appears in every model and in 73% of all runs (6% to 100% per model), and does not decrease with capability tier within a model family. When the informed agent does disclose, the warning is often challenged, and agents that challenge it enter the death room twice as often as those that do not. Telling all agents that one of them knows the death room collapses deception in six of eight models; telling the informed agent that the room is permanently fatal moves only one. On an open-weight model, an honesty steering vector reduces deception to 0% and adversarial honesty training to 6%. The platform and game provide a testbed for measuring deceptive behavior and comparing interventions.

---


### 627. [ufakzeka-kulak: Building and Evaluating a 31.6M-Parameter Turkish Speech Recognizer from Scratch](https://arxiv.org/abs/2611.03605)

**<font color=#1a73e8>作者：</font>** Sait Furkan Teke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ufakzeka-kulak is an open Turkish speech-to-text model of 31.6M parameters, a FastConformer encoder with a token-and-duration transducer (TDT) and a CTC head, trained from scratch and released under Apache-2.0. It writes cased, punctuated Turkish with numbers as words. Its 4,977 training hours come from sources whose licences allow commercial use; 281 hours are human-transcribed, and for the other 4,696 the training text is an uploader subtitle or a machine transcript, kept only where a second, independent reading of the audio agrees with it. The recipe, checkpoint, labelling and export choices were made on development data, and the test sets were scored once, in a release gate fixed before training. With greedy TDT decoding the normalised word error rate (WER) is 0.0921 (95 percent interval 0.0792 to 0.1055) on FLEURS Turkish test and 0.0916 (0.0873 to 0.0958) on Common Voice 27.0 Turkish test, lower than Whisper base and Whisper small on both sets with paired intervals wholly below zero; Whisper large-v3 (greedy) scores 0.0604 and 0.0767. On conversational speech the WER is 0.3807. We also report punctuation and casing, degraded audio, and how closely each shipped export reproduces the trained model.

---


### 628. [Efficient Closure Learning in Dynamical Systems: A Comparison of Data-Assimilated and Embedded Approaches](https://arxiv.org/abs/2611.03612)

**<font color=#1a73e8>作者：</font>** Rileigh Bandy, Teresa Portone, Mohammad Khalil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Increased computing power has transformed computational science and improved predictive capabilities for complex systems, but many phenomena still exceed current simulation capabilities or require rapid evaluations for fast design iterations. Closure models address this challenge by approximating unresolved effects in reduced or incomplete dynamical systems. Data-driven closures offer a flexible mechanism for improving model accuracy and applicability, but approaches that embed the closure within a computational model for construction and training phases can be computationally expensive and cause numerical instabilities in the computational model during training. To avoid the challenges posed by embedded approaches, staged approaches to closure-model learning have been developed. The first stage uses data assimilation to infer state and closure trajectories from observations. The second stage trains a machine learning closure model offline using the assimilated data, thereby avoiding repeated simulator calls during training. In this work, we investigate the cost and accuracy tradeoffs between embedded and staged data-driven closure modeling approaches for a synthetic epidemiological SIQR model with a nonlinear state-dependent quarantine closure. The results illustrate a practical accuracy-efficiency trade-off: for this exemplar, embedded training provides the strongest average accuracy, while the staged approach yields comparable qualitative behavior with a moderate increase in error, substantially fewer model evaluations, and improved optimization robustness.

---


### 629. [Benchmark Prediction with Sparse and Unpaired Cached Responses](https://arxiv.org/abs/2611.03614)

**<font color=#1a73e8>作者：</font>** Hayden Helm, Avijit Ghosh, Ben Johnson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating a generative model on all queries from all available benchmark tasks is prohibitively expensive. As such, models are often evaluated on different subsets of tasks and/or different subsets of queries from a given task. The resulting collection of responses and the corresponding (model, task) score matrix are sparse and unpaired. In this paper, we introduce the Product Kernel Perspective Space (PKPS), a collection of low-dimensional representations of models based on their embedded responses. PKPS generalizes existing methods for representing black-box generative models by comparing responses to similar -- rather than just identical -- queries and is therefore able to utilize sparse and unpaired information. Theoretically, we show that benchmark prediction using PKPS is query-efficient relative to methods that only use information from dense and paired portions of the evaluation data. Empirically, we show that PKPS-based methods outperform baselines on benchmark prediction across two large benchmark suites.

---


### 630. [Strategist: Evolving Reasoning with Agents](https://arxiv.org/abs/2611.03618)

**<font color=#1a73e8>作者：</font>** Taiming Lu, Qi Xu, Zhigang Hua 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A model is only half of an AI agent system. The other half is the inference strategy: the reasoning procedure that turns model calls into a response. Today that second half is written by hand, and the experience of building one strategy never carries to the next. We introduce Strategist, a meta-agent that evolves inference strategies across tasks. Each strategy is written as a blueprint,executable code that other strategies can reuse, and together the blueprints form a library. Given a task and a small development set, Strategist retrieves related blueprints, writes candidate strategies, tests them on real samples, and revises them from the results. Every candidate then enters the library, so later tasks build on earlier discoveries. On 30 benchmarks, Strategist beats the strongest baseline on 24 and matches its average accuracy (74.7% vs.74.0%) at 39% lower inference cost. Its strategies also transfer to unseen tasks and other models without further search. The part of an AI system that is not improved on its own now does.

---


### 631. [Thought-deciphering via hierarchical EEG-to-text alignment](https://arxiv.org/abs/2611.03623)

**<font color=#1a73e8>作者：</font>** Xiaopeng Mao, Morten Mørup, Xin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Communication is important for our well-being, but it can be impaired by disabilities, such as locked-in syndrome (LIS), cerebral palsy (CP), and dysarthria. Non-invasive brain-to-text brain-computer interfaces (BCIs) offer a promising solution by providing an alternative communication pathway for people with communication disabilities. However, most recent breakthroughs have relied on large, cumbersome, and costly neuroimaging modalities, such as functional magnetic resonance imaging (fMRI) and magnetoencephalography (MEG). Numerous studies have attempted decoding using the lighter and cheaper electroencephalography (EEG), but the results remain inferior compared to the other modalities. More importantly, we do not understand how these modalities are related to text at the letter, word, sentence, and higher semantic levels. Many prior studies have focused on decoding below the sentence level because it is considerably easier to design an experiment around phonemes, letters, and words. However, during communication, sentences play a much more important role than words and letters. This is because sentences carry information at such a high level that they can be understood even if some words and letters are missing. However, within sentence-level decoding, sentence classification is not as well investigated as sentence generation, making it difficult to decide whether a sentence should be retrieved or generated in the context of EEG-to-text decoding. This paper strives to investigate sentence-level EEG-to-text classification via a novel hierarchical alignment framework, where the main goal is to retrieve a read sentence using its context and EEG as inputs.

---


### 632. [FADE: Factored Ability--Difficulty Filtering for Online RLVR Scheduling](https://arxiv.org/abs/2611.03625)

**<font color=#1a73e8>作者：</font>** Tomas Duncun, Jonah Ellison, Mateo Ruiz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning with verifiable rewards (RLVR) learns only from prompts whose sampled completions disagree: all-pass and all-fail groups produce zero relative advantage and burn generation budget without moving the policy. Adaptive schedulers try to steer rollouts toward informative prompts, yet they rely on per-prompt pass-rate trackers that entangle two quantities evolving at very different speeds---the policy's shifting competence across reasoning skills and each prompt's intrinsic difficulty. When a single exponential average or Beta counter tracks both at once, short memory scrambles the relative ordering of prompts whereas long memory reports stale pass rates. We introduce FADE (Factored Ability--Difficulty Estimation), a bilinear state-space filter that separates the two timescales. FADE represents each prompt's success logit as the inner product of a whitened $K$-dimensional skill loading with a fast-drifting policy ability vector, minus a slow-shrinking scalar item intercept. Using Pólya--Gamma augmentation, each minibatch of binary rollout outcomes updates the $K$-dimensional ability posterior in closed form via a rank-$K$ Woodbury step, instantly transferring competence shifts to all unobserved prompts that share those skills while leaving item intercepts stable. From the resulting posterior mean and variance we derive a closed-form utility for the probability of drawing a non-degenerate rollout group. Across five reasoning benchmarks, two base models, and four scheduling paradigms under a matched rollout budget, FADE consistently improves downstream accuracy and calibration while adding less than $0.6$\,ms per step.

---


### 633. [Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data](https://arxiv.org/abs/2611.03626)

**<font color=#1a73e8>作者：</font>** Rafal Karp, Gene Liu, Shih-Hsin Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Isekai3D Synthetic Data Generation (SDG), a platform for simulating and capturing synthetic 3D gameplay for research in vision and world models, neural graphics, gameplay agents, and other applications. The platform combines reusable environment and character assets with Unreal Engine plugins in a two-stage workflow. First, world simulation generates gameplay while recording the world state, character movements, actions, and camera tracks needed for replay. Second, the recorded simulation is replayed to capture selected outputs, such as rendered video, images, and depth maps, at a specified resolution and frame rate under selected rendering and camera configurations. Separating simulation from capture allows the same recorded gameplay to produce multiple output variants without repeating the original simulation. Visual outputs are accompanied by frame-aligned camera, character, and action metadata. The platform uploads generated data directly in a training-friendly format, reducing intermediate storage, preparation time, and manual processing. This report describes the design of our overall system, including the platform's assets, plugins, and their functionality, explaining how they work together to generate diverse synthetic gameplay data.

---


> [!TIP]
> 当前位于：**601-633**（第 13/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-633**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
