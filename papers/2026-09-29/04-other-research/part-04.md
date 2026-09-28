# 📦 其他研究 | 2026年09月29日

> 本类共 **225** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-225](./part-05.md)

---

### 151. [AtomWorld-Mem: Memory-Restored World States for Long-Horizon Atomistic Evolution](https://arxiv.org/abs/2609.31133)

**<font color=#1a73e8>作者：</font>** Tian Luo, Ruge Zhang, Haozhi Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-fidelity atomistic evolution over long timescales requires more than observing the current crystal configuration. Instantaneous atomistic snapshots are often incomplete: locally similar configurations can correspond to different hidden dynamical contexts, future event preferences, and waiting-time scales. We argue that this snapshot ambiguity makes long-horizon atomistic evolution fundamentally a memory-based world-state restoration problem. To address this, we introduce AtomWorld-Mem, a memory-restored atomistic world model that recovers the latent world state missing from instantaneous crystal snapshots. AtomWorld-Mem treats the evolving alloy as an AtomWorld: spatial encoders write multi-scale atomistic keyframes from dense local topology and sparse long-range defect context, while short-term event memory and long-term structural memory integrate these keyframes across time to restore a future-predictive evolutionary state. The restored state is used to prioritize legal vacancy-mediated events under single-event Kinetic Monte Carlo (KMC) constraints, while event legality, physical execution, and residence-time updates remain governed by the underlying simulator. Empirically, AtomWorld-Mem improves long-horizon atomistic progress under fixed microscopic event budgets while maintaining high-fidelity evolution across energetic, structural, and vacancy-transport observables. It further transfers zero-shot across diverse unseen alloy-temperature AtomWorlds, suggesting that the learned memory-restoration mechanism captures reusable principles of hidden-state inference rather than a system-specific local energy heuristic. These results position memory-restored world-state modeling as a promising route toward efficient, physically grounded, and transferable atomistic evolution.

---


### 152. [Toward AI-Augmented Cooperative Engineering Workflows: Requirements and Architecture the European Rover Challenge](https://arxiv.org/abs/2609.31136)

**<font color=#1a73e8>作者：</font>** Ahmed R. Sadik, Frank Joublin, Mariusz Bujny 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing availability of Artificial Intelligence (AI) tools creates new opportunities to support engineering design processes, yet their current use often remains limited to isolated tasks such as coding, documentation, or information retrieval. Less attention has been given to how AI can support cooperative engineering workflows at the process level, where teams must coordinate requirements, tasks, communication, knowledge transfer, and subsystem integration. This paper investigates this challenge in the context of the European Rover Challenge (ERC), where student teams design and integrate complex rover systems within a single academic cycle under strict time constraints and high subsystem interdependence. We conducted a role adaptive 40 question survey with ERC 2025 teams, yielding 104 responses from 14 teams. The survey examined team structure, knowledge transfer, task management, integration practices, communication patterns, and current AI usage. The results reveal recurring workflow bottlenecks, including limited documentation, unclear requirements, fragmented communication, informal task monitoring, and substantial integration rework. Based on these findings, we derive requirements for AI augmented cooperative engineering work-flows and propose an initial assistant system architecture that connects user facing interfaces, credential management, service selection, specialized AI services, and external engineering tools. The proposed architecture aims to support task clarification, requirement and compliance management, communication summarization, integration risk detection, and continuous knowledge capture. In doing so, the paper contributes empirical requirements and an architectural direction for AI augmented cooperative engineering workflows in hybrid human AI team settings.

---


### 153. [JevAdvBench: A Benchmark and Black-Box Attacks for Reinforcement Learning for Calibrated Decisions Models](https://arxiv.org/abs/2609.31142)

**<font color=#1a73e8>作者：</font>** Jianyi Hu, Hangtao Zhang, Yi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Models trained with reinforcement learning for calibrated decisions (RLCD), such as Jev, answer a typed question about an input, the state, with a probability, a choice, or a score, and software acts on the answer without a person reading it. Their robustness has not been measured: adversarial benchmarks score what a model generates or executes, whereas a typed model generates nothing and returns a well-formed answer even when manipulated. Measurement is also hard, because identical requests can return different answers, most available labels come from the model itself, and the API preprocesses each request out of view. Our key idea is to score each attacked decision against the model's own clean decision rather than against labels, and to read it against the change caused by an identical re-run. Building on this, we introduce JevAdvBench, to our knowledge the first adversarial benchmark for RLCD models, with 812 typed questions over 66 scenarios, and a black-box attack suite of 9,744 single-edit variants that each edit one part of a request, with billed input tokens confirming that the edit reached the model. On jev-1.13.0, rewording stays within 1.2 percentage points of the re-run baseline, and fields outside the schema never reach the model. In contrast, one unverified opinion appended to the state flips 12.1% of decisions, statistically tied with the strongest injected command (10.1%), and pushes 38% of confident answers below the 0.8 confidence threshold that routes them to human review. Applications built on RLCD models should therefore treat the state as untrusted, argued input. Project website: this https URL

---


### 154. [Seeing Semantic Shift: Difference-Aware Sentence-Level Temporal Segmentation of Sign Language Videos](https://arxiv.org/abs/2609.31148)

**<font color=#1a73e8>作者：</font>** Bowen Guo, Shiwei Gan, Yafeng Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in sign language understanding have achieved impressive success on short, single-sentence videos, yet their performance drops sharply when applied to long, continuous sign language videos. To bridge this gap, we focus on a challenging and realistic setting: Visual-only Sentence-level Sign Language Segmentation (Vis-SSLS), which aims to partition continuous sign language videos into non-overlapping sentence-level segments without any caption assistance, serving as a crucial prerequisite for downstream recognition and translation tasks. However, sentence transitions in sign language are often smooth and visually ambiguous, lacking explicit pauses or posture resets. As a result, static frame representations may fail to capture the subtle temporal changes that indicate sentence boundaries. To address this challenge, we propose \textbf{SignShift}, a difference-aware segmentation framework that explicitly models frame-to-frame feature variation as semantic cues for sentence boundary detection. First, to model the feature variation, we design a Temporal Difference Module, which incorporates full-frame, facial, and hand cues, and employs inter-frame differencing to learn multi-scale temporal variations that capture both fine-grained local kinematics and global semantic transitions. Second, to mitigate over- and under-segmentation issues, we design a Segment Count Prediction module, which predicts the number of sentences to guide boundary selection. Extensive experiments on benchmark datasets demonstrate that SignShift substantially outperforms existing methods, validating its effectiveness.

---


### 155. [CRNDiff: Count-Native Diffusion Framework via Chemical Reaction Networks](https://arxiv.org/abs/2609.31149)

**<font color=#1a73e8>作者：</font>** Yuxuan Qiu, Praful Gagrani, Tetsuya J Kobayashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific measurements such as single-cell RNA (scRNA) sequencing often take the form of nonnegative integer counts, whereas continuous-state diffusion models approximate this discrete structure using continuous coordinates. Building on stochastic chemical reaction networks (CRNs), a class of count-native Markov jump processes, we introduce CRNDiff, a structured framework that combines count-space diffusion with inference-time conditioning on rare subpopulations. An independent birth--death instantiation yields a closed-form transition kernel for forward noising. This kernel enables reverse sampling via forward-filtering backward-sampling (FFBS) and supports data-driven selection of the terminal noising time, eliminating the need for a validation sweep. This tractability also lets us introduce tilted Feynman--Kac (FK) steering, a method for sampling target subpopulations from a frozen generator without retraining. By tilting posterior marginals before FK particle correction, steering mitigates importance-weight concentration when the target population is rare. Using scRNA-seq data from the human heart cell atlas, we test the ability of CRNDiff to generate cell-type-specific distributions. Across the three evaluated target populations, CRNDiff achieves the highest conditional fidelity among the evaluated generative models, with larger mean purity margins for rarer target populations. Generated cells preserve marker-level differential-expression structure. Replacing real training cells for the target classes with generated cells yields downstream classification performance approaching that of the real-data reference.

---


### 156. [FedHisto-PAST: Parameter-Efficient Stain-Aware Federated Learning for Cross-Site Lung Histopathology Classification](https://arxiv.org/abs/2609.31150)

**<font color=#1a73e8>作者：</font>** Muhammad Muhtasim Shahriar, M. M. Golam Hafiz, Saad Aloteibi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-site lung histopathology classification must account for stain variation, non-IID client data, missing classes, and the cost of adapting large pathology encoders. This study evaluates FedHisto-PAST v2 for three-way classification of adenocarcinoma (ACA), Normal, and squamous cell carcinoma (SCC). FedHisto-PAST v2 combines a frozen HIBOU-B foundation model with parameter-efficient adaptation, stain-conditioned paired-view prediction and feature consistency, reliability-aware prototype learning, and adaptive federated aggregation. Experiments used a five-client, non-IID, raw-data-local simulation with fixed internal evaluation, client-level analysis, component ablations, communication accounting, and a development-influenced exploratory LungHist700 cohort. All principal methods achieved near- ceiling internal performance, which limited discrimination on the fixed split. On LungHist700, FedHisto- PAST v2 achieved a Macro-F1 of 0.728560 and a balanced accuracy of 0.730454. Higher recognition of Normal and SCC was accompanied by lower ACA recall, and calibration remained imperfect. Prediction-level consistency was the only component with a clearly supported independent contribution in the external ablation analysis. Feature consistency and prototype regularization showed no conclusive independent overall gains in Macro-F1. The framework updated 1.253841% of the model parameters. The results provide exploratory cross-dataset evidence for stain-aware, parameter-efficient federation; they do not establish formal privacy, patient-level independence, prospective deployment, or clinical validation.

---


### 157. [HyperErase: Scale-Calibrated Hypernetwork for Multi-Concept Erasure in Text-to-Image Models](https://arxiv.org/abs/2609.31154)

**<font color=#1a73e8>作者：</font>** Yi Sun, Xinhao Zhong, Zhiqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-image (T2I) generation have substantially improved visual synthesis, but have also raised increasing safety concerns due to their potential to generate harmful or undesirable content. Existing concept erasure methods predominantly follow a static weight paradigm, producing a single frozen adapter that struggles to adapt to diverse prompt variations and suffers from parameter interference when scaling to multiple concepts. We propose \textbf{HyperErase}, a framework for concept erasure based on hypernetwork-driven prompt-conditioned parameter synthesis. Our approach first reframes concept erasure as prompt-conditioned parameter amortization and trains a hypernetwork to map textual descriptions to prompt-specific LoRA updates, eliminating the need for per-prompt gradient optimization or manual LoRA merging. To further improve the stability and precision of synthesized adapters, we develop a decoupled rectification strategy, which disentangles LoRA tokens into pattern and scale subspaces, applies a square-root transform to curb multiplicative over-scaling, and leverages teacher-derived canonical priors for inference-time correction. Extensive experiments across major concept categories demonstrate that HyperErase consistently improves the trade-off between erasure effectiveness, image quality, and semantic alignment, achieving performance comparable to gold-standard single-concept baselines. Furthermore, the resulting models can provide specialized LoRAs for each input prompt variation in a single forward pass without requiring gradient updates during inference. These principled and flexible framework offers a new paradigm for concept erasure in T2I models.

---


### 158. [Teacher-Anchored Selection of Post-Training Quantized Models under Domain Shift](https://arxiv.org/abs/2609.31155)

**<font color=#1a73e8>作者：</font>** Alejandro Rodriguez Dominguez, Muhammad Shahzad, Xia Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compressing a trained model yields a family of deployment candidates, and under domain shift the most compressed one need not be the one to deploy. We study selection over such a family, with candidates and teacher fixed and target labels absent or scarce. Two findings organize the label-free case. Minimum teacher distortion behaves almost as a constant rule, selecting the same eight-bit, per-channel, unclipped configuration in every run, which does not minimize empirical target cross-entropy. Established estimators divide sharply: in the overconfident-collapse regime of the CNN families, confidence-based estimators order the family close to backwards, and the diagnostics that identify it need the labels the setting denies, while output-distribution estimators match the teacher-relative anchor and on one architecture beat it. Distortion is nonetheless stable, so a supervised term can move selection away from it. Combining the two, we give exact quadratic identities for a canonical quadratic analogue of the family. We also show that under symmetric corruption the label-dependent part of a criterion linear in the label indicator is multiplied by one common factor whenever its coefficient sums are candidate-invariant, a class holding teacher contrasts and accuracy but not cross-entropy. These characterize the score's components without bounding selection regret. Across one hundred and thirty-four candidate families, one per independently trained convolutional or Vision Transformer teacher, anchoring reduces mean regret at the smallest label budget in every setting, an advantage that fades beyond twenty-five labels.

---


### 159. [Bayesian Tensor Autoencoder with Physics-informed Predictive Prior for Multi-dimensional Time Series Anomaly Detection](https://arxiv.org/abs/2609.31157)

**<font color=#1a73e8>作者：</font>** Jianan Liu, Chunguang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-dimensional time series, inherently tensorial, are common in practice. Despite great progress in time series anomaly detection, most existing methods are confined to uni-/multi-variate time series. When handling multi-dimensional time series using these methods, reshaping operations are required, which inevitably break the intrinsic correlations and thus lead to performance degradation. In uni-/multi-variate time series anomaly detection, AutoEncoders (AEs) are widely adopted and generally categorized into reconstruction-based and prediction-based AEs. The reconstruction-based AE utilizes the current observation for reconstruction, while the prediction-based AE utilizes the historical information to predict the current observation. Thus, the two AEs utilize different information. To bridge the gap between reconstruction-based and prediction-based AEs, so as to fully leverage the available information and thus further enhance performance, we propose a predictive prior and incorporate it into the reconstruction-based AE. It may not be very difficult to conceive this idea, but designing the predictive prior so that it can work for tensor anomaly detection is non-trivial. Specifically, to avoid breaking the intrinsic correlations within the multi-dimensional time series, we use the tensor AE as the backbone. To incorporate the predictive prior into the reconstruction-based AE, we propose a Bayesian fusion approach and our analysis reveals that this approach can enhance the modeling capability of the model for normal data. To mitigate the over-generalization problem of AE, we incorporate physical laws, i.e. tensor low-rank decomposition rules, into the neural networks in the predictive prior, leading to the Physics-informed Predictive Prior Tensor AE (PPPTAE) framework. Experimental results on real-world datasets demonstrate the effectiveness of the proposed method.

---


### 160. [Momentum-Guided Federated Split Distillation for Personalized Temporal Edge Intelligence](https://arxiv.org/abs/2609.31159)

**<font color=#1a73e8>作者：</font>** Ahmed-Rafik Baahmed, Jean-François Dollinger, Amine Brahmia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a momentum-guided federated split distillation framework for personalized, efficient, and autonomous temporal edge intelligence. We introduce TeRR-SAtt, our novel temporal reservoir student attention design that combines fixed reservoir representations, a lightweight temporal student, and personalized output modules. We also present AMGF, our anticipatory momentum-guided fusion mechanism that clusters clients through learning momentum and derives specialized teacher updates. On real-world smart-building data, TeRR-SAtt reduces edge training latency by 65.50%, inference latency by 44.70%, training memory usage by 18.40%, and inference CPU usage by 33.10% over the considered baselines. At the same time, AMGF improves local learning by up to 35.31% in RMSE compared to global updates.

---


### 161. [ReG-SAM: Reference Graph-Driven SAM for 2D Foundational Vessel Segmentation](https://arxiv.org/abs/2609.31160)

**<font color=#1a73e8>作者：</font>** Donghang Lyu, Zichen Zhang, Oleh Dzyubachyk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vessel segmentation in medical images is essential for many clinical tasks, ranging from diagnosis to treatment planning. However, it remains challenging due to complex vascular morphology and diverse imaging conditions. Existing deep learning methods rarely aim at building a generalizable vessel segmentor across anatomies and modalities. While the Seg- ment Anything Model (SAM) has shown promise for med- ical image segmentation, its original design does not fully exploit vascular morphology and struggles with fine-grained vascular structures, leading to suboptimal performance. In this paper, we propose ReG-SAM, a SAM-based framework tailored to 2D vessel segmentation that leverages reference graph set for enhancing vascular representations. Specifically, we introduce two modality-aware representations derived from the reference masks: graph prompt embeddings (GPEs) that encode global spatial features from graphs, and vascu- lar prototype embeddings (VPEs) that capture fine-grained modality-specific vessel characteristics from multi-scale fea- ture maps and vascular masks. Since both require vascular masks that are unavailable during inference and require robust modality-aware vascular feature representations, we construct a modality-wise vascular database and develop two reference graph-guided representation learning schemes for estimating GPEs and VPEs using samples from the database rather than ground-truth masks. Extensive experiments across 19 datasets demonstrate that ReG-SAM consistently outperforms existing baselines, even those using manual prompts, particularly on challenging thin vessels.

---


### 162. [I Act Therefore I Am: When Is JEPA's Action-Conditioning Enough to Learn Causal Mechanisms?](https://arxiv.org/abs/2609.31161)

**<font color=#1a73e8>作者：</font>** Yuhang Liu, Zhuo Huang, Javen Qinfeng Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent empirical and theoretical advances suggest that joint-embedding predictive architectures (JEPAs) may learn meaningful representations for action-conditioned prediction of future outcomes, thus becoming one of the foundational structures for world models. However, accurate prediction does not, in general, necessarily imply recovery of underlying causal states that give rise to the observed dynamics. This work investigates when and how JEPAs can recover the underlying causal states from observations. We first introduce a latent variable model, in which high-dimensional observations are generated from latent causal states whose dynamics are governed by action-conditioned transition mechanisms. Based on this formulation, we develop a general information-theoretic objective that combines conditional likelihood maximization for learning transition dynamics with entropy maximization for preserving latent state information. We then establish identifiability conditions under which representations learned by this general objective recover the underlying latent causal states up to component-wise invertible transformations and permutation. One key condition for such identifiability is sufficient action-induced variation in the transition mechanisms. Guided by this finding, we instantiate the general objective with an action-modulated Gaussian additive-noise model, yielding action-modulated JEPA (A-JEPA). Experiments on synthetic environments verify the theoretical findings under the identifiability conditions and robustness to moderate violations, while visual benchmarks demonstrate improved state recovery and transfer to unseen transition mechanisms.

---


### 163. [WorldTS: World Modeling for Multimodal Covariate-aware Time Series Forecasting](https://arxiv.org/abs/2609.31162)

**<font color=#1a73e8>作者：</font>** Yuhan Zhu, Xiangfei Qiu, Hanyin Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting is typically framed as learning a direct mapping from historical to future observations in the observation space. However, sequences of observations generally provide only a partial view of the dynamics of the underlying system, with future observations being shaped by latent dynamics. Recent latent-space forecasting methods thus achieve improved performance by predicting future observations from latent-space representations of historical observations rather than directly forecasting future observations in the observation space. Next, while future observations are also shaped by external factors, how to incorporate external, often multimodal, information into forecasting, so that it can shape latent-state formation and evolution directly, remains underexplored. We propose WorldTS, a world-modeling based forecasting framework that integrates multimodal covariates directly into the forecasting to further improve forecasting performance. Specifically, WorldTS employs a two-stage training strategy. First, it learns forecasting-relevant latent state dynamics conditioned on multimodal covariates, yielding encoded future states. Next, the learned state dynamics are frozen, and an observation decoder is trained to map the predicted future states back to future observations. Extensive experiments on 21 real-world datasets offer insight into WorldTS and its effectiveness.

---


### 164. [Audio emotion recognition for atypical hearing](https://arxiv.org/abs/2609.31168)

**<font color=#1a73e8>作者：</font>** Ulysse Roussel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> My doctoral work aims to explore Audio Emotion Recognition (AER) in the context of atypical listening. This research focuses on auditory hypersensitivity in people with autism, a phenomenon that is often difficult to evaluate and unique to each individual. Our core idea is to leverage our understanding of affect from acoustic traits, relying on the possibility of generalizing affective responses from a small amount of annotated data. As a first step, we fine-tune a large foundation model, Contrastive Language-Audio Pretraining (CLAP) using low-rank adaptation (LoRA), trained on a valence and arousal dataset of neurotypical listeners.

---


### 165. [TaskIR: Task-Driven Image Restoration via Degradation Adaptation and Task Feedback](https://arxiv.org/abs/2609.31170)

**<font color=#1a73e8>作者：</font>** Yanjie Tu, Qingsen Yan, Axi Niu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Task-driven image restoration aims to improve both image quality and downstream task performance. However, existing methods predominantly focus on single degradation type and struggle to handle the diverse degradations encountered in real-world scenarios. Different degradations impose distinct restoration demands, and insufficient restoration may leave residual degradations and artifacts that impair object boundaries and semantic cues, thereby compromising downstream task performance. To address these challenges, we propose TaskIR, a two-stage task-driven unified image restoration framework that integrates degradation-adaptive restoration with task feedback refinement. In Stage I, a Degradation Representation Module (DRM) extracts degradation representations, enabling a Degradation-Guided Transformer Block (DGTB) to dynamically modulate feature transformations for adaptive restoration. In Stage II, a Task-to-Restoration Feedback Generation module (TRFG) transforms heterogeneous task features into restoration feedback by modeling task-representation discrepancies associated with the current restoration. Subsequently, a Selective Task Feedback Refinement module (STFR) assesses feedback relevance and selectively refines intermediate restoration features to mitigate interference with well-restored content. Extensive experiments demonstrate that TaskIR achieves competitive restoration quality and downstream task performance across diverse degradations and tasks.

---


### 166. [Where a Model Sends Its Own Repeated Token](https://arxiv.org/abs/2609.31181)

**<font color=#1a73e8>作者：</font>** Nicolás Vera Zúñiga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Black-box model identification works by scoring a model's response to natural-language prompts. One line of work feeds models a degenerate input -- their own token, repeated -- to find a failure mode rather than an identity. We take that input and ask where the model goes when it does not. For each token t, read argmax p(. | t, t) in one forward pass; the result is a map on the whole vocabulary, with two halves. The first -- which tokens are fixed points -- is partially anticipated, and we report it as a failed estimand: the natural distance on it is 83% cardinality, separates a corpus manipulation by two bits in 3471 against a precision floor of zero, and attributes families at 0.5833. The second half, where the map sends tokens that are not fixed points, is unrecorded; the one paper holding those tokens logged them as a zero. Pairing on the source token removes the cardinality confound by construction (r from 0.9128 to -0.0932) and attributes families at 0.8333 -- twelve models scored against a pool of nineteen -- with chance 0.1389, across seven tokenizer groups and several corpora. Two nulls clear it: frequency-matched destinations agree at 0.1429, independent marginals at 0.0798. Family predicts agreement better than tokenizer (0.2031 against 0.1205), and recurrent architectures cluster at balanced accuracy 1.0 against a 0.7895 majority rate, or 0.90 once each model's dominant destination is excluded -- the figure we stand behind. We measure the robustness envelope: 8-bit weight rounding moves the map less than deduplicating the training corpus does (0.9004 against 0.6353, on one support), 4-bit destroys it (0.0098; 0.1812 at deployment granularity, so not a coarseness artefact), and the precision floor varies by model from 0.201 to 0.9778. All estimands and kill conditions were registered before the data, and the failed one is reported as fully as the surviving one.

---


### 167. [Evolutionary Safety of Recursive Self-Improving AI: Taxonomy, Risk Discovery, and Evaluation](https://arxiv.org/abs/2609.31186)

**<font color=#1a73e8>作者：</font>** Chang Gong, Jingping Bi, Di Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is advancing rapidly, with increasingly capable systems taking larger roles in reasoning, decision-making, scientific discovery, and autonomous development. As AI begins to participate in its own improvement, from model training and experience accumulation to agent evolution and automated AI development, the prospect of recursive self-improvement (RSI) is becoming increasingly relevant. This transition raises a fundamental safety question: how can safety be maintained when the system, its accumulated experience, and even the process producing its successors continue to change?
We introduce Evolutionary Safety as a perspective for studying safety under persistent and recursive self-improvement. It concerns not only whether an AI system is safe at a particular moment, but how safety properties change, persist, accumulate, and propagate throughout evolution. We characterize recurring manifestations, including intent drift, error accumulation, experience contamination, safety-property erosion, evaluator drift, and risk propagation. We then develop a taxonomy spanning persistent agent state, model state, evaluation and environmental feedback, computational substrate, and meta-level update mechanisms. Building on this taxonomy, we examine how evolutionary risks can be discovered and evaluated across states, updates, trajectories, and lineages, and derive governance principles for modification, selection, authorization, provenance, and recovery. Finally, we outline open problems toward maintaining safety guarantees as AI systems become increasingly persistent, adaptive, and recursively self-improving. Project resources and proposed evaluation systems are available at this https URL.

---


### 168. [ALF: An Active Learning Framework for Scientific Discovery](https://arxiv.org/abs/2609.31197)

**<font color=#1a73e8>作者：</font>** Shikha Surana, Alex Hawkins-Hooker, Olivia Gallup 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning for scientific discovery is almost systematically data bound. Producing relevant high quality data, under budget constraints, is amongst the most promising ways to advance the field. Active learning (AL) offers promise wherever labelling requires expensive experiment, measurement, or simulation. Most existing tools cover only part of the data acquisition loop, and typically focus on either offline benchmarking or online deployment, but not both. We present ALF, a modular AL Framework that runs the full data acquisition loop via five modular components. One clear API for both settings: offline, against an existing dataset for controlled and reproducible experimentation; and online, against an oracle for acquiring new candidates in real-world deployments. ALF is open-source and available at this https URL.

---


### 169. [Light Field Primitive for Novel View Synthesis](https://arxiv.org/abs/2609.31198)

**<font color=#1a73e8>作者：</font>** Liang Chen, Jiahui Ning, Xun Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Light Field Primitives (LFP), a formulation for novel view synthesis that replaces the dense ray database with a compact set of differentiable primitives in the classical two-plane parameterization. Each primitive condenses a group of rays into one learned record, and its response to a query is governed by how closely that query belongs to the group. Rendering a camera ray then reduces to compositing all responses it elicits, and a scene can be optimized directly from posed images and rendered in real time with rays. Beyond its competitive performance on standard benchmarks, the main advantage of LFP is structural: its primitives reside directly in the 4D ray space, so optical and appearance effects that are already operations on the light field become behaviors of a single shared renderer. With minimal changes to that renderer, LFP supports multi-scale anti-aliasing, defocus deblurring with refocusing, rendering for fisheye cameras, and even transparent object reconstruction with ray refraction, matching specialized frameworks that devote substantial machinery to these effects.

---


### 170. [Samples, Sources, Space: Decomposing Data Scale in Spatially Structured Representation Learning of Human Brain Microarchitecture](https://arxiv.org/abs/2609.31201)

**<font color=#1a73e8>作者：</font>** Christian Schiffer, Mathis Bode, Thomas Lippert 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling studies typically represent training data by a single count of samples. For hierarchically and spatially structured data, however, the same number of samples can be drawn from few or many sources and distributed differently across the underlying domain. We therefore study data scaling as an allocation problem, separating unique sample count, source diversity, and spatial coverage. We study this decomposition in microscopic whole-brain histology, where a source is an individual brain, and a sample is an image patch at a specific spatial location. Across 93 controlled pretraining runs of a contrastive model that uses spatial proximity for supervision, we vary data allocation, compute, and model capacity over 11.6 million spatially anchored image patches from 21 human brains. Performance improves with more unique samples, broader spatial coverage, additional compute, and larger model capacity. At fixed sample count, distributing samples across one to 18 subjects produces no detectable improvement, even though representations generalize substantially better to subjects encountered during pretraining. Inter-subject variation therefore strongly affects generalization, but additional subjects provide no benefit when a fixed sample budget is distributed across more sources. These results establish sample count, source diversity, and spatial coverage as distinct axes of data scaling in spatially structured representation learning.

---


### 171. [Preserve-and-Compose Training for Composed Image Retrieval](https://arxiv.org/abs/2609.31202)

**<font color=#1a73e8>作者：</font>** Sehyun Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed image retrieval (CIR) aims to retrieve images that satisfy a user-specified modification while preserving relevant visual content from a reference image. Collecting target images for this purpose is costly, motivating zero-shot CIR methods that instead use target captions as supervision. However, target captions may omit source details that should be preserved. We therefore propose, Preserve-and-Compose Training, which complements target-caption supervision with visual evidence from the source image. PACT learns from image--text--text (ITT) triplets without target images or gallery updates, aligning composed queries with target captions while preserving source evidence through visual supervision. We further introduce Chord scoring, which combines target similarity with source-relative directional agreement in the frozen image space. Results across four ZS-CIR benchmarks show that combining target-caption supervision with source-image evidence leads to strong retrieval performance across datasets, backbone scales, and external galleries. The code is available on this https URL.

---


### 172. [Budgeted Quotient-Residual Guidance for Frozen Pocket-Conditioned Molecular Diffusion](https://arxiv.org/abs/2609.31222)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Jinbo Bi, Minghu Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pocket-conditioned molecular diffusion updates ambient atom coordinates, but many lead-optimization objectives are expressed on quotient features such as distances, contacts, and anchored substructures. We introduce budgeted quotient-residual guidance (QRG), an inference-time correction that makes these quotient objectives active without retraining the molecular generator. QRG lifts quotient covectors to metric-horizontal ambient directions and delivers them through a trust budget set by the frozen sampler's own step norm: quotient geometry chooses the direction, while sampler motion bounds the scale. We derive the horizontal lift, closed-form sampler-budget update, KL/kinetic interpretation around a frozen reverse step, equivariance conditions, and a product-budget split for budget-capped section and residual controls. Controlled quotient tasks confirm that sampler-relative delivery activates signals that raw local quotient gradients leave dormant. On frozen TargetDiff backbones, official seed-0 CBGBench ligand-generation/editing sweeps show practical quality-runtime gains: Local-QRG improves validity from 0.815 to 0.864 on fragment growing, 0.664 to 0.707 on scaffold hopping, and 0.681 to 0.712 on linker design, while PredNext-QRG improves fragment/scaffold and remains near-neutral on linker. Novelty remains 1.000 and diversity is preserved in the matched multi-seed molecular slice, giving task-dependent improvements without sampler retraining or backbone modification. Overall, QRG provides a lightweight route to quotient-aware inference for frozen molecular samplers with explicit runtime accounting.

---


### 173. [Purin: A Biology-inspired Mechanism for Artificial Neural Networks](https://arxiv.org/abs/2609.31235)

**<font color=#1a73e8>作者：</font>** Zishu Liu, Chunbo Luo, Christos Grecos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial neural networks (ANNs) usually represent neural transmission with fixed trainable weights during a training batch, which omits short-term changes in synaptic efficacy. In addition, the discrete time-step simulation requires additional temporal processing that many conventional ANN architectures do not use. To overcome these challenges, we propose Purin, a biology-inspired and ANN-compatible mechanism, that introduces synaptic efficacy modulation into conventional convolutional neural networks. Purin uses a time-interval-based abstraction for neural activities, which allows Purin to introduce short- and long-term synaptic efficacy changes without using discrete time-steps. Purin introduces a bounded factor to represent temporary synaptic efficacy changes, together with two weight matrices that represent input-side and output-side efficacy. The weight matrices are updated by backpropagation and interpreted as the long-term synaptic efficacy changes. Experimental results show that after removing the confounding factors in the AlexNet, VGG11, and GoogLeNet architectures, Purin improves the classification accuracies in all three models across the evaluated datasets.

---


### 174. [Geometric Inconsistency Localization in Multi-View Image Sets](https://arxiv.org/abs/2609.31247)

**<font color=#1a73e8>作者：</font>** Xander Staelens, Albéric Loos, Bert Ramlot 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis (NVS) models can produce realistic new views of the same scene from different viewpoints. However, these generated views are not always geometrically consistent with one another. Multi-view (MV) consistency has shown promise as a tool for evaluating these NVS models. Its potential for multimedia forensics, however, remains largely unexplored, particularly for localizing geometric inconsistencies across wide-baseline image pairs. To enable research in this direction, we introduce DeformView, a wide-baseline MV dataset with pixel-level annotations of geometric inconsistencies. Using DeformView, we evaluate state-of-the-art MV consistency-scoring methods and show that approaches developed for NVS evaluation transfer poorly to the forensic task of geometric inconsistency localization. To address this limitation, we propose DEFECt3R, a lightweight learning-based classifier that uses cross-view feature relationships to localize geometric inconsistencies at the pixel level. By learning from explicit supervision, including hard negatives from geometrically consistent yet deformed views, DEFECt3R improves localization performance and substantially reduces false positives compared to existing consistency-scoring methods. Ablation experiments further show that both feature representations and correspondence quality contribute to localization performance. Overall, our findings demonstrate that MV geometric consistency is a promising yet underexplored signal for multimedia forensics and establish a benchmark and baseline for geometric inconsistency localization in wide-baseline MV image pairs. Code and dataset are available at this https URL

---


### 175. [Gauss What You Need: Compact Gaussian Splatting Across Scene Scales](https://arxiv.org/abs/2609.31248)

**<font color=#1a73e8>作者：</font>** Afif Boudaoud, Jiayi Liu, Alexandru Calotoiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting reconstructs a scene as a collection of Gaussian primitives from a set of posed photographs called the capture. The number of primitives used to represent the scene affects reconstruction quality, storage, and rendering cost. How to select this number automatically across capture scales remains unresolved: configurations effective on standard benchmarks can leave larger captures with too few Gaussians to reconstruct fine details. We observe that the surface to represent, given by the capture's extent and resolution, is known before training, whereas its content complexity becomes apparent during training, through the reconstruction quality on the training views. We introduce TangoGS, which combines capture-derived model sizing with training-based adaptation: the capture determines the scale of the model, and training feedback determines its final size within that scale. Before training, TangoGS derives a learning allowance for model growth from the capture's total pixels after discounting views that re-observe the same scene points. During training, reconstruction quality guides how many Gaussians to add and remove. On 13 standard benchmark scenes, TangoGS matches the mean PSNR of the best-performing evaluated baseline, LeGS, with $48\%$ fewer Gaussians. On eight large captures, the same configuration automatically scales to larger models when necessary, achieving the highest mean PSNR among evaluated methods: $0.54$ dB above the runner-up with $2.3\times$ as many Gaussians. Together, capture-derived learning allowances and training-quality guided density control enable a state-of-the-art quality--size compromise across scene scales without retuning.

---


### 176. [Deterministic Regime Switching and Feasibility Inversion in Dynamic Tensor Rematerialization](https://arxiv.org/abs/2609.31250)

**<font color=#1a73e8>作者：</font>** Mahesh Reddy Pagadala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We report fine-grained, deterministic instability in Dynamic Tensor Rematerialization (DTR), an online eviction policy for memory-constrained DNN training, measured on the reference DTR simulator (simrd) using public execution traces. On an LSTM trace, memory budgets differing by 0.10% of unconstrained peak memory select fast and slow execution regimes whose overheads differ by as much as 7.3x; the slow regime is driven by broadly repeated re-eviction of the same storages (evictions per storage rise from 1.33 to 8.27 while the set of distinct evicted storages is essentially unchanged: 5,233 vs 5,236, with the two sets overlapping at Jaccard 0.999). On a ResNet-32 trace, a fine budget sweep reveals a deterministic feasibility inversion: the run is feasible at ratio 0.101, infeasible (OOM) across 0.102-0.106, and feasible again from 0.107. We trace the immediate cause of the OOM to a fully pinned recursive rematerialization frontier that exceeds the budget after every evictable tensor has been evicted. Ablations using the DTR authors' own variants implicate the joint size-staleness scoring term in the observed LSTM instability. We argue these are at least two distinct budget-sensitive pathologies rather than one mechanism, and we separate what is demonstrated from what remains hypothesised. All results concern the reference simulator; reproduction in a production runtime is future work. Code, instrumentation, and raw results accompany this preprint.

---


### 177. [Peregrino: A Full-Hardware Accelerator for the Complete Falcon Post-Quantum Digital Signature Scheme on Resource-Constrained Edge Devices](https://arxiv.org/abs/2609.31252)

**<font color=#1a73e8>作者：</font>** Antonio Carreño, Jaime Señor, Jorge Portilla  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The arrival of quantum computers threatens the security guarantees of classical cryptography, since quantum algorithms can break schemes that remain secure against conventional attacks. The National Institute of Standards and Technology (NIST) has therefore standardized a set of post-quantum cryptographic algorithms, among them Falcon, a lattice-based digital signature scheme with the most compact signature and public-key sizes of the standardized candidates. Falcon's reliance on floating-point arithmetic makes it hard to implement in hardware, and prior work offers only partial accelerators for specific operations such as signature generation or verification, or a single full implementation generated through high-level synthesis (HLS). This work presents Peregrino, the first hardware accelerator of the complete Falcon digital signature scheme designed from scratch in HDL, targeting resource-constrained edge devices without a native floating-point unit through an emulated floating-point datapath. Implemented on a single Artix 7 XC7A200T FPGA, Peregrino uses 85261 LUTs, 41382 FFs, 44 BRAMs, and 142 DSPs for the Falcon-1024 variant. Against the only prior full implementation, the HLS-based FalconTakesOff, it uses 1,9$\times$ fewer LUTs, 3,4$\times$ fewer FFs, 2,7$\times$ fewer BRAMs, and 9,9$\times$ fewer DSPs, fitting the entire scheme on one FPGA where the HLS design requires at least two. Operating as a peripheral of an on-chip MicroBlaze soft-core, the accelerator additionally reduces key-pair generation, signature generation, and signature verification clock cycles by 92\%, 96\%, and 85\% over the emulated floating-point reference software.

---


### 178. [MoSAR: Mixture of Semantic Attention Regimes for Learning Adaptive and Approximable Attention Geometries](https://arxiv.org/abs/2609.31261)

**<font color=#1a73e8>作者：</font>** Michele Paolicelli, Alessandro Petruzzelli, Alessandro Franceso Maria Martina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The quadratic complexity of dense self-attention remains a central bottleneck for long-context language modeling. Many efficient alternatives address this cost by deciding in advance where attention should be sparse or local. We argue that attention approximation should instead be approached as a geometric problem, with the relevant interaction geometry learned from data: natural-language dependencies are input-dependent and difficult to prescribe in advance, so the model should learn where positional relevance can decay and where broader interactions must be preserved. We introduce Mixture of Semantic Attention Regimes (MoSAR), which learns such an adaptive, controlled-decay geometry over query--key interactions. Input-conditioned query and key routers, applied after positional encoding, select mixtures over short, medium, and global regimes, inducing a continuous distance-dependent attention field rather than a fixed sparsity pattern. This geometry is learned during training and can subsequently be discretized through top-1 routing. In controlled pre-training experiments with matched 500M-parameter models, MoSAR learns a substantially lower-reach attention geometry without degrading language-modeling quality, improving perplexity over dense RoPE at the training context length. Under length extrapolation, MoSAR achieves the best perplexity among all evaluated variants, including strong baselines such as ALiBi. Moreover, the learned geometry remains stable under deterministic top-1 discretization, suggesting that it is not only adaptive, but also amenable to low-cost approximation at inference time.

---


### 179. [Identifying Scientists on X](https://arxiv.org/abs/2609.31264)

**<font color=#1a73e8>作者：</font>** Philipp Meier, Katarina Boland, Laura Kallmeyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the growing importance of science-related discourse on the Web and the erosion of the classical knowledge order, it is important to identify different user groups, such as scientists, automatically. This work proposes an approach for identifying scientists and non- scientists on X/Twitter based on their user biographies and tweets. We show that we are able to classify accounts as scientists and non- scientists on two different datasets, reaching an F1 score of up to 0.88 using Random Forests with linguistic features and up to 0.96 using a contrastively fine-tuned DeBERTa model in an ensemble setup. Furthermore, we provide two datasets with X users labeled as scientists or non scientists and their respective tweets and user biographies.

---


### 180. [Cognitive Skills in the Age of AI: Computing Students and Experts Perceptions](https://arxiv.org/abs/2609.31272)

**<font color=#1a73e8>作者：</font>** Neha Rani, Vu Minh Anh Le, Austin M. Spangler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI is becoming increasingly integrated into daily workflows, especially in computing. We are gradually shifting towards an AI-rich future, an impending yet unknown one. One important emerging concern is whether we are accordingly preparing our future computing workforce. Further, we need to know what the important cognitive skills are to remain relevant in the computing workforce and if there are changes in cognitive skill importance. To investigate this direction, we conducted a mixed-methods study, collecting perceptions from computing students and computing experts regarding the importance of cognitive skills in the past, present, and future. We report that the perceived importance of most cognitive skills will decrease in the future, with an AI-rich environment, but critical thinking skills remain important. Further, we report reasons collected through interviews on why the importance of cognitive skills will change and how future computing students can prepare for it.

---


### 181. [MA-WAM: Multi-Agent World-Action Model for Test-Time Planning](https://arxiv.org/abs/2609.31281)

**<font color=#1a73e8>作者：</font>** Guowei Zou, Haitao Wang, Guoxin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent cooperative tasks require different agents to execute a joint action simultaneously, and each agent's action affects both the observations and responses of the other agents. Hence, a world model is needed to predict the team return resulting from the joint actions of all agents. A naive extension directly applies a single-agent world model to each agent's action when predicting the team return step by step. However, such an extension fails to capture the dependencies among the simultaneous actions of multiple agents. We propose Multi-Agent World-Action Model (MA-WAM), a test-time planning framework that enables a frozen multi-agent flow policy to evaluate futures of candidate joint actions. To our knowledge, MA-WAM is the first test-time world-model planner for multi-agent flow policies. MA-WAM predicts the consequences of each joint action according to cross-agent dependencies and enables efficient candidate scoring. Across 30 offline multi-agent reinforcement learning (MARL) settings on MAMuJoCo, SMAC, and MPE, MA-WAM achieves mean relative gains of 22.0% over direct execution and 25.6% over uniform action selection. Under the standard evaluation protocol on an A100 GPU, MA-WAM adds 12.1 ms, accounting for 2.5% of the measured generation-and-scoring time.

---


### 182. [MoTop: Motion-Topological Model For Micro AU Detection](https://arxiv.org/abs/2609.31285)

**<font color=#1a73e8>作者：</font>** Huai-Qian Khor, Mengting Wei, Yante Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial micro-expressions are spontaneous, brief, and subtle facial movements that reveal suppressed emotions in high-stakes environments. In contrast to classic expression analysis, detecting action unit (AU) yields a finer representation of facial movements, serving as a preliminary step before defining expression classes and other downstream tasks. Therefore, it represents a crucial upstream task in facial analysis, and improving an AU detection module increases the precision of facial analysis. Despite that, detecting AU is challenging because of the constrictive nature of the AU activation regions, leading to confusion among different AUs known as AU ambiguity. To model the fine-scale changes, we propose \textbf{MoTop}, a motion-topological model that is augmented with a learnable motion context, yielding regional soft guidance for facial activity, followed by facial landmarks that capture the fine-scale topological changes of micro AUs. To increase the micro facial landmark representations, we amplify the encoded facial landmark transitions via linear extrapolation, thereby increasing the spatial proximity of landmarks and enhancing the low-intensity landmark dynamics. In addition, we design anatomical facial clusters that enhance the hierarchical representation, facilitating multi-scale modelling of facial geometry and improving micro-topological representations. With these contributions, we have achieved state-of-the-art performance on the CD6ME protocol for the micro AU detection task.

---


### 183. [G2MAF: Test-Time Gradient Guidance for Multi-Agent Flow Policies](https://arxiv.org/abs/2609.31286)

**<font color=#1a73e8>作者：</font>** Guowei Zou, Haitao Wang, Guoxin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline multi-agent reinforcement learning (MARL) learns cooperative policies from fixed datasets without further environment interaction and a learned policy is frozen at deployment. Such a frozen policy typically proposes a single joint action and executes it directly at deployment time. However, this one-shot deployment often commits to a suboptimal proposal, even when better nearby alternatives remain consistent with the behavior data. To address this issue, we propose Gradient Guided Multi Agent Flow (G2MAF), a refinement framework for optimizing joint policies at test-time. G2MAF applies one globally normalized, projected critic gradient to guide and coordinate all agents' corrections while keeping the action both feasible and close to the frozen policy proposal. Across 24 MPE and SMAC settings, its canonical variant improves 20 frozen settings, with mean relative gains of 9.2% on MPE and 8.9% on SMAC, with model inference latency increased by about 6% only.

---


### 184. [Revisiting Certified Defense with Differential Privacy on Vision Transformers](https://arxiv.org/abs/2609.31310)

**<font color=#1a73e8>作者：</font>** Jun Yan, Weiquan Huang, Qixian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Certified defenses that incorporate differential privacy have proven effective on Convolutional Neural Networks (CNNs), furnishing rigorous robustness guarantees against norm-bounded adversaries. However, the certified robustness behavior of Pixel Differential Privacy (PixelDP) remains largely unexplored with the self-attention architecture now dominating the deep-learning landscape. Given that the Transformer has a profound impact on our daily applications from the digital world to the physical world, it is crucial to study certified robustness through differential-privacy-style stability. To fill this research gap, we revisit this construction in Vision Transformers and identify a failure mode that is largely hidden in the convolutional setting. When noise is injected after the patch embedding, the Laplace mechanism with the inherited grouped $\ell_1$ sensitivity bound collapses to chance-level accuracy across noise scales, whereas the Gaussian mechanism remains trainable. This contrast isolates the source of failure: not the injected noise itself, but the geometry of the sensitivity constraint. We show that the attenuation induced by the inherited $\Delta_{1,1}$ projection increases with layer width and kernel size according to a random-matrix scale $C/(\sqrt{M}+\sqrt{N})$. Replacing the $\ell_1$-type constraint with a spectral-norm constraint eliminates the collapse across datasets and architectures, but creates a fundamental obstacle: the repaired models no longer satisfy the sensitivity condition required by the standard Laplace certificate. We resolve this mismatch by deriving a dimension-free $(\varepsilon,\ \delta)$-privacy guarantee for the Laplace mechanism under $\ell_2$ sensitivity through concentration of the privacy loss.

---


### 185. [CytoSPM: Open-Vocabulary Cytopathology Detection with Structured Prompt Bank](https://arxiv.org/abs/2609.31314)

**<font color=#1a73e8>作者：</font>** Wenjie Li, Zishan Xu, Jinyang Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cytopathology detection requires open-vocabulary recognition because cellular categories are fine-grained, long-tailed, and continuously evolving across different organ systems. However, existing cytology detectors are mostly single-domain and closed-set, and there is still no unified benchmark for evaluating open-vocabulary cytopathology detection. We present PentaCyto, a multi-domain benchmark covering cervical, urinary, respiratory, serous fluid, and thyroid cytology, with 24 base categories and 9 held-out novel categories. Each category is associated with structured cytomorphology prompts that describe diagnostic morphological attributes and provide clinically grounded textual knowledge. We further propose CytoSPM, an efficient detector based on a decoupled two-stage design. It first extracts reusable class-agnostic visual representations, and then performs class-aware structural prompt matching with class names and cytomorphology prompts. On PentaCyto, CytoSPM outperforms existing methods in novel-category detection and open-vocabulary detection while maintaining efficient inference.

---


### 186. [LUCID: Learning Under Confounding for Inference and Discovery in Time Series](https://arxiv.org/abs/2609.31315)

**<font color=#1a73e8>作者：</font>** Mohammad Fesanghary  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unobserved common causes are pervasive in real-world time series and can induce spurious associations that causal discovery methods mistake for direct edges. We propose LUCID (Learning Under Confounding for Inference and Discovery, a regime-adaptive deconfounding layer that first estimates the confounding regime from data using a Marčenko--Pastur spectral router, then applies a deconfounding strategy matched to that regime. When the spectrum indicates pervasive factor confounding, LUCID attenuates factor-dominated variation and recovers contemporaneous (lag-$0$) structure from the resulting innovations, with edge selection calibrated against a data-driven edge-free null. Rather than being tied to a particular discovery algorithm, it can wrap existing discovery engines; we demonstrate consistent improvements across three such methods. On a diverse synthetic out-of-distribution benchmark spanning changes in confounder strength and sparsity, loading density, lag structure, volatility dynamics, edge heterogeneity, persistence, intermittency, and tail behavior, LUCID achieves the best family-weighted directed, lag-resolved graph $F_1$ ($0.60$), improving over the strongest baseline by $0.19$ absolute ($\approx\!46\%$ relative). Its advantage widens relative to looser lag-collapsed scoring, and remains robust under intermittent and heavy-tailed confounding. Code reproducing the method, the benchmark generators, and every reported experiment is available at this https URL.

---


### 187. [More Sensors Only One Field: Rethinking Continual Spatio-Temporal Forecasting](https://arxiv.org/abs/2609.31325)

**<font color=#1a73e8>作者：</font>** Lewei Xie, Haoyu Zhang, Jiajun Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual spatio-temporal forecasting supports traffic management and environmental monitoring under evolving dynamics and expanding sensor networks. However, conventional graph-based continual learning methods tie forecasting representations to the current sensor layout, so sensor expansion can alter the representation of learned spatial relationships. Our key insight is that sensor expansion changes the evidence available about a process without necessarily changing the dynamics to be learned. We propose STFO (Spatio-Temporal Field Operator), which parameterizes forecasting knowledge as a shared field-evolution operator and handles changing sensor layouts through observation and query interfaces. Normalized coordinate-based aggregation lifts irregular sensor histories onto a fixed latent grid, enabling reuse of learned spatial maps across observation sets without sensor-specific parameters. To accommodate process drift, a spectral descriptor summarizes variation across spatial scales and conditions Fourier propagation and attention to adapt operator responses to the current spatial regime. Coordinate-based decoding queries the evolved field at sensor locations and combines spatial corrections with local-history predictions. Experiments on PEMS-Stream, CA-Stream, and AIR-Stream demonstrate state-of-the-art average forecasting performance. STFO-Large reduces average MAE over DOL by 8.4% on PEMS-Stream and 4.7% on CA-Stream. Our code is available at this https URL.

---


### 188. [CG-HAF: An Interpretable Global-Local Lesion-Burden Fusion Framework for Ordinal Acne Severity Grading in Agentic Skincare Support](https://arxiv.org/abs/2609.31326)

**<font color=#1a73e8>作者：</font>** Muhammad Muhtasim Shahriar, Md. Naimur Asif Borno, Saad Aloteibi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ordinal acne severity grading requires distinguishing visually similar neighboring grades while jointly weighing holistic facial appearance and localized lesion burden - evidence that most existing approaches collapse into a single opaque representation. We introduce CG-HAF, a global-local fusion framework that instead keeps this evidence explicit: averaged holistic severity probabilities from independently trained classifiers are combined with structured lesion-burden descriptors from an object detector (lesion count, detection confidence, lesion area) into a compact representation, from which a lightweight, interpretable classifier produces the final grade. On a widely used benchmark, this fusion yields a clear, statistically supported improvement over global-evidence-only baselines, with the largest gains on the most severe cases. Testing on an independent dataset with a different grading standard shows that strong within-dataset performance does not transfer automatically, and a follow-up diagnostic attributes much of this gap to mismatched grading criteria rather than detection failure alone. These findings support interpretable global-local fusion as an effective strategy for ordinal acne grading while highlighting criterion alignment as key to cross-dataset portability, with a further illustration of how the resulting severity signal can support transparent, non-diagnostic decision-making in skincare applications.

---


### 189. [Bridging Body and Brain: Gene-Driven Morphology--Control Co-Design](https://arxiv.org/abs/2609.31329)

**<font color=#1a73e8>作者：</font>** Fu Feng, Ruixiao Shi, Yucheng Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Morphology--control co-design jointly optimizes an agent's body structure and control policy as an integrated embodied system. However, existing methods typically model morphology design and control with separate networks coupled only indirectly through a shared task objective, limiting explicit high-level coordination. Inspired by natural genes that coordinate biological development, we introduce \textbf{Morphogene}, a compact latent blueprint that bridges an agent's body and brain. Through AdaConcat, Morphogene jointly conditions morphology and control generation at the limb level, allowing its variations to induce coordinated changes in both components. Building on this representation, we propose \textbf{GeCode}, which formulates co-design as exploration in the compact Morphogene space. Each Morphogene anchors a local design region in which nearby body--brain designs are explored, while performance-guided updates move these anchors toward promising regions for more efficient exploration of the broader design space. This process combines local refinement with global exploration while preserving body--brain compatibility. Extensive experiments across diverse 2D and 3D co-design tasks demonstrate that GeCode consistently outperforms existing state-of-the-art methods, achieving substantially faster convergence and higher final performance.

---


### 190. [DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models](https://arxiv.org/abs/2609.31349)

**<font color=#1a73e8>作者：</font>** Haojun Xu, Jie Huang, Xin Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large video diffusion models offer expressive priors for embodied prediction and learning, yet their many-step sampling remains costly for interactive downstream use. Distribution Matching Distillation (DMD) enables few-step video generation, but can suppress robot--object motion while preserving visual quality. Examining DMD's teacher and fake-score signals, we find that weak re-noising keeps the teacher posterior concentrated near motion-deficient rollouts, limiting motion-restoring guidance. Meanwhile, stronger-motion rollouts tend to incur larger fake-score fitting errors, which can hinder the generator's learning of interaction dynamics. We propose DyMD, a DMD framework that adapts both teacher supervision and critic fitting to the evolving student. Temporal affinity--conditioned re-noise sampling adapts the timestep distribution to each rollout's current interaction fidelity by mixing the base schedule with a teacher prior motivated by local posterior variation, thereby balancing motion recovery and appearance refinement. To better track stronger-motion rollouts, dynamics-guided fake-score tracking uses a noise-conditioned predictor to estimate noise-relative fitting difficulty from latent temporal dynamics, then upweights predicted-hard rollouts in the critic loss. Using DyMD, we distill a 14B teacher into a four-step 1.3B student with no auxiliary modules at inference. On embodied-video benchmarks, the student improves R-Bench task adherence by $9.6$ percentage points and PAI-Bench-G Domain score by $5.1$ points over Base DMD while maintaining comparable visual quality. As a backbone for downstream action planning, our student achieves 34% mean success across two WorldArena tasks, compared with 16% for Base DMD.

---


### 191. [Progressive Memory Transformer: Memory-Aware Attention for Time-Series](https://arxiv.org/abs/2609.31351)

**<font color=#1a73e8>作者：</font>** Tord Sture Stangeland, Andreas Köhler, Steffen Mæland 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series carry structure simultaneously at multiple scales (fine-grained variation, mid-range motifs, and global properties) and downstream tasks operate at correspondingly different scales. Most existing self-supervised learning approaches supervise representations globally via instance-level contrastive losses and limited temporal neighborhood supervision, but do not explicitly exploit the structural hierarchy. We propose a learning framework that explicitly enforces a structural hierarchy across three scales independently: a local objective for token continuity, a mid-range objective for window-level motifs, and a global objective for sequence-level agreement. Realizing this framework requires the backbone to expose a representation at each scale; we introduce \textbf{Progressive Memory Transformer} (PMT), which augments a transformer with writable, window-aligned memory that exposes the mid-range scale alongside the token and sequence-level representations conventional transformers already provide. Across seven UCR/UEA/UCI classification benchmarks, a cue-retention probe, and forecasting benchmarks, PMT learns representations that probe well at the global, mid-range, and local scales---strong low-label classification (1--5\% labels), competitive forecasting performance across multiple horizons, and quantitative and qualitative evidence that memory states capture mid-range motifs.

---


### 192. [EEG-based Word Association Paradigm for Adult ADHD Screening: An Exploratory Pilot Study](https://arxiv.org/abs/2609.31359)

**<font color=#1a73e8>作者：</font>** Caroline Peng, Tony Russell-Rose  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the prevalence of Attention Deficit Hyperactivity Disorder (ADHD) over the past decades, healthcare systems across the globe face critical diagnostic challenges due to long diagnostic waiting times and a reliance on subjective behavioural assessments that cannot distinguish ADHD from comorbid psychiatric disorders, especially for adult patients. This exploratory study investigates whether EEG-based word association paradigms show promise as a complementary approach to screening for ADHD in adults. Using a mixed-method approach, the study examines neurological and cognitive differences between neurotypical individuals (NT), clinically diagnosed ADHD participants (ND), and self-reported ADHD cases awaiting formal diagnosis (SR) across three word association tasks. While established EEG biomarkers (ERP N400, Theta/Beta Ratio, and Alpha Suppression) show no significant group differences, semantic distance analysis reveals a statistically significant main effect ($p=0.003$), with the SR group showing the most divergent associations. These preliminary findings suggest that word association paradigms may capture cognitive differences not detected by standard EEG metrics and encourage further large-scale investigation as a potential complement to existing adult ADHD screening tools.

---


### 193. [Brenier Meets Adversarial Training: Optimal Transport Geometry for Robust Learning](https://arxiv.org/abs/2609.31363)

**<font color=#1a73e8>作者：</font>** Alireza Abdollahpoorrostam, Ehsan Sharifian, Buse Şen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributionally robust optimization (DRO) provides a principled framework for learning under distribution shift, but its practical use is hindered by the difficulty of evaluating worst-case risks for nonconvex loss functions. We study a penalized DRO formulation in which the adversary may choose any distribution but incurs a Wasserstein penalty for deviating from the empirical distribution. We show that the adversary's problem can be reformulated as an optimization problem over transport maps that push empirical samples to adversarial ones, and we prove that optimal maps are cyclically monotone. We also show that standard adversarial training---based on per-sample local optimization---violates cyclical monotonicity and wastes transport costs unless the adversary is severely restricted. We propose two remedies. First, we introduce multi-start particle ascent, which alternates parallel gradient ascent with reassignment to enforce cyclical monotonicity across samples. Second, we parameterize adversarial maps as gradients of input-convex neural networks, which guarantees cyclical monotonicity by construction. Experiments on robust regression, image classification, and robust control show that our methods consistently outperform standard adversarial training and state-of-the-art baselines, achieving improved robustness and better generalization under distribution shift.

---


### 194. [ContraFM-S2O: Flow Matching-Based One-step SAR-to-Optical Image Translation Model with Contrastive Learning](https://arxiv.org/abs/2609.31378)

**<font color=#1a73e8>作者：</font>** Mingqian Yu, Wei-kuan Chiang, Qiurui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, diffusion models and GAN-based models have become the mainstream approaches for SAR-to-optical image translation, owing to their advantages, such as high-quality generation and stable training. However, they have shortcomings such as high inference latency and the generated optical images suffer from low detail fidelity, often resulting in blurred edges and loss of fine textures. Thus, we propose ContraFM-S2O, which is a flow matching-based model for SAR-to-optical image translation. Unlike conventional diffusion models, ContraFM-S2O learns to predict the velocity field in training and solves ODE instead of SDE during inference to improve the sampling efficiency. In addition, ContraFM-S2O replaces instantaneous velocity with average velocity along the interpolation path to realize one-step SAR-to-optical image translation and uses contrastive learning to improve the quality of the generated optical images. Experiments show our model achieves state-of-the-art on SAR2Opt and QXS datasets, outperforming baselines, and reduces inference latency via one-step generation.

---


### 195. [Completed Pairs Hide Capped Failures: A ReVerPi Case Study of Selective Context Projection](https://arxiv.org/abs/2609.31381)

**<font color=#1a73e8>作者：</font>** Guangzhe Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Context projection replaces older tool observations with compact, addressable excerpts, reducing repeated input while potentially adding evidence-retrieval turns. We study this trade-off in ReVerPi, a Pi extension with archived observations and matched full/projected continuations. In an 86-run source-reading campaign with 641 model requests, the 15 completed pairs show identical success: 12/15 per arm. Twelve further boundary runs stop, with the runner suppressing the companion whenever the first arm fails to complete. Restoring all 27 boundary runs bounds projected-minus-full success between $-$9 and +1 tasks. One omitted, selector-chosen projected continuation successfully retrieves archive text yet exhausts twelve requests; its full counterpart answers in three. The eleven jointly correct pairs form a fully observed success stratum within this recorded frame: projection reduces aggregate logical tokens by 25%, while increasing the median pair's tokens by 29% and total suffix requests from 35 to 55. Separating fitting from evaluation changes the selector's apparent tie: outside its four fitting pairs, it incurs one extra failure and 8.6% more logical tokens over thirteen comparable runs. This methodological case study connects stopping rules, known bounded failures, unexecuted companions, and resource aggregation. Its findings concern the recorded campaign, rather than population noninferiority or superiority over unrestricted Pi. Evaluations should retain every intervention boundary, execute both allocated arms independently of the first arm's completion, and report completion alongside interaction and token expenditure.

---


### 196. [PANEL: An Open-Source, Self-Hosted Web Platform for Human Evaluation of Generative Models](https://arxiv.org/abs/2609.31392)

**<font color=#1a73e8>作者：</font>** Matteo Spanio, Andrea Poltronieri, Mart\'ın Rocamora  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human judgement is the reference measure for evaluating generative models, yet the software used to collect it lags behing the methodology. Researchers adapt listening-test frameworks designed for perceptual protocols such as MUSHRA, rely on closed commercial survey platforms, or implement single-use web applications. Live arenas such as Chatbot Arena and Music Arena rank publicly deployed systems at scale, but do not support controlled comparisons of a laboratory's own models with its own participants. We present PANEL, an open-source, self-hosted platform for such studies. A study is authored in the browser and distributed as a single link, with audio, video, image, and text stimuli, seven question types, and screening and skip logic. The platform reports per-question summaries, across-condition significance tests, pairwise win rates and Bradley--Terry scores, and supports power analysis from pilot data. Consent versioning, self-service withdrawal, retention enforcement, and audit logging support GDPR-compliant operation. Each study exports as a machine-readable specification. PANEL is available at this https URL.

---


### 197. [Short Paper: Prefix Count Limits Can Increase First-Hit Discovery in Card Reissuance](https://arxiv.org/abs/2609.31398)

**<font color=#1a73e8>作者：</font>** Wasif Faisal, Suprava Saha Dibya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a card number is compromised, an attacker may search for active numbers sharing its prefix. An issuer might respond by reissuing cards from heavily populated prefixes into less populated ones. We show that this intuitive count control can backfire. For fixed search regions, exposure weights, and total activity, we derive exactly when reducing the maximum prefix count increases the chance that a budgeted search finds an active number. In matched synthetic simulations over 50,000 candidates, targeted replacement meets the count limit in every run but raises supplied-12-digit-prefix discovery relative to equal-volume random replacement in three of twelve settings. Thus a lower prefix count does not by itself certify lower enumeration risk.

---


### 198. [Differential Attention Unlocks Complementary EEG and Speech Fusion for Emotion Recognition](https://arxiv.org/abs/2609.31399)

**<font color=#1a73e8>作者：</font>** Philip H. Lee, Shreeram Suresh Chandra, John H.L. Hansen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition (MER) increasingly pairs EEG with speech, treating internal neural signals and external vocal expression as informative views of affect. In practice, naive fusion underperforms the stronger single modality, because EEG artifacts inject noise that corrupts the shared representation. We introduce EmoSpeechBrain, a multimodal framework built on the insight that noise suppression is a precondition for effective fusion. Its EEG encoder uses differential attention, taking the difference between two attention maps to cancel shared noise and isolate discriminative neural activity. An attention-based gating adapter aligns both modalities in a shared space and weights each one's contribution to the prediction. On two datasets - PME4 and EAV, EmoSpeechBrain improves MER accuracy by up to 12.9% over other state-of-the-art (SOTA) EEG encoders, and surpasses unimodal speech and EEG baselines by up to 13.1% and 23.1%. These results show that once EEG noise is suppressed, fusion delivers gains that naive combination cannot.

---


### 199. [Decodable In-Context State and Model Output Across Training](https://arxiv.org/abs/2609.31401)

**<font color=#1a73e8>作者：</font>** Manas Venkata Sai Ravulapalli, Samrath Singh Chadha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior work established that a probe can decode an in-context binding on model errors and that probe-guided steering can repair some of them. We follow probe accuracy, model output, and steering response across public pretraining and post-training checkpoints. Probe accuracy rises during Pythia pretraining, while probe-guided steering moves from negligible all-trial benefit to a larger benefit at two model sizes. Saved scores distinguish probe-correct errors with low and above-uniform model probability for the correct candidate. Oracle-target steering already repairs many early errors, but saved aggregates cannot separate target quality from intervention sensitivity. A held-out comparison of decoders trained on the final state or candidate logits finds no detected final-state advantage on late-checkpoint model errors. An information-theoretic counterexample explains why decodability on errors alone cannot establish discarded output information. The connection to downstream omissions remains open.

---


### 200. [Context-Aware Functional Modeling for Android Third-Party Library Detection](https://arxiv.org/abs/2609.31409)

**<font color=#1a73e8>作者：</font>** Dihao Fan, Jian Zhang, Yasai Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party libraries (TPLs) are widely used in Android apps, but their reuse can introduce security risks and interfere with downstream program analyses. Existing Android TPL detection approaches face two key limitations: their hand-crafted features are fragile under aggressive code transformations, and their whole-library matching strategies are ineffective when apps retain only part of a TPL.
In this paper, we propose LibFan, a learning-based Android TPL detection approach based on context-aware functional modeling. It realizes this modeling through two complementary components: context-aware contrastive learning at the method level and functional partitioning at the library level. At the method level, it learns semantic representations through contrastive training while incorporating outgoing call relationships and class-level context, improving robustness to obfuscation, shrinking, and optimization. At the library level, it partitions each TPL into functionally coherent units and determines library presence using the best-matching partition, thereby accommodating partial library reuse. To evaluate LibFan, we construct a new benchmark comprising 200 apps and 46 vulnerable TPLs, with each app compiled under four transformation configurations. Under the most challenging R8 full mode, LibFan achieves F1 scores of 81.3% at the library level and 47.6% at the version level, representing relative improvements of 64.9% and 35.6% over the state of the art, respectively.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-225](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
