# 📦 其他研究 | 2026年05月07日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-213](./part-05.md)

---

### 151. [Self-Improvement for Fast, High-Quality Plan Generation](https://arxiv.org/abs/2605.03625)

**<font color=#1a73e8>作者：</font>** Robert Gieselmann, Henrike von Huelsen, Mihai Samson 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models trained on synthetic plan data are a promising approach to generalized planning. Recent work has focused on finding any valid plan, rather than a high-quality solution. We address the challenge of producing high-quality plans, a computationally hard problem, in sub-exponential time. First, we demonstrate that, given optimal data, a decoder-only transformer can generate high-quality plans for unseen problem instances. Second, we show how to self-improve an initial model trained on sub-optimal data. Each round of self-improvement combines multiple model calls with graph search to generate improved plans, used for model fine-tuning. An experimental study on four domains: Blocksworld, Logistics, Labyrinth, and Sokoban, shows on average a 30% reduction in plan length over the source symbolic planner, with over 80% of plans being optimal, where the optimum is known. Plan quality is further improved by inference-time search. The model's latency scales sub-exponentially in contrast to the satisficing and optimal symbolic planners to which we compare. Together, these results suggest that self-improvement with generative models offers a scalable approach for high-quality plan generation.

---


### 152. [RPBA-Net: An Interpretable Residual Pyramid Bilateral Affine Network for RAW-Domain ISP Enhancement](https://arxiv.org/abs/2605.03626)

**<font color=#1a73e8>作者：</font>** Yucheng Xin, Wu Chen, Xiang Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To address module fragmentation, uninterpretable mappings, and deployment constraints in RAW-domain demosaicing, color correction, and detail enhancement, this paper proposes RPBA-Net, an interpretable residual pyramid bilateral affine network for RAW-domain ISP enhancement. Given packed RAW as input, the method performs residual affine base reconstruction by estimating a base RGB representation and learning identity-guided residual affine corrections, thereby unifying demosaicing and enhancement. It further builds pyramid bilateral affine grids and combines guide-driven autoregressive adaptive slicing with adaptive cross-layer fusion to hierarchically model global tone restoration and local texture enhancement. In addition, smoothness, cross-scale consistency, and magnitude regularization terms are introduced to improve model stability, controllability, and structural interpretability. Extensive experiments demonstrate that RPBA-Net surpasses representative RAW-to-sRGB methods and achieves state-of-the-art performance in reconstruction fidelity and perceptual quality, while maintaining low model complexity and strong deployment potential for mobile and embedded platforms.

---


### 153. [Information Plane Analysis of Binary Neural Networks](https://arxiv.org/abs/2605.03636)

**<font color=#1a73e8>作者：</font>** Maximilian Nothnagel, Bernhard C. Geiger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Information plane (IP) analysis has been suggested to study the training dynamics of deep neural networks through mutual information (MI) between inputs, representations, and targets. However, its statistical validity is often compromised by the difficulty of estimating MI from samples of high-dimensional, deterministic representations.
In this work, we perform IP analyses on binary neural networks (BNNs) where activations are discrete and MI is finite. We characterise the finite-sample behaviour of the plug-in entropy estimator and identify regimes for sample size $N$ and representation dimensionality $D$ under which MI estimates are reliable. Outside these regimes, we show that empirical MI estimates saturate to $\log_2 N$, rendering IP trajectories uninformative.
Restricting attention to the reliable regime, we train 375 BNNs to investigate the existence of late-stage compression phases and the relationship between compressed representations and generalisation performance. Our results show that while late-stage compression is frequently observed, compressed latent representations do not consistently correlate with improved generalization performance. Instead, the relationship between compression and generalisation is highly dependent on task, architecture, and regularisation.

---


### 154. [Diffusion Masked Pretraining for Dynamic Point Cloud](https://arxiv.org/abs/2605.03639)

**<font color=#1a73e8>作者：</font>** Zhuoyue Zhang, Jihua Zhu, Chaowei Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic point cloud pretraining is still dominated by masked reconstruction objectives. However, these objectives inherit two key limitations. Existing methods inject ground-truth tube centers as decoder positional embeddings, causing spatio-temporal positional leakage. Moreover, they supervise inter-frame motion with deterministic proxy targets that systematically discard distributional structure by collapsing multimodal trajectory uncertainty into conditional means. To address these limitations, we propose Diffusion Masked Pretraining (DiMP), a unified self-supervised framework for dynamic point clouds. DiMP introduces diffusion modeling into both positional inference and motion learning. It first applies forward diffusion noise only to masked tube centers, then predicts clean centers from visible spatio-temporal context. This removes positional leakage while preserving visible coordinates as clean temporal anchors. DiMP also reformulates point-wise inter-frame displacement supervision as a DDPM noise-prediction objective conditioned on decoded representations. This design drives the encoder to target the full conditional distribution of plausible motions under a variational surrogate, rather than collapsing to a single deterministic estimate. Extensive experiments demonstrate that DiMP consistently improves downstream accuracy over the backbone alone, with absolute gains of 11.21% on offline action segmentation and 13.65% under causally constrained online this http URL are available at this https URL.

---


### 155. [Agent-Based Modeling of Low-Emission Fertilizer Adoption for Dairy Farm Decarbonisation using Empirical Farm Data](https://arxiv.org/abs/2605.03648)

**<font color=#1a73e8>作者：</font>** Surya Jayakumar, Kieran Sullivan, John McLaughlin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To understand complex system dynamics in dairy farming, it is essential to use modeling tools that capture farm heterogeneity, social interactions, and cumulative environmental impacts. This study proposes an agent-based modeling (ABM) framework to simulate nitrogen management and the adoption of low-emission fertilizer across 295 Irish dairy farms over a 15-year period. Using empirical data, the model represents farm communication through a social network, capturing peer influence and discussion group dynamics, where adoption probabilities are driven by social contagion, farm-scale characteristics, and policy interventions such as subsidies and carbon taxes. The framework estimates sectoral greenhouse gas emissions, cumulative abatement, and private-social cost trade-offs, using Monte Carlo simulation and sensitivity analysis to quantify uncertainty. The model shows strong agreement with observed adoption trajectories ($R^2 = 0.979$, RMSE = 0.0274) and is validated against empirical data using a Kolmogorov-Smirnov test (D = 0.2407, p < 0.001), indicating its ability to reproduce structural patterns in adoption behavior. Adoption dynamics are further characterized using a logistic diffusion model consistent with Rogers' innovation diffusion theory, capturing progression from early adoption to a saturation level of approximately 91%. By framing decarbonization as a socio-technical diffusion process rather than a purely economic optimization problem, this study provides an in silico policy laboratory for evaluating the robustness and diffusion speed of climate mitigation strategies prior to implementation.

---


### 156. [Rethinking Temporal Consistency in Video Object-Centric Learning: From Prediction to Correspondence](https://arxiv.org/abs/2605.03650)

**<font color=#1a73e8>作者：</font>** Zhiyuan Li, Rongzhen Zhao, Wenyan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The de facto approach in video object-centric learning maintains temporal consistency through learned dynamics modules that predict future object representations, called slots. We demonstrate that these predictors function as expensive approximations of discrete correspondence problems. Modern self-supervised vision backbones already encode instance-discriminative features that distinguish objects reliably. Exploiting these features eliminates the need for learned temporal prediction. We introduce Grounded Correspondence, a framework that replaces learned transition functions with deterministic bipartite matching. Slots initialize from salient regions in frozen backbone features. Frame-to-frame identity is maintained through Hungarian matching on slot representations. The approach requires zero learnable parameters for temporal modeling yet achieves competitive performance on MOVi-D, MOVi-E, and YouTube-VIS. Project page: this https URL

---


### 157. [AniMatrix: An Anime Video Generation Model that Thinks in Art, Not Physics](https://arxiv.org/abs/2605.03652)

**<font color=#1a73e8>作者：</font>** Tencent HY Team  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models internalize physical realism as their prior. Anime deliberately violates physics: smears, impact frames, chibi shifts; and its thousands of coexisting artistic conventions yield no single "physics of anime" a model can absorb. Physics-biased models therefore flatten the artistry that defines the medium or collapse under its stylistic variance. We present AniMatrix, a video generation model that targets artistic rather than physical correctness through a dual-channel conditioning mechanism and a three-step transition: redefine correctness, override the physics prior, and distinguish art from failure. First, a Production Knowledge System encodes anime as a structured taxonomy of controllable production variables (Style, Motion, Camera, VFX), and AniCaption infers these variables from pixels as directorial directives. A trainable tag encoder preserves the field-value structure of this taxonomy while a frozen T5 encoder handles free-form narrative; dual-path injection (cross-attention for fine-grained control, AdaLN modulation for global enforcement) ensures categorical directives are never diluted by open-ended text. Second, a style-motion-deformation curriculum transitions the model from near-physical motion to full anime expressiveness. Third, deformation-aware preference optimization with a domain-specific reward model separates intentional artistry from pathological collapse. On an anime-specific human evaluation with five production dimensions scored by professional animators, AniMatrix ranks first on four of five, with the largest gains over Seedance-Pro 1.0 on Prompt Understanding (+0.70, +22.4 percent) and Artistic Motion (+0.55, +16.9 percent). We will publicly release the AniMatrix model weights and inference code.

---


### 158. [A Paradigm for Interpreting Metrics and Identifying Critical Errors in Automatic Speech Recognition](https://arxiv.org/abs/2605.03671)

**<font color=#1a73e8>作者：</font>** Thibault Bañeras-Roux, Mickael Rouvier, Jane Wottawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The most commonly used metrics for evaluating automatic speech transcriptions, namely Word Error Rate (WER) and Character Error Rate (CER), have been heavily criticized for their poor correlation to human perception and their inability to take into account linguistic and semantic information. While metric-based embeddings, seeking to approximate human perception, have been proposed, their scores remain difficult to interpret, unlike WER and CER. In this article, we overcome this problem by proposing a paradigm that consists in incorporating a chosen metric into it in order to obtain an equivalent of the error rate: a Minimum Edit Distance (minED). This approach parallels transcription errors with their human perception, also allowing an original study of the severity of these errors from a human perspective.

---


### 159. [Real Image Denoising with Knowledge Distillation for High-Performance Mobile NPUs](https://arxiv.org/abs/2605.03680)

**<font color=#1a73e8>作者：</font>** Faraz Kayani, Sarmad Kayani, Asad Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While deep-learning-based image restoration has achieved unprecedented fidelity, deployment on mobile Neural Processing Units (NPUs) remains bottlenecked by operator incompatibility and memory-access overhead. We propose an NPU-aware hardware-algorithm co-design approach for real-world image denoising on mobile NPUs. Our approach employs a high-capacity teacher to supervise a lightweight student network specifically designed to leverage the tiled-memory architectures of modern mobile SoCs. By prioritizing NPU-native primitives -- standard 3x3 convolutions, ReLU activations, and nearest-neighbor upsampling -- and employing a progressive context expansion strategy (up to 1024x1024 crops), the model achieves 37.66 dB PSNR / 0.9278 SSIM on the validation benchmark and 37.58 dB PSNR / 0.9098 SSIM on the held-out test benchmark at full resolution (2432x3200) in the Mobile AI 2026 challenge. Following the official challenge rules, the inference runtime is measured under a standardized Full HD (1088x1920) protocol, where it runs in 34.0 ms on the MediaTek Dimensity 9500 and 46.1 ms on the Qualcomm Snapdragon 8 Elite NPU. We further reveal an "Inference Inversion" effect, where strict adherence to NPU-compatible operations enables dedicated NPU execution up to 3.88x faster than the integrated mobile GPU. The 1.96M-parameter student recovers 99.8% of the teacher's restoration quality via high-alpha knowledge distillation (alpha = 0.9), achieving a 21.2x parameter reduction while closing the PSNR gap from 1.63 dB to only 0.05 dB. These results establish hardware-aware distillation as an effective strategy for unifying high-fidelity denoising with practical deployment across diverse mobile NPU architectures. The proposed lightweight student model (LiteDenoiseNet) and its training statistics are provided in the NN Dataset, available at this https URL.

---


### 160. [Graph Neural Network based Hierarchy-Aware Embeddings of Knowledge Graphs: Applications to Yeast Phenotype Prediction](https://arxiv.org/abs/2605.03690)

**<font color=#1a73e8>作者：</font>** Filip Kronström, Alexander H. Gower, Daniel Brunnsåker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a method for finding hierarchy-aware embeddings of knowledge graphs (KGs) using graph neural networks (GNNs) enriched with a semantic loss derived from underlying ontologies. This method yields embeddings that better reflect domain knowledge. To demonstrate their utility, we predict and interpret the effects of gene deletions in the yeast Saccharomyces cerevisiae and learn box embeddings for KGs in the absence of a prediction task. We further show how box embeddings can serve as the basis for evaluating KG revisions.
Our yeast KG is constructed from community databases and ontology terms. Low-dimensional box embeddings combined with GNNs are used to predict cell growth for double gene knockouts. Over 10-fold cross validation, these predictions have a mean $R^2$~score~of~0.360, significantly higher than baseline comparisons, demonstrating that high-level qualitative knowledge is informative about experimental outcomes. Incorporating semantic loss terms in the training of the models improves their predictive performance ($R^2$=0.377) by aligning embeddings with ontology structure. This shows that class hierarchies from ontologies can be exploited for quantitative prediction. We also test the trained models on triple gene knockouts, showing they generalise to data beyond those seen in training.
Additionally, by identifying co-occurring relations in the yeast KG important for the cell-growth predictions, we construct hypotheses about interacting traits in yeast. A biological experiment validates one such finding, revealing an association between inositol utilisation and osmotic stress resistance, highlighting the model's potential to guide biological discovery.

---


### 161. [A Comprehensive Analysis of Tokenization and Self-Supervised Learning in End-to-End Automatic Speech Recognition applied on French Language](https://arxiv.org/abs/2605.03696)

**<font color=#1a73e8>作者：</font>** Thibault Bañeras-Roux, Mickael Rouvier, Jane Wottawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance of end-to-end automatic speech recognition (ASR) systems enables their increasing integration into numerous applications. While there are various benefits to such speech-to-text systems, the choice of hyperparameters and models plays a crucial role in their performance. Typically, these choices are determined by considering only the character (CER) and/or word error rate (WER) metrics. However, it has been shown in several studies that these metrics are largely incomplete and fail to adequately describe the downstream application of automatic transcripts. In this paper, we conduct a qualitative study on the French language that investigates the impact of subword tokenization algorithms and self-supervised learning models from different linguistic and acoustic perspectives, using a comprehensive set of evaluation metrics.

---


### 162. [Distribution-Free Pretraining of Classification Losses via Evolutionary Dynamics](https://arxiv.org/abs/2605.03722)

**<font color=#1a73e8>作者：</font>** Meng Xiang, Yan Pei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Evolutionary Dynamic Loss (EDL), a framework that learns a transferable classification loss in the probability space using unlimited synthetic prediction-label pairs, without accessing real samples during the main loss pretraining stage. EDL parameterizes the loss as a lightweight network and is trained with a semantics-free ranking-consistency objective that assigns larger penalties for more erroneous predictions. To robustly explore the space of loss functions, we optimize EDL via an evolutionary strategy and introduce chaotic mutation to improve exploration under noisy fitness evaluations. Experiments on CIFAR-10 with ResNet backbones show that EDL can serve as a drop-in replacement for cross-entropy and achieves competitive or improved accuracy, while ablation studies confirm that chaotic mutation yields faster convergence and better synthetic pretraining metrics than standard Gaussian mutation.

---


### 163. [Internet of Things Security: A Survey on Common Attacks](https://arxiv.org/abs/2605.03744)

**<font color=#1a73e8>作者：</font>** Dalton Cézane Gomes Valadares, Luiz Antonio Pereira Silva, Daniel Hindemburg de Miranda Marques 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The exponential growth of the Internet of Things (IoT) has integrated connected devices into various sectors like smart cities, digital health, and Industry 4.0, generating vast amounts of real-time data to support intelligent decision-making. However, this widespread adoption is fundamentally challenged by significant security risks, primarily due to the inherent computational limitations of devices, lack of standardization, and an expanding attack surface. Given that security is paramount to ensuring trust in these environments, this paper presents a comprehensive survey and a multi-dimensional analysis of the IoT threat landscape. It describes 28 common attacks, ranging from traditional threats, such as Man-in-the-Middle, to specialized IoT exploits, including node replication and skimming. To provide a structured understanding of these risks, we employ the STRIDE model for functional threat classification alongside the CVSS framework for quantitative criticality assessment. Furthermore, the research establishes a robust mapping between these threats and five foundational vulnerability classes (Process, Code, Communication, Operation, and Device), uncovering the specific technical entry points exploited by adversaries. Beyond threat identification, the survey presents state-of-the-art mitigation techniques and discusses emerging paradigms and research gaps, working as a roadmap for future investigation and providing a consolidated technical foundation for both researchers and practitioners aiming to build resilient and secure IoT ecosystems.

---


### 164. [FluxFlow: Conservative Flow-Matching for Astronomical Image Super-Resolution](https://arxiv.org/abs/2605.03749)

**<font color=#1a73e8>作者：</font>** Shuhong Liu, Xining Ge, Ziteng Cui 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ground-to-space astronomical super-resolution requires recovering space-quality images from ground-based observations that are simultaneously limited by pixel sampling resolution and atmospheric seeing, which imposes a stochastic, spatially varying PSF that cannot be resolved through upsampling alone. Existing methods rely on synthetic training pairs that fail to capture real atmospheric statistics and are prone to either over-smoothed reconstructions or hallucination sources with no physical counterpart in the observed sky. We propose FluxFlow, a conservative pixel-space flow-matching framework that incorporates observation uncertainty and source-region importance weights during training, and a training-free Wiener-regularized test-time correction to suppress hallucination sources while preserving recovered detail. We further construct the DESI--HST Dataset, the large-scale real-world benchmark comprising 19,500 real co-registered ground-to-space image pairs with real atmospheric PSF variation. Experiments demonstrate that FluxFlow consistently outperforms existing baseline methods in both photometric and scientific accuracy.

---


### 165. [GEM-FI: Gated Evidential Mixtures with Fisher Modulation](https://arxiv.org/abs/2605.03750)

**<font color=#1a73e8>作者：</font>** Marco Mustafa Mohammed, Fatemeh Daneshfar, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evidential Deep Learning (EDL) enables single-pass uncertainty estimation by predicting Dirichlet evidence, but it can remain overconfident and poorly calibrated, and it often fails to represent multi-modal epistemic uncertainty. We introduce Gated Evidential Mixtures (GEM), a family of models that learns an in-model energy signal and uses it to gate evidential outputs end-to-end in a distance-informed manner. GEM-CORE learns a feature-level energy and maps it to a bounded gate that smoothly suppresses evidence when support is low. To capture epistemic multi-modality without multi-pass ensembling, GEM-MIX adds a lightweight mixture of evidential heads with learned routing weights while preserving single-pass inference. Finally, GEM-FI stabilizes mixture allocations via a Fisher-informed regularizer, reducing head collapse and producing smoother boundary uncertainty. Across image classification and OOD detection benchmarks, GEM improves calibration and ID/OOD separation with single-pass inference. On CIFAR-10, GEM-FI vs. DAEDL improves accuracy from 91.11 to 93.75 (+2.64 pp), reduces Brier x100 from 14.27 to 6.81 (-7.46), and also improves misclassification-detection AUPR from 99.08 to 99.94 (+0.86). For epistemic OOD detection, GEM-FI achieves AUPR/AUROC of 92.59/95.09 on CIFAR-10 to SVHN and 90.20/89.06 on CIFAR-10 to CIFAR-100, compared with 85.54/89.30 and 88.19/86.10 for DAEDL.

---


### 166. [Vanishing L2 regularization for the softmax Multi Armed Bandit](https://arxiv.org/abs/2605.03752)

**<font color=#1a73e8>作者：</font>** Stefana-Lucia Anita, Gabriel Turinici  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi Armed Bandit (MAB) algorithms are a cornerstone of reinforcement learning and have been studied both theoretically and numerically. One of the most commonly used implementation uses a softmax mapping to prescribe the optimal policy and served as the foundation for downstream algorithms, including REINFORCE. Distinct from vanilla approaches, we consider here the L2 regularized softmax policy gradient where a quadratic term is subtracted from the mean reward. Previous studies exploiting convexity failed to identify a suitable theoretical framework to analyze its convergence when the regularization parameter vanishes. We prove here theoretical convergence results and confirm empirically that this regime makes the L2 regularization numerically advantageous on standard benchmarks.

---


### 167. [GeoTopoDiff: Learning Geometry--Topology Graph Priors through Boundary-Constrained Mixed Diffusion for Sparse-Slice 3D Porous Reconstruction](https://arxiv.org/abs/2605.03764)

**<font color=#1a73e8>作者：</font>** Yue Shi, Peng Wang, Mingzhe Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based voxel prior modelling is challenging for the reconstruction of large-scale 3D porous microstructures. Due to the demanding requirements for simultaneously modelling both the continuous pore morphology and the discrete pore-throat topology, the diffusion models require fully observed CT scans to provide topology-faithful priors, which results in an inherent trade-off among throughput, topological fidelity, and field of view in practical industrial applications. We propose GeoTopoDiff, a graph diffusion-based framework for reconstructing 3D porous microstructures from sparse CT slices. GeoTopoDiff transfers the learning of diffusion priors from a voxel-based space to a mixed graph state space, which simultaneously encompasses continuous pore geometry and discrete pore-throat topology. A topology-aware partial graph prior from sparsely observed CT slices is introduced to constrain the reverse denoising process. Experiments on anisotropic PTFE and Fontainebleau sandstone show that GeoTopoDiff reduces morphology-related errors by 19.8% and topology-sensitive transport errors by 36.5% on average. Our findings suggest that the mixed graph state space promotes the diffusion denoising process to reduce posterior uncertainty under a sparse observations. All models and code have been made publicly available to facilitate the exploration of diffusion models in the field of 3D porous microstructures simulation.

---


### 168. [Firmware Distribution as Attack Surface: A Security Study of ASIC Cryptocurrency Miners](https://arxiv.org/abs/2605.03770)

**<font color=#1a73e8>作者：</font>** Pierre Pouliquen, Hadrien Barral, David Naccache 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> ASIC cryptocurrency miners are a core component of blockchain infrastructures, directly converting computation and energy into monetary value. Despite their economic im- portance, their security is rarely evaluated in a structured manner. In this paper, we show that the firmware distribution ecosystem of mining devices fundamentally challenges existing trust assumptions. We introduce a scalable methodology based on the collection and static analysis of publicly distributed firmware artifacts, requiring neither device access nor runtime interaction. Applying this approach, we reconstruct and analyze 134 firmware images spanning manufacturers that account for over 99% of deployed miners (Bitmain, MicroBT, Canaan, Iceriver). Our re- sults reveal that firmware artifacts alone are sufficient to recover internal architecture, identify security weaknesses, and recon- struct complete attack paths leading to high-impact adversarial objectives. In particular, our analysis reveals vulnerabilities that enable realistic large-scale attack scenarios, including firmware phishing and the exploitation of miners still operating over Stratum V1. Validation on two real devices confirms that publicly distributed artifacts closely reflect deployed software and that these weaknesses translate into attack capabilities. Overall, our study shows that firmware distribution mechanisms themselves constitute a primary attack surface, significantly lowering the barrier to compromise in the ASIC mining ecosystem.

---


### 169. [Task Vector Geometry Underlies Dual Modes of Task Inference in Transformers](https://arxiv.org/abs/2605.03780)

**<font color=#1a73e8>作者：</font>** Hao Yan, Haolin Yang, Yiqiao Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are effective at inferring the latent task from context via two inference modes: recognizing a task seen during training, and adapting to a novel one. Recent interpretability studies have identified from middle-layer representations task-specific directions, or task vectors, that steer model behavior. However, a lack of rigorous foundations hinders connecting internal representations to external model behavior: existing work fails to explain how task-vector geometry is shaped by the training distribution, and what geometry enables out-of-distribution (OOD) generalization. In this paper, we study these questions in a controlled synthetic setting by training small transformers from scratch on latent-task sequence distributions, which allows a principled mathematical characterization. We show that two inference modes can coexist within a single model. In-distribution behavior is governed by Bayesian task retrieval, implemented internally through convex combinations of learned task vectors. OOD behavior, by contrast, arises through extrapolative task learning, whose representations occupy a subspace nearly orthogonal to the task-vector subspace. Taken together, our results suggest that task-vector geometry, training distributions, and generalization behaviors are closely related.

---


### 170. [What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity](https://arxiv.org/abs/2605.03782)

**<font color=#1a73e8>作者：</font>** Haoxi Li, Qinglin Hou, Jianfei Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To navigate partially observable visual environments, recent VLM agents increasingly internalize world modeling capabilities into their policies via explicit CoT reasoning, enabling them to mentally simulate futures before acting. However, relying solely on passive reasoning over visited states is insufficient for sparse-reward tasks, as it lacks the epistemic drive to actively uncover the ``known unknown'' required for robust generalization. We ask: Can VLM agents actively find signals that challenge and refine their internal world model through curiosity-driven exploration? In this work, we propose GLANCE, a unified framework that bridges reasoning and exploration by grounding the agent's linguistic world model into the stable visual representations of an evolving target network. Crucially, GLANCE leverages the discrepancy between linguistic prediction and visual reality as an intrinsic curiosity signal within reinforcement learning, steering the agent to actively explore areas where its internal model is uncertain. Extensive experiments across a series of agentic tasks show the effectiveness of GLANCE, and demonstrate that aligning ``what the agent thinks'' with ``what the agent sees'' is key to solving complex or sparse agentic tasks.

---


### 171. [ReLeaf: Benchmarking Leaf Segmentation across Domains and Species](https://arxiv.org/abs/2605.03784)

**<font color=#1a73e8>作者：</font>** Robert Martinko, Daniel Steininger, Julia Simon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rising global food demand and growing climate pressure increase the need for sustainable, precise agricultural practices. Automated, individualized plant treatment relies on fine-grained visual analysis, yet leaf-level segmentation remains underexplored despite its value for assessing crop health, growth dynamics, yield potential and localized stress symptoms. Progress is limited by a lack of dedicated datasets, especially regarding species coverage, and by the absence of systematic evaluations of modern instance-segmentation architectures for this task. We address these gaps by surveying current data and identifying four suitable, publicly available leaf-segmentation datasets. Using them, we compare one-stage, two-stage and Transformer-based detectors and identify a YOLO26 model configuration to provide the best trade-off for real-world precision-agriculture tasks. Extensive cross-domain generalization experiments reveal substantial performance drops across plant species and recording setups, especially for models trained solely on laboratory data. To strengthen data availability, we introduce a new benchmark dataset with leaf-level masks for 23 plant species, created via semi-automatic annotation of selected CropAndWeed images. A model trained on all four existing datasets achieves a mean mAP50-95 of 83.9% across their corresponding test sets and 40.2% on our new benchmark, demonstrating improved generalization and highlighting the need for diverse leaf-segmentation datasets in robust precision agriculture.

---


### 172. [A Robust Unsupervised Domain Adaptation Framework for Medical Image Classification Using RKHS-MMD](https://arxiv.org/abs/2605.03787)

**<font color=#1a73e8>作者：</font>** Sapna Sachan, Rakesh Kumar Sanodiya, Amulya Kumar Mahto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Labeling medical images is a major bottleneck in the field of medical imaging, as it requires domain-specific expertise, and it gets further complicated due to variability across different medical centers and different imaging devices. Such heterogeneity introduces domain shifts and modality discrepancies, which limits the generalization of trained models. To address this important challenge, we propose an unsupervised domain adaptation framework that combines transfer learning with a Reproducing Kernel Hilbert Space based Maximum Mean Discrepancy loss for the alignment of source and target domains. By jointly optimizing classification and RKHS-MMD losses, the methodology enhances generalization to unannotated medical datasets while diminishing reliance on manual annotation. Experimental evaluations presented on two chest X-ray datasets, which are obtained from different medical centers, show outstanding improvements over models trained without adaptation. Furthermore, we perform a comparative study to see that RKHS-MMD performs better than the standard Maximum Mean Discrepancy in reducing modality gap, emphasizing its effectiveness for medical image classification and also its strong capability in advanced AI-driven medical diagnostics.

---


### 173. [Graph Convolutional Support Vector Regression for Robust Spatiotemporal Forecasting of Urban Air Pollution](https://arxiv.org/abs/2605.03795)

**<font color=#1a73e8>作者：</font>** Nourin Jahan, Madhurima Panja, Muhammed Navas T 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban air quality forecasting is challenging because pollutant concentrations are nonlinear, nonstationary, spatiotemporally dependent, and often affected by anomalous observations caused by traffic congestion, industrial emissions, and seasonal meteorological variability. This study proposes a Graph Convolutional Support Vector Regression (GCSVR) framework for robust spatiotemporal forecasting of urban air pollution. The model combines graph convolutional learning to capture inter-station spatial dependence with support vector regression to model nonlinear temporal dynamics while reducing sensitivity to outlier observations. The proposed framework is evaluated using air quality records from 37 monitoring stations in Delhi and 18 stations in Mumbai, representing inland and coastal metropolitan environments in India. Forecasting performance is assessed across multiple horizons and compared with established temporal and spatiotemporal benchmarks. The results show that GCSVR consistently improves predictive accuracy and maintains stable performance across seasons and outlier-prone pollution episodes. Statistical test further confirms the reliability of the proposed approach across the two cities. Finally, conformal prediction is integrated with GCSVR to generate calibrated prediction intervals, enhancing its practical value for uncertainty-aware air quality monitoring and public health decision-making.

---


### 174. [GPUBreach: Privilege Escalation Attacks on GPUs using Rowhammer](https://arxiv.org/abs/2605.03812)

**<font color=#1a73e8>作者：</font>** Chris S. Lin, Yuqin Yan, Guozhen Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> NVIDIA GPUs with GDDR memories have been shown susceptible to Rowhammer-based bit-flips, similar to CPUs. However, Rowhammer exploits on GPUs have been limited to injecting untargeted bit-flips in victim data like weights of machine learning models, to degrade model accuracy, unlike CPU exploits shown capable of privilege escalation. In this paper, we demonstrate that GPU Rowhammer exploits can be as potent as CPU Rowhammer attacks. By exploiting the GPU page table management to identify when and where new page tables are allocated, we enable an unprivileged user CUDA kernel of one process to use RowHammer bit-flips to gain access to the GPU memory of other processes or co-tenants via targeted tampering of such page-tables resident on the GPU memory. Using this newly found primitive, we demonstrate the first GPU-side privilege escalation attacks, leaking secret data such as cryptographic keys from cuPQC libraries, and even tampering with the model's GPU assembly code to degrade models more stealthily than previous attacks. We further demonstrate that GPU-side privilege escalation can lead to CPU-side privilege escalation, defeating the protections provided by the IOMMU, enabling a malicious user-level program with GPU access to gain root shell and system-wide control, even in a non-multi-tenant setting.

---


### 175. [Realizable Bayes-Consistency for General Metric Losses](https://arxiv.org/abs/2605.03823)

**<font color=#1a73e8>作者：</font>** Dan Tsir Cohen, Steve Hanneke, Aryeh Kontorovich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study strong universal Bayes-consistency in the realizable setting for learning with general metric losses, extending classical characterizations beyond $0$-$1$ classification \citep{bousquet_theory_2021, hanneke2021universalbayesconsistencymetric} and real-valued regression \citep{attias_universal_2024}. Given an instance space $(\mathcal X,\rho)$, a label space $(\mathcal Y,\ell)$ with possibly unbounded loss, and a hypothesis class $\mathcal H \subseteq \mathcal Y^{\mathcal X}$, we resolve the realizable case of an open problem presented in \citet{pmlr-v178-cohen22a}. Specifically, we find the necessary and sufficient conditions on the hypothesis class $\mathcal H$ under which there exists a distribution-free learning rule whose risk converges almost surely to the best-in-class risk (which is zero) for every realizable data-generating distribution. Our main contribution is this sharp characterization in terms of a combinatorial obstruction: Similarly to \citet{attias2024optimallearnersrealizableregression}, we introduce the notion of an infinite non-decreasing $(\gamma_k)$-Littlestone tree, where $\gamma_k \to \infty$. This extends the Littlestone tree structure used in \citet{bousquet_theory_2021} to the metric loss setting.

---


### 176. [Reproducing Complex Set-Compositional Information Retrieval](https://arxiv.org/abs/2605.03824)

**<font color=#1a73e8>作者：</font>** Vincent Degenhart, Dewi Timman, Arjen P. de Vries 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Complex information needs may involve set-compositional queries using conjunction, disjunction, and exclusion, yet it remains unclear whether current retrieval paradigms genuinely satisfy such constraints or exploit `semantic shortcuts'. We conduct a reproducibility study to benchmark major retrieval families and reasoning-targeted methods on QUEST and QUEST+Variants, and introduce LIMIT+, a controlled benchmark where relevance depends on arbitrary attribute predicates and constraint satisfaction, and less on pretrained knowledge. Our findings show that (i) on QUEST, the best neural retrievers achieve an effectiveness that is more than double what can be achieved with BM25 (Recall@100 ${>}$0.41 vs.\ 0.20), but reasoning-targeted methods like ReasonIR and Search-R1 do not outperform general-purpose retrievers uniformly; (ii) on LIMIT+, gains fail to transfer, where the strongest QUEST method collapses from Recall@100${\approx}$0.42 to below 0.02, while classic lexical retrieval gains to ${\sim}$0.96. Lastly, (iii) stratifying by compositional depth reveals a consistent degradation across all methods, where algebraic sparse and lexical methods show more stable performance while dense approaches collapse. We release code and LIMIT+ data generation scripts to support future reproducibility and controlled evaluation.

---


### 177. [Identity-Consistent Multi-Pose Generation of Contactless Fingerprints](https://arxiv.org/abs/2605.03830)

**<font color=#1a73e8>作者：</font>** Zhiyu Pan, Xiongjun Guan, Jianjiang Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contactless fingerprint recognition has gained increasing attention due to its advantages in hygiene and acquisition flexibility. However, the absence of physical contact constraints introduces severe nonlinear geometric distortions caused by free finger poses in 3D space, resulting in a substantial cross-modal domain gap between contactless and conventional contact-based fingerprints. Existing solutions largely rely on explicit geometric correction or image enhancement, which are fragile under extreme pose variations. In this paper, we propose Identity-Consistent Multi-Pose Generation of Contactless Fingerprints (IMPOSE), a physics-inspired framework that synthesizes identity-preserving, multi-pose contactless fingerprint samples to empower recognition models. IMPOSE consists of three stages: (1) rolled fingerprint identity generation via latent diffusion with discrete codebook representations, (2) cross-modal translation from rolled to contactless modality guided by Sauvola-based local adaptive binarization as an identity anchor, and (3) physics-based multi-pose simulation through 3D finger model texture mapping and projection. The generated samples maintain strict identity consistency at the ridge topology level and spatial alignment with standard fingerprint coordinate space. Extensive experiments on the UWA and PolyU CL2CB databases demonstrate that fine-tuning fixed-length dense descriptors (FDD) with IMPOSE-synthesized data achieves state-of-the-art cross-modal matching, reducing EER to 8.74% on UWA and 2.26% on PolyU CL2CB. Synthetic data also yields consistent gains across mainstream representations including DeepPrint and AFRNet, and the hybrid strategy combining synthetic and real data achieves the best overall results. The code and generated samples are available at this https URL.

---


### 178. [A Domain Incremental Continual Learning Benchmark for ICU Time Series Model Transportability](https://arxiv.org/abs/2605.03832)

**<font color=#1a73e8>作者：</font>** Ryan King, Conrad Krueger, Ethan Veselka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, machine learning has made significant progress in clinical outcome prediction, demonstrating increasingly accurate results. However, the substantial resources required for hospitals to train these models, such as data collection, labeling, and computational power, limit the feasibility for smaller hospitals to develop their own models. An alternative approach involves transferring a machine learning model trained by a large hospital to smaller hospitals, allowing them to fine-tune the model on their specific patient data.
However, these models are often trained and validated on data from a single hospital, raising concerns about their generalizability to new data. Our research shows that there are notable differences in measurement distributions and frequencies across various regions in the United States. To address this, we propose a benchmark that tests a machine learning model's ability to transfer from a source domain to different regions across the country. This benchmark assesses a model's capacity to learn meaningful information about each new domain while retaining key features from the original domain.
Using this benchmark, we frame the transfer of a machine learning model from one region to another as a domain incremental learning problem. While the task of patient outcome prediction remains the same, the input data distribution varies, necessitating a model that can effectively manage these shifts. We evaluate two popular domain incremental learning methods: data replay, which stores examples from previous data sources for fine-tuning on the current source, and Elastic Weight Consolidation (EWC), a model parameter regularization method that maintains features important for both data sources.

---


### 179. [Conditions for well-posed color recovery in scattering media](https://arxiv.org/abs/2605.03837)

**<font color=#1a73e8>作者：</font>** Grigory Solomatov, Derya Akkaynak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering scene color from images captured in scattering media is a fundamental inverse problem in optical imaging. Yet the problem is intrinsically ill-posed as multiple solutions can explain the same observation, and prediction error cannot be controlled without understanding the space of candidate solutions. Here, we present sufficient conditions under which color recovery in a scattering medium becomes well-posed. Observing that ill-posedness stems from (i) projection of spectral signals onto pixel intensities, and (ii) unknown medium parameters, we demonstrate that sensor improvements alone cannot resolve medium-induced distortions without additional constraints. We identify recovery patterns, cross-pixel relationships that naturally occur in images, and prove, for an ideal hyperspectral camera, that they restrict the solution to a unique candidate. This opens the door to a new class of vision algorithms grounded in first principles, enabling quantitative analysis of images in scattering environments.

---


### 180. [Complex Equation Learner: Rational Symbolic Regression with Gradient Descent in Complex Domain](https://arxiv.org/abs/2605.03841)

**<font color=#1a73e8>作者：</font>** Sergei Garmaev, Maurice Gauché, Olga Fink  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression aims to discover interpretable equations from data, yet modern gradient-based methods fail for operators that introduce singularities or domain constraints, including division, logarithms, and square roots. As a result, Equation Learner-type models typically avoid these operators or impose restrictions, e.g. constraining denominators to prevent poles, which narrows the hypothesis class. We propose a complex weight extension of the Equation Learner that mitigates real-valued optimization pathologies by allowing optimization trajectories to bypass real-axis degeneracies. The proposed approach converges stably even when the target expression has real-domain poles, and it enables unconstrained use of operations such as logarithm and square root. We Validate the method on symbolic regression benchmarks and show it can recover singular behavior from experimental frequency response data.

---


### 181. [Mechanical Conscience: A Mathematical Framework for Dependability of Machine Intelligenc](https://arxiv.org/abs/2605.03847)

**<font color=#1a73e8>作者：</font>** Munkhdegerekh Batzorig, Purevbaatar Ganbold, Kyungbin Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributed collaborative intelligence (DCI), encompassing edge-to-edge architectures, federated learning, transfer learning, and swarm systems, creates environments in which emergent risk is structurally unavoidable: locally correct decisions by individual agents compose into globally unacceptable behavioral trajectories under uncertainty. Existing approaches such as constrained optimization, safe reinforcement learning, and runtime assurance evaluate acceptability at the level of individual actions rather than across behavioral trajectories, and none addresses the multi-participant, uncertainty-laden nature of DCI deployments. This paper introduces mechanical conscience (MC), a novel concept and simplified mathematical framework that operationalizes trajectory-level normative regulation for both single-agent and distributed intelligent systems. Mechanical conscience is defined as a supervisory filter that minimally corrects a baseline policy's actions to reduce cumulative deviation from a normatively admissible region, while accounting for epistemic uncertainty. We introduce associated constructs, conscience score, mechanical guilt, and resonant dependability, that provide an interpretable vocabulary and computable governance signals for this emerging field. Core theoretical properties are established: admissibility equivalence, existence of optimal regulation, and monotonic deviation reduction. Illustrative results demonstrate that MC-regulated agents maintain trajectory-level normative acceptability where conventional controllers drift outside admissible bounds, and that the framework naturally extends to suppress interaction-induced emergent risk in multi-agent DCI settings.

---


### 182. [Parameter-Efficient Multi-View Proficiency Estimation: From Discriminative Classification to Generative Feedback](https://arxiv.org/abs/2605.03848)

**<font color=#1a73e8>作者：</font>** Edoardo Bianchi, Antonio Liotta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating how well a person performs an action, rather than which action is performed, is central to coaching, rehabilitation, and talent identification. This task is challenging because proficiency is encoded in subtle differences in timing, balance, body mechanics, and execution, often distributed across multiple views and short temporal events. We discuss three recent contributions to multi-view proficiency estimation on Ego-Exo4D. SkillFormer introduces a parameter-efficient discriminative architecture for selective multi-view fusion; PATS improves temporal sampling by preserving locally dense excerpts of fundamental movements; and ProfVLM reformulates proficiency estimation as conditional language generation, producing both a proficiency label and expert-style feedback through a gated cross-view projector and a compact language backbone. Together, these methods achieve state-of-the-art accuracy on Ego-Exo4D with up to 20x fewer trainable parameters and up to 3x fewer training epochs than video-transformer baselines, while moving from closed-set classification toward interpretable feedback generation. These results highlight a shift toward efficient, multi-view systems that combine selective fusion, proficiency-aware sampling, and actionable generative feedback.

---


### 183. [Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation](https://arxiv.org/abs/2605.03849)

**<font color=#1a73e8>作者：</font>** Bin Wu, Mengqi Huang, Shaojin Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distillation-based acceleration has become foundational for making autoregressive streaming video diffusion models practical, with distribution matching distillation (DMD) as the de facto choice. Existing methods, however, train the student to match the teacher's output indiscriminately, treating every rollout, frame, and pixel as equally reliable supervision. We argue that this caps distilled quality, since it overlooks two complementary axes of variance in DMD supervision: Inter-Reliability across student rollouts whose supervision varies in reliability, and Intra-Perplexity across spatial regions and temporal frames that contribute unequally to where quality can still be improved. The objective thus conflates two questions under a uniform weight: whether to learn from each rollout, and where to concentrate optimization within it. To address this, we propose Stream-R1, a Reliability-Perplexity Aware Reward Distillation framework that adaptively reweights the distillation objective at both rollout and spatiotemporal-element levels through a single shared reward-guided mechanism. At the Inter-Reliability level, Stream-R1 rescales each rollout's loss by an exponential of a pretrained video reward score, so that rollouts with reliable supervision dominate optimization. At the Intra-Perplexity level, it back-propagates the same reward model to extract per-pixel gradient saliency, which is factored into spatial and temporal weights that concentrate optimization pressure on regions and frames where refinement yields the largest expected gain. An adaptive balancing mechanism prevents any single quality axis from dominating across visual quality, motion quality, and text alignment. Stream-R1 attains consistent improvements on all three dimensions over distillation baselines on standard streaming video generation benchmarks, without architectural modification or additional inference cost.

---


### 184. [A Deeper Dive into the Irreversibility of PolyProtect: Making Protected Face Templates Harder to Invert](https://arxiv.org/abs/2605.03857)

**<font color=#1a73e8>作者：</font>** Vedrana Krivokuća Hahn, Jérémy Maceiras, Sébastien Marcel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents a deeper analysis of the "irreversibility" property of PolyProtect, a biometric template protection method initially proposed for securing face embeddings. PolyProtect transforms embeddings into protected templates via multivariate polynomials, whose coefficients and exponents are distinct for each subject enrolled in the face recognition system. A polynomial is applied to consecutive sets of elements from a given embedding, where the amount of overlap between the sets is a tunable parameter. We begin our irreversibility analysis by demonstrating that PolyProtected templates are easier to invert using a numerical solver based on cosine distance, as opposed to Euclidean distance (used in the earlier PolyProtect work). To make this inversion more difficult, we then propose a "key selection algorithm", which tries to choose "keys" (coefficients and exponents of the PolyProtect polynomial) that enhance the irreversibility of PolyProtected templates, compared to when the keys are purely random. Our experiments show that this algorithm is effective at generating PolyProtected templates that are significantly more difficult to invert, and that it approximately equalises the irreversibility of PolyProtected templates generated using different "overlap" parameters. This allows for better control of the irreversibility versus accuracy trade-off, known to exist across different overlaps. We also show that accuracy in the PolyProtected domain can be affected by the range in which the embedding elements lie, but that this can be improved by normalizing the embeddings prior to applying PolyProtect. This work is reproducible using our open-source code.

---


### 185. [MCJudgeBench: A Benchmark for Constraint-Level Judge Evaluation in Multi-Constraint Instruction Following](https://arxiv.org/abs/2605.03858)

**<font color=#1a73e8>作者：</font>** Jaeyun Lee, Junyoung Koh, Zeynel Tok 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-constraint instruction following requires verifying whether a response satisfies multiple individual requirements, yet LLM judges are often assessed only through overall-response judgments. We introduce MCJudgeBench, a benchmark for constraint-level judge evaluation in multi-constraint instruction following. Each instance includes an instruction, a candidate response, an explicit constraint list, per-constraint gold labels in {yes, partial, no}, and controlled response-side perturbations. The evaluation protocol further includes evaluation prompt variants to test judge stability. We evaluate proprietary and open-source LLM judges using both correctness and inconsistency metrics, distinguishing intrinsic inconsistency under stochastic decoding from procedural inconsistency under prompt and response perturbations. Our results show that judge reliability has multiple dimensions: strong overall performance does not guarantee equally reliable detection across label categories, especially for rarer partial and no cases. Judges with higher correctness do not always have lower inconsistency. Evaluation with reasoning improves correctness but does not uniformly improve stability. These findings motivate evaluating LLM judges at the constraint level to study these failure modes.

---


### 186. [Correct Is Not Enough: Training Reasoning Planners with Executor-Grounded Rewards](https://arxiv.org/abs/2605.03862)

**<font color=#1a73e8>作者：</font>** Tianyang Han, Hengyu Shi, Junjie Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has become a common way to improve explicit reasoning in large language models, but final-answer correctness alone does not reveal whether the reasoning trace is faithful, reliable, or useful to the model that consumes it. This outcome-only signal can reinforce traces that are right for the wrong reasons, overstate reasoning gains by rewarding shortcuts, and propagate flawed intermediate states in multi-step systems. To this end, we propose TraceLift, a planner-executor training framework that treats reasoning as a consumable intermediate artifact. During planner training, the planner emits tagged reasoning. A frozen executor turns this reasoning into the final artifact for verifier feedback, while an executor-grounded reward shapes the intermediate trace. This reward multiplies a rubric-based Reasoning Reward Model (RM) score by measured uplift on the same frozen executor, crediting traces that are both high-quality and useful. To make reasoning quality directly learnable, we introduce TRACELIFT-GROUPS, a rubric-annotated reason-only dataset built from math and code seed problems. Each example is a same-problem group containing a high-quality reference trace and multiple plausible flawed traces with localized perturbations that reduce reasoning quality or solution support while preserving task relevance. Extensive experiments on code and math benchmarks show that this executor-grounded reasoning reward improves the two-stage planner-executor system over execution-only training, suggesting that reasoning supervision should evaluate not only whether a trace looks good, but also whether it helps the model that consumes it.

---


### 187. [Memory-Efficient Continual Learning with CLIP Models](https://arxiv.org/abs/2605.03866)

**<font color=#1a73e8>作者：</font>** Ryan King, Gang Li, Bobak Mortazavi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pretraining (CLIP) models excel at understanding image-text relationships but struggle with adapting to new data without forgetting prior knowledge. To address this, models are typically fine-tuned using both new task data and a memory buffer of past tasks. However, CLIP's contrastive loss suffers when the memory buffer is small, leading to performance degradation on previous tasks. We propose a memory-efficient, distributionally robust method that dynamically reweights losses per class during training. Our approach, tested on class incremental settings (CIFAR-100, ImageNet1K) and a domain incremental setting (DomainNet) adapts CLIP models quickly while minimizing catastrophic forgetting, even with minimal memory usage.

---


### 188. [Bodyless Presence: Reconsidering the Minimal Self in Immersive Video](https://arxiv.org/abs/2605.03873)

**<font color=#1a73e8>作者：</font>** Koichi Toida  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Immersive video, namely 180-degree and 360-degree video designed to be viewed through head-mounted displays, constitutes a boundary case between interactive VR and conventional two-dimensional video for reconsidering self-experience in XR. It can generate a sense of being there without providing a corresponding body, while allowing only limited sensorimotor contingency through head rotation. From a phenomenological standpoint, this paper reinterprets presence in immersive video not as bodily extension or ownership of an avatar, but as a form of self-experience in which self-location becomes relatively dominant under conditions of reduced body schema availability. This paper calls this condition a self-location-dominant state. In immersive video, the user cannot actively intervene in the recorded environment, and stable agency or ownership is difficult to establish. Nevertheless, events such as viewpoint motion, impact, and direct address are not experienced merely as changes within an image, but as events concerning the position of the self. The minimal self in immersive video is therefore redescribed not primarily as a subject of agency or ownership, but as a self spatially located at a viewpoint while the body schema remains backgrounded. This perspective connects research on presence, the sense of embodiment, and the minimal self, and proposes self-location as a central analytic axis for theorising self-experience in immersive video.

---


### 189. [Spatiotemporal Convolutions on EEG signal -- A Representation Learning Perspective on Efficient and Explainable EEG Classification with Convolutional Neural Nets](https://arxiv.org/abs/2605.03874)

**<font color=#1a73e8>作者：</font>** Laurits Dixen, Stefan Heinrich, Paolo Burelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classification of EEG signals using shallow Convolutional Neural Networks (CNNs) is a prevalent and successful approach across a variety of fields. Most of these models use independent one-dimensional (1D) convolutional layers along the spatial and temporal dimensions, which are concatenated without a non-linear activation layer between. In this paper, we investigate an alternative encoding that operates a bi-dimensional (2D) spatiotemporal convolution. While 2D convolutions are numerically identical to two concatenated 1D convolutions along the two dimensions, the impact on learning is still uncertain. We test 1D and 2D CNNs and a CNN+transformer hybrid model in a low-dimensional (3-channel) and a high-dimensional (22-channel) BCI motor imagery classification task. We observe that 2D convolutions significantly reduce training time in high-dimensional tasks while maintaining performance. We investigate the root of this improvement and find no difference in spectral feature importance. However, a clear pattern emerges in representational similarity across models: 1D and 2D models yield vastly different representational geometries. Overall, we suggest an improved model with a 2D convolutional layer for faster training and inference. We also highlight the importance of architecturally-driven encoding when processing complex multivariate signals, as reflected in internal representations rather than purely in performance metrics.

---


### 190. [DMGD: Train-Free Dataset Distillation with Semantic-Distribution Matching in Diffusion Models](https://arxiv.org/abs/2605.03877)

**<font color=#1a73e8>作者：</font>** Qichao Wang, Yunhong Lu, Hengyuan Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation enables efficient training by distilling the information of large-scale datasets into significantly smaller synthetic datasets. Diffusion based paradigms have emerged in recent years, offering novel perspectives for dataset distillation. However, they typically necessitate additional fine-tuning stages, and effective guidance mechanisms remain underexplored. To address these limitations, we rethink diffusion based dataset distillation and propose a Dual Matching Guided Diffusion (DMGD) framework, centered on efficient training-free guidance. We first establish Semantic Matching via conditional likelihood optimization, eliminating the need for auxiliary classifiers. Furthermore, we propose a dynamic guidance mechanism that enhances the diversity of synthetic data while maintaining semantic alignment. Simultaneously, we introduce an optimal transport (OT) based Distribution Matching approach to further align with the target distribution structure. To ensure efficiency, we develop two enhanced strategies for diffusion based framework: Distribution Approximate Matching and Greedy Progressive Matching. These strategies enable effective distribution matching guidance with minimal computational overhead. Experimental results on ImageNet-Woof, ImageNet-Nette, and ImageNet-1K demonstrate that our training-free approach achieves significant improvements, outperforming state-of-the-art (SOTA) methods requiring additional fine-tuning by average accuracy gains of 2.1%, 5.4%, and 2.4%, respectively.

---


### 191. [Raising the Ceiling: Better Empirical Fixation Densities for Saliency Benchmarking](https://arxiv.org/abs/2605.03885)

**<font color=#1a73e8>作者：</font>** Susmit Agrawal, Jannis Hollman, Matthias Kümmerer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Empirical fixation densities, spatial distributions estimated from human eye-tracking data, are foundational to saliency benchmarking. They directly shape benchmark conclusions, leaderboard rankings, failure case analyses, and scientific claims about human visual behavior. Yet the standard estimation method, fixed-bandwidth isotropic Gaussian KDE, has gone essentially unchanged for decades. This matters now more than ever: as the field shifts toward sample-level evaluation (failure case analysis, inverse benchmarking, per-image model comparison), reliable per-image density estimates become critical. We propose a principled mixture model that combines an adaptive-bandwidth KDE based on Abramson's method, center bias and uniform components, and a state-of-the-art saliency model, to capture different spatial and semantic types of interobserver consistency, and optimize all parameters per image via leave-one-subject-out cross-validation. Our method yields substantially higher interobserver consistency estimates across multiple benchmarks, with median per-image gains of 5-15% in log-likelihood and up to 2 percentage points in AUC. For the most affected images -- precisely those most relevant to failure case analysis -- improvements exceed 25%. We leverage these improved estimates to identify and analyze remaining failure cases of state-of-the-art saliency models, demonstrating that significant headroom for model improvement remains. More broadly, our findings highlight that empirical fixation densities should not be treated as fixed ground truths but as evolving estimates that improve with better methodology.

---


### 192. [From Data Lifting to Continuous Risk Estimation: A Process-Aware Pipeline for Predictive Monitoring of Clinical Pathways](https://arxiv.org/abs/2605.03895)

**<font color=#1a73e8>作者：</font>** Pasquale Ardimento, Mario Luca Bernardi, Marta Cimitile 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a reproducible and process-aware pipeline for predictive monitoring of clinical pathways. The approach integrates data lifting, temporal reconstruction, event log construction, prefix-based representations, and predictive modeling to support continuous reasoning on partially observed patient trajectories, overcoming the limitations of traditional retrospective process mining. The framework is evaluated on COVID-19 clinical pathways using ICU admission as the prediction target, considering 4,479 patient cases and 46,804 prefixes. Predictive models are trained and evaluated using a case-level split, with 896 patients in the test set. Logistic Regression achieves the best performance (AUC 0.906, F1-score 0.835). A detailed prefix-based analysis shows that predictive performance improves progressively as new clinical events become available, with AUC increasing from 0.642 at early stages to 0.942 at later stages of the pathway. The results highlight two key findings: predictive signals emerge progressively along clinical pathways, and process-aware representations enable effective early risk estimation from evolving patient trajectories. Overall, the findings suggest that predictive monitoring in healthcare is best conceived as a continuous, dynamically aware process, in which risk estimates are progressively refined as the patient journey evolves.

---


### 193. [Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems](https://arxiv.org/abs/2605.03900)

**<font color=#1a73e8>作者：</font>** Jie Zhou, Qin Chen, Liang He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.

---


### 194. [Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes](https://arxiv.org/abs/2605.03921)

**<font color=#1a73e8>作者：</font>** Cyrille Kone, Kevin Jamieson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the $(\varepsilon, \delta)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/\delta)$. We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP. Our method achieves asymptotic optimality in sample complexity, also in terms of posterior contraction rate, and runs in $O(S^2AH)$ per episode, matching standard model-based approaches. Unlike prior algorithms such as MOCA and PEDEL, our guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/\delta)$. Our results provide both theoretical insights and practical tools for efficient policy identification in tabular MDPs.

---


### 195. [Reservoir property image slices from the Groningen gas field for image translation and segmentation](https://arxiv.org/abs/2605.03942)

**<font color=#1a73e8>作者：</font>** Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.

---


### 196. [TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis](https://arxiv.org/abs/2605.03944)

**<font color=#1a73e8>作者：</font>** Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.

---


### 197. [Integrating Feature Correlation in Differential Privacy with Applications in DP-ERM](https://arxiv.org/abs/2605.03945)

**<font color=#1a73e8>作者：</font>** Tianyu Wang, Luhao Zhang, Rachel Cummings  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard differential privacy imposes uniform privacy constraints across all features, overlooking the inherent distinction between sensitive and insensitive features in practice. In this paper, we introduce a relaxed definition of differential privacy that accounts for such heterogeneity, allowing certain features to be treated as insensitive even when correlated with sensitive ones. We propose a correlation-aware framework, $\textsf{CorrDP}$, which relaxes privacy for insensitive features while accounting for their correlations with sensitive features, with the correlations quantified using total variation distance. We design algorithms for differentially private empirical risk minimization (DP-ERM) under the $\textsf{CorrDP}$ framework, incorporating distance-dependent noise into gradients for improved theoretical utility guarantees. When the correlation distance is unknown, we estimate it from the dataset and show that it achieves a comparable privacy-utility guarantee. We perform experiments on synthetic and real-world datasets and show that $\textsf{CorrDP}$-based DP-ERM algorithms consistently outperform the standard DP framework in the presence of insensitive features.

---


### 198. [HELO Cryptography: A Lightweight Cryptographic System for Enhancing IoT Security in P2P Data Transmission](https://arxiv.org/abs/2605.03948)

**<font color=#1a73e8>作者：</font>** Tahsin Ahmed, Arjita Saha, Arian Nuhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The recent surge in security concerns for IoT devices highlights the increasing threat of cryptographic vulnerabilities. These weaknesses can lead to unauthorized access, data breaches, and manipulation of device functions, compromising the privacy and security of both the devices and their users. Given the limited computational power of IoT devices, especially when handling large amounts of data, encrypting and transmitting data over insecure networks poses significant challenges. This situation not only heightens security risks and prolongs runtime, but also degrades performance and consumes more resources. To address these issues, a novel cryptographic system named HELO (Hybrid Encryption Lightweight Optimization) is proposed. It is hybridized and gives solid security against cryptographic cyberattacks. However, the research objective is to enhance the security level of IoT devices without decreasing their performance. This system is ideal for resource-constrained gadgets due to its lightweight mechanism. Finally, it offers top-level cryptographic security for IoT gadgets by guaranteeing confidentiality, integrity, and availability while doing P2P data transmission.

---


### 199. [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](https://arxiv.org/abs/2605.03952)

**<font color=#1a73e8>作者：</font>** Jonathan Steinberg, Oren Gal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.

---


### 200. [Transformers with Selective Access to Early Representations](https://arxiv.org/abs/2605.03953)

**<font color=#1a73e8>作者：</font>** Skye Gunasekaran, Téa Wright, Rui-Jie Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-213](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
