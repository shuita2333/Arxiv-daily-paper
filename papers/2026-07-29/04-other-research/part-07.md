# 📦 其他研究 | 2026年07月29日

> 本类共 **442** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-442](./part-09.md)

---

### 301. [Plato-Bio: verification-first biological novelty screening with temporal rediscovery and structural benchmarks](https://arxiv.org/abs/2607.23975)

**<font color=#1a73e8>作者：</font>** Stefan G. Creadore  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model research agents can connect literature retrieval, analysis code, and manuscript preparation, but coherent output does not establish scientific validity. We developed Plato-Bio, a biology-routed extension of the open Plato/Denario architecture that couples explicit workflow states with provenance records, citation checks, claim-to-evidence links, scoped file writes, and publication gates. A source audit identified and repaired three defects that could distort evaluation: loss of task domain in the default factory, omission of declared method signals from scoring, and evidence sidecars that lacked the drafted-claim denominator. On the current clean revision, the full Python suite completed with 931 passes, six skips, and no failures or errors; targeted biology, genomics, evidence/citation, and adversarial-safety suites likewise completed without failure. We evaluated two narrow use cases. In a frozen historical rediscovery task, independent pre-1986 literature bridges ranked the later-studied relation between fish oil and Raynaud phenomenon first; TF-IDF ranked it second and corpus frequency third. This single curated task measures retrospective ranking, not prospective discovery. In a separate comparison of AlphaFold models with experimental structures for 15 human proteins, 11 targets had high-confidence-core C-alpha RMSD below 1 Angstrom (median 0.501 Angstrom). Four targets exceeded 2 Angstrom, and confidence masking reduced the SUMO1 discrepancy from 16.61 to 2.58 Angstrom over 74 residues. The workflow emitted 27 traceable discrepancy regions, all retained as unvalidated hypotheses. Plato-Bio therefore provides reproducible software contracts and auditable screening baselines; broader claims of agent efficacy or biological novelty require preregistered evaluation, independent review, and prospective validation.

---


### 302. [Mutual Modality Trust with Lightweight Reconstruction Regularization for Fine-grained Tire Pattern Recognition](https://arxiv.org/abs/2607.23979)

**<font color=#1a73e8>作者：</font>** Jianning Yang, Jie Fang, Xinda Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual tire recognition serves as a core supporting technique for vehicle safety monitoring, autonomous driving perception and automated automotive maintenance. Existing fine-grained tire recognition techniques suffer from three prominent limitations. They tend to depend on only one visual source, lack the capacity to jointly model spatial and frequency cues for minute tread texture extraction, and suffer severe overfitting given limited annotated tire imagery. This paper proposes a lightweight fine-grained tire pattern recognition method incorporating dual-branch independent inference and enhanced feature fusion to boost recognition performance. The framework employs two task-specialized branches dedicated to tire surface and tread indentation, respectively, to extract modality-specific discriminative features. Each branch conducts independent prediction, while cross-branch feature fusion exploits Mutual Modality Trust (M$^2$T) to realize complementary feature enhancement across two modalities. Besides, a frequency-domain hierarchical guidance module is devised, which leverages bandpass filters to decompose feature maps into high- and low-frequency components and enables fine-grained cross-layer feature modulation. Furthermore, a Lightweight Reconstruction Regularization (LR$^2$) is introduced to retain abundant intrinsic information within feature embeddings, substantially improving feature stability and recognition robustness under limited labeled training data. In addition, we establish a surface-indentation multi-source dataset namely MTire299 for fine-grained tire tread recognition, which covers 299 categories with a total of 14795 paired image samples. Extensive experiments conducted on two public tire datasets validate the superiority and efficacy of the proposed algorithm.

---


### 303. [Beyond GDPR: Examining Disclosure Gaps in Mobile AR Privacy Policies under U.S. State Privacy Laws](https://arxiv.org/abs/2607.23984)

**<font color=#1a73e8>作者：</font>** Hong Chen, Xueling Zhang, Hong-Ning Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile Augmented Reality (MAR) apps can collect and process highly sensitive data such as spatial maps and biometrics, yet their privacy policies remain largely understudied. Prior audits of app privacy policies have typically focused on a single legal framework, such as the GDPR. Meanwhile, 20 U.S. states have comprehensive privacy laws in effect, creating a fragmented and rapidly evolving set of privacy policy obligations. To date, no study has systematically audited privacy policies against this emerging body of state-level legislation.
In this paper, we present the first large-scale audit of MAR privacy policies under U.S. state privacy laws. We construct a dataset covering the MAR ecosystem, including 8,013 Google Play MAR app metadata records worldwide, and a U.S.-based subset with 6,620 APKs and 6,426 privacy policy files. We further derive an auditable disclosure taxonomy with 5 baseline requirements, 10 triggered requirements, and 4 logic chains, and build a validated four-stage automated pipeline that produces traceable, evidence-grounded disclosure judgments.
Our audit reveals widespread disclosure gaps: 44.62\% of audited policies exhibit severe disclosure omissions, with each missing more than eight requirements, and four privacy-policy requirements have violation rates above 90\%. These findings suggest that MAR privacy disclosures are not keeping pace with the growing complexity of U.S. state privacy regulation. We release our dataset, taxonomy, and auditing pipeline to support future research on scalable privacy compliance auditing.

---


### 304. [Adaptive Data Admission and Retention for Streaming Federated Learning](https://arxiv.org/abs/2607.23987)

**<font color=#1a73e8>作者：</font>** Zhuoyi Zhao, Ben Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study streaming federated learning with limited client memory, where newly generated training data incur time-varying sampling costs and must be selectively admitted and retained over time. We consider a joint server-side admission and client-side memory-management framework with the objective of minimizing the cumulative excess population risk under a sampling-cost budget and buffer constraints. We first derive a learning-error bound that explicitly captures the effects of instantaneous training sample size, distinct-sample growth, and reuse imbalance through a characterization of the effective sample size. Through a surrogate penalty obtained from this bound, we develop an Active-Constraint Drift-Plus-Penalty (ACDPP) policy that combines a structured client-side $K$-step retention rule with a server-side online admission rule and a time-varying rectangular admission region. We further present a sequence of comparison arguments, via an auxiliary constant-admission policy, that connects the ACDPP learning bound to a costless oracle benchmark. This yields explicit guarantees in terms of sublinear regret and sampling-cost violation, while the buffer-occupancy violation is controlled through offline selection of the retention horizon. Experiments on multiple datasets demonstrate that the proposed policy remains close to the oracle benchmark while satisfying the sampling-cost and buffer constraints.

---


### 305. [Effective Receptive Field Ordering Matters for Infrared Small Target Detection](https://arxiv.org/abs/2607.23994)

**<font color=#1a73e8>作者：</font>** Guoyi Zhang, Yanjin Du, Zhengyao Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we investigate a previously unexplored architectural dimension for infrared small target detection: the organization of effective receptive fields (ERFs) during feature refinement. Unlike existing approaches that primarily improve individual feature operators, we argue that ERF organization constitutes an architectural dimension independent of receptive field design itself, and formulate deep feature transformation as a progressive residual correction process, from which a theoretical framework for ERF scheduling is established. Specifically, we reveal that ERF refinement is governed by two fundamental properties: scale-frequency correspondence, which aligns different ERF scales with distinct residual frequency characteristics, and nonlinear non-commutativity, which makes different ERF orderings produce fundamentally different refinement trajectories. Together, these properties show that ERF organization, rather than ERF scale alone, governs refinement dynamics. Guided by these principles, we propose Receptive Field Ordering Network (RFONet), which realizes hierarchical ERF scheduling through a multigrid-inspired V-cycle strategy using only standard $3\times3$ convolutions. RFONet achieves state-of-the-art performance on multiple benchmarks with only 1.16M parameters and over 157 FPS inference speed. Beyond empirical performance, our theoretical analysis provides theoretical guarantees for stable residual refinement under perturbations, frequency shifts, and partial occlusions, which are consistently reflected in superior noise robustness and cross-dataset generalization. Finally, our framework reformulates ERF organization as a task-dependent optimization objective, providing a principled foundation for future adaptive receptive field scheduling.

---


### 306. [Exploring Budgeted Image Classification with Content-Sensitive Resource Allocation](https://arxiv.org/abs/2607.23997)

**<font color=#1a73e8>作者：</font>** Athanasios G. Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ever-growing adoption of Artificial Intelligence (AI) creates the need to deploy Deep Neural Networks in a variety of computational environments. We consider dynamic environments, where computational requirements are subject to change, and we pose the following question: How do we adjust the complexity of an AI classification system, in order to maximize its accuracy, while meeting changing computational constraints? We call this problem Budgeted Image Classification, and we formally formulate it as a resource allocation integer program. Given a computational budget, a batch of images, and a classification system that can make decisions with varying complexity (it has multiple decision points), we explore strategies to allocate images to decision points, in order to maximize accuracy within the available budget. The original integer program is NP-Hard, so, we propose a continuous relaxation, leading to a content-agnostic allocation strategy which assigns images to decision points without considering their particular content. We address this issue by proposing a content-sensitive strategy, that we experimentally show it leads to superior performance. We theoretically study the behavior of our strategies, deriving conditions that must be satisfied by decision points to be suitable for budgeted classification. We analyze fails cases, offering insights for future research directions.

---


### 307. [Low-light Image Enhancement via Multi-scale Attention combined with Fourier Transform](https://arxiv.org/abs/2607.24002)

**<font color=#1a73e8>作者：</font>** Wenbin Du, Jian Long, Zhu Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement (LLIE) aims to improve image quality and clarity in diverse and demanding low-illumination environments. However, existing deep learning-based LLIE methods struggle to accurately capture real-world illumination and restore texture details, largely because their algorithmic strengths remain underutilized. To address these issues, we present a supervised frequency domain deep learning network for LLIE, named multi-scale attention combined with the Fourier transform (MSFT) which adopts a U-shaped, one-stage architecture that infuses guidance from low-light images into the network by channeling it through multi-scale attention. We further fuse the amplitude information from priori channels with that of the low-light image in MSFT's self-created module, and carry out multi-scale guidance along with the network. Subsequently, to better enhance the faint feature, such as fine content and textures, and to better fuse global context confidence in the decoding stage, we separately introduce a multi-shape synergistic attention and a lightweight network that effectively integrate information in high-dimensional space to embed into the superlative feature space channel containing rich texture information. Extensive experiments conducted on LOL, SID, SMID, and SDSD datasets demonstrate that MSFT significantly outperforms state-of-the-art competitors. For example, compared with Retinexformer, our method achieves a peak signal-to-noise ratio of up to 41.76 decibels on the SDSD-outdoor dataset with an increase of 11.92 decibels and a structural similarity index of 0.988 with a 13.80% improvement.

---


### 308. [Structural Loss Metrics for Tensor Approximation via Matrix Low-Rank Approximation](https://arxiv.org/abs/2607.24009)

**<font color=#1a73e8>作者：</font>** Hiroki Hasegawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Matricized low-rank approximation via SVD is a standard surrogate for tensor decompositions, but entry-wise reconstruction error fails to capture multiway geometric degradation. Under an orthogonal Tucker model, we characterize this degradation using two metrics: cross-mode Direction Loss, measuring geometric subspace deviation from rank truncation and noise rotation, and Interaction Loss, quantifying multilinear interaction distortion in the core tensor. We prove that squared relative reconstruction error orthogonally decomposes into interaction loss and out-of-subspace energy, and derive a Wedin-type bound establishing the stability of a plug-in Direction Loss estimator. Experiments on synthetic and hyperspectral datasets demonstrate that nearly identical reconstruction errors can yield markedly different structural-loss profiles; hyperspectral patches with comparable reconstruction errors exhibit up to a 4.6-fold difference in Direction Loss, correlating with severe visual blurring.

---


### 309. [AptAvatar: Fast and Vivid Long-Form Audio-Driven Video Generation for Production-Ready Avatars](https://arxiv.org/abs/2607.24013)

**<font color=#1a73e8>作者：</font>** Hengyuan Zhang, Jingna Sun, Meiguang Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Production-ready audio-driven avatar generation requires efficient inference without sacrificing fidelity or motion expressiveness. However, existing acceleration methods often compromise quality through restrictive architectural choices, such as causal attention and short temporal horizons, or by reducing model capacity and resolution. Without such compromises, we propose AptAvatar, a 14B-parameter long-form audio-driven avatar generation framework that delivers fast and expressive inference. For efficiency in production-level applications, AptAvatar addresses the extreme two-step generation challenge. To bridge the gap between the multi-step teacher model and the two-step student model, we introduce Endpoint-Anchored Distribution Distillation. It augments vanilla distribution matching with a dedicated Anchor Score Estimator trained on the trajectory-endpoint distribution defined from a frozen pretrained 4-step bridge generator. This provides an attainable endpoint-level anchor for the evolving two-step student. To improve long-horizon consistency, we further introduce Self-Generated History Replay, which reuses cached outputs from earlier generator checkpoints as history conditions during chunk-wise training. This approximates inference-time conditioning on self-generated histories without costly online rollouts, mitigating quality degradation from accumulated history errors. Extensive experiments demonstrate that AptAvatar generates vivid 720p long-form avatar videos with only 2 NFEs, achieving a 60x speedup while preserving visual fidelity and long-horizon identity. Code is available at this https URL

---


### 310. [DailyBench: A Unified Benchmark for AI-Generated and Manipulated Images from Modern Generative Models](https://arxiv.org/abs/2607.24016)

**<font color=#1a73e8>作者：</font>** Xin Jiang, Hao Tang, Junyao Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative models have shifted AI-generated image detection from identifying easily distinguishable, fully synthetic images to identifying highly realistic content generated by both modern generation and manipulation pipelines. However, existing detection benchmarks are often built with outdated generative models and primarily emphasize full-image synthesis, creating a growing mismatch between benchmark data and the images encountered in real-world generation and editing scenarios. To bridge this gap, we introduce DailyBench, a high-quality unified benchmark for evaluating whether AI-generated image detectors can generalize across both modern full-image synthesis and object-level manipulation. DailyBench contains two complementary subsets: FakeBench, which includes high-quality images synthesized by recent open-source and commercial generative models, and ManipulationBench, which introduces challenging object-level edits applied to real images using advanced image-conditional models. This design makes DailyBench a realistic testbed for studying both generator-level generalization and manipulation-aware detection under subtle local edits. Experiments on DailyBench reveal substantial robustness gaps in current detectors: methods reporting 91-96% balanced accuracy on GenImage drop to 60-76% on FakeBench and 54-66% on ManipulationBench. These results show that existing detectors remain poorly generalized to realistic synthesis and manipulation, highlighting DailyBench as a rigorous testbed for developing robust and manipulation-aware AI-generated image detection methods. The project is available at this https URL

---


### 311. [Self-Supervised Consistency Enhanced Disentangled Learning for Neural Decoding Generalization in Brain-Machine Interface](https://arxiv.org/abs/2607.24023)

**<font color=#1a73e8>作者：</font>** Jiyu Wei, Di Hong, Zhanjie Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Brain-Machine Interfaces (BMIs) provide a direct communication pathway between the brain and external devices, enabling humans to control assistive and robotic technologies, with potential applications in rehabilitation, human motor augmentation, and human-centered robotics. However, due to neural drift, the performance of BMIs decreases over time, posing challenges for long-term viability, particularly for invasive BMIs (iBMIs). Existing solutions suffer from two main drawbacks: (i) difficulty in learning robust neural representations, and (ii) neglecting that neural drift varies across motor parameters (e.g., velocity, direction, and speed). To overcome these limitations, we propose Self-Supervised Consistency enhanced Disentangled Learning (SSCDL), a neural decoding generalization framework built on two key innovations. We first design a backbone model named Consistency enhanced Neural Decoder (CND), using a novel teacher-student consistency constraint with simulated neural signal perturbations to learn robust representations invariant to neural drift. Then, we employ three dedicated CNDs under the Complementary-Disentangled Generalization (CDG) mechanism, which disentangles motor signals into velocity, direction, and speed with inspiration from neural preference theory. This disentangled learning enables SSCDL to capture invariant neural representations from diverse neural preference perspectives, significantly enhancing cross-day generalization. Extensive experimental results show that SSCDL delivers state-of-the-art decoding performance, exhibiting high robustness and cross-day stability. These capabilities underscore its strong potential for long-term interaction in human-centric robotic and fine-grained assistive applications.

---


### 312. [A Unified Stereo Geometry Estimation Framework for Disparity and Surface Normal](https://arxiv.org/abs/2607.24024)

**<font color=#1a73e8>作者：</font>** Qizhe Wei, Xianda Guo, Shaocong Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo matching and surface normal estimation are fundamental tasks in 3D vision. However, existing feed-forward stereo methods still struggle to produce reliable predictions in challenging regions, mainly due to the lack of strong geometric priors. In this paper, we propose $\textbf{GeoStereo}$, a unified stereo geometry estimation framework that leverages powerful diffusion priors to jointly predict disparity and surface normals. Specifically, GeoStereo couples a feed-forward stereo matching pipeline with a diffusion-based normal estimation branch. To enable effective interaction between the two tasks, we introduce a disparity to normal initialization strategy and construct a warp to left-view condition for the diffusion process. This coupled design allows the diffusion branch to provide strong structural priors that enhance disparity estimation in ill-posed regions, while the feed-forward branch offers reliable geometric guidance for accurate normal prediction. Extensive experiments show that GeoStereo performs reliably in challenging scenarios, including low-light environments, highly reflective surfaces, and transparent objects. Under zero-shot settings, it achieves Rank-1 disparity estimation on multiple benchmarks, including KITTI and NYUv2, and delivers the best normal estimation accuracy on many real indoor benchmarks, such as iBims-1 and ScanNet. Project page: this https URL

---


### 313. [Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification](https://arxiv.org/abs/2607.24027)

**<font color=#1a73e8>作者：</font>** Haopeng Li, Yitong Li, Junsong Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers are essential for high-fidelity video generation, but long token sequences make attention a dominant inference bottleneck. Training-free dynamic sparse attention alleviates this bottleneck by computing only selected key-value blocks, yet existing methods struggle to sparsify attention both efficiently and accurately for two reasons: (1) Rigid, unpredictable, and costly routing: selecting a fixed fraction of top-ranked blocks by proxy score imposes fixed budgets, whereas retaining blocks to reach a target cumulative proxy probability mass yields dynamic but potentially imbalanced budgets; both incur non-negligible overhead from computing and materializing proxy scores. (2) Lossy keep-or-drop sparsification: unselected blocks are discarded entirely, degrading accuracy under aggressive sparsity. These limitations motivate cheaper dynamic-budget routing while limiting accuracy degradation. In this paper, we introduce training-free Sol-Attn (Sparsifying online attention), which unifies dynamic routing, sparse computation, and approximation correction in a single online-softmax pass, achieving a better accuracy-efficiency trade-off in sparse attention. The core of Sol-Attn is on-the-fly block thresholding with proxy-score reuse, which selects critical blocks by comparing block proxy scores against a threshold during online softmax. This design enables dynamic yet controllable block budgets without materializing the proxy map, while directly reusing the proxy scores of unselected blocks to approximate their contribution. Experiments across image and video generation tasks show that Sol-Attn advances the quality-efficiency frontier of training-free sparse attention, delivering 2.1 times and 2.3 times end-to-end speedups for video generation and editing, respectively, while preserving visual quality.

---


### 314. [MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition](https://arxiv.org/abs/2607.24030)

**<font color=#1a73e8>作者：</font>** Sangmin Lee, Woojin Chung, Woongjib Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Massively multilingual automatic speech recognition (ASR) models covering hundreds of languages must maintain robust performance across diverse linguistic and acoustic conditions. However, these models often encounter the curse of multilinguality, where model capacity is diluted across languages. To address this challenge, we propose Mixture of Language Group Experts (MoLGE), built upon speech self-supervised models (S3Ms). MoLGE assigns dedicated expert modules to clusters of similar languages, reducing the number of required submodules compared to conventional language-specific Mixture-of-Experts (MoE) schemes. It further integrates a hierarchical Low-Rank Adaptation (LoRA) strategy into the disentangled acoustic and linguistic components of the S3M architecture, enabling efficient modeling of language-specific characteristics while maintaining parameter efficiency. Further, we investigate the impact of language grouping strategies based on both linguistic and data-driven criteria on overall performance, providing an interpretable perspective on how language structure influences scalability in multilingual speech systems. In experiments, we evaluate MoLGE on a multilingual benchmark encompassing 495 languages. Results demonstrate that MoLGE consistently outperforms dense multilingual baselines with a minimal increase in trainable parameters. Notably, these language grouping strategies yield substantial improvements for both phonetic and orthographic aspects of ASR modeling. Our findings suggest that structured language specialization provides an effective pathway for massively scaling language coverage of multilingual ASR.

---


### 315. [A Cyclic Adaptation-Generalization Framework with Uncertainty-Guided Self-Paced Learning for Long-Term Brain-Machine Interfaces](https://arxiv.org/abs/2607.24031)

**<font color=#1a73e8>作者：</font>** Jiyu Wei, Di Hong, Zhanjie Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Brain-Machine Interfaces (BMIs), which link the brain to external devices, hold great potential in rehabilitation, human performance augmentation, and human-centered robotics. However, invasive BMIs face a critical challenge for long-term deployment due to neural drift, which degrades decoding performance over time and necessitates frequent recalibration. Existing methods designed to mitigate neural drift typically rely on either domain adaptation (DA) or domain generalization (DG) alone and often fail to capture fine-grained distribution shifts across neural subdomains, resulting in limited performance. To overcome these limitations, we propose Uncertainty-guided Self-paced Cycling (UnSPC), a robust framework that synergizes DA and DG for target domain refining under an Uncertainty-guided Self-paced Pseudo-labeling (UnSPL) mechanism. To handle subdomain neural drift across domains, UNSPL is proposed to iteratively mine reliable pseudo-labeled samples with a noise-robust ranking strategy for further fine-tuning. Leveraging these high-quality samples, we introduce a novel Cycling Adaptation and Generalization (CycAG) strategy, which integrates DA and DG within an iterative cycle to progressively mitigate both global and subdomain drift. This cyclic process enables effective alignment to evolving target distributions while preserving robust and transferable representations, thereby mitigating performance degradation under long-term neural drifts. Extensive experiments on multiple neural decoding datasets demonstrate the effectiveness and robustness of UnSPC. To our knowledge, our proposed UnSPC is the first to cyclically integrate DA and DG with pseudo-labeling, paving the way toward stable long-term BMI controls.

---


### 316. [The Half-Lives of Generative-AI Evidence: A 40-Record Audit, a Claim-Currency Framework, and a Reflexive Case of Frontier-Model-Assisted Research](https://arxiv.org/abs/2607.24032)

**<font color=#1a73e8>作者：</font>** Carlo Iacono  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative-AI evaluations can become historical before publication, yet calendar age does not affect every conclusion equally. This paper has two linked purposes. First, it audits a maximum-variation purposive corpus of 40 empirical records appearing between 18 July 2025 and 17 July 2026. The audit coded publication route, execution timing, model identity, age of the newest named generation or immutable snapshot, same-family supersession and refresh behaviour. At appearance, the newest named model was a median 281 days old (middle 50%: 75-478; range: 11-939). Median age was 395 days for 25 journal articles, 56 days for 14 preprints and 49 days for one laboratory report. Thirty-five records included a superseded family, seven supplied a precise dated identifier, three clearly refreshed model evidence, and one added a late sensitivity test. All 40 included an OpenAI system, a feature of this corpus rather than a prevalence estimate. The paper distinguishes model age from claim currency and proposes six reporting practices. Second, it treats its own two-day production process as a reflexive case of frontier-model-assisted research creation. GPT-5.6 Sol Pro in ChatGPT supported candidate discovery, source reconciliation, calculations, drafting and critique; the author checked sources, made all substantive decisions and accepts responsibility. This is a proof-of-practice, not a controlled estimate of productivity or quality. By applying its own Model Facts and model-currency statement, the paper shows how rapid AI-assisted research can be made inspectable without treating model output as independent validation. The title uses half-lives metaphorically; no universal decay rate is estimated.

---


### 317. [Pointer-Augmented Autoregressive Generation of Patent Claims with Joint Topology and Content Decoding](https://arxiv.org/abs/2607.24040)

**<font color=#1a73e8>作者：</font>** Yongmin Yoo, Zhangkai Wu, Longbing Cao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive decoders emit flat token sequences and cannot enforce hierarchical constraints across output segments, a limitation that becomes acute in patent claim generation, where a claim set forms a dependency forest whose scope must narrow monotonically with depth. Topology and content are mutually dependent: a dependent claim's wording must reflect its parent's scope, yet the parent must be chosen before that wording exists, so neither post-hoc parsing nor grammar-constrained decoding suffices. We propose SPG (Structure-aware Patent Generation), which predicts topology inside the autoregressive pass. A pointer head selects each dependent claim's parent, and its gradients, together with a depth-adaptive scope regularizer, reshape the shared decoder's representations during training. A second stage then applies a violation-weighted preference objective over self-generated deficient candidates, supplying the negative signal that granted-patent corpora lack. On HUPD-DCG, SPG on Llama-3-8B-Instruct recovers 79.0\% of gold parent links, a quantity its training reward never supervises, and raises antecedent consistency from 0.292 to 0.478 over a supervised baseline of equal scale, with expert evaluation corroborating these gains.

---


### 318. [A Design Space for Quantum Circuit Visualizations](https://arxiv.org/abs/2607.24042)

**<font color=#1a73e8>作者：</font>** Hyeok Kim, Leilani Battle  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Quantum circuit visualizations play an essential role in supporting sense-making and communication of quantum programs. While several tools exist for rendering quantum circuits, they vary widely in encoding options due to idiosyncrasies among machine and platform providers. We observe an opportunity to coalesce these disparate rendering approaches under a single, unified grammar to enable consistent, cross-platform enhancement of quantum circuit visualizations. However, it is unclear how to design such a grammar to best support the quantum computing community. Towards this end, we contribute a design space of quantum circuit visualizations by analyzing 182 static and 12 interactive cases collected from online tutorials and documentations, research publications, public presentations, and prior systems. Based on our analysis, we discuss how our design space relates to existing visualization principles yet exhibits unique aspects. We conclude with opportunities for future systems regarding data structure, cognition, and integrability.

---


### 319. [The Effect of Photorealism Consistency between the Virtual Hands and Environment on the Sense of Body Ownership and Presence in Virtual Reality](https://arxiv.org/abs/2607.24047)

**<font color=#1a73e8>作者：</font>** Nami Ogawa, Takuji Narumi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual reality (VR) technology allows users to feel a virtual body as if it was their own (i.e., body ownership illusion). Previous studies have explored how the visual realism of the user's virtual body influences the sense of body ownership in VR, focusing on the aspect of anthropomorphism. However, the effect of photorealism, another element that characterizes the visual realism of a virtual human, has not been systematically examined in the context of body ownership illusion. Therefore, we investigate the effect of the rendering style of virtual hands on the sense of body ownership, hypothesizing that the effect is affected by the rendering style of the virtual environment. In addition, we examine the effect of photorealism on presence (i.e., the sense of being there), as existing studies have offered inconsistent evidence. To this aim, we conducted a 3 x 3 mixed-design remote VR experiment (N=117) that factored in the rendering styles of both the virtual hand and the environment and analyzed the subjective data from the questionnaire. The results suggest that neither the rendering style of virtual hands nor the consistency of the rendering style between the virtual hand and the environment influenced the sense of body ownership. Nevertheless, the more photorealistically the virtual environment was rendered, the stronger the presence. Our results indicate that different dimensions of virtual body realism affect the sense of body ownership differently, thereby highlighting the importance of applying a suitable classification of realism to understand the body ownership illusion for virtual bodies more in depth.

---


### 320. [Quantum-Inspired Evolutionary Neighborhood Search for Arrival-Departure Track Utilization Adjustment under Short-Term Disturbances](https://arxiv.org/abs/2607.24049)

**<font color=#1a73e8>作者：</font>** Xiaobin Li, Wuming Lei, Yanbin Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Short-term disturbances at major passenger railway stations alter train arrival and departure times as well as the release sequence of station resources. Effective recovery therefore requires coordinated adjustment of arrival-departure track allocation, station resource occupation, and train retiming. This study represents the station resources involved in train arrival, track occupancy, and departure operations as zone-level resource-occupation intervals. An arrival-departure track allocation adjustment model is formulated. Resource compatibility is imposed as the feasibility condition, while train delays and resource reassignment costs are jointly considered. A quantum-inspired evolutionary algorithm combined with neighborhood search (QEA-NS) is proposed to solve the model. Perturbation instances are constructed using GTFS timetable data from Frankfurt Hauptbahnhof, Germany. QEA-NS is compared with CP-SAT under the same candidate resource set and feasibility criteria. Both methods generate solutions satisfying the modeled resource compatibility constraints. QEA-NS yields a total delay of 388 min, compared with 519 min for CP-SAT, representing a reduction of 25.2\%. The mean delay of delayed trains decreases from 4.99 to 3.73 min, although QEA-NS requires a longer solution time. Across 10 random perturbation instances, QEA-NS achieves lower total delay in every case. Its mean total delay and standard deviation are 390.5 min and 35.945 min, respectively, compared with 673.8 min and 105.739 min for CP-SAT. The results indicate that, under the adopted resource representation and constraints, QEA-NS improves the delay performance of recovery plans. Its computational efficiency, however, requires further improvement.

---


### 321. [PointCHR: Point Cloud Analysis via Curvature-Aware Hyperbolic Rectification](https://arxiv.org/abs/2607.24052)

**<font color=#1a73e8>作者：</font>** Xinxing Yu, Liying Yang, Hao Mo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-curvature regions in 3D point clouds encapsulate critical fine-grained geometric semantics yet exhibit a distinct long-tail sparsity in their spatial distribution. The inherent limitations of polynomial volume growth in Euclidean space frequently render these intricate geometric features challenging to adequately resolve within a uniform-scale feature space. Consequently, these regions are frequently overshadowed by smooth global features dominated by low-curvature regions, thereby limiting the discriminative capacity of the network. To address this issue, we propose PointCHR, a curvature-aware hyperbolic rectification (CHR) for point cloud analysis. Utilising the property of exponential volume expansion in the vicinity of hyperbolic manifolds, CHR presents a learnable curvature-guided radial rectification mechanism. By adaptively projecting high-curvature points towards boundary regions endowed with larger effective embedding capacities, PointCHR effectively mitigates the representation crowding problem inherent in Euclidean settings. Extensive experimentation has demonstrated that PointCHR significantly enhances the ability of backbone to capture fine-grained geometric details, achieving state-of-the-art performance across multiple benchmarks.

---


### 322. [Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation](https://arxiv.org/abs/2607.24054)

**<font color=#1a73e8>作者：</font>** Jingkun Luo, Da-Tian Peng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A correct answer can conceal why an agent succeeded. Once agents change their information state during evaluation, correctness no longer distinguishes intended reasoning from answer acquisition. Outcome evidence and exposure detection do not establish whether success depended on an acquired target; we call this missing evaluation object success provenance. AcquaBench audits it through matched CLEAN, GOLD, and SHAM value substitution on four standardized surfaces with joint qid-clustered analysis. CLEAN retains benchmark-authorized information. GOLD makes the correct target available. SHAM preserves source structure and exposure opportunity but substitutes a matched incorrect value. GOLD minus CLEAN measures the total score response to correct-target availability; GOLD minus SHAM tests whether that response tracks target correctness beyond matched source exposure. In D0, GOLD exceeds SHAM by 19.1 to 25.9 percentage points, showing that success follows the correct value. In D2, GOLD still exceeds SHAM under distributed sufficiency while coloc no longer transfers as a high-score marker, with AUROC 0.376 and 0.142. Behavioral dependence can thus persist beyond this probe's intended observation unit. In model comparison, a supported 5.0-point CLEAN score gap compresses to a raw GOLD difference of -0.6 points without establishing rank inversion. Agent benchmarks should report success together with whether the evaluated information state supported it.

---


### 323. [Capacity-Aware Deep Learning for Generalizable Traffic Volume Estimation Across Links and Cities](https://arxiv.org/abs/2607.24056)

**<font color=#1a73e8>作者：</font>** Léo Hein, Giovanni De Nunzio, Aurélie Pirayre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Network-wide traffic volume estimation typically relies on propagating measurements from fixed sensors, making performance highly dependent on sensor density and limiting deployment in sparsely instrumented networks. We propose a link-level learning framework that estimates hourly traffic volumes from widely available territorial data only, including probe speed profiles, road and topological descriptors, along with weather observations. A supervised local mapping is learned from sparse sensor measurements and evaluated under two generalization settings: intra-network (unseen links within the training network) and inter-network (unseen city). This formulation frames traffic volume estimation as a spatial out-of-distribution generalization problem under sparse supervision. To enhance spatial robustness, we introduce a capacity-aware formulation that models volume as the product of a link-specific structural capacity and an hourly regime-aware utilization ratio, embedding traffic-theoretic constraints directly into the learning process. Extensive experiments in both generalization settings demonstrate that the proposed structural constraints consistently outperform a state-of-the-art baseline under spatial distribution shift.

---


### 324. [Constrained Reinforcement Learning Using Successor Representations](https://arxiv.org/abs/2607.24057)

**<font color=#1a73e8>作者：</font>** Michael Girstl, Alexander Mattick, Christopher Mutschler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world Reinforcement Learning depends on the ability to formulate safety constraints into a policy. A common way to model such constraints is to introduce an additional cost signal in the Markov Decision Process, which notifies the agent of unwanted behavior independently of the reward signal. Unfortunately, current methods are hard to adapt to changes in the cost function introduced by, e.g., domain shift or obstacles moving over time. The lack of adaptability means that policies are too unflexible to deal with complex real-world conditions. We propose the Safe Deep Successor Representation (SafeDSR), a novel method that allows quick retraining of policies towards new cost structures. SafeDSR extends the Deep Successor Representation (Kulkarni et al., 2016) to Constrained Reinforcement Learning by introducing a single learnable weight matrix to decouple the learned value function across dynamics, rewards, and costs. This matrix can be updated in a supervised manner instead of having to adapt the whole network if the cost structure of the environment changes. We demonstrate this ability in a freely configurable two-dimensional navigation environment and show that our method is competitive on a simple navigation task while being considerably more flexible

---


### 325. [ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning](https://arxiv.org/abs/2607.24062)

**<font color=#1a73e8>作者：</font>** Wenwu Fan, Qihong Lin, Zhijie Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) training for Large Language Models (LLMs) often suffers from instability due to the discrepancy between training and inference. This training-inference discrepancy stems from two primary factors: an architectural separation between training and inference engines, and the use of low-precision quantization in inference versus higher-precision computation in training. To address training instability issues caused by high training-inference discrepancy, we present the principles and methods for its adaptive control. We propose Adaptive Control Reinforcement Learning (ACRL), which adaptively maintains the training-inference discrepancy within a reasonable range to ensure stable RL training. Beyond stabilization, ACRL inherently increases policy entropy, thereby enhancing exploration and improving accuracy. The experimental results show that when the inference engine utilizes FP8 quantization, ACRL consistently maintains the training-inference discrepancy within a reasonable range and stabilizes RL training. Furthermore, ACRL not only matches the accuracy of the BF16 baseline but also outperforms importance sampling (IS) fixes.

---


### 326. [The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards](https://arxiv.org/abs/2607.24063)

**<font color=#1a73e8>作者：</font>** Keyu Li, Jin Gao, Dequan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On standard factuality tasks, frontier models now cluster near the top of the scale. The question is therefore shifting from how factual a system is toward how much compute that factuality costs. Static leaderboards score factuality in isolation and treat compute as free, so they cannot tell a genuinely better system apart from one that simply spends more. Consider a ranking reversal. A brute-force Best-of-4 agent posts the higher raw factuality score (H-Score 0.9169 vs 0.9103) and would top a static leaderboard, but once cost is counted it is the worse system, losing on Q-Score (0.5169 vs 0.5217) at roughly four times the tokens and latency, under a reported cost weight whose sensitivity we sweep. So the system that tops a static leaderboard can be the worse one to deploy. To make this trade-off visible, we introduce MAS-HQ (Multi-Agent System Hallucination Quest), a resource-aware evaluation protocol. It wraps any factuality detector and normalizes for cost, and it pits systems against each other rather than scoring them in isolation. The Q-Score measures factuality minus normalized cost under a competitive match. Across summarization and open-domain QA, single-agent baselines drift into resource-heavy over-optimization, while competition elicits more resource-efficient policies. These gains are small but consistent, and stable across 100 trials. The axis stays discriminative for frontier systems (Gemini-2.5-Pro, and GPT-5 in simulated preview) whose raw factuality scores are already bunched near the ceiling. MAS-HQ provides a reproducible way to measure how much a factual answer costs.

---


### 327. [MarineEVT: Advancing Event-Centric Marine Video Understanding via Visual Tool Reasoning](https://arxiv.org/abs/2607.24064)

**<font color=#1a73e8>作者：</font>** Tuan-An To, Yuk-Kwan Wong, Tuan-Anh Vu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Vision-Language Models (VLMs) have achieved remarkable success in visual understanding, driven by the growing availability of high-quality image-text pairs. However, the performance of VLMs often degrades in the video domain due to the essential need for temporal understanding and the scarcity of large-scale annotated video data. In this work, we focus on marine video understanding, which brings further challenges: first, it requires substantial domain expertise; and video VLMs usually struggle with localizing and interpreting critical information from marine videos, as the informative events are typically sparse, unpredictable, and unevenly distributed. To address these challenges, we carefully curate the first event-centric marine video understanding dataset called MarineEVT, which features 20K multi-task, video-level visual question-answering pairs spanning multiple dimensions of marine understanding and analysis. Meanwhile, based on MarineEVT, we decompose marine video understanding as an Event-centric Visual Tool-integrated Reasoning process EVT-R1 for short, where we leverage powerful visual tools to drive the model to localize and interpret critical information aligned with visual questions and human intent. To demonstrate its effectiveness, we compare EVT-R1 against 11 SOTA VLMs in different settings. EVT-R1 outperforms the top open-source and top commercial models by 5.22 and 11.09, respectively. MarineEVT and EVT-R1 lay the foundation for ecological discovery and marine education, fostering the development of VLMs capable of interpreting marine dynamics, reasoning about ecological interactions, and supporting sustainable ocean video understanding and analysis.

---


### 328. [MiSS: A Logic-Driven Explanation of Minimal Sufficient Coalitions for Point Cloud Classifiers](https://arxiv.org/abs/2607.24074)

**<font color=#1a73e8>作者：</font>** Mengda Xing, Jean-Marie Lagniez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present MiSS, a black-box, query-based framework for explaining 3D point cloud classifiers through perturbation-relative sufficiency reasoning. MiSS treats a superpoint partition as an interpretable abstraction layer and asks whether the original prediction can be certified from a minimal coalition of geometric regions under a specified perturbation distribution. Unlike abductive explainers that require Boolean feature spaces or white-box logical encodings of the predictor, MiSS separates candidate proposal from verification: a weighted MaxSAT procedure proposes coalitions using a heuristic adaptive cardinality floor, certified exact-size fallback, a safely tightened upper bound, blocking clauses, and a surrogate acquisition heuristic learned from previous oracle evaluations, while a blackbox statistical oracle decides sufficiency from prediction queries. The system returns a statistically verified sufficient coalition as a binary attribution, with minimum cardinality guaranteed when certified search completes. Experiments on ModelNet40 and ShapeNet with PointNet and PointMLP classifiers show higher precision and coverage than rule-based baselines in most settings, with lower explanation time than exhaustive search.

---


### 329. [When Low CER is Not Enough: An Analysis of Hallucinations in Vision-Language OCR Systems on Historical Uruguayan Documents](https://arxiv.org/abs/2607.24077)

**<font color=#1a73e8>作者：</font>** Marina Gardella, Camilo Mari{ñ}o, Diego Belzarena 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) is a key component in the digitization of historical archives. Recently, Vision-Language Models (VLMs) have emerged as strong alternatives to traditional OCR systems, achieving state-of-the-art performance on standard benchmarks. However, their suitability for archival transcription remains insufficiently understood. In this work, we benchmark traditional OCR systems and VLM-based approaches on the Berrutti dataset, a challenging collection of Uruguayan dictatorship-era documents derived from microfilm scans. While VLMs consistently outperform traditional methods in terms of Character Error Rate (CER) and Word Error Rate (WER), we show that these improvements hide a more complex picture. Through a detailed qualitative analysis, we uncover systematic failure modes that are invisible to standard metrics, including orthographic normalization, spurious content generation, and semantic substitutions that preserve fluency while altering meaning. Errors affecting named entities are particularly critical, as they can introduce substantial semantic distortions with minimal impact on CER and WER. These findings reveal a critical gap between quantitative OCR performance and transcription fidelity in real-world archival settings, and highlight the need for evaluation frameworks that go beyond character-level accuracy to capture the semantic reliability of generated transcriptions.

---


### 330. [Towards simultaneous decoding of kinetic and kinematic movement parameters during grasp and lift task by noninvasive brain imaging](https://arxiv.org/abs/2607.24081)

**<font color=#1a73e8>作者：</font>** Parth G. Dangi, Yogesh Kumaar Meena  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Brain-machine interfaces (BMIs) can assist individuals with limited mobility, such as stroke survivors or amputees. One of the key challenges in developing BMIs is expanding their usability and control, which can be achieved by accurately decoding multiple kinematic and kinetic parameters. To address this, we propose three regression models: partial least squares regressor, multilayered perceptron, and attention based regressor, to decode multiple movement parameters from EEG signals. We evaluated these models on the WAY EEG GAL dataset, focusing on their performance under subject specific and subject independent conditions with two strategies: a single model for all parameters and a baseline with separate models for each parameter. Among all regressors, the attention based regressor achieved the best performance, with an $R^2$ of 0.8 and a latency of 29.2 milliseconds, demonstrating significant improvement in simultaneous multi parameter decoding. However, its performance dropped for single parameter decoding. The multi layered perceptron showed more consistent but lower accuracy across both decoding types ($R^2$ = 0.49). These findings highlight the potential of attention based models for real time multi command BMI systems and contribute to the development of more intuitive control devices.

---


### 331. [Towards High-Level Semantic Intelligence](https://arxiv.org/abs/2607.24082)

**<font color=#1a73e8>作者：</font>** Xiujie Song, Gefei Yang, Yining You 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI have substantially expanded its cognitive and reasoning capabilities. From the perspective of semantic complexity, the development of AI reveals a clear trajectory from simple to complex semantic processing. While early AI systems mainly addressed tasks involving direct and literal semantic perception or expression, contemporary systems are increasingly expected to perform more sophisticated cognitive reasoning, enabling the understanding and generation of High-Level Semantics (HLS). A similar trajectory can also be observed in human cognitive development. We define this transition as the shift from Basic-Level Semantic Intelligence (BLSI) to High-Level Semantic Intelligence (HLSI). However, this issue has not yet been systematically and comprehensively examined in prior work. Motivated by this gap, this survey reviews the development of AI semantic intelligence from the perspective of semantic complexity. We systematically survey existing research on HLS tasks, including humor, sarcasm, metaphor, empathy, persuasion, narrative, and other general HLS phenomena, across text, speech, vision, and multimodal scenarios. Specifically, we summarize data construction methods, modeling and optimization strategies, and evaluation methodologies for both understanding and generation. HLS is essential for advancing AI toward genuinely human-like intelligence. By synthesizing existing methods and insights from the perspective of semantic intelligence, this survey aims to support the continued development of AI toward HLSI.

---


### 332. [Learning Reusable Hybrid Motion Priors for Humanoid Locomotion from Motion Imitation](https://arxiv.org/abs/2607.24083)

**<font color=#1a73e8>作者：</font>** Valerio Belli, Valerio Modugno, Enrico Mingo Hoffman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning can produce robust humanoid controllers, but each new task is typically trained as a separate policy with its own reward design and training process. Motion imitation provides an alternative source of motor competence by training policies to track retargeted human motions, yet the resulting controllers remain reference trackers and are not directly usable as task policies. We propose a three-stage pipeline that turns motion-imitation skills into a reusable hybrid motion prior (HMP) for humanoid locomotion. First, an expert policy is trained to imitate retargeted human motion-capture clips. Second, the expert is distilled into a frozen architecture composed of a proprioceptive encoder, a residual vector-quantized (RVQ) codebook, and an action decoder. Third, task-level policies are trained to solve locomotion tasks by selecting discrete codebook entries while the HMP remains frozen. We evaluate the method on velocity tracking, point-goal navigation, and fall-recovery velocity tracking in simulation, and deploy the velocity-tracking policy on a real Unitree G1 robot. The distillation process preserves the tracking behavior of the expert, while the resulting HMP can be reused without retraining as the action interface for different downstream locomotion policies. The learned HMP reveals an interpretable codebook structure in which the number of active RVQ stages modulates the available gait patterns. We further show that training the codebook with the rotation trick improves latent organization and reduces downstream falls compared with a standard straight-through estimator.

---


### 333. [Cascade Forgery Mining Network for Fingerprint Presentation Attack Detection](https://arxiv.org/abs/2607.24090)

**<font color=#1a73e8>作者：</font>** Hongyan Fei, Chuanwei Huang, Zheng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fingerprint Presentation Attack Detection (PAD) is a critical component of fingerprint identification systems, serving as a protective measure against unauthorized access. In this paper, we observe that different regions of a fingerprint image can exhibit varying Artifact Extraction Difficulty (AED), with high-AED regions requiring more sophisticated extraction mechanisms to capture more subtle discriminative evidence. To address this issue, we propose to quantify AED using local Gabor feature certainty and partition fingerprint images into multiple regions based on their respective AED values. We then propose an AED guided Cascade Forgery Mining Network (CFM-Net) that employs an adaptive-depth feature extraction architecture to detect more precise and comprehensive artifact evidence across regions with heterogeneous AED values. Furthermore, we introduce an Orientation Guided Adversarial Training (OGAT) module to filter out identity information from PAD features while preserving the integrity of original artifact evidence. Experimental evaluations on LivDet datasets demonstrate the superior performance of our approach compared to state-of-the-art methods and achieve significant improvement in the classification ability of high AED fingerprints.

---


### 334. [LU-500: A Logo Benchmark for Concept Unlearning](https://arxiv.org/abs/2607.24101)

**<font color=#1a73e8>作者：</font>** Keyu Li, Jin Gao, Jialing Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept unlearning is increasingly used to limit the reproduction of protected or unsafe visual concepts in text-to-image models. Existing evaluations, however, mostly study targets that dominate the whole image, such as styles, broad object categories, or portrait-like identities, leaving company logos comparatively underexamined. Logos create a different failure mode: a small localized mark can carry the entire protected concept, must be visually precise to remain recognizable, and can be triggered implicitly by products, storefronts, packaging, or advertisements even when the word ``logo'' is absent. We introduce LU-500, a logo-unlearning benchmark built from Fortune Global 500 companies to study this localized and semantically entangled setting. LU-500 contains nearly 10,000 curated text-query and logo-image pairs, with an explicit track (LUex-500) and an implicit contextual track (LUim-500). To avoid reducing the task to a binary detector score, we define a multi-grained protocol that evaluates both local logo removal and global image preservation in pixel and latent spaces. Experiments on representative inference-time methods, including NP, SLD, and SEGA, and compatible fine-tuning-based methods such as ESD and Forget-Me-Not, show that the evaluated methods struggle to remove logo evidence without changing non-target content. We further analyze ProLU, a prompt-space multi-agent baseline: it improves local erasure by removing logo-inducing semantics, but also illustrates why prompt filtering is not a substitute for weight-level disentanglement. Correlation analyses over logo area, location, and structural complexity suggest that future logo unlearning may need spatially aware controls, such as SSIM-guided constraints, rather than purely global concept suppression.

---


### 335. [BeyondFusion: Self-Aligned Latent Diffusion for Calibration-Free Infrared Super-Resolution and Infrared-Visible Fusion](https://arxiv.org/abs/2607.24110)

**<font color=#1a73e8>作者：</font>** Minchong Chen, Xiaoyun Yuan, Minyu Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile infrared-visible imaging typically pairs a compact infrared sensor with a high-resolution visible camera for complementary perception. While cross-sensor misalignment caused by different optics, viewpoints, fields of view, and exposure timings hinders practical deployment. In this paper, we propose BeyondFusion, a unified latent diffusion framework for calibration-free visible-guided infrared super-resolution and infrared-visible fusion tasks. The proposed framework supports both task-specific training and joint training where two tasks are optimized and executed as two readouts of the same generative process. Instead of relying on explicit registration or geometric warping, BeyondFusion introduces a cross-modal self-aligning (CMSA) module into the denoising U-Net. CMSA reorganizes infrared and visible latent tokens into a shared attention space to learn content-adaptive cross-modal correspondence during the denoising process. Together with misalignment augmentation module, the model is facilitated to exploit visible structural and semantic cues while preserving thermal consistency, enabling high-frequency infrared reconstruction and informative fused-image generation under uncalibrated conditions. Extensive experiments on public benchmarks and a mobile infrared-visible imaging system show strong performance across aligned inputs, low-resolution infrared observations, synthetic misalignments, and real mobile captures with unsynchronized sensors. Ablation studies, unified training analysis, and downstream pedestrian detection further validate the effectiveness of BeyondFusion for calibration-free multimodal imaging.

---


### 336. [Scaling GUI Agents with Visual State Transitions](https://arxiv.org/abs/2607.24112)

**<font color=#1a73e8>作者：</font>** Xiangyan Liu, Kaixin Li, Haonan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce State Transition Pretraining (STP) as a new scaling axis for GUI agents. During the STP stage, we continually pretrain a unified multimodal model on visual state transitions by jointly optimizing inverse dynamics (predicting actions from state changes) and forward dynamics (predicting next states from current states and actions). This optimization equips the model with better action-grounded visual representations and an internal world model of GUI dynamics. When subsequently fine-tuned on trajectories with task instructions, our STP-trained models consistently outperform baselines trained solely via direct trajectory fine-tuning across agent benchmarks in both desktop and mobile GUI scenarios (AgentNetBench, AndroidControl, and GUIOdyssey). Further empirical studies show that joint dynamics optimization yields stable improvements over single-objective training, and downstream performance scales steadily with the volume of transition data.

---


### 337. [Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems](https://arxiv.org/abs/2607.24117)

**<font color=#1a73e8>作者：</font>** Ali Zahid Raja  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern multi-agent knowledge systems increasingly accumulate knowledge through chains of autonomous transformations rather than direct retrieval. Existing provenance work records what happened - execution traces, tool calls, evidence links - and source-reliability estimation is long established (truth discovery, reputation systems). What is missing is an operational framework that attaches graded, per-domain transmitter reliability to claim-level transmission chains, with completeness semantics, transformation-typed aggregation, decoupled content criticism, and serve/review/quarantine routing.
Classical Islamic hadith science confronted a structurally similar problem: deciding whether knowledge transmitted through chains of human narrators should be accepted. Over centuries it developed a rigorous methodology - isnad (a complete transmission chain attached to every claim), rijal (systematic grading of each narrator's integrity and precision), weakest-link chain evaluation, corroboration through independent chains, and matn criticism (content evaluated independently of chain quality). This paper transfers that methodology to AI system design.
We contribute a formal mapping from hadith-science concepts to multi-agent pipelines, a relational schema implementing claim chains and a graded narrator registry, a decision matrix combining chain grade with content criticism, and an evaluation on 20,000 claims from real physics textbooks. The evaluation validates weakest-link quarantine and independent-chain corroboration; reports a partial failure of the grade-recovery loop, which missed the highest-fault narrator; and reports two analyses as inconclusive, including a matched-coverage comparison the framework could not reach with the reference content critic. The paper is explicit throughout about which claims the evidence does and does not yet support.

---


### 338. [ViDS: Video Diffusion Shader using 3D Face Tracking](https://arxiv.org/abs/2607.24124)

**<font color=#1a73e8>作者：</font>** Wenbo Ji, Davide Davoli, Zhe Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ViDS, a Video Diffusion Shader that leverages 3D face tracking for expressive and identity-preserving portrait animation. We first reconstruct the identity-specific 3DMM mesh from the reference image, and then animate it using expression and pose parameters from a driving video. Leveraging dense geometric cues from 3DMM normal maps, we employ a video diffusion model as a neural shader to synthesize lifelike portrait animations while preserving the appearance and identity of the reference image. We find that more accurate 3DMM tracking enables finer-grained expression control. We also introduce an autoregressive diffusion sampling process that extends generation beyond the model's native window while reducing discontinuities between adjacent clips. Compared with prior diffusion-based approaches for portrait animation that rely on landmark-based conditioning or implicit motion latents, our method achieves more detailed and consistent expression and pose control while faithfully preserving identity and appearance. Detailed ablation studies validate the effectiveness of our design choices. Project page: this https URL

---


### 339. [EEGForceFusion: Joint Tokenised-Continuous Representation Learning for Subject-Independent Grasp Force Decoding](https://arxiv.org/abs/2607.24126)

**<font color=#1a73e8>作者：</font>** Sankalp Sunil Turankar, Yogesh Kumar Meena  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Brain-machine interfaces provide a link between neural activity and external devices, enabling restoration of motor function and advancing human-machine interaction using non-invasive electroencephalography (EEG). However, continuous grasp force decoding remains challenging due to complex temporal dynamics, high inter-subject variability, and limited generalisation of existing approaches. To address this, we propose a hybrid EEG decoding framework that jointly models continuous and tokenised representations, enabling capture of both fine-grained neural structure and long-range temporal dependencies. The proposed approach integrates convolutional-recurrent representation learning, quantisation-based tokenisation, and transformer-based temporal modelling within a unified fusion-based regression architecture. Experimental evaluation on the WAY-EEG-GAL dataset under strict leave-one-subject-out conditions achieves $R^2$ = 0.817 in offline settings and $R^2$ = 0.793 in simulated real-time evaluation, with latency suitable for real-time deployment. These results demonstrate strong cross-subject generalisation and highlight the practicality of hybrid continuous-tokenised representations for real-time EEG-based force decoding in assistive robotics, neuro-rehabilitation, and human-machine interaction.

---


### 340. [MAPLE: Efficient and Diverse Multi-Alpha Generation for Portfolio Construction](https://arxiv.org/abs/2607.24131)

**<font color=#1a73e8>作者：</font>** Yu-Chen Den, Kuan-Yu Chen, Kendro Vincent 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical alpha mining achieves strong risk-adjusted returns by combining many low-correlated predictive signals, yet deep learning stock-ranking methods typically produce a single alpha per stock, rely on increasingly complex architectures with diminishing gains, and obtain diversity only through separate models or implicit routing, without explicitly controlling inter-alpha correlation. We introduce MAPLE (Multi-Alpha Position-aware Listwise Ensembling), a backbone-agnostic framework that recovers this diversity principle within a single training pass. MAPLE combines a unified, capacity-scaled prediction head with an extreme-rank weighted listwise ranking loss and a diversity regularizer that explicitly penalizes pairwise correlation across alphas. Across four equity markets spanning the US, China, and Japan, MAPLE achieves the best average Sharpe and Calmar ratios among nine baselines, using up to 55x fewer parameters and 2.5x less training time, and generalizes across five backbone architectures with Sharpe and Calmar Ratio gains of 10-23% and 17-43%, respectively. Behavioral analysis further shows why each component works: the unified head already reduces inter-alpha correlation before any diversity loss is applied, and the extreme-rank loss lets diversity regularization improve rather than erode per-alpha ranking quality as capacity scaling sustains this balance at scale. These results show that principled loss design and capacity allocation, rather than architectural complexity, drive diverse and effective multi-alpha generation.

---


### 341. [LoTA-N2N: Local Trace Adaptation for Zero-Shot Self-Supervised Image Denoising](https://arxiv.org/abs/2607.24135)

**<font color=#1a73e8>作者：</font>** Jintong Hu, Bin Xia, Junlin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image self-supervised denoising replaces unavailable clean targets with surrogate targets constructed from noisy observations. Its effectiveness therefore depends on how closely the surrogate objective remains aligned with supervised denoising, especially when noise is correlated, spatially nonstationary, or unknown. We express the discrepancy between a broad class of MSE-based self-supervised objectives and supervised MSE as a parameter-independent constant and a trace interaction between the surrogate-target residual and the prediction error. The corresponding gradient discrepancy is determined by the gradient of this interaction. This formulation provides a common view of paired-noise, blind-spot, weak-noise, re-corruption, and sub-image methods, while revealing that a small global interaction may conceal substantial positive and negative regional interactions through spatial cancellation. Building on these observations, we propose LoTA-N2N, a two-stage zero-shot adaptation framework. Stage 1 trains a denoiser on complementary sub-image pairs and freezes it to construct detached clean-sub-image proxies. Stage 2 estimates the residual--prediction interaction using these proxies and suppresses its patch-wise absolute magnitude. We show that the local construction prevents spatial cancellation and upper-bounds the magnitude of the corresponding global interaction. Experiments across natural, confocal, and X-ray images, complemented by iteration-matched controls, controlled noise shifts, and gradient diagnostics, show consistent gains over MSE-only adaptation under IID, spatially varying, and mixed noise. Overall, LoTA-N2N demonstrates that estimated local interaction and spatial cancellation control provide effective design principles for single-image self-supervised denoising without paired clean targets, repeated acquisitions, or a predefined re-corruption model.

---


### 342. [BioSentinel at EXIST 2026: Soft-Label Optimization with XLM-RoBERTa for Sexism Intent Classification in Memes](https://arxiv.org/abs/2607.24137)

**<font color=#1a73e8>作者：</font>** Chandru Munisamy, Karthikeya Raguveer, Alapan Kuila  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the BioSentinel team's participation in EXIST 2026 Task 2.2: Source Intention in Memes, part of the CLEF 2026 evaluation campaign. The task requires classifying the communicative intent behind memes as direct, judgemental, or no (non-sexist), under a Learning with Disagreement (Le-Wi-Di) paradigm that mandates both hard-label and soft-label (probability distribution) predictions. We present a text-centric approach built on xlm-roberta-base (270M parameters) trained with a composite loss function combining KL divergence on soft annotator distributions and weighted cross-entropy on hard labels. On the official test set, the system achieved an ICM-Soft-Norm of 0.3229 and ICM-Norm of 0.3778, with a hard F1-score of 0.4236, ranking 40th (out of 118 submissions) in the soft-soft evaluation and 49th (out of 187 submissions) in the hard-hard evaluation. We provide an analysis of the dataset characteristics, exploratory larger-architecture runs, and the role of annotator disagreement in shaping model design for subjective NLP tasks. Ablation results show that KL loss improves soft-label metrics, while CE loss improves hard-label accuracy. We also report a separate validation-set temperature analysis.

---


### 343. [Image Inpainting via Stochastic Dynamics](https://arxiv.org/abs/2607.24140)

**<font color=#1a73e8>作者：</font>** Jiaqi Kuang, Zihao Guo, Zhongmin Qian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image inpainting aims to recover missing regions while preserving structural consistency. We propose a non-parametric method without network training based on data-guided stochastic dynamics. Starting from a masked image, the missing pixels are evolved through a reverse-time stochastic differential equation with a kernel-weighted correction estimated directly from a reference dataset. This empirical correction guides the reconstruction toward high-density regions of the data distribution without training a neural network or fitting a parametric density model. Experiments on MNIST, Fashion-MNIST, and MVTec show that the proposed method outperforms Mean Fill, Telea, and Navier-Stokes inpainting in PSNR, SSIM, and visual quality. On CelebA, it remains competitive and produces plausible completions for structure-sensitive occlusions. These results demonstrate the effectiveness of empirical reference statistics as a non-parametric prior for image inpainting.

---


### 344. [An Empirical Study of Feature Selection Granularity](https://arxiv.org/abs/2607.24145)

**<font color=#1a73e8>作者：</font>** Muhammad Rajabinasab, Arthur Zimek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature selection aims to identify the most informative and relevant features for a given dataset, either in terms of capturing the underlying data structure and distribution better, or with respect to the performance on a downstream task. Existing research in this area has largely focused on developing novel algorithms (in both supervised and unsupervised settings), proposing new evaluation metrics and frameworks, or benchmarking the performance of existing methods. In this work, we examine feature selection through an algorithmic design perspective. Conventional feature selection algorithms typically compute feature importance scores globally across the entire feature set and then select the top-ranked features in a single step. However, this approach raises a critical question: Can the presence of less informative (or noisy) features mask or obscure the true importance of other, more relevant features? In other words, would a recursive strategy, where features are removed one by one while re-evaluating importance at each step, yield different and potentially better results than the standard global ranking approach? To answer this question, we conduct an extensive empirical study using five diverse feature selection algorithms. We implement each algorithm under both the conventional global selection design and the greedy recursive elimination design. We then analyze the impact of this algorithmic choice, both individually for each method and collectively across all methods, on a range of standard feature selection evaluation metrics. The empirical evaluation results show that the greedy approach improves the overall feature selection quality almost consistently, albeit on the expense of higher computational cost, supporting our initial expectation that the curse of dimensionality also obscures the ways of mitigating it.

---


### 345. [A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference](https://arxiv.org/abs/2607.24148)

**<font color=#1a73e8>作者：</font>** Zhuoran Song, Haozhe Jiang, Chunyu Qi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have demonstrated strong potential for embodied AI, yet their high inference latency on GPUs limits real-time deployment. Existing accelerators, such as Dadu-Corki, improve efficiency but treat VLA models as full-precision workloads, leaving substantial redundancy in both memory and computation underexploited.
In this paper, we propose VQVLA, an algorithm-hardware co-design framework that accelerates VLA inference by exploiting weight similarity and execution dynamics. We first introduce MotionVQ, a motion-aware vector quantization scheme that dynamically adjusts quantization precision based on the robot's execution state, reducing memory access while preserving task success rate. We then propose a merged-centroid vectorized GEMM paradigm that operates on the codebook-index representation, eliminating redundant multiplications through spatial aggregation and temporal reuse of centroids. To realize these optimizations, we design an accelerator that efficiently supports dynamic precision selection and centroid-reuse computation. Experimental results show that VQVLA achieves 6.5x, 2.8x, 1.9x, 3.3x, and 4.3x speedup over the A100 GPU, Dadu-Corki, LUT-DLA, CodeGEMM, and ShiftAddLLM, respectively, with negligible accuracy degradation.

---


### 346. [Looking for Affect in Spontaneous Finnish Speech through Linguistic Interpretability](https://arxiv.org/abs/2607.24155)

**<font color=#1a73e8>作者：</font>** Kalle Lahtinen, Liisa Mustanoja, Okko Räsänen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing research on affect in speech has shown how acoustic surface characteristics and content-related linguistic aspects of speech both relate to perceived emotional arousal and valence. However, it is not clear what the relative contributions of these two factors are in the perceptual process. This is especially true for Finnish, for which most existing studies focus on either acoustic-phonetic or text analysis. This paper presents a study where we systematically explore the combinatory role of text- and audio-based features in modeling the human perception of valence and arousal using a newly released affective speech corpus for spontaneous Finnish. We show that the combination of text- and audio-based features improves valence regression results over the individual modalities, whereas for arousal regression the complementary effect is not substantial. The results support prior findings from other languages, providing new data and knowledge on spontaneous Finnish speech.

---


### 347. [Calibrated Tree-Neural Fusion for Fine-Grained Vegetation Community Classification](https://arxiv.org/abs/2607.24160)

**<font color=#1a73e8>作者：</font>** Dristi Datta, Md Khalid Hasan Sakib, Manoranjan Paul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate vegetation-community classification is essential for ecological monitoring, habitat assessment, and evidence-based environmental management in heterogeneous landscapes. Existing studies often rely on standalone tree ensembles or generic neural networks, although fine-grained ecological classes frequently exhibit overlapping spectral, topographic, and structural characteristics. Many frameworks also provide limited protection against stacking leakage, insufficient probability calibration, weak minority-class evaluation, and little evidence of stability across repeated data splits. To address these limitations, this study proposes Calibrated EcoTreeFuseNet-Plus, a tree-neural probability-fusion framework that combines out-of-fold tree probabilities, EcoFuseNet-V2 outputs, validation-selected meta-learning, and post-hoc temperature scaling. Raster values from six LiDAR-derived terrain and canopy variables and two hyperspectral vegetation indices were extracted at coordinate-based reference locations. Quality control removed 26 samples with missing elevation and one sample with non-finite NDWI, producing 1,833 complete records across 29 vegetation and non-vegetation classes. On the held-out test set, the proposed model achieved an accuracy of 0.8000, a macro F1-score of 0.7768, a balanced accuracy of 0.7903, and an MCC of 0.7903. Calibration reduced the expected calibration error from 0.3866 to 0.0651 without changing class predictions. Five-seed evaluation yielded a macro F1-score of 0.7717 +/- 0.0112, indicating stable performance across repeated splits. The results demonstrate a reliable discrimination-calibration trade-off for small-sample, fine-grained ecological classification.

---


### 348. [Do Current Retrievers Cover All the Evidence? A Controlled Study of Conjunctive Cross-Page Retrieval](https://arxiv.org/abs/2607.24165)

**<font color=#1a73e8>作者：</font>** Sungguk Cha, DongWook Kim, Mintae Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding a long document relevant to a multi-part request is not the same as establishing that it contains every requested piece of evidence. We study this gap for conjunctive document retrieval, where two or three explicit conditions must be supported on different pages of one document. We use n-Clue as a controlled measurement instrument: 1{,}000 queries over 2{,}021 documents pair all-condition golds with naturally occurring documents that satisfy only a subset, and a complete-first success requires a top-10 gold to precede every released subset qrel. Across 70 configurations, condition-wise decomposition improves two dense backbones by 6.8--7.3 points and lexical--visual fusion adds 8.7, while four generic rerankers all reduce Gold-NDCG; these directions replicate on a four-source stress set. Scaling one dense family from 0.6B to 8B changes complete-first success by 0.0 points. The strongest displayed hybrid illustrates the resulting gap: it finds a gold for 81.1\% of queries but succeeds complete-first on only 35.8\%, and the gap persists across condition count, target length, candidate density, query rendering, and the four-source stress set. Finally, page-aware visual systems surface stored support for every condition on only 5.1--5.3\% of queries. These results identify condition coverage, rather than gold discovery alone, as the central bottleneck.

---


### 349. [Falsifiable Commitment Planning for Self-Correcting Web Agents](https://arxiv.org/abs/2607.24167)

**<font color=#1a73e8>作者：</font>** Guangyi Liu, Huan Zhao, Quanming Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon web agents often go off track before final failure: a trajectory can remain locally plausible even after the current state, reused skill, or plan assumption no longer supports the user instruction. Existing agents can plan, reflect, or reuse experience, but their plans rarely specify the evidence under which an active step should still be trusted. We propose FCPAgent, a falsifiable commitment planning framework for robust long-horizon web agents. FCPAgent represents each plan step as a Falsifiable Commitment Unit (FCU): a subgoal grounded in a reusable skill, together with confirming evidence, falsifying evidence, and a confidence score. Execution is organized as a plan-test-repair loop. The hybrid commitment testing module checks candidate actions before they modify the browser and checks observations after execution; for efficiency, it combines lightweight evidence matching with LLM-based diagnostic verification. When evidence falsifies a commitment, scope-aware repair localizes the contradiction to the execution, skill, or planning level and revises the smallest adequate part. On WebArena, FCPAgent achieves a 13.8% relative improvement in average success over the strongest baseline, with especially large gains on long-horizon tasks.

---


### 350. [Forecasting the Emergence and Evolution of Crash Hotspots: A Unified Deep Learning Framework for Proactive Traffic Safety](https://arxiv.org/abs/2607.24168)

**<font color=#1a73e8>作者：</font>** Jingwen Zhu, Keshu Wu, Pei Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Road crashes remain among the gravest threats to public safety, and preventing them is a defining task of transportation systems worldwide. Much of that harm concentrates at hotspots, yet a hotspot is less a place than an episode; it emerges quietly at an intersection or along an arterial, intensifies for weeks, then subsides, only to reappear elsewhere. Enforcement guided by maps of past crashes inevitably trails this cycle, patrolling yesterday's hotspots while tomorrow's form unwatched. Breaking that lag requires three capabilities at once: detecting hotspots as they are born, forecasting where they will sit next week, and following each one through its life. We introduce HERALD (Hotspot Emergence, Risk Anticipation, and Life-cycle Dynamics), a unified deep learning framework that provides all three from a single statewide model. HERALD distills each county's recent crash history into weekly risk maps and forecasts the next with a CNN--Transformer, whose mixture-of-experts lets one model serve dense urban cores and sparse rural corridors alike. Each forecast is anchored in the county's long-run crash geography, sharpened by the self-exciting effect of recent crashes, and paired with explicit warnings of where new hotspots are about to appear. Followed over time, every hotspot acquires a legible life story, from birth through growth and stability to decline and death. Across six heterogeneous Wisconsin counties, HERALD forecasts more accurately than five identically trained baselines, locates hotspots most precisely, and flags emerging risks before they take hold. A single adjustable setting trades accuracy for extra sensitivity where deployment demands it. The result shifts hotspot management from mapping the past to anticipating the future.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-442](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
