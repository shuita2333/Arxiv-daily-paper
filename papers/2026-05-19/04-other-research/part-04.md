# 📦 其他研究 | 2026年05月19日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-234](./part-05.md)

---

### 151. [Community-aware evaluation and threshold calibration for open-set plankton image recognition](https://arxiv.org/abs/2605.15835)

**<font color=#1a73e8>作者：</font>** Xi Chen, Eryuan Huang, Yingjun Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated plankton image recognition is increasingly used in aquatic ecosystem monitoring, but deployed classifiers inevitably encounter unseen taxa and non-target particles. Open-set recognition methods are usually evaluated with sample-level metrics such as AUROC, AUPR, and FPR@95% unknown-recall operating points, whereas ecological monitoring depends on community-level estimates of taxon abundance and diversity. This study examines the mismatch between these objectives using controlled pseudo-communities and three datasets spanning marine zooplankton imaged by ZooScan, marine phytoplankton imaged by IFCB, and freshwater plankton imaged by an in-situ camera. We define Open-Set Community Distortion (OSCD), a Bray-Curtis-style error over known taxa plus an unknown bin, with directional components distinguishing known-taxon overestimation from underestimation. Closed-set classifiers achieved high known-class accuracy, but unknown samples were often absorbed with high confidence and in structured ways. Sample-level OOD metrics were not sufficient to select ecological operating points: for MSP, FPR@95% unknown-recall thresholds produced large test-community OSCD on all three datasets mainly because true known taxa were over-rejected into the unknown bin. Community-aware threshold calibration reduced MSP OSCD relative to fixed 95% known recall on SYKE-ZooScan 2024 and SYKE-IFCB 2022; on ZooLake the fixed-recall baseline was already close to the community-aware threshold, and the best community-level method was a prototype-distance variant rather than MSP. The benefit of community-aware calibration therefore depends on validation-community representativeness and the gap between fixed recall and the community optimum. These results show that open-set plankton recognition should be evaluated as an ecological measurement problem, not only as a sample-level detection task.

---


### 152. [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843)

**<font color=#1a73e8>作者：</font>** Jichen Hu, Jiawei Guo, Jiazhong Cen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D world modeling systems based on generative scene synthesis, such as Marble, can create coherent and explorable 3D environments, yet their outputs are typically static monolithic assets with limited editability and physical interaction. This restricts their use in immersive content creation and embodied simulation, where generated worlds must be actively modified and manipulated. To tackle this challenge, we present WorldAct, a framework that converts static generated 3D worlds into editable and interaction-ready scenes. WorldAct uses a multimodal agent to guide scene decomposition, identify actionable objects, reconstruct geometrically aligned object-level meshes for interaction, and restore the residual background via 3D inpainting. The resulting scenes support object-level editing, collision-aware manipulation, and embodied task execution while preserving global scene coherence. Experiments show that WorldAct enables richer interaction scenarios than the original generated scenes, suggesting a practical path toward editable and interactive 3D world models.

---


### 153. [GHOST: Geometry-Hierarchical Online Streaming Token Eviction for Efficient 3D Reconstruction](https://arxiv.org/abs/2605.15852)

**<font color=#1a73e8>作者：</font>** Leyang Chen, Junyi Wu, Zhiteng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction from long monocular video sequences requires maintaining a key-value (KV) cache that grows linearly with sequence length, creating a severe memory bottleneck. Existing approaches either truncate the cache to a fixed set of anchor frames, leading to reconstruction quality degradation, or rely on attention-score heuristics that are agnostic to 3D scene structure, failing to preserve geometrically valuable tokens. To address these problems, we present GHOST (Geometry-Hierarchical Online Streaming Token Eviction), a training-free KV cache management framework that exploits the model's own 3D geometry outputs to evict redundant tokens online. GHOST introduces three mutually reinforcing innovations: a hierarchical dual-level importance scoring scheme, a privilege mechanism that protects special tokens from eviction, and a cosine-similarity-guided layer-wise budget allocation. Experiments on various benchmarks show that GHOST preserves excellent reconstruction quality while cutting the KV cache by nearly half and delivering 1.75x faster inference compared to state-of-the-art methods. Our code is available at this https URL.

---


### 154. [On RGB-TIR Stereo Calibration under Extreme Resolution Asymmetry](https://arxiv.org/abs/2605.15860)

**<font color=#1a73e8>作者：</font>** Michał Król, Michał Salamonowicz, Władysław Skarbek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate geometric calibration of RGB-thermal infrared (TIR) stereo camera systems is essential for multimodal building envelope analysis, yet remains challenging when low-cost thermal sensors with very low spatial resolution are employed. This paper presents a practical stereo calibration framework for an RGB camera (2028 x 1520 px) paired with a TIR camera operating at only 80 x 62 px - a pixel-count ratio of approximately 1:625. An active OLED screen dynamically switches modality-specific patterns (checkerboard for TIR, ChArUco for RGB) on a single physical surface, providing controlled and repeatable thermal contrast. A dedicated corner detection algorithm combining perspective rectification, Hessian saddle-point analysis, and Mean Shift localisation achieves reliable checkerboard detection at 80 x 62 px without per-frame parameter tuning. A baseline-constrained bundle adjustment enforces physically consistent rig geometry under the planar-calibration-object degeneracy, yielding a stereo baseline of 32.7 mm (nominal 30 mm) with an overall reprojection error of 0.382 px. The system is validated on a thermally active building mock-up using constant-depth and per-pixel depth estimation, demonstrating consistent TIR-to-RGB projection suitable for building energy performance assessment.

---


### 155. [From Observed Viability to Internal Predictive Approximation: A Single-Subject Latent-Space Analysis of Gait Dynamics Under Occlusal Constraint](https://arxiv.org/abs/2605.15862)

**<font color=#1a73e8>作者：</font>** Jacques Raynal, Pierre Slangen, Elsa Raynal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive biomechanical systems may show similar observable gait performance while differing in latent organization and longitudinal behavior. This study examines whether an observed longitudinal transformation of gait organization can be approximated within a predictive latent-space framework, without claiming clinical prediction or causal occlusal effects.
Using an exploratory single-subject design in a Parkinsonian participant, gait was recorded with instrumented insoles during two sessions separated by eleven weeks. Six occlusal observational probes were tested: natural occlusion, open-mouth disengagement, strong clenching, two vertical-dimension increases in centric relation, and one vertical-dimension increase with mandibular protrusion. Principal Component Analysis was used to construct a PC1--PC2 latent representation. A simplified supervised machine-learning model, implemented as a feed-forward neural network, was trained to approximate the observed M1--M2 transformation.
The primary analysis focused on the three centric-relation conditions and tested whether the displacement hierarchy could be reproduced. The model preserved the ordering OC3 < ONL < OC2.5. The extended six-probe analysis also preserved the global structure of the exploratory displacement pattern, with OC3 and OC3P closely grouped and the highest displacements associated with OC2.5 and open-mouth disengagement. Held-out M2 and leave-condition-out analyses showed condition-dependent approximation variability.
These findings do not establish generalizable prediction, therapeutic superiority, causal occlusal effects, or clinical viability forecasting. They support only the restricted conclusion that observed longitudinal latent transformations can be internally approximated within this single-subject dataset, providing a methodological bridge toward future multi-subject predictive viability models.

---


### 156. [Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination](https://arxiv.org/abs/2605.15864)

**<font color=#1a73e8>作者：</font>** Chufan Shi, Cheng Yang, Yaokang Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) often produce self-reflective statements like "let me check the figure again" during reasoning. Do such statements trigger genuine visual re-examination, or are they merely learned textual patterns? We investigate this via VisualSwap, an image-swap probing framework: after a model reasons over an image, we replace it with a visually similar but semantically different one and test whether the model notices. We introduce VS-Bench, 800 image pairs curated from MathVista, MathVerse, MathVision, and MMMU-Pro. Experiments on Qwen3-VL, Kimi-VL, and ERNIE-VL reveal a striking failure: models overwhelmingly miss the swap, with accuracy dropping by up to 60%. Counterintuitively, thinking models are nearly 3x more vulnerable than their instructed counterparts, and scaling offers no mitigation. Multi-turn user instructions restore visual grounding, but self-generated reflective statements during continuous generation do not. Attention analysis explains why: user instructions substantially elevate attention to visual tokens, whereas self-reflection does not. Current VLMs tend to say rather than actually see when claiming to perform visual re-examination. Our code and dataset are available at the project page: this https URL

---


### 157. [Ti-iLSTM: A TinyDL Approach for Logic-Level Anomaly Detection in Industrial Water Treatment Systems](https://arxiv.org/abs/2605.15874)

**<font color=#1a73e8>作者：</font>** Mandar Joshi, Farzana Zahid, Judy Bowen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial Water Treatment Systems (IWTS) are safety critical cyber-physical infrastructures and due to increased connectivity, these systems are exposed to cyber threats that can manipulate process behaviour without creating obvious devices outliers. In particular, logic-layer deception anomalies can preserve numerically plausible measurements while breaking expected cause-and-effect relationships in the control process. These attacks are difficult to detect using threshold-based monitoring or require heavy server-oriented anomaly detection models. This paper explores the potential of Tiny Deep Learning (TinyDL) to provide lightweight on-device logic-level anomaly detection for resource constrained Programmable Logic Controllers (PLCs). We propose a novel framework, TinyDL-based incremental LSTM (Ti-iLSTM) which optimises the memory and space foot print of Long Short-Term Memory (LSTM), to detect logic-layer inconsistencies in Programmable Logic Controller (PLC) based Industrial Water Treatment Systems (IWTS). Experiments on the publicly available SWaT dataset show that the optimised model achieves high detection performance (F1-score=0.983 and ROC-AUC=0.998). A deployment-style validation on the WADI dataset confirms that the proposed light-weight framework remains applicable beyond a single dataset. The research demonstrates that combining logic-aware supervision with Tiny Deep Learning (TinyDL) sequence learning creates an efficient and accurate anomaly detection suitable for resource constrained Programmable Logic Controllers (PLCs) in industrial environments.

---


### 158. [Shapley Neuron Values for Continual Learning: Which Neurons Matter Most?](https://arxiv.org/abs/2605.15877)

**<font color=#1a73e8>作者：</font>** Mohammad Ali Vahedifar, Abhisek Ray, Qi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning enables neural networks to learn tasks sequentially without forgetting previously acquired knowledge. However, neural networks suffer from catastrophic forgetting, where learning new tasks degrades performance on earlier ones. We address this problem with Shapley Neuron Valuation (SNV), a principled framework that quantifies Neuron importance in continual learning, grounded in cooperative game theory. SNV selectively freezes important Neurons while keeping others plastic, enabling buffer-free continual learning without expanding architecture. Experiments on ImageNet-1k show that SNV consistently outperforms existing buffer-free methods. In particular, SNV improves accuracy by +2.88% in the class incremental learning and +6.46% in the task incremental learning scenarios compared to the second baseline.

---


### 159. [FSCM: Frequency-Enhanced Spatial-Spectral Coupled Mamba for Infrared Hyperspectral Image Colorization](https://arxiv.org/abs/2605.15880)

**<font color=#1a73e8>作者：</font>** Tingting Liu, Yuan Liu, Guiping Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal infrared imaging is robust to illumination variations and smoke interference, making it important for all-weather perception. However, the lack of natural color and fine texture limits target recognition, human visual interpretation, and the transfer of visible-light models. Existing infrared colorization methods mainly rely on single-band images, where insufficient spectral cues may lead to structural distortion and semantic confusion. Although infrared hyperspectral images provide rich spectral responses and material information, existing single-band frameworks remain limited in modeling spatial-spectral coupling and weak texture details. To address these issues, this paper presents FSCM, a spectral-information-guided GAN framework. Within FSCM, a frequency-enhanced spatial-spectral state-space generator composed of cascaded FSB units is constructed. Each FSB integrates three complementary components: state-space modeling captures global spatial-spectral dependencies; the frequency enhancement module (FEM) combines multi-level wavelet decomposition and Fourier gating to recover structural contours, directional high-frequency details, and global frequency responses; and the dual-stream hybrid gating module (DGM) integrates deformation-aware sampling with sparse attention to enhance effective local structures and suppress background interference. Additionally, an online semantic segmentation-guided loss is introduced to constrain the generated results, improving semantic consistency in complex road scenes. Experiments show that FSCM outperforms existing infrared colorization methods in visual quality and semantic fidelity.

---


### 160. [FedEDAuth -- Federated Embedding Distribution Authentication for Counterfeit IC Detection](https://arxiv.org/abs/2605.15885)

**<font color=#1a73e8>作者：</font>** Naseeruddin Lodge, Dhruva Aklekar, Vineet Chadalavada 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread of counterfeit integrated circuits (ICs) poses severe risks to the security, reliability, and trustworthiness of modern electronic systems. Federated learning (FL) offers a privacy-preserving paradigm for collaborative counterfeit detection across the semiconductor supply chain, but its vulnerability to byzantine data poisoning attacks limits practical deployment. This paper presents Federated Embedding Distribution Authentication (FedEDAuth), a lightweight, embedding level client authentication framework that detects and filters malicious participants before model aggregation. FedEDAuth leverages reference embedding distributions derived from a golden dataset and evaluates clients using outlier analysis, mean shift measurements, and micro-cluster behavior without requiring access to raw data or gradients. Integrated into standard FL pipelines, FedEDAuth consistently identifies all poisoned clients in experimental settings with 50 distributed participants under the byzantine data poisoning attack, achieving a 100% malicious client detection rate. After filtering, the federated model achieved a high counterfeit IC classification performance of 94.17% accuracy. These results not only validate FedEDAuth's effectiveness but also underscore the broader potential of secure, trustworthy FL frameworks as a critical advancement for next generation hardware security solutions, enabling robust, collaborative intelligence across the semiconductor supply chain.

---


### 161. [Practical Validity Conditions for Byzantine-Tolerant Federated Learning](https://arxiv.org/abs/2605.15887)

**<font color=#1a73e8>作者：</font>** Mélanie Cambus, Darya Melnyk, Tijana Milentijević 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust aggregation is the core operation in Byzantine-tolerant federated learning. To ensure the quality of aggregation independently of data distribution or attacks, validity conditions are needed. They provide geometric guarantees of where the output of the aggregation must lie. The widespread convex validity requires the output to lie in the convex hull of the honest vectors. Although this guarantee is strong in theory, it is poorly suited to modern federated learning systems, as it has dimension-dependent resilience and excludes many practical aggregation rules.
We introduce the minimum enclosing ball (MEB) validity condition for robust aggregation, as well as its multiplicative relaxation, $c$-MEB validity, where $c$ is a constant. We show that exact MEB validity still suffers from limited resilience, while relaxed $c$-MEB validity is achievable if a majority of clients is honest, i.e. $n>2t$. We give an optimal MinMax-MEB rule for the relaxed condition with the bound $c<\sqrt{2}$ and prove explicit relaxed-MEB guarantees for standard aggregators including minimum-diameter averaging, medoid and geometric median. Finally, we relate MEB validity to convex, relaxed-convex and box validity studied in prior literature, thus providing a systematic map of geometric validity conditions for Byzantine-robust aggregation. Our results show that relaxed MEB validity connects validity conditions in distributed computing and Byzantine-tolerant aggregation rules, and offers a practical alternative to convex validity.

---


### 162. [CHoE: Cross-Domain Heterogeneous Graph Prompt Learning via Structure-Conditioned Experts](https://arxiv.org/abs/2605.15888)

**<font color=#1a73e8>作者：</font>** Peiyuan Li, Yongqi Huang, Jitao Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous Graph Prompt Learning (HGPL)has emerged as a promising paradigm for bridging the gap between the objectives of pre-training foundation models and their downstream applications in heterogeneous graph settings. However, existing HGPL methods are primarily designed for in-domain scenarios, whereas real-world deployments often span multiple domains, and the data used for pre-training and downstream tasks may originate from different distributions. Consequently, the applicability of current HGPL approaches is limited to in-domain settings, and their performance typically degrades when application domains shift. To address this serious limitation, we develop CHoE, a cross-domain HGPL method built upon an expert network. During pre-training, we introduce and train structure-conditioned experts, and during prompt tuning, we adopt a structure-aware expert routing and load balancing mechanism to select structurally compatible experts for each meta-path view. In addition, we design a prompt-based semantic fusion module to integrate representations across multiple views for downstream prediction. Extensive experiments show that CHoE consistently improves performance in few-shot cross-domain applications, outperforming all baseline approaches.

---


### 163. [Uncertainty-Aware Wildfire Smoke Density Classification from Satellite Imagery via CBAM-Augmented EfficientNet with Evidential Deep Learning](https://arxiv.org/abs/2605.15894)

**<font color=#1a73e8>作者：</font>** Ranjith Chodavarapu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid and accurate wildfire smoke severity assessment from satellite images is essential for emergency response, air quality modeling, and human health risk management. Existing deep learning approaches treat smoke detection as a binary task, producing point estimates without any measure of prediction confidence. We propose a probabilistic framework to categorize a satellite patch into Light, Moderate, and Heavy severity classes and to provide decomposed epistemic and aleatoric uncertainty in a single forward pass. Our architecture uses the backbone of a pre-trained EfficientNet-B3 and a CBAM module with an evidential deep learning head that predicts Dirichlet concentration parameters, directly estimating vacuity (epistemic) and dissonance (aleatoric) without Monte Carlo sampling. Evaluated on 16,298 real satellite patches derived from the Wildfire Detection dataset, our model achieves 93.8% weighted test accuracy (91.1% unweighted) with ECE=0.0274. Selective prediction retaining the most certain 50% of patches achieves 96.7% accuracy. As image quality degrades, uncertainty increases monotonically, and vacuity is a practical scan quality measure. The Moderate class represents transitional smoke conditions that exhibit the highest epistemic uncertainty (mean vacuity = 0.187), confirming the model correctly identifies ambiguous smoke boundary regions. CBAM spatial attention maps localize to structurally distinctive scene regions, and t-SNE demonstrates the clear cluster separation of Light and Heavy smoke.

---


### 164. [From Layers to Networks: Comparing Neural Representations via Diffusion Geometry](https://arxiv.org/abs/2605.15901)

**<font color=#1a73e8>作者：</font>** Atharva Khandait, Jan E. Gerken  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion geometry is a manifold learning framework that uses random walks defined by Markov transition matrices to characterize the geometry of a dataset at multiple scales. We use diffusion geometry for neural representations, incorporating tools from multi-view learning into this field for the first time. Our key technical observation is that a broad class of similarity measures based on representational similarity matrices (RSMs) admits a closed-form equivalent formulation in terms of row-stochastic Markov matrices, opening the door to manipulations from diffusion geometry. As a first application, we develop multi-scale variants of Centered Kernel Alignment and Distance Correlation, which utilise the $t^{th}$ power of the underlying transition matrix to probe the data geometry at adjustable diffusion scales. Going further, we introduce variants of these measures which fuse the Markov matrices of several layers via alternating diffusion into a single operator that captures the network's joint sample geometry, allowing similarity to be computed across multiple layers and shifting the comparison from layer-to-layer to network-to-network. We perform extensive numerical experiments, evaluating our measures on the Representational Similarity (ReSi) benchmark comprising 14 architectures trained on 7 datasets across three different domains. Our methods achieve SoTA results in accuracy and output correlation for both language and vision tasks across different models. We furthermore show SoTA performance on an additional benchmark evaluating on out-of-distribution data.

---


### 165. [Context-aware Entity-Relation Extraction for Threat Intelligence Knowledge Graphs](https://arxiv.org/abs/2605.15904)

**<font color=#1a73e8>作者：</font>** Inoussa Mouiche, sherif Saad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cybersecurity Knowledge Graphs (CKGs) unify diverse Cyber Threat Intelligence (CTI) sources into structured, queryable formats, offering scalable solutions for automating proactive and real-time security responses. Their increasing adoption has significantly enhanced the workflow and decision-making efficiency of security professionals. However, constructing CKGs requires extracting entity-relation triples from unstructured CTI reports, a task hindered by complex report structure, domain-specific language, and semantic ambiguity. As a result, existing pipeline-based approaches often suffer from error propagation, reducing extraction accuracy and limiting generalizability. This paper introduces the Context-aware Threat Intelligence Knowledge Graph (CTiKG) framework, a pipeline architecture designed to accurately extract and classify threat entities and their relationships from CTI reports. CTiKG incorporates hybrid NLP models that leverage SecureBERT+ contextual embeddings and expert knowledge from a domain ontology to reduce misclassifications and mitigate cascading errors. Experiments on the DNRTI-AUG-STIX2 dataset, which comprises 21 entity types aligned with STIX 2.1, demonstrate significant improvements over state-of-the-art baselines, yielding 3-4% gains in NER and up to 8% in RE performance, based on precision, recall, and F1-score. Additional validation on DNRTI and STUCCO benchmarks confirms the framework's robustness and practical applicability. All datasets, including the curated DNRTI-AUG-STIX2, are released on GitHub to foster reproducibility and further research.

---


### 166. [A Causally Grounded Taxonomy for Image Degradation Robustness Evaluation](https://arxiv.org/abs/2605.15906)

**<font color=#1a73e8>作者：</font>** Stefan Becker, Simon Weiss, Wolfgang Hübner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image degradations can occur during acquisition, processing, and transmission, altering visual appearance and affecting downstream vision tasks. They are studied in several communities, including synthetic corruption benchmarks for robustness evaluation, perceptual image quality assessment, and physically grounded analyses of imaging systems or real camera failures. Although these areas address closely related phenomena, they often use incompatible grouping schemes and backend specific severity definitions, making results difficult to compare across datasets, degradation sources, and tasks.
We propose a causally grounded framework for organizing and interpreting image degradations across these settings. Instead of introducing new degradations or redefining existing benchmarks, we provide an interpretive representation and measurement layer that makes implicit assumptions explicit. Each degradation is described along two orthogonal axes: its dominant causal source in the imaging pipeline (environment, sensor/optics, ISP/renderer/codec, or transfer/system), and its resulting perceptual effect. This dual axis abstraction yields a compact taxonomy spanning algorithmic corruptions, perceptual distortions, and physically motivated imaging artifacts.
To address inconsistent severity semantics without changing existing implementations, we introduce a lightweight severity measurement layer. For every degradation and each native severity level of a given backend, we quantify degradation strength using full reference image quality metrics: PSNR, SSIM, and LPIPS. This makes severity observable and comparable across sources while preserving native parameterizations. We demonstrate the framework through COCO Degradation, a taxonomy aligned benchmark for evaluating object detector robustness under diverse imaging conditions.

---


### 167. [RaPD: Resolution-Agnostic Pixel Diffusion via Semantics-Enriched Implicit Representations](https://arxiv.org/abs/2605.15908)

**<font color=#1a73e8>作者：</font>** Yanhao Ge, Shanyan Guan, Weihao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural images are continuous, yet most generative models synthesize them on discrete grids, limiting resolution-flexible generation. Continuous neural fields enable resolution-free rendering, but prior methods introduce continuity only at the decoding stage as an interpolation module, leaving the generative latent space discretized and reconstruction-oriented. We propose RaPD (Resolution-agnostic Pixel Diffusion), which performs diffusion in a continuous Neural Image Field (NIF) latent space. RaPD bridges this reconstruction-generation gap with Semantic Representation Guidance for generation-aware latent learning and a Coordinate-Queried Attention Renderer for coordinate-conditioned, scale-aware rendering. A single denoised latent can be rendered at arbitrary resolutions by changing only the query coordinates, keeping diffusion cost fixed. Experiments demonstrate superior generation quality and resolution scalability.

---


### 168. [Towards Generalization of Block Attention via Automatic Segmentation and Block Distillation](https://arxiv.org/abs/2605.15913)

**<font color=#1a73e8>作者：</font>** Shuaiyi Li, Zhisong Zhang, Yan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block attention, which processes the input as separate blocks that cannot attend to one another, offers significant potential to improve KV cache reuse in long-context scenarios such as Retrieval-Augmented Generation (RAG). However, its broader application is hindered by two key challenges: the difficulty of segmenting input text into meaningful, self-contained blocks, and the inefficiency of existing block fine-tuning methods that risk degrading performance. To address these, we first construct SemanticSeg, a large and diverse semantic segmentation dataset containing over 30k instances across 16 categories-including books, code, web text, and conversations with text lengths ranging from 2k to 32k. Using this dataset, we train a lightweight segmenter to automatically partition text into human-instinct-aligned blocks with controllable granularity. Second, we propose block distillation, a training framework that is more efficient than block fine-tuning, which uses a frozen full-attention teacher model to guide the block-attention student. This framework integrates three novel components: block sink tokens to mitigate information loss at block boundaries, block dropout to leverage training signals from all blocks, and token-level loss weighting to focus learning on block-attention-sensitive tokens. Experiments across multiple models and benchmarks demonstrate that our segmenter outperforms heuristic and statistical baselines, and block distillation achieves near-full-attention performance under block attention, establishing a practical and scalable pathway for deploying block attention.

---


### 169. [SLIP & ETHICS: Graduated Intervention for AI Emotional Companions](https://arxiv.org/abs/2605.15915)

**<font color=#1a73e8>作者：</font>** Minseo Kim  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI emotional companions face a safety-rapport paradox: restrictive safeguards can damage supportive alliance, while permissive systems risk user harm. We present SLIP (Staged Layers of Intervention Protocol), a four-stage graduated methodology deriving interventions (none, soft, hard) from structured qualitative indicators -- affect intensity (a) and narrative dynamism (m) -- alongside ETHICS (Emergent Taxonomy for Human-AI Interaction Context Signals), a "signals not labels" taxonomy. An evaluation combining a small-scale production deployment (N=68 entries, 10 users, 10 weeks) with a synthetic persona battery (N=91, 5 behavioral-risk profiles) achieved 0% false positives for the flow persona and showed expected escalation patterns in crisis-oriented personas. However, initial results showed that 8 consecutive days of high-energy elevation produced zero interventions (0/8), exposing a boundary where the "do not pathologize" principle conflicts with safety. A subsequent three-model stress test demonstrated that increased model capability improves detection from 0/8 to 6/8 while preserving 0/10 flow false positives in the largest model. Read as preliminary, these findings position graduated intervention as a design direction for navigating -- not resolving -- the safety-rapport tension in affective computing.

---


### 170. [AdaEraser: Training-Free Object Removal via Adaptive Attention Suppression](https://arxiv.org/abs/2605.15921)

**<font color=#1a73e8>作者：</font>** Dingming Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object removal aims to eliminate specified objects from images while plausibly inpainting the affected regions with background content. Current training-free methods typically block attention to object regions within self-attention layers during the image generation process, leveraging surrounding background information to restore the image. However, indiscriminate suppression of self-attention in the vacated areas can degrade generation quality, as the model must simultaneously reconstruct background content in these regions. To solve this conflict, we propose AdaEraser, an adaptive framework that dynamically modulates attention based on the estimated presence of target object concepts. Through analysis of self-attention map evolution across denoising timesteps before and during removal, we develop a token-wise adaptive attention suppression strategy. This approach enables progressive perception of object removal throughout the denoising process, with the suppression strength in self-attention layers adjusted adaptively. Extensive experiments demonstrate that AdaEraser achieves superior performance in object removal, outperforming even training-based methods.

---


### 171. [Invaria: Learning Scale and Density Invariance in Point Clouds via Next-Resolution Prediction](https://arxiv.org/abs/2605.15923)

**<font color=#1a73e8>作者：</font>** Chun-Peng Chang, Shaoxiang Wang, Alain Pagani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image encoders achieve high generalization by decoupling semantic meaning from resolution, an ability yet to be fully realized in the 3D domain. We investigate the failure of 3D point cloud encoders to achieve similar generalization and find that existing models are highly sensitive to sampling resolution and scale changes, leading to significant performance degradation. This sensitivity is a major bottleneck for real-world deployment in robotics, as it suggests models overfit to specific quantization densities and object scales rather than learning invariant semantic features. To mitigate this dependency, we propose Invaria, a point cloud encoder that achieves scale and density invariance through next-resolution prediction and receptive field calibration. While our objective is not the explicit generation of high-resolution point clouds, we find that this training objective encourages the model to learn robust, structural invariants. The resulting encoder achieves significant performance gains during resolution shifts while maintaining high efficiency through a compact model size and reduced token requirements. Specifically, on ScanNet, Invaria achieves a 56.0\% higher mIoU at 3$\times$ lower resolution and a 20\% improvement when the objects scale is reduced by a factor of 3. These gains are achieved with a 45\% smaller model size and an average reduction of 40\% in input tokens.

---


### 172. [Synchronized Realities: Towards Magic Mobile Experiences through Aligned AR](https://arxiv.org/abs/2605.15924)

**<font color=#1a73e8>作者：</font>** Jan Henry Belz  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In virtual reality environments, the alignment of perceptual modalities is crucial for immersion and presence. In the AR domain, it is difficult to create such alignments because elements in the physical world are often beyond the user's control. However, recent advances in generative AI enable on-demand content creation, enabling highly reactive AR experiences. Combined with contextual information about the physical world, it has become possible to design experiences that seamlessly align with the user's environment. In this reflection paper, I emphasize the importance of "synchronized" realities for context-aware AR experiences, particularly in mobility scenarios. I present several examples of existing synchronized experiences and examine their commonalities and distinctions. Finally, I discuss opportunities and pitfalls of synchronizing AR experiences with the physical world.

---


### 173. [GEMS -- Guided Evolutionary Molecule Design for Sustainable Chemicals](https://arxiv.org/abs/2605.15932)

**<font color=#1a73e8>作者：</font>** Coelina Robinson, Franziska Weissbach, Kjell Jorner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designing safe and sustainable chemicals is critical to combat chemical pollution in our environment. Machine learning (ML) methods have been developed to aid with de novo molecule design. However, data on the environmental impacts of chemical compounds are sparse, resulting in low-fidelity ML oracles and unreliable candidate proposals. Furthermore, generative ML models rely on numerical scoring functions that cannot fully capture the nuanced chemical intuition of expert scientists required for real-world molecular design. We present GEMS-an interactive visual analytics tool that enables domain experts to directly collaborate with a genetic algorithm for molecule design. Users can integrate their expert knowledge to guide the evolutionary process by modifying the scoring function and molecule population without programming knowledge or ML developer support. A usage scenario demonstrates the system's application in designing sustainable antioxidant alternatives. In an interview session with domain scientists, we collected feedback on the usefulness of GEMS.

---


### 174. [Privacy is Fungibility: Why Endogenous Tokens Are Not Money](https://arxiv.org/abs/2605.15934)

**<font color=#1a73e8>作者：</font>** Alex Lynham, Geoffrey Goodell  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this paper, we make a case that endogenous tokens such as cryptoassets are not money. First, we define and classify tokens found on public, permissionless ledgers, contrasting them with privately issued stablecoins and proposed CBDC designs. We then discuss the work of Kahn et al in Money is Privacy on cash versus simplified credit, and we extend their analysis to the situation found on most public, permissionless ledgers. Many public, permissionless ledgers utilize an account-based abstraction for balances, resulting in a default state that maps onto the most harmful models of agent interaction enumerated in Money is Privacy. The conclusion is threefold: that most blockchain economies lack a cash-like primitive; that stablecoins do not intrinsically fulfil this role; and that the reliance of a network on an endogenous token for security exposes holders even of a privacy-preserving asset to the same risk, if that asset relies on the same global ledger state as the endogenous token.

---


### 175. [A Retrieval-Enhanced Transformer for Multi-Step Port-of-Call Sequence Prediction in Global Liner Shipping](https://arxiv.org/abs/2605.15937)

**<font color=#1a73e8>作者：</font>** Yanzhao Su, Fang He, Yineng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate multi-step port-of-call sequence prediction is vital for tactical resource orchestration and logistical efficiency. However, existing methods struggle with unreliable voyage schedules and the inability of AIS data to provide visibility beyond the immediate next port. To address this, this study proposes a Connectivity-Constrained and Retrieval-Enhanced (CCRE) deep learning framework. Inspired by Retrieval-Augmented Generation, CCRE introduces a retrieval-enhanced historical encoder that queries a global maritime database for contextually similar navigational precedents. Transforming these scenarios into candidate-level semantic representations compensates for data sparsity in long-tail routes and resolves routing ambiguities. Integrating this with a Transformer-based trajectory encoder, the architecture executes adaptive "middle fusion" via cross-attention. This dynamically shifts predictive reliance from real-time kinematics for short-term accuracy to historical context for long-term strategic stability. To ensure sequence-level coherence, forecasting is formulated as a joint sequence generation problem using an autoregressive Transformer decoder enriched with Scheduled Sampling and Gumbel-Softmax relaxation. This mitigates error accumulation, while topology masks strictly enforce maritime network reachability to eliminate operationally infeasible routes. Evaluated on a global dataset, CCRE achieves a 72.3% first-destination accuracy and a 61.4% average three-step accuracy, outperforming baselines like CatBoost and LSTM by average margins of 12.6% and 11.3%, respectively. Case studies further corroborate the model's scalability and ability to capture complex routing patterns across diverse international trade lanes.

---


### 176. [From Failure to Feedback: Group Revision Unlocks Hard Cases in Object-Level Grounding](https://arxiv.org/abs/2605.15951)

**<font color=#1a73e8>作者：</font>** Yuyuan Liu, Yiping Ji, Anjie Le 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finetuning Large Vision-Language Models with reinforcement learning has emerged as a promising approach to enhance their capability in object-level grounding. However, existing methods, mainly based on GRPO, assign rewards at the response level. Such sparse reward, often criterion-induced, leads to minimal learning signals when all candidate responses fail in challenging scenarios. In this work, we propose a group-revision optimisation paradigm that enhances learning on hard cases. It begins with a sampled initial response and generates a set of revised candidates to explore improved grounding outcomes. Inspired by reward shaping, we introduce a consolidation process that quantifies each candidate's improvement over the initial attempt and converts it into informative shaping signals. These signals are used to both refine the reward and modulate the advantage, amplifying the influence of high-quality revisions. Our method achieves consistent gains across referring and reasoning segmentation, REC, and counting benchmarks compared with prior GRPO-based models. Our code is available at this https URL.

---


### 177. [Driving Through the Network: Performance and Workload Under Latency and Video Impairment](https://arxiv.org/abs/2605.15952)

**<font color=#1a73e8>作者：</font>** Ines Trautmannsheimer, Ahmed Azab, Frank Diermeyer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Teleoperation promises to extend the operational envelope of automated vehicles, yet it critically depends on network latency and video quality. We report a fixed-base driving-simulator study (N=25) with a 2x2 manipulation of added latency (100/300 ms) and bitrate (500/2000 kbit/s), plus a best-case baseline (0 ms added, 9000 kbit/s). We measured effective glass-to-glass (G2G) latency per condition (baseline approx. 413 ms; effective totals approx. 500-700 ms) and verified stable framerate and encoder settings. Multimodal measures covered performance (speed, steering reversals, crashes), oculomotor behavior (blink rate, fixation duration), physiology (RR interval, heart rate, skin conductance), and subjective workload. Latency and bitrate each increased operator load and modestly affected performance. Physiological measures (heart rate, RR interval) exhibited sub-additive interactions, whereas performance and oculomotor interactions were small or non-significant. Equivalence tests showed that 300 ms with 2000 kbit/s was velocity-equivalent to best-case (SESOI +/- 2 km/h), while 300 ms with 500 kbit/s was not. We argue that latency and video quality should be treated as largely independent design levers, and that physiology-aware adaptation can anticipate overload before safety is compromised.

---


### 178. [When and Why Adversarial Training Improves PINNs: A Neural Tangent Kernel Perspective](https://arxiv.org/abs/2605.15959)

**<font color=#1a73e8>作者：</font>** Yuan-dong Cao, Chi Chiu SO, Jun-Min Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) are powerful surrogates for differential equations but are notoriously difficult to train due to spectral bias, stiffness, and poor accuracy on high-frequency or multiscale solutions. Adversarial training based on generative adversarial networks (GANs) has recently gained surprisingly strong empirical results in improving training, but the underlying mechanisms remain elusive. To this end, we propose a new analysis framework for adversarially trained PINNs, based on the key observation of how the discriminator in GANs can influence the training dynamics of PINNs. The framework first provides a much needed theoretical grounding to why and when adversarial training is effective in PINNs, then presents a unified analysis of GANs variants in such training, and finally leads to a new, practical, efficient training algorithm for PINNs. Empirical results demonstrate that our method can significantly reduce the pathology of PINNs training, thereby providing better models with superior performances, often several magnitudes more accurate than alternative methods.

---


### 179. [PAGER: Bridging the Semantic-Execution Gap in Point-Precise Geometric GUI Control](https://arxiv.org/abs/2605.15963)

**<font color=#1a73e8>作者：</font>** Jingxuan Wei, Xi Bai, Shan Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large vision-language models have significantly advanced GUI agents, enabling executable interaction across web, mobile, and desktop interfaces. Yet these gains largely rely on a forgiving region-tolerant paradigm, where many nearby pixels inside the same component remain valid. Precise geometric construction breaks this assumption: actions must land on points in continuous canvas space rather than tolerant regions. Because geometric primitives carry ontological dependencies, a local coordinate error can induce cascading topological failures that distort downstream objects and invalidate the final construction. We identify this regime as precision-sensitive GUI tasks, requiring point-level accuracy, geometry-aware verification, and robustness to dependency-driven error propagation. To benchmark it, we introduce PAGE Bench, with 4,906 problems and over 224K process-supervised, pixel-level GUI actions. We further propose PAGER, a topology-aware agent that decomposes construction into dependency-structured planning and pixel-level execution. Pixel-grounded supervised tuning establishes executable action grammar, while precision-aligned reinforcement learning mitigates rollout-induced exposure bias through state-conditioned geometric feedback. Experiments reveal a pronounced Semantic-Execution Gap: general multimodal models can exceed 88% action type accuracy yet remain below 6% task success. PAGER closes this gap, delivering 4.1x higher task success than the strongest evaluated general baseline and raising step success rate from below 9% for GUI-specialized agents to over 62%, establishing a new state of the art for point-precise GUI control.

---


### 180. [Entropy-Based Characterisation of the Polarised Regime in Latent Variable Models](https://arxiv.org/abs/2605.15965)

**<font color=#1a73e8>作者：</font>** Peter Clapham, Lisa Bonheme, Marek Grzes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational Autoencoders (VAEs) often exhibit a polarised regime in which latent variables separate into active, passive, and mixed subsets. Existing criteria for identifying active dimensions depend on a Gaussian prior, limiting their applicability to variational models and specific priors. We propose a simple information-theoretic classification of the polarised regime based on the entropy of the mean representation. We show theoretically how this entropy couples to KL minimisation through entropy--variance bounds, and we relate the resulting criterion to Bonheme's active/passive conditions. We also clarify a key limitation: entropy of the mean alone cannot reliably distinguish active from mixed dimensions without additional signals from the variance representation. Empirically, we evaluate the entropy criterion on $\beta$-VAEs, identifiable VAEs, Least-Volume Autoencoders, and L2-regularised autoencoders, and find that it consistently recovers a polarised regime when such a regime is present across the model classes studied. Finally, we show that passive dimensions can yield small but consistent improvements on downstream tasks when latent codes are appropriately normalised, suggesting that collapse is often a matter of scale rather than absolute information removal.

---


### 181. [Ontology for Policing: Conceptual Knowledge Learning for Semantic Understanding and Reasoning in Law Enforcement Reports](https://arxiv.org/abs/2605.15978)

**<font color=#1a73e8>作者：</font>** Anita Srbinovska, Jansen Orfan, Adrian Martin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Law enforcement reports contain structured fields and written narratives. However, many incident facts that are needed for review, police training, and investigations are in natural language and require manual reading. We propose a framework using symbolic methods for converting narratives into evidence-linked facts. Our objective is to measure the value of narratives to recover incident details only from the unstructured text and build temporal graphs with time cues and domain axioms. We achieve this by redacting personal identifiers, semantic parsing, predicate mapping to ontology, and reasoning. We evaluate the symbolic approach on 450 property crime reports and a short human review. Of the extracted events from the system, 54.1% had a confidence score of at least 0.80 and 93.7% were mapped through the PropBank--VerbNet--WordNet semantic path. 100% agreement was reached on incident initiation, stolen items, and temporal cues and lower agreement for forced entry interpretation.

---


### 182. [Petri Net Induced Heuristic Search for Resource Constrained Scheduling](https://arxiv.org/abs/2605.15983)

**<font color=#1a73e8>作者：</font>** Ido Lublin, Dor Atzmon, Izack Cohen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We formulate the Resource-Constrained Project Scheduling Problem (RCPSP) as optimal search over the reachability graph of a Timed Transition Petri Net with Resources, using relative-delay tokens so that scheduling decisions correspond to transition firings in the induced state space. We solve the resulting problem with $A^*$ guided by a heuristic that combines Critical Path and resource-based lower bounds, and prove that it is consistent under our token-based time semantics. Experiments on the PSPLIB benchmarks show that the approach outperforms strong exact Mixed-Integer Linear Programming (MIP) baselines (SCIP, CBC) in both success rate and solve time. Per-instance analysis shows that heuristic search and MIP degrade along independent axes, resource tightness for $A^*$ and formulation size for MIP, with resource strength mediating which solver benefits from scale.

---


### 183. [Defining Cultural Capabilities for AI Evaluation: A Taxonomy Grounded in Intercultural Communication Theory](https://arxiv.org/abs/2605.15990)

**<font color=#1a73e8>作者：</font>** Isar Nejadgholi, Masoud Kianpour, Krishnapriya Vishnubhotla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tremendous efforts have been put into evaluating the inclusivity and effectiveness of AI systems across cultures. However, the cultural capabilities considered in much of the literature remain vaguely defined, are referred to using interchangeable terminology, and are typically limited to recalling accurate information about various demographics, regions, and nationalities. To address this construct ambiguity, we draw from Intercultural Communication scholarship and propose a three-level taxonomy of AI-relevant cultural capabilities: Cultural Awareness answers "Does the model know?", Cultural Sensitivity answers "How does it frame its knowledge?", and Cultural Competence answers "Can it adapt as the interaction evolves?". Beyond conceptual clarification, we position this taxonomy as a practical tool for improving the validity and interpretability of AI evaluation in real-world, multicultural settings. Without such construct clarity, evaluation results risk overstating model capabilities and may lead to inappropriate deployment decisions in culturally sensitive contexts.

---


### 184. [Quantum Futures Interactive: A Live Demonstration of Post-Quantum Blockchain Security, Infrastructure Tradeoffs, and Sustainable Distributed Trust](https://arxiv.org/abs/2605.15991)

**<font color=#1a73e8>作者：</font>** Dongping Liu, Aoyu Zhang, Luyao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advances in quantum computing introduce long-term security challenges for widely deployed public-key cryptographic systems used across blockchain platforms and decentralized applications. Although post-quantum cryptography (PQC) standards are emerging, understanding quantum risk remains fragmented across research, engineering, governance, and investment communities. This demo presents Quantum Futures Interactive, a live interdisciplinary demonstration platform combining educational visualization, participatory interaction, and cryptographic artifact generation to illustrate the transition from classical to quantum-resilient blockchain systems. Participants engage in a structured interaction flow including quantum threat education, sentiment capture, technology prioritization, infrastructure tradeoff exploration, and generation of post-quantum cryptographic outputs. The system integrates distributed trust concepts, sustainability-aware infrastructure considerations, and responsible innovation within an interactive decision framework. The demonstration supports interdisciplinary dialogue on blockchain resilience while aligning with United Nations Sustainable Development Goals (SDGs).

---


### 185. [Constrained latent state modeling: A unifying perspective on representation learning under competing constraints](https://arxiv.org/abs/2605.15995)

**<font color=#1a73e8>作者：</font>** Gwenolé Quellec  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning latent representations from complex data is central to modern machine learning, spanning temporal, multimodal, and partially observed systems. In such settings, representations are better understood as latent states capturing underlying system dynamics, rather than as mere compressed summaries of observations. Yet current approaches remain fragmented, relying on distinct -- and often implicit -- assumptions about what these states should represent. We argue that this fragmentation reflects a more fundamental limitation: latent representations are typically learned from underconstrained objectives that fail to specify the properties that meaningful latent states should satisfy. As a result, multiple representations can satisfy the same objective, leading to ambiguity in their structure and interpretation. While many of the underlying principles have been explored in isolation, their interactions have not been explicitly formalized. In this work, we propose constrained latent state modeling (CLSM) as a unifying perspective. We identify a set of core properties -- predictive sufficiency, minimality, temporal coherence, observation compatibility, invariance to nuisance factors, and structural constraints -- and show that they are intrinsically coupled through fundamental trade-offs. Revisiting major modeling families through this lens, we show that existing approaches can be interpreted as enforcing different subsets of constraints, thereby occupying distinct regions of a common design space. This perspective reframes persistent challenges such as lack of identifiability as consequences of underconstrained formulations, rather than isolated technical limitations. More broadly, CLSM provides a principled framework to make design choices explicit, to analyze trade-offs, and to guide the development of more interpretable, robust, and task-aligned latent state models.

---


### 186. [Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning](https://arxiv.org/abs/2605.15997)

**<font color=#1a73e8>作者：</font>** Yuyuan Liu, Can Peng, Yingyu Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in deep learning has significantly advanced CT image analysis, particularly for segmentation tasks. However, these advances are largely confined to image-level pattern recognition, with most methods lacking explicit anatomical or contextual reasoning. Large vision-language models introduce linguistic context into image analysis, yet most approaches typically focus on a single task, which is insufficient for clinical workflow analysis that requires multiple fine-grained types of analysis, such as anatomy detection and segmentation. In this paper, we propose a unified autoregressive framework that integrates language-guided visual reasoning into CT interpretation. Our method introduces task-routing tokens that trigger detection and segmentation heads conditioned on the hidden states of a large vision-language model, enabling coherent generation of visual outputs (e.g., masks and bounding boxes) and textual reasonings. To progressively enhance localisation accuracy and semantic clarity, we further design a "closer-look" mechanism that allows the model to perform progressive coarse-to-fine visits to regions of interest under refined fields of view. To support model training and evaluation, we curated a new multimodal CT dataset containing pixel-wise masks, bounding boxes, spatial prompts, and structured descriptions for visual objects constructed through an AI-assisted annotation process with human verification. Experiments on public benchmarks demonstrate consistent improvements over the SoTA, achieving up to 1.0% Dice on BTCV and 1.7% Dice on MosMed+, while additionally providing appearance reasoning outputs. The code and dataset will be available.

---


### 187. [Echo-Forcing: A Scene Memory Framework for Interactive Long Video Generation](https://arxiv.org/abs/2605.16003)

**<font color=#1a73e8>作者：</font>** Mingqiang Wu, Weilun Feng, Zhefeng Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models enable open-ended generation through local attention and KV caching. However, existing training-free long-video optimization methods mainly focus on stable extension under a single prompt, making them difficult to handle interactive scenarios involving prompt switching, old scene forgetting, and historical scene recall. We identify the core bottleneck as the functional entanglement of historical KV states: stable anchors and recent dynamics are handled by the same cache policy, leading to outdated background contamination, delayed response to new prompts, and loss of long-range memory. To address this issue, we propose Echo-Forcing, a training-free scene memory framework specifically designed for interactive long video generation with three core mechanisms: (1) Hierarchical Temporal Memory, which decouples stable anchors, compressed history, and recent windows under relative RoPE; (2) Scene Recall Frames, which compresses historical scenes into spatially structured KV representations to support long-term recall; and (3) Difference-aware Memory Decay, which adaptively forgets conflicting tokens according to the discrepancy between old and new scenes. Based on these designs, Echo-Forcing uniformly supports smooth transitions, hard cuts, and long-range scene recall under a bounded cache budget. Extensive evaluations on VBench-Long further demonstrate that Echo-Forcing achieves the best overall performance in both long-video generation and interactive video generation settings. Our code is released in this https URL

---


### 188. [End-to-end plaque counting and virus titration from laboratory plate images with deep learning](https://arxiv.org/abs/2605.16008)

**<font color=#1a73e8>作者：</font>** Eugenia Moris, Alicia Costábile, Sebastián Rey 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plaque assays remain the gold standard readout of virus infectivity; however, plaque counting from plate images is labor-intensive and prone to inter-operator variability. We present an end-to-end, computer-aided workflow for cytopathic effect-based virus titration directly from laboratory plaque assay images. The proposed approach combines two models derived from the Segment Anything Model (SAM): a SAM2-based well-segmentation module that localizes assay wells across heterogeneous imaging conditions, and a SAM-based plaque-segmentation model that detects and enumerates plaques within each well. The method was evaluated on a mixed dataset comprising private plaque assay images of Mayaro virus and Coxsackievirus B3, together with public Vaccinia virus images from the VACVPlaque dataset. The pipeline outputs per-well plaque counts, automatically computes plaque-forming units per milliliter (PFU/mL), and is integrated into a web-based platform that allows users to review results and organize experiments. On held-out plates (17 from MAYV/CVB3 and 22 from VACV), the workflow generalized across two plate formats (6-well and 12-well) and showed strong agreement with manual annotations (Pearson correlation coefficients of 0.92 for MAYV/CVB3 and 0.88 for VACV). Automated plaque counts were further compared with annotations from four independent experts, demonstrating high concordance. The proposed system will be open sourced and publicly released upon acceptance of this manuscript to enable reproducible, scalable, and audit-ready plaque assay analysis while substantially reducing manual annotation effort.

---


### 189. [Accelerated Gradient Descent for Faster Convergence with Minimal Overhead](https://arxiv.org/abs/2605.16017)

**<font color=#1a73e8>作者：</font>** Manuel Graca, L. Miguel Silveira, Arlindo Oliveira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present CT-AGD (Curvature-Tuned Accelerated Gradient Descent), an optimization method for non-convex optimization problems in deep learning training tasks. CT-AGD is a general boosting procedure that accelerates first-order methods by explicitly capturing the local curvature using finite-difference quotients, and the development of heuristics aimed at mitigating noise and bias introduced by stochastic mini-batch training. CT-AGD has a comparable storage and computational overhead as adaptive gradient methods such as Adam. Our extensive experiments demonstrate that CT-AGD achieves the same level of accuracy as the baseline first-order methods, yet reduces the required training epochs by 33% on average.

---


### 190. [Variational Autoregressive Networks with probability priors](https://arxiv.org/abs/2605.16020)

**<font color=#1a73e8>作者：</font>** Piotr Białas, Piotr Korcyl, Tomasz Stebel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monte Carlo methods are essential across diverse scientific fields, yet their efficiency is frequently hampered by critical slowing down-a sharp increase in autocorrelation times near phase transitions. Although deep learning approaches, such as neural-network-based samplers, have been proposed to alleviate this issue, they face another serious problem: the difficulty of training the models. This difficulty partially stems from the overly general nature of original machine-learning architectures, which often ignore underlying physical symmetries and force networks to relearn them from scratch. In this paper, we demonstrate that incorporating physical priors into the model significantly enhances performance. Building upon existing strategies that integrate spin-spin interactions, we propose a framework that utilizes a prior probability distribution as a starting point for training. Our results for the Ising model, as well as for the Edwards-Anderson spin glass model, suggest that moving away from `blank slate' models in favor of physics-informed priors reduces the training burden and facilitates the simulation of larger system sizes in discrete spin models.

---


### 191. [ScreenSearch: Uncertainty-Aware OS Exploration](https://arxiv.org/abs/2605.16024)

**<font color=#1a73e8>作者：</font>** Michael Solodko, Justin Wagle  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Desktop GUI agents operate under partial observability: visually similar screens can correspond to different underlying workflow states, so locally plausible actions can lead to sharply different outcomes. We frame this as a problem of computer/OS state exploration, where effective behavior requires both expanding the reachable frontier and reducing ambiguity before committing. We present ScreenSearch, a system that combines structural screen retrieval and deduplication with an ambiguity-aware PUCT graph-bandit for large-scale desktop exploration. The retrieval layer converts UIA trees into location-aware structural features, indexes related screens through sparse token search and metadata filters, and maintains a shared deduplicated state graph across VM workers. On top of this graph, we define a scalable ambiguity signal based on matched-action outcome dispersion. If similar screens produce different next states under the same action signature, the state should be probed further rather than treated as resolved. We use this signal together with frontier rewards to drive large-scale exploration and replay-start policy evaluation over the shared graph. Across 11 desktop applications, ScreenSearch collects over 1M screenshots and over 30K deduplicated states, yielding large exploration corpora with substantial cross-application and within-application diversity. On a fixed replay-start slice, we observe a clear novelty--ambiguity trade-off: some policies reduce ambiguity quickly while discovering little frontier. Ambiguity reduction alone is therefore not a sufficient exploration objective. Appendix ablations show that stronger proposal priors can materially improve unique-state discovery during corpus building. These results suggest that state identity, proposal quality, and ambiguity-aware search all matter when deciding when to probe and when to commit.

---


### 192. [Mind Dreamer: Untethering Imagination via Active Latent Intervention on Latent Manifolds](https://arxiv.org/abs/2605.16030)

**<font color=#1a73e8>作者：</font>** Shaojun Xu, Xiaoling Zhou, Yihan Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-Based Reinforcement Learning (MBRL) leverages latent imagination for sample efficiency, yet remains constrained by Historical Tethering: imagination is typically initialized from observed states. This creates a learning asymmetry, where the world model's manifold discovery outpaces the policy's sparse-reward optimization. We propose Mind Dreamer (MD), a framework that operationalizes Active Latent Intervention (ALI) to transcend Markovian continuity. MD reformulates discovery as the minimization of a global Relay Manifold Expected Free Energy (R-EFE); by sampling initial states from a learned generator $s_0 \sim p_{gen}(\cdot)$ rather than the historical buffer, MD utilizes an adversarial generator to synthesize non-continuous latent jumps to epistemic blind spots that are physically plausible yet cognitively challenging. To resolve the credit assignment paradox across these spatial ruptures, we derive the Relay Value Function (RVF) and Relay Uncertainty Function (RUF). These potentials treat synthesized anchors as counterfactual intermediary states, propagating pragmatic and epistemic value through a principled Bellman-style formulation. Notably, we prove that uncertainty propagation across discontinuities necessitates a quadratic discount $\gamma^2$, establishing a formal epistemic horizon. Theoretically, MD approximates a variance-minimizing importance sampler that expands the manifold's spectral gap, reducing the hitting time to critical bottleneck states. Empirically, MD achieves a 1.67$\times$ average speedup over DreamerV3 on DeepMind Control Suite, reaching 8.8$\times$ in sparse-reward tasks.

---


### 193. [Who Owns This Agent? Tracing AI Agents Back to Their Owners](https://arxiv.org/abs/2605.16035)

**<font color=#1a73e8>作者：</font>** Ruben Chocron, Doron Jonathan Ben Chayim, Eyal Lenga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly deployed to act autonomously in the world, yet there is still no reliable way to trace a harmful agent back to the account that deployed it. This creates the same accountability gap across both ends of the intent spectrum: benign operators may deploy misconfigured or overbroad agents that cause harm unintentionally, while malicious operators may deliberately weaponize agents for scams, harassment, or cyber attacks. In many cases, these agents are powered by vendor-hosted models, a dependency that holds even for sophisticated adversaries such as state actors conducting cyber operations. In either case, affected parties can observe the behavior but cannot notify the responsible operator, stop the session, or identify the account for investigation.
We formalize this gap as the problem of agent attribution: linking an observed agent interaction to the responsible account at the hosting vendor. To our knowledge, this is the first work to define the problem and present a practical solution. Our protocol is canary-based: an authorized party injects a canary into the agent's interaction stream, and the vendor searches a narrow window of session logs to recover the originating session and account. Simple canaries suffice in non-adversarial settings. For adversarial operators who filter or paraphrase incoming content, we develop robust canary constructions that cannot be suppressed without degrading the agent's own task performance, yielding a formal asymmetry in the defender's favor. We evaluate a variety of scenarios including real-world agents and show that our attribution method is reliable, robust, and scalable for vendor-side deployment.

---


### 194. [Looped SSMs: Depth-Recurrence and Input Reshaping for Time Series Classification](https://arxiv.org/abs/2605.16048)

**<font color=#1a73e8>作者：</font>** Mónika Farsang, Ramin Hasani, Daniela Rus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) are inherently recurrent along the sequence dimension, yet depth-recurrence - reusing the same block repeatedly across layers, as recently applied in looped transformers - has not been explored in this model family. We show that a looped SSM with $k$ parameters iterated $L$ times consistently closely matches or outperforms a standard SSM with $k \cdot L$ independent parameters across four architectures (LRU, S5, LinOSS, LrcSSM) and six time series classification benchmarks, despite operating within a strictly smaller hypothesis space, as we formally establish. Since the larger model contains the looped model as a special case, this dominance cannot be explained by expressivity and instead points to parameter sharing across depth as a beneficial inductive bias that simplifies optimization. These results demonstrate that depth-recurrence is orthogonal to sequence-recurrence and independently beneficial. We further show that input reshaping is an equally neglected design axis: concatenating timesteps for low-dimensional inputs, or flattening and rechunking the joint feature-time dimension for high-dimensional ones, yields accuracy gains of 1-6% across all models, confirmed over 5 random seeds. Both techniques provide standalone improvements that compound when combined, suggesting that depth and input reshaping are two independent and underexplored design axes for SSMs on time series.

---


### 195. [Reasoners or Translators? Contamination-aware Evaluation and Neuro-Symbolic Robustness in Tax Law](https://arxiv.org/abs/2605.16052)

**<font color=#1a73e8>作者：</font>** Parisa Kordjamshidi, Samer Aslan, Madhavan Seshadri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have significantly enhanced automated legal reasoning. Yet, it remains unclear whether their performance reflects genuine legal reasoning ability or artifacts of data contamination. We present a comprehensive empirical study of tax law reasoning approaches and implement a contamination detection protocol to rigorously assess LLM reliability. We show that performance can be inflated by contamination. Building on this analysis, we conduct a systematic evaluation, comparing monolithic LLMs with hybrid systems that translate statutory text into formal representations and delegate inference to symbolic solvers. We build a novel test suite designed to probe generalization to unseen documents via case and rule variations. Our findings indicate that legal reasoning is inherently compositional and that neuro-symbolic frameworks offer a more reliable and robust foundation for legal AI, as well as improved generalization to unobserved situations.

---


### 196. [Ada-Diffuser: Latent-Aware Adaptive Diffusion for Decision-Making](https://arxiv.org/abs/2605.16054)

**<font color=#1a73e8>作者：</font>** Fan Feng, Selena Ge, Minghao Fu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has framed decision-making as a sequence modeling problem using generative models such as diffusion models. Although promising, these approaches often overlook latent factors that exhibit evolving dynamics, elements that are fundamental to environment transitions, reward structures, and high-level agent behavior. Explicitly modeling these hidden processes is essential for both precise dynamics modeling and effective decision-making. In this paper, we propose a unified framework that explicitly incorporates latent dynamic inference into generative decision-making from minimal yet sufficient observations. We theoretically show that under mild conditions, the latent process can be identified from small temporal blocks of observations. Building on this insight, we introduce Ada-Diffuser, a causal diffusion model that learns the temporal structure of observed interactions and the underlying latent dynamics simultaneously, and furthermore, leverages them for planning and control. With a modular design, Ada-Diffuser supports both planning and policy learning tasks, enabling adaptation to latent variations in dynamics, rewards, and latent actions. Experiments on simulated control and robotic benchmarks demonstrate its effectiveness in accurate latent inference and adaptive policy learning.

---


### 197. [Robust Prior-Guided Segmentation for Editable 3D Gaussian Splatting](https://arxiv.org/abs/2605.16065)

**<font color=#1a73e8>作者：</font>** Raushan Joshi, Jean-Yves Guillemaut  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3D-GS) enables real-time 3D scene reconstruction but lacks robust segmentation for editing tasks such as object removal, extraction, and recoloring. Existing approaches that lift 2D segmentations to the 3D domain suffer from view inconsistencies and coarse masks. In this paper, we propose a novel framework that leverages the Segment Anything Model High Quality (SAM-HQ) to generate accurate 2D masks, addressing the limitations of the standard SAM in boundary fidelity and fine-structure preservation. To achieve robust 3D segmentation of any target object in a given scene, we introduce a prior-guided label reassignment method that assigns labels to 3D Gaussians by enforcing multiview consistency with learned priors. Our approach achieves state-of-the-art segmentation accuracy and enables interactive, real-time object editing while maintaining high visual fidelity. Qualitative results demonstrate superior boundary preservation and practical utility in Virtual Reality (VR) and robotics, advancing 3D scene editing.

---


### 198. [SAFE Quantum Machine Learning with Variational Quantum Classifiers](https://arxiv.org/abs/2605.16067)

**<font color=#1a73e8>作者：</font>** Ying Chen, Paolo Giudici, Vasily Kolesnikov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a variational quantum classifier operating on high dimensional deep representations via amplitude encoding, stabilized by a learnable classical pre encoding this http URL combining normalized amplitude embeddings with bounded quantum observables, the resulting model induces a structured and smooth hypothesis class with controlled sensitivity to input variations. Model reliability is assessed using SAFE-AI metrics derived from the Cramer von Mises divergence, enabling consistent evaluation across accuracy, robustness, and explainability dimensions. Empirical results show that the proposed quantum model provides competitive predictive performance compared with strong classical baselines while exhibiting a more balanced SAFE reliability profile, with improved robustness to noise and stability under structured feature removal. These findings suggest that variational quantum circuits offer a principled mechanism for stability oriented SAFE learning in safety critical settings.

---


### 199. [AgriMind: An Ensemble Deep Learning Framework for Multi-Class Plant Disease Classification](https://arxiv.org/abs/2605.16076)

**<font color=#1a73e8>作者：</font>** Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plant disease detection is still largely manual in Bangladesh, where extension workers eyeball leaf samples across millions of smallholdings. We built AgriMind to automate this: an ensemble of ResNet50, EfficientNet-B0, and DenseNet121 trained on 20,638 PlantVillage images across 15 pepper, potato, and tomato disease classes. Transfer learning with frozen ImageNet backbones and 10 epochs of head-only training keeps the pipeline lightweight. Individual models hit 96--97% on the held-out test set, but averaging their softmax outputs pushes the ensemble to 99.23% -- a two-thirds cut in error rate. We tried biasing the average toward the best validation model; it backfired. Dropping any single model also hurt. Pepper and potato classify perfectly; tomato, with ten visually similar classes, still reaches 99.01%. On an NVIDIA T4 GPU the full ensemble runs at 53 FPS. Whether that translates to real-time mobile use depends on TensorFlow Lite optimization -- work we have not yet completed.

---


### 200. [ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation](https://arxiv.org/abs/2605.16080)

**<font color=#1a73e8>作者：</font>** Qing Huang, Zhipei Xu, Xuanyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rise of AI-generated images (AIGIs) poses growing challenges for digital authenticity, prompting the need for efficient, generalizable image forgery detection systems. Existing methods, whether non-LLM-based or LLM-based, exhibit distinct advantages and limitations. While non-LLM-based models offer efficient low-level artifact detection, they often lack semantic understanding. Conversely, LLM-based methods provide strong semantic reasoning and explainability but are computationally intensive and less sensitive to subtle visual artifacts. Moreover, the true contribution of explanatory reasoning texts to forgery detection performance remains unclear. In this work, we investigate the intrinsic value and potential of LLM-generated reasoning texts, considering it a source of generalization and semantic-error sensitivity. Based on these findings, we propose ReAlign, a novel framework that distills high-quality reasoning texts generated by a GRPO-optimized LLM into a lightweight AIGI detector via contrastive learning. ReAlign effectively inherits the generalization ability and semantic sensitivity capability of reasoning textual representations, while remaining efficient and lightweight for deployment. Moreover, ReAlign adopts a tailored joint optimization strategy that integrates contrastive loss for image-text alignment and classification loss for accurate forgery discrimination. Experimental results on AIGCDetectBenchmark, AIGI-Holmes, and our newly constructed UltraSynth-10k demonstrate that ReAlign consistently outperforms existing state-of-the-art detectors in both accuracy and generalization, particularly when facing complex, high-fidelity forgeries from modern generative models.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
