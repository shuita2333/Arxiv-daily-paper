# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 51. [Diffusion Models, Denoiser Architecture and Creativity](https://arxiv.org/abs/2605.16415)

**<font color=#1a73e8>作者：</font>** Itamar Levine, Yair Weiss  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The creativity of diffusion models refers to their ability to generate highly realistic images that are different from their training data. Creativity is somewhat surprising since it is known that if the denoiser used in the diffusion model is the Bayes optimal denoiser for a given training set, then the model will simply copy the training samples. In this paper we present empirical and theoretical results that suggest that creativity in diffusion models is due to an interaction between the denoiser architecture and the target distribution. Theoretically, we give explicit forms for the distribution of generated samples as a function of the target distribution and the denoiser architecture for three different denoiser architectures (linear, polynomial, bottleneck). Empirically, we show that small changes in the popular UNET denoiser architecture leads to very different forms of creativity, and these small changes often yield samples that are highly nonrealistic. Taken together, our results show that diffusion models will only be successful if the inductive bias of the denoiser architecture is in strong alignment with the true target distribution.

---


### 52. [Video Reconstruction using Diffusion-based Image-to-Video Generation with Trajectory Guidance](https://arxiv.org/abs/2605.16420)

**<font color=#1a73e8>作者：</font>** Stelio Bompai, Ioannis Kontopoulos, Giannis Spiliopoulos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of reconstructing missing or dropped frames in top-down drone video of autonomous surface vehicles performing structured maritime manoeuvres. We propose a pipeline that converts raw GPS telemetry and a single reference frame into a trajectory-guided video sequence using a pre-trained image-to-video diffusion model, requiring no domain-specific fine-tuning. GPS coordinates from onboard telemetry logs are projected into image space via an equirectangular mapping, producing per-vessel motion cues that condition the SG-I2V diffusion model. The generated frames are evaluated against ground-truth video using perceptual, temporal and trajectory-based metrics, and benchmarked against optical flow extrapolation and RIFE interpolation baselines. SG-I2V produces the most naturally appearing frames among all methods (BRISQUE 25.52, closest to ground-truth 23.64), the most realistic motion magnitude (temporal smoothness 1.14 vs. ground truth 1.42), and the strongest GPS trajectory adherence (9.31px vs. 28.70px for ground-truth, the latter reflecting approximate temporal alignment between footage and GPS logs rather than generation error), demonstrating that trajectory-guided diffusion synthesis is a viable approach to maritime video reconstruction under challenging low-texture, small-object conditions.

---


### 53. [EAGT: Echocardiography Augmentation for Generalisability and Transferability](https://arxiv.org/abs/2605.16427)

**<font color=#1a73e8>作者：</font>** Soroush Elyasi, Sara Adibzadeh, Nasim Dadashi Serej 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for echocardiography segmentation often struggle to generalise across institutions, scanners, and patient populations, where collecting large, consistently annotated datasets is infeasible. Data augmentation is widely used to improve the robustness of deep learning models; however, its role in enhancing cross-dataset generalisability in echocardiography remains insufficiently understood. This study presents a large-scale multi-dataset evaluation of 29 data augmentation techniques and their pairwise combinations for 2D left ventricular segmentation using a U-Net trained on Unity, CAMUS, and EchoNet Dynamic datasets. Each augmentation was explored under several hyperparameter settings and assessed through repeated runs using Dice and IoU in both in-domain and cross-dataset scenarios, with statistical significance quantified via independent t-tests. Results show that anatomically plausible geometric transformations, particularly affine, shift-scale-rotate, perspective, and random horizontal flip, substantially improve cross-dataset performance, whereas aggressive intensity- or artefact-based augmentations often degrade generalisability. Pairwise augmentation combinations outperform individual augmentations and show that moderate flip-centric combinations, especially random horizontal flip with affine, yield consistent gains across most transfer scenarios. These findings provide empirically grounded guidance for designing augmentation policies that enhance the robustness and transferability of echocardiography segmentation models.

---


### 54. [QuantFPFlow: Quantum Amplitude Estimation for Fokker--Planck Policy Optimisation in Continuous Reinforcement Learning](https://arxiv.org/abs/2605.16429)

**<font color=#1a73e8>作者：</font>** Abraham Itzhak Weinberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce \textbf{QuantFPFlow}, a reinforcement learning framework that integrates quantum amplitude estimation into the Fokker--Planck~(FP) formulation of stochastic policy optimisation. Classical continuous-space RL agents must estimate the FP partition function $Z = \int e^{-V(\mathbf{x})/D}\,d\mathbf{x}$ at cost $\calO(1/\varepsilon^{2})$; QuantFPFlow replaces this with a Grover-amplified amplitude estimator achieving $\calO(1/\varepsilon)$ -- a provable quadratic speedup. While the full quantum acceleration requires fault-tolerant hardware, the quantum-inspired classical simulation demonstrated here already exhibits the $\calO(1/\varepsilon)$ algorithmic structure.
The estimated stationary distribution $\rhostar$ drives a theoretically grounded exploration bonus $\Raug = \Renv + \alpha\log(1/\rhostar(s))$. This bonus steers the agent toward globally optimal regions of multimodal reward landscapes while simultaneously constraining policy variance through FP diffusion matching.
On a continuous-control task specifically designed to expose local-optima failure, QuantFPFlow achieves mean reward $1{,}295.7 \pm 423.2$ versus $1{,}284.0 \pm 474.0$ for Soft Actor-Critic~(SAC), while discovering the global optimum \textbf{10.4\,\% more frequently} (33.9\,\% vs.\ 30.7\,\%). Policy entropy remains near $H(\pi)\approx 6.5$\,nats throughout training, whereas SAC collapses to $1.5$\,nats, confirming that FP diffusion matching actively prevents premature convergence. Dimensionality experiments further show computational scaling of $\calO(d^{0.35})$ for QuantFPFlow versus $\calO(d^{0.76})$ for classical FP estimation.

---


### 55. [Edge-AI-Driven Learning-to-Rank for Decentralized Task Allocation in Circular Smart Manufacturing](https://arxiv.org/abs/2605.16433)

**<font color=#1a73e8>作者：</font>** Mohammadhossein Ghahramani, Yan Qiao, Mengchu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task allocation in smart manufacturing systems needs to operate under decentralized decision-making, dynamic workloads, and shared resource constraints. In circular manufacturing settings, these challenges are further intensified by the need to balance operational efficiency with resource and energy sustainability. While learning-based approaches have been explored, many focus on predicting absolute performance metrics that do not necessarily translate into improved allocation outcomes, since decentralized assignment is governed by the relative ordering of candidate machines. This work proposes an Edge-AI-driven decentralized task allocation framework based on ranking-aware negotiation, where lightweight decision intelligence is embedded at the machine level to enable low-latency coordination without centralized control. The framework is developed progressively: a resource-aware heuristic first establishes the decentralized bidding structure, an Edge-AI-based regression model then provides learned local bid approximation, and a ranking-aware formulation finally reshapes the learning objective to align with the ordering-based nature of winner selection. Each machine evaluates incoming tasks using local information, including processing capability, queue state, and resource contention. The framework is evaluated via discrete-event simulation under high-load and tight-deadline scenarios using delay, deadline violations, throughput, and energy consumption. Results show improved delay and deadline adherence under high load, and enhanced energy efficiency under tighter constraints, leading to more resource-efficient operation aligned with circular manufacturing objectives. These findings demonstrate that aligning learning objectives with decentralized decision structures is critical for effective negotiation-driven task allocation.

---


### 56. [GPU-Accelerated Deep Learning for Heatwave Prediction and Urban Heat Risk Assessment](https://arxiv.org/abs/2605.16435)

**<font color=#1a73e8>作者：</font>** Adis Alihodžić  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heatwaves are an important problem in cities, and climate change makes this problem more difficult. In this paper, we present a GPU-based deep learning framework for next-day prediction of urban thermal conditions and for heat risk assessment. The study was carried out in Sarajevo by using MODIS land surface temperature data and Open-Meteo forecast data. We tested several models, including convolutional models and spatiotemporal models. Among them, ConvLSTM with a mixed loss function gave the best results. The obtained values were MAE = 0.2293, RMSE = 0.3089, and R2 = 0.8877. The experiments also showed that results can be improved by using longer temporal series and additional meteorological variables. Since the framework was implemented on a GPU and trained with mixed precision, the execution time was reduced. Based on the predicted temperature fields, it was also possible to combine hazard information with exposure and vulnerability data in order to generate city heat risk maps. The proposed framework can be used as a practical basis for city heat analysis.

---


### 57. [Byzantine-Resilient Federated Learning via QUBO-Based Client Selection on Quantum Annealers](https://arxiv.org/abs/2605.16438)

**<font color=#1a73e8>作者：</font>** Andras Ferenczi, Sutapa Samanta, Dagen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) trains a global model across decentralized clients while preserving data privacy, but at scale it is vulnerable to malicious updates. Byzantine-resilient aggregation methods such as MultiKrum score gradients against their nearest neighbors and can miss malicious updates that preserve the statistical properties of honest ones. We propose a quantum annealing approach that reformulates client selection as a Quadratic Unconstrained Binary Optimization (QUBO) problem, encoding pairwise distances into a cost function solved by quantum annealers (QA). Unlike MultiKrum's greedy per-client scoring, the QUBO formulation jointly optimizes over all subsets to find the mutually closest group of $m$ clients. At small scale (15 clients), QUBO outperforms MultiKrum on the most challenging Byzantine attacks: e.g., Advanced LIE is detected with 95.11% accuracy versus 81.33% on MNIST and 97.78% versus 75.56% on CIFAR-10. QUBO fares poorly on simpler attacks where MultiKrum excels, so the two methods are complementary. QUBO quality also degrades as the number of clients grows. To address this, we introduce a MultiSignal ensemble that uses a dual-feature routing gate based on Euclidean and cosine Krum score gaps to classify attacks into four regimes and routes evasion attacks to a suspicion-penalized QUBO with agreement voting. At 100 clients on MNIST, MultiSignal achieves 95.3% average detection accuracy versus 91.8% for classical MultiKrum, with the largest gains on Sparse Lie (72.0% to 95.2%, +23.2 points) and Advanced Lie (80.4% to 85.2%, +4.8 points). These results show that QUBO-based quantum annealing with MultiSignal is a principled and scalable defense against the most challenging Byzantine strategies in federated learning.

---


### 58. [Semantic Smoothing via Novel View Synthesis for Robust SAR Image Classification](https://arxiv.org/abs/2605.16440)

**<font color=#1a73e8>作者：</font>** Daniel Brignac, Fengwei Tian, Banafsheh Latibari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are vulnerable to adversarial perturbations, limiting deployment in safety-critical applications such as synthetic aperture radar (SAR) automatic target recognition (ATR). Randomized smoothing improves robustness by averaging predictions over noisy inputs, but isotropic noise often fails to preserve the semantic structure of SAR imagery. We propose semantic smoothing, a defense that replaces noised-based perturbations with structured randomized transformations generated by a novel view synthesis model. For SAR, we condition on acquisition geometry to synthesize multiple plausible radar views. Predictions across generated randomized views are aggregated to form a robust classifier. Experiments show that semantic smoothing improves robustness against standard attacks, such as FGSM and PGD, and SAR-specific attacks, such as OTSA and SMGAA, while also increasing clean classification accuracy. These results demonstrate that randomized smoothing via semantically preserving geometric transformations is a promising alternative to isotropic noise for adversarial defense in structured sensing domains.

---


### 59. [DeepArrhythmia: Segment-Contextualized ECG Arrhythmia Classification via Selective Evidence Acquisition](https://arxiv.org/abs/2605.16441)

**<font color=#1a73e8>作者：</font>** Jiahui Li, Ruili Fang, Zishuai Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Beat-level Electrocardiography (ECG) arrhythmia detection aims to assign an arrhythmia class to each beat in a recording, yet many existing systems treat beats as isolated local instances. This is limiting because beat labels often depend on multi-beat rhythm context, including timing, compensatory pauses, and beat-to-beat morphological consistency. We present DeepArrhythmia, a tool-grounded multimodal framework for segment-contextualized beat-level ECG arrhythmia classification. Given a multi-beat ECG segment, DeepArrhythmia combines the raw ECG signal and a rendered waveform image, localizes R peaks to identify beat instances, and produces structured beat-level predictions. The framework decouples physiological measurement from evidence integration using specialized tools for beat localization, numerical rhythm--morphology extraction, and morphology-focused textual analysis. DeepArrhythmia uses segment-level confidence to route between minimal and rich evidence states, since richer physiological evidence is not uniformly useful. This agentic design integrates rhythm context, explicit physiological grounding, and selective evidence acquisition for decision making.

---


### 60. [Two-Valued Symmetric Circulant Matrices: Applications in Deep Learning](https://arxiv.org/abs/2605.16443)

**<font color=#1a73e8>作者：</font>** Jayakrishna Amathi, Venkata Prasanth Yanambaka, Saraju P. Mohanty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the success of deep neural networks in vision, medical diagnosis, and IoT scenarios, their deployment on resource-limited platforms poses serious challenges due to their high storage requirements, computational complexity, and large footprint. In particular, fully connected layers require a large number of weights, making it difficult for edge devices to accommodate them. To overcome these challenges associated with limited platforms, this paper proposes the Two-Valued Symmetric Circulant Matrix (TVSCM), a very sparse architecture that employs just two weights per layer to keep it circulant and symmetric. The extreme form of structured sparse architecture provides negligible storage costs compared to traditional full-weight storage. Instead of hardware and additional stages of other traditional sparse learning techniques, such as low-rank approximation and pruning approaches, this architecture provides an extreme form of sparsity, achieving very minimal storage requirements. The simulation study demonstrates more than 80$\times$ reduction in model parameters, reducing parameters from 623,290 to 7,852 on MNIST and from 24,709 to 942 on the MIT-BIH arrhythmia dataset, while maintaining comparable accuracy from 97.6% to 93.5% on MNIST and from 97.6% to 93.1% on MIT-BIH. Due to its minimal architectural requirements and very low power consumption, this architecture would be ideal for edge computing platforms, tiny-ML platforms, IoMT systems, and battery-powered systems.

---


### 61. [Diffusion Attention Expert Model for Predicting and Semi-automatic Localizing STAS in Lung Cancer Histopathological Images](https://arxiv.org/abs/2605.16444)

**<font color=#1a73e8>作者：</font>** Liangrui Pan, Jiadi Luo, Yuxuan Xiao 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate intraoperative and postoperative diagnosis of spread through air spaces (STAS) is essential for guiding surgical decisions and postoperative management in lung cancer. However, histopathological assessment is labor-intensive and is prone to missed or incorrect diagnoses. We propose a Diffusion Attention Expert Model (DAEM) to detect STAS in frozen sections (FSs) and paraffin sections (PSs). Its diffusion attention expert module leverages full attention aggregation to learn multi-scale features from histopathological images, while a dual-branch architecture strengthens multi-scale feature representation. On an internal dataset, DAEM achieves AUCs of 0.8946 for FSs and 0.9112 for PSs. Validation on external multi-center datasets from eight institutions demonstrates strong generalizability and interpretability. Using tumor microenvironment (TME) features in PSs, we further enable semi-automatic measurement of STAS location and its distance from the primary tumor. Several quantitative TME metrics are identified as potential biomarkers for STAS, including micropapillary-type STAS. Overall, DAEM offers a clinically actionable framework for STAS assessment by enabling accurate and interpretable detection on FSs and PSs, supporting postoperative risk stratification through quantitative TME-based analysis.

---


### 62. [Avoiding Structural Failure Modes in Tabular Fair SSL: Online Primal-Dual Allocation under Confidence Gating](https://arxiv.org/abs/2605.16446)

**<font color=#1a73e8>作者：</font>** Hangchun Liang, Changchun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning (SSL) enables prediction with limited labels, but high-stakes tabular applications (medical, credit, recidivism) require statistical fairness guarantees. We identify a structural conflict in tabular fair SSL through a diagnostic stress test: under confidence-gated pseudo-labeling, moment-matching fairness regularizers can trigger two failure modes -- Masking Collapse (fairness erodes confidence, starving pseudo-labels) and Trivial Saturation (drift to constant predictors). We propose Online Primal-Dual Allocation (OPDA), an online controller that schedules fairness and entropy-based stability penalties using violation, risk, and pseudo-label health signals, avoiding per-dataset selection of a fixed fairness weight within this diagnostic regime. On the evaluated tabular benchmarks (Adult, ACSIncome, COMPAS), OPDA mitigates the degenerate regimes observed under static weighting and simple single-signal adaptive baselines. On Adult and COMPAS, it yields non-degenerate operating points competitive with the empirical static-$\lambda$ frontier; on ACSIncome, it preserves utility with a wider fairness-utility spread. Relative to OPDA-lite, the full controller mainly shifts the operating point toward higher utility on ACSIncome, while Adult highlights the fairness-utility trade-off between the two variants. These results position OPDA as a calibration-free controller for non-degenerate operating points in tabular fair SSL without per-dataset tuning.

---


### 63. [Nested Spatio-Temporal Time Series Forecasting](https://arxiv.org/abs/2605.16447)

**<font color=#1a73e8>作者：</font>** Yinghao Ai, Yukai Zhou, Ruoxi Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal forecasting is critical for real-world applications like traffic management, yet capturing reliable interactions remains challenging under noisy and non-stationary conditions. Existing methods primarily rely on historical spatial priors, often failing to account for evolving temporal correlations and suffering from systematic errors. In this work, we propose a nested forecasting framework that couples future macro-level regional trends with micro-level historical observations, enabling top-down guidance from abstract future representations for fine-grained forecasting. Specifically, we employ a spectral clustering-based approach to construct semantically coherent regions, providing both theoretical and empirical evidence that this representation effectively filters systematic noise while preserving essential trends. Building on this, we develop a progressive coarse-to-fine predictor to integrate these representative features into the inference process. This enables the model to leverage trend predictions to anticipate dynamic anomalies, such as periodic offsets, in advance. Furthermore, extensive experiments on multiple high-dimensional datasets demonstrate that our method consistently outperforms state-of-the-art baselines, validating the effectiveness of future macro-guided nested forecasting.

---


### 64. [PESD-TSF: A Period-Aware and Explicit Structured Decomposition Framework for Long-Term Time Series Forecasting](https://arxiv.org/abs/2605.16449)

**<font color=#1a73e8>作者：</font>** Hua Wang, Xianhao Jiao, Fan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep forecasting models often suffer from attenuated periodic perception and entangled trend-noise representations as network depth increases. Moreover, the widely adopted channel-independent paradigm, while improving training stability, disrupts intrinsic dynamic coordination among variables, hindering the modeling of cross-variable consistency in multivariate time series. To address these issues, we propose PESD-TSF, a physics-inspired structured decomposition framework for long-term time series forecasting that jointly emphasizes interpretability and predictive accuracy. PESD-TSF introduces three key designs. First, a Multiplicative Periodic Gating mechanism incorporates continuous-time priors to dynamically modulate signal amplitudes, preserving periodic structures across deep layers. Second, a multi-scale structured encoder integrates detrended attention with hierarchical sampling to explicitly decouple long-term trends from high-frequency variations while retaining fine-grained temporal semantics. Third, to recover disrupted inter-variable dependencies, we propose Cross-Scale Collaborative Attention (CSCA) together with an RLC regularization scheme, which reconstructs global inter-variable topology in deep feature spaces and enforces physically consistent collaboration through orthogonality and consistency constraints. Extensive experiments on benchmark datasets from multiple domains demonstrate that PESD-TSF consistently achieves state-of-the-art performance, with particularly strong gains on multivariate forecasting tasks involving complex inter-variable coupling, highlighting its superior structural modeling capability and generalization.

---


### 65. [Physics-Guided Geometric Diffusion for Macro Placement Generation](https://arxiv.org/abs/2605.16451)

**<font color=#1a73e8>作者：</font>** Jongho Yoon, Jinsung Jeon, Seokhyeong Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Macro placement is a pivotal stage in VLSI physical design, fundamentally determining the overall chip performance. Recent data-driven placement methods have demonstrated significant potential, yet they often struggle to handle sequential dependencies and to balance topological connectivity with physical constraints. To bridge this gap, we propose MacroDiff+, a physics-guided geometric diffusion framework. Specifically, we design a dual-domain denoising architecture that couples topological connectivity encoded by heterogeneous GNNs with global geometric context modeled by a Transformer. Furthermore, we introduce Physics-Guided Sampling, an inference strategy that actively steers the generation using explicit gradients to ensure both statistical plausibility and physical validity. On the ISPD2005 MMS benchmarks, MacroDiff+ outperforms state-of-the-art baselines with a 6.1-6.2% reduction in wirelength. Notably, it exhibits superior stability and scalability on large-scale designs where prior methods fail to converge. The source code is available at this https URL.

---


### 66. [QuChaTeR: A Hybrid Quantum-Chaotic Temporal Framework for Earthquake Prediction](https://arxiv.org/abs/2605.16454)

**<font color=#1a73e8>作者：</font>** Emir Kaan Özdemir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Seismic prediction remains challenging due to the highly nonlinear and chaotic dynamics of earthquake signals. While classical deep learning models such as LSTMs and CNNs capture local temporal features, and quantum models offer richer state representations, their integration with chaos-driven mechanisms is underexplored. We introduce QuChaTeR, a hybrid architecture that combines wavelet-based preprocessing, chaotic maps, and variational quantum circuits with recurrent structures to enhance temporal feature extraction. Implemented in PyTorch and PennyLane, QuChaTeR is benchmarked against classical (LSTM, GRU, RNN, 1D-CNN, Reservoir Computing) and quantum-inspired (Quantum LSTM) baselines. On real-world seismic datasets, QuChaTeR consistently converges faster and achieves superior performance across multiple evaluation criteria. Despite promising results, scalability and quantum hardware limitations remain challenges. Overall, this work demonstrates how quantum-chaotic hybridization provides a practical pathway toward more accurate and robust earthquake prediction.

---


### 67. [Conservative AI for Safety-Sensitive Medical Image Restoration: Residual-Bounded CT-CTA Enhancement for Intracranial Aneurysm-Relevant Signal Recovery](https://arxiv.org/abs/2605.16458)

**<font color=#1a73e8>作者：</font>** Weijun Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration models are increasingly applied to degraded medical scans, but in safety-sensitive settings they must improve image quality without uncontrolled modification of clinically important regions. This is especially relevant for intracranial CT and CT angiography (CTA), where small vessels and aneurysm-relevant cues lie near high-contrast anatomical boundaries. We frame medical image restoration as a conservative AI problem and present a residual-bounded 2.5D restoration framework trained on synthetically degraded CT/CTA inputs. The model adds a learned residual to the original center slice through an edit-control map that limits the magnitude and spatial extent of modification. We evaluate the framework using an aneurysm-relevant image-recovery matrix, paired comparison against a Gaussian baseline, Monte Carlo stability testing, anatomical localization of meaningful edits, and external evaluation on low-dose CT. On 50 out-of-distribution CT-CTA cases, the bounded model achieved a mean target gain of 0.0635, a mean PSNR of 37.51 dB, and an iatrogenic-edit rate of 4.0%. Across 1,000 Monte Carlo runs, it remained net positive in 85.4% of runs with no stably negative cases. On external low-dose CT, the model was directionally beneficial and produced a substantially smaller modification footprint than the baseline. Meaningful edits concentrated in brain and skull regions while unrelated anatomy showed negligible change. These findings provide preliminary computational evidence that residual-bounded restoration is feasible in boundary-sensitive vascular imaging, but they do not establish clinical diagnostic performance and require expert review and prospective validation before clinical use.

---


### 68. [REC-RL: Referring expression counting via Gaussian and range-based reward optimization](https://arxiv.org/abs/2605.16460)

**<font color=#1a73e8>作者：</font>** Hui Liu, Yunlai Teng, Kunlong Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring expression counting (REC) is an intention-driven task that requires context-aware visual reasoning. While recent vision-language models incorporate language for visual understanding, most existing REC methods rely on rulebased reinforcement learning with rewards focused primarily on final accuracy, overlooking the quality of intermediate reasoning. We propose REC-RL, a reinforcement learning framework that introduces a think-range-answer paradigm to explicitly optimize the visual reasoning process. RECRL employs Group Relative Policy Optimization and two lightweight rewards: an accuracy reward that combines range-based interval supervision with Gaussian-based precision guidance, and a format reward that enforces structured outputs. By modeling intermediate focus prediction as internal decision-making, REC-RL avoids additional annotations and better aligns with human perception. Extensive experiments demonstrate consistent improvements over strong baselines and robust generalization across benchmarks.

---


### 69. [Asking Back: Interaction-Layer Antidistillation Watermarks](https://arxiv.org/abs/2605.16462)

**<font color=#1a73e8>作者：</font>** Guang Yang, Amir Ghasemian, Fengchen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting unauthorized knowledge distillation from a deployed LLM API is hard because the defender controls neither the attacker's training pipeline nor the next-token logits. Existing defenses operate on the teacher's output tokens -- biasing the next-token distribution (green-list watermarks, cryptographic schemes, antidistillation sampling) or rewriting outputs after generation. Recent work shows a paraphrasing attacker can strip these signals without losing the underlying knowledge.
We propose interaction-layer antidistillation watermarks, which move the trace one layer higher, into the teacher's interaction behavior: the defender wraps the teacher with a system prompt that intermittently induces a behavioral marker -- an explicit follow-up question, a low-frequency variant, or a declarative restatement. An oblivious distiller inherits the behavior, and the defender audits via black-box queries with a human-validated LLM-as-judge (Cohen's kappa = 0.84/0.78 on strong/style rubrics).
Across 63 LoRA-distilled students under a Llama-3.3-70B-Instruct teacher (35,343 judged samples), behavioral watermarks transfer at 88.9% (Gemma) / 80.9% (OLMo) / 45.2% (Qwen) relative fidelity (H1, H2). Under non-adaptive DIPPER paraphrasing, robustness decomposes into a teacher-self ceiling (about 66.4%) and student-relative retention of 21-112%, with OLMo preserving the watermark above the teacher itself (H3, F-Amp). Low-density (about 20%) explicit and implicit declarative variants transfer above per-family baseline (H4, F-Style). An N=20 in-lab study (pre-registered Latin-square) shows all marker variants within 0.22 Likert step of baseline; TOST, Friedman, and Bonferroni-Wilcoxon support H5. The interaction layer is a viable design locus for antidistillation watermarking, complementary to token-, model-, and reasoning-trace-layer defenses.

---


### 70. [MHMamba: Multi-Head Mamba for 3D Brain Tumor Segmentation](https://arxiv.org/abs/2605.16464)

**<font color=#1a73e8>作者：</font>** Hanjun Tao, Hua Wang, Fan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain tumors exhibit high heterogeneity in morphology and multimodal contrast, making manual slice-by-slice de lineation time-consuming and experience-dependent, thus necessitating efficient and stable automated segmentation methods. To address the limitations of CNNs in modeling long-range dependencies, and the heavy computational and memory overhead and inter-block contextual in coherence of Transformers in 3D MRI, this paper proposes Multi-Head Mamba (MHMamba). This method combines a U-shaped architecture with a multi-head state-space model (Mamba), splitting the channel dimension into parallel SSM heads and aggregating them with residuals. This enhances long-range representation and improves the stability of multimodal training while maintaining linear complexity. To further align statistics and enhance lesion response, we designed a channel-space calibration module for multi-head outputs and introduced an adaptive fusion mechanism at skip connections to dynamically connect global semantics with local details, thereby improving boundary consistency and the detection of small-volume lesions. We conducted experiments and ablations on BraTS2021 and BraTS2023. The results showed that MHMamba achieved stable and significant improvements in overall accuracy, boundary smoothness, and sensitivity to tumor core and small-volume enhancement areas, while preserving the linear-complexity advantage of Mamba-based modeling, thus verifying the effectiveness and versatility of the method.

---


### 71. [Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex](https://arxiv.org/abs/2605.16468)

**<font color=#1a73e8>作者：</font>** Idan Daniel Grosbard, Mor Geva, Galit Yovel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A central goal in understanding human vision is to uncover the visual features that drive neuronal activity. A growing body of work has used artificial neural networks as encoding models to predict cortical responses to natural images, revealing the visual content that activates category-selective regions. However, existing approaches are largely correlational and treat the encoder as a black box, leaving open which image features drive each voxel's response. We introduce Mechanistically Interpretable Neural Encoding (MINE), a framework that opens this black box by applying mechanistic-interpretability tools to localize the features within natural images that drive millimeter-scale (voxel-level) activity. MINE predicts each voxel's response using language-aligned image representations, and produces semantically interpretable descriptions of the features critical for the voxel's activation. We further generalize these per-image features into per-voxel functional profiles. To validate the per-image descriptions, we show they are sufficient to generate images that elicit voxel responses matching the responses to the original images, more accurately than images generated from random or low-attribution controls. Moreover, counterfactually inserting or removing the predicted features from images shifts activation in the expected direction, providing causal evidence. Counterfactual editing guided by the per-voxel activation profiles produces even stronger activation shifts, indicating that the profiles faithfully capture each voxel's selectivity. Finally, we apply MINE to well-studied category-selective brain regions, showing it recovers their known categorical preferences while revealing fine-grained unique voxel structure within each region. Overall, our results establish mechanistic interpretability as a path to discover and causally validate fine-grained hypotheses about neural function.

---


### 72. [Seeking the Unfamiliar but Memorable: Conceptual Creativity as Meta-Learning](https://arxiv.org/abs/2605.16477)

**<font color=#1a73e8>作者：</font>** Mengye Ren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What does it mean to create a new concept, rather than retrieve a familiar one? Repeatedly sampling a generative model at the same prompt produces variations with similar styles and typical content. We propose that creativity is the production of stimuli that are unfamiliar to an adaptive observer at first sight, but quickly learnable from a few exposures. We formalize this as a Creator-Appraiser pair: a Creator generates a candidate, an Appraiser adapts to it for a few inner-loop learning steps, and the Appraiser's improvement becomes the reward the Creator optimizes through. We instantiate the framework with diffusion as the Creator, an autoencoder Appraiser on MNIST, and a CLIP Appraiser with a low-rank adapter for natural images. The diffusion model remains frozen with no additional language conditioning; the meta-learning gradient is enough to produce both stylistic variations and concept compositions that the base model does not generate on its own.

---


### 73. [SeamCam: Quantifying Seamless Camouflage via Multi-Cue Visual Detectability](https://arxiv.org/abs/2605.16515)

**<font color=#1a73e8>作者：</font>** Amin Karimi Monsefi, Abolfazl Meyarian, Mridul Khurana 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animals are described as effectively camouflaged when they blend seamlessly with their surrounding, yet no standardized quantitative measure of this seamlessness exists. We address this gap by framing camouflage evaluation as a visual localization problem: a well-camouflaged animal is one that remains difficult to detect even when its category is known. We introduce SeamCam (Seamless Camouflage), a metric that quantifies how detectable an animal is from the available visual evidence. Given an image and a target species, SeamCam generates category-conditioned detection proposals, extracts segmentation masks, and identifies the subset whose collective union yields the highest IoU with the ground-truth mask. The SeamCam score is one minus this maximum recoverable localization signal, where a higher score indicates stronger camouflage (i.e., lower detectability). In a human two-alternative forced-choice study with 94 participants and 2,390 comparisons, SeamCam achieves 78.82% agreement with human camouflage difficulty judgments, outperforming state-of-the-art by about 25%. We then demonstrate SeamCam's utility as a preference signal for Direct Preference Optimization (DPO) to fine-tune a diffusion-based inpainting model for camouflage generation. This offers an affordable training approach with an objective explicitly suited for camouflage generation, unlike typical diffusion models. To support rigorous benchmarking, we further introduce CamFG-1.5k, a curated dataset of 1,521 high-resolution images in which animals are fully visible prior to camouflage generation, enabling unbiased evaluation by controlling for occlusion artifacts present in existing datasets. this https URL

---


### 74. [DepthPolyp: Pseudo-Depth Guided Lightweight Segmentation for Real-Time Colonoscopy](https://arxiv.org/abs/2605.16519)

**<font color=#1a73e8>作者：</font>** Zhuoyu Wu, Wenhui Ou, Lexi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate polyp segmentation in colonoscopy is essential for early colorectal cancer detection, yet real-world clinical environments pose persistent challenges such as motion blur, specular reflections, and illumination instability. Most existing methods are optimized on clean benchmark images and suffer noticeable performance degradation when deployed in authentic surgical scenarios. We propose DepthPolyp, a lightweight and robust segmentation framework based on pseudo-depth-guided multi-task learning and efficient feature modulation. The architecture combines hierarchical Ghost factorization for compact feature generation, Interleaved Shuffle Fusion for low-cost cross-scale interaction, and Dynamic Group Gating for adaptive group-wise feature weighting. Extensive experiments demonstrate that DepthPolyp achieves strong cross-dataset generalization when trained on degraded data and evaluated on both clean and noisy target domains, consistently outperforming lightweight baselines and remaining competitive with substantially larger models. In real surgical video evaluation on PolypGen, DepthPolyp achieves better segmentation performance than models up to $20\times$ larger while preserving real-time inference speed. With only 3.57M parameters and 0.86 GMACs, the proposed method runs at over 180 FPS on mobile devices, making it well suited for real-time deployment in resource-constrained clinical environments. Code and pretrained weights are available at: this https URL

---


### 75. [Global Convergence of Sampling-Based Nonconvex Optimization through Diffusion-Style Smoothing](https://arxiv.org/abs/2605.16520)

**<font color=#1a73e8>作者：</font>** Zeji Yi, Chaoyi Pan, Guanya Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling-based optimization (SBO), like cross-entropy method and evolutionary algorithms, has achieved many successes in solving non-convex problems without gradients, yet its convergence is poorly understood. In this paper, we establish a non-asymptotic convergence analysis for SBO through the lens of smoothing. Specifically, we recast SBO as gradient descent on a smoothed objective, mirroring noise-conditioned score ascent in diffusion models. Our first contribution is a landscape analysis of the smoothed objective, demonstrating how smoothing helps escape local minima and uncovering a fundamental coverage-optimality trade-off: smoothing renders the landscape more benign by enlarging the locally convex region around the global minimizer, but at the cost of introducing an optimality gap. Building on this insight, we establish non-asymptotic convergence guarantees for SBO algorithms to a neighborhood of the global minimizer. Furthermore, we propose an annealed SBO algorithm, Diffusion-Inspired Dual-Annealing (DIDA), which is provably convergent to the global optimum. We conduct extensive numerical experiments to verify our landscape results and also demonstrate the compelling performance of DIDA compared to other gradient-free optimization methods. Lastly, we discuss implications of our results for diffusion models.

---


### 76. [Toward Template-Free Explainability for Monte Carlo Tree Search](https://arxiv.org/abs/2605.16524)

**<font color=#1a73e8>作者：</font>** Siqi Lu, Mirsaleh Bahavarnia, Hiba Baroud 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Probabilistic search algorithms, such as Monte Carlo Tree Search (MCTS), have proven very effective in solving sequential decision-making tasks under uncertainty. However, interpreting asymmetric search trees that incorporate bandit-based tree traversal and simulation-based value estimation is difficult for end users based solely on raw tree statistics. While prior work requires hand-crafted formal logic constraints that must be updated when the problem changes, we present a framework that enables large language models (LLMs) to generate evidence-grounded explanations of MCTS decisions from recorded search traces in an end-to-end manner. Our framework maps natural-language questions to a structured set of intent categories, determines whether the existing tree contains sufficient evidence, triggers targeted expansion when needed, and generates explanations using tree statistics such as visit counts, value estimates, and risk information. Experimental results provide the first evidence that LLMs can serve as end-to-end explainers for probabilistic search, without requiring intermediate formal representations.

---


### 77. [Hypergraph Pattern Machine: Compositional Tokenization for Higher-Order Interactions](https://arxiv.org/abs/2605.16527)

**<font color=#1a73e8>作者：</font>** Kyrie Zhao, Zehong Wang, Tianyi Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergraphs model higher-order relations that drive real-world decisions, from drug prescriptions to recommendations. A central structural signal in such data, beyond what pairwise relations can express, is interaction compositionality: whether a higher-order relation is compositional, emergent, or inhibitory with respect to its observed or unobserved sets. In polypharmacy, the regime decides whether a drug should be dropped, kept, or excluded: a compositional drug triple can be safely simplified, an emergent triple requires all drugs jointly, and an inhibitory triple flags a drug that disrupts an existing interaction. However, existing hypergraph learning methods, which merely propagate messages over observed hyperedges, leave this compositional signal unmodeled, allowing dangerous drug combinations to slip through and be misclassified. To this end, we propose the Hypergraph Pattern Machine (HGPM), shifting the paradigm from message passing to learning the compositional pattern of subsets. It tokenizes compositional subsets, organizes them in an inclusion DAG, and trains an inclusion-aware Transformer under masked reconstruction. On ten hypergraph benchmarks, HGPM matches or exceeds state-of-the-art methods. Notably, in a real adverse-event prediction case, HGPM correctly identifies the drug addition that inhibits the side effect among feature-identical candidates, a discrimination existing methods cannot make. The code and data are in this https URL.

---


### 78. [Multiscale Supervised Unbalanced Optimal Transport Flow Matching](https://arxiv.org/abs/2605.16529)

**<font color=#1a73e8>作者：</font>** Qiangwei Peng, Lezhi Chen, Peijie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unbalanced optimal transport (UOT) provides a principled framework for modeling single-cell transitions and birth-death dynamics, but its high computational cost limits scalability to large-scale datasets. Although single-cell data often contain hierarchical annotations and known transition priors, existing UOT approximations rarely exploit this multiscale structure or prior knowledge. We introduce Multiscale Supervised Unbalanced Optimal Transport Flow Matching (MUST-FM), a simulation-free framework that scales UOT by leveraging hierarchical data structure. MUST-FM further supports an optional supervised formulation that incorporates transition priors, such as cell lineages, to guide the learning of displacement fields and mass variations. Experiments show that MUST-FM reduces computational overhead while achieving robust and biologically meaningful trajectory inference, enabling dynamic modeling of atlas-scale single-cell datasets.

---


### 79. [Boundedly Rational Meta-Learning in Sequential Consumer Choice](https://arxiv.org/abs/2605.16532)

**<font color=#1a73e8>作者：</font>** Mehrzad Khosravi, Max Kleiman-Weiner, Hema Yoganarasimhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many consumer decisions are repeated choices under uncertainty. Standard models capture these decisions using Bayesian learning and dynamic programming: consumers update beliefs from feedback and use those beliefs to guide future choices. In many markets, however, learning does not restart when consumers enter a new context: prior experience with a brand, product, or provider can shape beliefs in later, related decisions. We study this cross-context knowledge transfer, or meta-learning, in sequential choice. We design a hierarchical laboratory task in which participants repeatedly choose among airlines across routes and observe noisy binary outcomes. Reduced-form evidence shows that participants improve not only within routes, but also across routes: they choose better airlines earlier in later routes and reduce pseudo-regret. To identify the mechanism behind this transfer, we compare human choices to a no-transfer benchmark and a fully integrated Bayesian meta-learning benchmark. In particular, we introduce a class of boundedly rational meta dynamic programming policies, BRMDP(D), that approximate full integration using a limited number of hyper-posterior draws, denoted by D. Trial-by-trial likelihood comparisons show that low-D boundedly rational meta-learning, especially BRMDP(1), fits participant behavior better than both no transfer and fully integrated Bayesian transfer. Consumers, therefore, transfer brand-level regularities across contexts, but through coarse representations of prior uncertainty. The findings imply that models of consumer learning should allow for approximate cross-context transfer, and that managerial counterfactuals based on either no-transfer or fully integrated learning can be misleading.

---


### 80. [Symphony for Speech-to-Text: Supporting Real-Time Medical Voice Interfaces](https://arxiv.org/abs/2605.16545)

**<font color=#1a73e8>作者：</font>** Arne Nix, Robert James, Lasse Borgholt 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> After decades of use in dictation and, more recently, ambient documentation, speech is emerging as a primary modality for interacting with technology and AI in healthcare. Yet medical speech recognition remains difficult: systems must capture specialized terminology, resolve contextual ambiguity, and render measurements, abbreviations, and clinical shorthand precisely. Existing solutions are typically optimized either for general-purpose transcription or narrow dictation workflows, limiting their reliability in safety-critical settings and their usefulness for broader clinical workflows. We introduce Symphony for Speech-to-Text, a medical-grade speech recognition system for real-time streaming and batch file-based clinical use. Symphony decomposes the transcription process into specialized components for recognition, formatting, and contextual correction to optimize medical term recall while producing clinically structured text in real time and adapting across use cases. Evaluations on public benchmark and medical speech datasets show that Symphony substantially outperforms state-of-the-art systems in clinical settings while matching or exceeding them in general-domain settings, suggesting robust generalization rather than overfitting. We release a clinical benchmark dataset to support reliable validation and further progress in medical speech recognition. Symphony is available through a production-grade API for live dictation, conversational transcription, and batch audio file processing.

---


### 81. [Post-Quantum Discovery as a Governance Capability: Evidence-Based Cryptographic Visibility and Exposure Prioritisation in a Critical Service Provider](https://arxiv.org/abs/2605.16549)

**<font color=#1a73e8>作者：</font>** Jelena Zelenovic, Leila Taghizadeh, Edoardo Pena-Gonzalez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post Quantum Cryptography (PQC) readiness is increasingly constrained not by algorithm availability, but by cryptographic visibility, dependency complexity, and fragmented governance. This paper presents an anonymised case study of a large European critical service provider that initiated PQC readiness through a discovery first strategy, utilizing tool supported cryptographic inventorying to establish an evidence based baseline prior to migration planning. The discovery phase revealed systemic challenges, including distributed cryptographic ownership, uneven evidence quality across legacy and modern environments, and high dependency on third party cryptographic roadmaps. To operationalise these findings, the organisation introduced a structured exposure register that enabled prioritisation based on asset criticality, confidentiality longevity, and migration feasibility. We argue that PQC discovery should be understood as a governance capability that stabilises organisational knowledge and converts cryptographic uncertainty into measurable accountability, supporting risk based decision making and ecosystem coordination. The results contribute actionable lessons for institutions pursuing crypto-agility and resilience under post quantum harvest now, decrypt later threat models.

---


### 82. [Attention-Aware Transformer-Based Aggregation Network for Video Periocular Recognition](https://arxiv.org/abs/2605.16550)

**<font color=#1a73e8>作者：</font>** Luiz G F Carreira, Breno A Mariano, Victor H C de Melo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video periocular recognition is the task of recognizing an individual's identity based on the region around an individual's eyes. The periocular area is one of the most discriminative regions of the human face, making it suitable for recognition tasks. Its use as a biometric modality has emerged as an alternative, especially in surveillance scenarios where conventional biometric traits such as face or iris recognition become unfeasible due to unconstrained acquisition conditions. This paper proposes an attention-aware approach for video-based periocular recognition in surveillance environments. The framework consists of two main modules: feature embedding and aggregation. The feature embedding module is a deep convolutional neural network that maps periocular data to feature vectors. The aggregation module is an encoder-only transformer that adaptively learns to aggregate frame-level features into a single video representation and a feature vector for the still reference image. Experiments on the publicly available COX Face dataset show the robustness of the proposed method, consistently outperforming naive aggregation schemes. In the best scenario, the approach achieves $99.8\%$ of TPR@$1e^{-1}$ and $96.6\%$ of Rank-5.

---


### 83. [PQR: A Framework to Generate Diverse and Realistic User Queries that Elicit QA Agent Failures](https://arxiv.org/abs/2605.16551)

**<font color=#1a73e8>作者：</font>** Yunan Lu, Luigi Liu, Omar Yahia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM-based agents remains challenging because identifying meaningful failure cases often requires substantial human effort to design realistic test scenarios. Prior works primarily focus on automatically discovering agent failures induced by adversarial users, while overlooking queries with real user intents that also trigger agent failures. We introduce PQR, a framework that not only surfaces agent failures with respect to specific objectives (e.g., helpfulness, safety, etc.) but also resembles real users' intents. PQR operates through an iterative interaction between two complementary modules. The query refinement module performs rewrites to explore diverse query variations, while the prompt refinement module uses prior feedback to derive new objective-violating strategies and realism policies for refining prompts, which in turn generate failure-triggering yet realistic queries. We evaluate PQR on detecting an e-commerce QA agent's unhelpful responses. Our method uncovers 23% - 78% more unhelpful responses, and our generated queries are more diverse and realistic compared to previous methods.

---


### 84. [From Prompts to Protocols: An AI Agent for Laboratory Automation](https://arxiv.org/abs/2605.16552)

**<font color=#1a73e8>作者：</font>** Angelos Angelopoulos, James F. Cahoon, Ron Alterovitz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating science laboratories enables faster, safer, more accurate, and more reproducible execution of protocols, accelerating the discovery and testing of new materials, drugs, and more. However, setting up and running autonomous labs requires coordinating numerous instruments and robots, forcing scientists to write code, manage configuration files, and navigate complex software infrastructure. We present an AI agent architecture that integrates large language models with laboratory orchestration, enabling scientists to interactively create and monitor automated lab protocols using natural language. Integrated into the Experiment Orchestration System (EOS), the AI agent operates under an agentic loop with automated validation and error correction, and supports the complete experimental lifecycle: creating protocols, running and monitoring both protocols and closed-loop optimization campaigns, and analyzing results. A visual graph editor renders protocols as interactive node-based diagrams synchronized with the AI agent's protocol representation, enabling seamless alternation between AI-assisted and manual protocol construction. Evaluated on three simulated automated labs spanning chemistry, biology, and materials science, the AI agent achieves a 97% first-attempt protocol generation success rate and an order of magnitude reduction in required interface actions.

---


### 85. [Scaling Accessible Mathematics on arXiv: HTML Conversion and MathML 4](https://arxiv.org/abs/2605.16562)

**<font color=#1a73e8>作者：</font>** Deyan Ginev, Brian Caruso, Bruce Miller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report on the ongoing development of arXiv's HTML Papers offering, available on every new TeX/LaTeX submission since its initial release in 2023.
The main highlights from 2025 and early 2026 are:
(i) community-driven improvements to HTML fidelity and service health, with roughly half of 6,000 user reports resolved;
(ii) corpus-scale conversion work aimed at 90% error-free HTML (currently 75%);
(iii) initial MathML 4 Intent annotations for accessible speech output;
(iv) an in-progress Rust port of LaTeXML, reducing compute costs and enabling faster previews on submission.
The arXiv HTML Papers project remains experimental, but is gradually maturing as we better understand the needs of arXiv's readers and the technical opportunities presented by new standards and by advances in programming languages and AI.

---


### 86. [A Method for Securely Transmitting Large Video Files Using Chaotic Compression and Encryption](https://arxiv.org/abs/2605.16563)

**<font color=#1a73e8>作者：</font>** Shiladitya Bhattacharjee, Subha Bhattacharya, Arnab Chatterjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Conventional techniques for compression and encryption are frequently laborious and resource-intensive, rendering them inappropriate for real-time applications. A plethora of research has been presented in the current literature to address these difficulties together; yet, it fails to propose any suitable strategy. Therefore, this study introduces an innovative simultaneous data compression and encryption (SDCE) system specifically designed for large video files. The methodology amalgamates chaotic map-based encryption with Huffman encoding for lossless compression into a cohesive framework, markedly diminishing computational overhead and processing duration while augmenting data security. The logistic map is utilized to produce a pseudo-random chaotic sequence for XOR-based encryption, guaranteeing robust security against unwanted access. The research findings demonstrate its efficacy in enhancing data privacy compared to other existing and related strategies, particularly in terms of generating greater entropy and avalanche effects. It produces superior throughput, compression ratio, peak signal-to-noise ratio (PSNR), and reduced bits per rate (BPC), along with a smaller percentage of data loss, which further supports its ability to provide enhanced data integrity compared to other existing methods.

---


### 87. [Skim: Speculative Execution for Fast and Efficient Web Agents](https://arxiv.org/abs/2605.16565)

**<font color=#1a73e8>作者：</font>** Mike Wong, Kevin Hsieh, Suman Nath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skim is a speculative execution framework for web agents that exploits the predictable structure of purpose-built websites. Today's web-agent expense is not intrinsic to the tasks but a property of how agents are composed: frontier-model inference, browser rendering, and ReAct-style planning are applied to every step of every task regardless of complexity. Skim's key observation is that websites enforce stable URL patterns, answer formats, and task-to-trajectory mappings across queries of the same type, so most queries can bypass these heavyweight components entirely. An offline profiler captures these patterns once per site. At runtime, Skim matches each query to a template, synthesizes the destination URL, and extracts the answer with a small model. A lightweight verifier gates each fast-path output against the query and schema; rare misspeculations cascade to the full agent, warm-started by the fast path's final URL to preserve upstream trajectory progress. Across standard web-agent benchmarks paired with three backboneagents (WebVoyager, AgentOccam, BrowserUse), Skim reduces median per-task cost by 1.9x and latency by 33.4% with no accuracy loss.

---


### 88. [Automatic Unsupervised Ensemble Outlier Model Selection--Extended Version](https://arxiv.org/abs/2605.16567)

**<font color=#1a73e8>作者：</font>** Hong-Phuc Phan, Tuan-Anh Vu, Tung Kieu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised outlier detection is attractive because it eliminates the need for labeled data. Moreover, forming multi-model ensembles can improve detection robustness. However, composing an ensemble without labeled data is challenging. Naively composed ensembles can suffer from ensemble saturation, where redundant or unreliable detection models degrade performance and incur unnecessary computation. We propose MetaEns, an automatic unsupervised framework for selecting ensembles of outlier detection models. Using labeled meta-datasets, MetaEns learns a model that predicts marginal ensemble gains, estimating the expected improvement from adding a candidate model to a partially constructed ensemble. At test time, this learned signal is combined with a submodular-inspired proxy objective that enforces diminishing returns through diversity-aware discounting and family-level risk regularization, thereby enabling greedy sequential selection with adaptive early stopping. As a result, MetaEns constructs compact, high-quality ensembles without access to ground-truth labels. Experiments on 39 real-world datasets show that MetaEns consistently outperforms state-of-the-art unsupervised selectors and ensemble baselines, achieving higher average precision while using fewer models.

---


### 89. [Scalable Uncertainty Reasoning in Knowledge Graphs](https://arxiv.org/abs/2605.16568)

**<font color=#1a73e8>作者：</font>** Jingcheng Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs are pivotal for semantic data integration. The real-world data they model is often inherently uncertain. Within knowledge graphs, uncertainty manifests in three distinct levels: imprecise attribute values, probabilistic triple existence, and incomplete schema knowledge. However, current Semantic Web standards lack native support for reasoning over such uncertainty, and naïve extensions often incur computational intractability. In this thesis, I aim to develop a modular framework that addresses each level through tailored techniques: (1) defining probabilistic literals and a corresponding query algebra for continuous attributes; (2) a compilation-based framework transforming SPARQL provenance into tractable probabilistic circuits for uncertain triples; and (3) topology-aware geometric embeddings for statistical schema reasoning. The central hypothesis is that specialized reasoning mechanisms, namely algebraic, logical, and geometric approaches, can reconcile semantic precision with computational tractability.

---


### 90. [TriALS: Triphasic-Aided Liver Lesion Segmentation Benchmark in Non-Contrast CT](https://arxiv.org/abs/2605.16572)

**<font color=#1a73e8>作者：</font>** Marawan Elbatel, Mohamed Ghonim, Jiaji Mao 等 65 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated segmentation of liver lesions on non-contrast computed tomography (NCCT) is clinically important but fundamentally challenging, particularly in low-resource settings across Africa and Asia where contrast agents are frequently unavailable. Progress has been limited by the absence of annotated NCCT benchmarks. Here we describe the TriALS challenge for automated liver lesion segmentation under contrast-limited conditions, supported by a multi-centre dataset of 150 cases with four-phase CT acquisitions (600 volumes) from Egyptian and Chinese institutions. Algorithms were evaluated on 70 cases from three institutions, including an independent external cohort. The top-performing method achieved a mean venous-phase Dice of 0.754, consistent with human-level performance, yet dropped to 0.57 on NCCT. On external validation, the leading method outperformed off-the-shelf models by up to 28% in Dice on NCCT. Algorithm performance was most strongly predicted by training data scale and pre-training strategy. A cross-year comparison exposed a persistent perceptual barrier on NCCT that scaling pre-training alone cannot overcome. Data, annotations, and code are available at this https URL.

---


### 91. [Wavelet Flow Matching for Multi-Scale Physics Emulation](https://arxiv.org/abs/2605.16573)

**<font color=#1a73e8>作者：</font>** Gabriele Accarino, Juan Nathaniel, Carla Roesch 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate emulation of multi-scale physical systems governed by PDEs demands models that remain stable over long autoregressive rollouts while preserving fine-scale structures. Deterministic emulators produce overly-smoothed predictions, while generative approaches better capture details but are costly. Latent-space generative models have emerged as a compromise but with the additional cost of separately pre-trained autoencoders. We propose Wavelet Flow Matching (WFM), a novel generative emulator that overcomes current trade-offs between cost and skill by performing optimal-transport directly in the multi-scale wavelet space. Rather than learning a latent compression, WFM leverages the hierarchical structure of a U-Net to jointly predict transport velocities of a prescribed wavelet representation. On three challenging systems of chaotic fluid dynamics, WFM achieves superior long-horizon stability, accuracy and spectral coherence compared to state-of-the-art models. Our results clearly position the wavelet space as an effective training-free representation for generative emulation of complex physical dynamics.

---


### 92. [Attend Locally, Remember Linearly: Linear Attention as Cross-Frame Memory for Autoregressive Video Diffusion](https://arxiv.org/abs/2605.16579)

**<font color=#1a73e8>作者：</font>** Kunyang Li, Mubarak Shah, Yuzhang Shang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion is a powerful paradigm for streaming and interactive video generation. However, its reliance on softmax self-attention leads to quadratic compute complexity in sequence length and memory usage due to key-value caching, which limits its scalability to long video horizons. Existing remedies (e.g., sparse attention and KV-cache compression) reduce per-step cost but still rely on a linearly growing cache or irreversibly discard past context, and thus fail to address linear memory growth and streaming context management. To address this scalability bottleneck, we propose ARL2 (Attend Locally, Remember Linearly), a hybrid attention module that replaces quadratic cross-frame attention with a fixed-size recurrent state. We decompose self-attention into two branches: an intra-frame softmax branch for spatial detail and local dependencies, and an inter-frame gated recurrent linear branch that maintains a fixed-size state for streaming context. Our key insight is that softmax attention captures fine-grained local interactions, while a recurrent state provides controllable long-range memory. This design achieves linear-time scaling with constant memory while improving temporal consistency over the full-softmax model. To prevent noisy intermediate states from corrupting memory, we update the recurrent state only after the denoised pass. To avoid within-frame information asymmetry, all tokens share the same pre-update state rather than sequential updates. To the best of our knowledge, this is the first work to convert a pretrained AR video diffusion model into a hybrid linear attention architecture, through an efficient two-stage training scheme for AR video. With 75% of layers replaced by hybrid linear attention, the model achieves up to 2.26 wall-clock speedup and 54% memory reduction, while maintaining comparable quality with improving temporal consistency.

---


### 93. [Structure-Aware Masking for Protein Representation Learning](https://arxiv.org/abs/2605.16581)

**<font color=#1a73e8>作者：</font>** Thomas Walton, Ayan Goel, Amirali Aghazadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked language modeling (MLM) is the standard objective for training protein language models, typically implemented by randomly masking individual residues at a fixed rate (e.g., 15%). This practice implicitly assumes that all sequence positions contribute equally to representation learning. In downstream fitness prediction tasks, however, protein sequences are governed by three-dimensional structural dependencies and long-range residue contacts that induce strong nonlocal couplings between residues. We introduce Bucket Masking, a structure-aware masking strategy that selects groups of residues based on their proximity in three-dimensional space, preferentially masking structurally coupled regions during training. By conditioning the masking distribution on residue contacts, Bucket Masking shifts the learning objective toward modeling long-range interactions that are critical for protein function. Across four downstream protein fitness prediction tasks, Bucket Masking enables up to a 14% improvement over standard random masking, excelling at predicting higher-order mutational interactions. Through controlled ablations, we show that these improvements arise from mask placement rather than span size, establishing masking as a positional inductive bias.

---


### 94. [ArtMesh: Part-Aware Articulated Mesh Fields with Motion-Consistent Dynamics](https://arxiv.org/abs/2605.16582)

**<font color=#1a73e8>作者：</font>** Sylvia Yuan, Dan Wang, Ravi Ramamoorthi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ArtMesh, a mesh-native method for reconstructing articulated objects explicitly as connected triangle meshes with per-part rigid motion from multi-view images in start and end states. Existing 3D Gaussian Splatting pipelines for articulated reconstruction inherit the unstructured point-based geometry of their splatting base, which provides no surface topology for reasoning about part boundaries or enforcing motion consistency along the object's connectivity. ArtMesh instead builds on a mesh-based differentiable rendering backbone, enabling part-aware dynamics to act directly on the structured topology. To make the topology compatible with articulation, we introduce part-aware restricted Delaunay remeshing, producing connected submeshes whose triangles do not cross semantic part boundaries. The dynamic mesh field then optimizes articulation using bidirectional Vertex-wise Motion Consistency on transported mesh vertices and Pixel-wise Motion Consistency on rendered RGB-D observations. We introduce Articulate-100, a new benchmark of 100 articulated objects spanning 16 PartNet-Mobility categories. On this benchmark, ArtMesh outperforms prior 3DGS-based pipelines in joint parameter estimation and part-level geometric reconstruction, with the largest gains on objects with many movable parts.

---


### 95. [STRIKE: A Structured Taxonomy of Cybercrime for Risk, Impact, Knowledge, and Evolution](https://arxiv.org/abs/2605.16589)

**<font color=#1a73e8>作者：</font>** Melissa Pappy, Linh Nguyen, Suman Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybercrime has grown exponentially in both scale and sophistication, posing significant threats. As attack methods evolve rapidly, traditional classification schemes often fail to capture the complexity and diversity of modern threats. To address this gap, we introduce STRIKE,a Structured Taxonomy for Risk, Impact, Knowledge, and Emerging Threats, which provides a unified, multi-dimensional framework for categorizing cybercrimes. STRIKE spans both conventional and emerging domains, including ransomware, phishing, network intrusion, child sexual abuse material (CSAM), cryptojacking, deepfakes, and supply chain attacks. It organizes threats using criteria such as attack vectors, adversarial tactics, societal impact, detection techniques, and mitigation strategies. Alongside the taxonomy, we review recent advances in detection methodologies and present a response workflow to assist practitioners under active threat conditions. This work offers researchers, security professionals, and policymakers a practical foundation for threat analysis, comparative evaluation, and adaptive cyber defense.

---


### 96. [Why Modeling Human Haptic Material Perception with AI Is Difficult](https://arxiv.org/abs/2605.16602)

**<font color=#1a73e8>作者：</font>** Yasemin Vardar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Touch plays a central role in how humans perceive and recognize materials through physical contact. Despite decades of research, the mechanisms by which tactile signals are transformed into meaningful perceptual representations remain poorly understood, limiting the design of interactive systems and intelligent agents with human-like haptic perception. Recent advances in artificial intelligence (AI) offer new opportunities to model and exploit tactile data; however, haptics presents fundamental challenges for contemporary AI due to its interaction-dependent, multimodal nature. This position paper argues that progress at the intersection of AI and haptics is constrained by three key bottlenecks: (1) the scarcity of large, diverse, and balanced haptic datasets; (2) the lack of standardized evaluation platforms and perceptual benchmarks; and (3) limitations in model capacity and interpretability when applied to tactile perception. I discuss how these challenges impede generalization, reproducibility, and scientific insight into human touch and review emerging strategies to address them. This paper highlights opportunities for coordinated, cross-disciplinary efforts to advance AI systems that not only perform robust haptic perception but also contribute to a deeper understanding of human touch.

---


### 97. [Controlla: Learning Controllability via Graph-Constrained Latent Geometry](https://arxiv.org/abs/2605.16603)

**<font color=#1a73e8>作者：</font>** Jamuna S. Murthy, Amin Karimi Monsefi, Rajiv Ramnath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable multimodal generation is commonly formulated as an inference-time conditioning problem using prompts, guidance, or auxiliary modules. While effective, such approaches do not explicitly structure how semantic attributes evolve, which can lead to identity drift and inconsistent cross-modal behavior. We propose Controlla, a modular factorized-control framework that treats controllability as a property of structured latent geometry. Controlla learns identity and attribute factors from multimodal inputs and aligns them with graph priors using graph-constrained optimal transport, encouraging attributes to follow graph-consistent trajectories while preserving reference identity. To evaluate this setting, we construct AffectHuman-43K, a leakage-aware multimodal benchmark for reference-grounded affective control, and introduce geometry-aware metrics for trajectory consistency and latent disentanglement. Experiments show consistent improvements in controllability, identity preservation, and cross-modal alignment, with additional analyses on graph sensitivity, extensibility, and robustness.

---


### 98. [R2V Agent: Teaching SLMs When to Ask for Help](https://arxiv.org/abs/2605.16604)

**<font color=#1a73e8>作者：</font>** Raghu Vamshi Hemadri, Humaira Firdowse Mohammed, Rishabh Maheshwary 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient agentic systems should incur expensive frontier-model costs only on decisions where a cheaper local model is likely to fail. Existing LLM cascades usually route whole queries before execution, but task difficulty shifts mid-trajectory - after flaky tool calls, truncated observations, or compounding local errors - making pre-execution routing brittle. We introduce \textbf{R2V-Agent}, a risk-calibrated SLM-LLM routing framework for interactive agents. R2V combines four components: a distilled small language model (SLM) policy, a stronger teacher LLM, a lightweight process verifier that scores candidate actions at each step, and a calibrated step-level router. The router is our central contribution: after the SLM is trained, it estimates residual failure risk at each step and escalates only when teacher intervention is warranted. To make the routing problem well-defined, we first train a stable local SLM using a standard offline pipeline: behavioral cloning (BC) on teacher trajectories, followed by verifier-guided Direct Preference Optimization (DPO) with consistency regularization. The router is then trained on this fixed policy's residual failures using Brier-calibrated probability estimation and a Conditional Value-at-Risk (CVaR)-constrained objective that penalizes worst-case failures across perturbation seeds. Across HumanEval+, TextWorld, and TerminalBench with four SLM backbones, R2V improves the reliability-cost frontier: it achieves $94.3\%$ HumanEval+ success with $0.60\%$ LLM escalation, recovers TextWorld from $64.6\%$ SLM-only success to $98.2\%$ at $41.7\%$ escalation, and reaches $93.3\%$ TerminalBench success at $33.9\%$ LLM calls, roughly half the heuristic-router cost.

---


### 99. [PromptDecipher: Supporting AI Tutor Authoring Through Editable Simulated Interactions](https://arxiv.org/abs/2605.16605)

**<font color=#1a73e8>作者：</font>** Miina Koyama, Ruiwei Xiao, John Stamper  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chatbots have long been explored as tools to support learning, and recent advances in large language models have significantly expanded the availability of platforms for educators to author AI tutoring chatbots. Yet effective authorship demands more than writing a system prompt; it requires educators to act as learning designers, AI interaction designers, and QA engineers. In practice, however, teachers rarely fulfill these roles. Our formative study found that virtually none systematically tested their bots before deploying them to students. To address this gap, we present PromptDecipher, a system that restructures the authoring workflow around a direct correction-based interaction rather than writing abstract system prompts, teachers interact with a live chat preview and edit undesirable bot responses. An automated pipeline then analyzes the correction, proposes a targeted system prompt rewrite, and validates the change across pre-defined test scenarios. This enforces QA as a first-class activity and scaffolds teachers in roles they would otherwise skip. PromptDecipher will be deployed in an AI for Educators course enrolling hundreds of higher-education instructors. A live prototype (this https URL), an anonymized codebase (this https URL), and anonymized demo (this https URL) are available via links in the footnote.

---


### 100. [To MRL or not to MRL: Text Embeddings are Robust to Truncation Without Matryoshka Embeddings, Except In Heavy Truncation Scenarios](https://arxiv.org/abs/2605.16608)

**<font color=#1a73e8>作者：</font>** Sotaro Takeshita, Yurina Takeshita, Simone Paolo Ponzetto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matryoshka Representation Learning (MRL) is a widely adopted approach for training text encoders so they provide useful text representations at various sizes, available by simply truncating the resulting vectors at sizes pre-determined at training time. Recent works have shown that randomly truncating text embeddings has minimal impact in downstream performance unless vectors are reduced in size by at least 70%, suggesting that embeddings are already robust to truncation without the use of MRL. However, no prior work has compared random truncation to MRL, so it is unclear how the two methods compare as effective embedding reduction methods. In this paper, we study this by applying the same truncation used by MRL to models trained with and without MRL. Our results across several models and downstream tasks show that, unless heavily truncating embeddings (i.e. reducing their size by at least 80%), truncated embeddings of non-MRL models are competitive with, and often outperform models trained with MRL. This suggests that truncation robustness may not necessarily come from MRL, and that the choice of spending the additional training cost of MRL depends on whether heavy truncation is desired.

---


> [!TIP]
> 当前位于：**51-100**（第 2/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
