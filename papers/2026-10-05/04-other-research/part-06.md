# 📦 其他研究 | 2026年10月05日

> 本类共 **385** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-385](./part-08.md)

---

### 251. [Auditing Routing Entropy as an Uncertainty Signal in Attention-Residual Transformers](https://arxiv.org/abs/2610.01495)

**<font color=#1a73e8>作者：</font>** Wenhao Liang, Lin Yue, Wei Emma Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic architectures leave a per-example routing trace beside each prediction, and diffuse routing is easy to read as a sign that the prediction is unreliable. We audit that reading for routing entropy in Attention-Residual (AR) variants of Swin-Tiny and DeiT-Small, trained from scratch on CIFAR-10/100 with a soft-binned calibration auxiliary loss, asking whether the trace carries information about correctness beyond what the model's own confidence already reveals. Three checks probe this increment: does a routing signal appear at fixed confidence, does it replicate across training seeds, and can a held-out predictor exploit it against output-only and shuffled-trace controls? A sensitivity audit then injects effects of known size and measures the fraction of each that the probes recover. No test in the fixed 30-test binned family survives multiplicity correction, and neither the nominal hit nor a borderline result recurs in its sibling seeds. Across 24 paired runs a scalar routing probe yields no pooled improvement in routing-stratified calibration, and an entropy-profile probe predicts correctness better than the same probe given shuffled profiles yet worse than a confidence-only predictor in both binary log-loss and Brier score: a gain over shuffled traces does not become a gain over the output. Conditioning on the complete logit vector leaves the corresponding comparison unresolved. The audit bounds how far these non-detections can be read: at an injected effect of 0.010 nats the profile probe recovers 24-59% of the oracle gain, and a reference-preserving correction probe recovers 8% and 23% in the two CIFAR-100 settings, below the threshold we fixed for applying it to real labels. The results establish control-dependent gains and incomplete estimator recovery, not the absence of conditional routing information.

---


### 252. [VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in Video Generation](https://arxiv.org/abs/2610.01499)

**<font color=#1a73e8>作者：</font>** Yu Huang, Jungang Li, Zhiyuan Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generation models can produce highly realistic videos from natural language instructions, with visual quality approaching cinematic standards. Existing evaluation benchmarks, however, predominantly assess visual quality, aesthetic appeal and physical plausibility, while paying limited attention to text, an essential medium for conveying information in everyday scenes. A generated video may appear visually compelling and feature lifelike subjects, yet still render the text within the scene incorrectly. To address this overlooked dimension, we introduce \textbf{VTR-Bench}, a systematic benchmark for evaluating the \textbf{V}isual \textbf{T}ext \textbf{R}endering capabilities of video generation models. VTR-Bench situates text within concrete application scenarios, such as advertisements and scientific videos, with 300 carefully constructed prompts spanning five scenario categories. We develop an automated evaluation pipeline with human alignments that separately assesses text fidelity through carrier-specific transcription and scene and motion requirements through a prompt-specific chain of query. Beyond evaluation, we introduce a \textbf{Keyframe-Guided Agentic Framework} in which a Director agent coordinates image and video generation with visual evaluation, guiding iterative refinement and candidate selection through visual feedback. Experiments on 11 state-of-the-art models reveal widespread difficulties in accurately rendering scene text, with the best-performing model recording an overall word error rate (WER) of 0.250. We further analyze text rendering failures to characterize the challenges faced by current video generation models. These findings highlight visual text rendering as a key challenge for video generation and demonstrate a practical path toward improvement. Code is available at this https URL.

---


### 253. [Learned End-to-End Guidance Schedules for Diffusion Models](https://arxiv.org/abs/2610.01502)

**<font color=#1a73e8>作者：</font>** Aneesh Barthakur, Mathias Niepert, Luiz F.O. Chamon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are a powerful generative paradigm used across multimedia and scientific applications. Guided diffusion methods impose requirements on the generation by adding the gradient of a differentiable loss (the guidance function) as a drift term during inference. The weight of this drift (the guidance scale) is critical for the trade-off between data quality and requirement satisfaction. To achieve both of these goals, guided diffusion must resort to small guidance scales and lengthy sampling, incurring high computational costs. This work proposes learned end-to-end guidance schedules (LEEGS) to achieve these objectives with fewer sampling steps. LEEGS trains a time-dependent schedule by minimizing the guidance function over a small set of examples using stochastic gradient descent. Backpropagating through guided sampling is computationally expensive, so LEEGS uses an approximation of the gradient that cuts training time by a factor of 4. We evaluate LEEGS on diverse guidance tasks, including (a) image inpainting, (b) noisy image inverse problems, (c) face-ID-guided generation, and (d) forward and inverse PDE problems, outperforming baselines at equal budget (50 or 100 NFEs), or matching constant guidance with only 10% of the steps.

---


### 254. [FedCKA: Representation-Guided Layer Personalization for Federated 3D Perception Across Driving Domains](https://arxiv.org/abs/2610.01510)

**<font color=#1a73e8>作者：</font>** Jolle Verhoog, Ali Burak Ünal, Holger Caesar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust perception in intelligent vehicles demands 3D object detectors that remain dependable under domain shifts, such as changes in time of day, location, or weather. However, due to costly annotation and rare shifts, some environments lack sufficient data to train a standalone detector. Federated learning offers a privacy-preserving framework for collaborative model training, enabling clients to benefit from shared learning across diverse environments. Yet, this framework traditionally relies on a single global consensus model, which struggles to perform across heterogeneous local data distributions. Local conditions are better captured by adapting a subset of the model, but many personalization approaches rely on predefined layer partitions or fixed personalization ratios, thereby limiting adaptation to client-specific divergence. To reduce this rigidity, we propose FedCKA, a Centered Kernel Alignment (CKA)-based strategy that dynamically handles the personalization-globalization trade-off. Specifically, FedCKA computes layer-wise feature similarities between local client models and the global consensus model during training. By converting layer-wise similarity scores into client-specific aggregation masks, FedCKA selectively shares representation-consistent layers. Evaluation on a unified multi-domain benchmark based on nuScenes shows that FedCKA outperforms established federated baselines, including FedBN, FedRep, and FedSelect, improving average NDS by 7 percentage points over the strongest baseline. The findings offer both a comparative benchmark and a promising direction for robust federated 3D perception across shifts in location, weather, and illumination. Code is available at this https URL.

---


### 255. [VoxelSynth3D: Interpretable Volumetric Image-Domain Metal Artifact Reduction with a Paired Synthetic CLINIC-Metal Benchmark](https://arxiv.org/abs/2610.01512)

**<font color=#1a73e8>作者：</font>** Amritesh Banerjee, Abdul Basit, Renil Renji Joseph 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metal artifacts in postoperative musculoskeletal CT obscure bone-implant and adjacent soft-tissue interfaces. Many metal artifact reduction (MAR) methods require unavailable raw projections or learned models that may shift across scanners and implants. We present VoxelSynth3D, a training-free 3D image-domain framework for reconstructed CT. The framework combines support masking, normalized tissue synthesis, deviation gating, and restricted edge refinement. Detected implant voxels are preserved in the output, while correction targets metal-induced artifacts in the surrounding tissue. We also construct Synthetic CLINIC-Metal, a controlled paired synthetic evaluation resource, from no-metal CTPelvic1K volumes with clean targets, metal/artifact masks, fixed seeds, and patient-level splits; 75 unpaired real metal cases receive qualitative/no-reference evaluation only. The operating point was fixed in a near-flat validation basin. With exact-mask oracle localization, all methods share a metal-excluded tissue ROI. On 40 held-out cases, VoxelSynth3D reduced RMSE from 801.48 to 786.18 HU (paired gain 15.30 HU, 95% CI 11.68-19.23), improving every case and exceeding the evaluated 3D Gaussian smoother by 13.58 HU. Clean-edge agreement decreased next to metal but exceeded input beyond 5 mm. Thus, VoxelSynth3D provides case-consistent within-distribution tissue-error reduction with a localized structural tradeoff. Spacing-aware sensitivity retained aggregate broad-region improvement and identified near-metal calibration as a target.

---


### 256. [Decision Titan: Test-Time Training for Long-Term Memory in Offline Reinforcement Learning](https://arxiv.org/abs/2610.01513)

**<font color=#1a73e8>作者：</font>** Jude Waide, Robert Lieck  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term dependencies remain a major challenge for sequential decision-making in the field of AI: RNNs suffer from vanishing gradients and the limited expressivity of vector-based hidden states, whilst Transformer-based models are limited by the quadratic scaling of attention. Recent work has proposed tackling this problem with the Test-Time Training (TTT) framework, which stores episodic memories in the parameters of a neural network through gradient descent at both train and test-time. This approach has seen success in the domain of Natural Language Processing, however, to the best of our knowledge it has not yet been applied to the domain of Reinforcement Learning (RL), nor has there been a study analysing how this memory practically functions. In this paper, we study the potential of the TTT framework for offline RL by augmenting a Decision Transformer with TTT layers, dubbed the Decision Titan. We analyse performance and properties of the model in the X-Maze environment, an extension of T-Maze designed to test sequential memory, and investigate how the memory mechanism learns by visualising gate values over time. Our key findings are that Decision Titan can learn long-term dependencies with ranges 20x longer than the context window, generalises to lengths 1.7x the training data, but crucially temporal generalisation depends on the time embeddings used, and the ability to learn long-term dependencies depends on how the relevant information is encoded.

---


### 257. [SuperMotion: Source-Preserving Denoising for Text-Driven Human Motion Editing](https://arxiv.org/abs/2610.01517)

**<font color=#1a73e8>作者：</font>** Fa-Ting Hong, Peter Wonka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven human motion editing aims to realize a requested change while preserving compatible source content. Existing diffusion editors rely largely on learned conditioning for preservation of the unedited part, yet their outputs can lose temporal detail as denoising proceeds. We propose the \textbf{Source-Preserving Denoising framework (SuperMotion)}, which explicitly reuses the source at each reverse step for source preservation. We first align the source motion to the output timeline and predict a preservation gate that controls reuse across frames and feature dimensions. A clean-space source anchor then utilizes the learned preservation gate to blend the predicted clean motion with the aligned source and passes the corrected estimate directly to the sampling posterior. Because the aligned source is a realized motion rather than a regression output, the anchor injects sample-level temporal detail that a reconstruction-trained denoiser tends to smooth away. To learn effective source reuse, we supervise the anchored estimate against the editing target and match its second temporal differences through a temporal high-frequency loss. These objectives require no explicit edit masks. Extensive experiments show that SuperMotion improves editing accuracy, reaching 33.20\% full-pool R@1 on MotionFix, while reducing temporal-detail attenuation and preserving motion dynamics as it realizes the requested changes. Ablations confirm that the learned preservation gate is responsible for the gain and that it reuses the source to retain the unedited content properly.

---


### 258. [Langevin-Informed Transfer Learning: Replacing Target Samples by Black-Box Feedback](https://arxiv.org/abs/2610.01522)

**<font color=#1a73e8>作者：</font>** Vladimir R. Kostic, Karim Lounici, Hélène Halconruy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many scientific and machine learning systems, from molecular dynamics to diffusion models and beyond, are governed by stochastic dynamics with low-dimensional structure, evolving on slow timescales. However, target trajectories, used to identify and interpret such dynamics, are often inaccessible: only biased or static samples that explore the underlying manifold are available. We introduce Langevin-Informed Transfer Learning (LITL), a framework for recovering target Langevin dynamics from biased source samples using only black-box feedback. LITL learns the leading spectral structure of the target infinitesimal generator and the projected drift through Dirichlet representation learning, enabling kinetic reconstruction in spectral form and slow-manifold gradient field estimation. We further introduce a spherical variant well suited to steering normalized latent representations commonly used in learning systems toward desired objectives. We establish finite-sample guarantees for eigenvalue, eigenfunction, and projected drift estimation in Sobolev norms, thereby ensuring generalization of these quantities and their first-order derivatives. Empirically, LITL recovers physical transition timescales from biased molecular simulations, builds kinetic structure from static samples of generative models, reconstructs spherical symmetries of physical systems, and enables post-hoc latent steering of trained neural networks under black-box feedback. Together, these results position spectral operator learning as a practical framework for recovering stochastic dynamics under distribution shift and unlock applications across machine learning and the physical sciences.

---


### 259. [Exact Distinguishability in Non-Markovian Decision Processes](https://arxiv.org/abs/2610.01527)

**<font color=#1a73e8>作者：</font>** Kabir Murjani, Nisarg Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-Markovian environments are often modeled as Regular Decision Processes (RDPs), where dynamics depend on the interaction history through a finite automaton. Existing offline guarantees for RDPs rely on a distinguishability assumption on the behaviour policy but provide no means of verifying it. When the assumption is violated, distinct models may explain the data equally well. We study when data collected under a fixed behaviour policy can distinguish two candidate RDPs. We prove that the posterior odds between observationally equivalent candidates remain equal to the prior odds at every sample size, even when the policy visits every automaton state, and verify both results formally in Lean 4. We then characterize this equivalence exactly and derive PEC, an algorithm that decides it in time linear in the size of the product automaton. The distinguishability assumption of prior work fails on three of our four test environments, and the experiment identified by PEC restores it in each case.

---


### 260. [Calibrating Prediction Timeliness Through Multi-Objective Hyperparameter Optimization for Remaining Useful Life Prediction](https://arxiv.org/abs/2610.01530)

**<font color=#1a73e8>作者：</font>** Tugrul Cabir Hakyemez, Ener Uras Gokhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In predictive maintenance, early and late RUL prediction errors carry asymmetric consequences, yet hyperparameter optimization typically targets a single accuracy metric that treats both directions equally. This study treats the optimization objective itself as a design variable. Five architectures (MLP, LSTM, XGBoost, TCN, and Transformer) are evaluated under three regimes: single-objective maximization of $R^2$, single-objective minimization of the NASA scoring function, and a multi-objective formulation that jointly optimizes both criteria. The multi-objective search employs NSGA-II with Entropy-CRITIC weighting for Pareto selection. Seventy-five model-dataset-strategy combinations are assessed on the NASA C-MAPSS turbofan and BackBlaze hard-disk drive benchmarks. On C-MAPSS, all strategies achieve comparable accuracy ($R^2 \approx 0.89$), yet multi-objective optimization reduces directional imbalance by approximately 33%, improving calibration of early versus late predictions. Model rankings prove configuration-dependent, with simpler architectures frequently outperforming deeper temporal models. On BackBlaze, the objectives shift from complementary to conflicting, producing divergent Entropy-CRITIC weights and a substantial generalization gap (best $R^2 \approx 0.34$). These results demonstrate that the optimization objective materially shapes prognostic behavior and that multi-objective search provides a practical mechanism for calibrating prediction timeliness in RUL modeling.

---


### 261. [Neither Black nor White: Balancing Semantic and Collaborative Signals with Graph-Informed Semantic IDs (GrIS)](https://arxiv.org/abs/2610.01533)

**<font color=#1a73e8>作者：</font>** Aleksei Medvedev, Alejandro Ariza-Casabona, Steven Derby 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing work on Semantic IDs (SIDs) for generative recommendation treats SID construction as a representation learning problem: encode items into a quantised latent space and read off codes. We argue this view is incidental. SID construction is, at heart, a recursive clustering problem, and once stated this way the natural object to cluster is a graph whose nodes carry semantic content and whose edges carry collaborative signal; SID assignment becomes a hierarchical graph partition. This reframing yields a unified framework, Graph-Informed Semantic IDs (GrIS), that subsumes prior approaches rather than displacing them. RQ-VAE and RQ-KMeans are recovered as the special case where the graph is empty, exposing content-only quantisation as one corner of a larger design space along two so-far-collapsed axes: graph construction and recursive partition algorithm. We explore two contrasting instantiations: RecDMoN, which performs hierarchical assignment via differentiable graph pooling, and RQ-GAE, which extends RQ-VAE with graph-aware item representations and a graph reconstruction objective. On multiple real-world datasets, GrIS consistently improves over CF-aware SOTA, with gains of up to +52\% Hit@10. Because graph construction and partition are explicit, separately configurable components, improvements on either axis can be combined and evaluated systematically.

---


### 262. [The AI Assessment Sandbox Configurator: A Framework to Support Technical Assessment in AI Regulatory Sandboxes](https://arxiv.org/abs/2610.01539)

**<font color=#1a73e8>作者：</font>** Alessio Buscemi, German Castignani, Daniele Pagani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The EU's Artificial Intelligence Act requires all Member States to establish AI Regulatory Sandboxes (AIRS) by August 2027: supervised environments bringing together national Competent Authorities, technical experts, and the organisations under assessment. When AIRS engagements include structured technical testing, running such testing at scale demands dedicated infrastructure, yet the tooling ecosystem remains structurally fragmented, with heterogeneous tools producing outputs that are difficult to compare, trace, and reuse. From the procedural conditions of AIRS engagements and the AI Act obligations for high-risk systems, we derive 11 architectural and governance requirements for the infrastructure that operationalises technical testing within an AIRS. In response to these requirements, we introduce the AI Assessment Sandbox Configurator, an open-source framework combining a curated Catalogue of tests and controls accessed through a stable plug-in API, a shared data model that harmonises heterogeneous outputs, role-specific dashboards for multi-disciplinary interpretation, and audience-segmented reporting. We describe the architecture and current release, and report an early-stage pilot that exercised the harmonisation and reporting layers within a live AIRS engagement and contributed to an official Exit Report. We discuss the roadmap, the governance questions raised by the Catalogue's tiered contribution model, and the institutional pathways through which an open-source assessment ecosystem could emerge across Member States.

---


### 263. [Synthetic training for long-tail haemorrhagic lesion segmentation in data-scarce settings](https://arxiv.org/abs/2610.01542)

**<font color=#1a73e8>作者：</font>** Yuan Cao, Sumeet Dash, Antonia Zachariadis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cerebral microbleeds (CMBs) and cortical superficial siderosis (cSS) are imaging markers of cerebral small vessel disease, but their automated segmentation is limited by the scarcity of positive cases and voxel-level annotations. We propose a synthetic training framework for long-tail haemorrhagic lesion segmentation that requires no real lesion annotations for training and leverages radiological description of the lesions. Starting from anatomical brain parcellations, the framework applies spatial augmentation and voxel resampling, procedurally inserts cSS and CMB labels using clinical priors on lesion location and morphology, and synthesises images through randomised intensity assignment, blurring, and Rician noise simulation. Models were trained on dynamically generated image-label pairs and evaluated against manual delineations in 10 cSS cases and 13 CMB cases. The proposed configurations outperformed classical filter baselines. For cSS, the hypointensity constrained model achieved higher AUPRC and AUROC than the Frangi filter (AUPRC: 0.284 vs 0.083; AUROC: 0.907 vs 0.731). For CMBs, explicit synthesis of blood vessels as lesion mimics improved performance over the classical baseline (AUPRC: 0.538 vs 0.004; AUROC: 0.999 vs 0.968). These results support our proposal as a feasible strategy for data-scarce haemorrhagic lesion segmentation.

---


### 264. [Revisiting Cross-Reconstruction for Generalizable Deepfake Detection](https://arxiv.org/abs/2610.01544)

**<font color=#1a73e8>作者：</font>** Bingjian Yang, Shilei Zhao, Zheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing image forgery detectors often suffer from generalization to unseen manipulation methods due to the limited ability to capture transferable forensic cues. Recent cross-reconstruction based methods attempt to improve generalization through semantic-artifact disentanglement, but typically align heterogeneous artifacts across generators and exclude artifact representations during reconstruction, which may overlook the inherent diversity and visual cues of manipulation artifacts. In this work, we revisit cross-reconstruction and introduce an artifact-oriented disentanglement framework for robust image forgery detection. We argue that \textbf{artifact diversity}, i.e., the intrinsic variations of manipulation artifacts introduced by different generation processes, contains complementary forensic cues rather than undesirable domain variations. Instead of enforcing explicit artifact alignment, our framework preserves diverse artifact characteristics through semantically aligned cross-generator reconstruction. Furthermore, we incorporate artifact representations into the reconstruction process and introduce a masked frequency-aware reconstruction strategy to emphasize manipulation-related residuals while reducing semantic interference. This design enables the model to learn transferable forensic representations from diverse artifacts. Extensive experiments on multiple benchmark datasets demonstrate improvements under both cross-dataset and cross-generator evaluation settings. Further analysis and ablation studies validate the effectiveness of artifact diversity preservation and artifact-aware cross-reconstruction.

---


### 265. [Towards Optimal Policy Improvement](https://arxiv.org/abs/2610.01566)

**<font color=#1a73e8>作者：</font>** Yaniv Oren, Viliam Vadocz, Wiktor Zabka 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Practical Reinforcement Learning (RL) algorithms learn to solve Markov Decision Processes (MDPs) through iterative policy improvement in the presence of approximate evaluation. We study policy improvement from first principles, defining optimal policy improvement as producing the best policy attainable in a single update under specified constraints. We show that optimal improvement restricted to a set of states is equivalent to solving an induced MDP, characterizing planning with an explicit or implicit model as a path towards optimal policy improvement. Because practical methods commonly solve such induced problems through iterative improvement in the form of greedification, we take steps towards optimal greedification under the central practical constraint of approximate evaluation. We formulate greedification under this constraint as probabilistic decision-making under uncertainty and derive a novel operator that is optimal with respect to the resulting objective. Empirically, the operator and its practical gradient-based approximations improve aggregate performance across GumbelAlphaZero, SAC, ReBRAC and Generalized Policy Iteration, in experiments spanning discrete and continuous actions, model-based and model-free, online and offline RL.

---


### 266. [Beyond Pointwise Error: A Multi-Metric Evaluation of Spatial Climate Downscaling](https://arxiv.org/abs/2610.01579)

**<font color=#1a73e8>作者：</font>** Loys Masquelier, Etienne Le Naour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Climate downscaling aims to reconstruct fine scale spatial fields from coarse resolution inputs. Evaluating the quality of these reconstructions is challenging: low pointwise error can come at the cost of fine scale variability, while realistic spatial variability can be achieved with inaccurate local structures. The evaluation metric can therefore change which method appears to perform best. This work presents a multi metric benchmark comparing five spatial downscaling methods on ERA5 temperature, wind, and precipitation fields. Five criteria assess complementary properties: pointwise error, structural similarity, distribution error, spectral error, and gradient error. The results reveal a systematic trade off between spatial fidelity and fine scale variability. Some methods perform best on pointwise and spatially aligned metrics, but lose high frequency content, while others preserve substantially more spectral variability at the cost of less accurately positioned local structures. Consequently, method rankings change across metrics and variables. These results show that there is no single best downscaling method. Multi metric evaluation is therefore essential for assessing which properties of a climate field are preserved.

---


### 267. [Protocol Integration of Physical Layer Deception into EAP-TEAP Wi-Fi Authentication](https://arxiv.org/abs/2610.01580)

**<font color=#1a73e8>作者：</font>** Moustafa Ibrahim, Bin Han, Hans D. Schotten  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Credential-based Extensible Authentication Protocol (EAP) authentication cannot distinguish a legitimate credential holder from an adversary using compromised credentials. Physical Layer Deception (PLD) complements credential-based authentication by exposing a deceptive primary object over a primary transport while a separate recovery object travels with differentiated reliability over a secondary channel. Existing PLD studies remain, to our knowledge, at the physical/link-model level; using PLD's activation/deactivation mechanism as an authentication gate creates an authentication-specific design requirement, since an all-inactive attempt would exercise no recovery path. We present a batched PLD-based re-verification step for Enterprise Wi-Fi's TEAP/RADIUS/IEEE 802.11 authentication chain, implemented end to end across the server, access point, and device in the open-source hostap 2.12 codebase. Each attempt carries three rounds, at least one active, with no dedicated activation flag. Across four campaigns totaling 1593 attempts, the prototype evaluates batched recovery behavior, rejects the implemented naive credential-bearing attacker in all 30 attempts, measures successful-path latency, and evaluates the security-reliability trade-off for one, two, and three active rounds under two modeled recovery regimes. The evaluation exercises the protocol and software-MAC behavior directly and analyzes informed and retry-seeking attackers under the software recovery model.

---


### 268. [PAGER: Partial-to-global Alignment via Geometric and Relational Distillation](https://arxiv.org/abs/2610.01589)

**<font color=#1a73e8>作者：</font>** Akira-Miranda Adeyomi Adeniran-Lowe, Binod Singh, Lars Arnold Dethlefsen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained 3D encoders are typically developed on globally reconstructed scenes expressed in a consistent world coordinate frame, whereas embodied systems must reason from partial, viewpoint-dependent observations in camera coordinates. We show that this shift from globally learned 3D feature spaces to realistic partial observations exposes a severe representation mismatch, which we find consistently across representative state-of-the-art encoders, including Sonata and Concerto. A frozen Sonata encoder with a global linear probe achieves 72.47 mIoU on full ScanNet scenes, but 2.57 mIoU on single-frame camera-coordinate inputs. Training-free gravity alignment recovers performance to 41.64 mIoU, showing that coordinate-frame mismatch is a dominant source of degradation but cannot be fully resolved through canonicalization alone. We introduce PAGER, a label-free adaptation method that aligns partial-view features with a frozen global 3D semantic space using only paired partial/global geometry. It learns lightweight adaptation modules while keeping the pretrained encoder and global segmentation probe frozen. Matched-point feature alignment anchors partial features to their global counterparts, while relational supervision preserves their similarity structure with respect to the global representation. Global geometry provides supervision only during training. Inference operates directly on the partial observation. Without partial-view labels, PAGER outperforms label-supervised PEFT on both Sonata and Concerto, and in zero-shot ScanNet$\rightarrow$ScanNet++ transfer surpasses fully fine-tuned Sonata ($53.93$ vs.\ $48.09$ mIoU), suggesting that preserving the frozen global representation can improve cross-dataset transfer.

---


### 269. [Two Routes to the Middle: Placement Search and Brain Readouts Converge on Where Continual Learners Should Specialize](https://arxiv.org/abs/2610.01590)

**<font color=#1a73e8>作者：</font>** Yuan Huang, Zihan Chen, Runbin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learners that keep a task-specific adapter in every block of a pre-trained vision transformer accumulate storage linearly with the number of tasks; keeping task-specific adapters in only a few blocks curbs this growth but raises the question of where to place them. We investigate this question from two perspectives. Algorithmically, training all contiguous four-block placements yields an inverted U: final accuracy peaks at intermediate depth and varies by up to 3.5 percentage points (pp), while inexpensive criteria based on weight spectra or activation statistics favor the deepest blocks. From neuroscience, the hierarchical organization and intermediate-stage plasticity of the visual cortex motivate us to ask whether a measurement taken outside the learner can guide layer specialization without placement search. LS-B observes the first tasks through a frozen fMRI encoding model of twelve human visual areas and commits task-specific capacity once to the blocks whose readouts vary most across tasks relative to their stable structure. Across three ViT-B/16 backbones, LS-B yields stable, backbone-specific allocations. On the two backbones with placement search, AugReg and iBOT, the selected blocks overlap the intermediate-depth region identified by search. Under matched storage and observation budgets, the selected blocks outperform the shallowest and deepest four-block configurations. On Split ImageNet-R, LS-B uses 60% of full-BiLoRA adapter storage while remaining within 1.5 pp of its final accuracy. The allocation requires no labels or backpropagation, adds under 0.6% runtime, and exhibits backbone-specific cortical signatures.

---


### 270. [Hob-VL: A Benchmark for Visually Grounded Boolean Reasoning](https://arxiv.org/abs/2610.01605)

**<font color=#1a73e8>作者：</font>** Yuzhou Wang, Emile Anand, Ijay Narang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable visual reasoning requires composing multiple visual observations and returning consistent answers to logically equivalent questions. We introduce Hob-VL, a benchmark for visually grounded Boolean reasoning. Hob-VL comprises two tasks: (1) evaluating whether a Boolean rule holds in an image, and (2) identifying the (unique) object satisfying a Boolean description. Hob-VL contains 6,000 human-verified balanced Yes/No questions, each defined by a Boolean combination of ten visual statements, across 1,000 generated scenes and 46 diverse labeled photographs, along with 1,000 object-identification questions over the same photographs. Our question families are deliberately constructed to challenge reasoning through misleading local cues and nested logical operations, and include symbolic and structured natural-language presentations. Across eight model configurations with thinking disabled or minimized, Boolean accuracy ranges from 48.52% to 50.57%, while the identification accuracy reaches at most 43.0%. A thinking-enabled GLM configuration achieves uneven gains while retaining substantial errors and inconsistencies. Hob-VL exposes these failures through executable reference answers and matched evaluations.

---


### 271. [Exposing the Cost of Deep Learning Audio Development](https://arxiv.org/abs/2610.01619)

**<font color=#1a73e8>作者：</font>** Constance Douwes, Paul Magron, Romain Serizel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The environmental impact of deep learning has attracted increasing attention over the past decade. Existing studies mainly focus on the energy and carbon emissions of model training and inference, while the whole development phase is often overlooked. Yet, architecture prototyping and intensive experiments are conducted during this stage, which is highly energy-demanding. In this article, we propose a methodology to estimate these costs, based on activity logs from the Grid5000 shared computing platform used by the LORIA laboratory. As a case-study, we focus on audio projects developed in the Multispeech research team. We evaluate the overall energy cost of four projects, and we compare them to those of training the reported models. Our results show that the energy required for the development phase is 3 to 256 times greater than that required to train the best-performing model alone. These results advocate for a more systematic reporting of energy consumption across the entire life cycle of deep learning-based audio projects.

---


### 272. [FedLore: Communication and Memory Efficient Federated Learning via Shared Gradient Low-Rank Projection](https://arxiv.org/abs/2610.01620)

**<font color=#1a73e8>作者：</font>** Junkang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated training of foundation models is constrained by client memory and communication costs. LoRA-based methods reduce these costs through low-rank adapters, but their fixed rank budget can limit adaptation. Gradient low-rank optimization offers greater flexibility, yet independently chosen client subspaces create a problem we term \emph{subspace fragmentation}: local projections interact with data heterogeneity to bias aggregated directions, while aggregation can increase update rank and communication cost. Thus, accurate local gradient compression need not preserve global descent. We propose \texttt{FedLore}, which shares a low-rank optimization basis within each round and refreshes it across rounds. The shared basis enables exact aggregation in low-rank coordinates and eliminates the identified projection bias. Subspace refresh allows the accumulated model update to exceed the per-round rank budget. We characterize the aggregation bias and establish an $O(T^{-1/2})$ stationarity bound for the projected-SGD variant under a global-gradient coverage condition and standard smoothness and variance assumptions, with bounded gradient heterogeneity. Experiments on vision and language tasks, including federated pre-training, show that \texttt{FedLore} outperforms the evaluated low-rank adapter baselines and matches or exceeds full-parameter training, while reducing communication and optimizer-state memory.

---


### 273. [Measuring the Stability Assumption Behind Action Chunking](https://arxiv.org/abs/2610.01626)

**<font color=#1a73e8>作者：</font>** Aryan Goyal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Action chunking improves the performance of policies learned by behavioural cloning, and several mechanisms have been proposed to explain why, including temporal consistency, horizon reduction, representation learning, and reduced error compounding. We instead study what happens to an action error once it enters the system. At each state, we inject a small action error and measure how fast it grows or shrinks under two execution regimes: open-loop, where the rest of the chunk is replayed without replanning, and closed-loop, where the policy replans after the perturbation. The fitted rate labels each state as contracting, expanding, or unresolved. Across twelve manipulation tasks from three benchmark suites, we find that confidently stable states are rare, while error amplification is common among states whose propagation rate can be resolved. We further find that the measured propagation rate depends strongly on the fitting horizon: amplification is typically front-loaded, so short windows can overestimate longer-horizon propagation. Finally, we train predictors on these labels and find that a state's open-loop regime can be recovered from camera frames and proprioception alone, while its closed-loop propagation is only partially recoverable because it also depends on how the policy acts after the perturbation. These results suggest that error-compounding arguments alone do not provide a complete account of action chunking: neither passive open-loop dynamics nor policy replanning consistently contracts an injected error, and replanning rarely turns open-loop amplification into confident contraction. This suggests that closed-loop reactivity should be trained explicitly, using perturbation- and tree-coverage-oriented training to expose policies to deviations they must recover from, rather than expected to emerge reliably from standard imitation learning.

---


### 274. [After Cooperation Is Learned: Gradient Routing and Optimizer-Dependent Maintenance in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.01630)

**<font color=#1a73e8>作者：</font>** Chaoyuan Hao, Wentao Yue, Tianyou Lai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cooperative MARL is commonly evaluated through cooperation discovery from random initialization, leaving open whether continued optimization can destabilize learned cooperation. Actor-critic comparisons can also conflate critic presence with value gradients entering shared actor representations. We study cooperation maintenance, defined as the survival of a behaviorally verified cooperative policy under continued training. We formulate maintenance as a right-censored event-time problem and compare matched warm starts: X0 allows value loss gradients to update shared actor features, X1 retains the critic while blocking those gradients, and X5 removes the learned critic as a critic-free reference. This isolates direct value-gradient access while controlling initialization, critic computation, and evaluation. Positive reward scaling preserves strategic preferences and equilibria while perturbing learning dynamics. Gradient audits confirm the intended routing pathways, and frozen-policy torso perturbations probe whether route-induced updates align with local cooperation boundaries. In confirmatory MinEx and CleanUp-lite experiments, higher scales selectively increase maintenance sensitivity in X0; X1 remains near the censoring ceiling, and X5 has no confirmed events in the tested settings. In CleanUp-lite, route-by-scale displacement is associated with reduced local cooperation margins; MinEx shows a weaker, optimizer-dependent effect. These results identify a conditional, scale-sensitive maintenance risk associated with direct value-gradient routing rather than a universal failure of critics.

---


### 275. [Generalization in Neural Networks Through the Lens of Magnitude Potential](https://arxiv.org/abs/2610.01633)

**<font color=#1a73e8>作者：</font>** Sahel Torkamani, Henry Gouk, Rik Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explaining generalization and training dynamics in neural networks remains a challenge, and various approaches have been developed to study different aspects of these phenomena. In this paper, we introduce the idea of {\em magnitude potential} -- a quantity based on the theory of metric magnitude -- that reflects how well an arbitrary point is represented by a given set. We find that this basic quantity can be applied to examine various features in neural generalization. The ratio between the magnitude potential with respect to a class and with respect to the entire data, computed at the logit layer, is informative of the representation of the point. In experiments, these ratios for individual training points are found to be correlated with the Feldman memorization scores. Magnitude potential ratios aggregated across points detect structural changes in the decision boundaries and provide a geometric indicator of grokking in modular arithmetic. Although the magnitude potential ratio and neural collapse are both closely associated with intra-class and inter-class geometric structure, the magnitude potential ratio remains informative even when neural collapse is explicitly suppressed.

---


### 276. [Fusing Visual and Textual Representations via Multi-layer Fusing Transformers for Vietnamese Visual Question Answering](https://arxiv.org/abs/2610.01637)

**<font color=#1a73e8>作者：</font>** Cong Phu Nguyen, Huy Tien Nguyen, Tung Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent decades, artificial intelligence has made significant progress in understanding and interacting with images. One of the important applications of this technology is Visual Question Answering (VQA), a research field that requires computers to understand and answer questions about images in a natural manner. Despite extensive research and development in VQA for English, there have been very few similar efforts made for other languages, especially Vietnamese. This gap presents a significant challenge and opportunity for the advancement of VQA technology in the Vietnamese language context. By bridging this gap, the field of Vietnamese VQA not only enriches the diversity of research in artificial intelligence but also enables practical applications in various domains, such as education, healthcare, and entertainment, catering to Vietnamese-speaking populations worldwide. Thus, the exploration and development of Vietnamese VQA systems hold immense potential for advancing both research and practical applications in the intersection of computer vision and natural language processing. In this paper, we propose a Multi-layer Fusing Transformer model utilizing a cross attention module to combine multiple modality features of images and texts from different layers in an aggregated representation. Our architecture allows us extract information from low level to high level. Through detailed experiments and ablation studies, our model achieves promising results against the competitive baselines in ViVQA dataset for Vietnamese language.

---


### 277. [FedSAP: Federated Learning with Structured Adaptive Partitioning for Multi-Domain Heterogeneous Edge Devices](https://arxiv.org/abs/2610.01638)

**<font color=#1a73e8>作者：</font>** Wentao Yue, Tianyou Lai, Hongji Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) on heterogeneous edge devices must jointly accommodate unequal resource budgets and domain-shifted local data. Existing resource-adaptive methods decide how much of a model each client trains but not where retained capacity should reside or how it should be shared, whereas federated domain-generalization methods usually assume a shared full architecture. Uniform compression can therefore discard high-utility channels, and a single aggregation path can mix transferable features with domain-sensitive updates. We propose FedSAP, a domain-aware heterogeneous FL framework that casts structured pruning as budget-constrained tri-state channel allocation. FedSAP converts each keep ratio into non-uniform layer budgets, assigns stable channels to a Global pool, useful domain-sensitive channels to pseudo-domain-specific Private pools, and low-utility channels to a Dropped state. This partition lets broadly useful features benefit from cross-client pooling while isolating domain-sensitive updates from incompatible clients. Domain-Guided Assignment infers pseudo-domains from shallow-gradient similarity, while Type-Matched Aggregation restricts each channel to its intended sharing scope. Across three random seeds, FedSAP reaches 76.00% and 72.67% mean global accuracy on Digits and Office-Caltech, exceeding the strongest baseline by 1.70 and 4.92 percentage points while supporting client pruning ratios of up to 80% across heterogeneous clients.

---


### 278. [MCIR: A Feature Dependence-Aware Explainability Method with Reliability Guarantees](https://arxiv.org/abs/2610.01641)

**<font color=#1a73e8>作者：</font>** Poushali Sengupta, Sabita Maharjan, Frank Eliassen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine-learning models often contain strongly dependent or redundant features, making feature attribution difficult because shared predictive information can be distributed across correlated predictors. Existing methods such as SHAP, LIME, HSIC, MI/CMI, and SAGE may therefore produce unstable rankings under multicollinearity or near-duplicate predictors. We propose the Mutual Correlation Impact Ratio Method (MCIR-M), a dependence-aware global feature-importance approach that quantifies the unique predictive information contributed by each feature beyond a selected dependence neighbourhood. MCIR-M introduces the Mutual Correlation Impact Ratio (MCIR), which conditions each feature on strongly dependent neighbours and computes a normalized ratio of conditional to block-level information. The population score lies in [0,1] and equals zero under exact conditional redundancy. We also introduce a lightweight estimation procedure that computes MCIR using a fraction of the available data and evaluates agreement with full-data explanations. Across controlled synthetic redundancy experiments and the UCI HAR benchmark, MCIR shows dependence-aware ranking behaviour, with its clearest advantage under injected near-duplicate predictors. Comparisons with independent and conditional SHAP, SAGE, HSIC, MI-based scores, and CIR-family baselines are mixed across real-data criteria. Reduced explanation samples lower computational burden in the evaluated configurations, while agreement with full-data explanations is assessed separately through ranking, head-set, and faithfulness diagnostics. Overall, MCIR-M provides a practical dependence-aware diagnostic for global explanation under strong feature dependence.

---


### 279. [Beyond Demographic Balance: Multi-Metric and Intersectional Evaluation of Fairness in MIMIC-IV Mortality Prediction](https://arxiv.org/abs/2610.01645)

**<font color=#1a73e8>作者：</font>** Abdullah Al Noman, Fahmid Al Rifat, Tahrima Hashem 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness conclusions in clinical prediction can depend strongly on both the metrics reported and the demographic resolution at which performance is evaluated. We revisit these evaluation choices for ICU mortality prediction on MIMIC-IV, comparing predictive-utility and subgroup-error metrics across several fairness interventions. As a complementary case study, we introduce a lightweight adaptation strategy that jointly balances ethnicity--gender--insurance representation without conditioning on mortality outcomes, allowing demographic representation balancing to be examined separately from outcome-conditioned or direct error-rate interventions. We evaluate its behavior at both marginal and corresponding three-way intersectional subgroup levels, while accounting for the statistical support of finer-grained estimates. The results show that interventions can receive substantially different assessments across accuracy/AUROC, sensitivity, and false-positive rate, and that marginal demographic summaries can conceal heterogeneous error profiles within their constituent intersections, including among larger subgroups. These findings highlight the importance of evaluating fairness interventions at both complementary metric and subgroup resolutions, while accounting for the intervention target and the reliability of subgroup estimates.

---


### 280. [CrossGMN: Graph Metanetworks for Cross-Architecture Weight-Space Transformations](https://arxiv.org/abs/2610.01649)

**<font color=#1a73e8>作者：</font>** Adir Dayan, Yam Eitan, Haggai Maron  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-space networks operate directly on parameters of other neural networks, enabling tasks such as predicting model properties, editing trained models, and generating weights. Weight-space symmetries such as neuron permutations make equivariance a key design principle. However, existing equivariant weight-space architectures have primarily been studied for transformations that preserve the network architecture. In contrast, many practical transformations, including model compression and upscaling, map a trained source network into a target network with a different architecture. In this setting, the source and target permutation symmetries act on different parameter spaces, making equivariance less straightforward to formulate. Our key idea for addressing this mismatch is to reformulate cross-architecture operators with two inputs: a trained source network and an initialization of the target network. This lets us define equivariant cross-architecture operators that refine the initialization of the target network using information from the source network, while being invariant to source-network permutations and equivariant to target-network permutations. Based on this formulation, we introduce CrossGMN, a graph metanetwork that jointly processes both networks through symmetry-preserving cross-network message passing. We prove CrossGMN is universal for continuous cross-architecture operators on compact sets under a general-position assumption. We evaluate CrossGMN for model compression, predicting a smaller network's parameters to accelerate subsequent knowledge distillation. Across 2-D and 3-D INRs and image classification with MLPs, CNNs, and Vision Transformers, CrossGMN speeds up distillation by up to 8.89x, transfers across datasets without retraining (3.78x), and a single model can accelerate compression from heterogeneous source architectures into a common target architecture.

---


### 281. [Combining Homomorphic Encryption and Differential Privacy in Federated Learning for Model Inspection and Availability](https://arxiv.org/abs/2610.01650)

**<font color=#1a73e8>作者：</font>** Ceren Yıldırım, Kamer Kaya, Sinan Yıldırım 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing prevalence of decentralized data has led to a growing interest in federated learning, which enables collaborative model training without clients sharing their sensitive local data. However, FL alone does not sufficiently protect sensitive training data and is generally coupled with privacy-preserving techniques, such as differential privacy and homomorphic encryption. Although powerful, these techniques address separate concerns via different mechanisms, so relying on just one might prove insufficient or impractical for addressing challenges associated with federated learning. In this work, we propose a privacy-preserving federated learning framework that combines homomorphic encryption-based training with differential privacy-based model inspection and release. We adopt a Markov chain Monte Carlo-based Bayesian privacy estimation method to estimate the privacy of our proposed framework. Our results show that this method improves both model utility and estimated privacy over the baseline method that relies solely on differential privacy for training. In our experiments with the FEMNIST dataset, by the end of training, our method reaches a test loss of $1.09$, compared to $2.37$ for the differential privacy-only approach, while providing stronger estimated privacy protection, with the estimated posterior mean of the privacy parameter $\epsilon$ of $4.32$, compared to $7.26$ for the differential privacy-only approach. We also show that intermittent model monitoring can preserve the encrypted training trajectory while, under our evaluated experimental setting, providing estimated privacy comparable to or stronger than the differential privacy-only approach.

---


### 282. [DiVid: Diagnosing Dimension-Specific Diversity Collapse in Video Generation Models](https://arxiv.org/abs/2610.01661)

**<font color=#1a73e8>作者：</font>** Huanran Hu, Zihui Ren, Dingyi Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress, video generation models often produce highly similar outputs when repeatedly sampled from the same prompt, limiting their usefulness for creative exploration. Existing diversity evaluations primarily rely on global scalar metrics, which obscure where diversity collapses in the spatiotemporal space of videos. We introduce DiVid, a dimension-level diagnostic framework that decomposes video generation diversity into six interpretable dimensions: Semantic, Style, Subject, Scene, Motion, and Camera. Each dimension is measured through a reproducible computer-vision pipeline and analyzed alongside quality and instruction faithfulness to examine potential trade-offs. Systematic evaluation of representative video generation models reveals that diversity is highly dimension-specific: models with strong global diversity scores still collapse on specific factors, particularly Motion and Camera. These rankings persist after filtering unfaithful generations, indicating genuine capability differences rather than off-prompt outputs. Beyond measurement, controlled prompt interventions identify two fundamental bottlenecks: default mode convergence, where models fall back to dominant patterns under open-ended prompts; and realization gaps, where models fail to faithfully realize diverse, explicitly requested alternatives, particularly for temporal factors. The larger faithfulness losses for temporal factors highlight the difficulty of controlling motion and camera variation through text alone. DiVid thus shifts the study of diversity from measuring whether it exists to diagnosing where and why it collapses, and provides actionable directions for dimension-aware training objectives and control signals. The framework will be released to facilitate future research on diverse and controllable video generation.

---


### 283. [pCoMole: Pareto-Constrained Molecule Editing with Discrete Flows](https://arxiv.org/abs/2610.01663)

**<font color=#1a73e8>作者：</font>** Tong Chen, Maximilian Holsman, Lin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biomolecular therapeutics often start from known sequences and require targeted editing to improve multiple properties while satisfying hard biochemical and manufacturability constraints. However, existing generative methods do not jointly support multi-objective optimization, hard feasibility, and sequence editing in discrete, variable-length biological spaces. In this work, we introduce Pareto-Constrained Molecule Editing (pCoMole), a framework built on discrete flow matching that steers a pre-trained Edit Flow toward user-specified preferences while enforcing terminal feasibility. pCoMole defines a feasibility-gated terminal distribution using an augmented Tchebycheff utility and realizes the resulting preference tilt through a Doob-h transform of the underlying edit process. To make this construction practical, we approximate the required harmonic function using short Monte Carlo rollouts over candidate edits, yielding an efficient guided editor with provable preference consistency. We validate pCoMole by shrinking GFP while retaining fluorescence-related properties, shortening diverse Cas9 orthologs while preserving PAM specificity, and compressing peptide binders into short peptidomimetics that optimize seven drug-related properties under hard constraints. In wet lab testing, two 229-residue pCoMole-designed eGFP variants retained clear green fluorescence in BL21 cells after 10 deletions, with either one or two substitutions. Together, pCoMole enables constraint-aware, Pareto-aligned editing of biomolecular sequences in discrete, variable-length spaces.

---


### 284. [When Text-to-Image Helps Editing: The Effects of Conditioning During Denoising](https://arxiv.org/abs/2610.01681)

**<font color=#1a73e8>作者：</font>** Lidia Troeshestova, Alexander Ustyuzhanin, Sergey Kastryulin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified models are trained for both instruction-based image editing and text-to-image (T2I) generation, but standard editing pipelines keep source-image conditioning throughout denoising. We ask whether editing can benefit from T2I, and study how the effects of conditioning vary across edits and denoising stages. In pure editing, source attention declines for some edits over the sampling trajectory. This observation led us to task switching, which lets the model draw on its T2I capabilities. Across three unified editors and four benchmarks, switching to the T2I task for bounded intervals improves edit quality, while mean perceptual preservation remains close to pure editing across all three models. Unified editors therefore benefit from using both conditioning modes they are trained for, and the timing of the switch sets the balance between quality and preservation.

---


### 285. [MiLoop: Selective Memory Propagation for Neural Combinatorial Optimization](https://arxiv.org/abs/2610.01685)

**<font color=#1a73e8>作者：</font>** Changliang Zhou, Yuanyao Chen, Rongsheng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constructive neural combinatorial optimization (NCO) has emerged as a promising paradigm that learns to construct solutions to combinatorial optimization problems (COPs) step by step, which reduces reliance on handcrafted rules and enables fast inference. While many methods with dynamic embeddings generalize well, they typically rebuild subproblem representations from scratch at each step using deep attention stacks. Many high-performing methods in this category rely on solution labels or pseudo-labels for efficient training, or on aggressive search space pruning during reinforcement learning (RL). To address these limitations, we propose Memory-in-the-Loop (MiLoop), a purely RL-based constructive framework that leverages the multi-step computation already required by a rollout for selective memory propagation. Each rollout provides solution-quality feedback for learning while propagating historical representations, thereby enabling a shallow policy to learn effective dynamic embeddings without external solution labels or training-time search-space pruning. Specifically, MiLoop fuses current embeddings with historical memory before the attention layers and applies adaptive gated updates afterward. The updated representations support both current decisions and stepwise reuse. Extensive experiments across four COPs demonstrate that MiLoop consistently produces high-quality solutions on instances ranging from 100 to 10 million nodes, highlighting its strong generalization ability.

---


### 286. [Compound interpretation is based on analogy](https://arxiv.org/abs/2610.01688)

**<font color=#1a73e8>作者：</font>** Tian Shen, Harald Baayen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How compound meanings are best predicted from constituent meanings remains a central question in computational models of lexical semantics. Comparing different computational models provides a way to evaluate alternative accounts of how semantic information is combined during compound comprehension. We propose a new model, the Compound Analogy Model (CAM), that predicts a compound's embedding by adding its constituent embeddings together with the average shift vectors of the two constituents' compound families. The resulting model is parameter-free and exploits local analogical structure in the semantic space. We evaluated CAM against the CAOSS model on Mandarin Chinese compounds. CAM consistently achieved higher prediction accuracy than CAOSS on both training and held-out data, with the exception of three-character compounds, for which analogical generalization is constrained by both small constituent families and a pronounced imbalance in family size between the two constituents. The advantage of CAM remained when evaluation was based on frequency-defined train-test splits that better approximate generalization from familiar to novel compounds. To assess the cognitive plausibility of the two models, we further examined whether model-derived semantic measures predict visual lexical decision latencies for two-character compounds. Predictors derived from CAM provided improved prediction for response latencies compared to predictors derived from the CAOSS model. These findings indicate that compound meaning is better characterized as local analogical generalization than as the application of a learned global linear transformation, and demonstrate that analogical semantic structure provides a cognitively plausible basis for compound comprehension.

---


### 287. [Artifact Annotations Partially Substitute for Per-User Calibration: SAFE-EDA and a Normalization-Controlled Evaluation of Wrist-EDA Affect Recognition](https://arxiv.org/abs/2610.01692)

**<font color=#1a73e8>作者：</font>** Haochen Chai, Xinbi Luo, Zining Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wrist electrodermal activity (EDA) differs in amplitude from one person to the next, so affect-recognition models normalize their input before classification. Studies that test such models on held-out subjects seldom report where the normalization statistics come from, yet statistics computed from the held-out subject's own recording give the model information that a device does not have when it is first worn. We asked how this choice alters the measured benefit of pretraining. A compact convolutional network, SAFE-EDA, was pretrained on expert artifact annotations from 43 subjects and compared with the same network trained from scratch on the Wearable Stress and Affect Detection (WESAD) dataset (15 subjects, leave-one-subject-out), with two normalization sources crossed with four window hops. When the statistics came only from training subjects, pretraining raised macro-F1 by 0.078 to 0.227; when they came from the held-out user's full recording, the gain fell to between 0.020 and 0.050 and was no longer significant. Artifact supervision was far more useful than self-supervised pretraining on the same recordings (0.078 versus 0.008). Across 13 configurations in two datasets, the pretrained network was better in 12, but on the second dataset (26 subjects) per-user normalization increased the gain instead of reducing it, so the interaction depends on the data. Only five of 50 published WESAD studies state which data were used for normalization. Reporting this choice is necessary to separate first-use performance from performance after calibration.

---


### 288. [Learning PDE Dynamics between Submanifolds Using Green's Observation Operators](https://arxiv.org/abs/2610.01697)

**<font color=#1a73e8>作者：</font>** Jan Tauberschmidt, Jephte Abijuru, Samuel Okon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many physical systems are driven and observed only on lower-dimensional submanifolds of a larger spatial domain, while their dynamics are governed by the ambient medium occupying that domain. Examples include laser-heated parts imaged by an infrared camera, and ground-level emissions measured on a sensor plane. Full-domain solvers, however, compute the entire volume for every new source although only the observation submanifold is needed, and black-box surrogates do not exploit that the ambient medium remains fixed. We introduce the \emph{Green's Observation Operator (GObO)}, which maps the ambient medium once to the Green's kernel of a linear PDE restricted to the source and observation submanifolds. New sources then cost one lower-dimensional integral and no network evaluation. Exponential rates in the kernel yield an exact finite streaming state with horizon-independent memory; we prove its stability and an approximation rate for the restricted heat kernel. On three-dimensional heat conduction and advection--diffusion with collocated and distinct source and observation geometries, GObO trained on static sources predicts responses to moving sources zero-shot with 4--8$\times$ lower error than black-box surrogates, at 1.4\,ms per query after a single conditioning pass. The same kernel transfers across resolutions and admits corrections for mild nonlinearities, including radiative losses and temperature-dependent conductivity, without retraining, at the cost of lower in-distribution accuracy.

---


### 289. [Task-Oriented Rank Adaptation for Continual Learning in Text Classification](https://arxiv.org/abs/2610.01702)

**<font color=#1a73e8>作者：</font>** Rey Sanchez Lopez, Eduardo Morales Manzanares, Hugo Jair Escalante  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) in text classification faces two critical challenges: catastrophic forgetting and negative transfer across sequential tasks. Parameter-Efficient Fine-Tuning (PEFT) methods such as LoRA enable efficient adaptation by learning low-rank updates of the model parameters. However, these compact representations are normally trained in isolation, limiting their reuse across related tasks. We introduce Task-Oriented Rank Adaptation (TORA), a geometric routing framework that leverages the low-rank structure of LoRA adapters to decide whether to transfer knowledge from the most compatible expert (Boosting) or isolate the new task (Shielding) based on structural similarity. Evaluated across 15 diverse text classification benchmarks, TORA consistently avoids harmful routing decisions: compatible tasks exceed their isolated performance while reducing training time, and structurally distant tasks are protected from interference with no loss in accuracy. With a single geometric threshold and no reliance on task identities or predefined sequences, TORA provides a simple and effective approach for dynamic adapter routing in sequential text classification systems.

---


### 290. [MEGA: Object-Level Mesh Extraction from 3D Gaussian Splatting via Spatial Visual Distillation](https://arxiv.org/abs/2610.01707)

**<font color=#1a73e8>作者：</font>** Liwei Liao, Yingkui Zhang, Qianqian Tong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mesh extraction from 3D Gaussian Splatting (3DGS) aims to endow 3D Gaussians with accurate geometric structures, enabling explicit and precise 3D occupancy. However, existing methods primarily focus on scene-level mesh extraction, making them unable to represent object-level occupancy and often resulting in non-watertight surfaces. To overcome these limitations, we propose \textbf{MEGA} (\underline{M}esh \underline{E}xtraction from \underline{GA}ussians), a ``segment-then-mesh'' framework for extracting object-level, watertight meshes from complex 3DGS scenes. At the core of MEGA are \textbf{Spatial Visual Distillation (SVD)} and a mask-guided neural surface reconstruction module. SVD treats the 3DGS model as a teacher, sampling diverse camera poses and rendering the corresponding views of each segmented object. These observations are then used to train a mesh reconstruction model through photometric supervision. Extensive experiments on several widely used benchmarks demonstrate that MEGA achieves state-of-the-art performance in recovering accurate object-level 3D occupancy. Moreover, MEGA enables complex physical interactions by combining high-quality object-level meshes for geometric occupancy with 3DGS representations for photorealistic rendering.

---


### 291. [CoEvolve: Construct-to-Edit Visual Grounding with Bidirectional State Refinement](https://arxiv.org/abs/2610.01710)

**<font color=#1a73e8>作者：</font>** Dongwei Sun, Yujie Zhang, Bowen Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual grounding localizes an object described by language with a bounding box. Most multimodal grounding models compress target identification, spatial reasoning, and boundary estimation into one terminal prediction. Free-form rationales make reasoning linguistically explicit but do not necessarily expose measurable, editable spatial states. Intermediate localization errors are therefore difficult to diagnose and correct, allowing incorrect region choices and imprecise boundaries to persist in the final box. We introduce CoEvolve, a construct-to-edit framework that separates grounding into explicit state construction and state editing. Region-Evolution Reinforcement (RER) organizes grounding analysis into a progressive semantic--spatial trajectory, with each reasoning step committing to an explicit candidate region. Bidirectional Denoising Refiner (BDR) treats the reasoning text as fixed semantic context and refines the trajectory's coordinate fields through bidirectional same-position reconstruction. Geometry- and behavior-level objectives provide target geometry and edit-preference signals for consolidating reliable candidates, preserving accurate inputs, or correcting toward annotations. Evaluations cover natural-image and remote-sensing grounding. With a 9B backbone, CoEvolve rivals models up to 241B parameters in grounding accuracy. Under controlled corruption, a single BDR pass improves mean box overlap by over 27 percentage points, demonstrating strong recovery from substantial localization errors. State-source comparisons further support the complementarity of explicit state construction and source-matched editing. The project is at this https URL.

---


### 292. [vFedProtoQNAS: Prototype-Guided Personalized Quantum Neural Architecture Search for Virtual Federated Learning](https://arxiv.org/abs/2610.01718)

**<font color=#1a73e8>作者：</font>** Seok Bin Son, Samuel Yen-Chi Chen, Soohyun Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantum federated learning (QFL) has emerged as a promising approach for collaboratively training compact quantum neural networks (QNNs) over distributed private data on resource-constrained devices. However, differences in device capabilities make a single shared QNN architecture unsuitable for all clients. While personalized quantum neural architecture search (QNAS) allows each client to select a device-specific QNN, averaging parameters across structurally different QNN architectures mixes semantically inconsistent circuit operations. To address this, prototype-guided personalized QNAS for virtual FL (vFedProtoQNAS) is proposed, where model parameters are never aggregated across clients and federated collaboration is achieved through class-wise prototype sharing. Each client independently searches and trains a client-specific QNN, computes class-wise local prototypes from latent representations, and refines them using global prototypes from the server as federated semantic anchors. Experiments demonstrate that vFedProtoQNAS improves accuracy by 3.70\% over FedAvg and enhances class-consistent representation alignment.

---


### 293. [Anomaly Detection and Localization for the Pantograph-Catenary System](https://arxiv.org/abs/2610.01721)

**<font color=#1a73e8>作者：</font>** Francesco Vitale, Hangli Ge, Francesco Flammini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monitoring the Pantograph-Catenary System (PCS) provides insight into the health conditions of the pantograph and the railway infrastructure. Recent industrial solutions trace the pantograph's contact wire height and stagger (PCS height/stagger) using video monitoring through convolutional neural networks. However, these solutions do not account for the train route's geographic location. Therefore, in this paper we propose a novel framework for 1) localization of the PCS height/stagger by alignment with the nominal GPS coordinates of the reference route, and 2) collective anomaly detection to evaluate the health conditions of the PCS. We apply and assess the localization and detection performance of the methodology to a case-study based on a real-world industrial dataset provided by a railway transportation company, which includes the PCS height/stagger of several train journeys across Italian railway routes.

---


### 294. [Rethinking Memorization Mitigation in Diffusion Models: Reinforcing Text Conditioning](https://arxiv.org/abs/2610.01723)

**<font color=#1a73e8>作者：</font>** Hyungjun Joo, Sehwan Kim, Hyeonggeun Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models have achieved remarkable progress in image synthesis, yet can exhibit memorization by closely reproducing individual training examples. Effective mitigation must preserve useful prompt information to guide alternative depictions. We introduce a training-free method that redistributes cross-attention with Gaussian smoothing before reinforcing content-token contributions and attenuating padding contributions, without additional denoiser evaluations. With this intervention, stronger content conditioning can improve prompt alignment at comparable training-image similarity. A local analysis identifies when reinforcement preserves shared value information while redistribution reduces localized attention mass. On Stable Diffusion v1.4 and v2.0, all evaluated smoothing widths lie on the empirical Pareto frontiers for training-image similarity versus both prompt alignment and image preference. A configuration selected on Stable Diffusion reduces template reproduction in DeepFloyd IF without further tuning. These findings support jointly controlling conditioning allocation and strength to generate prompt-consistent alternatives.

---


### 295. [Removing spurious minima for planar features by skip connections](https://arxiv.org/abs/2610.01728)

**<font color=#1a73e8>作者：</font>** Jakob Paul Zimmermann, Moritz Grillo, Andrei Balakin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding loss landscapes is central to explaining neural-network training, yet their structure remains only partially understood even in simple models. We study the Gaussian population loss of shallow, bias-free ReLU networks in the teacher--student setting. This provides a simple model for studying essential aspects such as feature learning and overparameterization. For teacher networks with positive output weights and planar features, we show that including a learned linear skip removes all spurious local minima with non-negative student output weights once the student network is at least as wide as the teacher network. In contrast, without the skip, we construct a fixed teacher network with positive output weights and only three hidden neurons in input dimension two whose spurious local minima persist at every student width at least three. Thus, a learned linear skip can remove spurious minima that persist under arbitrary overparameterization. Furthermore, we show that a positive output weight student network always learns the subspace spanned by the teacher features: student features at local minima with non-negative student output weights lie in the span of the teacher features. For ReLU networks in two dimensions, even heavily overparameterized student networks have effective width controlled by the teacher width: every critical point with positive student output weights has at most twice as many distinct student feature directions as teacher neurons. Finally, we transfer the benignity result to empirical minima over parameter balls of any prescribed radius, with the required sampling accuracy depending on that radius.

---


### 296. [The Achilles' Heel of Partial Reconfiguration: Optical Side-Channel Leakage on the 7-Series ICAP](https://arxiv.org/abs/2610.01736)

**<font color=#1a73e8>作者：</font>** Antonio Saavedra, Jan Caspar Marx, Lars Renkes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Major FPGA manufacturers have incorporated bitstream encryption to protect sensitive configuration data. However, for the most widely used FPGA families, multiple attacks against unpatchable protection schemes hard-wired into the devices can bypass or fully break them, making patchable schemes desirable.
In this work, we present a proof-of-concept implementation of an AMD-proposed asymmetric key encryption scheme for bitstream protection for 7-Series FPGAs, using partial reconfiguration from the Programmable Logic. We analyze the security implications and hardware overhead of this implementation. We then propose and demonstrate an optical side-channel attack that is able to recover plain-text configuration data during the dynamic reconfiguration process. This attack leverages Photon Emission Microscopy and Electro-Optical Probing to first locate and then contactlessly extract the plain-text data from the ICAP interface, which internally connects the Programmable Logic with the configuration logic.
We located the ICAP buses in an AMD XC7A200T device and show that the data on it can be extracted with Electro-Optical Probing. We claim that even advanced encryption schemes utilizing Partial Reconfiguration and custom cryptographic engines are vulnerable to optical attacks, as reconfiguration is only possible via hard-wired, vulnerable configuration interfaces.

---


### 297. [Fixed-point neural samplers on discrete spaces](https://arxiv.org/abs/2610.01739)

**<font color=#1a73e8>作者：</font>** Jiajun He, Denis Blessing, Mouyang Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from discrete, unnormalized distributions without access to data is a challenging problem. Neural samplers offer a promising approach by training generative models from density evaluations directly. Despite recent progress, existing discrete neural samplers are prone to mode collapse, come without convergence guarantees when trained via fixed-point iterations, and are often tied to a specific reference process such as masked or uniform diffusion. In this work, we introduce Discrete Gibbs Iterative Neural Sampler, a fixed-point neural sampler that addresses these limitations, enabling efficient, scalable learning, substantially reducing mode collapse in practice. Our framework builds on masked diffusion and also extends to transport between pairs of distributions. We demonstrate that the resulting method scales effectively to high-dimensional systems, supports amortized sampling across different conditions, and enables accurate estimation of alloy phase diagrams.

---


### 298. [3DROID: A Renderable 3D Gaussian Dataset with Measured Per-Scene Reliability](https://arxiv.org/abs/2610.01744)

**<font color=#1a73e8>作者：</font>** Wonguen Cho, Junhoo Lee, Nojun Kwak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robot manipulation models primarily reason from 2D observations while acting in the 3D physical world. To bridge this gap, recent work has augmented robot data with geometric priors such as depth, point clouds, and 3D trajectories, while renderable 3D Gaussian representations provide another promising form of 3D supervision. However, 3DGS representation is designed mainly for photometric fidelity and may not preserve real-world metric scale, particularly when the supplied camera extrinsics are unreliable. We study the effect of extrinsic reliability and pose conditioning on feed-forward 3DGS, and propose a calibration-aware pipeline that anchors reconstructed scenes to the robot's metric workspace. Our experiments show that pose conditioning improves novel-view fidelity, while its geometric benefit depends on the reliability of the injected extrinsics. Using this pipeline, we present a renderable, metric-pose-anchored dataset with scene-level reliability information for robot manipulation research. Our dataset is available at this https URL

---


### 299. [FFBL-Coop: Association-Decoupled Cooperative 3D Multi-Object Tracking](https://arxiv.org/abs/2610.01750)

**<font color=#1a73e8>作者：</font>** Haoxin Wu, Xiaokai Bai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cooperative 3D tracking must integrate complementary observations across agents and time while maintaining consistent identities. When evidence integration and identity inheritance share a matching decision, errors arising from cross-view appearance differences and spatial misalignment can compromise both feature fusion and track continuity. We propose FFBL-Coop, a fuse first, bind later framework that separates instance admission from identity management. Confidence-ranked Slot Admission (CSA) allocates cooperative queries to available ego slots using confidence and spatial proximity. Unified Representation Aggregation (URA) uses cooperative semantic features and aligned anchors to guide ego-feature retrieval, refining the augmented query bank within a shared transformer decoder. After refinement, Cooperative-Priority Identity Anchoring (CPIA) combines learned association with persistent mappings to establish accepted identity assignments across frames. A shared codebook reduces transmitted payload while retaining AP and AMOTA close to the uncompressed variant. FFBL-Coop achieves AMOTA/AP of 0.611/0.548 on V2X-Seq and 0.688/0.653 on Griffin-25M. Code will be released.

---


### 300. [Evidence-Gated Research: Statistically Controlled Model Adoption in Adaptive Search](https://arxiv.org/abs/2610.01751)

**<font color=#1a73e8>作者：</font>** Yifan Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive model search is path dependent: once a challenger is adopted, it becomes the reference from which later candidates are generated. A statistically unsupported replacement can therefore alter hypotheses that have not yet been proposed. We introduce Evidence-Gated Research (EGR), a statistical adoption layer for moving-incumbent search. EGR freezes each challenger before decision evidence is revealed, builds anytime-valid evidence across a predeclared set of environments, routes evidence predictably toward unresolved components, composes a persistent candidate e-value, and passes that e-value to an online controller. Under explicit conditional-validity and predictability conditions, the resulting procedure controls false discovery rate for the declared all-environment adoption target even though earlier adoptions change later challengers. In a 5,000-trajectory closed-loop benchmark, development-only e-LOND attains persistent FDR 0.621, whereas no persistent false-adoption path is observed for the audited EGR variants in that finite run. In matched replay over 600 challenger--incumbent pairs, Stagewise EGR preserves fixed-anytime alternative crossing decisions while using 56.1% less decision evidence at the representative threshold. A three-environment public-data study and a 40,000-sample controlled neural benchmark reproduce the evidence-efficiency pattern. These results identify model replacement as a distinct statistical control point in adaptive model development.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-385](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
