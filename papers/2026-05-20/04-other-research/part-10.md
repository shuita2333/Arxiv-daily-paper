# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 451. [Operationalising Post Quantum TLS Automated Configuration Profiling and Hybrid PQC Deployment in Financial Infrastructure](https://arxiv.org/abs/2605.17955)

**<font color=#1a73e8>作者：</font>** Harish Balaji, Aarav Varshney, Prasanna Ravi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organisations are upgrading their cryptographic infrastructure to become quantum safe before large scale quantum computers materialise. Post quantum cryptography (PQC) standards now exist for key exchange and digital signatures, but the urgent question for adopters is how to operationalise PQC in complex environments with confidence. In banking, Transport Layer Security (TLS), for example, protects data in transit across public facing channels and internal services, and is terminated at many heterogeneous endpoints (web servers, API gateways, load balancers, reverse proxies), each a potential quantum vulnerable component and migration target. We argue that the bottleneck is operational rather than algorithmic, hybrid key exchanges such as MLKEM and hybrid MLKEM key exchanges are already available in mainstream libraries, but security teams lack precise visibility into TLS configurations and repeatable methods for enabling PQC compatible settings across a heterogeneous estate. This paper presents a configuration parsing methodology that automatically extracts and normalises TLS cryptographic posture across dominant enterprise web server stacks, producing a unified, provenance traced cryptographic inventory as a foundation for migration and compliance. We demonstrate the approach on 8,443 real world Nginx configurations from public repositories and in a proof of concept deployment at a financial institution, where MLKEM and hybrid MLKEM key exchanges at TLS termination points (web server and API gateway) securing an internal application, with zero application layer changes and manageable performance overhead.

---


### 452. [Function graph transformers universally approximate operators between function spaces](https://arxiv.org/abs/2605.17968)

**<font color=#1a73e8>作者：</font>** Takashi Furuya, David Mis, Ivan Dokmanić 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the approximation of nonlinear operators between function spaces by transformers. Our approach is to lift functions to measures supported on their graphs and leverage a recently introduced measure-theoretic view of transformers. A function $h$ is represented by its graph measure $\gamma_h$, with finite tokens $\{(x_j,h(x_j))\}_{j=1}^N$ being its empirical approximations. We show that this framework elegantly models discretization refinement via convergence of measures and provides a natural setting for operator learning. Within this framework, we introduce function graph transformers, a graph-preserving subclass of measure-theoretic transformers that maps graph measures to graph measures, which is to say that outputs remain single-valued functions. Crucially, this additional structure does not reduce generality: we prove that the resulting graph-preserving maps can be approximated by finite compositions of standard softmax self-attention layers and pointwise MLPs, yielding universal approximation results for broad classes of nonlinear operators. Unlike existing theoretical approaches to operator learning with transformers, the measure-theoretic framework also accommodates regularized negative-order Sobolev inputs for which discretization invariance is particularly challenging, as well as query points on different output domains. Overall, function graph transformers provide a continuum viewpoint and mathematical toolkit for transformer-based operator learning, clarifying the roles of positional encodings, graph structure, regularization, and ensuring consistency across discretizations.

---


### 453. [Learning to Balance: Decoupled Siamese Diffusion Transformer for Reference-Based Remote Sensing Image Super-Resolution](https://arxiv.org/abs/2605.17980)

**<font color=#1a73e8>作者：</font>** Bin Luo, Runmin Dong, Zhaoyang Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based methods demonstrate significant potential for remote sensing image super-resolution at large scaling factors, particularly in reference-based super-resolution (RefSR) where high-resolution reference images provide critical fine-grained texture priors. However, existing methods often suffer from a trade-off between over-reliance on reference information, which leads to texture artifacts, and underutilization, which results in insufficient detail recovery. To address these issues, we propose DS-DiT, a Decoupled Siamese Diffusion Transformer method that decouples low-resolution and reference interactions at the attention level. By enabling low-resolution structural priors and reference texture information to interact independently with the noisy latent, the framework effectively mitigates inter-source competition. Furthermore, to compensate for the limited local modeling ability of global attention, we introduce a Patch-Level Weights (PLW) module that adaptively modulates the fusion of conditional sources. In addition, this siamese architecture facilitates an autoguidance strategy during inference, which enhances reconstruction by exploiting the prediction discrepancy between strong and weak reference conditions. This approach boosts generation quality without additional training. Experimental results across multiple datasets and scaling factors demonstrate that DS-DiT outperforms existing methods in both quantitative metrics and visual fidelity.

---


### 454. [LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injectio](https://arxiv.org/abs/2605.17986)

**<font color=#1a73e8>作者：</font>** Lei Zhao, Abhay Bhaskar, Edgar Dobriban  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents such as OpenClaw are increasingly deployed in local workflows with access to external tools. This creates indirect prompt-injection (IPI) risk: an agent may execute harmful instructions embedded in untrusted inputs such as email, downloaded files, webpages, repositories, or group-chat messages. Existing evaluations are often small, purely simulated, or focused on a narrow set of channels. We introduce LivePI (Live Prompt Injection), a structured benchmark for IPI risk in a production-like but test-controlled environment. LivePI covers seven input surfaces, twelve attack/rendering families, and five malicious goals, including protected-information exfiltration, unauthorized security-control changes, unsafe code retrieval or execution, inbox-summary exfiltration, and cryptocurrency transfer. We run LivePI on a real virtual machine with live but test-controlled email, chat, web, local-file, repository, and wallet interfaces. Across GPT-5.3-Codex, Claude Opus 4.6, Gemini 3.1 Pro, Kimi K2.5, and GLM-5, total attack success rates range from 10.7% to 29.6%. Group-chat injection is uniformly successful across the evaluated backbones in our deployment, and repository-link attacks produce high-severity failures despite a small denominator. We also evaluate a two-layer defense consisting of prompt-level filtering and pre-execution tool-call authorization. In the GPT-5.3-Codex setting, the defense intercepts all tested malicious-goal completions in LivePI before execution while preserving benign utility on PinchBench-derived workloads.

---


### 455. [Low Latency Gaze Tracking via Latent Optical Sensing](https://arxiv.org/abs/2605.17990)

**<font color=#1a73e8>作者：</font>** Yidan Zheng, Matheus Souza, Kaizhang Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a real-time gaze tracking system that directly acquires task-relevant latent features using a fully passive optical encoder. Instead of forming and processing full-resolution images, our approach leverages a microlens array with a co-designed binary chromium mask to perform spatially multiplexed optical encoding, producing a compact set of measurements sufficient for gaze estimation. By integrating sensing and feature extraction in the optical domain, the proposed system eliminates the need for high-bandwidth image readout and substantially reduces computational overhead. The encoded measurements are captured by a 4 x 4 phototransistor array and mapped to gaze direction using a lightweight neural network. Our proof-of-concept prototype enables an end-to-end sensing-to-inference latency of 3.4 ms, outperforming published research systems. We demonstrate the effectiveness of our approach on both simulated and real-world data, achieving competitive gaze estimation accuracy while significantly improving latency and energy efficiency compared to conventional camera-based pipelines. This work highlights the potential of task-driven optical sensing for ultra-low-latency, computationally efficient human-computer interaction systems.

---


### 456. [Bridging the Gap: Converting Read Text to Conversational Dialogue](https://arxiv.org/abs/2605.18001)

**<font color=#1a73e8>作者：</font>** Parshav Singla, Agnik Banerjee, Aaditya Arora 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent advancements within speech processing, converting read speech to conversational speech has gained significant attention. The primary challenge in this domain is maintaining naturalness and intelligibility while minimizing computational overhead for real-time applications. Traditional read speech often lacks the nuanced prosodic variation essential for natural conversational interactions, posing challenges for applications in virtual assistants, customer service, and language learning tools. This paper introduces a novel approach, Prosodic Adjustment with Conversational Context (PACC), aimed at converting read speech into natural conversational speech used in various modern applications. PACC utilizes advanced deep neural networks to analyze and modify prosodic features such as intonation, stress, and rhythm. Unlike conventional methods, our approach uses High-Fidelity Generative Adversarial Networks (HiFi-GAN) for speech synthesis. Our experimental results demonstrate significant improvements in speech conversion, enhancing naturalness and achieving better model accuracy with additional training on speech datasets. This research establishes new benchmarks in speech conversion tasks and Mean Opinion Score (MOS) evaluation for testing model accuracy, and we show that our approach can be successfully extended to other speech conversion applications.

---


### 457. [RL4RLA: Teaching ML to Discover Randomized Linear Algebra Algorithms Through Curriculum Design and Graph-Based Search](https://arxiv.org/abs/2605.18004)

**<font color=#1a73e8>作者：</font>** Jinglong Xiong, Xiaotian Liu, Ruoxin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized linear algebra (RLA) algorithms are a modern class of numerical linear algebra techniques that play an essential role in scientific computing and machine learning, with broad and growing adoption. However, their discovery remains mostly a manual process that requires deep expert knowledge and inspiration. While Reinforcement Learning (RL) offers a pathway to automation, standard approaches struggle with sparse reward landscapes and vast search spaces inherent to high-performing RLA algorithms. In this paper, we present RL4RLA, a general RL framework that automates the discovery of interpretable, symbolic RLA algorithms. Unlike black-box approaches, our method builds explicit algorithms from basic linear algebra primitives, ensuring verifiable and implementable representations. To enable efficient discovery, we introduce: (1) a numerical curriculum that progressively increments problem difficulty to encode inductive bias specific to the RLA domain; (2) Monte Carlo Graph Search, which optimizes exploration by identifying and merging equivalent partial algorithms. We demonstrate that RL4RLA rediscovers state-of-the-art methods, including sketch-and-precondition solvers, Randomized Kaczmarz, and Newton Sketch, and can be targeted to produce algorithms optimized for specific trade-offs between accuracy, speed, and stability. Code is available at this https URL.

---


### 458. [Scalable Decision-Focused Learning through Cost-Sensitive Regression](https://arxiv.org/abs/2605.18005)

**<font color=#1a73e8>作者：</font>** Noah Schutte, Senne Berden, Tias Guns 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world combinatorial problems involve uncertain parameters, which can be predicted given contextual features and historical data. These `predict-then-optimize' or `contextual optimization' problems have gained significant attention: end-to-end training methods can now minimize the downstream task cost rather than the predictive error. However, despite their effectiveness, these decision-focused learning (DFL) approaches often rely on repeated solving of the underlying combinatorial optimization problem during training, making them computationally expensive and difficult to scale. We reframe the learning problem as a cost-sensitive multi-output regression problem: multi-output due to the combinatorial problem having multiple uncertain parameters, and cost-sensitive due to the downstream task cost being the real target. Our technical contribution is the formalization of multiple loss function components that follow from this reframing: cost-insensitive normalization, decision-aware asymmetric penalization of over- and underpredictions, and instance-based costs that mimic the true downstream task-based loss locally. These components require zero or one solve per training data instance, while requiring no further solves during training. Experiments show that the combination of loss components achieves comparable downstream task quality to the state of the art, while being significantly more efficient, enabling scaling to problem sizes that have not been tackled before with DFL.

---


### 459. [Semantic Reranking at Inference Time for Hard Examples in Rhetorical Role Labeling](https://arxiv.org/abs/2605.18007)

**<font color=#1a73e8>作者：</font>** Anas Belfathi, Nicolas Hernandez, Laura Monceaux 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rhetorical Role Labeling (RRL) assigns a functional role to each sentence in a document and is widely used in legal, medical, and scientific domains. While language models (LMs) achieve strong average performance, they remain unreliable on hard examples, where prediction confidence is low. Existing approaches typically handle uncertainty implicitly and treat labels as discrete identifiers, overlooking the semantic information encoded in label names. We introduce RISE, an inference-time semantic reranking framework that leverages label semantics to refine predictions on hard instances. RISE automatically identifies low-confidence predictions and reranks model outputs using contrastively learned label representations, without retraining or modifying the underlying model. Experiments on eight domain-specific RRL datasets with seven LMs, including encoder-based and causal architectures, show an average gain of +9.15 macro-F1 points on hard examples. For explainability, we further propose manual hardness annotations to study difficulty from both model and human perspectives, revealing a moderate agreement with Cohen's kappa = 0.40.

---


### 460. [Uncertainty Reliability Under Domain Shift: An Investigation for Data-Driven Blood Pressure Estimation in Photoplethysmography](https://arxiv.org/abs/2605.18008)

**<font color=#1a73e8>作者：</font>** Mohammad Moulaeifard, Ciaran Bench, Philip J. Aston 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification (UQ) is critical for safety-critical domains like healthcare, yet it is rarely evaluated under realistic out-of-distribution (OOD) conditions. Here, we assessed predictive performance and uncertainty reliability for deep learning-based blood pressure (BP) estimation from photoplethysmography (PPG) signals under both in-distribution (ID) and OOD settings. Using an XResNet1D-50 trained on PulseDB and tested on four external datasets, we compared deep ensembles (DE) and Monte Carlo dropout (MCD) with Gaussian negative log-likelihood (GNLL) and mean squared error (MSE) losses, optionally followed by post-hoc recalibration via conformal prediction (CP), temperature scaling (TS), and isotonic regression (IR).
The key findings of our study are as follows: (1) DE provides stronger predictive robustness under domain shift than MCD, an advantage that becomes clear primarily under external shift. (2) Recalibrated GNLL-based methods yield the best uncertainty calibration (e.g., GNLL+DE+CP for systolic blood pressure (SBP), GNLL+DE+TS for diastolic blood pressure (DBP)), while MSE-based uncertainty requires recalibration to become practically useful. (3) Across settings, CP and TS offer the most consistent gains, with IR remaining competitive in several cases.
Overall, our results identify DE-based methods as most robust for predictive performance under domain shift, GNLL as strongest for native UQ, and recalibration as essential for making MSE-based uncertainty practical. These findings highlight the need to jointly assess predictive accuracy and calibration on external data for trustworthy cuffless BP estimation

---


### 461. [Functionalization via Structure Completion and Motion Rectification](https://arxiv.org/abs/2605.18010)

**<font color=#1a73e8>作者：</font>** Mingrui Zhao, Sai Raj Kishore Perla, Kai Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acquisition and creation of 3D assets have been largely view- or appearance-driven. As a result, existing digital 3D models often lack the requisite structural components to function as intended, such as joints, supports, interiors, or interaction elements. At the same time, even human-annotated motions are frequently error-prone, leading to physically implausible behavior. We introduce object functionalization, a novel task aimed at transforming visually plausible but non-functional 3D models into functional and physically operable ones. We formulate functionalization as a graph completion problem over a new functional graph representation, where labeled nodes represent object parts, labeled edges encode functional and contact relations, and movable nodes carry motion attributes, so that structural functional deficiencies manifest as missing nodes or incorrect edges. We develop a neural Graph Functionalizer (GraFu) to complete an incomplete graph representing a non-functional 3D object. The completed graph then drives a geometry realization stage that instantiates predicted connectors and structural elements in 3D, with the compelling side effect of rectifying erroneous human-annotated and predicted motions. To support training and evaluation, focusing on furniture as a rich and challenging target category, we introduce FurFun-233, a dataset of 233 paired non-functional and functionalized furniture models. On PartNet-Mobility ("zero-shot") and HSSD test sets, our method matches state-of-the-art methods in motion prediction accuracy while substantially improving functionality in terms of collision and connectivity.

---


### 462. [SAS: Semantic-aware Sampling for Generative Dataset Distillation](https://arxiv.org/abs/2605.18012)

**<font color=#1a73e8>作者：</font>** Mingzhuo Li, Guang Li, Linfeng Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks have achieved impressive performance across a wide range of tasks, but this success often comes with substantial computational and storage costs due to large-scale training data. Dataset distillation addresses this challenge by constructing compact yet informative datasets that enable efficient model training while maintaining downstream performance. However, most existing approaches primarily emphasize matching data distributions or downstream training statistics, with limited attention to preserving high-level semantic information in the distilled data. In this work, we introduce a semantic-aware perspective for dataset distillation by leveraging Contrastive Language-Image Pretraining (CLIP) as a semantic prior for post-sampling. Our goal is to obtain distilled datasets that are not only compact but also semantically class-discriminative and diverse. To this end, we design three semantic scoring functions that quantify class relevance, inter-class separability, and intra-set diversity in a pretrained semantic space. Based on image pools generated by existing distillation methods, we further develop a two-stage strategy for effective sampling: the first stage filters semantically discriminative samples to form a reliable candidate set, and the second stage performs a dynamic diversity-aware selection to reduce redundancy while preserving semantic coverage. Extensive experiments across multiple datasets, image pools, and downstream models demonstrate consistent performance gains, highlighting the effectiveness of incorporating semantic information into dataset distillation.

---


### 463. [TinySAM 2: Extreme Memory Compression for Efficient Track Anything Model](https://arxiv.org/abs/2605.18013)

**<font color=#1a73e8>作者：</font>** Zhaoyuan Ding, Yijing Yang, Han Shu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segment Anything Model 2 (SAM 2) serves as a core foundation model in the field of video segmentation. Building upon the original SAM model, it introduces a memory bank mechanism and demonstrates outstanding performance in tasks such as semi-supervised video object segmentation and tracking anything. However, the complex computational characteristics of SAM 2's multi-stage image encoder and memory module have raised the barrier to the model's deployment in practical applications. To address this issue, we propose TinySAM 2, a lightweight video segmentation model that balances performance and efficiency. First, a memory quality management mechanism is introduced to select and retain high-informative historical frames as the memory. In addition, a joint-spatial-temporal token compression is proposed that reduces the memory storage and computational cost. Specifically, average pooling is employed to first compress redundancy tokens in the spatial domain. In the temporal domain, informative tokens are selected across frames in the memory bank based on token-level similarity measurement. Besides, we take RepViT as the lightweight image encoder, which further reduces the model parameters. Extensive experiments on challenging datasets such as DAVIS and SA-V demonstrate that TinySAM 2 achieves 90% of the performance of SAM 2.1, with only 7% memory tokens and 3% training data. This study effectively alleviates the bottlenecks in parameter count, computational load, and deployment costs associated with SAM 2, providing a resource-efficient solution for the widespread application of video segmentation models on devices.

---


### 464. [Federated Learning by Utility-Constrained Stochastic Aggregation for Improving Rational Participation](https://arxiv.org/abs/2605.18020)

**<font color=#1a73e8>作者：</font>** M Yashwanth, Arunabh Singh, Ashok Nayak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) algorithms implicitly assume that clients passively comply with server-side orchestration by sharing local model updates upon server request. However, this overlooks an important aspect in real-world cross-silo environments: clients are often rational agents who may prioritize their utilities such as local model performance over that of the global model. In settings with significant statistical heterogeneity, rational clients may opt out of the federation if the perceived benefits of collaboration fail to meet their local utility thresholds. Such attrition degrades the global model performance and can lead to the collapse of the federated training process. In this work, we introduce FedUCA, (Federated Learning by Utility-Constrained Stochastic Aggregation for Improving Rational Participation), a framework that formalizes the server's role as an optimizer seeking to maximize global model performance by sustaining client participation. We substantiate our framework through extensive experiments on standard datasets demonstrating that by prioritizing participation feasibility, FedUCA achieves significantly higher client retention and, consequently, a superior global model performance.

---


### 465. [Unveiling Memorization-Generalization Coexistence: A Case Study on Arithmetic Tasks with Label Noise](https://arxiv.org/abs/2605.18022)

**<font color=#1a73e8>作者：</font>** Linyu Liu, Pinyan Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Highly over-parameterized models can simultaneously memorize noisy labels and generalize well, yet how these behaviors coexist remains poorly understood. In this work, we investigate the underlying mechanisms of this coexistence using modular arithmetic tasks under heavy label noise. Through extensive experiments on two-layer neural networks, we find that larger models tend to generalize better under appropriate optimization and model configurations, while noisy labels are memorized faster than clean data. Over-parameterized models internally form a generalization structure, but its expression in the output is suppressed by the need to fit noisy labels. Remarkably, even with 80\% label noise, near-perfect test accuracy can be achieved by extracting this internal structure using frequency-based methods. We further propose a task-agnostic method to partition networks into generalization and memorization components. Although this subnetwork improves generalization, it is limited compared with frequency-based extraction, indicating that the generalization structure is distributed across neurons and motivating the development of new tools to retrieve generalizable knowledge from over-parameterized networks.

---


### 466. [DSAA: Dual-Stage Attribute Activation for Fine-grained Open Vocabulary Detection](https://arxiv.org/abs/2605.18023)

**<font color=#1a73e8>作者：</font>** Donghong Jiang, Endian Lin, Hanqing Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-Vocabulary Object Detection (OVD) models break the limitations of closed-set detection, enabling the iden- tification of unseen categories through natural language prompts. However, they exhibit notable limitations in fine- grained detection tasks involving attributes like color, ma- terial, and texture. We attribute this performance bottle- neck in OVD models to a core issue: when category sig- nals dominate, OVD models tend to marginalize attribute information during inference. This leads to incorrect bind- ing between attributes and target objects. To address this, we propose the Dual-Stage Attribute Activation (DSAA) framework, which enhances fine-grained detection capa- bilities by strengthening attribute semantics at two criti- cal stages. In the text embedding stage, we employ At- tribute Prefix Adapter (APA) module to generate attribute prefixes that inject explicit attribute priors. To further am- plify the influence of these attributes, our Key/Value (K/V) Modulator module then intervenes during the BERT encod- ing phase, selectively enhancing the Key and Value vec- tors of the corresponding attribute tokens. In addition, we introduce an attribute-aware contrastive loss to improve discrimination among same-category instances with differ- ent attributes during training. Experimental results on the FG-OVD benchmark demonstrate the effectiveness of our method across various mainstream open-vocabulary mod- els.

---


### 467. [Interaction-Breaking Adversarial Learning Framework for Robust Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.18024)

**<font color=#1a73e8>作者：</font>** Sunwoo Lee, Mingu Kang, Yonghyeon Jo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperation is central to multi-agent reinforcement learning (MARL), yet learned coordination can be fragile when external perturbations disrupt inter-agent interactions. Prior robust MARL methods have primarily considered value-oriented attacks, leaving a gap in robustness when interaction structures themselves are corrupted. In this paper, we propose an interaction-breaking adversarial learning (IBAL) framework that takes an information-theoretic view to construct attacks that impede coordination by perturbing agents' observations and actions, and trains agents to perform reliably under such disruptions. Empirically, our approach improves robustness over existing robust MARL baselines across diverse attack settings and yields stronger performance even under agent-missing scenarios.

---


### 468. [FedSDR: Federated Self-Distillation with Rectification](https://arxiv.org/abs/2605.18028)

**<font color=#1a73e8>作者：</font>** Ziheng Ren, Zhanming Shen, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of Large Language Models faces severe statistical heterogeneity. However, existing model-level defenses often overlook the root cause: intrinsic data distribution mismatches. In this work, we first establish Federated Self-Distillation (FedSD) as a fundamental and potent strategy. By projecting client representations into a smoothed ``model-understanding space,'' FedSD alone serves as a universal booster, demonstrating superior performance over conventional algorithms. Despite its success, we identify a subtle trade-off termed the Rewrite Paradox -- unconstrained self-distillation can inadvertently increase hallucinations and redundancy. To refine this paradigm, we further propose FedSDR (Federated Self-Distillation with Rectification), the ultimate reinforced framework. It augments FedSD with a dual-stream mechanism: a local LoRA-S (Smoothing) branch to implicitly absorb heterogeneity via distilled data, and a parallel global LoRA-R (Rectification) branch anchored to raw data to enforce factual correctness. By selectively aggregating only LoRA-R, FedSDR yields a globally aligned and faithful model. Extensive experiments verify its superior performance.

---


### 469. [New Insight of Variance reduce in Zero-Order Hard-Thresholding: Mitigating Gradient Error and Expansivity Contradictions](https://arxiv.org/abs/2605.18035)

**<font color=#1a73e8>作者：</font>** Xinzhe Yuan, William de Vazelhes, Bin Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hard-thresholding is an important type of algorithm in machine learning that is used to solve $\ell_0$ constrained optimization problems. However, the true gradient of the objective function can be difficult to access in certain scenarios, which normally can be approximated by zeroth-order (ZO) methods. The SZOHT algorithm is the only algorithm tackling $\ell_0$ sparsity constraints with ZO gradients so far. Unfortunately, SZOHT has a notable limitation on the number of random directions % in ZO gradients due to the inherent conflict between the deviation of ZO gradients and the expansivity of the hard-thresholding operator. This paper approaches this problem by considering the role of variance and provides a new insight into variance reduction: mitigating the unique conflicts between ZO gradients and hard-thresholding. Under this perspective, we propose a generalized variance reduced ZO hard-thresholding algorithm as well as the generalized convergence analysis under standard assumptions. The theoretical results demonstrate the new algorithm eliminates the restrictions on the number of random directions, leading to improved convergence rates and broader applicability compared with SZOHT. Finally, we illustrate the utility of our method on a ridge regression problem as well as black-box adversarial attacks.

---


### 470. [Exploring Trust Calibration in XAI - The Impact of Exposing Model Limitations to Lay Users](https://arxiv.org/abs/2605.18036)

**<font color=#1a73e8>作者：</font>** Alfio Ventura, Tim Katzke, Jan Corazza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Trust calibration -- aligning user trust judgment with model capability -- is crucial for safe deployment of explainable AI (XAI), yet is often evaluated via global trust ratings detached from objective performance evidence. We present a preregistered, incentivized between-subject online study (N=418 representative UK sample) on explainable skin-lesion classification that disentangles expectation-setting from experienced performance. Participants completed 15 case evaluations using a fixed XAI panel (malignancy score, reliability score, and saliency map). We systematically manipulated five experimental onboarding conditions varying example-based information and limitation disclosures with five stimulus packages naturally varying observed prediction quality. Calibration was operationalized as the deviation between trust-related judgments (TAIS and case-wise ratings) and objective performance benchmarks for the encountered cases, analysed with hierarchical mixed-effects models. Only limitation disclosure for case-wise measures reliably impacts trust calibration, and short-term experience did not yield progressive calibration. Further, the experienced package of stimuli explained substantially more variance than the experimental manipulation. However, participants were hard-pressed to differentiate between case-wise perceived trust, trustworthiness, and accuracy estimation. We discuss implications for designing limitation communication and for measuring and analysing calibration metrics in XAI evaluations. All study materials and data of this study are publicly available for replication and further academic use.

---


### 471. [Patch Ensembles for Robust Salmon Re-Identification with Weak Trajectory Labels](https://arxiv.org/abs/2605.18038)

**<font color=#1a73e8>作者：</font>** Espen Uri Høgstedt, Christian Schellewald, Annette Stahl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Salmon re-identification in commercial net-pens is challenging due to large populations, which impose strict accuracy requirements and make large-scale labeled data acquisition infeasible. Trajectory IDs can be used as proxy labels, but this introduces trajectory-ID bias. To address these challenges, we propose a patch-based re-identification framework that fuses patch-level predictions into a salmon identity decision. A key component is the prediction of the salmon's lateral line, enabling extraction of texture-anchored patches and patch slices. To enable realistic evaluation, we introduce an experimental setup using multiple cameras placed 6 m apart, allowing the same fish to be recorded in different trajectories. This enables the construction of a cross-camera test set through manual match confirmation. Our ensemble approach outperforms the full-image baseline in same-trajectory validation (0.932 to 0.965 mAP) and cross-camera testing (0.609 to 0.860 mAP). The substantial improvements in the cross-camera setting demonstrate improved generalizability and robustness. Code and data: this https URL.

---


### 472. [SGSoft: Learning Fused Semantic-Geometric Features for 3D Shape Correspondence via Template-Guided Soft Signals](https://arxiv.org/abs/2605.18039)

**<font color=#1a73e8>作者：</font>** Soyeon Yoon, Chang Wook Seo, Hyunjung Shim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning dense correspondences across deformable 3D shapes remains a long-standing challenge due to structural variability, non-isometric deformation, and inconsistent topology. Existing methods typically trade off generalization, geometric fidelity, and efficiency. We address this by proposing SGSoft, a unified intrinsic pipeline that (i) constructs a geodesic correspondence field on a canonical template, (ii) learns multimodal dense descriptors guided by pretrained semantic priors with this geodesic correspondence field supervision, (iii) retrieves dense correspondences in a single feed-forward pass via nearest-neighbor search in descriptor space. This formulation enables stable and topology-invariant supervision under large pose variation, structural differences, and remeshing. SGSoft achieves state-of-the-art inter-category generalization while offering the best accuracy-efficiency trade-off among prior methods. It also achieves near real-time inference without pre-alignment, pairwise optimization, or post-refinement. Learned descriptors can be transferred effectively to downstream tasks such as semantic segmentation and deformation transfer, establishing a scalable and deployment-ready paradigm for dense 3D correspondence.

---


### 473. [DocOS: Towards Proactive Document-Guided Actions in GUI Agents](https://arxiv.org/abs/2605.18048)

**<font color=#1a73e8>作者：</font>** Jingjing Liu, Ziye Huang, Zihao Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Graphical User Interface (GUI) agents have shown promising performance in automated device interaction, they primarily depend on static parametric knowledge from pre-training or instruction tuning. This reliance fundamentally limits their ability to handle long-tailed tasks that require explicit procedural knowledge absent from model parameters, often forcing agents to resort to inefficient and brittle trial-and-error exploration. To mitigate this limitation, we introduce \textbf{Proactive Document-Guided Action} for GUI agents in dynamic, open-web environments, a novel paradigm that mirrors human problem-solving by enabling agents to autonomously search for relevant documentation to resolve long-tailed tasks. To evaluate agents' capability in this paradigm, we propose \textbf{DocOS}, a benchmark designed to assess document-guided problem solving in fully interactive environments. DocOS requires agents to autonomously navigate a web browser, locate relevant online documentation, comprehend procedural instructions, and faithfully ground them into executable GUI actions. Extensive experiments reveal that progress is strictly constrained by dual bottlenecks: agents struggle to reliably locate relevant information during proactive search and frequently fail to faithfully ground retrieved instructions into precise actions, pointing toward document-guided interaction as a crucial pathway for enabling self-evolving GUI agents in dynamic environments.

---


### 474. [Efficient 3D Content Reconstruction and Generation](https://arxiv.org/abs/2605.18052)

**<font color=#1a73e8>作者：</font>** Jiahao Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic 3D content creation seeks to replace labor-intensive modeling and scanning pipelines with systems that can synthesize or recover 3D assets directly from text or images. Its applications span video games, virtual reality, robotics, and simulation, enabling rapid asset prototyping, diverse interactive world generation, and efficient 3D data collection for training foundation models. Contemporary solutions largely follow two complementary paradigms: (i) text- or image-to-3D generation, which learns priors over 3D geometry and appearance to create novel assets from natural language or a single view image; and (ii) 3D reconstruction, which estimates camera poses and geometry from RGB images. This thesis advances both directions. On the generation side, I introduce Instant3D, which combines multi-view diffusion with feed-forward sparse-view 3D reconstruction to produce high-quality assets in 5-20 seconds. On the reconstruction side, I develop FastMap, a structure-from-motion pipeline that achieves up to 10x speedup over prior state-of-the-art by using first-order optimization with fused GPU kernels extensively, while maintaining comparable pose accuracy and downstream novel view synthesis quality.

---


### 475. [Protection Is (Nearly) All You Need: Structural Protection Dominates Scoring in Globally Capped KV Eviction](https://arxiv.org/abs/2605.18053)

**<font color=#1a73e8>作者：</font>** Gabriel Garcia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study KV cache eviction under a shared globally capped decode-time harness. Seven policies (LRU, H2O, SnapKV, StreamingLLM, Ada-KV, QUEST, Random) share a prompt-boundary vulnerability: without structural protection, they collapse to near-zero quality on six pure-transformer models (F1$\leq$0.064). Reserving 10\% of cache at each boundary recovers 69--90\% of the $C{=}2{,}048$ reference-ceiling quality on seven LongBench models at $C{=}256$ (13\% retention); a ten-model panel spans 68--98\%. An attention-mass pilot (Qwen2.5-3B, $N{=}30$) suggests why: the position-0 sink holds ${\sim}75\%$ of prefix mass, while other boundary tokens sit near ${\sim}0.41{\times}$ uniform expectation, so attention scorers retain the sink but still drop structurally critical tokens. With protection, simplified score-isolation variants are TOST-equivalent to LRU at $K{=}32$ ($\Delta{=}0.02$); at $K{=}8$, attention policies pairwise converge yet beat LRU by 0.011--0.021 F1 across $C{=}256$ and $C{=}512$. Faithful Ada-KV/QUEST add ${\sim}0.03$--$0.04$ F1 on Mistral-7B and Phi-3.5 beyond simplified variants. A NIAH-32K regime-transfer pilot on Qwen3-4B (decode vs.\ prefill, $C{\in}\{512,2048\}$) shows near-identical protection lifts (ratio 0.99--1.00). At 64K, protection helps but recovery is modest; faithful per-head scoring matches full-cache ceiling on Gemma-3-4B at 6.3\% retention only when the model already supports strong 64K retrieval without eviction. Overall: protection dominates; scoring differences are secondary once boundaries are guarded; per-head allocation gives a further modest gain.

---


### 476. [Threats to Arabic Handwriting Recognition: Investigating Black-Box Adversarial Attacks on embedded ConvNet models](https://arxiv.org/abs/2605.18058)

**<font color=#1a73e8>作者：</font>** Mohsine EL Khayati, Abdelillah Semma, Abdelaziz Courr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Arabic handwriting recognition (AHR) has made significant progress with deep learning models. AHR research has largely focused on performance, with security receiving little attention. This study provides what appears to be a new line of inquiry by demonstrating the vulnerability of high-performing models to adversarial black-box attacks. The focus on black-box attacks reflects real-world scenarios where the attacker has no prior knowledge of the model architecture. Extensive experiments were conducted on two benchmark AHR datasets containing Arabic handwritten Characters. Results demonstrated the effectiveness of the attacks, with the Pixle attack achieving an attack success rate of 99-100\% on most models. Other, less aggressive attacks achieved success rates of 50-96\% across most experiments. Despite the higher attack success rate, the attacks maintain the structural integrity of the characters, rendering them almost imperceptible to the human eye. The findings indicate the higher vulnerability of the studied models to adversarial manipulation. This underscores the need to strengthen efforts to secure these models and ensure their reliability in AHR real-world applications.

---


### 477. [Embedded ConvNet Ensembles: A Lightweight Approach to Recognize Arabic Handwritten Characters](https://arxiv.org/abs/2605.18060)

**<font color=#1a73e8>作者：</font>** Mohsine El Khayati, Rachid Elouahbi, Abdelillah Semma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Arabic Handwritten Character Recognition (AHCR) has recently advanced significantly with deep Convolutional Neural Networks (ConvNets). However, many models in the literature are deep and computationally expensive in terms of parameters and FLOPs, limiting their deployment on resource-constrained devices, which are increasingly common. This study addresses this gap by proposing a combination of lightweight embedded ConvNet models and ensemble learning techniques. Extensive experiments were conducted to identify best practices in AHCR, considering training hyperparameters, learning strategies, model choices, and ensemble methods. Results show that embedded models can achieve accuracy comparable to, or even surpassing, heavier architectures. Ensemble learning further enhances performance with only modest computational overhead, particularly under challenging training scenarios. Among the ensembling strategies, soft voting yielded the best overall results.

---


### 478. [The MixCount Dataset: Bridging the Data Gap for Open-Vocabulary Object Counting](https://arxiv.org/abs/2605.18063)

**<font color=#1a73e8>作者：</font>** Corentin Dumery, Niki Amini-Naieni, Shervin Naini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object counting is a foundational vision task with over a decade of dedicated research, yet state-of-the-art models still fail systematically in the mixed-object setting that dominates real-world applications such as industrial inspection and product sorting. We show that this gap is strongly driven by limitations in existing training and evaluation data: real counting datasets are prohibitively expensive to annotate and suffer from labeling noise, while existing synthetic alternatives lack diversity and realism. We address this with MixCount, a dataset and benchmark for mixed-object counting designed to target the failure modes of current counting models. To overcome the high cost of constructing and labeling such data, we develop an automatic generation pipeline that synthesizes images, fine-grained textual descriptions, and pixel-perfect counting annotations at scale, eliminating the labeling ambiguity that plagues prior datasets. Evaluating state-of-the-art counting models on MixCount exposes severe degradation in the mixed-object setting. More importantly, training these models on our synthesized data yields substantial gains on real-world benchmarks, reducing MAE by 20.14% on FSC-147 and by 18.3% on PairTally. These results establish MixCount as both a benchmark and a training dataset for fine-grained counting, and demonstrate that our pipeline, which produces effectively unlimited labeled data, helps address a long-standing bottleneck in counting models.

---


### 479. [Improving Spatio-Temporal Residual Error Propagation by Mitigating Over-Squashing](https://arxiv.org/abs/2605.18068)

**<font color=#1a73e8>作者：</font>** Seyed Mohamad Moghadas, Esther Rodrigo Bonet, Bruno Cornelis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual error propagation remains a fundamental problem in recurrent models, where small prediction inaccuracies compound over time and degrade long-horizon performance. Accurately modeling the correlation structure of such residuals is critical for reliable uncertainty quantification in probabilistic multivariate timeseries forecasting. While recent time-series deep models efficiently parametrize time-varying contemporaneous correlations, they often assume temporal independence of errors and neglect spatial correlation across the observed network. In this paper, we introduce Teger, a structured uncertainty module that overcomes the spa- tial and temporal limitations of error-correlated autoregressive forecasting. Teger proposes a spatial curvature-aware graph rewiring mechanism explicitly strengthening information-bottleneck edges identified by discrete Forman curvature. The component is integrated into a low-rank-plus-diagonal covariance head, preserving tractable inference via the Woodbury identity. Teger is backbone-agnostic, requiring only the latent state produced by any autoregressive encoder. We provide theoretical evidence of Teger, and experimentally evaluate it on LSTM, Transformer, and xLSTM backbones across four real-world spatio-temporal datasets, showing consistent improvement in Continuous Ranked Probability Score (CRPS). We further provide a formal theoretical analysis connecting curvature-aware rewiring to (i) oversquashing alleviation, (ii) improved spectral connectivity, (iii) reduced effective resistance, and (iv) improved covariance calibration bounds

---


### 480. [Equilibrium Selection in Multi-Agent Policy Gradients via Opponent-Aware Basin Entry](https://arxiv.org/abs/2605.18078)

**<font color=#1a73e8>作者：</font>** Yevhen Shcherbinin, Arina Redina, Maxim Kalpin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent policy-gradient methods have been shown to converge locally near stable Nash equilibria. Local convergence, however, does not determine which equilibrium is reached. We study this question through basin-entry probability with respect to a target set of equilibria selected by an external criterion, such as payoff dominance. For finite-unroll Meta-MAPG, we show that the update decomposes into ordinary policy gradient plus own-learning and peer-learning corrections, with controlled sampling noise and finite-unroll bias. We identify the peer-learning correction as the main equilibrium-selection mechanism: under a local alignment condition, the probability of entering the certified attraction region of the target stable-Nash set increases, relative to ordinary policy gradient. Because persistent correction may shift zero-update points of the original game, annealing the correction after entering the basin recovers ordinary policy-gradient dynamics and inherits local stable-Nash convergence guarantees. Experiments in Stag Hunt, iterated Prisoner's Dilemma, and preliminary neural-policy coordination environments support this basin-entry view, showing increased entry into cooperative basins under peer-aware updates.

---


### 481. [The Expressive Power of Low Precision Softmax Transformers with (Summarized) Chain-of-Thought](https://arxiv.org/abs/2605.18079)

**<font color=#1a73e8>作者：</font>** Moritz Brösamle, Stephan Eckstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing expressivity results for transformers typically rely on hardmax attention, high precision, and other architectural modifications that disconnect them from the models used in practice. We bridge this gap by analyzing standard transformer decoders with softmax attention and rounding of activations and attention weights, while allowing depth and width to grow logarithmically with the context length. As an intermediate step, we construct hardmax transformers with ternary activations and well-separated attention scores that simulate Turing machines using Chain-of-Thought (CoT). This lets us convert the constructions to equivalent softmax transformers without the unrealistic parameter magnitudes or activation precision that prior approaches would require. Using the same technique, we analyze a recently proposed summarized CoT paradigm and show that it simulates Turing machines more efficiently, with model size scaling logarithmically in a space bound rather than a time bound. We empirically test predictions made by our results on a Sudoku reasoning task and find better alignment with learnability than for prior high-precision results. Our code is available at this https URL.

---


### 482. [pyforce-1.0.0: Python Framework for data-driven model Order Reduction of multi-physiCs problEms](https://arxiv.org/abs/2605.18082)

**<font color=#1a73e8>作者：</font>** Stefano Riva, Yantao Luo, Carolina Introini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> pyforce is a Python package implementing Data-Driven Reduced Order Modelling techniques for applications to multi-physics problems, mainly set in the Nuclear Engineering world. The package is part of the ROSE (Reduced Order modelling with data-driven techniques for multi-phySics problEms): mathematical algorithms aimed at reducing the complexity of multi-physics models (for nuclear reactors applications), at searching for optimal sensor positions and at integrating real measures to improve the knowledge on the physical systems. With respect to the previous original implementation based on dolfinx package (v0.6.0), version 1.0.0 of pyforce has been completely re-written using pyvista as backend for mesh importing, computing integrals, and visualisation of results; in addition, functions are stored as numpy arrays, improving the ease of use of the package. This choice allows to use pyforce with any software solver able to export results in VTK format.

---


### 483. [Learning to Solve Compositional Geometry Routing Problems](https://arxiv.org/abs/2605.18094)

**<font color=#1a73e8>作者：</font>** Mingfeng Fan, Jianan Zhou, Jiaqi Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the Compositional Geometry Routing Problem (CGRP), a unified superclass of traditional routing problems that covers point-only, line-only, area-only, and arbitrary hybrid task geometries, providing a broad abstraction for real-world routing scenarios. Beyond standard point-based routing, CGRP with non-point tasks can be inherently asymmetric, tightly coupled travel routes with the intrinsic path, and enlarges the action space with numerous feasible yet often irrelevant options, thereby posing significant challenges for both representation learning and decision-making. To address these challenges, we propose DiCon, a differential attention-assisted solver with contrastive learning, as a plug-and-play framework that tackles the problem from two complementary angles. First, we introduce a differential attention mechanism that actively suppresses the probability mass on less competitive candidate actions. Second, we design a double-level contrastive learning objective to promote robust global instance representations and regularize geometry-aware task representations. Extensive experiments demonstrate that DiCon achieves strong performance, broad versatility, and superior generalization across diverse CGRP instances with different compositions.

---


### 484. [SENSE: Satellite-based ENergy Synthesis for Sustainable Environment](https://arxiv.org/abs/2605.18101)

**<font color=#1a73e8>作者：</font>** Kailai Sun, Mingyi He, Heye Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban Building Energy Modeling plays a critical role in achieving the United Nations' Sustainable Development Goals 7 and 11. Although existing studies based on satellite imagery and deep learning have achieved remarkable progress, many challenges exist: most existing studies are inherently predictive, failing to reflect the generative nature of urban planning; although generative AI and diffusion models have seen explosive growth in satellite imagery, they lack the urban functional generation (e.g., energy layer); third, aligned high-quality high-resolution building energy data with satellite imagery is limited and scarce. Here we propose SENSE (Satellite-based ENergy Synthesis for Sustainable Environment), a unified generative UBEM framework that jointly synthesizes realistic urban satellite imagery and aligned high-quality building energy consumption and height maps. By conditioning on road networks and urban density metrics, SENSE, based on a controllable diffusion model, leverages the knowledge learned by large vision models to generate urban building energy consumption and height information (annotations) in the latent space. Experiments across four cities (New York City, Boston, Lyon, Busan) demonstrate that SENSE achieves high visual fidelity and strong physical consistency, satisfying the ASHRAE standard metric. Experiments demonstrate that SENSE can generate enough annotated synthetic data using less than 20% labeled energy data, boosting downstream prediction performance by 10% IoU. Compared to SOTA urban energy prediction methods, SENSE significantly reduced prediction error (reduced 3%-11% NMBE and 1%-9% CVRMSE). This study offers an energy-efficiency urban planning and physical generation solution for urban science, energy science and building science. The dataset and code: this https URL and this https URL.

---


### 485. [DanceHMR: Hand-Aware Whole-Body Human Mesh Recovery from Monocular Videos](https://arxiv.org/abs/2605.18102)

**<font color=#1a73e8>作者：</font>** Wenhao Shen, Ming Zhou, Hengyuan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular video human mesh recovery is essential for digital humans, avatar animation, and embodied simulation, where both temporal stability and expressive whole-body motion are required. Existing video HMR methods produce coherent body motion but often overlook detailed hand articulation, while image-based whole-body methods recover SMPL-X meshes independently per frame, often leading to jittery and inaccurate hand motion. We present a temporally coherent whole-body HMR framework for challenging in-the-wild monocular videos. Our model unifies body context and part-specific hand observations through residual body-hand fusion, enabling stable body motion and detailed hand recovery within a single temporal architecture. We further introduce close-up-aware augmentation to improve robustness under upper-body framing. Experiments on whole-body and body-only benchmarks demonstrate improved hand reconstruction and competitive body accuracy. Our method also produces temporally stable and 2D-consistent SMPL-X motion in challenging real-world videos.

---


### 486. [TaskGround: Structured Executable Task Inference for Full-Scene Household Reasoning](https://arxiv.org/abs/2605.18109)

**<font color=#1a73e8>作者：</font>** ZhiYuan Feng, Yu Deng, Ruichuan An 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In real home deployments, household agents must often operate from a complete household scene and a situated household request, rather than from a clean task specification. Such requests require agents to identify task-relevant entities, recover intended task conditions, and resolve ordering constraints from the surrounding scene context. We formalize this capability as full-scene household reasoning: given a complete household scene and a situated household request, an agent must infer executable task structure before producing a grounded skill-level action sequence. This setting is challenging because complete household scenes contain substantial task-irrelevant information, making direct complete-scene prompting inefficient and error-prone. In practical deployment, this challenge is further amplified by privacy and local compute constraints, which favor compact open-weight models with limited long-context reasoning ability. We propose TaskGround, a training-free and model-agnostic Ground-Infer-Execute framework that grounds complete scenes into compact task-relevant scene slices, infers executable task structure, and compiles it into grounded skill-level action sequences. To evaluate this setting, we introduce FullHome, a human-validated evaluation suite of 400 household tasks spanning diverse home-scale environments and both goal-oriented and process-constrained requirements. On FullHome, TaskGround improves task success rates by large margins across both proprietary and open-weight models. Notably, it makes Qwen3.5-9B competitive with GPT-5 under direct complete-scene prompting while reducing total input-token cost by up to 18x. Our results identify executable task-structure inference as a central bottleneck in full-scene household reasoning and show that structured grounding can make compact local models substantially more effective for practical household deployment.

---


### 487. [iPOE: Interpretable Prompt Optimization via Explanations](https://arxiv.org/abs/2605.18113)

**<font color=#1a73e8>作者：</font>** Jiahui Li, Sean Papay, Roman Klinger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt optimization has often been framed as a discrete search problem to find high-performing and robust instructions for an LLM. However, the search result might not make it transparent why and where specific prompt changes lead to performance gains. This is in contrast to how humans are instructed for annotation tasks. Here, researchers carefully design annotation guidelines, leading to enhanced annotation consistency. Our paper aims at joining these two approaches and introduces iPOE, a novel interpretable prompt optimization strategy via explanations. We guide the prompt optimization process by automatically created guidelines from explanations of annotation decisions (either automatically generated or from humans). This set of guidelines is furthermore optimized by as series of operations, including removing, adding, shuffling, and merging. The resulting prompt includes guidelines that instruct the annotation, making the decision process of the LLM and the optimization transparent. It therefore supports also laypeople in the area of prompt optimization, particularly in challenging domains requiring expertise. In our experiments on four datasets, we find that iPOE can improves over prompts without guidelines and with random selected guidelines by up to $31\%$ and $35\%$, respectively. Moreover, LLM explanations can replace human explanations in the proposed method.

---


### 488. [WinTok: A Win-Win Hybrid Tokenizer via Decomposing Visual Understanding and Generation with Transferable Tokens](https://arxiv.org/abs/2605.18115)

**<font color=#1a73e8>作者：</font>** Yiwei Guo, Shaobin Zhuang, Zhipeng Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building a unified visual tokenizer is essential for bridging the gap between visual understanding and generation. Yet existing approaches struggle with the inherent conflict between these tasks, as a single token space is forced to support both high-level semantic abstraction and low-level pixel reconstruction. We propose WinTok, a concise hybrid tokenizer that achieves a win-win performance by explicitly decoupling the two objectives. WinTok supplements pixel tokens with a set of learnable semantic tokens, effectively mitigating cross-task interference without incurring the computational overhead of dual tokenizers. To further enhance understanding capability, we introduce an asymmetric token distillation mechanism: the semantic tokens are guided by pretrained semantic embeddings from any visual foundation model, enabling them to inherit strong discriminative power while maintaining flexibility. Across 10 challenging benchmarks, WinTok delivers consistent improvements in reconstruction, understanding, and generation. Trained on only 50M open-source data, WinTok surpasses the strong baseline UniTok by 11.2% in classification accuracy and achieves a competitive reconstruction rFID of 0.41, despite using substantially less training data. Code is released at this https URL.

---


### 489. [POST: Prior-Observation Adversarial Learning of Spatio-Temporal Associations for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2605.18128)

**<font color=#1a73e8>作者：</font>** Suofei Zhang, Yaxuan Zheng, Haifeng Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing Multivariate Time Series Anomaly Detection (MTSAD) frameworks increasingly rely on integrating Graph Neural Networks (GNNs) with sequence models to capture complex spatio-temporal dependencies. However, less attention is paid to the spatial over-generalization problem, where unconstrained structural modeling indiscriminately reconstructs anomalies, inevitably degrading detection recall. To tackle this problem, we propose a novel framework that unifies spatio-temporal modeling through a joint prior-observation adversarial learning paradigm. In the spatial dimension, the model alternately learns adjacency matrices as structural prior and models the association discrepancy between prior and data-driven observation in a minimax manner during training. Such adversarial optimization not only improves the model sensitivity for time-wise detection, but also enables the model to localize anomalies to specific channels. To systematically evaluate this anomaly localization capability, we further construct a synthetic benchmark equipped with precise channel-wise annotations. Extensive experiments across public datasets and our dedicated benchmark demonstrate that the proposed framework establishes a new state-of-the-art in both time-wise detection and spatial localization tasks. Our code, pre-trained models, and benchmark are publicly available at this https URL.

---


### 490. [Rad-VLSM: A Cross-Modal Framework with Semantics-Assisted Prompting for Medical Segmentation and Diagnosis](https://arxiv.org/abs/2605.18130)

**<font color=#1a73e8>作者：</font>** Fengyi Zhang, Xujie Zeng, Mohan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation is more clinically valuable when it supports diagnosis rather than merely producing lesion masks. However, diagnostically relevant lesion cues are often subtle and localized, while existing models may be distracted by background tissues, acoustic artifacts, and irrelevant visual correlations. To address this problem, we propose Rad-VLSM, a two-stage cross-modal framework for semantics-assisted lesion focusing, robust segmentation, and visually grounded diagnosis. In the first stage, a BLIP-2-based vision-language alignment module identifies lesion-related candidate regions under semantic guidance and converts them into box prompts. In the second stage, these prompts are fed into a SAM-based multitask network, where a multi-candidate region aggregation strategy improves prompt stability and guides lesion segmentation. The predicted masks are then used as spatial priors for diagnosis, and a visual-radiomics fusion head integrates lesion-aware visual features with selected radiomics descriptors. By using semantic information for localization rather than direct prediction, Rad-VLSM reduces text-to-diagnosis dependence and grounds diagnosis in lesion-level evidence. Experiments on a private clinical breast ultrasound dataset and public benchmarks show that Rad-VLSM achieves strong segmentation and diagnostic performance with favorable generalization.

---


### 491. [Who Generated This 3D Asset? Learning Source Attribution for Generative 3D Models](https://arxiv.org/abs/2605.18132)

**<font color=#1a73e8>作者：</font>** Sihan Ma, Siyuan Liang, Dacheng Tao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative 3D models are deployed in gaming, robotics, and immersive creation, making source attribution critical: given a 3D asset, can we identify whether and which generative model created it? This problem faces two core challenges: dispersed attribution signals, where 3D fingerprints are distributed across multi-view, geometric, and frequency-domain cues; and realistic deployment constraints, where scarce labels, degraded prompts, and mixed real/synthetic assets undermine attribution reliability. To systematically study this problem, we construct, to the best of our knowledge, the first passive source attribution benchmark for modern generated assets, covering 22 representative 3D generators under standard, few-shot, and realistic deployment protocols. Based on this benchmark, we find that generative 3D models leave two types of stable fingerprints: cross-view inconsistency and structural artifacts reflected in geometric statistics and frequency-domain cues. To capture these dispersed signals, we propose a hierarchical multi-view multi-modal Transformer that fuses appearance, geometric, and frequency-domain features within each view and models global relationships across views. Extensive experiments demonstrate strong performance, achieving 97.22% accuracy under full supervision and 77.17% accuracy with only 1% training data, corresponding to fewer than five samples per generator. These results show that modern 3D generators leave stable and attributable fingerprints, establishing a new benchmark and methodological foundation for trustworthy 3D content provenance.

---


### 492. [An Empirical Study of Privacy Leakage Chains via Prompt Injection in Black-Box Chatbot Environments](https://arxiv.org/abs/2605.18133)

**<font color=#1a73e8>作者：</font>** Hongjang Yang, Hyunsik Na, Daeseon Choi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based chatbot agents increasingly process user requests by combining natural-language reasoning with external tools such as web browsing. These capabilities improve usability, but they also create attack surfaces when untrusted external content is processed as part of a user' s task. This paper studies a privacy-leakage attack chain based on indirect prompt injection in black-box chatbot environments, where the attacker has no access to model weights, system prompts, or agent implementation details including how a trajectory is actually managed during its processing for a query. We first analyze how an attacker can hijack an agent' s intended task by crafting external content that appears benign to the victim while inducing the agent to execute an attacker-defined objective. We then evaluate a new prompt-injection technique, called exemplification, which uses a bridge in the external content to reframe the user prompt and the benign beginning of the retrieved page as few-shot examples before appending the attacker' s objective. We compare its attack success rate with a prior fake-completion technique. Finally, we demonstrate a proof-of-concept data-exfiltration chain using fictitious personal information in a controlled setting. Our results suggest that prompt injection, jailbreak-style instruction steering, and web-tool invocation can be combined into a feasible privacy-leakage path in deployed chatbot agents.

---


### 493. [Generative AI and the Productivity Divide: Human-AI Complementarities in Education](https://arxiv.org/abs/2605.18143)

**<font color=#1a73e8>作者：</font>** Lihi Idan, Bharat Anand  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative Artificial Intelligence (GenAI) is transforming how firms create, process, and apply knowledge, yet little is known about the heterogeneity of its productivity effects across users. We report results from a randomized controlled experiment in which participants-analogs of early-career knowledge workers-were assigned to self-study a technical domain using either traditional resources or large-language-model (LLM) assistance. On average, GenAI access significantly increased task performance, but the distribution of gains was highly uneven. Improvements were not predicted by GPA or prior knowledge, but by \textit{AI Interaction Competence (AIC)} -- the ability to elicit, filter, and verify model outputs. High-AIC participants realized outsized gains; low-AIC participants saw limited or even negative marginal returns. A scaffolding intervention (conceptual maps) reduced outcome variance, indicating that standardized workflows can mitigate inequality in AI-mediated performance. We interpret these findings through the lens of human-AI complementarities: GenAI raises mean productivity while introducing a new axis of capability inequality. Managerially, firms should pair GenAI access with short AIC micro-training and simple standard operating procedures to capture value consistently and avoid uneven adoption outcomes.

---


### 494. [DARTIC: Decentralized Anonymous Reputation at Scale for Trustworthy Crowdsourcing](https://arxiv.org/abs/2605.18146)

**<font color=#1a73e8>作者：</font>** Mouhamed Amine Bouchiha, Mourad Rabah, Ronan Champagnat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> On-chain crowdsourcing leverages blockchain's decentralization, transparency, and tamper-resistance to build trustworthy and verifiable Web3 crowdsourced services. However, existing decentralized reputation frameworks do not reconcile anonymity, reputation binding, and scalability. This paper demonstrates how on-chain crowdsourcing can simultaneously achieve these requirements under a trust-minimized model. We introduce DARTIC, a decentralized, anonymous, and scalable reputation-driven framework for crowdsourcing. DARTIC presents a dual-ledger system that enables requesters and workers to use distinct pseudonyms across interactions, ensuring unlinkability while maintaining accountability. To mitigate Sybil and reputation-reset attacks, we employ zkSNARK-based set membership proofs, cryptographically binding all user pseudonyms to a single access token without revealing the linkage. For scalability, we investigate two aggregation techniques that compress multiple proofs into a single succinct proof to minimize verification overhead. In addition, we design an automated, privacy-preserving reputation model that dynamically evaluates contributions across diverse crowdsourcing contexts. To demonstrate practicality, we instantiate and assess DARTIC in both crowdsensing and federated learning scenarios. Experimental results show that (i) individual proof generation for token spending completes in less than 3s, (ii) aggregation reduces the verification time of 1024 proofs from 8.7s to 0.96s, and (iii) zk-batching lowers gas costs by more than 100x compared to a pure Layer-1 deployment. These results demonstrate that anonymity, robust reputation binding, and scalability can be jointly achieved in fully decentralized crowdsourcing systems.

---


### 495. [In-Vehicle Human-Machine Interface to Support Drivers in Conditionally Automated Platooning](https://arxiv.org/abs/2605.18149)

**<font color=#1a73e8>作者：</font>** Anna-Lena Hager, Mohamed Sabry, Walter Morales-Alvarez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Vehicle platooning enables close-gap driving and offers potential benefits for traffic efficiency and safety. In conditionally automated platooning, drivers remain responsible for supervising the system and intervening when necessary, making effective Human-Machine Interfaces (HMIs) critical for maintaining situational awareness and stable driver-automation coordination. This paper investigates whether an in-vehicle HMI providing continuous system-state and inter-vehicle distance information improves supervisory behavior, safety, and platoon stability. We conducted a simulation-based experiment integrated with a 6-degree-of-freedom motion system to enhance scenario realism. Dependent variables included collision occurrence, response latency following platoon disconnection, and the number of manual interventions during intact platooning.
Results showed significantly fewer manual interventions when the HMI was active, with intervention rates about 80% higher without it. No significant effects were found for collision occurrence or response latency, indicating that additional information improves supervisory stability during platooning but does not substantially affect emergency reactions or collision rates.

---


### 496. [Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework](https://arxiv.org/abs/2605.18150)

**<font color=#1a73e8>作者：</font>** Mengyu Sun, Ziyuan Yang, Zunlong Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.

---


### 497. [FOL2NS: Generating Natural Sentences from First-Order Logic](https://arxiv.org/abs/2605.18155)

**<font color=#1a73e8>作者：</font>** Mei Jia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translating formal language into natural language is a foundational challenge in NLP, driving various downstream applications in semantic parsing, theorem validation, and question answering. In this study, we introduce First-Order Logic to Natural Sentence (FOL2NS), a neurosymbolic framework designed to generate synthetic FOL formulas and convert them into natural human expressions. It handles deeply nested structures with varying quantifier depths (QD), which are rarely captured by existing corpora. By combining rule-driven modules with fine-tuned language models, FOL2NS enhances the diversity and coverage of the generated samples. In our experiments, we systematically evaluate the framework's capabilities through both character-level analysis and overall performance metrics. Experimental results show that FOL2NS can reliably produce well-formed templates and fluent statements, but it faces challenges in achieving precise semantic representations and natural generation as structural complexity increases.

---


### 498. [Semi-LAR: Semi-supervised Contrastive Learning with Linear Attention for Removal of Nighttime Flares](https://arxiv.org/abs/2605.18156)

**<font color=#1a73e8>作者：</font>** Xiyu Zhu, Wei Wang, Kui Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lens flare removal is challenging due to the large spatial extent of flare artifacts and their entanglement with scene structures, while existing methods heavily rely on large-scale paired data. We propose a semi-supervised flare removal framework that enables stable learning from unlabeled images by jointly addressing pseudo-label reliability and representation discrimination. We propose an adaptive pseudo-label repository that progressively refines pseudo supervision through no-reference quality assessment, momentum-based updates, and invalid label filtering, effectively mitigating error accumulation. Moreover, we propose a flare-aware contrastive loss that explicitly treats flare-contaminated inputs as negatives and performs patch-level contrastive learning, encouraging representations that are discriminative against flare patterns while remaining consistent with reliable pseudo targets. Extensive experiments on multiple flare benchmarks demonstrate that the proposed framework is model-agnostic and consistently improves performance and robustness.

---


### 499. [TRACE: Trajectory Correction from Cross-layer Evidence for Hallucination Reduction](https://arxiv.org/abs/2605.18163)

**<font color=#1a73e8>作者：</font>** Tej Sanibh Ranade  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hallucination correction is not a one-direction problem. We show that intermediate layers are neither uniformly more truthful than final layers nor uniformly less trustworthy. Yet hallucination reduction is usually instantiated through one fixed intervention form: contrast one layer against another, steer along a truthfulness direction, or defer to external evidence. This framing is structurally incomplete. Cross-layer factual evidence does not evolve uniformly: in some failures truthful support is present internally and later suppressed, whereas in others candidate competition remains genuinely multi-directional across depth, so no single signed scalar family is generally sufficient. We introduce Trajectory Correction from Cross-layer Evidence for Hallucination Reduction (TRACE), a deterministic, training-free algorithm which corrects hallucinations at inference time by deriving both the corrective layer and the appropriate correction operator from each input's cross-layer candidate trajectory inside the LLM's own forward pass. Under one frozen hyperparameter setting, TRACE selects among scalar reversal, earlier-state recovery, and candidate-space correction using only model-internal evidence. Evaluated as a single universal algorithm across 15 models, 8 model families, and 3 factuality benchmarks, TRACE improves every evaluation cell, yielding mean gains of +12.26 MC1 points and +8.65 MC2-style points with no regressions, with gains reaching +47.20 MC1 and +43.38 MC2-style points. The method uses no labels, retrieval, pretraining, finetuning, or per-model calibration.

---


### 500. [Do You Need Text Rectification? Soft Attention Mask Embedding for Rectification-Free Scene Text Spotting](https://arxiv.org/abs/2605.18173)

**<font color=#1a73e8>作者：</font>** Antonio Colombo, Giovanni Bianchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end scene text spotting, which unifies text detection and recognition within a single framework, has witnessed remarkable progress driven by deep learning advances. However, most existing approaches still suffer from incomplete mask proposals caused by multi-scale variation, arbitrary text shapes, and complex background interference, thereby degrading recognition accuracy. In this paper, we propose a novel Soft Attention Mask Embedding module (SAME) that leverages the global receptive field of Transformer encoders to encode high-level features and compute soft attention weights, which are then hierarchically embedded with predicted masks to generate refined text-boundary-aware masks that effectively suppress background noise. Building upon this module, we present SAME-Net, a robust end-to-end text spotting framework that requires neither character-level annotations nor auxiliary text rectification modules. Since the soft attention mechanism is fully differentiable, recognition loss gradients can be back-propagated through the SAME module to the detection branch, enabling joint optimization of detection and recognition objectives. Extensive experiments on challenging benchmarks demonstrate the effectiveness of our approach: SAME-Net achieves 84.02\% end-to-end H-mean on the arbitrarily-shaped Total-Text dataset, surpassing the previous state-of-the-art GLASS by 1.02\% in full-lexicon accuracy without additional training data, and obtains competitive 83.4\% strong-lexicon results on the multi-oriented ICDAR 2015 dataset.

---


> [!TIP]
> 当前位于：**451-500**（第 10/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
