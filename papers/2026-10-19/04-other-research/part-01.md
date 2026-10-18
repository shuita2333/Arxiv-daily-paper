# 📦 其他研究 | 2026年10月19日

> 本类共 **278** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-278](./part-06.md)

---

### 1. [DeepUnfolding_Agent: A Classical_Quantum Adaptive Control API](https://arxiv.org/abs/2610.20615)

**<font color=#1a73e8>作者：</font>** Shanika Iroshi Nanayakkara, Shiva Raj Pokhrel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adaptive optimization workflows in machine learning, federated learning, quantum machine learning, and hybrid classical quantum systems often embed controller logic directly inside task specific training scripts. This coupling limits reuse, reproducibility, safety validation, and fair comparison across execution environments. This paper presents DeepUnfolding Agent, a schema-driven FastAPI platform that exposes deep unfolded adaptive control as an external software service. External executors register a strategy schema, submit round-level diagnostic variables, receive schema-bounded control actions, execute one optimization round, and return feedback for controller update. The framework separates controller intelligence from domain specific execution through a strategy registry, diagnostic to state adapter, controller factory, safety guard, executor abstraction, feedback update path, SQLite persistence layer, Docker deployment, and reproducible benchmark scripts. The implementation supports classical, quantum-aware, hybrid, Qiskit Aer, and optional IBM quantum processing execution pathways. We validate the software through unit, schema, API, safety, orchestration, Quantum execution, checkpointing, and Docker tests, and demonstrate external user fixed versus adaptive workflows across finance, healthcare, genomics, transport, noisy quantum simulation, and hardware backed IBM Quantum execution. The results show that DeepUnfolding-Agent provides a reusable and traceable adaptive control layer for heterogeneous optimization workflows. Our quantum experiments are interpreted as API level quantum control and hardware portability evidence.

---


### 2. [FlowBudget: Training-Free Sampling-Budget Estimation for Flow Matching Models](https://arxiv.org/abs/2610.20636)

**<font color=#1a73e8>作者：</font>** Zahra Dehghani, Pablo Piantanida, Mohammadhadi Shateri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from continuous flow-based generators such as flow matching models requires numerical ODE or SDE integration, making inference cost depend on the number of function evaluations (NFEs). In practice, the sampling budget is inherited from prior work or selected through expensive FID-versus-NFE sweeps, using FID to assess image-generation quality, requiring sample generation and evaluation at multiple budgets. This makes sampling-budget selection dependent on repeated empirical evaluation. We therefore ask a complementary question to solver design and timestep allocation: for a fixed pretrained model and solver, what numerical resolution is sufficient? We introduce FLOWBUDGET, a training-free estimator of solver-relative sampling complexity. Using simulation-free interpolation probes of the learned dynamics, FLOWBUDGET normalizes the leading one-step discretization error by the motion, estimates its coefficient from interpolation probes, and maps a numerical tolerance to a step budget using the solver order. We derive estimators for numerical solvers in flow~matching sampling, namely Euler and Heun for ODE sampling and additive-noise Euler--Maruyama for SDE sampling, and connect the ODE coefficients to terminal integration error. Experiments on SiT, FlowDCN and Rectified Flow models, spanning flow-model architectures and formulations, test whether FLOWBUDGET can estimate the NFE budget without generating samples at multiple budgets or performing an FID-versus-NFE sweep. The code is available at this https URL

---


### 3. [Expanding Attention: A Taylor-Series Route to Linear-Time Transformers with a Fixed Number of Recurrent States](https://arxiv.org/abs/2610.20637)

**<font color=#1a73e8>作者：</font>** Zicong Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We expand the exponential kernel of attention into a truncated Taylor series of $n$ terms and factorize each term into a tensor-power inner product, which collapses the causal history into exactly $n$ recurrent states, each updated by one rank-one outer product per token and independent of context length $N$. The recursion is lossless with respect to the truncated kernel ($2.2 \times 10^{-16}$ in float64), and the states are additive across chunks ($5.7 \times 10^{-14}$), so prefill admits a parallel scan. Measured exponents are $t \propto N^{2.28}$ for softmax against $N^{0.91}$ for states, with a crossover at $N \approx 728$ and $20.8\times$ at $N = 8192$; per-token decoding latency is constant at $7.3\,\mu$s against $N^{1.04}$ for softmax, giving $76.0\times$ at $N = 65536$. Accuracy improves exponentially in $n$ while cost grows combinatorially, since the $m$-th state is $\binom{d+m-1}{m}$ wide---a bound confirmed by SVD---so the optimum is second order, $n = 3$, at $6.5 \times 10^{-4}$ error and $9{,}945$ elements per head. Query and key normalization is a prerequisite: without it the argument exceeds the convergence radius and adding terms stops helping.

---


### 4. [KNOU-Flood: Advancing global streamflow forecasting with lead-aware probabilistic machine learning](https://arxiv.org/abs/2610.20640)

**<font color=#1a73e8>作者：</font>** Minjong Cheon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global streamflow forecasting supports flood preparedness, yet data-driven models trained on reanalysis lose skill when driven by operational forecasts, increasingly so with lead time. AIFL addresses this shift with a two-stage transfer-learning recipe and a deterministic LSTM, but it feeds one forecast lead time into the whole input window and gives no uncertainty. We ask how far this open recipe can be extended without changing its recurrent core. KNOU-Flood keeps a single-layer LSTM and the two-stage training and changes the information around it: a longer input window (424 days), lead-aware forecast inputs, GraphCast as a second forecast source next to ECMWF HRES, and a latent-noise ensemble trained with the fair CRPS. We compare against a re-implementation of the AIFL recipe (its code is not public) under identical data, stations, splits and metrics. Our contributions are threefold. First, over three seeds and 2,099 test basins (2021-2023), KNOU-Flood reaches a median KGE' of 0.65 at LT1 and 0.48 at LT10 against 0.62 and 0.34, with significant gains at all ten lead times under two scoring protocols, also against a 1024-unit baseline and on held-out basins (one seed each). Second, identical weights give an LT10 KGE' of 0.18 or 0.34 depending on how forecasts are fed, so much of the lead-time decay reported for AIFL is an input-protocol effect; the probabilistic head contributes most to the gain, followed by the raw GraphCast channels, the longer window and mixed fine-tuning. Third, the ensembles reach lower CRPS than probabilistic versions of the baseline, are nearly calibrated with inference-time dropout, and detect 1.5- and 2-year floods better than all baselines; the benefit for rarer floods depends on the seed, and an exploratory tail-weighted variant improves 10-year and larger events. KNOU-Flood is a controlled extension of an open recipe, not a new architecture.

---


### 5. [Forensic Analysis of the HackRF One with PortaPack Mayhem Firmware](https://arxiv.org/abs/2610.20647)

**<font color=#1a73e8>作者：</font>** Düzgün Küçük  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software-defined radios (SDRs) have become an inexpensive, portable platform for replay attacks, location spoofing and jamming. The HackRF One can operate stand-alone when fitted with a PortaPack interface board running the open-source Mayhem firmware. No peer-reviewed study has addressed the forensic analysis of this device family. This work establishes, at source-code level, where forensically relevant data reside on the microSD card of a device running Mayhem v2.0.1, in which format, when they are written and how they should be interpreted. The methodology is applied to an SD card image that the author acquired from their own device after four months of real use, and every inference is drawn from the image alone. The workflow covers timestamp rules that depend on the real-time clock (RTC) battery state, traces of on-device trimming and text editing, cluster-level recovery of deleted in-phase/quadrature (IQ) captures, and decoding of recorded signals cross-checked with an independent decoder. In the example image, the final part of a deleted IQ capture and a trimmed-away capture segment are recovered, and six captures are attributed to a single rolling-code on-off keying (OOK) transmitter sharing one 32-bit identifier. The study provides practitioners with an artifact catalogue, interpretation rules and acquisition recommendations.

---


### 6. [Towards automatic digital garment assembly](https://arxiv.org/abs/2610.20651)

**<font color=#1a73e8>作者：</font>** Alejandro Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating digital garments from existing two-dimensional patterns remains a time-consuming process. Although patterns are widely available in digital form, their assembly in garment CAD software involves manual definition of sewing operations and arrangement of the pattern panels for drape simulation. We present two learning-based approaches that automate both tasks using the 2D vector pattern as their sole input. Our automatic sewing model operates at the segment level, leveraging a Transformer encoder with multiple prediction heads. Our novel architecture supports many-to-many, ordered segment correspondences, as well as hems, overlapping seams needed for multilayer garments, and construction properties such as seam allowances and stitch types, required for the finished virtual garment but neglected by previous methods. A complementary panel-level model predicts body-region assignments, layers, and placement coordinates to initialize the drape simulation. We evaluate both models on a curated dataset of 4,035 professionally assembled garment instances. The sewing model exactly recovers all seam and hem topologies of 63.3\% of test garments, while the arrangement model meets the specified placement criteria for all panels in 66.2\% of test garments. We also integrate both methods into garment CAD software, demonstrating automatic assembly of successfully predicted garments.

---


### 7. [Does Personalization Break Trust? Open-Set Rejection Calibration Under Few-Shot On-Device Intent Adaptation](https://arxiv.org/abs/2610.20652)

**<font color=#1a73e8>作者：</font>** Vaibhav Prajapati, Pushp Garg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Always-on virtual assistants increasingly personalize on-device to new user-specific commands via few-shot fine-tuning (e.g., LoRA), but this adaptation is evaluated almost exclusively on whether it learns the new commands, not on whether the assistant can still recognize an input that matches none of its intents - the out-of-scope (OOS) rejection problem. We show that naive few-shot LoRA personalization degrades OOS-rejection AUROC (area under the ROC curve) on every one of five public intent-classification benchmarks (mean drop $0.055$--$0.258$, five seeds each), while in-scope accuracy is preserved. A scorer-invariant check shows part of this drop is an artifact of the standard confidence scorer's own miscalibration under adaptation, though a smaller, genuine effect remains under any scorer; we trace it to a measurable shrinkage of the embedding margin around known-intent regions (pooled Spearman rho=0.61$). A deployment-cheap fix is scoring rejection by Mahalanobis distance instead of softmax confidence without extra training/retraining recovers most of the lost quality on 3 of 5 datasets at no accuracy cost, beats two further OOD scoring baselines, and generalizes across shot count, LoRA rank, and a second base encoder. We report honestly where the fix falls short and release all code for reproducibility.

---


### 8. [Empirical Evaluation of Machine Learning for Cloud Cryptojacking Detection: Effects of Preprocessing and Evaluation Protocols](https://arxiv.org/abs/2610.20658)

**<font color=#1a73e8>作者：</font>** Amitabh Chakravorty, Nelly Elsayed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) has been widely applied to cloud cryptojacking detection. Classical machine learning models remain among the most widely used approaches for cloud cryptojacking detection. This paper presents an empirical evaluation of six widely used classical machine learning models for AI-based cloud cryptojacking detection under different preprocessing and evaluation settings. Because no public cloud-native cryptojacking dataset is currently available, experiments were conducted using two publicly available proxy datasets, DS2OS and NSL-KDD. The evaluated models include Random Forest, XGBoost, LightGBM, Gradient Boosting, Decision Tree, and K-Nearest Neighbors (KNN). Experimental results show that preprocessing choices and evaluation protocols have a measurable impact on model performance. On DS2OS, removing identifier-related features reduced the accuracy of most models to approximately 96%, while KNN achieved higher accuracy with lower attack recall. On NSL-KDD, models obtained 77 to 80\% accuracy on the official test set containing unseen attack types, compared with above 99.5% under a random train-test split. Attack-class precision, recall, and Matthews Correlation Coefficient (MCC) further provide complementary insights into classifier performance beyond overall accuracy. The results provide an empirical comparison of commonly used classical machine learning models under consistent experimental settings and offer insights into how preprocessing, dataset selection, and evaluation methodology influence reported performance.

---


### 9. [Hybrid DeepXAI Fusion Network for Interpretable Big Data Analytics and Secure Cloud Decision-Making Systems](https://arxiv.org/abs/2610.20661)

**<font color=#1a73e8>作者：</font>** B. Nancharaiah, Ramakrishna Kolikipogu, J. Sulthan Alikhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Big data analytics supports modern intelligent systems, but model complexity and limited transparency can undermine interpretability, trust, and security in decision-making. This paper presents the Hybrid DeepXAI Fusion Network, a deep learning framework that integrates temporal, relational, and contextual features with explainable artificial intelligence (XAI) mechanisms. The architecture combines one-dimensional convolutional neural networks (1D-CNNs) for temporal feature extraction, Transformer encoders for contextual modeling, and graph neural networks (GNNs) for inter-feature dependency analysis. An attention-based fusion mechanism integrates these representations. Class Activation Mapping (CAM) and an explanation loss are incorporated to improve interpretability and explanation consistency. The framework is designed for deployment in a federated cloud architecture, using homomorphic encryption and blockchain-based auditing to support data privacy and accountability. Experimental evaluations across healthcare, finance, and energy datasets report 98.42% accuracy, 97.9% precision, 98.1% recall, and a 98.0% F1-score, outperforming the evaluated CNN-LSTM, Transformer-only, and XGBoost baselines. Under projected gradient descent (PGD) adversarial perturbations, the model reportedly retains accuracy above 91.5%. Scalability experiments report throughput of 80,000 messages per second with latency below 200 milliseconds. These results suggest that the proposed framework has potential for interpretable and secure cloud-based decision-support systems.

---


### 10. [Value-Informed Schedule Trimming for Accelerated Sequential Monte Carlo Guidance in Discrete Diffusion](https://arxiv.org/abs/2610.20669)

**<font color=#1a73e8>作者：</font>** Jaehyeon Kim, Ziseok Lee, Siyoung Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward-guided discrete diffusion enables test-time alignment with downstream objectives, but applying Sequential Monte Carlo (SMC) guidance at every denoising step is computationally expensive. Active guidance steps require additional reward evaluations and, for gradient-based proposals, value-gradient computations. Sparse guidance reduces this cost by guiding only a subset of timesteps, but commonly used schedules are fixed heuristics whose effectiveness can vary substantially across tasks. We propose VISTA, a training-free method that automatically selects guided timesteps under a fixed budget. VISTA formulates sparse guidance as approximation of the ideal full-guidance probability path and derives an estimable upper bound on \(\ell_1\) path deviation. Using value statistics collected from a small number of full-guidance warmup generations, VISTA optimizes the resulting empirical surrogate exactly via dynamic programming. The warmup generations can be retained as model outputs, and after schedule selection VISTA has the same per-generation guidance complexity as other sparse schedules with the same budget. Across text, biological sequence, and image generation tasks, VISTA discovers task-dependent schedules and outperforms hand-designed sparse schedules in most tested settings, while approaching or exceeding full-guidance performance on several task metrics. In toxic-text generation, for example, VISTA attains a 0.99 unique-toxic ratio compared with 1.00 for full guidance while reducing post-selection per-generation latency from 204.23 s to 38.16 s, a 5.35$\times$ speedup.

---


### 11. [When Correctness Feedback Erases Evidence: Phase-Separated Completeness Auditing in Verus](https://arxiv.org/abs/2610.20676)

**<font color=#1a73e8>作者：</font>** Adarsh Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Correctness feedback suppresses the very evidence that specification-completeness auditing is designed to uncover: programs that satisfy a written contract but violate intended behavior. We demonstrate this objective reversal on 12 Verus/Rust tasks across four model families under matched call budgets. Independent no-feedback discovery more than doubles certified-witness yield relative to IntentShield's corrective-feedback loop (59.0% versus 27.1%). A format-matched iterative control places the larger share of this gap in feedback content, not independent restarts. The advantage holds in every model family and survives parser repair. A separate phase-separated execution matches the aggregate yield without reusing responses; most certified witnesses also fail held-out cases. Preserving these witnesses delivers stronger specification repair: Phase-Revised contracts achieve 81.3% implementation success, versus 62.5% for IS-Revised, with Direct-Revised close behind. Both no-feedback witness sources substantially outperform weakened contracts. The effect does not reproduce in the available Dafny and Lean evaluations, establishing an empirical boundary around the studied Verus/Rust workflow. Completeness auditing and correctness repair have opposing immediate objectives. Preserve and certify the admitted failure before repairing it.

---


### 12. [Spectral Indistinguishability and Learning-Curve Identifiability in Quadratic Networks](https://arxiv.org/abs/2610.20678)

**<font color=#1a73e8>作者：</font>** Dekun Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study what spectral summaries and scalar learning curves reveal about centered quadratic networks. We construct analytic positive input densities with exactly Gaussian one- and two-coordinate marginals. Their complete fourth-moment operators are intertwined by an orthogonal map fixing the entire diagonal teacher algebra, so the corresponding anchored spectral measures agree. For selected common teachers with a nonzero cycle invariant, their factorized loss curves differ because the map does not preserve matrix multiplication. Cycle length $r$, which can be arbitrarily large, gives $O(\varepsilon^r)$ contrast uniformly in training time for each fixed construction. For a supplied pair, noisy scalar loss queries require order $\varepsilon^{-2r}$ observations, while bounded initialization interventions with scalar gradient readouts require order $\varepsilon^{-2}$. A shared-input score, equal to a paired-gradient difference, attains the optimal input-sample exponent without knowing the teacher. An explicit family of diverging auxiliary teacher scales instead admits a nonzero finite limiting contrast at coupling $1/\log L$. Conversely, for Gaussian inputs and a rationally independent teacher spectrum, one exact scalar loss curve identifies the initial predictor up to sign conjugation. Within this rationally independent class, with nonzero diagonal inverse-state error in every coordinate and calibrated time and loss scales, it also identifies the unknown teacher spectrum and active dimension, modulo simultaneous rotations. For fixed dimension and distinct unordered teacher sums, dimension-minimal exact observations give generic joint local recovery. Finite exact global bounds hold for a known teacher and, on the active class, under a blind dimension cap. Exact certificates and full-weight replay verify the construction; numerical inverse checks reveal severe ill-conditioning.

---


### 13. [Learning Topology-Aware Representations for Mechanics-Relevant TPMS Metamaterials](https://arxiv.org/abs/2610.20684)

**<font color=#1a73e8>作者：</font>** Songlin Duan, Shuo Yang, Yujia Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning informative representations of mechanical Triply Periodic Minimal Surface (TPMS) metamaterials is important for mechanics analysis and structural design, yet existing methods have rarely explicitly supervised learned representations with information about global structural connectivity that is relevant to mechanical response. We propose a topology-aware representation learning framework that integrates persistent homology into a DMAE backbone to explicitly encode global structural connectivity. A persistence-guided masking strategy prioritizes patches associated with persistent topological features, while an auxiliary persistent-homology decoder encourages the latent representation to retain information about topological feature counts across connected components, tunnels, and voids. We evaluate the learned representations on two complementary TPMS datasets using family classification, mechanical-property classification, unsupervised clustering, and regression. Across the two datasets, our method demonstrates strong performance in both structural family and mechanical-property classification, improving family classification by up to 3.9% while achieving the best linear-probe performance. More notably, unsupervised property-clustering performance improves by up to 26.7% and 51.5% across the two datasets, while strong regression performance is retained with $R^2=0.993$. These results establish persistent topology as an effective inductive bias for representation learning of complex three-dimensional mechanical metamaterials.

---


### 14. [Quantile-Guided Diffusion for Probabilistic Time-Series Forecasting](https://arxiv.org/abs/2610.20739)

**<font color=#1a73e8>作者：</font>** Shadi Omari, Bashar Khoury, Assaf Schuster  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantile forecasts summarize uncertainty at each future time step, while diffusion forecasters represent it through sampled future trajectories. We study how predicted quantiles can serve as distributional controls for diffusion forecasting. Specifically, we investigate how the mechanism of quantile integration affects its effectiveness in guiding a pretrained diffusion forecaster. We find that residual control throughout the denoising network yields the most consistent improvements. We instantiate this approach as Control-TS, which learns a quantile-control pathway while keeping the pretrained backbone frozen. Across eight benchmarks, Control-TS consistently improves the backbone's CRPS, achieves competitive performance against state-of-the-art forecasting models, and retains its gains in capacity-matched comparisons. Further analyses examine how these gains depend on quantile granularity, predictor choice, and forecast quality. Finally, we introduce the Conditional Linear Predictive Score (CLPS), which complements distributional metrics by evaluating the downstream forecasting utility of generated futures. Together, these findings support predicted quantiles as an effective interface between explicit uncertainty estimates and diffusion-based trajectory generation.

---


### 15. [Vertical Sliced Wasserstein Distances for Meta-Measures](https://arxiv.org/abs/2610.20743)

**<font color=#1a73e8>作者：</font>** Elaheh Akbari, Ahmadreza Moradipari, Kyungtae Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many modern learning problems require comparing probability distributions whose individual observations are themselves probability measures, naturally giving rise to meta-measures in $\mathcal{P}(\mathcal{P}(\Omega))$. However, optimal transport distances on this space can be prohibitively expensive to evaluate. We introduce the vertical sliced Wasserstein ($\mathrm{VSW}$) distance, a scalable metric on $\mathcal{P}(\mathcal{P}(\Omega))$. Rather than slicing along the transport geometry of $\mathcal{P}(\Omega)$, $\mathrm{VSW}$ projects each inner measure using continuous test functions and compares the resulting one-dimensional distributions with one-dimensional Wasserstein distance. We prove that $\mathrm{VSW}$ is a valid metric on $\mathcal{P}(\mathcal{P}(\Omega))$, metrizes weak convergence, and admits dimension-independent statistical convergence guarantees. Empirically, $\mathrm{VSW}$ provides high accuracy and efficiency compared with existing distances for meta-measures. We further derive a practical particle gradient for the empirical $\mathrm{VSW}_2^2$ objective and demonstrate its use for gradient-based transport of meta-measures. $\mathrm{VSW}$ provides a simple and scalable alternative for comparing and optimizing distributions of distributions.

---


### 16. [Foundations of Hardware-Software Leakage Contracts](https://arxiv.org/abs/2610.20754)

**<font color=#1a73e8>作者：</font>** Jan Reineke  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Microarchitectural attacks such as Spectre and Meltdown undermine security by exploiting software-visible side effects of microarchitectural optimizations like caches and speculative execution. To use modern hardware securely, programmers must take into account the security implications of these optimizations. Yet instruction set architectures (ISAs)---the conventional abstraction layer between hardware and software---are ill-suited for secure programming: by design, they abstract from microarchitectural details and therefore fail to reflect their security consequences.
A new security abstraction is emerging to fill this void: hardware-software leakage contracts. To support the principled development of secure software on modern hardware such contracts characterize side-channel leakage at the ISA level. Thereby they enable programmers and compilers to generate code that is provably resistant to side-channel attacks---without having to explicitly reason about the microarchitecture. On the other hand, they provide a specification for hardware designers to ensure that microarchitectures do not introduce unintended and undocumented side channels. This paper introduces the foundations of this emerging topic, discussing recent contributions and unresolved challenges along the way.

---


### 17. [Purify Before You Align: Improving Representation Alignment for Diffusion Models](https://arxiv.org/abs/2610.20761)

**<font color=#1a73e8>作者：</font>** Yingheng Wang, Yaoqiang Li, Yaqin Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment improves and accelerates diffusion training by encouraging intermediate features to match a pretrained visual encoder. However, standard alignment matches pretrained representations without distinguishing what information may be more useful for generation. We introduce local appearance purification (LAP), which improves generation quality and makes encoders such as MAE more effective alignment targets by removing locally predictable content and aligning to the residual. LAP modifies only the alignment target, and requires no changes to diffusion training or inference. Through controlled interventions within a fixed encoder, we show that effective alignment depends on what information the target emphasizes, not simply how much image information it contains. Our theory gives a variational interpretation of standard alignment and, for fixed local predictors, a sum of token-wise information bounds conditioned on local appearance. To understand why purification benefits some encoders more than others, we derive an exact constant-readout test that measures how well the target can be matched without using the diffusion model's hidden state. LAP improves generation quality across five pretrained representations (MAE, AIMv2, CLIP, DINOv2, DINOv3), with the largest gain for MAE: on ImageNet-256 with SiT-B/2, it reduces FID from $53.1$ to $42.3$. Its gains persist with stronger alignment recipes and tokenizers. Computed before diffusion training, the constant-readout score predicts the benefit of purification (Spearman $\rho=0.94$ across 13 encoders).

---


### 18. [When Reality Outpaces Cognition: A New Scaling Principle for Reliable Intelligence](https://arxiv.org/abs/2610.20764)

**<font color=#1a73e8>作者：</font>** Ahsan Adeel, Talha Bin Riaz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper challenges the understanding capabilities of existing AI paradigms and emerging world models by asking a fundamental question: How quickly can reality change before an intelligent system can no longer reliably perceive, reason, and act? We formulate this as a theory- and model-agnostic challenge in which systems must infer reliable actions for increasingly distant future states across a growing observation--reality gap. We operationalize this challenge through the effective Speed of Coherent Cognition (\(S_C^{\mathrm{eff}}\)), defined as the highest tested Speed of Reality (\(S_R\)) through which a system continuously satisfies a predefined behavioural reliability criterion from baseline. As a proof of concept, reinforcement-learning agents are trained at the baseline \(S_R\) and evaluated, without retraining, as \(S_R\) is increased by up to \(50\times\) while computational resources remain fixed. We compare Transformer and gated-MLP baselines with \(Co^4\), an architecture inspired by cellular mechanisms implicated in conscious processing and awake thought. Across the tested scenarios, \(Co^4\) achieves substantially higher \(S_C^{\mathrm{eff}}\) than the baselines, motivating \(S_C^{\mathrm{eff}}\) as a new benchmark and the scaling of coherent cognition as a principle for reliable AI.

---


### 19. [Semantic Alignment of EEG and Text: A Contrastive Learning Framework for Decoding Imagined Speech](https://arxiv.org/abs/2610.20766)

**<font color=#1a73e8>作者：</font>** Shahryar G. Namdari, Francesco Iacomi, Riccardo Barbieri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imagined speech decoding from EEG offers a promising route toward naturalistic brain-computer interfaces. Traditional closed-set classifiers treat semantic categories as independent labels and do not explicitly exploit relationships among linguistic intents, limiting output flexibility. We adapt a multimodal contrastive learning framework to imagined speech, aligning EEG trials with language representations in the embedding space of a frozen pretrained text encoder. An EEG encoder is trained with a composite objective combining semantically reweighted EEG-sentence alignment and text-prototype-based class discrimination, encouraging semantic structure while preserving separability among 39 intent categories. We evaluate the approach on the Chisco imagined speech dataset across five subjects, reporting Top-k accuracy, macro-F1, and balanced pairwise matching accuracy (2v2). We also investigate maximum EEG-text cosine similarity (MaxCosine) as an intrinsic indicator of decoding reliability and probe semantic structure beyond category labels using five evaluation-time semantic axes and a qualitative Semantic Gallery Probe (SGP) with previously unseen candidate sentences. The contrastive framework achieved decoding performance comparable to a task-optimized closed-set classifier while mapping EEG into a frozen language embedding space. MaxCosine identified subsets of held-out trials with higher Top-1 and Top-5 accuracy across subjects. Evaluation-time semantic axes showed mean agreement above the 50% chance reference across all five dimensions, and the SGP qualitatively illustrated direct comparison with unseen candidate sentences. Together, these findings suggest that EEG-language alignment can retain comparable fixed-intent decoding while supporting similarity-based retrieval, intrinsic reliability ranking, and evaluation of broader semantic structure.

---


### 20. [Selection-Safe Conformal Early Exit: Distribution-Free Coverage under Adaptive Depth](https://arxiv.org/abs/2610.20773)

**<font color=#1a73e8>作者：</font>** Adria Binte Habib, Ibne Farabi Shihab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibrating a conformal prediction set at each early exit does not preserve coverage once a data-dependent exit is selected. We construct one terminal path score from prefix maxima, calibrate a single split-conformal quantile, and return nested prefix sets that all contain the valid terminal set. The guarantee is selection-safe without an alpha/L correction and holds simultaneously for every post-calibration label-free stopping policy that preserves terminal-set containment. We also bound the efficiency cost of the path maximum by the empirical tail of the early-over-terminal score excess. Across eight encoder task-backbone cells, pathwise selection attains macro coverage 0.901 versus 0.814 for naive layerwise selection, with average set size 1.41 and latency fraction 0.71. On CIFAR-100 with a 24-exit ViT-L/16 (n_cal=500), first-eligible stopping at budget b=4 attains coverage 0.902, set size 2.76, and latency fraction 0.57, and the same calibration supports deployment-time budget changes without refitting. In a joint exit-count/calibration-size sweep at n=100, pathwise set size moves only from 3.02 to 3.11 as exits increase from 4 to 24, while Bonferroni degenerates to the full label space for 12 or more exits. Paired comparison against MinSE valid selection at (n,L)=(100,24) gives a set-size difference of 0.80 [0.47, 1.13]. Full-vocabulary decoder experiments remain a negative boundary, with sets of 7,162-9,620 tokens. Pathwise calibration is most useful when candidate exits are many relative to calibration size, when budgets change after calibration, and when shallow heads return actionable sets.

---


### 21. [Verdict: Encode Once, Decide Many](https://arxiv.org/abs/2610.20778)

**<font color=#1a73e8>作者：</font>** Avdhesh Singh Chouhan, Jack Perry  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automating organizational work means answering many small typed questions about one piece of state (does this email need a reply, how urgent is it, who owns it) with probabilities good enough to act on without a human. The open typed-decision model we compare against, like a standard cross-encoder, answers each question with a separate pass over the input. We present Verdict-MQ, an open encoder that reads a case once and answers all of its questions: given identical retained state tokens after truncation (verified on every reported case), a structured attention mask makes the state encoding independent of the questions, keeps questions from influencing each other, and makes option order irrelevant by construction. On the typed-decisions benchmark, a 395M Verdict-MQ matches the soft gold labels significantly better than the released 421M Laya specialist on all five fresh seeds (KL 0.080 vs 0.117, Brier 0.045 vs 0.061), an advantage that survives per-system temperature scaling; its higher accuracy (0.801 vs 0.767) lies past the benchmark's own saturation point, so we read that margin as closer agreement with the benchmark's labelling teacher. On RACE, BoolQ and MultiRC, against a matched fine-tuned baseline it wins on MultiRC and loses on RACE and on BoolQ, where its training is unstable; we measure zero-shot references ourselves, including a closed general system (Jev) that beats every fine-tuned encoder. A controlled comparison measures what the shared state costs: giving each question its own question-aware copy of the state gains 0.9-3.5 points on RACE and MultiRC at 1.4-2.5x the per-case latency, and nothing measurable on typed decisions, with the invariance guarantees unchanged.

---


### 22. [ReasonUni: Reasoning-Augmented Reconstruction Advances Unified Multimodal Models](https://arxiv.org/abs/2610.20781)

**<font color=#1a73e8>作者：</font>** Feize Wu, Zhiyuan Yan, Yuhuan Hong 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-text (I2T) understanding and text-to-image (T2I) generation are dual tasks in unified multimodal models (UMMs). Reconstructive post-training couples these tasks, but existing reconstruction-based methods remain perception-centric and provide limited supervision for reasoning about structure, intent, and transformation. We propose ReasonUni, a reasoning-augmented reconstructive post-training framework that extends this coupling beyond perception. Given an original image and an editing instruction, the UMM first reasons about what and how to edit and describes the target state, then generates the corresponding target image conditioned on this understanding output. To jointly optimize both modules, we introduce TreeGRPO, a tree-structured reinforcement learning method that samples multiple reasoning paths and candidate images per path, then aggregates visual rewards to update both modules under a unified objective. Experiments across multiple benchmarks demonstrate consistent gains in both understanding and generation, showing that reasoning-augmented reconstruction yields genuine mutual gains for UMMs.

---


### 23. [EvolvingBrain: An Adaptive Skill System for Multi-modal Agents Self-Evolution in Open Worlds](https://arxiv.org/abs/2610.20786)

**<font color=#1a73e8>作者：</font>** Runxuan Liu, Jingqi Shi, Baoxin Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-modal agents have made significant progress in interacting with open worlds. However, their ability to self-evolve remains limited. Supervised fine-tuning enables imitation but not active experience organization, while outcome-based reinforcement learning promotes exploration yet underuses intermediate trajectory information. Therefore, we propose EvolvingBrain, which uses an adaptive skill system as the brain for agent self-evolution, consisting of two following components. Stratified Skill Self-Evolution: extracts Procedural Patterns and Problematic Patterns from model-specific trajectories, summarizes experience by generating skills, and evolves through multiple interactions with the open world, ultimately forming a Stratified Skill Architecture consisting of Domain, Plan, and Action/Trap Skills, which provides the agent with a multi-granularity knowledge repository and a novel evolution approach. State-Aware Adaptive Execution: summarizes long-horizon interactions into Structured Abstractive Memory and uses it to guide the State-Aware Skill Fusion Strategy, enabling the agent to utilize knowledge according to its current state. Experiments on VAB-Minecraft and DiscoveryWorld demonstrate that EvolvingBrain improves success rates on open-world tasks and exhibits generalization capabilities. Our code is provided in the supplementary materials and will be publicly released in the camera-ready version.

---


### 24. [Sliced Wasserstein Sketches with Error Certificates](https://arxiv.org/abs/2610.20788)

**<font color=#1a73e8>作者：</font>** Elaheh Akbari, James Liu, Keaton Hamm 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compact representations that support geometrically meaningful comparisons are valuable for learning from probability distributions. We study optimal, free-weight $M$-atom quantization of one-dimensional probability measures in quadratic Wasserstein distance and extend it to higher dimensions via slicing. Using $L$ shared projections yields a sketch with $O(LM)$ comparison time. Our main result is an exact decomposition of squared distance error into residual and partition-mismatch terms, yielding computable certificates for arbitrary centroid sketches. For optimal sketches, a finite $(2+\delta)$ moment for some $\delta>0$ guarantees $O(M^{-1})$ error in the finite-direction sliced distance, while equal-mass sketches can converge more slowly. Each slice preserves its mean, while storing residual energies enables covariance recovery from sufficiently many generic directions. Experiments on document, point-cloud, and flow-cytometry benchmarks show that optimal sketches substantially reduce storage while preserving the classification performance of uncompressed sliced distances. They also improve generalization from few labelled subjects and support end-to-end learning as compact pooling layers.

---


### 25. [Blame Errant Words, Not the Canvas: Defect-Aware Spatial Credit Assignment for Visual Text Generation](https://arxiv.org/abs/2610.20794)

**<font color=#1a73e8>作者：</font>** Sujie Hu, Huaisong Zhang, Pujing Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent reinforcement learning approaches have improved visual text generation, yet generated images still suffer from incorrect wording and malformed glyphs. We identify two coupled limitations: recognition-based rewards often overlook visible glyph defects, while whole-image scalar feedback obscures the uneven quality of individual text regions. These limitations motivate our central principle: $\textit{Blame errant words, not the canvas}$, to effectively preserve local quality distinctions. First, we introduce $\mathbf{TextDART}$, a defect-aware region-targeted reward model that localizes individual text regions and independently evaluates their semantic correctness and glyph quality, providing fine-grained, region-precise feedback. Building on TextDART, we propose $\mathbf{SCANNER}$, which turns these regional judgments into spatially differentiated policy feedback. It normalizes rewards for each text target across sampled images and casts the resulting regional advantages onto the corresponding latent tokens. Extensive experiments on existing benchmarks and our newly established $\textbf{PolyText-Bench}$ demonstrate that our approach achieves state-of-the-art performance in text accuracy and glyph fidelity. Project page: this https URL

---


### 26. [EEG-Based Prediction of Music Enjoyment Using Deep Learning with Explainable Temporal Analysis](https://arxiv.org/abs/2610.20795)

**<font color=#1a73e8>作者：</font>** Parshav Singla, Simranjit Kaur, Maanya Walia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding why listeners enjoy music is difficult because the experience is subjective and changes as a piece unfolds. Electroencephalography (EEG) offers a non-invasive way to study neural responses during listening, yet earlier work has mostly treated music emotion as a categorical label or relied on black-box models. We formulate enjoyment prediction as a regression problem on the public MUSIN-G dataset, which contains 128-channel EEG from 20 listeners together with song-level enjoyment ratings. Six deep learning models were compared under a participant-wise protocol, in which 15 listeners were used for training and validation and 5 were held out for testing. DeepConvNet, CNN-LSTM and GNN-CNN reached the lowest mean absolute error (0.97 to 0.99 on the 1 to 5 scale), while the temporal convolutional network (TCN) had the highest Pearson correlation with the ratings (r = 0.21). Gradient-based and occlusion-based explanations, averaged over all held-out windows, identify the time segments within each two-second window that most influence the TCN predictions. The study provides a reproducible cross-listener benchmark for EEG-based enjoyment regression and shows how explainability analysis complements standard metrics.

---


### 27. [Privacy-Preserving Text Inference for Health-Misinformation Classification and Semantic Retrieval](https://arxiv.org/abs/2610.20796)

**<font color=#1a73e8>作者：</font>** Jasleen Kaur, Chloé Cachet, Koray Karabina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Health-misinformation analysis presents a dual challenge: misleading claims can affect public well-being, while systems designed to detect them may expose sensitive user-submitted text. This motivates privacy-preserving inference for public-health applications in which user queries may contain confidential medical information and trained models and reference databases are maintained on organizational servers. We design a privacy-preserving text inference framework based on CKKS homomorphic encryption for health-misinformation classification and semantic retrieval. The classification pipeline fuses BioBERT embeddings, PCA-reduced MPNet embeddings, and SVD-reduced TF-IDF features, while the retrieval pipeline combines MPNet embeddings with ISCC-SCT semantic fingerprints through late fusion. We evaluate predictive performance and benchmark plaintext versus ciphertext-based execution. The hybrid classifier achieved an accuracy of 0.971 and a macro-F1 score of 0.950, with identical reported metrics under plaintext and ciphertext-based inference. The hybrid late-fusion similarity model achieved a Pearson correlation of 0.8691 with human sentence-pair similarity scores on STS-B. For ciphertext-based retrieval, we evaluated naive and optimized implementations. The optimized implementation uses CKKS single instruction, multiple data (SIMD) packing to compute and return multiple similarity scores together, reducing single-query latency over 7,128 indexed items from 222.028 to 5.168 seconds and communication overhead from 6.11 GB to 2.13 MB. These findings demonstrate the technical feasibility of privacy-preserving text inference for health-misinformation applications and characterize its predictive utility and efficiency trade-offs.

---


### 28. [Optimal Explicit and Implicit Regularization Strengths in High-Dimensional Continual Linear Regression](https://arxiv.org/abs/2610.20804)

**<font color=#1a73e8>作者：</font>** Gilad Karpel, Daniel Soudry  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study continual linear regression in a high-dimensional regime, where a learner observes a sequence of tasks and updates its parameters sequentially. In this setting, we derive an explicit closed-form expression for the generalization loss of a model trained with gradient descent for a fixed number of steps per task, which holds for arbitrary teachers. We prove that the optimal fixed step size decays nearly inversely with the number of tasks, specifically as $\ln T / T$, for a single teacher and, more generally, i.i.d. teachers. Under this scaling, we show that the resulting generalization loss is asymptotically equivalent to that achieved by optimally tuned L2 (isotropic) regularization. Furthermore, we extend our analysis to generalized ridge regression with diagonal regularization matrices, obtaining a closed-form characterization of the generalization loss and identifying necessary and sufficient conditions under which the optimal regularizer is isotropic. Finally, we identify a regime where the optimal step size remains finite even as the number of tasks tends to infinity, thus revealing a non-trivial tradeoff between task variability and implicit regularization, in contrast to the i.i.d. teacher scaling. Our theoretical predictions are corroborated by experiments on both linear models and neural networks, providing practical guidance for the design of continual learning systems.

---


### 29. [A Self-Improving Agent that Grows its Own DSL: Oracle-Free Operator Induction for Exact Question Answering](https://arxiv.org/abs/2610.20809)

**<font color=#1a73e8>作者：</font>** Yun-Shiuan Chuang, Yirou Ge, Yixi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A self-improving agent has to decide which new skills to keep, and in practice it keeps whatever earns a high reward, convinces a judge model, or compresses its library, even when the skill is wrong. That is fine until the answers have to be exactly right: over a table of transactions, a total is either right or wrong. We ask a harder question: can an agent grow what it can compute with no reward, no judge, and no answer key, and still be exactly right? A single frozen model runs two nested loops over a small, exact domain-specific language (DSL). The inner loop answers new questions only when two independently written expressions agree on every record. The outer loop discovers its own missing capability and authors an operator for it, admitted only when an independent second implementation agrees and the result obeys a conservation law, all without ground truth. The inner loop roughly triples the answerable-question set, and the outer loop self-extends on disjoint starting sets, inventing operators outside the starting closure; a no-induction control answers none of the new questions. The admission rule is empirically sound: it rejects 138 of 138 buggy operator variants under an independent reference, even one written by a different model family, where the admit-if-it-runs, self-consistency, and compression signals the field relies on admit most of them. Unmodified, the same mechanism self-extends on two further domains with unrelated schemas, business-ledger and clinical-encounter question answering, growing their answerable sets more than tenfold and nearly twentyfold. The loop transfers across model families too: run with further proposers, the gate stays sound and independent families self-extend comparably, with only the induction yield tracking each proposer's DSL fluency.

---


### 30. [RIGen: Beyond Action Following with Reciprocal Interaction in Generative Gameplay](https://arxiv.org/abs/2610.20811)

**<font color=#1a73e8>作者：</font>** Mengfei Li, Yi Zhang, Xingtong Ge 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative gameplay requires more than immediate responses to player this http URL should have persistent consequences, while the generated world should act according to its own state and rules, shaping the player's situation and subsequent choices. Video generation captures local dynamics, but limited history, partially observed game state, and the need for contextual behavior decisions make such interactions difficult to sustain through audiovisual prediction alone. We introduce \rig (Reciprocally Interactive Generation), a framework for reciprocal interaction in generative gameplay. \rig combines persistent state and configurable rules, contextual interaction reasoning, and action-conditioned audiovisual generation. Together, these components make interaction consequences and actor behavior jointly determine generated content while maintaining consistency between game state and visible outcomes. We construct a Xonotic gameplay dataset to train an audiovisual generator for learning dynamics and interactions. Further post-training enables \rigarena, an interactive generative first-person shooter (FPS) prototype. Experiments demonstrate more reliable combat outcomes and reciprocal interaction between the player and the generated world. Project page: this https URL.

---


### 31. [O-RAN-Native Jamming Detection Under Network Heterogeneity](https://arxiv.org/abs/2610.20816)

**<font color=#1a73e8>作者：</font>** Sneihil Gopal, Fernando J. Cintrón, Richard A. Rouil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radio-frequency jamming threatens cellular network operations in contested environments. The Open Radio Access Network (O-RAN) architecture exposes per-User Equipment (UE) telemetry through the E2 interface, enabling Key Performance Indicator (KPI)-based jamming detection without proprietary hardware. However, operational deployment demands detection methods that generalize across heterogeneous networks. We propose a Statistical Ensemble Method (SEM) combining adaptive Median Absolute Deviation (MAD)-based baseline detection, count-based anomaly detection, and abrupt change detection through a weighted voting system. SEM operates in two modes: a cold-start mode requiring no labeled data for immediate deployment, and a supervised mode where parameters are refined offline via grid search as labeled data accumulates. We evaluate SEM against five machine learning (ML) classifiers and five deep learning (DL) sequence models using approximately 25 hours of testbed data comprising logs from eight heterogeneous 5G environments, employing both single-environment and multi-environment leave-one-out (LOO) validation. Our analysis indicates that under conditions not encountered during training (distribution shift), learning-based models tend to lose recall and miss jamming events, whereas SEM, even in cold-start mode, maintains detection capabilities at the cost of false alarms. Furthermore, SEM's parameter optimization can be mapped to O-RAN's Non-RT RIC as an rApp for continuous refinement, allowing operators to transition to learning-based alternatives once corpus coverage is sufficient.

---


### 32. [Temporal Specification Guidance for Text-to-Video Generation](https://arxiv.org/abs/2610.20822)

**<font color=#1a73e8>作者：</font>** Avishree Khare, Hideki Okamoto, Bardh Hoxha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-video models often generate the visual concepts requested in natural language prompts but fail to satisfy their intended ordering, timing, and persistence requirements. We propose representing these requirements as specifications in a formal Temporal Logic, and introduce Temporal Specification Guidance (TSG), a training-free inference-time framework that turns temporal specifications into executable objectives for guiding video generation during sampling. TSG scores traces of visual concept evidence using differentiable quantitative semantics and uses the score's gradients to construct a specification-guided denoising direction. We instantiate this framework with video-text attention traces, efficient differentiable scores for Metric Temporal Logic, and gradient-derived attention biases. This instantiation requires neither an external concept classifier nor backpropagation through the video transformer. Its attention-steered forward pass yields a denoising direction that augments classifier-free guidance (CFG). On a benchmark of 220 prompts spanning 11 categories of temporal constraints, including ordered object entry and state transitions, this instantiation improves specification satisfaction accuracy over CFG by 9.5-20 percentage points across five models, with minimal memory overhead. These results demonstrate the potential of temporal specifications and differentiable satisfaction objectives as a flexible interface for controlling video generation.

---


### 33. [Performance Characterization of Pulsar's Software-defined Watermark Verifier](https://arxiv.org/abs/2610.20827)

**<font color=#1a73e8>作者：</font>** Jason Anderson, Kaz Gunning  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pulsar provides the world's most secure PNT service by incorporating a Combinatorial Watermark into its ranging service. Under conservative signal conditions, Pulsar's Combinatorial Watermark, where 21 ranging code chips are inverted among the 1023, provides 32-bit authentication security each second. In this work, we present our software-defined radio (SDR) implementation of the Pulsar watermark processor. We discuss various threat models, multiple receiver architectures, implications to the receiver, and results from using Pulsar's SDR processing watermarked signals daily from the Pulsar-0 mission. Our results demonstrate the feasible implementation of Pulsar's watermark verification process in commercial GNSS receivers. This is an important milestone in making Xona's Pulsar service available to customers later this year after deployment of our first four production satellites.

---


### 34. [GhostLock: Learning-Assisted Blind GPS Signal Nullification Without Victim-Side Information](https://arxiv.org/abs/2610.20831)

**<font color=#1a73e8>作者：</font>** Khalil Ahmad, Omar Ansari, Mohsin Kamal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Global Positioning System (GPS) provides critical positioning, navigation, and timing (PNT) services for numerous safety- and mission-critical applications, making it an attractive target for physical-layer attacks. While GPS spoofing and jamming have been extensively studied, GPS Signal Nullification (GSN)-a physical-layer attack that suppresses authentic satellite signals through destructive interference prior to acquisition-remains largely unexplored. Existing wireless signal nullification techniques target conventional communication systems and typically require victim-side information, such as channel estimates or synchronization parameters, making them impractical for GPS. Furthermore, many GPS spoofing defenses assume authentic satellite signals remain available as trusted references, an assumption invalidated by GSN. To address this gap, we present GhostLock, a learning-assisted blind GSN framework requiring only an approximate target location estimate. GhostLock integrates a Blind Adaptive Filter (BAF) with a deep learning-based synchronization module to generate and align an anti-signal using only the attacker's locally received GPS signal, eliminating the need for victim-side observations. We implement GhostLock on a real-time software-defined radio (SDR) platform using GPS-SDR-SIM and GNU Radio. Experimental results demonstrate successful suppression of GPS signal acquisition, establishing the feasibility of blind GSN and motivating new detection and mitigation techniques for this emerging GPS threat model.

---


### 35. [MARS - A foundational map auto-regressor](https://arxiv.org/abs/2610.20843)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Suvam Bag, Rupanjali Kukal 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Map generation tasks feature extensive non-structural vectorized data (e.g., points, polylines, and polygons) and thus pose significant challenges to common pixel-wise generative models. Conventional approaches use multiple stages, first segmenting these features at the pixel level and then performing vectorized post-processing, with errors and complexity compounding at each stage. Motivated by the recent success of auto-regressive language modeling, we propose the first map foundation model, named Map Auto-Regressor (MARS), that is capable of generating both multi-polyline road networks and polygon buildings in a unified manner. For training MARS, we collected to our knowledge the largest multi-class map extraction dataset totaling 3.4M examples, which we call MAP-3M. Across four road and building datasets, MARS outperforms or matches the performance of multistage baselines. Additionally, we develop a "Chat with MARS" capability that enables interactive human-in-the-loop map generation and correction, supported by the auto-regressive nature of our end-to-end approach. We release our MAP-3M dataset and project demo page at (1) this https URL and (2) this https URL, respectively.

---


### 36. [Evolving Together, Failing Apart: The Skill-Policy Co-evolution Trap in Self-Improving Agents](https://arxiv.org/abs/2610.20845)

**<font color=#1a73e8>作者：</font>** Yujie Feng, Xiaobin Wang, Jinluan Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill-policy co-evolution, in which an agent's policy model and its skill bank improve each other during training, is a promising paradigm for self-improving agents. Current evaluations score the co-evolved policy on the final bank it trained with (the delivered bank). After deployment, however, skills may be rewritten, added or removed more frequently than the policy model is retrained, leaving the policy to operate on a drifted skill bank that neither the training objective nor existing evaluation protocols address. In this paper, we first establish, through theoretical and empirical analysis, that the fragility hidden by this blind spot is not incidental. The acceptance rule these methods share (cooperative acceptance) ties a policy's competence to the bank it co-evolved with, leaving it fragile once skills drift, regardless of the implementation; empirically, sensitivity to skill drift grows as co-evolution training proceeds. We therefore introduce the CO-evolution Drift Audit (CODA), a deployment-oriented evaluation protocol that simulates skill drift and, alongside success rate under worst-case drift, introduces two new metrics: a consistency rate under meaning-preserving edits and a resistance rate to corrupted skills. Across four co-evolution methods and five benchmarks (six settings), worst-case success is 5-13 points below the peak measured for each delivered pair, erasing 52-93% of the delivered bank's gain over the no-skill baseline. CODA thus reframes the target of co-evolution, from peak performance on the co-evolved bank to the ability to harness skills however they evolve, and provides a shared standard against which future methods can be audited.

---


### 37. [Denoising Score Matching in Diffusion Models: The Effect of Rank Constraints on Generalization](https://arxiv.org/abs/2610.20850)

**<font color=#1a73e8>作者：</font>** Anand Jerry George, Nicolas Macris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Architectural biases restrict the class of functions that a diffusion score network can represent, but their effect on generalization remains poorly understood. We study denoising score matching with score networks having a rank constrained non-linear term and a linear skip connection. Numerical experiments with trainable three-layer networks on data supported on an embedded sphere show that increasing rank lowers training error, but its effect on test error depends on sample size and data dimension. To explain this behavior, we analyze a random-feature score model under rank constraint with Gaussian data supported on a low-dimensional subspace. We characterize the optimal rank-constrained estimator through a truncated singular value decomposition and derive asymptotically precise limiting training and test errors when sample size $(n)$, feature width $(p)$, data dimension $(D)$, and rank $(r)$ scale proportionally with the ambient dimension $(d)$. The resulting spectral characterization distinguishes eigenmodes that improve the empirical fit from those that improve population accuracy. It also identifies the dimension of the orthogonal complement of the data subspace as a natural rank threshold. The theoretical learning curves qualitatively reproduce the observed rank-dependent overfitting, providing a tractable account of how bottlenecks or rank constraints can regularize score estimation and why their effectiveness depends on data dimension and sample size.

---


### 38. [Does Morphological Correctness Matter for Tokenization? A Scrambled Control Study in Tagalog](https://arxiv.org/abs/2610.20859)

**<font color=#1a73e8>作者：</font>** Abdul Rehman Antall, Baidya Nath Saha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typology-aware tokenizers are motivated by the claim that segmentation which respects morpheme boundaries preserves information that frequency-driven segmentation destroys. Studies routinely establish that it helps while assuming the boundaries must be linguistically correct. We separate them. Tagalog marks voice with infixes (s-um-ulat 'wrote', s-in-ulat 'was written'), so the root is not contiguous and no sequence of BPE merges can recover it. We build MorphAustro-Tok, a tokenizer that emits the root as a contiguous unit followed by a positional infix token, and compare it against a corpus-matched BPE baseline and, at two of three fertility levels, against a scrambled-morpheme control that preserves morph count, invertibility and per-type consistency while randomising the pseudo-infix. Across 33 runs, MorphAustro-Tok improves Tagalog machine translation over matched BPE by 0.84, 1.49 and 3.40 mean sentence-level chrF++ points. Token count does not explain the gain, since it grows as segmentation coarsens, and neither does capacity: at the coarsest level the scrambled arm carries more parameters and scores lower. Scrambling the analysis moves the gain by less than between-seed dispersion at both controlled levels, so we detect no contribution from morphological correctness at this scale.

---


### 39. [Long-Context Drafting Does Not Require Long-Context Drafters](https://arxiv.org/abs/2610.20865)

**<font color=#1a73e8>作者：</font>** Aref Jafari, Vansh Bhatia, Matt Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding pairs a cheap drafter with parallel verification against the target. At ultra-long context it stops paying, because a drafter that attends over the full prefix inherits the target's context-dependent cost, so the speedup it was meant to provide first erodes and then reverses. The standard response is to build a long-context drafter, by training or fine-tuning one, or by using a multi-token-prediction head shipped inside the target checkpoint. We argue this is unnecessary, because the drafters in use are target-conditioned, reading hidden states the target computed over the entire prefix, so distant context already reaches them without their own attention, and verification corrects what they miss. We therefore freeze released short-context drafters and run them far past their training length under two inference-time mechanisms, one bounding the attention cache they see, which fixes their cost, and one re-basing their rotary position indices into the trained range. No weight is touched and the only tunable saturates early, so one vLLM-side configuration spans 4k to two million tokens, costing at most 0.16x of speedup at short length. We prove when a common index shift leaves the drafter's computation exactly unchanged, and decompose acceptance into two measurable gaps with sharp bounds. Whatever speedup a frozen drafter delivers at short context, it retains out to two million tokens, across three target-drafter pairs and five corpora. The claim concerns the flatness rather than the multiple, and removing either mechanism eliminates it. The gain is conditional on the speculative cost per emitted token staying below the matched target-only cost.

---


### 40. [SHRED: Self-Play for Heterogeneous Road-Users without Expert Demonstrations](https://arxiv.org/abs/2610.20866)

**<font color=#1a73e8>作者：</font>** Wei-Jer Chang, Zhouchonghao Wu, Akshay Rangesh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Realistic traffic simulation and autonomous planning both depend on modeling interactions among heterogeneous road users whose dynamics, constraints, and behaviors differ fundamentally. Existing approaches predominantly learn realistic interaction behavior from large-scale human driving demonstrations. In this work, we ask whether such behavior can instead emerge purely through self-play. We present SHRED, a framework that jointly trains vehicles, pedestrians, and cyclists through large-scale heterogeneous self-play from random initialization, without demonstrations or logged-trajectory replay. SHRED combines type-specific dynamics and objectives with procedural scenario generation and per-agent randomization, allowing diverse behaviors to emerge through closed-loop interaction. On the Waymo Open Sim Agents Challenge (WOSAC), SHRED jointly controls all three road-user types and outperforms both the closest demonstration-free self-play baseline and prior self-play methods that use demonstration-trained reference policies. Policies trained only on nuPlan map geometry retain comparable realism under zero-shot evaluation on Waymo. For planning, SHRED outperforms all compared planners on the interaction-heavy InterPlan benchmark. Controlled ablations show that heterogeneity in self-play improves both traffic realism and planning performance, with particularly large planning gains in interaction-heavy scenarios. Together, these results establish heterogeneous procedural self-play as a scalable, demonstration-free paradigm for learning realistic and interactive traffic behavior.

---


### 41. [Anticipatory Commonsense with Moving Objects: An ASP-Based Framework for Predictive Reasoning with Interacting Trajectories](https://arxiv.org/abs/2610.20867)

**<font color=#1a73e8>作者：</font>** Julius Monsen, Jakob Suchan, Mehul Bhatt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a general declarative framework for anticipatory reasoning about interactive motion in complex dynamic environments. Our focus is on (explainable) anticipatory space-time mental model formation at a semantic level to heuristically guide low-level motion computation. Our method is hybrid, modular and elaboration tolerant integrating: 1) An ASP model characterising the dynamics of interactive motion trajectories; 2) Semantically-guided prediction for deriving `branching trajectory futures'; and 3) An energy-based {optimisation} model to evaluate, rank and filter anticipations. We evaluate with the Argoverse 2 benchmark, where each anticipated trajectory carries an explicit, inspectable event-level hypothesis, unlike end-to-end stochastic prediction.

---


### 42. [Clinically Interpretable Biological Age Estimation Using CatBoost and SHAP with Continuous and Categorical Features from NHANES](https://arxiv.org/abs/2610.20868)

**<font color=#1a73e8>作者：</font>** Yanni Sun, Zheng Qu, Kevin Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological age (BA) captures inter-individual variation in physiological aging beyond chronological age (CA). Although machine-learning models have advanced BA estimation, many rely primarily on continuous laboratory biomarkers, and SHapley Additive exPlanations (SHAP) dependence plots are typically interpreted visually. We developed a clinically interpretable machine-learning framework for BA estimation using heterogeneous clinical data from the National Health and Nutrition Examination Survey (NHANES 2011-March 2020, N = 24,983 adults aged >= 18). A CatBoost regression model incorporated 44 demographic, laboratory, physical examination, and lifestyle predictors to estimate CA, defining model-estimated age as BA. SHAP provided multi-level interpretability. Crucially, building on standard visual inspection, we implemented a prespecified automated procedure directly on SHAP dependence plots to quantify feature-value ranges associated with lowest and highest BA contributions, corresponding adjustment magnitudes, and zero-crossing thresholds. Model-estimated BA strongly correlated with CA in held-out testing data (Pearson r = 0.798, P < 0.001). Population-level SHAP identified blood urea nitrogen, serum glucose, vigorous recreational activity, red cell distribution width, and alanine aminotransferase among the leading predictors, with three categorical variables ranking among the top 25. Automated quantitative SHAP analysis mapped predictor-specific ranges, effect sizes, and inflection points, while waterfall plots enabled individual explanations. By extending qualitative visual interpretation to reproducible quantitative metrics across heterogeneous clinical data, this framework enhances transparency and provides a scalable methodological foundation for biological aging research and precision health.

---


### 43. [CogDrift-4D: Hierarchical Multimodal Modeling of Temporal Behavioral Decay for MCI Detection](https://arxiv.org/abs/2610.20877)

**<font color=#1a73e8>作者：</font>** Sankalp Vaish, Sumukh Veeramalla, Rishank Singh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early detection of mild cognitive impairment remains a critical bottleneck in dementia care, demanding scalable tools capable of capturing subtle behavioral decay. To capture the subtle temporal changes of cognitive decline, we introduce a behavioral dataset collected across seven unscripted multimodal interactions over an 18-month horizon. This dataset formalizes continuous, multi-session interactions into a dense 4D tensor (Batch * Session * Time * Feature) that explicitly preserves concurrent local dynamics alongside long-term changes. To effectively process these complex behavioral patterns, we propose CogDrift-4D: a novel, hierarchical 4D Transformer framework. To capture the complex trajectory of cognitive decline, CogDrift-4D implements a dual-level behavioral fatigue and drift modeling architecture. At the intra-session level, the model computes localized least-squares regression slopes to quantify the acute ``fading'' of frame-level facial action units and acoustic energy. At the inter-session level, a recursive cross-attention feedback encoder acts as a cumulative fatigue accumulator, mapping the patient's continuous behavioral drift across successive sessions. To mitigate environmental noise and track failures across sessions, a localized Quality Gate dynamically filters low-integrity features before final fusion, also an early fusion that integrates semantic insights with raw physical dynamics. Evaluated on structured verbal and linguistic interactions, our architecture successfully detects MCI with a classification accuracy of 0.733 +- 0.13 and an F1-score of 0.716 +- 0.14, outperforming advanced baselines. The framework provides a mathematically rigorous, scalable, and robust foundation for home-based, real-time dementia screening.

---


### 44. [DefoliationCAM: An Edge-AI System for Real-Time Insect Defoliation Severity Assessment in Grapevines](https://arxiv.org/abs/2610.20879)

**<font color=#1a73e8>作者：</font>** Fuchen Li, Wei-Zhen Liang, Pin-Chu Lai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Insect-induced defoliation threatens grapevine health and yield, yet severity assessment relies on subjective manual scouting. We developed DefoliationCAM (D-CAM), a solar-powered edge AI system that estimates canopy defoliation and transmits results via LoRa to a web dashboard. The pipeline uses YOLOX-Nano to localize grapevine cordons in 4K images and a MobileNet-based classifier with lightweight channel attention to classify 320 x 320 pixel patches. The 29,674 field-collected patches were labeled as background or one of four damage levels: no to negligible, mild, moderate, and severe. Merging moderate and severe classes reduced the class imbalance ratio from approximately 40:1 to 8.8:1. Synthetic augmentation increased macro-F1 from 0.768 to 0.838. The classifier outperformed ResNet-50 in macro-F1 with fewer parameters (1.08 M versus 23.52 M). Patch predictions were aggregated into a canopy-level Non-linear Global Defoliation Severity (NGDS) score and validated against an entomologist's ratings of 86 held-out canopy images. Quadratic discriminant analysis identified boundaries of 9% and 29% separating negligible damage, mild damage requiring monitoring, and action-level damage warranting on-site scouting and insecticide treatment consideration. The 29% boundary aligned with the 25%-30% action threshold range for Japanese beetle management in grapevine. Using TensorRT FP16 on an NVIDIA Jetson Orin Nano, the pipeline processed each 4K image in approximately 1.5 s, with a complete operating cycle of 57-60 s. A five-week deployment of two field units demonstrated the feasibility of autonomous solar-powered operation, LoRa communication, and remote defoliation monitoring. D-CAM supports frequent, objective canopy damage assessment for targeted scouting and timely pest-management decisions.

---


### 45. [Pixels to Tokens: Token Space Efficient Active Learning for Low-Budget Semantic Segmentation](https://arxiv.org/abs/2610.20881)

**<font color=#1a73e8>作者：</font>** Utku Cicek, Mahip Singh, Ziyao Shang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While foundation models and vision transformers (ViTs) have redefined visual representations, current active learning (AL) strategies for these backbones largely operate at the patch or region level, where annotation requirements remain high due to extensive pixel labeling. Extending ViT-based AL to the pixel-level, low-budget regime is uniquely challenging: with as little as one pixel query per image, a method must simultaneously identify the most informative locations and train a reliable decoder head from an extremely sparse signal. We introduce TEAL (Token-space Efficient Active Learning), the first pixel-level AL framework built around ViT representations. TEAL uses a frozen ViT backbone and performs diversity-based selection directly on its native token lattice, avoiding the artifacts introduced by interpolating token embeddings to dense pixel resolutions. Our framework applies a two-level MaxHerding strategy over multi-layer token descriptors to select representative candidates, followed by margin-based uncertainty refinement on a finer decoder grid. Across CamVid, Cityscapes, ADE20K, and Pascal Context, TEAL consistently outperforms previous baselines under extreme label scarcity, improving over the strongest baseline by up to +24.36 mIoU with a single labeled pixel (px) per image, and reaching up to 97% of fully supervised performance with just 10 px. To rigorously establish the source of the gains, we further show that the improvements persist when all baselines are equipped with the same DINOv3 backbone, demonstrating that coupling token-space selection with uncertainty refinement on the decoder grid makes ViT token geometry an effective foundation for extremely low-budget active segmentation.

---


### 46. [Wrong Votes, Right Gradients: Why Majority-Vote Rewards Track Verifiable RL](https://arxiv.org/abs/2610.20898)

**<font color=#1a73e8>作者：</font>** Dylan P. Wilson, Chengsong Huang, Jiaxin Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with self-generated labels, such as majority vote over a model's own samples, often recovers most of the gain of training with verifiable rewards. This is puzzling from the usual prompt-level view, in which majority vote only returns a model's modal answer and cannot add information about correctness. We argue that the relevant unit is the batch-level update. Because parameters are shared, a prompt's own gradient accounts for less than 1\% of the change in that prompt's output at practical batch sizes, so a wrong label matters only to the extent that label errors share a direction across prompts. We decompose the majority-vote update into shrinkage and misdirection relative to the gold update, and show that misdirection vanishes with batch size whenever errors are incoherent across prompts, however often the labels are wrong. Measuring per-response gradients on five models, we find that majority-vote errors are as incoherent as a random-reward null, that the majority-vote update agrees with the gold update as closely as two independent gold updates agree with each other, and that its noise-corrected cosine with the gold update is 1 within error. Randomly flipping up to 30\% of gold labels leaves the update direction intact, while the same fraction flipped by a shared rule destroys it, and rewards that favor a kind of response on every prompt, such as a learned reward model, fall measurably short. The equivalence holds at every checkpoint we examine but is local: gold-reward training still ends ahead on held-out majority accuracy. Error coherence, not error rate, determines when self-generated labels can stand in for verification.

---


### 47. [Sign Betting for Misspecified Regression: Variance Adaptivity and Optimal Approximation](https://arxiv.org/abs/2610.20903)

**<font color=#1a73e8>作者：</font>** Yinan Li, Han Han, Kwang-Sung Jun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study bounded regression under model misspecification, evaluating a function $f$ by its $L_1(P_X)$ distance to the conditional mean $\eta(x)=\mathbb{E}[Y\mid X=x]$, rather than the standard $L_2(P_X)$. This $L_1$ metric is natural for downstream decision problems such as bandits and reinforcement learning. We analyze the min--max estimator of Baraud & Maillard (2025), which we call \emph{sign-betting regression}. Our main results show that sign-betting regression achieves high-probability $L_1$ oracle inequalities under misspecification. Under realizability, our bound adapts to the average conditional variance and recovers the variance-adaptive rate of Li et al. (2026). We further characterize the optimal universal approximation factor for proper learning by showing that sign betting achieves factor 3, while no proper learner can satisfy a distribution-free, high-probability $L_1$ oracle inequality with a universal approximation factor strictly below 3. We extend the upper-bound analysis beyond finite classes and complement the theory with experiments in synthetic and real-world model-selection tasks.

---


### 48. [Task-Centric Multimodal Learning for Cognitive Impairment Detection](https://arxiv.org/abs/2610.20906)

**<font color=#1a73e8>作者：</font>** Sankalp Vaish, Rishank Singh, Sumukh Veeramalla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dementia affects millions of older adults worldwide, yet early detection remains difficult outside clinical settings. Traditional models primarily rely on text or voice-based responses, capturing only a limited view of human cognition despite the inherently multimodal nature of human expression. This work proposes a contactless, multimodal screening framework that leverages video, audio, and text signals collected during structured voice-based interactions with Amazon Alexa. By incorporating these modalities, our approach captures a more holistic representation of human behavior encompassing speech patterns, vocal characteristics, facial expressions, and linguistic structure, which may enable more accurate detection of cognitive decline. Different participants completed three conversational tasks designed to probe spontaneous speech, comprehension, and recall. We pursued three objectives: (1) evaluate which of the three Alexa tasks provides the most informative cognitive signals, (2) compare the effectiveness of unimodal models, and (3) assess the benefits of multimodal fusion models. Task-level analysis shows that the video model achieves its best performance on Command-Reading, with an accuracy of 0.65 (AUC 0.69), while the audio model performs best on Question-Answering, reaching an accuracy of 0.67 (AUC 0.73). In contrast, the multimodal model demonstrates consistently stable performance across tasks, achieving an accuracy of 0.76 (AUC 0.75) on Command-Reading and 0.76 (AUC 0.73) on Question-Answering. These findings demonstrate that multimodal behavioral cues captured through naturalistic interactions can reliably distinguish MCI from healthy aging, highlighting the limitations of traditional diagnostic paradigms and supporting the shift toward multimodal, real-world cognitive assessment frameworks.

---


### 49. [Decision-FLIP: Budget-Free Structured Pruning for Gaussian Occupancy Models](https://arxiv.org/abs/2610.20917)

**<font color=#1a73e8>作者：</font>** Jingxing Li, Anurag Paul, Subhasis Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Occupancy predictors rely on large persistent banks of Gaussians or learned queries whose size is fixed by hand. Common pruning proxies, such as opacity, activation frequency, or parameter magnitude, do not measure whether removing a row changes the model's voxel decisions. We introduce Decision-FLIP, a budget-free compilation framework whose scoring and structure selection need only unlabeled calibration inputs. Exact Mean-FLIP scores each persistent row by the number of voxel argmax decisions that change when the row is removed from the readout; a guarded Otsu split of the log-score distribution selects the survivor count without a target and abstains when the split is unsupported; and the survivors are physically compiled into a smaller checkpoint, so camera sampling, attention, and aggregation shrink with the bank. For streaming banks, scores are integrated over each row's lifecycle through warp, death, and refill. Across four Gaussian-bank model-dataset settings and one persistent-query transfer, the automatically selected cuts remove 12-79% of eligible rows and cut bank/query-dependent latency by 7-45% across settings with component profiles, with whole-model savings of up to 8.0% on the primary endpoints bounded by fixed-cost image, voxel, and sensor modules and peak-memory savings of up to 16.6%. Under matched one-epoch recovery controls, semantic mIoU changes by at most 0.18 point. Same-$K$ controls show that the ranking, not only the bank size, matters: random removal collapses GaussianFormer-1 and OccFormer, while label-free Mean-FLIP matches or outperforms supervised Taylor ranking on all five settings where that control was run. The method applies when removable primitives keep a stable checkpoint-row identity; it is budget-free in survivor count, not parameter-free.

---


### 50. [A Multi-Tiered AI Accessibility Model (MAIAM): Proportionate Access and Capability Limits for Comprehensive Frontier AI Safety](https://arxiv.org/abs/2610.20921)

**<font color=#1a73e8>作者：</font>** Chai K. Toh, Vasu Raj Jain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most debate about releasing capable AI systems treats the choice as binary: keep the model behind an API, or publish the weights. That framing runs together two separate decisions. One is how capable a system may become. The other is who may obtain a given capability, and on what terms. This paper is about the second decision. We propose a Multi-Tiered AI Accessibility Model (MAIAM) that sorts access by purpose, safety, and capability instead of by release artifact. Tier 1, AI for Learning, is broadly accessible and deliberately capability-bounded. Tier 2, AI for Exploration, serves research and development under registration, identity, and usage controls that tighten as capability rises. Tier 3, Full-Scale Frontier AI, is available only through structured, recorded, and accountable access. The principle behind the tiers is that accessibility should be proportional to capability, safety, and risk. We show why publishing frontier-class weights forfeits every safety lever a developer has after release, and, using evidence that safety fine-tuning can be stripped from open weights for a few hundred dollars, why an evaluation of the base model says little about its derivatives. We give criteria for assigning a system to a tier along capability, autonomy, domain-consequence, and usage/safety axes, and combine MAIAM with the SAFE AI Operating Point into a two-part framework: a Capability Boundary that fixes the safety limits not to be crossed, and an Accessibility Boundary that fixes who may obtain a capability below that limit. Capability limits alone do not make AI safe; a tiered access regime administered by regulating bodies is also needed.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-278](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
