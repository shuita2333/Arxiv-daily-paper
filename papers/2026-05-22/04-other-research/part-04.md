# 📦 其他研究 | 2026年05月22日

> 本类共 **352** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

---

### 151. [Decision-Path Patterns as Tree Reliability Signals: Path-based Adaptive Weighting for Random Forest Classification](https://arxiv.org/abs/2605.20716)

**<font color=#1a73e8>作者：</font>** Youngjoon Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random forests aggregate tree votes by simple majority, treating all trees as equally informative. We observe that the topological pattern along each tree's root-to-leaf decision path -- where and how often the dominant class label flips along it -- carries a signal of tree reliability that is exploitable for per-sample reweighting. The naive use of this signal is structurally confounded with the predicted class, so we propose a class-conditional ratio weighting that guarantees zero expected class bias by construction. On 30 binary classification benchmarks under a shared-forest, shared-split protocol with 30 repeats, the proposed method is the only one among four compared schemes -- RF, weighted RF, KNORA-Eliminate, KNORA-Union -- to yield a statistically significant accuracy improvement over RF (Wilcoxon p = 0.018), while the three alternatives all fail to do so (p > 0.5). It is also the only scheme without majority-recall regressions, with minority-recall regressions limited to 3/30 datasets -- a one-sided loss to which classical dynamic ensemble selection methods are susceptible. The gain is robust across forest sizes from 100 to 1000 trees.

---


### 152. [Robust Recommendation from Noisy Implicit Feedback: A GMM-Weighted Bayes-label Transition Matrix Framework](https://arxiv.org/abs/2605.20721)

**<font color=#1a73e8>作者：</font>** Zongyu Li, Xuanyu Liu, Gongce Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from implicit feedback in recommender systems is fundamentally challenged by pervasive label noise. While conventional denoising approaches often discard noisy instances to ensure robustness, this strategy inevitably suffers from low data utilization. Alternative methods that employ a Bayes-label transition matrix (BLTM) can leverage all available data, but their estimates tend to be biased in practical recommendation scenarios. To address these limitations, this paper proposes a Robust GMM-weighted Bayes-label Transition Matrix framework (RGBT). Our solution utilizes a Gaussian Mixture Model (GMM) to derive instance-specific reliability scores, which systematically calibrate the BLTM estimation to mitigate bias. Theoretical analysis confirms that our approach, by leveraging the BLTM framework with GMM calibration, simultaneously ensures full sample utilization, delivers consistent estimation, and critically, achieves a significant reduction in estimation variance. Extensive experiments on multiple real-world and synthetically flipped datasets demonstrate that RGBT not only utilizes noisy samples more effectively than mainstream reliable sample-based denoising methods, but also achieves significantly superior calibration capability of the transition matrix compared to state-of-the-art transition matrix-based denoising approaches.

---


### 153. [AGPO: Adaptive Group Policy Optimization with Dual Statistical Feedback](https://arxiv.org/abs/2605.20722)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Bokun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning improves LLM reasoning, but PPO/GRPO typically use fixed clipping and decoding temperature, which makes training brittle and tuning-heavy. We propose Adaptive Group Policy Optimization (AGPO), a critic-free refinement of GRPO that uses group-level statistics to control both update magnitude and exploration. AGPO uses a shared probe-derived statistical state to drive two controllers: (i) adaptive clipping, which sets the trust-region size from reward dispersion and skewness, probe vote entropy, policy entropy, and step-wise KL drift; and (ii) bidirectional adaptive temperature sampling, which heats or cools decoding around a base temperature according to centered uncertainty relative to a running baseline. On nine English and Chinese math/STEM benchmarks, Qwen2.5-14B trained with AGPO outperforms PPO/GRPO under the same generated-token budget, reaching 67.3% on GSM8K and 40.5% on MATH. Gains transfer to Llama-3-8B and Gemma-2-9B, and ablations confirm both modules are complementary. Our implementation is publicly available at this https URL.

---


### 154. [Memory-Efficient Partitioned DNN Inference on Resource-Constrained Android Crowds](https://arxiv.org/abs/2605.20723)

**<font color=#1a73e8>作者：</font>** Lakshani Manamperi, Disumi Pathirana, Thiwanka Pathirana 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying large deep neural networks on memory-constrained mobile devices is a central challenge in edge ML. While compression, pruning, and quantization reduce per-parameter cost, transformer-based models remain too large for the 3.3-7.4 GB RAM envelope of commodity Android handsets. We present the DNN pipeline scheduling subsystem of CROWDio, which achieves practical ONNX inference across resource-constrained Android workers without model modification, by distributing memory pressure across devices via five mechanisms: JIT deferred partition loading, a single-partition-resident constraint, a 4-tier affinity scheduler, a zlib-compressed tensor transport, and a streaming 1:1 dependency model. Evaluated on DistilBERT (Sanh et al., 2019) (approximately 67 M parameters, SST-2) across five Android handsets over ten runs, our system holds peak per-device RSS to 43+-2 MB and limits battery draw to 50+-3 mAh per run, while streaming concurrency cuts batch latency 34% below barrier synchronisation.

---


### 155. [Holistic Reliability Propagation: Decoupling Annotation and Prediction for Robust Noisy-Label](https://arxiv.org/abs/2605.20725)

**<font color=#1a73e8>作者：</font>** Jingyang Mao, Ningkang Peng, Yanhui Gu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning with noisy labels in multimedia classification often combines external annotations and model predictions into a single reliability weight, even though the two sources can fail for different reasons. We instead estimate disentangled reliabilities: bilevel meta-learning produces two batch-normalized scalars per sample, alpha for the given label and beta for the pseudo-label, without constraining them to sum to one. Holistic Reliability Propagation (HRP) then routes them to different objectives, using reliability-aware Mixup with global gating on the input branch and beta-gated pseudo-label positives on the contrastive branch. On synthetic and real-world benchmarks, HRP improves average accuracy over strong baselines and remains competitive at the highest noise rates.

---


### 156. [GAMR: Geometric-Aware Manifold Regularization with Virtual Outlier Synthesis for Learning with Noisy Labels](https://arxiv.org/abs/2605.20727)

**<font color=#1a73e8>作者：</font>** Ningkang Peng, Jingyang Mao, Xiaoqian Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) experience significant performance degradation when processing noisy labels, primarily due to overfitting on mislabeled data. Current mainstream approaches attempt to mitigate this issue by passively filtering clean samples during training. However, simple sample filtering within feature spaces degraded by noise struggles to distinguish between challenging samples and noisy samples, creating a bottleneck for model performance. We highlight for the first time the fundamental importance of actively reshaping feature space geometry for learning from noisy data. We propose a novel Geometry-aware Manifold Regularization Paradigm whose core idea is to explicitly construct energy barriers between data manifolds by actively synthesizing virtual outlier samples. By imposing geometric constraints that promote intra-class compactness and inter-class separation, this approach enhances the discriminability between hard and noisy samples, leading to the learning of more robust representations. Our regularization mechanism exhibits high universality, with effectiveness independent of any prior assumptions about noise patterns. It can be integrated as a standalone mechanism into existing sample selection frameworks, providing stronger robustness against diverse noisy environments. Experiments demonstrate that our paradigm achieves performance surpassing current state-of-the-art (SOTA) methods on multiple benchmarks, including CIFAR-10, with particularly pronounced advantages under more challenging asymmetric noise conditions. Furthermore, this paradigm significantly enhances the model's capability in Out-of-Distribution (OOD) detection, ensuring superior reliability and safety for deployment in open-world scenarios.

---


### 157. [Early High-Frequency Injection for Geometry-Sensitive OOD Detection](https://arxiv.org/abs/2605.20728)

**<font color=#1a73e8>作者：</font>** Chuanjie Cheng, Ningkang Peng, Chenxi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-hoc OOD detectors score logits or features after training, so their success depends on the geometry already encoded in the representation. We revisit this assumption through a band-wise MMD^2 analysis across CE, SimCLR, SupCon, and the OOD-oriented representation method PALM. In our diagnostic, low-frequency input bands induce weaker ID/OOD feature discrepancy, whereas higher-frequency bands tend to provide stronger separability. This observation motivates EIHF, an input-side intervention that exposes high-frequency evidence before the first convolution without changing the training objective. EIHF is strongest for geometry-sensitive OOD detection: under matched training and scoring settings, it reshapes class-conditional feature geometry and reduces ID/OOD Mahalanobis score overlap. Experiments on CIFAR-100 and ImageNet-100 show gains on CIFAR-100 and the best average FPR95 with second-best average AUROC on ImageNet-100, while also revealing a limitation on the scene-centric Places shift. Code is available at this https URL.

---


### 158. [TASTE: A Designer-Annotated Multi-Dimensional Preference Dataset for AI-Generated Graphic Design](https://arxiv.org/abs/2605.20731)

**<font color=#1a73e8>作者：</font>** Haonan Zhu, Elad Hirsch, Alexandria Minetti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models produce graphic design at production scale, but their supervision comes from photo-style preference data with a single overall verdict per comparison. Designers evaluate along several distinct axes, including typography, visual hierarchy, color harmony, layout, and brief fidelity, and a single label collapses them. We release TASTE (Typography, Aesthetics, Spatial, Tone, Etc.): ten professional designers ranked outputs from four current text-to-image models on nine criteria across two disjoint cohorts, yielding 1,600 ratings per criterion plus per-image hallucination flags on the holistic-preference cohorts. We pair the dataset with three contributions. First, a criterion-agnostic signal test framework, using Kendall's tau, majority probability, and Condorcet cycles against exact iid-uniform nulls at p = 4 and R = 5, places designer agreement on graphic design between food and movie preferences and photo-style image quality, with every TASTE criterion rejecting the random-rater null. Second, no pre-trained system in our benchmark, including six open-weight VLM judges from 3B to 33B parameters and three dedicated T2I scorers, HPSv2.1, PickScore-v1, and LAION-Aesthetic-V2, exceeds 0.55 macro agreement with the 5-designer majority; VLM judges trade off position bias against content sensitivity, so scaling moves along this frontier without improving accuracy. Third, a small pairwise-difference head trained on TASTE reaches 0.611, closing roughly half the gap to the 0.741 single-rater ceiling.

---


### 159. [Deep Attention Reweighting: Post-Hoc Attention-Based Feature Aggregation in CNNs for Disentangling Core and Spurious Features under Spurious Correlations](https://arxiv.org/abs/2605.20732)

**<font color=#1a73e8>作者：</font>** Kin Whye Chew, Jingxian Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional Neural Networks (CNNs) often exploit spurious correlations in datasets, learning superficially predictive yet causally irrelevant features, leading to poor generalization and fairness issues. Deep Feature Reweighting (DFR) is a post-hoc technique that reduces a trained model's reliance on spurious correlations by retraining its classification head on a target dataset. However, we show that DFR is fundamentally constrained by operating on entangled features, limiting its ability to amplify the core features while simultaneously suppressing the spurious ones. We trace this entanglement to the ubiquitous Global Average Pooling (GAP) layer, which indiscriminately collapses spatially distinct core and spurious features into a single representation. To address this, we propose Deep Attention Reweighting (DAR), a post-hoc attention-based aggregation module that replaces GAP and is retrained jointly with the classification head. DAR computes an adaptive weighting of spatial locations across feature maps, enabling selective suppression of spurious features before the collapse into entangled features. Across various datasets, metrics, and ablations, DAR consistently outperforms DFR, demonstrating that our attention-based aggregation mitigates GAP-induced entanglement and reduces spurious reliance.

---


### 160. [Sketch2MinSurf: Vision-Language Guided Generation of Editable Minimal Surfaces from Hand-Drawn Sketches](https://arxiv.org/abs/2605.20733)

**<font color=#1a73e8>作者：</font>** Wenda Wang, Anqi Liu, Junqi Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Converting hand-drawn sketches into structured 3D geometries remains challenging due to the difficulty of representing non-Euclidean surfaces and maintaining topological consistency. Existing generative models such as GANs, NeRFs, and diffusion architectures often fail to produce editable manifolds directly usable in downstream design workflows. We present Sketch2MinSurf, a hybrid vision-language and geometric optimization framework that integrates vision-language guidance with minimal-surface theory to generate smooth and editable 3D surfaces from hand-drawn sketches. The core of our approach is a spatial-topological encoding that represents geometry as tuples of node coordinates and real/virtual edge skeletons, enabling stable topological control during generation. We further introduce the Sketch2MinSurf Structural Loss (S2MS-Loss), a reward-modulated objective that jointly constrains geometric reconstruction and topological coherence. On a test set of 100 sketches, Sketch2MinSurf achieves a topological similarity score of 0.844, outperforming existing sketch-to-shape baselines. The generated manifolds are directly editable and free from non-manifold artifacts. A public art installation at a university showcases the method's potential for human-intent-driven 3D form generation. The dataset and code are available at this https URL.

---


### 161. [Lowering the Barrier to IREX Participation: Open-Source Algorithms, Toolkit, and Benchmarking for Iris Recognition](https://arxiv.org/abs/2605.20735)

**<font color=#1a73e8>作者：</font>** Siamul Karim Khan, Patrick J. Flynn, Adam Czajka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes two new open-source iris recognition algorithms, providing both Python and IREX-compliant C++ implementations to be submitted to the official IREX X program. This work has two primary goals: (a) to conduct the first-ever assessment of open-source iris recognition solutions according to IREX testing protocols, and (b) to offer a model C++ submission that significantly facilitates the entry of other teams' open-source methods into the IREX evaluation. The new methods consist of two Neural Networks trained with: (i) Triplet loss with Batch-Hard Triplet mining (TripletIris), and (ii) ArcFace loss (ArcIris). The paper also provides open-source IREX-compliant C++ implementations of two existing methods: (a) an iris image filtering-based algorithm utilizing human saliency-driven kernels (HDBIF), and (b) a human-interpretable algorithm for detecting and comparing Fuchs' crypts (CRYPTS). Except for CRYPTS, which faced timing constraints during 1:N search, these methods have undergone the official IREX X evaluation and have also been assessed using several popular academic benchmarks: Quality-Face/Iris Research Ensemble, Warsaw-Biobase Post-Mortem Iris, CASIA-Iris-Thousand-V4, CASIA-Iris-Lamp-V4, IIT Delhi Iris Database, IIITD Contact Lens Iris Database, NDIris3D, and Notre Dame Variable Iris Image Quality Release 2. Finally, this paper also provides open-source models for iris segmentation and circle estimation that can be incorporated into any new iris recognition method.

---


### 162. [Resolving Long-Tail Ambiguity in Unsupervised 3D Point Cloud Segmentation with Language Priors](https://arxiv.org/abs/2605.20737)

**<font color=#1a73e8>作者：</font>** Siqi Wei, Hongbin Xu, Feng Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing approaches for unsupervised 3D point cloud segmentation predominantly rely on a purely visual similarity-based learning-by-clustering paradigm, which suffers from a fundamental limitation: long-tail ambiguity. In such a paradigm, features of minor classes are consistently absorbed by dominant clusters, leading to severely imbalanced predictions. To address this issue, we propose LangTail, a language-guided hierarchical learning framework that leverages the balanced world knowledge encoded in language models to mitigate long-tail ambiguity in unsupervised 3D segmentation. The key idea is to establish multi-level associations between language-derived semantic priors and visually underrepresented minor classes, thereby compensating for the biased attention of purely visual clustering toward dominant classes. Specifically, LangTail first constructs an entity-level semantic prior from language models, capturing balanced and fine-grained world knowledge across categories. These priors are injected into a hierarchical clustering framework via contrastive alignment. This guides multi-granularity semantic structure formation and prevents minor classes from being absorbed by dominant clusters, yielding more discriminative representations for underrepresented categories. Extensive experiments on ScanNet-v2, S3DIS, and nuScenes demonstrate that LangTail consistently outperforms existing methods by significant margins, \ie, +13.5, +12.9, and +8.9 mIoU, respectively. These results demonstrate the effectiveness of language priors in improving the representation of minority classes in 3D point clouds. The code will be released at: this https URL.

---


### 163. [VBFDD-Agent for Electric Vehicle Battery Fault Detection and Diagnosis: Descriptive Text Modeling of Battery Digital Signals](https://arxiv.org/abs/2605.20742)

**<font color=#1a73e8>作者：</font>** Joey Chan, Zhen Chen, Ershun Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid proliferation of electric vehicles, the safety and reliability of lithium-ion batteries have become critical concerns. Effective anomaly detection is essential for ensuring safe battery operation. However, as battery systems and operating scenarios become increasingly complex, battery fault diagnosis and maintenance require stronger cross-domain adaptability and human-AI collaboration. Traditional fault detection and diagnosis methods are usually designed for specific scenarios and predefined workflows, making them less effective in complex real-world applications.
To address the scarcity of open-source battery fault report corpora and the lack of unified maintenance knowledge representation, this study proposes a descriptive text modeling approach for battery signal reports. Monitoring signals, statistical features, anomaly records, and state assessment results are transformed into structured and readable natural language descriptions, forming a language corpus for battery health diagnosis and maintenance.
Based on this corpus, we propose VBFDD-Agent, a vehicle battery fault detection and diagnosis agent for automotive-grade battery systems. VBFDD-Agent integrates descriptive battery-state texts, historical case retrieval, local maintenance manuals, and large language model reasoning to generate structured diagnostic results and maintenance recommendations. Experiments show that the proposed framework can accurately perform anomaly monitoring based on descriptive textual representations and provide flexible, efficient, and actionable maintenance suggestions. Expert evaluation further confirms the practical value of the generated recommendations. Overall, VBFDD-Agent extends traditional battery diagnosis from label prediction to interpretable and maintenance-oriented decision support.

---


### 164. [Draw2Think: Harnessing Geometry Reasoning through Constraint Engine Interaction](https://arxiv.org/abs/2605.20743)

**<font color=#1a73e8>作者：</font>** Juncheng Hu, Jiawei Du, Xin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models solve geometry problems with rising accuracy, yet their intermediate states remain latent and unverifiable: a relation expressed in textual reasoning or drawing code carries no guarantee that a constraint-satisfying configuration realizes it. We observe that existing externalization methods based on rendered pixels or one-shot scripts fail to provide exact, per-action geometric guarantees. Enforcing geometric relations by algebraic definition closes this gap: the workspace becomes a constraint-checked evolving canvas. We present Draw2Think, a framework that recasts geometric reasoning from latent spatial inference into agentic interaction with the GeoGebra constraint engine. In a Propose-Draw-Verify loop, Draw2Think externalizes hypotheses onto an executable canvas, measures exact geometric quantities, and feeds structured observations back to the model, so subsequent reasoning proceeds from checked canvas state grounded by the shared workspace. This externalization makes two properties separately auditable: model-level Construction Fidelity (whether the canvas realizes the intended configuration) and engine-level Measurement Faithfulness (exact values and relations from canvas constraints). Across construction, outcome, and rendering evaluations, Draw2Think builds canvases that pass 95.9% predicate-level and 84.0% strict problem-level construction checks on GeoGoal, improves outcome accuracy by up to 4.1%/16.4% on planar/solid benchmarks, and attains 68.2%/90.5% strict/relaxed rendering scores on GenExam-math. Project page is available at this https URL

---


### 165. [Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale](https://arxiv.org/abs/2605.20744)

**<font color=#1a73e8>作者：</font>** Amit Roth, Ankur Samanta, Matan Halevy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning autonomous agents with human intent remains a central challenge in modern AI. A key manifestation of this challenge is reward hacking, whereby agents appear successful under the evaluation signal while violating the intended objective. Reward hacking has been observed across a wide range of settings, yet methods for reliably measuring it at scale remain lacking. In this work, we introduce a new evaluation paradigm for measuring reward hacking. Whereas prior studies have primarily analyzed it post hoc by inspecting agent trajectories, we instead embed detectable reward hacking opportunities directly into environments. This makes their exploitation verifiable by design, enabling deterministic and automated measurement of whether and how agents exploit such vulnerabilities. We instantiate this approach in $\textit{TextArena}$ and release $\textit{Hack-Verifiable TextArena}$, a testbed in which reward hacking can be measured reliably. Using this benchmark, we analyze reward hacking behavior across language models in diverse environments and settings. We open source the code at this https URL.

---


### 166. [The Hidden Signal of Verifier Strictness: Controlling and Improving Step-Wise Verification via Selective Latent Steering](https://arxiv.org/abs/2605.20745)

**<font color=#1a73e8>作者：</font>** Yefan Zhou, Yilun Zhou, Austin Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative verifiers have emerged as a promising paradigm for step-wise verification, but their verification behavior is often poorly calibrated: they may be under-critical and miss erroneous steps, or over-critical and reject correct reasoning. We refer to this tendency to be overly lenient or overly critical as verifier strictness. In this work, we study whether verifier strictness can be controlled through hidden-state intervention. We uncover a verification-specific hidden-state signal: in step-wise verification, a verifier's tendency to accept or reject a solution step is encoded near the boundary of the corresponding verification paragraph. Exploiting this signal, we show that hidden-state steering can directly modulate verifier strictness without fine-tuning. However, uniform steering induces a trade-off between error detection and correctness certification. To address this, we propose VerifySteer, which exploits latent correctness signals for sample-level routing and selectively intervenes on paragraph boundaries. Experiments on ProcessBench and Hard2Verify show that VerifySteer outperforms prompt optimization and activation steering baselines, and is competitive with self-consistency while requiring 4-7x less inference compute. VerifySteer is also complementary to verification fine-tuning, providing further gains on top of fine-tuned verifiers. The code is available at this https URL.

---


### 167. [The Devil is in the Condition Numbers: Why is GLU Better than non-GLU Structure?](https://arxiv.org/abs/2605.20749)

**<font color=#1a73e8>作者：</font>** Xingyu Lyu, Qianqian Xu, Zhiyong Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gated Linear Units (GLU) and their variants are widely adopted in modern open-source large language model architectures and consistently outperform their non-gated counterparts, yet the underlying reasons for this advantage remain unclear. In this work, we study GLU by analyzing two-layer networks in the neural tangent kernel (NTK) regime. Our analysis reveals that the GLU structure reshapes the NTK spectrum, leading to a smaller condition number and a more compact eigenvalue distribution. Building on this finding, we further analyze the resulting training dynamics and show how the reshaped spectrum leads to faster convergence of GLU models, including a characteristic loss-crossing phenomenon observed between GLU and non-GLU models. Finally, we empirically observe that GLU has limited impact in reducing the generalization gap on various models, including ViT and GPT-2, suggesting that its primary benefit lies in accelerating optimization rather than reducing the generalization gap.

---


### 168. [PACD-Net: Pseudo-Augmented Contrastive Distillation for Glycemic Control Estimation from SMBG](https://arxiv.org/abs/2605.20751)

**<font color=#1a73e8>作者：</font>** Canyu Lei, David Repaske, Jianxin Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective diabetes management requires continuous monitoring of glycemic levels. Clinically, glycemic control is assessed using metrics such as Time in Range (TIR), Time Below Range (TBR), and Time Above Range (TAR), typically derived from continuous glucose monitoring (CGM). However, many patients rely on self-monitoring of blood glucose (SMBG) due to the high cost and limited accessibility of CGM. Unlike CGM, SMBG provides sparse and irregular measurements, making accurate estimation of these metrics challenging. Conventional supervised learning approaches struggle under such sparsity, leading to poor generalization and unstable performance. To address this, we propose PACD-Net, a self-supervised contrastive knowledge distillation framework for estimating glycemic control from SMBG. Pseudo-SMBG samples with richer temporal coverage are used as teacher signals to guide learning from sparse observations. In addition, multi-view contrastive learning enforces representation consistency across diverse sampling patterns. The model adopts a hybrid Swin Transformer-CNN backbone to capture temporal dependencies in sparse SMBG sequences. Experimental results demonstrate that PACD-Net consistently outperforms existing methods in estimating TAR, TIR, and TBR from real-world SMBG data, achieving improved accuracy as well as enhanced stability and generalization under extremely sparse observation settings. The proposed framework provides a practical tool for clinical SMBG interpretation and offers a generalizable approach for learning from sparse and irregularly sampled sensor data in broader applications.

---


### 169. [Conflict-Aware Additive Guidance for Flow Models under Compositional Rewards](https://arxiv.org/abs/2605.20758)

**<font color=#1a73e8>作者：</font>** Xuehui Yu, Fucheng Cai, Meiyi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference-time guided sampling steers state-of-the-art diffusion and flow models without fine-tuning by interpreting the generation process as a controllable trajectory. This provides a simple and flexible way to inject external constraints (e.g., cost functions or pre-trained verifiers) for controlled generation. However, existing methods often fail when composing multiple constraints simultaneously, which leads to deviations from the true data manifold. In this work, we identify root causes of this off-manifold drift and find that the approximation error scales severely with gradient misalignment. Building on these findings, we propose Conflict-Aware Additive Guidance ($g^\text{car}$), a lightweight and learnable method, which actively rectifies off-manifold drift by dynamically detecting and resolving gradient conflicts. We validate $g^\text{car}$ across diverse domains, ranging from synthetic datasets and image editing to generative decision-making for planning and control. Our results demonstrate that $g^\text{car}$ effectively rectifies off-manifold drift, surpassing baselines in generation fidelity while using light compute. Code is available at this https URL.

---


### 170. [SpineContextResUNet: A Computationally Efficient Residual UNet for Spine CT Segmentation](https://arxiv.org/abs/2605.20760)

**<font color=#1a73e8>作者：</font>** K S Nithurshen, Saurabh J. Shigwan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated segmentation of the vertebral column in Computed Tomography (CT) scans is a prerequisite for pathological assessment and surgical planning. However, state-of-the-art methods, particularly those based on Transformers or large-scale ensembles, demand substantial GPU resources, creating a barrier for clinical adoption in resource-constrained environments or on edge devices. To address this, we introduce SpineContextResUNet, a computationally efficient 3D Residual U-Net designed for rapid spinal localization. Our architecture integrates a lightweight Context Block that employs parallel multi-dilated convolutions to capture long-range anatomical dependencies without the high latency of Recurrent Neural Networks (RNNs) or the memory overhead of Self-Attention mechanisms. Extensive validation on two public benchmarks, VerSe2020 and CTSpine1K, demonstrates that our model achieves a Dice score of 88.17% and 88.13% respectively. To evaluate performance under strict hardware constraints, we compared our model against a bottlenecked SwinUNETR scaled to match our ~1.7M hardware footprint. While the constrained Transformer suffers severe performance degradation due to a lack of spatial inductive biases in a limited-data regime, our CNN-based approach successfully maintains high accuracy. Crucially, heavy baselines like TotalSegmentator fail due to memory exhaustion on commodity hardware (Intel Core i5, 8GB RAM), our model performs robust inference, making it a viable solution for point-of-care diagnostics and deployment on edge platforms like the Nvidia Jetson Orin Nano.

---


### 171. [ShapeBench: A Scalable Benchmark and Diagnostic Suite for Standardized Evaluation in Aerodynamic Shape Optimization](https://arxiv.org/abs/2605.20763)

**<font color=#1a73e8>作者：</font>** Shaghayegh Fazliani, Krissh Chawla, Jack Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid progress in aerodynamic shape optimization (ASO) has outpaced currently-available standardized evaluation frameworks. Fair comparison requires a unified benchmark spanning diverse shape classes, objective formulations, and matched-budget state-of-the-art baselines. We introduce ShapeBench, an open-source ASO benchmark with a unified API spanning 103 tasks across eight shape categories and multiple optimization regimes. Each ShapeBench task includes a validated surrogate for fast search; when feasible, a high-fidelity Computational Fluid Dynamics (CFD) pipeline for final verification is available, enabling systematic fidelity-gap analysis. ShapeBench provides a reproducible protocol with well-configured baselines to compare fairly using a consistent budget metric, allowing for comparison among both classical and LLM-driven methods, including general-purpose optimizers and a new domain-specialized evolutionary LLM baseline, ShapeEvolve. Results on ShapeBench demonstrate substantial variance in optimizer rankings across shape categories and problem formulations, with mean pairwise Spearman $\rho = 0.013$, so single-task conclusions do not reliably generalize across problem classes. The benchmark is also far from saturation; classical methods are rarely applicable across all shape categories and tasks, further highlighting the need for more general-purpose approaches.

---


### 172. [Diffuse to Detect: Bi-Level Sample Rebalancing with Pseudo-Label Diffusion for Point-Supervised Infrared Small-Target Detection](https://arxiv.org/abs/2605.20766)

**<font color=#1a73e8>作者：</font>** Zhu Liu, Yuanhang Yao, Ping Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point supervision has become a scalable solution to address dense annotation for infrared small target detection, but its performance is limited by two coupled bottlenecks: unstable pseudo-label evolution in cluttered, low-contrast infrared imagery and severe sample-distribution imbalance. In this paper, we present a more adaptive and stable framework to address these issues. Leveraging the intrinsic consistency between thermal radiation patterns and heat diffusion, we propose a physics-induced annotation strategy that expands single-point labels into reliable pseudo-masks. To further enhance supervision and alleviate sample imbalance, we develop a bi-level dual-update framework that jointly optimizes detector weights, sample weights, and diffusion parameters. A meta-classifier dynamically predicts sample-wise loss weights, while a differentiable diffusion module refines pseudo-labels with detection feedback, enabling adaptive interaction between training and hyperparameter optimization. Extensive experiments across multiple datasets demonstrate five-fold annotation acceleration, superior detection accuracy, and comparable performance with 30% of the training data, validating the efficiency and practicality of our approach. Our code is available at this https URL.

---


### 173. [Cumulative Meta-Learning from Active Learning Queries for Robustness to Spurious Correlations](https://arxiv.org/abs/2605.20771)

**<font color=#1a73e8>作者：</font>** Kin Whye Chew, Jingxian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spurious correlations in real-world datasets cause machine learning models to rely on irrelevant patterns, undermining reliability, generalization, and fairness. Active learning offers a promising way to address this failure mode by querying informative samples that distinguish core features from spurious ones. However, standard active-learning methods simply append queried examples to the labeled set, effectively updating only the likelihood term. In deep learning regimes, the influence of these informative samples can be diluted by the larger labeled set and memorized by overparameterized models. We propose Cumulative Active Meta-Learning (CAML), an active-learning framework that uses queried examples to meta-learn the prior, or inductive bias, governing how the model adapts. CAML casts each active-learning round as a meta-learning task: the current labeled set serves as meta-train data for adaptation, while the newly queried batch serves as meta-test data for evaluating generalization. Unlike conventional meta-learning, which treats tasks as independent and identically distributed, CAML exploits the sequential dependence between active-learning rounds by maintaining a cumulative inductive bias that is progressively refined. Theoretically, we show that this cumulative formulation introduces interaction terms that couple earlier meta-learned inductive biases with later query-induced objectives, capturing dependencies absent from standard meta-learning. Empirically, CAML improves minority-group accuracy across spurious-correlation benchmarks and acquisition strategies, with gains of up to 27.8% on Dominoes, 29.9% on Waterbirds, 14.3% on SpuCo, and 24.0% on CivilComments.

---


### 174. [AttriStory: Fine-grained Attribute Realization for Visual Storytelling with Diffusion Models](https://arxiv.org/abs/2605.20777)

**<font color=#1a73e8>作者：</font>** Manogna Sreenivas, Rohit Kumar, Soma Biswas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual storytelling with diffusion models has made impressive strides in maintaining character consistency across narrative scenes. However, a critical gap remains: while these methods ensure a character remains consistent across scenes, they provide no systematic method to ensure if fine-grained attributes such as color and textures of clothing, accessories are faithfully rendered in the generated images. Towards this goal, we introduce AttriStory, a benchmark enabling attribute realization in visual storytelling. We curate 200 multi-scene stories across 10 distinct artistic styles using Large Language Model. Each scene is constructed with detailed attribute specifications to enable rich visual narratives. Further, to address attribute realization, we propose a plug-and-play latent optimization module that operates during early denoising steps, when the model establishes structural and semantic content. We achieve this through AttriLoss objective designed to maximize alignment between the cross-attention maps for desired attribute-object pairs while suppressing spurious associations, guiding models to localize attributes correctly. This approach operates orthogonally to existing consistency mechanisms, integrating seamlessly with current story generation pipelines without requiring architectural modifications. Our experiments demonstrate consistent improvements on incorporating AttriLoss across all baselines. This work positions attribute realization as a distinct, complementary dimension of visual storytelling, alongside character consistency, advancing the field toward fine-grained attribute-controlled story generation. Project-page:this https URL

---


### 175. [Causal Machine Learning Is Not a Panacea: A Roadmap for Observational Causal Inference in Health](https://arxiv.org/abs/2605.20782)

**<font color=#1a73e8>作者：</font>** Donna Tjandra, Trenton Chang, Sonali Parbhoo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: The growing availability of large-scale observational clinical datasets and challenges in conducting randomized controlled trials have spurred enthusiasm in using causal machine learning (ML) for causal inference in observational data. We present a roadmap for applying causal ML to observational data. Materials and methods: We outline the importance of assessing validity assumptions within available data and applying causal ML responsibly for clinical experts using causal ML and ML practitioners with limited clinical expertise. Observations: Despite advances in causal ML, its limitations remain largely under-appreciated across disciplines. This gap in shared knowledge may impact the validity of findings. Discussion: Causal assumptions must be satisfied and modeling choices justified. Otherwise, these approaches risk producing biased or misleading results, with consequences for clinical research and patient care. Conclusion: Causal ML can be a powerful tool for generating causal hypotheses. We provide a template to strengthen the rigor and interpretability of causal analyses.

---


### 176. [Interaction Locality in Hierarchical Recursive Reasoning](https://arxiv.org/abs/2605.20784)

**<font color=#1a73e8>作者：</font>** Yosuke Miyanishi, Tetsuro Morimura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning requires both location-bound computation and location-invariant structure: agents must make local moves while preserving route, object, or constraint-level plans. We propose interaction locality, a task-geometry-aware framework for measuring whether information flow stays within nearby cells or semantic segments, or crosses them. We instantiate the framework with sparse-autoencoder feature ablations and finite-noise activation patching, with structural Jacobian and attention checks reported in the appendix, and apply it to HRM and TRM, two compact hierarchical and recursive reasoning models, on Maze-Hard, Sudoku Extreme, and ARC-AGI. Across these models, activation patching gives the clearest architectural fingerprint: high-level recurrent states tend to write information within nearby cells or same-segment units, while repeated recursive updates accumulate these local writes into broader solution structure. This pattern holds across maze paths, Sudoku constraints, and ARC-AGI object neighborhoods, with the strongest concentration in TRM. To test whether interaction locality extends beyond toy-yet-challenging grid benchmarks, we also apply it to MTU3D, a large-scale embodied 3D scene-grounding model. In this MTU3D setting, causal spatial locality appears primarily at the transition where visual scene features are handed to the downstream grounding module, rather than uniformly throughout the visual encoder. This contrast suggests that the local-to-global handoff observed in HRM and TRM is tied to explicit recursive reasoning dynamics, while embodied 3D models may concentrate causal spatial structure at module boundaries. Interaction locality turns the intuitive local-execution/global-planning story into a reproducible measurement framework for recursive and embodied spatial reasoning.

---


### 177. [Building Arabic NLP from the Ground Up: Twenty Years of Lessons, Failures, and Open Problems](https://arxiv.org/abs/2605.20786)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper reflects on twenty years of building NLP resources and research infrastructure for Arabic, a language spoken by hundreds of millions yet historically underserved relative to languages such as English or Chinese. The first decade focused on foundational linguistic infrastructure; the second shifted toward computational social science, social media analysis, and socially oriented applications. Rather than cataloguing outputs, the paper examines what the experience of building them revealed. Three counterintuitive lessons emerge: building datasets is as much a social process as a technical one; communities formed around shared tasks often matter more than the tasks themselves; and moving from language resources to computational social science exposes challenges that traditional NLP training does not address. We discuss three failures: a depression detection corpus that never reached clinical practice, a period of spreading across too many shared tasks without sufficient depth, and a long-standing assumption that Modern Standard Arabic infrastructure would transfer cleanly to dialectal tasks. These experiences suggest that the hardest problems in developing NLP for underserved communities are not linguistic but social, institutional, and epistemic, and require competencies the field rarely teaches.

---


### 178. [Findings of the Counter Turing Test: AI-Generated Image Detection](https://arxiv.org/abs/2605.20787)

**<font color=#1a73e8>作者：</font>** Rajarshi Roy, Nasrin Imanpour, Ashhar Aziz 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancements in generative AI technologies, such as Stable Diffusion, DALL-E, and Midjourney, have significantly transformed the creation of synthetic visual content. While these models enable innovation across industries, they also pose serious challenges, including misinformation, disinformation, and biased content generation. The increasing realism of AI-generated images makes their detection a pressing concern for researchers, policymakers, and industry stakeholders.
In this paper, we present the findings of the Defactify 4.0 workshop, which introduced the Counter Turing Test (CT2) for AI-Generated Image Detection. The competition consisted of two key tasks: (1) binary classification of images as either AI-generated or real and (2) identification of the specific generative model responsible for an AI-generated image. To facilitate this, we developed the MS COCOAI dataset, consisting of 50,000 synthetic images from multiple generative models alongside real-world images from the MS COCO dataset.
Participants employed diverse detection strategies, including convolutional neural networks (CNNs), Vision Transformers (ViTs), frequency-based analysis, contrastive learning, and multimodal techniques. The results demonstrated that while AI-generated images can be detected with high accuracy (F1-score > 0.83), identifying the exact model used remains significantly more challenging (highest F1-score: 0.4986). These findings highlight the need for improved model fingerprinting, adversarial robustness, and real-time detection mechanisms.

---


### 179. [Beyond Numerical Features: CNN-Driven Algorithm Selection via Contour Plots for Continuous Black-Box Optimization](https://arxiv.org/abs/2605.20797)

**<font color=#1a73e8>作者：</font>** Yiliang Yuan, Xiang Shi, Mustafa Misir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The present paper introduces a new representation-driven approach to per-instance algorithm selection, applied to black-box optimization, for automatically choosing the most promising solver from a fixed portfolio. Prior work in continuous optimization largely relies on numerical descriptors, including Exploratory Landscape Analysis features and learned embeddings such as Deep-ELA. This work studies a complementary representation: contour-map visualizations of probed landscapes. A CNN regressor takes multiple instance-specific contour views (stacked or encoded per view and aggregated) and predicts per-solver performance, enabling selection by the predicted best value. On the standard BBOB 2009 single-objective protocol, the resulting selectors significantly outperform the single best solver (SBS) and are competitive with feature-based baselines. A subsequent bi-objective evaluation under the DeepELA setting further indicates that the same image-based principle can be competitive when using windowed contour views. Overall, the results suggest that simple vision models can exploit spatial structure in probed landscapes for algorithm selection without handcrafted ELA features.

---


### 180. [Most Transformer Modifications Still Do Not Transfer at 1-3B: A 2020-2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor](https://arxiv.org/abs/2605.20798)

**<font color=#1a73e8>作者：</font>** Yang Zhao, Jiahao Lu, Bin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Narang et al. (2021) evaluated 40+ Transformer modifications at T5-base scale and concluded that most did not transfer. Five years later, the typical working regime has moved to 1-3B parameters, downstream evaluation has replaced pretraining perplexity, and a substantially different catalogue of modifications has emerged. We revisit their question by testing 20 post-2021 Transformer modifications at 1.2B and 3B under strict iso-data, iso-compute, iso-recipe control, with a multi-seed baseline noise floor and CLIMB-12 downstream evaluation as the primary metric. The central finding reproduces theirs at this curated set: most modifications do not transfer. Of the 20 modifications, only two clear Bonferroni correction at 1.2B; one of those two further fails to train stably at 3B under the shared recipe. We also find that the loss-downstream gap reported by Tay et al. (2023) enlarges several-fold for attention-output modifications: two significant failures converge to within 2-3% of baseline validation loss yet drop 6-16 CLIMB-points. We conclude that noise-floor reporting, downstream evaluation, and cross-scale stability testing are now prerequisites for architecture comparisons at 1-3B.

---


### 181. [Tunable MAGMAX: Preference-Aware Model Merging for Continual Learning](https://arxiv.org/abs/2605.20803)

**<font color=#1a73e8>作者：</font>** Kei Hiroshima, Kento Uchida, Shinichi Shirakawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) aims to train models sequentially on multiple tasks while mitigating catastrophic forgetting of previously learned knowledge. Recent advances in large pre-trained models (LPMs) and model merging techniques, such as MAGMAX, have demonstrated effective CL performance by combining task-specific parameters. However, existing methods primarily focus on average performance across all tasks and do not adequately address how to construct models accommodating different deployment environments or varying user preferences. This paper proposes a model merging framework, termed Tunable MAGMAX, which enables preference-aware control of task-specific performance in CL. Our method introduces a preference vector that controls the number of elements selected from each task vector during model merging, allowing us to adjust the merged model performance according to their deployment needs. We further propose a method for automatically constructing appropriate preference vectors by leveraging small amounts of target environment data and datasets from model training tasks, thereby eliminating the need for manual specification. The experimental result on CL benchmark tasks demonstrates that Tunable MAGMAX effectively controls task-wise performance and successfully adapts merged models to various target environments. The proposed Tunable MAGMAX achieves superior or comparable performance to baseline methods, making it a practical solution for deploying CL models to various environments where the preferences of each task performance differ.

---


### 182. [Decomposing Subject-Driven Image Generation via Intermediate Structural Prediction](https://arxiv.org/abs/2605.20807)

**<font color=#1a73e8>作者：</font>** Hanzhong Guo, Yizhou Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject-driven text-to-image generation still struggles to preserve high-frequency identity details such as logos, patterns, and text. Existing methods typically operate directly in RGB space, which often leads to detail degradation under substantial edits. We propose a two-stage framework that decouples structure from appearance by first predicting a Canny map and then rendering the final image conditioned on both the source appearance and the predicted structure. To improve text handling, we further introduce a fully automatic pipeline that constructs a 100k-pair text-aware dataset with cross-view textual consistency. Experiments, including GPT-4.1-based evaluation and a knowledge distillation study, show clear gains over selected baselines and suggest that intermediate structural prediction is an effective route for high-fidelity subject-driven generation. Our dataset and code will be made publicly available.

---


### 183. [AIR: Amortized Image Reconstruction Framework for Self-Supervised Feed-Forward 2D Gaussian Splatting](https://arxiv.org/abs/2605.20820)

**<font color=#1a73e8>作者：</font>** Zhaojie Zeng, Yuesong Wang, Yawei Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 2D Gaussian splatting provides an efficient explicit representation for image reconstruction, but existing methods still require costly per-image iterative optimization or rely on handcrafted priors for primitive allocation. We present AIR, a self-supervised feed-forward framework that amortizes iterative Gaussian fitting into a single network pass, eliminating per-image test-time optimization. AIR adopts a stage-wise residual architecture that progressively predicts additional Gaussian primitives from reconstruction residuals, together with an explicit Stage Control mechanism that activates new primitives only in under-reconstructed regions. A Predict--Optimize--Distill training strategy stabilizes multi-stage prediction by distilling short-horizon optimized Gaussian increments back into the predictor. The stabilized predictor is then jointly finetuned across stages and equipped with an image-adaptive quantizer for compact Gaussian storage. Experiments on Kodak and DIV2K show that AIR achieves better reconstruction quality than representative Gaussian-based baselines while reducing encoding time to 160--300\,ms. Code: this https URL

---


### 184. [VSCD: Video-based Scene Change Detection in Unaligned Scenes](https://arxiv.org/abs/2605.20821)

**<font color=#1a73e8>作者：</font>** Jiae Yoon, Ue-Hwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting what has changed in an environment is essential for long-term autonomy, yet most change detection settings assume fixed viewpoints, mild misalignment, or only a few changed objects. We introduce Video-based Scene Change Detection (VSCD), which predicts a pixel-wise change mask for each query frame, given a reference and a query RGB video of the same indoor space recorded at different times under unconstrained camera motion. The two videos are not temporally synchronized, and many object instances may appear or disappear. To study this setting, we build a large-scale benchmark with over 1.1 million frames annotated with pixel-accurate change masks, together with a real-world test set for evaluating transfer beyond simulation. We propose a query-centric multi-reference model that learns temporal matching implicitly from change-mask supervision, aligns candidate reference features to the query via local patch correspondence, and fuses per-candidate change features using frame-level and patch-level confidence before decoding a high-resolution mask once per frame. Our approach achieves state-of-the-art performance against strong image- and video-based baselines, and we validate its real-world impact by deploying it on a mobile robot for two downstream applications -- visual surveillance and object incremental learning.

---


### 185. [TERDNet: Transformer Encoder-Recurrent Decoder Network for Scene Change Detection](https://arxiv.org/abs/2605.20822)

**<font color=#1a73e8>作者：</font>** Jiae Yoon, Ue-Hwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we address the challenge of Scene Change Detection (SCD), where the goal is to identify variations between two images of the same location captured at different times. Existing SCD models often overlook the varying importance of features across layers, employ single-step decoders that confine refinement, and provide limited insight into encoder pretraining strategies. We propose TERDNet, a Transformer Encoder-Recurrent Decoder Network designed to overcome these limitations. TERDNet consists of a transformer-based encoder that extracts multi-level representations, a feature fusion module that integrates correlation volumes with these features, a recurrent 3-gate-GRU decoder that performs iterative refinement, and a combined convolution-interpolation upsampler that restores fine-grained resolution. Extensive experiments on four public benchmarks show that TERDNet consistently outperforms prior approaches and produces more accurate and detailed change masks. Ablation studies confirm the benefit of segmentation-based pretraining and the effectiveness of our fusion design. In addition, robustness tests under viewpoint misalignment confirm TERDNet's potential for deployment in real-world robotic systems, where reliable perception is critical. Our code is available at this https URL.

---


### 186. [RelWitness: Open-Vocabulary 3D Scene Graph Generation with Visual-Geometric Relation Witnesses](https://arxiv.org/abs/2605.20823)

**<font color=#1a73e8>作者：</font>** Minh Anh Nguyen, Quang Huy Tran, Bao Ngoc Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene graph generation seeks to describe object instances and their relations with flexible natural-language predicates. The central difficulty is not only vocabulary expansion, but supervision reliability: relation annotations in 3D scene graph datasets are selective, and many valid object-pair relations are unannotated. We propose RelWitness, a framework for open-vocabulary 3D scene graph generation from posed RGB-D sequences under incomplete relation supervision. The key concept is a relation witness: a concrete visual-geometric cue that makes a relation observable in the captured scene. Support relations require contact and vertical ordering; containment requires enclosure; proximity requires metric closeness; orientation requires facing direction; and stable relations should persist across views where both objects are visible. RelWitness constructs relation witness records from RGB views, depth maps, reconstructed 3D geometry, role-sensitive text, object-prior null views, and multi-view consistency. A visual-geometric witness verifier assigns unannotated relation candidates to verified missing positives, reliable negatives, or uncertain unlabeled cases. A witness-guided positive-unlabeled objective then learns from incomplete annotations without turning every missing label into a negative. We further introduce witness-consistent decoding and an RGB-D missing-relation audit protocol. Simulated manuscript-planning experiments on 3DSSG/3RScan and ScanNet-derived open-vocabulary splits show the intended behavior: improved unseen-relation recognition, higher witness precision, lower hallucination, and reduced redundant relation phrases. All numerical results are planning values and must be replaced by reproduced measurements before submission

---


### 187. [Markovian Circuit Tracing for Transformer State Dynamic](https://arxiv.org/abs/2605.20824)

**<font color=#1a73e8>作者：</font>** Abdullah X  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many sequence computations are easier to study as movement through internal states than as isolated local circuits. We introduce Markovian Circuit Tracing (MCT), a diagnostic pipeline for testing whether transformer activations contain coarse state-transition structure. The benchmark uses synthetic Hidden Markov Model (HMM) tasks where latent states, transition matrices, Bayesian belief vectors, Bayes-optimal predictions, and forced-state counterfactual targets are known exactly. Across six HMM families and three seeds per family, tiny causal transformers learn near-Bayes next-token predictors, with mean excess loss over Bayes of 0.0138. Residual activations contain partial Bayesian belief information in this controlled synthetic benchmark. State abstractions extracted from these activations recover coarse transition signal, strongest in persistent and lower-state regimes, and weaker in ambiguous-emission and six-state regimes. The clearest result comes from state forcing. Patching a recovered-state centroid reduces KL to the exact HMM counterfactual target from 0.1957 in the unpatched model to 0.0532 on average, beating wrong-state, mean-activation, random-activation, and shuffled-label controls. The contribution is a controlled benchmark and evaluation framework for transformer state-dynamics interpretability, with MCT as a simple reference pipeline

---


### 188. [HyDAR-Pano3D: A Hybrid Disentangled Anatomical Recovery Framework for Panoramic-to-3D Reconstruction](https://arxiv.org/abs/2605.20827)

**<font color=#1a73e8>作者：</font>** Yaoyao Yue, Jérôme Schmid, Xiaoshuang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic radiograph (PR) is fundamentally used in routine dental care, but it inherently provides only a two-dimensional (2D) projection of complex three-dimensional (3D) craniofacial anatomy. Most existing learning-based methods attempt to computationally recover this 3D information by directly regressing native cone-beam computed tomography (CBCT) volumes from PR. However, this direct mapping requires the model to simultaneously learn common anatomical structures and patient-specific morphological variations. This entangled formulation makes the ill-posed 2D-to-3D inverse problem highly ambiguous, often producing over-smoothed reconstructions with blurred anatomical boundaries. To address this, we propose HyDAR-Pano3D, a two-stage framework that reformulates PR-to-CBCT reconstruction as a disentangled anatomical recovery problem. In Stage 1, a dual-encoder network integrates radiographic features with SAM-derived semantic priors to reconstruct an arch-normalized canonical volume. In Stage 2, an Anatomical Restoration Network predicts a prior-constrained structured deformation field to map this canonical volume back to the native space, restoring individual morphological variations. Experiments on three large-scale datasets show that HyDAR-Pano3D significantly outperforms baseline methods ($p < 0.05$), achieving a 25.76 dB PSNR, 85.70\% SSIM, and an 83.83\% overall anatomical Dice score. The synthesized volumes successfully support downstream segmentation of whole teeth (82.4\% Dice) and the inferior alveolar canal (72.2\% Dice), demonstrating that our disentangled approach preserves clinically relevant structures to enable robust anatomy-aware assessment when CBCT data is unavailable.

---


### 189. [USV: Towards Understanding the User-generated Short-form Videos](https://arxiv.org/abs/2605.20838)

**<font color=#1a73e8>作者：</font>** Haoyue Cheng, Su Xu, Liwei Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Several large-scale video datasets have been published these years and have advanced the area of video understanding. However, the newly emerged user-generated short-form videos have rarely been studied. This paper presents USV, the User-generated Short-form Video dataset for high-level semantic video understanding. The dataset contains around 224K videos collected from UGC platforms by label queries without extra manual verification and trimming. Although video understanding has achieved plausible improvement these years, most works focus on instance-level recognition, which is not sufficient for learning the representation of the high-level semantic information of videos. Therefore, we further establish two tasks: topic recognition and video-text retrieval on USV. We propose two unified and effective baseline methods Multi-Modality Fusion Network (MMF-Net) and Video-Text Contrastive Learning (VTCL), to tackle the topic recognition task and video-text retrieval respectively, and carry out comprehensive benchmarks to facilitate future research. Our project page is this https URL.

---


### 190. [Activation-Free Backbones for Image Recognition: Polynomial Alternatives within MetaFormer-Style Vision Models](https://arxiv.org/abs/2605.20839)

**<font color=#1a73e8>作者：</font>** Jeffrey Wang, Jonathan Gregory, Grigorios G. Chrysos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision backbones treat pointwise activations (e.g., ReLU, GELU) and exponential softmax as essential sources of nonlinearity, but we demonstrate they are not required within MetaFormer-style vision backbones. We design activation-free polynomial alternatives for three core primitives (MLPs, convolutions, and attention), where Hadamard products replace standard nonlinearities to yield polynomial functions of the input. These modules integrate seamlessly into existing architectures: instantiated within MetaFormer, a modular framework for vision backbones, our PolyNeXt models match or exceed activation-based counterparts across model scales on ImageNet classification, ADE20K semantic segmentation, and out-of-distribution robustness. We also substantially outperform prior polynomial networks at reduced computational cost, showing that polynomial variants of standard modules beat complex custom architectures.

---


### 191. [Finite-Time Regret Analysis of Retry-Aware Bandits](https://arxiv.org/abs/2605.20854)

**<font color=#1a73e8>作者：</font>** Bingkui Tong, Junpei Komiyama, Soichiro Nishimori 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a stochastic bandit algorithm motivated by retry-aware objectives that value the best outcome among multiple attempts, such as pass@$k$ and max@$k$. Given a posterior over arm values, ReMax chooses a sampling distribution that maximizes the posterior expected maximum reward over $M$ virtual draws. Although this objective was introduced in reinforcement learning as an exploration mechanism under uncertainty, its regret properties in bandit problems have remained unclear. For Gaussian rewards and the first nontrivial case $M=2$, we characterize the optimal ReMax distribution through an expected-improvement balance condition and prove the first sublinear regret bound for ReMax. Our analysis separates the usual saturation behavior of suboptimal arms from a ReMax-specific underestimation effect, in which the optimal arm may be sampled too rarely after an unfavorable estimate. This explains why ReMax can be more exploitative than Thompson sampling (TS) and why its regret analysis is technically delicate. Experiments support this picture: ReMax often outperforms KL-UCB and Thompson sampling under mild underestimation, while posterior-variance scaling empirically mitigates severe underestimation.

---


### 192. [Multi-Step Likelihood-Ratio Correction for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2605.20865)

**<font color=#1a73e8>作者：</font>** Deokgyu Yoon, Hyungkyu Kang, Joongkyu Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) plays a pivotal role in improving the reasoning ability of large language models. However, widely used PPO surrogate objectives are fundamentally local, as they rely on a local approximation of the exact policy gradient objective. While this approximation improves stability by reducing the variance induced by importance sampling, it also introduces structural bias into the surrogate objective, which must be controlled through trust region mechanisms. In this work, we introduce the $N$-step forward trace, which augments the PPO surrogate objective using the cumulative likelihood ratio of the next $N-1$ tokens. Building on this idea, we propose $N$-Step Forward-Trace Policy Optimization (NFPO), a practical RLVR algorithm that integrates the $N$-step forward trace into the masked policy gradient framework. NFPO provides a continuous bridge between the PPO surrogate objective and the exact policy gradient objective, offering a principled mechanism for controlling the bias-variance trade-off. Our theoretical analysis shows that, with an appropriate choice of $N$, the proposed objective yields a tighter policy-improvement bound than the standard PPO surrogate. Experiments on comprehensive reasoning benchmarks demonstrate that NFPO consistently improves performance, supporting our theoretical findings.

---


### 193. [CAdam: Context-Adaptive Moment Estimation for 3D Gaussian Densification in Generative Distillation](https://arxiv.org/abs/2605.20872)

**<font color=#1a73e8>作者：</font>** SeungJeh Chung, Geonho Park, Misong Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive densification is the engine of 3D Gaussian Splatting (3DGS). However, when transposed to the optimization-based Generative Distillation paradigm, this reconstruction-native mechanism reveals fundamental limitations, resulting in inefficient representations cluttered with redundant primitives. We diagnose this failure as a Densification Dilemma stemming from the stochastic nature of generative guidance: the standard magnitude-based accumulation indiscriminately aggregates transient noise alongside geometric signals, making it difficult to strike a balance between over-densification and under-fitting. To resolve this, we introduce Context-Adaptive Moment Estimation (CAdam), a novel framework that reinterprets densification as a statistically grounded signal verification problem. CAdam leverages the first moment of gradients to exploit the interference principle, where stochastic fluctuations cancel out via destructive interference while consistent geometric drifts accumulate via constructive interference, effectively disentangling the underlying signal from the generative noise floor. This is further augmented by a quantile-based context awareness and an intrinsic Signal-to-Noise Ratio (SNR) gating mechanism, which ensure robust adaptation across optimization stages and enable the soft termination of densification. Extensive experiments across diverse objectives (SDS, ISM, VFDS) and strong generative 3DGS backbones show that CAdam reduces Gaussian count by 85%-97% relative to standard densification while preserving overall comparable perceptual quality. These results highlight signal-aware density control as a practical way to improve memory efficiency in optimization-based generative distillation.

---


### 194. [Terminal-World: Scaling Terminal-Agent Environments via Agent Skills](https://arxiv.org/abs/2605.20876)

**<font color=#1a73e8>作者：</font>** Zihao Cheng, Hongru Wang, Zeming Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Terminal agents extend Large Language Models with the ability to execute tasks directly in command-line environments, but their progress is bottlenecked by the scarcity of high-quality training data. Existing approaches bootstrap from partial sources such as human-defined seeds or GitHub repositories to instantiate one component and then complete the rest, producing tasks confined to narrow seed distributions, environments misaligned with task semantics, and inefficient trajectories from unguided exploration. To address these limitations, we introduce Terminal-World, a fully automated pipeline that uses agent skills as the central synthesis primitive, which jointly encode what to accomplish, when to apply (preconditions and environment state), and how to execute, enabling task instructions, environments, and teacher trajectories to be co-derived. To further broaden the synthesis space, Terminal-World composes skills into skill teams and skill graphs for multi-role and cross-domain task synthesis. Using this pipeline, we construct 5,723 training environments and train Terminal-World-8B/14B/32B, evaluated across 6 benchmarks where the Terminal-World series consistently outperforms terminal-agent baselines. Notably, using the same teacher model and only 1.2% of the training data, Terminal-World-32B surpasses Nemotron-Terminal-32B on Terminal-Bench 2.0 by +4.5 Pass@1 (31.5) and achieves 43.8 Pass@3.

---


### 195. [CIG: Exploration via Conditional Information Gain](https://arxiv.org/abs/2605.20878)

**<font color=#1a73e8>作者：</font>** Tim Joseph, Marcus Fechner, Philipp Stegmaier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intrinsic rewards for exploration in reinforcement learning condition on different contexts: lifelong rewards score each transition against accumulated experience but ignore within-rollout redundancy; episodic rewards penalize intra-trajectory repetition but discard lifetime progress. Hybrid methods combine both signals through heuristic weights or require Gaussian-process dynamics that do not scale beyond low-dimensional state spaces. Trajectory-level information gain decomposes into per-step terms that condition on the replay buffer and rollout prefix simultaneously, but remains intractable for deep models. We derive the Conditional Information Gain (CIG) reward as a tractable surrogate: a log-determinant objective over an ensemble disagreement kernel whose Cholesky factorization yields causal per-step rewards that retain both conditioning sets while scaling to high-dimensional state spaces. We instantiate CIG in a model-based setting, where rollouts are short and within-rollout corrections remain largely unexplored. Across twelve tasks spanning discrete (MiniGrid) and continuous control (OGBench), in both clean and stochastic-distractor settings, CIG outperforms or matches prior exploration methods while remaining robust to stochastic distractors.

---


### 196. [NeighborDiv: Training-free Zero-shot Generalist Graph Anomaly Detection via Neighbor Diversity](https://arxiv.org/abs/2605.20879)

**<font color=#1a73e8>作者：</font>** Kaifeng Wei, Teng Liu, Liang Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Anomaly Detection (GAD) is increasingly shifting to Generalist GAD (GGAD) for cross-domain "one-for-all" detection, but existing GGAD methods predominantly rely on the neighbor consistency principle, falling into the \textbf{Node-to-Neighbor Consistency Paradigm} for anomaly quantification. These methods suffer from complex training pipelines, heavy training data dependency, high computational costs, and unstable cross-domain generalization. To address these limitations, we propose NeighborDiv, a training-free generalist graph anomaly detection framework based on neighbor diversity. Departing from the dominant Node-to-Neighbor Consistency Paradigm, we shift the focus to the \textbf{Neighbor-to-Neighbor Diversity Paradigm}, and uncover that the internal structural dispersion of a node's neighbor set is a powerful, independently discriminative anomaly signal. We quantify neighbor diversity via the variance of inter-neighbor feature similarities, which captures how a node organizes its local graph environment, and operates independently of conventional node-to-neighbor consistency frameworks. Extensive experiments under two standard GGAD evaluation paradigms show NeighborDiv achieves state-of-the-art performance, with relative gains of 10.25% in average AUC and 17.78% in average AP over the second-best baseline under Single-Domain Independent Training (SDIT), and 6.89%/9.58% in AUC/AP under Unified Multi-Domain Training (UMDT), respectively. Notably, NeighborDiv yields zero performance volatility across all datasets, eliminating training-set dependency and establishing a lightweight and highly practical GGAD framework.

---


### 197. [Learning fMRI activations dictionaries across individual geometries via optimal transport](https://arxiv.org/abs/2605.20883)

**<font color=#1a73e8>作者：</font>** Sonia Mazelet, Rémi Flamary, Bertrand Thirion  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dictionary learning is a powerful tool for creating interpretable representations. When applied to functional magnetic resonance imaging (fMRI) data, the resulting patterns of brain activity can be used for various downstream tasks, such as brain state classification or population-level analysis. However, a major challenge is the variability in brain geometry across individuals. This is usually addressed by projecting each individual brain geometry onto a common template, which removes subject-specific information. In this work, we introduce a novel approach to dictionary learning on fMRI data that explicitly accounts for this variability. We use the optimal transport-based Fused Gromov-Wasserstein (FGW) distance to compare graphs with different geometries and features. To address the challenge of computing multiple FGW distances for large graphs such as those arising from fMRI data, we rely on amortized optimization to learn a neural network that predicts an approximation of the optimal transport plans, which substantially reduces the computational cost. Additionally, we learn dictionary atoms that depend on the FGW trade-off parameter, which controls the balance between feature alignment and structural consistency. Numerical experiments on the HCP dataset demonstrate that the proposed approach captures different levels of geometric variability in the data and provides representations that preserve essential information.

---


### 198. [Training distribution determines the ceiling of drug-blind cancer sensitivity prediction](https://arxiv.org/abs/2605.20885)

**<font color=#1a73e8>作者：</font>** Taekyung Heo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precision oncology requires predicting which drugs will suppress a specific tumor from its molecular profile, but drug-blind sensitivity prediction has plateaued despite increasingly complex drug representations. Here we show that this stagnation reflects a metric artifact rather than a representational bottleneck. The standard benchmark, global Pearson r, is dominated by between-drug potency differences that a trivial drug-mean predictor captures without any cell-specific learning. Per-drug Pearson r, which isolates within-drug cell ranking, reveals that no drug encoding improves over cell-only features across four independent datasets. A controlled experiment channeling mechanism-of-action identity as either a drug feature or a training-distribution constraint identifies the cause. Supplying MoA as a feature yields negligible benefit, whereas using it to stratify training raises per-drug r substantially for targeted kinase inhibitors, because pan-cancer co-training suppresses pathway-specific sensitivity signals. Mechanism-stratified training and response matching from pilot observations provide two deployable strategies that together recover the principal sources of predictive gain in drug-blind sensitivity prediction.

---


### 199. [Map-Mono-Ego: Map-Grounded Global Human Pose Estimation from Monocular Egocentric Video](https://arxiv.org/abs/2605.20889)

**<font color=#1a73e8>作者：</font>** Hiroyuki Deguchi, Ryosuke Hori, Kotaro Amaya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular egocentric human pose estimation is essential for ubiquitous activity monitoring. However, understanding the user's absolute location within the environment remains a challenge. Existing methods primarily focus on relative motion from an initial position, and tend not to account for the wearer's absolute location within an environment. Furthermore, inherent scale ambiguity in monocular vision leads to severe translational drift, limiting long-term tracking without specialized multi-sensor hardware. To address this, we propose MapMonoEgo, a novel framework achieving globally consistent human pose estimation solely from a monocular camera by leveraging a pre-scanned 3D point cloud. We also introduce AIST-Living dataset, a new dataset pairing egocentric video with ground-truth motion in a scanned environment. Experiments demonstrate that our approach significantly outperforms the state-of-the-art baseline, proving its utility for practical monitoring tasks without specialized hardware.

---


### 200. [GenAI-Driven Threat Detection with Microsoft Security Copilot](https://arxiv.org/abs/2605.20896)

**<font color=#1a73e8>作者：</font>** Scott Freitas, Amir Gharib  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Defending against today's increasingly sophisticated cyberattacks requires security analysts to continuously translate evolving attacker tradecraft into detection logic. This places defenders in a reactive posture, requiring constantly updated expertise across an increasingly fragmented security landscape. We introduce the Dynamic Threat Detection Agent (DTDA), an always-on adaptive agent that continuously investigates security incidents across Microsoft Defender to uncover hidden threats and generate explainable detections when attack-story gaps are found. DTDA combines: (1) a unified activity timeline spanning alerts, events, user and entity behavior analytics, and threat intelligence; (2) versioned LLM prompt contracts with schema validation, grounding requirements, bounded retries, and fail-closed suppression; (3) a planner-executor investigation loop that generates attack-specific hypotheses and gathers supporting and refuting evidence; and (4) dynamic alert generation with a context-relevant title, severity, MITRE mappings, remediation guidance, implicated entities, and natural-language attack description. Integrated into Microsoft Security Copilot and deployed across tens of thousands of Defender customers, DTDA operates continuously at industry scale. In a 120-day online evaluation, DTDA achieves 80.1% precision from customer feedback while generating novel alerts for approximately 15% of investigated incidents. In offline evaluation, DTDA recovers hidden malicious activity with 0.78 F1 using GPT-5.4, improving over GPT-4.1 by 0.12 F1 and outperforming the baseline by 0.26 F1 points. Operationally, DTDA processes single-incident investigations end-to-end in a median of 28 minutes at a median token cost of USD 2.04, with a 0.38% job-level failure rate. These results demonstrate that autonomous agents can identify missed malicious activity at a production scale.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
