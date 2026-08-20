# 📦 其他研究 | 2026年08月21日

> 本类共 **184** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-184**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-184**

---

### 151. [Introducing the Privacy-HSD Trade-off: Hate Speech Detection, but not at the Cost of Privacy](https://arxiv.org/abs/2608.19006)

**<font color=#1a73e8>作者：</font>** Stephen Meisenbacher, Vlad Garbuz, Chirill Donos 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hate speech is a real and timely threat that affects a large portion of online users, especially youth and minority groups. While building reliable and robust automatic hate speech detection (HSD) systems is paramount, we argue that this must also be balanced with the individual right to privacy. Exploring the intersection of HSD and privacy, we demonstrate that HSD systems might unintentionally achieve performance at the cost of encoding authorship, posing a threat to privacy. Building on these findings, we establish the notion of a privacy-HSD trade-off, which demands a careful balance. We benchmark a series of text privatization methods, as well as our newly proposed domain-specific AgnoSpeech technique, showing that balancing privacy and HSD is difficult but feasible. The findings make a strong case for more research on the trade-offs between privacy and HSD, both of which have tangible implications for the safeguarding of online participation.

---


### 152. [Harness Continual Learning: Continual Adaptation Beyond Model Parameters](https://arxiv.org/abs/2608.19013)

**<font color=#1a73e8>作者：</font>** Borui Kang, Jinrui Gu, Junhan Lv 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience. Modern agents can also adapt through a harness of prompts, memories, tools, skills, and routing rules. Because these contents jointly shape later execution, a harness update can disrupt previously reliable behavior even when the model is frozen. This raises a new question: how can an agent continually improve its state outside the model while retaining behavior acquired earlier? We formulate Harness Continual Learning (HCL), a new continual learning paradigm in which the harness evolves around a frozen foundation model, and define the resulting loss of earlier behavior as harness-level forgetting. We instantiate HCL with four execution-facing components: the Task Interface, Experience Memory, Capability Map, and Adaptive Router. We further introduce guarded harness evolution to separate update generation from state commitment. A Continual Optimizer proposes candidate harnesses from post-execution feedback, and a Continual Evaluator commits the resulting candidate harness only after checking current improvement, historical retention, and validity. Experiments on textual reasoning, multimodal perception, and open-world interaction demonstrate capability accumulation and failure recovery, with relative gains exceeding 10% over corresponding baselines in multiple settings. Component ablations assess the contribution of each harness component, while controlled retention sweeps reveal measurable harness-level forgetting and show that the stability--plasticity trade-off can be explicitly adjusted.

---


### 153. [One-Stage Object Detectors in Autonomous Driving](https://arxiv.org/abs/2608.19014)

**<font color=#1a73e8>作者：</font>** Jonel Roman, Ryan Sirjue, Peter Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles depend on fast and reliable perception systems to detect surrounding vehicles, pedestrians, cyclists, traffic signs, and other road objects in real time. This paper presents a comprehensive survey and analysis of one-stage object detectors for autonomous driving rather than an implementation of a new detection system. The survey reviews the evolution of major one-stage detectors, including YOLOv1, SSD, RetinaNet, EfficientDet, anchor-free detectors such as FCOS and CenterNet, and recent real-time models such as YOLOv10. It compares these architectures through their design choices, feature-fusion strategies, loss functions, deployment trade-offs, and reported benchmark performance. The paper also summarizes commonly used autonomous-driving datasets, evaluation metrics, open challenges, and future research directions. Overall, this survey highlights how one-stage detectors balance speed, accuracy, efficiency, and robustness, while also emphasizing the remaining gap between benchmark results and dependable real-world autonomous-driving performance.

---


### 154. [Orthogonal Polynomial Approximation for Matrix Log Normalization in Global Covariance Pooling](https://arxiv.org/abs/2608.19021)

**<font color=#1a73e8>作者：</font>** Md Rifat Ur Rahman, Md Raihan Khan, Md Sakib Hossain Shovon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global Covariance Pooling (GCP) improves deep networks by capturing second-order feature statistics, and is especially effective for fine-grained recognition. Because covariance matrices live on the Symmetric Positive Definite (SPD) manifold, a normalization step is required before the Euclidean classifier. The faithful choice is the matrix logarithm (MLN-COV), which maps the SPD manifold to its tangent space; in practice it was abandoned in favour of the matrix square root because its eigendecomposition-based gradient is numerically unstable. We show that this instability is an artifact of computing the logarithm spectrally, not of the logarithm itself. Approximating the logarithm with finite polynomials in the covariance matrix removes the eigendecomposition from both passes: every operation becomes a General Matrix Multiplication (GEMM), the gradient stays bounded on the spectral support of the pre-normalized covariance, and the unstable 1/(lambda_i-lambda_j) term never appears. The key ingredient is a mean-eigenvalue pre-normalization that centres the spectrum near 1, away from the singularity of log, with a scalar post-compensation that returns the singular part of log(A) in closed form. Our recommended normalizer is a degree-8 Chebyshev expansion evaluated by a three-term matrix recurrence, with a matching reverse recurrence for the backward pass; Legendre, Laguerre, Taylor and Pade expansions are studied as controls that isolate the roles of the basis and of the target function. On three fine-grained benchmarks and ImageNet-1k the decomposition-free logarithm is both faster and more accurate than the spectral logarithm and than the square-root approximations it replaces, and at matched basis and degree the log target beats the square-root target, confirming that the gain comes from the faithful Riemannian map rather than from a better polynomial family.

---


### 155. [Institutional Books - Enriched Text: A customizable multilingual open-source pipeline for denoising, deduplicating, and annotating OCR text at scale](https://arxiv.org/abs/2608.19026)

**<font color=#1a73e8>作者：</font>** David Lowry-Duda, Matteo Cargnelutti, Catherine Brobston 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Released in 2025, Institutional Books: Harvard Library (IB-HL) is a collection of 983,004 volumes (242B o200k_base tokens), originally digitized through Harvard Library's participation in the Google Books Library project. As researchers and developers have begun to use IB-HL, a tension has emerged between standard large-scale preprocessing practices and the goals of careful information stewardship. Many existing pipelines optimize for web text: as a result, they tend to aggressively filter, deduplicate, restrict by language, and sometimes discard meaningful metadata. Meanwhile, researchers seeking to use IB-HL duplicate effort while performing similar processing and analysis.
We describe an approach that we call Enriched Text. Instead of producing a single 'complete' stream of tokens, we normalize the text while preserving metadata through annotations. We separate endmatter, detect per-paragraph language, identify clusters of duplicate paragraphs, and compute per-paragraph bits-per-byte scores. We provide this information through HTML-like annotations layered on top of the text. By parsing these annotations, users can tailor the output to their own needs instead of accepting a global editorial decision on content. The pipeline applies to all $\approx$250 languages in the collection.
This report describes this project's goals, implementation, and design rationale. The release includes IB-HL-ET (an enriched-text version of IB-HL containing 217B o200k_base tokens across 983,003 volumes, organized into 1.39B annotated subtopic paragraphs) and the pipeline that produced it. These serve to make the collection easier for machines to parse and for humans to study.

---


### 156. [Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering](https://arxiv.org/abs/2608.19029)

**<font color=#1a73e8>作者：</font>** Pradeep Murugesan, Luoxiao Yang, Xueli Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning. Existing medical QA systems, typically based on single-agent architectures and static retrieval, often lack adaptability, persistent memory, and structured decision-making. This work introduces an adaptive memory and reflection (AMR) agentic system, a multi-agent framework in which specialized agents use dedicated memory and reflection-based feedback to retrieve relevant prior cases and improve subsequent reasoning. Complexity assessment routes questions through solo, collaborative, or escalated workflows, while consensus and ethical overseer modules support reasoning consolidation and output review. Evaluation on MedQA and MedMCQA demonstrates strong performance compared with several baselines. Ablation studies show that combining agent-specific memory, reflection, and external retrieval yields the strongest performance. These findings highlight the potential of structured memory and feedback for developing more trustworthy medical agents. The source code is publicly available at this https URL.

---


### 157. [Counterfactual Contrastive Analysis](https://arxiv.org/abs/2608.19032)

**<font color=#1a73e8>作者：</font>** Yunlong He, Pietro Gori  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Counterfactual Explanations (VCEs) aim to explain image classifiers by generating minimally edited and realistic versions of an input image that change the classifier's prediction. Existing VCE methods are inherently classifier-dependent and therefore susceptible to classifier biases and failure modes, such as sensitivity to shortcut features and calibration errors. In this paper, we propose a classifier-free approach for visual counterfactual generation based on Contrastive Analysis (CA). Given two datasets corresponding to different classes (e.g., healthy and patients), we disentangle the generative factors that are common across the two datasets from those that are salient to each dataset, and generate counterfactual images by swapping only the salient factors. By operating directly on data distributions rather than decision boundaries, our method provides model-agnostic VCEs that are less sensitive to classifier biases. Our approach leverages the high-quality synthesis and well-structured latent space of StyleGAN2. We use the feature space F, instead than the usual W-space, to improve detail preservation. Unlike conventional CA approaches, which typically assume salient factors in only one dataset, we introduce an adapted framework and loss functions for VCE that allow multiple salient factors in each dataset. We evaluate our method on three medical imaging datasets and demonstrate superior counterfactual generation quality compared to existing approaches.

---


### 158. [USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes](https://arxiv.org/abs/2608.19036)

**<font color=#1a73e8>作者：</font>** Li-Heng Chen, Haokai Pang, Chengye Su 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial representation learning for autonomous driving aims to map raw visual signals into structured 3D scene representations, where object-centric bounding boxes and rendering-oriented 3D primitives (\eg, 3D Gaussians) serve as two distinct yet highly complementary levels for scene understanding. Existing methods typically treat dynamic reconstruction and instance-level perception as separate tasks, despite their shared goal of estimating the underlying 3D world state. As a result, dynamic reconstruction is under-constrained while 3D detection lacks geometric grounding. To address this gap, we propose USR-Drive, a unified conditional generative framework that, given only posed multi-view driving videos, jointly recovers dense dynamic geometry and instance-level object layouts within a shared scene representation. Specifically, USR-Drive represents dense Gaussian primitives and sparse 3D bounding boxes as two aligned latent token streams and jointly denoises them with a unified multi-modal diffusion Transformer. Unlike prior paradigms that use boxes as external conditions or predict them with detached modules, USR-Drive treats them as mutually constrained state variables with a Unified Positional Encoding (UPE) that aligns heterogeneous tokens within a shared metric spatiotemporal coordinate. Via such unified representation and generative framework, the two modalities reinforce each other: geometry supplies dense metric evidence for box prediction, while boxes provide instance-level structural priors that help preserve spatial consistency and reduce ambiguity in sequential 3D geometric representation. Our approach successfully delivers state-of-the-art results for both dynamic reconstruction and 3D detection on the nuScenes and VKitti datasets.

---


### 159. [Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery](https://arxiv.org/abs/2608.19047)

**<font color=#1a73e8>作者：</font>** Alizer Wong, Heng Cui, Yi Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Eureka, a task-conditioned Meta-Agent architecture that compiles long-horizon tasks into dynamic obligation graphs with explicit acceptance semantics. During execution, Eureka forms Macro-Agents with specialized state, memory, operators, tools, verifiers, and local topology via receding-horizon planning, architecture promotion, and minimal-sufficient compilation. When bottlenecks recur, cost-benefit-gated evolution updates the local architecture under constraints. Theoretically, we establish results on regret, planning invalidation, amortization, subtree interfaces, serializability, and verification. Experimentally, Eureka completes 170/170 recursive tasks and generates 3,948 certificates with no false acceptances. Active context compresses median input from 9,490 to 4,005 tokens; incremental processing avoids 65.38% recomputation across 12,000 tasks; 16,000 concurrent executions serialize consistently. The same Meta-Agent instantiates a Theory-Discovery Agent and a Math/Conjecture Agent. The former yields structural results in quantum-process and spacetime theory. The latter identifies bottlenecks in Riemann Hypothesis research and advances a positivity certificate for Suzuki's localized Weil quadratic form to 0 < a <= 69/200 = 0.345, reaching ~99.55% of (log 2)/2. These results suggest that scientific-agent capability depends not only on the base model but on whether an architecture can be formed to match the task's cognitive structure.

---


### 160. [Multi-Agent Off-Policy Deep Reinforcement Learning for Smart Campus Coverage](https://arxiv.org/abs/2608.19049)

**<font color=#1a73e8>作者：</font>** Omar Rady, Mohamed Ayman, Ali Arafa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) has recently gained a great attention due to its real-time adaptation and effectiveness in complex optimization problems. This paper investigates the optimal deployment of millimeter-wave (mmWave) base stations (BSs) in a realistic, non-convex campus topology. The optimization problem is NP-hard, due to the non-convex, non-smooth nature of the max-min fairness objective. To overcome these constraints, we formulate the BS placement as a Markov Decision Process (MDP) and systematically benchmark four DRL schemes: a discrete single-agent Deep Q-Network (DQN), a spatially partitioned Multi-Agent DQN, a continuous single-agent Deep Deterministic Policy Gradient (DDPG), and a geographically partitioned multi-agent DDPG framework. Numerical evaluations reveal that the multi-agent DDPG approach substantially outperforms single-agent in dense scenarios. Additionally full coverage is achieved, and a fairness Jain's index of 0.94 is obtained. Finally, the multi-agent demonstrates highly efficient computational convergence of dense scenarios with $400$ users.

---


### 161. [Malformer: A Multi-Modal Malware Detector Using Transformers](https://arxiv.org/abs/2608.19052)

**<font color=#1a73e8>作者：</font>** Samuel Howard, Kshitiz Aryal, Mahmoud Abdelsalam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional malware detection systems that rely on a single representation of malware often fail to identify novel threats. These representations of malware binaries, also known as modalities, do not provide the models with sufficient information to discriminate among all samples. Additionally, individual representations introduce new failure modes, with some modality extraction being dependent upon the success of disassembling. Past works have integrated either additional modalities or more discriminative representations for classification. In this work, we present Malformer, a quadrimodal malware detection model that incorporates text, image, graph, and audio representations of Windows executables. We demonstrate that multimodal transformer fusion can enhance the performance of Windows malware detectors over that of unimodal and bimodal detectors. Malformer employs a combination of two RoBERTa encoders paired with a modified Vision Transformer for image data, WavLM for audio data, and an adaptive loss-weighting scheme to fuse modality-specific representations. Evaluated on a dataset of 201,549 binary samples, Malformer achieved 98.3% accuracy and an F1 score of 0.9833, outperforming both unimodal baselines and bimodal detectors by 4.6-17.6 percentage points. Malformer demonstrates that multimodal fusion provides a promising foundation for countering the growing scale of malware threats, equipping defenders with generalized and resilient detection capabilities.

---


### 162. [Generalized Audio-Driven Synthesis of Precise Drummer Motion](https://arxiv.org/abs/2608.19055)

**<font color=#1a73e8>作者：</font>** Álvaro G. Iñesta, Mattia Ryffel, Amit H. Bermano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Music-driven character animation enables and enhances transformative applications in entertainment and interactive education. However, synthesizing realistic drumming motion from audio remains challenging due to the inherent tension between high-acceleration dynamics and the need for extreme spatial-temporal precision. Existing approaches, often reliant on motion matching or MIDI input, struggle with generalizing to diverse real-world audio. Moreover, the field lacks standardized evaluation metrics capable of distinguishing precise drumming from noisy motion. In this paper, we introduce a generative diffusion framework featuring a dual-objective loss function that decouples skeletal integrity from drumstick precision, thus enabling centimeter-level stick precision without sacrificing natural body dynamics. Additionally, leveraging our own dataset and data augmentation strategy, the model generalizes to non-curated, in-the-wild audio. To rigorously evaluate performance, we propose two novel metrics: an impact-to-target distance to quantify spatial precision and an audio-motion correlation score to assess temporal alignment. Our quantitative analysis and user studies demonstrate that our system generates high-quality motion that is often indistinguishable from ground-truth performances.

---


### 163. [When Two Tracers Disagree: An Investigation of Multimodal Fusion for Clinical PET/CT Segmentation](https://arxiv.org/abs/2608.19063)

**<font color=#1a73e8>作者：</font>** Jack A. Johnson, Bartłomiej W. Papież  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> PSMA and FDG PET/CT visualise complementary biological information in prostate cancer. Combining both tracers could capture heterogeneous tumour phenotypes that may be missed by either alone, yet there is no consensus on effective deep learning architectures for fusing these modalities. We evaluated multimodal image-fusion strategies for automatic whole-body PET/CT lesion segmentation to estimate total tumour burden. Using the public DEEP-PSMA Challenge dataset, we trained tracer-specific 3D nnU-Net baselines and compared (i) early fusion with a single encoder and one decoder (OEOD) or two decoders (OETD), and (ii) intermediate fusion via a dual-encoder cross-attention U-Net (DECA-UNet). Tracer-specific baselines performed strongly (PSMA Dice = 0.93; FDG = 0.81). Fusion yielded mixed results: OEOD produced a combined Dice of 0.90 (on an easier, non-tracer-specific task), whilst the tracer-specific fusion models reached PSMA/FDG = 0.69/0.64 (OETD) and 0.76/0.57 (DECA-UNet). Whilst fusion often provided reasonable PSMA segmentation, FDG performance degraded and no strategy consistently exceeded the single-tracer baselines. Under the evaluated setting, tracer-specific models remain the stronger baseline; clinically useful gains from multimodal fusion will likely require architectures that better preserve tracer specific representations. Our code is available at: this https URL

---


### 164. [Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk](https://arxiv.org/abs/2608.19073)

**<font color=#1a73e8>作者：</font>** Deep Kumar Ganguly, Jan Křetínský  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a robust-optimization identity---a confidence level fixes the radius of a relative-entropy ball of alternative models---but that ball cannot reach catastrophes the nominal deems impossible, precisely what a safe agent must hedge. We instead use an optimal-transport ball and study the coherent risk measure it induces, the Wasserstein entropic value-at-risk. It has a variational dual mirroring the entropic formula (an inverse temperature becomes a transport price), occupies a definite place in the risk hierarchy, and provably accounts for the reachable catastrophes the entropic measure ignores; we verify both dualities numerically. Driving the transport radius by belief entropy then yields a closed-form robust dynamic-programming operator whose caution contracts as the belief sharpens, with a certified safety sandwich and a sharp safety switch.

---


### 165. [SPK: Eliciting Structured Prior Knowledge for Interpretable Out-of-Distribution Detection in Real-Time Object Detection](https://arxiv.org/abs/2608.19080)

**<font color=#1a73e8>作者：</font>** Changshun Wu, Weicheng He, Xiaowei Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detectors often produce over-confident predictions for objects outside their training categories, leading to so-called out-of-distribution (OoD) hallucinations. Existing approaches for detecting or mitigating such hallucinations typically either construct scoring functions directly over learned object detector representations or modify the object detector itself to suppress hallucination emergence. However, the latent priors implicitly encoded in these representations remain largely unexplored and have not been explicitly decoded for OoD detection. To uncover and exploit these latent priors, we propose Structured Prior Knowledge (SPK), a hallucination-oriented framework that explicitly elicits OoD-relevant priors from pretrained object detectors. Specifically, SPK leverages in-distribution data and hallucination-inducing samples as diagnostic supervision to elicit part-level semantic concepts underlying object detector decision-making, rather than using them merely for rejection or object detector adaptation. The elicited semantic priors are further integrated with geometric and contextual priors to form a compact five-dimensional SPK representation for OoD detection. Extensive experiments across diverse object detector architectures and multiple OoD benchmarks demonstrate that SPK achieves state-of-the-art OoD detection. Our findings reveal that pretrained object detectors already encode substantially richer latent knowledge than is typically exploited for OoD detection. More importantly, this knowledge can be explicitly elicited and organized into a compact, structured, and interpretable knowledge space for prediction reliability analysis. This suggests a promising proactive route for improving object detector reliability by explicitly uncovering and leveraging latent priors. Code and data are available at: this https URL

---


### 166. [Does Mapping Non-Maximal Probabilities to GMM Components Matter for S-JEPA Encoder Representations?](https://arxiv.org/abs/2608.19084)

**<font color=#1a73e8>作者：</font>** Wenxuan He, Yunpeng Li, Shan Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> S-JEPA uses soft Gaussian mixture model (GMM) posteriors instead of hard cluster labels to preserve uncertainty. It remains unclear whether the probability values alone are sufficient, or whether it also matters which GMM components receive the non-maximal probabilities. We test this with two matched controls. FIXED-RANDPERM keeps the top-1 component and probability together with the multiset of non-maximal probability values, but reassigns those non-maximal values using a mapping fixed for each physical frame. UNIFORM-TAIL keeps the top-1 component, its probability, and total non-maximal mass but distributes that mass uniformly. Across three independent seeds, REAL SOFT outperforms both controls on two frozen Encoder readouts. It provides better recovery of the original GMM tail and greater accessibility of spectral dynamics over short time scales after controlling for the complete spectrum of the current frame. In two exposure experiments, both readouts improved overall as more frames retained the original mapping. We also descriptively follow one Phase 2 trajectory after the switch to the online GMM. These results show that the numerical probability structure of the soft target does not fully determine the learned Encoder representation. The mapping of non-maximal probabilities to GMM components also matters.

---


### 167. [Detecting Backdoors in Object Detection via Pre-NMS Prediction Distribution Shift](https://arxiv.org/abs/2608.19088)

**<font color=#1a73e8>作者：</font>** Longtian Wang, Zhengyu Zhao, Chenhao Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection models deployed in safety-critical applications remain vulnerable to backdoor attacks that cause targeted misbehaviors when a hidden trigger is present. Existing detection methods either rely on trigger inversion or exploit architecture-specific assumptions, and critically, representative existing methods fail to generalize reliably to scene-level attacks, where a single trigger induces anomalous behavior across all objects in the scene simultaneously. We present DistScan, a backdoor detection framework based on a simple but previously unexploited observation: backdoor injection systematically shifts a model's pre-NMS prediction class distribution away from its training class frequencies, even on clean inputs without any trigger present. DistScan aggregates intermediate class predictions over a clean validation set and flags a model as backdoored if the resulting distribution deviates significantly from the training class frequencies, requiring no model weight access, no trigger knowledge, and no additional training. Extensive experiments on MS-COCO and PASCAL VOC across two architectures and three scene-level attack scenarios demonstrate that DistScan substantially outperforms existing methods, improving average detection accuracy over the best-performing applicable baseline by 27.32 percentage points.

---


### 168. [Pretraining Reusable Inference Across Views with Synthetic Task Priors](https://arxiv.org/abs/2608.19115)

**<font color=#1a73e8>作者：</font>** Jielong Lu, Zhihao Wu, Jiajun Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern pretrained encoders make representations from heterogeneous views increasingly reusable, but the procedure that determines view utility and combines evidence is still relearned for each downstream task. Consequently, knowledge about view relevance, complementarity, reliability, and missingness is repeatedly discarded rather than transferred across tasks. We therefore reformulate multi-view learning as learning a reusable, task-conditioned inference procedure rather than a fixed fusion function. Based on this perspective, we propose SIMPLE, a prior-fitted multi-view in-context learner that predicts query labels by conditioning on a small labeled support set. Since existing real-world datasets cover only a limited range of view configurations and task structures, we construct a controllable synthetic task prior in embedding space. It generates diverse support-query episodes with varying class structures, shared and view-specific factors, representation geometries, cross-view dependencies, reliability levels, missingness patterns, and distribution shifts. A hierarchical inference architecture then performs reasoning within views, across views, and across support and query samples. Experiments on multi-view and multi-omics benchmarks demonstrate that the frozen variant of SIMPLE achieves competitive performance without updating the inference backbone, while lightweight adapter calibration attains leading performance on most evaluated datasets. Together, the results under frozen, one-shot, and missing-view settings support the central hypothesis that multi-view reasoning itself can be pretrained and reused, while lightweight adapter calibration provides task-specific alignment when needed.

---


### 169. [Enhancing EBSD throughput of battery electrode materials using super-resolution generative adversarial networks](https://arxiv.org/abs/2608.19117)

**<font color=#1a73e8>作者：</font>** John Mangum, Andrew Glaws, Francois Usseglio-Viretta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantitative microstructural characterization of Li-ion battery electrode materials using electron backscatter diffraction (EBSD) has been proven as a critical method for optimizing cell performance. However, the inherently slow nature of EBSD can hinder the throughput of analyses needed for statistical representation of a material microstructure being developed. This work demonstrates a machine learning super-resolution framework using a generative adversarial network (SRGAN) to significantly increase EBSD throughput. The SRGAN model was trained on EBSD data of LiNixMnyCozO2 (NMC) cathode particles to computationally enhance low-resolution datasets and its performance is compared against classical interpolation methods across various upscaling factors (2x to 12x). Both qualitative image metrics and quantitative microstructural analysis verified that the SRGAN systematically outperformed classical methods, particularly in preserving small grains and maintaining realistic grain boundaries. We demonstrate that a 5x upscaling factor, corresponding to a 25x speed-up in acquisition time or a 25x larger field of view, is practical while maintaining acceptable accuracy in key metrics like grain size and shape. For instance, at 5x upscaling, relative errors were +5.7%, +8.2%, and -14.6% on grain area-equivalent diameter, grain maximum sphere-inscribed diameter, and grain boundary length, respectively. The SRGAN methodology developed in this work significantly enhances the efficiency of EBSD acquisition for more statistically robust microstructural dataset, enabling EBSD as a high-throughput characterization tool for materials research and industrial process development.

---


### 170. [Discretizing Continuous Time Series for Imputation with Masked Diffusion Training](https://arxiv.org/abs/2608.19119)

**<font color=#1a73e8>作者：</font>** Dongbin Kim, Seungyun Lee, Geonwoo Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series imputation is a crucial area for reliable time series analysis, yet it remains challenging due to the complex temporal dynamics and noise of real-world data. Existing approaches, however, exhibit two limitations: missing and observed values are embedded within the same representation space without explicit structural separation, and continuous diffusion-based methods are trained to predict added noise rather than the original signal. To address these, we propose the Masked Diffusion Time-series Imputation Model (MDTIM), which leverages the training paradigm of masked diffusion model for imputation tasks. The MASK token is structurally orthogonal to valid observations, and the model directly predicts the original values, naturally aligning both the representation and the learning objective with the imputation task. To bridge the gap between discrete masked diffusion and the continuous, ordinal nature of time series, we further introduce Stochastic Discretization, which maps continuous values to ordinal-aware tokens while preserving continuous dynamics. Our experiments on diverse benchmarks confirm that MDTIM achieves superior robustness and scalability, consistently outperforming state-of-the-art deterministic and generative baselines across various missing scenarios.

---


### 171. [PGFS++: Molecular Property Improvement under Synthesis and Diversity Constraints](https://arxiv.org/abs/2608.19121)

**<font color=#1a73e8>作者：</font>** Boqiao Zhang, Godbless James, Sai Krishna Gottipati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving molecular properties, such as drug-likeness or binding affinity, is a recurring task in early-stage drug discovery. However, molecules optimized in an unconstrained chemical space have limited practical value if they cannot be synthesized. Policy Gradient for Forward Synthesis (PGFS) is a synthesis-aware reinforcement learning method for molecular improvement, but its use of reactant embedding prediction makes reactant selection indirect, which, as we show, limits learning effectiveness. We first develop PGFS+, in which reaction templates and second reactants are represented by trainable embedding lookup tables. Combined with a more effective scoring function and RL algorithm, PGFS+ significantly improves the desired property. However, it exposes a reward-hacking failure mode: a powerful reactant search can map diverse input molecules to the same high-reward magnet molecule, improving the reward while collapsing the output diversity. We therefore introduce PGFS++, a synthesis-aware reinforcement learning framework for input-specific molecular improvement. Given an input molecule, PGFS++ treats it as the start of a forward-synthesis trajectory, applies learned reaction templates with compatible in-stock building blocks, and produces a molecule with improved target properties, an explicit synthesis route, and structural similarity to the input. Experiments on molecular improvement tasks show that PGFS++ improves target properties while preserving high output diversity.

---


### 172. [Toward Quantum Advantage in Learning Parities with Structured Noise via Lower Bound Optimization of the Condition Number](https://arxiv.org/abs/2608.19122)

**<font color=#1a73e8>作者：</font>** Yusen Han, Xuelian Li, Juntao Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Learning Parities with Structured Noise (LPSN) can be reduced to solving nonlinear Boolean systems. In quantum computing, such systems are typically transformed into Macaulay linear systems and solved via quantum linear system algorithms, a process severely limited by the condition number. To address this, we propose a novel reduction method for Macaulay linear systems. Under the assumptions of Ding et al., we derive a condition number lower bound incorporating a scaling factor.
This reduction not only guarantees efficient quantum state preparation but also exhibits a distinct advantage regarding the condition number interval relative to the reduced right-hand side vector, thereby reducing the lower bound of the condition number and ultimately optimizing the upper bound on the time complexity of the quantum algorithm for solving Boolean systems.
Furthermore, applying this improved quantum algorithm to LPSN significantly reduces sample complexity by exploiting the Macaulay system's solution structure. We further provide a concrete logical-level quantum resource estimate, demonstrating that the optimized condition number translates directly into a reduction in circuit width, depth, and gate count. Finally, we establish an algorithm selection strategy by systematically comparing quantum and classical approaches across noise pattern adaptability, sample complexity, and time complexity. Results demonstrate that our quantum algorithm exhibits the potential to outperform classical counterparts under specific parameter regimes.

---


### 173. [Leaf Values as Coordinates: Exact Contrastive Explanation for Gradient-Boosted Ensembles](https://arxiv.org/abs/2608.19127)

**<font color=#1a73e8>作者：</font>** Emanuele Luzio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A gradient-boosted ensemble predicts by summing one leaf value per tree. Read
those values as coordinates rather than as intermediate results, and every
instance becomes a point in R^M on which the model acts linearly: the score is
the sum of the coordinates.
This small change of view makes contrastive explanation exact. The difference
between two instances is a vector that is identically zero wherever they share
a leaf, so the gap between a rejected applicant and an accepted one is carried
by a handful of coordinates, each traceable to a real split in a real tree.
Nothing is fitted, sampled, or assumed additive in features -- the additivity
is already there, in the right space.
We build a recourse method on this representation and evaluate it on five
tabular datasets under repeated cross-validation. Its recommendation
reconstructs the model's own decision to 6.2 x 10^-15, so an auditor can
re-check the arithmetic without the model. On the credit datasets it is
Pareto-non-dominated on effort against realism. And when recommendations are
restricted to changes the subject could actually make -- not their age, not a
settled delinquency -- it retains 58% of its validity where the strongest
baseline retains 41%, a distinction the standard evaluation cannot see because
it never asks whether a recommendation can be carried out.

---


### 174. [Beyond Trial Averaging: Anchoring Neural and Visual Representations for Few-Repetition Brain-to-Image Retrieval](https://arxiv.org/abs/2608.19128)

**<font color=#1a73e8>作者：</font>** Zhenyao Cui, Siyuan Kan, Dingkun Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding visual information from brain signals probes neural representations and enables neuro-rehabilitation and dream decoding. Recent brain-to-image retrieval approaches have achieved promising performance, typically by averaging many (up to 80) neural trials per image, requiring repeated stimulus presentation that increases latency, cost, and user burden. When only one or a few repetitions are available, the retrieval accuracy drops sharply. This drop is commonly attributed to query noise because averaging suppresses noise and increases signal stability. However, we find a non-transitive alignment pattern: the low-repetition query signal and the image representation each align with the high-repetition center, but not directly with each other. This pattern shows that query noise is only part of the problem and that gallery placement also affects retrieval. We therefore propose a neural-anchor-based retrieval (NEAR) framework that treats the high-repetition center as an anchor and approaches it from both sides: a denoiser pulls the noisy query toward the true anchor, and a small network predicts each candidate's pseudo anchor from its image and pulls the image toward it. Across four datasets spanning EEG, MEG and fMRI, NEAR consistently improved retrieval in the few-repetition regime. On THINGS-EEG2, it improved 200-way Top-1 accuracy by 5.7 and 9.3 percentage points respectively, when averaging one and four repetitions. By anchoring neural and visual representations, NEAR reduces reliance on repeated acquisition and brings neural retrieval closer to real-world deployment.

---


### 175. [SCORE: Subject Coordinate Recovery for Label-Free Cross-Subject EEG-to-Image Retrieval](https://arxiv.org/abs/2608.19134)

**<font color=#1a73e8>作者：</font>** Zhenyao Cui, Siyuan Kan, Siyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate visual decoding can reveal how the brain represents visual information and recover perceived content from neural signals such as electroencephalography (EEG), with potential for neural communication. However, current EEG-to-image retrieval methods perform far below their within-subject counterparts for new users without labeled calibration, limiting real-world deployment. To understand this gap, we analyze EEG features across subjects and find that different subjects preserve similar relationships among concepts but express them along different coordinate directions. We therefore propose Subject Coordinate Recovery (SCORE), a target label-free framework combining recovery-aware source training with coordinate alignment at deployment. During training, SCORE aligns source subject EEG with a common image space and simulates unseen-subject recovery through source-only episodes. At deployment, with both encoders frozen, SCORE selects reliable EEG-image landmarks through hubness-corrected matching and estimates an orthogonal transformation to recover target EEG coordinates without source data or target labels. In 200-way retrieval on two public benchmarks, SCORE outperforms the unadapted baseline for every target subject and achieves the best overall accuracy. It reaches 53.23%/83.55% and 12.01%/32.16% Top-1/Top-5 on THINGS-EEG2 and Alljoined-1.6M, respectively, surpassing the strongest baselines by 17.45/15.70 and 3.08/4.62 percentage points. Without target labels or encoder updates, SCORE brings brain-based visual decoding closer to robust, practical, low-latency deployment across users.

---


### 176. [Autonomous Cyber Defense in Connected Vehicles: A Multi-Agent Approach to V2X Security](https://arxiv.org/abs/2608.19135)

**<font color=#1a73e8>作者：</font>** Krishna Teja Medam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A connected vehicle has roughly 100 milliseconds to decide whether an incoming Basic Safety Message is real or fabricated. If a false emergency braking alert reaches the planning pipeline in time, the car brakes - a safety failure triggered by a security failure. Existing intrusion detection systems are not designed to handle that coupling. They operate per vehicle, per message, with static rules - blind to attack patterns that only emerge across a fleet or over time, and blind to the fundamental tension between dropping a suspicious message and dropping a real emergency alert. We propose a three-tier multi-agent architecture that treats this timing constraint as a hard design requirement, not a performance target. At the vehicle level, an onboard agent classifies each incoming V2X message into one of four actions - Accept, Drop, Quarantine, or Escalate - within a 10-millisecond budget, deliberately biased toward Escalate when uncertain, passing ambiguous cases to the roadside edge agent rather than risking a dropped legitimate alert. The edge agent operates across a roadside unit zone with a 50-millisecond budget, fusing threat assessments from multiple vehicles and resolving safety-security conflicts using complementary sensor observations. The cloud tier refines detection models through Byzantine fault-tolerant federated learning and redistributes updated weights to the fleet. Every timing constraint derives directly from the 100-millisecond Basic Safety Message cycles mandated by SAE J2735 and ETSI EN 302 637-2. No existing framework simultaneously assigns standards-grounded latency budgets to all three deployment tiers while treating safety-security conflict resolution as a first-class design constraint. Remaining open problems - adversarial poisoning at the edge and the absence of regulatory frameworks for autonomous security response - are discussed as future work.

---


### 177. [Bridge Graphical Models: Coupling, Projection, and Current-Preserving Dynamics for Generative Modeling](https://arxiv.org/abs/2608.19144)

**<font color=#1a73e8>作者：</font>** Tiantian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time generative models are often built from endpoint-conditioned bridges, but generation requires a different object: a non-anticipative Markov decoder that only observes the current state and time. We identify this bridge-to-decoder compression as a structural bottleneck shared by diffusion models, flow matching, rectified flow, Schrödinger bridges, and field-based generative models. We introduce the \emph{Markovization gap}, the time-integrated conditional variance of the bridge velocity given the Markov state. It is the MMSE of predicting endpoint-conditioned motion from the information available to a sampler, and it measures an irreducible loss incurred before any neural network is trained. To make this bottleneck comparable across model families, we define \emph{Bridge Graphical Models} (BGMs), which separate endpoint coupling, bridge law, Markovian projection, and current-preserving dynamics representation as independent design choices. The same formalism also represents Poisson and electrostatic models as field-line bridge kernels with a corresponding field-line Markovization gap. Across synthetic, latent, and pixel-space pilots on CIFAR-10 and Fashion-MNIST, a feature-space proxy gap estimated in minutes before training ranks design choices in the same direction as downstream training loss and FID under fixed architecture, bridge, sampler, and compute. These results support the Markovization gap as a pre-training diagnostic for bridge and coupling design.

---


### 178. [Trade-offs in Data Color Palette Design Tools](https://arxiv.org/abs/2608.19148)

**<font color=#1a73e8>作者：</font>** Shiyi He, Andrew M McNutt  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designing a color palette for data requires designers to balance multiple constraints, including accessibility and aesthetics. Color palette tools support this process through features including direct manipulation, automated palette generation and evaluation, previews, and so on. Despite their prominence, relatively little is known about how these different mechanisms shape design across contexts. We conducted an exploratory think-aloud crowd work study with 40 self-identified designers. Each participant used one of four palette tools selected to span different interaction modalities to complete a series of accessibility- and aesthetics-oriented design tasks. We observed two preliminary patterns. First, tool differences were more pronounced in accessibility-constrained tasks. Second, even when accessibility was not explicitly required, some tools produced more accessibility-friendly palettes and prompted more accessibility-oriented thinking. In this tool genre, then, system design shapes outcomes both via built-in functionality, as well as by directing designers' attention toward particular constraints and design considerations.

---


### 179. [Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions](https://arxiv.org/abs/2608.19151)

**<font color=#1a73e8>作者：</font>** Tomasz R. Bielecki, Thibaut Mastrolia, Haoze Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting. Due to the path dependence of the memory of the Hawkes intensity, this problem does not fall within classical stochastic control theory outside particular Markovian kernels. We first develop a finite-dimensional Markovianization procedure and algorithm to approximate multivariate Hawkes processes with mixtures of exponential kernels. We prove the convergence of the Markovianized approximation of the Hawkes process, its intensity, and the value of the problem to the original non-Markovian processes and the value of the primal problem. We then formulate continuous-time deterministic policy gradient learning on the Markovianized approximation of the problem, called Hawkes-CT DDPG. We propose a model-free algorithm to solve the non-Markovian Hawkes-driven optimization by observing only the event times of the process, the realization of the solution to the SDE, and a chosen set of decay filters, while the Hawkes kernel coefficients remain unknown. We compare our continuous time reinforcement learning Hawkes-CT DDPG method with discrete time reinforcement learning techniques under three different types of kernels: simple exponential, Erlang, and power-law kernels.

---


### 180. [FedGuard-DC: Privacy-Preserving Federated Load Forecasting and Cyber-Attack Detection for Data-Center Loads in Transmission Systems](https://arxiv.org/abs/2608.19155)

**<font color=#1a73e8>作者：</font>** Md Kibria Saroare, Md Rubel Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of large data-center (DC) loads is creating new challenges for power-system visibility, privacy, and cyber-physical security. System operators need accurate short-term information about these fast-varying loads, while DC operators may avoid sharing raw megawatt measurements because they can reveal sensitive workload and utilization patterns. This paper presents FedGuard-DC, a federated learning (FL) framework for privacy-preserving DC load forecasting and local false-data-injection attack (FDIA) detection. Each DC trains a dual-head model on its own measurements, where a shared encoder supports both a forecasting head and a reconstruction head. A calibrated anomaly score combines forecast residual and reconstruction error to detect corrupted measurements locally. Raw measurements and absolute MW demand remain at each DC, while only model updates are shared with the global controller. Optional differential privacy and robust trimmed-mean aggregation are included to evaluate privacy-utility behavior and poisoned-client resilience. The framework is validated using EMT simulation data from four large DC loads rated between 150 and 350 MW integrated into the IEEE 39-bus New England system. Results show a 0.5 s-ahead normalized forecast RMSE of 0.023-0.038 pu, compared with 0.32-0.34 pu for persistence. FedGuard-DC detects FDIA with ROC-AUC of 0.979, F1 = 0.930, and precision of 0.988, while robust aggregation reduces the poisoned-client RMSE impact from 0.042 to 0.035 pu.

---


### 181. [Lévy Attention: Single-Pass Predictive Uncertainty for Continuous-Time Attention](https://arxiv.org/abs/2608.19171)

**<font color=#1a73e8>作者：</font>** Sotirios P. Chatzis, Loukas Papadoulas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep models for irregularly-sampled time series answer queries at arbitrary continuous timestamps, yet report nothing about how far each answer should be trusted. We show the attention layer itself can close that gap: with the right stochastic formulation, the pass that makes each prediction also reports, in closed form and at no extra cost, how far it should be trusted. We introduce Lévy Attention, a cross-attention operator whose output is a stochastic integral against an inhomogeneous Poisson random measure: query-key compatibilities assemble an intensity over a continuous (time x channel) index space, the measure scatters atoms under it, and the output averages an interpolated value field at those atoms. In expectation it reduces to a mollified cosine-kernel attention, so it replaces a softmax layer and trains with exact gradients.
What softmax discards, the Poisson construction preserves in closed form: the evidence $\Lambda_q$ (total compatibility mass) and the disagreement $\mathrm{tr}\,\Sigma_V(q)$ (value spread). An exact variance identity makes their combination $\hat\sigma(q)=\sqrt{\mathrm{tr}\,\Sigma_V(q)\,\varphi(\Lambda_q)}$ the root-mean-square deviation of the sampled operator, emitted by the deterministic pass with no trained head.
Empirically, disagreement carries the signal, while the evidence factor swings from uninformative on dense data to strongly informative on sparse. On t-PatchGNN the operator swap costs at most 5.6% accuracy against a matched control and nothing on the sparsest dataset. The free disagreement signal improves on 20-pass MC dropout across matched five-seed suites, and $\hat\sigma$ scales a calibrated Gaussian whose zero-sample CRPS beats a fifty-draw sampler; a split-conformal wrapper reaches nominal coverage at every level, and one pass ranks 3,383 unseen patients by trust in 1.4 seconds.

---


### 182. [Image-Guided Pavement Defect Recognition in GPR Data with novel 3D Deep Learning Architecture](https://arxiv.org/abs/2608.19177)

**<font color=#1a73e8>作者：</font>** Yuandong Pan, Linjun Lu, Mudan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ground Penetrating Radar (GPR) is a widely adopted non-destructive sensing technology for subsurface inspection in civil and transportation engineering. Despite its potential for pavement condition assessment, the large-scale application of GPR in automated inspection has two key challenges: the scarcity of annotated real-world datasets and the lack of deep learning models designed for the unique characteristics of 3-Dimensional (3D) GPR data. This study addresses these limitations by firstly introducing a cost-effective data preparation pipeline that integrates orthomosaic Red Green Blue (RGB) imagery with 3D GPR scans to generate annotated 3D GPR datasets. The proposed method uses the aligned segments of RGB and GPR data, using pavement surface images as a reference to transfer labels of surface-visible defects to corresponding GPR segments, enabling efficient large-scale annotation in a real-world dataset collected on a highway section under operation. In addition to the dataset contribution, we propose a specialised 3D Convolutional Neural Network (CNN) architecture incorporating residual connections, mixed convolutional kernel sizes, and both depthwise and channelwise attention mechanisms to enhance feature representation and defect classification. The model is evaluated on binary classification tasks for detecting patch and crack defects in pavement structures. Experimental results demonstrate that the proposed network outperforms baseline architectures across multiple evaluation metrics. Ablation studies further confirm the effectiveness of the designed architectural components. This work contributes a scalable and practical method for real-world dataset generation, along with a novel deep learning framework.

---


### 183. [SiNMULI: Novel Signed Network Approach for Malicious URL Identification](https://arxiv.org/abs/2608.19190)

**<font color=#1a73e8>作者：</font>** Avijit Gayen, Sayan Mondal, Angshuman Jana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In today's era of rapid advancements in artificial intelligence, computer security and online safeguarding measures have undergone significant improvements. However, malicious websites continue to facilitate the spread of phishing schemes, fraudulent activities and unsolicited communications. Conventional methodologies in machine learning, deep learning and counterfeit website detection predominantly depend on static data analysis, which frequently proves ineffective against the evolving nature of malicious online entities. In response to these challenges, in this work, we propose a signed network-based approach for malicious URL identification, SiNMULI. We introduce an innovative framework that conceptualises the identification of harmful URLs as a signed network-based binary classification problem strongly rooted in the fundamental principles of social network analysis and social balance theory. In this approach, a signed network is constructed based on the backlinks, i.e., external hyperlinks of URLs, wherein each node symbolises a URL and the hyperlinks function as signed edges. Utilising a balance-theoretic inference mechanism, our methodology propagates edge signs and classifies unlabeled domains by employing a 51% majority rule across incoming links. Experimental results on this real-world dataset demonstrate that SiNMULI achieves 99.89% accuracy, 99.62% precision, and 99.80% F1-score, outperforming traditional ML and deep learning baseline models. Beyond high accuracy, SiNMULI offers interpretability, resilience against adversarial obfuscation, and independence from training data, making it a lightweight and scalable solution for real-world cyber defence.

---


### 184. [The Structured Totient Preimage Problem: Reconstruction, Collisions, and Cryptographic Implications](https://arxiv.org/abs/2608.19191)

**<font color=#1a73e8>作者：</font>** Luis Adrián Lizama-Pérez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We define and study the Structured Totient Preimage (STP) problem as a restricted reconstruction relation with a direct cryptographic motivation. Let $p_1,\ldots,p_k$ be distinct primes of the same bit length and reveal only $x=\prod_{i=1}^k(p_i-1)$. Given $(x,\lambda,k)$, STP asks for any set of $k$ distinct $\lambda$-bit primes satisfying this product. The relation is efficiently verifiable, but its reconstruction complexity is not known. We establish three concrete results. First, for factored $x$ we derive the exact number of ordered exponent allocations and a bound showing that direct reconstruction is polynomial for fixed $k$ when $\Omega(x)=O(\log\lambda)$; this rules out that regime as a basis for a strong hardness claim. Second, we give exhaustive algorithms for reconstruction and collision analysis. Third, we exhaustively evaluate 28 parameter pairs, with $2\leq k\leq5$, up to $\lambda=16$ for pairs and 4,588,935 prime sets in the largest census. The data quantify non-injectivity through collision participation, maximum multiplicity, and conditional ambiguity in bits. These results isolate STP from general inverse-totient computation and motivate a Structured Totient Preimage Assumption for explicitly growing parameter families. Under such an assumption, STP becomes a candidate preimage-resistant relation whose implications for commitments, proofs of knowledge of multiplicative witnesses, and authentication can be stated precisely. The paper establishes the computational foundation and parameter constraints for those constructions; it does not claim a security reduction or post-quantum hardness.

---


> [!TIP]
> 当前位于：**151-184**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-184**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
