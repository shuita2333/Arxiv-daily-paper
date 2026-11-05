# 📦 其他研究 | 2026年11月06日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-236](./part-05.md)

---

### 151. [The Split Protocol Decides the Result: Re-Evaluating Encrypted Traffic Classification](https://arxiv.org/abs/2611.06290)

**<font color=#1a73e8>作者：</font>** Mayan Sharma, Kriti Saini, Devansh Behl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Encrypted traffic classifiers are routinely reported at 95-99% accuracy. We show that on one of two public corpora, the same model and code score macro-F1 0.992 under the evaluation protocol standard in the literature and 0.567 under a protocol that keeps flows from one packet capture on one side of the split. Nothing changes but the partition (gap 0.426 over eight seeds, p = 0.008 after Holm-Bonferroni correction).
The inflation is not a property of random splitting as such. On a month of backbone QUIC traffic, we evaluate five split protocols at eight seeds each: random, temporal and client-disjoint splitting are statistically indistinguishable from session-disjoint, while server-disjoint splitting costs 0.192 macro-F1 (d = 17.0, p = 0.008). Which axis matters depends on how the corpus was collected, in a way invisible from its label space.
We give a diagnostic that identifies the right axis before any model is trained: single-identifier probes. A decision tree on the capture identifier alone reaches 0.983 under a random split and exactly 0.000 under session-disjoint splitting.
Under this evaluation, a metric-trained flow embedding leads four deep baselines but does not beat gradient-boosted trees on twenty packet sizes. Five of our own pre-registered architectural claims fail: distance-based rejection of unknown applications beats softmax thresholding, but ablating every metric objective makes rejection better, because class separation correlates at r = -0.88 with rejection quality. Few-shot enrollment is flat within a corpus but, across corpora, five labelled flows per class recover 91% of the deficit left by failed zero-shot transfer.
All splits, results, code and negative findings are released.

---


### 152. [STEK: Structural-Terrain-Enhanced Koopman-Inspired Cross-Channel Regularization for Retrospective Battery Multi-Target Estimation](https://arxiv.org/abs/2611.06299)

**<font color=#1a73e8>作者：</font>** Jing Wang, Shiyuan Piao, Fugee Tsung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrospective battery characterization across heterogeneous cells is challenging because cycling records vary substantially with chemistry, protocol, cell format, capacity, and operating conditions. An endpoint charge--discharge curve captures the local condition of an evaluated cycle, while a cell-level lifecycle terrain summarizes structural evolution across the archived trajectory. We propose STEK, a structural-terrain-enhanced framework for retrospective battery multi-target estimation. STEK combines a cell-level lifecycle (dQ/dV) terrain with an endpoint-derived structural proxy through quality-proxy-conditioned gating. Bounded FiLM and a validity-gated residual head refine the endpoint-curve representation while preserving a curve-based prediction pathway. Battery-type and optional material-text representations further condition an identity-centered low-rank linear map, providing a Koopman-inspired cross-channel consistency objective without modeling temporal dynamics or performing rollout. Under the fixed seven-output MIX-battery protocol, the full retrospective setting improves aggregate performance over endpoint-only learned baselines across multiple temporal backbones; this comparison reflects both the additional archived context and the modeling design. Under matched auxiliary inputs, STEK outperforms direct concatenation and quality-unaware FiLM, while descriptor-removal tests show graceful fallback to the endpoint pathway. Deterministic rules remain preferable for directly recoverable capacity summaries. The method targets retrospective archive harmonization rather than online estimation from cycle t alone.

---


### 153. [When Does Risk-Controlled Throughput Forecasting Actually Control Risk? A Reproduction Study on LEO Satellite Link](https://arxiv.org/abs/2611.06307)

**<font color=#1a73e8>作者：</font>** Mayan Sharma, Kriti Saini, Devansh Behl 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk-budgeted throughput forecasting converts a point forecast of LEO satellite capacity into a conservative bound whose overestimation rate is held at a user-specified budget, so that admission control can act on it safely. We reproduce the state of the art, BG-CFQS, on the three Starlink traces its authors used and on an independent fourth dataset, and report four findings. First, its risk guarantee is reproducible but conditional on the calibration split: under a random split we recover every published quantity, including risk-pass on 3 of 3 datasets, but under a contiguous temporal split, which is what a deployed terminal faces, it holds on 1 of 3. Second, independent of any split, the method cannot serve a risk budget below 0.15, the low end of its candidate quantile set. On all four datasets the achieved rate is identical at budgets of 0.05, 0.10 and 0.15, overshooting by 1.4x to 3.7x at the tightest. Third, static conformal calibration cannot improve a ranking, only shift an operating point; we confirm this exactly on latency spike detection, where online calibration improves AUPRC by up to 51%. Fourth, group-conditional online recalibration splits into two mechanisms. The online part replicates: it tracks the budget within 1% from 0.05 to 0.35, where static calibration is 16 to 21% off. The group-conditional part does not: on three of four datasets, conditioning on any available covariate, including measured serving-satellite geometry, is worse than not conditioning, and our attempt to predict which datasets benefit failed. What is new here is empirical, not algorithmic: we claim the findings, not the methods.

---


### 154. [Conformal Prediction for Distribution-to-Distribution Regression](https://arxiv.org/abs/2611.06320)

**<font color=#1a73e8>作者：</font>** Trung-Khang Tran, Tuan A. Hoang, Viet-Hoang Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal Prediction (CP) provides a model-agnostic framework for constructing finite-sample prediction sets with coverage guarantees and has become a tool for reliable decision-making in high-risk settings. Recent advances have extended Split Conformal Prediction to increasingly complex learning problems, including multilabel, high-dimensional, and functional outputs. In this work, we study CP for Distribution-to-Distribution Regression, a setting of growing interest across many application domains. We show that a naive application of Split CP yields prediction sets that, while marginally valid, are non-interpretable, e.g., lacking a well-defined volume or a tractable sampling procedure, and of limited practical value. To overcome this, we propose a new conformal framework that operates in an orthogonal basis space, producing interpretable prediction sets while preserving coverage guarantees. We further develop an adaptive variant with asymptotic conditional coverage under mild assumptions. Empirical results on synthetic and real-world datasets validate the effectiveness of the proposed approach. The code is publicly available at this https URL.

---


### 155. [EnzymeRSI: A dual-loop recursive self-improvement system for enzyme design](https://arxiv.org/abs/2611.06321)

**<font color=#1a73e8>作者：</font>** Genoria AI Team, Yuejie Hou, Lixiang Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improvement in enzyme engineering is usually pursued by optimising which candidates to assay within a fixed model and workflow; when the bottleneck arises from a mismatched method or a failing workflow, that route is difficult to escape. We present EnzymeRSI, a dual-loop system for recursive self-improvement (RSI). The outer loop evolves harness assets without changing model weights, the inner loop develops prediction and selection algorithms under controlled conditions, and a cloud laboratory system is specified to close the physical loop with quality-controlled feedback. By updating its prediction strategy through iterative comparison, the outer loop raised the mean development-set Spearman correlation on ProteinGym by 0.044 across five assays, reaching 0.335 on CD19 and 0.683 on OPSD (rhodopsin); of the two first places, only CD19 was produced by the outer loop itself. In the self-improvement of the ThermoMPNN algorithm the inner loop reached a PCC of 0.849, and on TadA-Bench it reached a Spearman correlation of 0.307 in 1.13 h. In three prospective wet-lab tests of the system's experimental decision-making, 10 of the 32 candidates that had not been pre-specified for the luciferase RLuc showed at least twice the wild-type activity; a recommended variant of the cytidine deaminase A3A raised 5mC conversion to 90.2%; and path selection in evolution raised the catalytic efficiency of the DNA polymerase KOD-E on a modified substrate to 31.1 times that of the parent. By treating the organisation of the research workflow and the development of algorithms as a single falsifiable dry-to-wet loop, this work offers an evolutionary paradigm for moving beyond the blind spots of a fixed method and for autonomous enzyme engineering.

---


### 156. [Learning to Tune with Biased Gradients: Iterative Feedback Tuning of Model-Free Control on Throttle Valves](https://arxiv.org/abs/2611.06338)

**<font color=#1a73e8>作者：</font>** Félix Martinez-Jiménez, Sander Miller-Murphy, Tobie Ondoa-Essomba 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative feedback tuning (IFT) learns the parameters of a fixed-structure controller by stochastic gradient descent. At each iteration, two closed-loop experiments are run on the plant: the first one measures the tracking error, and the second one, driven by this error, provides the sensitivities from which the gradient of the cost is estimated. This estimate is unbiased for linear plants only. We study the biased case on automotive electronic throttle valves, whose friction and stiction vary between valves and runs, controlled by an intelligent proportional (model-free) controller, which is an incremental PI controller. We show that the mismatch of the controller state at the start of the two experiments, which stiction makes unavoidable, adds an error inversely proportional to the amplitude of the second experiment. On digital twins of ten valves, the IFT gradient is a descent direction in only 69\% of the low-cost region, friction being the cause, and all update rules plateau and then drift. On two hardware valves, the best update rule depends on the noise structure of the gradient. On the first valve, where one gradient component is buried in noise, Adam outperforms Gauss--Newton, its normalisation and its momentum each improving one parameter. On the second valve, where both components are consistent, the same normalisation amplifies a direction that Gauss--Newton rightly discounts, and Adam drifts to a controller worse than the initial one. The twins reproduce the mechanism but not this ranking.

---


### 157. [Prism: Bidirectional Self-Teaching for Unified Multimodal Models](https://arxiv.org/abs/2611.06343)

**<font color=#1a73e8>作者：</font>** Peng Zhang, Qian Chen, Xianyin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models (UMMs) aim to support visual understanding and generation within a single model. Existing post-training methods either use understanding as a fixed teacher to improve generation, or rely on ground-truth trajectories to supervise both understanding and generation. Prism instead derives bidirectional supervision from self-generated interleaved rollouts, constructing training targets according to the reliability of their text and image chains. We propose Prism, a bidirectional self-teaching post-training method for UMMs. Like a prism decomposing mixed light, Prism decouples a coupled interleaved trajectory into a text chain and an image chain, assesses the reliability of each chain, and constructs a corresponding training target from their reliability states. Experiments on both SenseNova-U1 and BAGEL show that Prism improves both understanding and generation. On the generation side, GenEval improves from 85.8 to 89.2 (+3.4), and DPG improves from 86.1 to 87.3 (+1.2) on SenseNova-U1. On the understanding side, the total MME score improves from 2282.6 to 2311.6, and MMVP improves from 58.0 to 62.0. Consistent improvements are observed on BAGEL. These results highlight that Prism enables coordinated improvements in generation and understanding by constructing reliability-guided self-training targets from self-generated trajectories, without relying on an external verifier or externally annotated corrected trajectories during target construction.

---


### 158. [Today's Work, Tomorrow's Workforce: Incentivizing Learning in AI-Assisted Work](https://arxiv.org/abs/2611.06346)

**<font color=#1a73e8>作者：</font>** Moritz Diener, Daniel Hendriks, Philipp Spitzer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> At work, people develop skills through experience: novices acquire skills by completing tasks, while experts retain theirs through continued practice. AI assistance changes this process by offering workers a choice between solving tasks independently and accepting the AI's answers. While relying on AI saves immediate effort, it can also displace the practice needed to acquire and retain skills, including those required to oversee the AI. We extend an existing accept-or-solve model to a sequence of tasks in which workers' skills evolve through independent practice and reliance on AI. We compare myopic workers, who maximize immediate utility, with strategic workers, who also value their future skills. We show that novices can become trapped at low skill levels, while experts may lose skill, even as AI-assisted outcome accuracy remains high. Strategic workers, by contrast, may choose to solve independently even when AI is more accurate, recognizing the future value of acquiring and retaining their skills. We then study incentives that reward correct independent work and characterize the payments needed to encourage skill acquisition and retention. We show that independent work can become self-sustaining once workers acquire sufficient skill, eliminating the need for continued incentives. Counterintuitively, supporting a higher skill target can sometimes reduce long-run incentive costs, either by enabling self-sustaining independent work or by lowering the payments needed to maintain proficiency. Our findings thereby shift the focus from whether workers should rely on AI on individual tasks to how organizations can sustain human expertise over time, and which skills are worth investing in.

---


### 159. [Flexible Intensities Matter: A Comprehensive Re-evaluation of Hawkes Processes and Neural Temporal Point Processes](https://arxiv.org/abs/2611.06348)

**<font color=#1a73e8>作者：</font>** Hendrik Mehrtens, Florian Buettner, Oliver Stegle  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal point processes (TPPs) are the canonical framework for event sequence data, with applications spanning seismology, social media, and electronic health records. Recently, neural TPPs have been reported to substantially outperform classical TPPs, such as Hawkes processes, but these comparisons pitted flexible neural models against Hawkes processes in their most restricted form, and did not consider large-scale medical data. Here, we revisit this comparison through a systematic evaluation of Poisson and Hawkes processes of increasing flexibility against neural TPPs, on five established benchmark datasets and on two large-scale medical evaluation tasks derived from UK Biobank disease histories and MIMIC-IV ICU records, under autoregressive next-event prediction. First, the previously reported gap between Hawkes processes and neural TPPs largely disappears once Hawkes processes are equipped with flexible, learnable baselines and kernels. Second, the flexibility of the intensity parametrization also limits prior neural TPPs: a Transformer with a spline-based intensity head outperforms previous intensity-based neural TPPs and is on par with the intensity-free model. Decomposing the log-likelihood into a time term $\log p(t)$ and a type term $\log p(d \mid t)$, we find that this flexibility advantage lies almost entirely in the time density: more flexibility does not improve the type term. On these benchmarks, the gains of neural TPPs thus lie mostly in modeling when events occur, not which. Third, our results underscore the value of complex datasets for evaluating TPPs: only on the MIMIC-IV ICU records do neural TPPs retain an advantage in the type term. Our results inform both future method development and model choice. We release our framework, TorchPP, as an open-source package with consistent implementations of classical and neural TPPs.

---


### 160. [FlashRelight: Portrait Video Relighting with Dynamic Lighting](https://arxiv.org/abs/2611.06355)

**<font color=#1a73e8>作者：</font>** Jiahui Sheng, Le Li, Limin Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Portrait video relighting aims to modify the illumination of a portrait video while preserving photorealism and temporal stability. The task becomes particularly challenging under dynamic lighting, where illumination direction, intensity, and color vary over time. To tackle this problem, we introduce FlashRelight, a novel two-stage framework for dynamic portrait video relighting. FlashRelight first suppresses the source illumination through delighting, and then synthesizes the target dynamic lighting on an illumination-neutral portrait video. FlashRelight supports three complementary control modalities: envmap sequences for explicit frame-level lighting control, dynamic lighting text for semantic illumination editing, and lighting reference videos for visual lighting transfer. Training follows a low-cost hybrid strategy that combines static one-light-at-a-time (OLAT) data with generated dynamic-lighting portrait videos, covering both controlled illumination variation and realistic portrait motion. Extensive experiments show that FlashRelight achieves temporally coherent and photorealistic dynamic relighting while enabling flexible cross-video lighting transfer. Code is available at this https URL

---


### 161. [Corralling AI Risks with Grassroots Contracts](https://arxiv.org/abs/2611.06374)

**<font color=#1a73e8>作者：</font>** Ehud Shapiro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI's inflection point is a fountain of alarming risks. Digital platforms in particular are vulnerable to three major AI risks, as those in control of global platforms cede control to AI, of the algorithms, of membership and of content: (1) AI control of global platforms, social and economic, used by the majority of humanity, resulting in the majority of humanity becoming vulnerable to AI control. (2) Unaccountable AI agents operating anonymously on social and economic digital platforms, side-by-side with humans, possibly masquerading as humans, serving unknown masters with unknown goals, operating under unknown restraints without accountability or culpability. (3) Unattributed deepfakes generated by anonymous AI, with people unable to distinguish them from genuine content and with their producers evading accountability and culpability.
Here, we propose to corral these AI risks with grassroots contracts, a digital incarnation of a two-centuries old notion of Pierre-Joseph Proudhon. We present grassroots contracts for a social graph with accountable AI agents and for a social network with digital provenance, and working smartphone apps that implement the two and show how they corral these major AI risks: (1) AI control of global platforms. (2) Unaccountable AI agents. (3) Unattributed deepfakes.

---


### 162. [From hydrological laws to catchment models: A process-based model matches deep-learning accuracy on three continents](https://arxiv.org/abs/2611.06382)

**<font color=#1a73e8>作者：</font>** Xilin Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dooge asked whether hydrology has laws at the catchment scale. We ask whether a low-dimensional system built under physical laws can match the accuracy of neural networks that outperform process-based models on the same inputs. Three laws constrain a lumped catchment model. Conservation makes it a flux-connected storage network, dissipation fixes the sign of every flux and aggregation determines how the unresolved composition enters the fluxes, through effective laws over threshold distributions and a memory of the forcing. These laws admit four kinds of refinement. A parsimonious model under them, CaRT (11 parameters per catchment), is refined in a loop assisted by AI agents. Each refinement addresses an observed deficit through a hypothesis from the literature. The result, CaRT+, has fourteen states, 35 parameters per catchment and no daily neural network. Most refinements follow from aggregation over thresholds or from variables that carry no water but modulate fluxes. On 602 British and 593 US gauged catchments, single CaRT+ models reach median Nash-Sutcliffe efficiencies of 0.863 and 0.765 in held-out years. A stateful LSTM reaches 0.869 and 0.751 and an entity-aware LSTM 0.862 and 0.754, while three-seed LSTM ensembles remain ahead of the CaRT+ ensemble by 0.003-0.012 in median paired NSE. On 505 drier Australian gauged catchments unused in development, single CaRT+ models reach 0.778 against 0.762 and 0.753 for the two LSTMs. The results suggest that catchment-scale laws exist as laws of form, with the constitutive families shared and only their parameters learned.

---


### 163. [Presentation Sensitivity in Typed Decision Models for Subjective Text Evaluation](https://arxiv.org/abs/2611.06384)

**<font color=#1a73e8>作者：</font>** Jatin Agrawal, Radhika Mamidi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed decision models offer structured choices, scores, and probabilities for low-cost automated evaluation. We present a controlled audit of presentation sensitivity in Jev, Clef Flash, and Perplexity Decider across native choice and score interfaces. Across six datasets with 9,000 multiply annotated humor, helpfulness, and summarization items, we collect 702,000 judgments under interventions that vary positions, identifiers, authorship claims, endorsements, decision framing, and rating rubrics while preserving the evaluated texts. Jev's second-position probability advantage reaches 6.11 percentage points on summaries; reversing reader endorsements changes Perplexity's selected humor text on 40.40% of pairs; and rejection framing reduces Clef's summary agreement with human preferences by 23.36 points. Rating formats also shift score levels while often preserving rankings. Across these findings, repeatability, presentation robustness, and human alignment emerge as distinct properties of an evaluator. Reliable use therefore requires validating the decisions and score interpretations on which an evaluation pipeline depends.

---


### 164. [Shoot on (Core)Sight: Re-enabling Secure Debug on the RP2350 with Photon-Emission Microscopy and Laser Fault Injection](https://arxiv.org/abs/2611.06386)

**<font color=#1a73e8>作者：</font>** Antoine Plin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fault-resistant policy storage does not guarantee fault-resistant enforcement. We demonstrated this distinction on the RP2350A4 using differential photon-emission microscopy (PEM) and laser fault injection (LFI). PEM narrowed the area for laser scanning, which found two sites where pulses set the DEBUGEN bits enabling core~1 Secure debug. An online attack sequence using only Serial Wire Debug (SWD) feedback restored sustained access. After rescue reset, the sequence recovered a 128-bit test secret. This reset reloads the secret's runtime page lock from a stored policy that permits Secure reads and prevents user firmware from tightening the lock.

---


### 165. [MA-Mesh: Resilient Multi-Agent Collaboration via Role-based Self-Healing](https://arxiv.org/abs/2611.06389)

**<font color=#1a73e8>作者：</font>** JunYong Lee, Woo Kyung Kim, Honguk Woo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective collaboration in multi-agent systems requires mechanisms for coordination and adaptability in dynamic and uncertain environments. However, existing multi-agent systems rarely model resilience explicitly, instead relying on ad-hoc output correction that limits systematic, runtime management of robustness. In this work, we propose Multi-Agent Mesh (MA-Mesh), a framework that constructs a role-based self-healing layer on top of a collaboration pattern. Specifically, MA-Mesh generates resilience-aware system specifications and synthesizes them into executable multi-agent policy code. To enhance resilience, we introduce two self-healing mechanisms: Cross-agent reflection, a mechanism that allows agents to evaluate not only their own outcomes but also the performance of their peers, enabling informed behavioral adjustments and collective policy refinement; Role-based failover, a strategy which dynamically reassigns roles and enables agents to substitute for one another when sub-tasks fail or agents underperform, ensuring continuity of task execution. Experimental results across diverse tasks (e.g., software development, tool use, scientific reasoning) demonstrate that MA-Mesh significantly outperforms existing multi-agent systems in both task performance and robustness under system uncertainty.

---


### 166. [KolTa: A Physics-Informed Active Learning Framework for Formulation Discovery with Limited Data](https://arxiv.org/abs/2611.06394)

**<font color=#1a73e8>作者：</font>** Boyong Tang, Tao Wang, Lei Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding high-performing formulations is difficult when few have been measured and experimental budgets are limited. We propose KolTa, an active learning framework that selects batches to discover the top 5% of formulations at a target temperature under a fixed query budget. KolTa combines a three-stage predictor of component contributions, role-conditioned interactions, and anchored temperature response with task-specific soft physics constraints. Its Physics-Residual-Calibrated Upper Confidence Bound (PRC-UCB) acquisition rule combines predicted utility, ensemble disagreement, and a target-temperature physics residual, with nonnegative exploration weights fitted to out-of-fold signed errors. We evaluate the framework on three measured tasks and one simulated task covering binary-mixture viscosity, drug solubility, ionic-liquid viscosity, and electrolyte conductivity. KolTa ranks first or second in mean area under the learning curve (AULC) on every task and outperforms seven of the eight comparator strategies in paired tests, winning 75 of 78 paired comparisons across tasks and seeds against those seven strategies. Across the three measured tasks, its largest gap to the best mean AULC is 0.032, compared with at least 0.056 for every comparator. On Drug, reaching 80% average recovery of the remaining targets across drugs requires an estimated median of 348 additional formulation queries, about 18% fewer than the fastest comparator. Researchers can adapt the framework to diverse formulation problems through component roles and physical constraints.

---


### 167. [Interpretable Text Embeddings Based on Hierarchical Questions](https://arxiv.org/abs/2611.06402)

**<font color=#1a73e8>作者：</font>** Kohei Oda, Po-Min Chuang, Kiyoaki Shirai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> QA-based text embeddings represent texts as vectors consisting of 1/0 answers to yes/no questions. Although these embeddings provide detailed information for interpretation and achieve high task performance, they often require humans to examine a large number of questions. Furthermore, the relationship between the number of questions and the appropriate level of question granularity has not been sufficiently studied. To address these challenges, we propose a method for constructing hierarchical questions for text embeddings. As the hierarchy deepens, questions become more specific and their number increases. During interpretation, we reduce the number of questions that humans need to examine by replacing questions at deeper levels with aligned questions at shallower levels. The question hierarchy is constructed through recursive clustering, contrastive prompting, and question alignment. Experimental results on general-purpose tasks show that our method improves interpretability while maintaining task performance. It is also found that, when only a limited number of questions are available, questions at shallower levels tend to achieve higher task performance than those at deeper levels, even with the same number of questions.

---


### 168. [A Bag of Tricks for Defending Deep Learning-based Face Recognition Pipelines against Backdoor Attacks](https://arxiv.org/abs/2611.06412)

**<font color=#1a73e8>作者：</font>** Quentin Le Roux, Marti Jimenez, Yannick Teglia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The protection of mature, multi-stage Face Recognition Systems is crucial to system providers. This technical report targets the threat model most relevant to industry practitioners: although model training is performed in-house, training data is sourced from possibly-compromised third parties. Given this setting, we present three practical defense "tricks" against data poisoning-based backdoor attacks. The first operates at training-time, detecting poisoned identities during training or prior to a pipeline's deployment. The last two operate at inference-time, filtering suspicious inputs before an answer can be sent back to a potential attacker. Each method is presented with their motivation, algorithms and computational impact, and evaluated on realistic face recognition workloads. Our goal is to provide actionable hardening techniques to system providers.

---


### 169. [Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory in Exploration Tasks](https://arxiv.org/abs/2611.06414)

**<font color=#1a73e8>作者：</font>** Chongyuan Dai, Yaling Shen, Zirui Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term problem-solving processes, such as scientific research and software development, proceed along an evolving trial-and-error trajectory toward a central goal. We term these \textit{exploration tasks}, which require models to remember not only facts but also how solutions are tested against intermediate outcomes and early attempts are continually revised or revived. However, existing long-term memory research focuses on factual recall and updates, overlooking the interconnected nature of exploration. We observe that exploration processes naturally form graphs, with branching approaches linked by revisions and reconsiderations. Motivated by this, we propose \textsc{LExMem}, a graph-guided benchmark designed to evaluate \underline{\textsc{Mem}}ory in \underline{\textsc{L}}ong-term \underline{\textsc{Ex}}ploration tasks. We model exploration processes as graphs and introduce an evolutionary mechanism to increase their structural complexity, yielding 224 dialogues and 2,018 question-answer instances derived from graph structures. Building on the same insight, we propose \textsc{LExGraph}, a graph-based memory framework that incrementally organizes dialogues into interconnected memory nodes and retrieves evidence through hybrid retrieval and neighbor expansion. Extensive experiments demonstrate that \textsc{LExMem} poses a significant challenge to existing retrieval- and memory-based systems, whereas \textsc{LExGraph} achieves superior performance and generalizes effectively to external benchmarks. Codes and datasets are available at this https URL.

---


### 170. [Unaligned Image Guided Denoising via Cross-modal Conditional Flow Matching](https://arxiv.org/abs/2611.06422)

**<font color=#1a73e8>作者：</font>** Runmin Zhang, Linshan Li, Si-Yuan Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents UGD-FM, a novel unaligned image guided denoising framework based on cross-modal conditional flow matching. Unlike previous approaches that assume spatially aligned inputs or only handle small-baseline rectified pairs, we address a more challenging setting where severe target noise and large-range two-dimensional cross-modal misalignment coexist. Specifically, we formulate guided denoising as a progressive flow matching process, allowing image restoration and aligned guidance aggregation to mutually reinforce each other. To support efficient few-step inference, we introduce a stage-focused and inference-consistent training strategy that focuses on task-critical denoising stages, and mitigates the training-inference mismatch. We further propose adaptive sparse guidance propagation for efficient and reliable large-range matching, regularized by perceptual and geometric auxiliary losses. Experiments demonstrate that UGD-FM achieves state-of-the-art denoising performance with only one or two inference steps, and is compatible with modern single-image restoration backbones.

---


### 171. [Partially Interpretable Decision Trees](https://arxiv.org/abs/2611.06428)

**<font color=#1a73e8>作者：</font>** Ludovic Schwartz, Federico Berton, Tim van Erven  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partially interpretable models extend simple interpretable models with the option to defer complicated inputs to an accurate but uninterpretable black-box model. By deferring more inputs, the model gets more accurate; by deferring fewer, it gets more interpretable. Existing procedures to train such partially interpretable models build on linear models or decision rules. We propose three algorithms for decision trees: a partially interpretable extension of the existing Branches algorithm, which performs exact search to optimize the tree; a conversion algorithm that we run on top of standard CART, which is computationally more efficient; and a generalized CART whose splitting criterion takes into account the option to defer while growing the tree. Perhaps surprisingly, the performance of the three algorithms is similar across many realworld datasets. We can explain this through a formal bound on the potential gain of smart tree construction, provided the black box accuracy is sufficiently homogeneous across the domain. We also construct a synthetic dataset where the accuracy of the black box is deliberately inhomogeneous. There, our deferral-aware generalization of CART does outperform regular CART and matches the performance of exact search. Finally, we evaluate an application to concept bottleneck models. Partially interpretable decision trees can replace uninterpretable neural networks after the bottleneck. On undeferred inputs, the model is fully interpretable, and deferring preserves accuracy.

---


### 172. [Within-Family EfficientNet Scaling under Fixed-Resolution Transfer Learning for Spectral-Domain Optical Coherence Tomography Retinal Disease Classification](https://arxiv.org/abs/2611.06452)

**<font color=#1a73e8>作者：</font>** Shkelqim Sherifi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background/Objectives: CNNs perform well in retinal disease classification from spectral-domain optical coherence tomography (SD-OCT), but whether EfficientNet's natural-image scaling hierarchy transfers to medical-image transfer learning at fixed resolution remains unclear. This study evaluates EfficientNet-B0-B7 for four-class SD-OCT classification and accuracy-efficiency trade-offs. Methods: Eight ImageNet-pretrained variants (4.05-64.10M instantiated backbone parameters) were evaluated at 224x224 on the Kermany dataset. Grayscale images were replicated to RGB and processed using model-embedded preprocessing and augmentation. Training comprised frozen-backbone head training followed by partial fine-tuning. Metrics covered classification, discrimination, efficiency, and visual analyses. Results: Test accuracy varied non-monotonically from 95.93% (B0) to 96.95% (B1); B7 achieved 96.73%. B1 had the highest accuracy and Drusen F1 (0.8780), while B7 had Drusen F1 of 0.8720 and the highest Drusen recall (0.9177). Drusen had the lowest F1 across all variants and contributed 82.2% of the summed squared deviation in class-specific F1; class ranking remained Normal > CNV > DME > Drusen. The OCT accuracy ranking differed from the reported ImageNet hierarchy, where B7 ranked first. The accuracy-to-parameter ratio fell from 19.82 to 1.48 percentage points per million total parameters. The final train-test gap had a weak, non-significant association with test accuracy (r = 0.26, p = 0.53). Conclusions: Larger EfficientNet variants did not consistently improve SD-OCT classification. B1 achieved the highest accuracy and Drusen F1, whereas B7 showed a secondary accuracy recovery at greater model size and CPU latency, indicating task and protocol dependent scaling effects. As cross-partition duplicates have not been independently audited, results are conditional on the supplied split.

---


### 173. [CoDecide: Content-Adaptive Video Decoding for High-Throughput Video Analytics](https://arxiv.org/abs/2611.06455)

**<font color=#1a73e8>作者：</font>** Shristy Shah, Thomas B. Moeslund, Kamal Nasrollahi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analytics on video archives are bottlenecked by decoding. In a dense pipeline that runs a detector on every frame, decoding is a small fraction of the runtime, but once the detector is restricted to selected frames, decoding takes over as the main cost. We introduce CoDecide, a retrospective analytics system that only decodes the frames where new content appears, using signals from the compressed bitstream to find them. Motion tells us something is moving, but not whether it is new to the scene or has been there the whole time. To make that distinction, we supervise a lightweight compressed-domain student on a label-free novelty signal from a frozen DINOv2 teacher, which fires on semantically new regions rather than on any motion. Consequently, the student model generalizes to new camera deployments without requiring per-camera retraining. At inference, it decides which frames to decode and which regions to reconstruct. Detections from the decoded frames are propagated to the skipped frames using motion vectors. We evaluate CoDecide with a leave-one-dataset-out protocol on VIRAT, MEVA, and ShanghaiTech. Against a dense per-frame detector, CoDecide recovers more moving-object detections than prior compressed-domain selectors at an equivalent decoding budget, outperforming even a competitor trained directly on the target camera. CoDecide runs 15 to 24x faster than a pipeline that decodes and detects every frame. Code is available at this https URL.

---


### 174. [Model Merging Does Not Require Uniform LoRA Ranks](https://arxiv.org/abs/2611.06486)

**<font color=#1a73e8>作者：</font>** Zirong Xie, Zainab Afolabi, Nikita Kozodoi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines separately fine-tuned experts into a single model without retraining. Standard practice trains every expert at the same LoRA rank, which couples the rank choice across experts even though each domain has its own best rank. We show this coupling is a property of the merge method, not of merging. We train 36 experts on three domains (mathematics, instruction following, multilingual) at four ranks and three model scales, then merge with six methods at uniform ranks and at each domain's own best rank. Giving experts different ranks costs averaging and utility-based selection nothing, and gains them up to 1.8 pp of multi-domain accuracy, while the conflict-resolution methods are inconsistent and can lose up to 4 pp. The split has a simple cause. Merging keeps only a fixed share of the pooled spectral components, and methods that choose them by size discard many that would have reduced loss. They also tend to discard the same expert: the instruction adapter has the smallest singular values, so it is dropped almost entirely and IFEval falls by 16 to 25 pp. Choosing components by their effect on loss instead keeps all three experts, and leaves accuracy nearly flat across an 8$\times$ rank range (0.7 pp, against 6.7 pp for TIES at 4B scale). Rank can therefore be chosen per expert whenever the merge operator does not select by magnitude.

---


### 175. [Measuring the collaboration, not the agent](https://arxiv.org/abs/2611.06487)

**<font color=#1a73e8>作者：</font>** Xinxiao Li, Eisei Nakahara  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Benchmarks for visualization agents score the agent alone; the human only supplies reference answers. For high-dimensional data this misses what matters: the knowledge of which variables count is held by on-site experts, not by the model, so the useful question is how well an analyst and an agent do together. We study one specific form of collaboration, the agent proposes a view, the analyst accepts, rejects, or modifies it, and those judgments are kept for later sessions, and propose five measures for it: complementarity, intervention efficiency, appropriate reliance, knowledge retention, and agency. The first four are computed from interaction logs alone. We test the measures, not people: in a testbed for parallel-coordinates design on public manufacturing data (UCI SECOM), with a simulated analyst whose behavior we control, all four are computable and respond to the controlled differences. Whether they reveal anything about real analysts is the next step; we release the testbed for it.

---


### 176. [FPTR: Feasibility-Preserving Transactional Refinement for Deadline-Constrained Joint Beam and Resource Allocation](https://arxiv.org/abs/2611.06491)

**<font color=#1a73e8>作者：</font>** Minghao Kong, Zirong Liu, Jianhao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Short-interval wireless schedulers must return a complete, feasible beam-and-resource allocation before each execution deadline, and a late or invalid output gives no utility in the current control cycle. Searching longer can increase transmitted traffic, but it may also miss the deadline or leave only an infeasible intermediate solution. We propose Feasibility-Preserving Transactional Refinement (FPTR), which always keeps a validated feasible allocation, the incumbent. Each refinement stage builds a separate candidate and leaves the incumbent unchanged. A candidate replaces the incumbent only if it is complete, passes the feasibility validator before its stage cutoff, and strictly improves the objective; otherwise it is discarded. Four refinement stages use this rule: buffer-aware resource selection, compatibility-group (CG) user sharing, beam-mask rebuilding from remaining demand, and joint reassignment of two resources. On 150 fixed synthetic instances, the full pipeline (Full) raises traffic by 3.83% on average over a lightweight beam-first reference and by 1.79% over its Base constructor. In a separate suite with matched inputs, Full exceeds six independent search baselines (ALNS, tabu search, GA, simulated annealing, iterated local search, and GRASP) by 6.68-8.35%, where outputs later than 100 ms receive zero utility. All 750 Full runs in the internal suite returned feasible allocations, and none exceeded 100 ms. Separating mandatory output construction from optional refinement lets spare computation time improve the allocation without endangering the incumbent. The open-source implementation supports independent reproduction.

---


### 177. [NaijaFacts: A Framework for Disentangling Language from Knowledge in Facts about Nigeria](https://arxiv.org/abs/2611.06504)

**<font color=#1a73e8>作者：</font>** Zainab Afolabi, Nikita Kozodoi, Jack Butler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual benchmarks for African languages mostly translate generic questions into local languages, measuring linguistic competence but not whether models know facts about Africa. We introduce \naija, a benchmark of factual and statistical questions about Nigeria, authored by native speakers and grounded in authoritative official statistics, with every question available in English, Nigerian Pidgin, \yoruba, Igbo, and Hausa. Answering similar questions for the UK and US yields a country by language matrix that disentangles a language effect (the model knows the fact but degrades in a low-resource language) from a knowledge effect (the fact is absent in every language). Across eight frontier and Nigeria-adapted models, the knowledge effect dominates: English-query accuracy is 49--50\% for the US/UK but 20\% for Nigeria. The language effect is smaller and tracks web representation, degrading from English to \yoruba{} (9 points on Nigeria, up to 24 on US/UK questions). We find scale does not help: the strongest models reach 66--79\% on the UK and the US but none exceed 31\% on Nigerian statistics. Extending to all 54 African countries with our best performing frontier model shows the same profile continent-wide, 96\% on culture and 98\% on politics against 26\% on statistics, so the gap is not specific to Nigeria.

---


### 178. [ElecLoad: Adaptive Electricity Load Forecasting Guided by Multiple Events](https://arxiv.org/abs/2611.06508)

**<font color=#1a73e8>作者：</font>** Huajian Zhang, Mingyue Cheng, Xingpeng Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate electricity load forecasting provides critical decision support for energy procurement, generation scheduling, and supply-demand balancing, contributing to the economic efficiency and operational reliability of power systems. However, future electricity demand can be affected by the complex interplay of multiple events described in Web notices, weather alerts, and event schedules. Their effects vary over time and can reinforce or offset one another, making electricity load difficult to forecast accurately. While existing methods can incorporate context as additional input, how to use the effects of multiple events and their interactions to guide the load forecasting process itself remains to be explored. To address this gap, we propose ElecLoad, a context-aware agent for multi-event electricity load forecasting that adaptively organizes the forecasting process. Specifically, we train ElecLoad to combine historical load with context to analyze each event's relevance to the target load, the timing of its effects, and potential interactions among events. Guided by this analysis, ElecLoad adaptively chooses to forecast the entire forecast horizon directly or to partition it into segments according to changes in event effects. When the horizon is partitioned, sub-agents independently generate initial forecasts for each segment. The main agent then reviews these forecasts, and the sub-agents perform selective refinement guided by its feedback. Experiments on multiple electricity load datasets show that ElecLoad achieves state-of-the-art performance in most evaluation scenarios. Code is available at this https URL.

---


### 179. [Nowcasting Future Performance for Population Pruning in Survival-of-the-Fittest Training](https://arxiv.org/abs/2611.06512)

**<font color=#1a73e8>作者：</font>** Rico Städeli, Léo Meynent, Boris Knyazev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training high-performing neural networks often involves evaluating populations of candidate models with varying hyperparameters, architectures, or random seeds. Training every candidate to completion is computationally expensive, yet stopping seemingly weaker runs early risks discarding models that would ultimately perform better, as learning curves can cross. To address this challenge, we investigate whether intermediate training checkpoints can predict future model accuracy and enable more informed pruning decisions. Our nowcasters predict test accuracy five epochs ahead or at the end of training. They are trained with accuracy and loss histories, weight statistics, and SANE representations as inputs. SANE is a transformer autoencoder that encodes a checkpoint as a sequence of latent tokens. We then use the nowcasters in Survival-of-the-Fittest (SOTF) training. SOTF repeatedly ranks runs during training by predicted accuracy and stops the lowest-ranked ones. Our results show that weight statistics work best for five-epoch forecasts, and SANE representations work best for final accuracy prediction. For evaluation, we compare SOTF with pruning the population by current accuracy. In homogeneous model zoos such as the CNN zoos, pruning by current accuracy already retains a final model only slightly worse than the best. Model zoos with a larger spread in performance, such as the ResNet-18 and ViT zoos, are more difficult to prune by current accuracy alone. In these zoos, SOTF with nowcasted final accuracy almost closes the gap to the best model.

---


### 180. [An Interaction-Aware Decision Framework for FDIC-Assisted Distressed Bank Acquisitions: Empirical Evidence from the FDIC Failed-Bank Panel and the SVB-First Citizens Case](https://arxiv.org/abs/2611.06514)

**<font color=#1a73e8>作者：</font>** Yousef Nejatbakhsh, Malihe Aliasgari, Parsa Safaee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acquirers of failed banks weigh acquisition value, regulatory protection, risk, buyer strength, and execution difficulty jointly, because each signal's meaning depends on the others: high non-performing loans matter less when government loss sharing absorbs the losses. The proposed Spider Network Filtering Framework encodes such dependencies as four interpretable interaction rules among five dimensions, yielding graph-inspired features for a logistic model and a Pursue/Caution/Avoid decision rule. We evaluate it on 55 acquisitions assisted by the Federal Deposit Insurance Corporation in 2008-2024 by acquirers with a parent listed in the United States. Six financial inputs come from regulatory reports published before each failure; two deal terms, which the winning bidder knows when it bids but investors learn at the announcement, come from the regulator's press releases. The outcome, a positive three-day abnormal return around the announcement, records the market's initial reception, not realized success. Under grouped, nested cross-validation, the Spider-enhanced model reaches a mean area under the receiver operating characteristic curve of 0.594, against 0.615 for logistic regression on the same inputs and 0.632 for ridge regression; permutation tests that repeat the full model selection give at most weak evidence that any of them ranks better than chance. The Spider score used directly does not rank better than chance, and an apparent link between target distress and higher returns disappears against a bank-sector benchmark. Thresholds tuned for the F1 score approve most acquisitions with negative returns and realize negative utility when each costs three times what a positively received acquisition gains.

---


### 181. [Dialect Matters: A Dialect-Aware Baseline for Igala-English Machine Translation](https://arxiv.org/abs/2611.06517)

**<font color=#1a73e8>作者：</font>** Etuh E., Eli. A. Jiya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The massive permeability of intelligent systems in every sphere of human activities have greatly enhanced clarity, ease of work, and increased general global understanding which has significantly awaken the use of intelligent systems by all users. Intelligent systems greatly rely on precise dataset/corpus for the correctness of their output. Despite efforts by researchers to address Low-resource language in the Natural Language Processing (NLP), Igala still has zero parallel corpora despite efforts by researchers. We present a dialect-aware baseline for Igala-English machine translation, among first open systems and first with dialectal variation analysis. Our dataset of 1137 sentences (899 training) is first with dialect tags: Idah 459 (40.4%), Ankpa 297 (26.1%), Ibaji 160 (14.1%), Other 187 (16.4%), Ogugu 32 (2.8%). Same English yields 20-60 Igala forms. Mixed-dialect training achieves balanced BLEU 11.66 versus Idah-only model which drops 4.7 BLEU on Ibaji (13.2 on Idah, 8.5 on Ibaji), proving dialect fairness requires mixing. Fine-tuned from Helsinki-NLP/opus-mt-en-mul (78M), epoch ablation shows convergence at 8 epochs and overfitting at 15. BLEU 11.66, chrF 46.69. Analysis shows 899 sentences on log-linear trend consistent with African low-resource literature. This work provides first dialectal impact analysis for Igala and establishes baseline for future work.

---


### 182. [IDSISA: Influence-Distilled Sharded Training for Efficient Machine Unlearning](https://arxiv.org/abs/2611.06519)

**<font color=#1a73e8>作者：</font>** Deeraj SK, Sadhana Devarajan, Tanmoy Hazra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning removes the influence of specific training examples to comply with privacy regulations. Full retraining gives strong guarantees but is computationally prohibitive at scale; approximate methods are efficient but lack formal guarantees. SISA (Sharded, Isolated, Sliced, and Aggregated training) achieves certified deletion through data sharding and independent retraining, but random partitioning scatters forget requests across most shards, and isolated retraining degrades utility. We introduce IDSISA (Influence-Distilled SISA), which uses influence functions to concentrate forget-prone samples into few shards and distillation from unaffected shards to recover utility lost to isolation. The deletion guarantee inherited from SISA's retraining step remains exact and requires no probabilistic qualification; the distillation-based utility recovery is a separately quantified, empirically bounded approximation ($\epsilon_{\text{cert}} \leq 0.015$ in expectation). We further formalize certification under sequences of repeated deletion requests, where cross-shard distillation can create dependencies between shards; we prove that a closure-based cascading retraining procedure restores the deletion guarantee to the full aggregated model under any deletion sequence. Experiments on ResNet-18/CIFAR-10, ResNet-18/CIFAR-100, BiLSTM/IMDB, TCN/IMDB, and a fully connected network on Fashion-MNIST show $14-91\%$ better selective forgetting, up to $50\%$ better utility retention in relative terms (with consistent percentage-point gains on the other architectures, where a relative baseline is undefined), and unlearning-time changes ranging from $-6.7\%$ to $+6.4\%$ depending on architecture, relative to SISA.

---


### 183. [Spatially and Compositionally Controlled Multimodal Glioblastoma MRI Synthesis with Latent Diffusion](https://arxiv.org/abs/2611.06540)

**<font color=#1a73e8>作者：</font>** Steven Glass, Max Van Puyvelde, Marija Pizurica 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glioblastoma exhibits substantial heterogeneity in tumour morphology and composition across MRI modalities, often making available clinical datasets highly unbalanced in terms of patient pathologies. We propose a two-stage latent diffusion model (LDM) framework for the generation of explicitly controllable 2D glioblastoma MRI scans. First, a segmentation LDM generates tumour maps conditioned on location, spatial extent, axial position, and subregion composition. Second, a modality-conditioned LDM with ControlNet generates T1, T1Gd, T2, and FLAIR images adhering to the requested segmentation. On a held-out test set, generated segmentations achieved a mean centroid error of 0.842 pixels and a subregion proportion error of 0.795 percentage points. ControlNet improved Fréchet inception distance (FID) across all four modalities, reducing pooled FID from 42.59 to 36.12. An expert reader study yielded mean quality ratings of 6.60 for real images, 6.83 for ControlNet-generated images, and 6.77 for fully synthetic images.

---


### 184. [LungMend: A Healthy-Only Latent Diffusion Shape Prior for Lung Mask Correction in Severe Tuberculosis CT](https://arxiv.org/abs/2611.06556)

**<font color=#1a73e8>作者：</font>** Rezkellah Noureddine Khiat, Pierre-Yves Brillet, Catalin Fetita  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung segmentation models such as R231 are widely used, but they fail on severe tuberculosis (TB) CT: cavities and consolidations look like non-lung tissue and are left out of the mask. We present LungMend, a post-processing model that corrects such masks using only healthy anatomy. A latent diffusion model, trained on healthy lungs with synthetically corrupted masks, learns to recover the complete lung from the faulty mask and the bone anatomy, without any pathological data or CT intensities. LungMend recovers cavities and consolidations that R231 misses and improves accuracy on expert-annotated slices. Code: this https URL

---


### 185. [From Fixed Defaults to Calibrated Activation Policies for Long-Term Time-Series Forecasting](https://arxiv.org/abs/2611.06559)

**<font color=#1a73e8>作者：</font>** Shijie Xu, Boyan Tang, Jianghua Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time-series forecasting supports decisions in energy, transportation, and other applications where reliable predictions are needed beyond the observed data. Although forecasting research has advanced model architectures, fixed activation configurations provide limited guidance on how activation choices should vary across datasets and prediction horizons. This study aims to establish when task-specific activation choices improve forecasting accuracy and how previous experiments can guide the selection of suitable configurations for new tasks. We develop a calibrated selection policy that learns a reliable default from prior experiments, adapts the activation function and its location to each task, and retains the default when evidence for a change is insufficient. In an evaluation supported by 1,225 Informer training runs across 17 dataset variants and 51 forecasting tasks, the policy reduces mean squared error by 7.86% on average relative to the conventional fixed-activation baseline and improves 72.55% of tasks. These findings establish activation choice and placement as practical opportunities for improving existing forecasting models and show how accumulated experimental evidence can guide configuration decisions without repeating an exhaustive search for every task.

---


### 186. [Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains](https://arxiv.org/abs/2611.06585)

**<font color=#1a73e8>作者：</font>** Yichiet Aun, Mohammed A. Alhartomi, Jing Jie Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents rely on third-party tools, such as Model Context Protocol (MCP) servers, whose publishers can be authenticated and whose execution can be restricted by runtime security policies. Yet authenticity does not guarantee benign behaviour: a legitimately signed tool may perform its advertised function while concealing malicious code that leaks confidential information. We demonstrate this trust failure with a signed MCP tool that embeds sensitive data in requests to a policy-allowed destination. Meta's MCPGuard-Dynamic, a state-of-the-art runtime defence, blocks a direct exfiltration attempt in the same run, yet fails to prevent this attack in every trial. We introduce germline execution, which limits information disclosure without inspecting or trusting tool implementations. Each tool invocation runs in ephemeral copies forked from a data-free germline process, each receiving only information authorised for its destination. Even if malicious code executes, what it can disclose is bounded by the data available to its copy. Under explicit assumptions on copy confinement and a data-free germline, we prove sink noninterference for every signed release and, for releases deterministic within our replay model, show that a verified witness establishes a flow violation. Across 153 attack runs, no unauthorised disclosure was detected under germline execution, compared with 5.9-74.5% of runs under baseline defences and an ablation. Invocations served by a single copy completed in 10-49 ms, 2-28x faster than restarting the tool for every invocation, the conventional way to clear state. These results show that data-isolated execution protects agent toolchains against malicious code concealed within authenticated software.

---


### 187. [Thermodynamics-Informed Learning Captures Hierarchical Hydrogen-Bond Networks in Deep Eutectic Solvents](https://arxiv.org/abs/2611.06590)

**<font color=#1a73e8>作者：</font>** Yanpeng Ye, Chaoran Duan, Mian Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep eutectic solvents (DESs) offer a tunable platform for lignocellulose refining, but their solvation behavior depends on multicomponent hydrogen-bond networks rather than individual constituent properties. We develop TiNN, a thermodynamics-informed neural network that hierarchically represents HBA-HBD association and solute accommodation through a learned free-energy pathway. Trained on 938 records, TiNN achieves a test-set $R^2$ of 0.917 and generalizes to new HBA-HBD combinations and sparse conditions. Ablation identifies solute-specific stabilization as the largest contributor to prediction accuracy, while the importance of hydrogen-bond compatibility depends on the dissolution mechanism. Experimental measurements of glucose, xylan, and Kraft lignin in acidic, basic, and neutral DESs show that TiNN reduces the geometric mean solubility error from more than 23-fold with COSMO-RS to approximately 1.5-fold. Without training on fractionation data, TiNN also distinguishes DES formulations with high and low lignin and hemicellulose removal from corn stover. These results support chemically grounded solvent screening for lignocellulose fractionation.

---


### 188. [BudgetSplat: Budget-Controllable Generalizable Gaussian Splatting](https://arxiv.org/abs/2611.06593)

**<font color=#1a73e8>作者：</font>** Yuxi Hu, Jun Zhang, Wei Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting enables efficient generalizable novel view synthesis, but existing pixel-aligned methods often generate highly redundant Gaussian primitives, causing the final representation size and rendering cost to grow rapidly with image resolution and the number of input views. We propose BudgetSplat, a budget-controllable feed-forward framework that adapts the final Gaussian representation to a user-specified preservation ratio. Rather than treating compaction as simple importance ranking, we formulate it as a joint problem of importance estimation, spatial coverage, and cross-view redundancy. A single trained model supports varying numbers of context views and multiple test-time budgets without per-budget retraining or per-scene compression. To realize this formulation, Intra-Cross Mask Supervision provides structure-, coverage-, and redundancy-aware guidance for learning Gaussian importance, while budget-conditioned feature modulation adapts Gaussian opacity and attributes to the requested preservation ratio. Coverage-Aware Budget Selection further combines patch-wise pre-selection, view-wise opacity ranking, and 3D redundancy suppression to construct compact yet spatially distributed Gaussian representations. Experiments on indoor reconstruction and cross-dataset generalization demonstrate consistent quality--size trade-offs across different input view counts and preservation ratios, substantially reducing final representation storage and rendering cost while preserving rendering quality.

---


### 189. [SpikePose: Lightweight Video Human Pose Estimation](https://arxiv.org/abs/2611.06594)

**<font color=#1a73e8>作者：</font>** Yunhao Huang, Kaushik Bhargav Sivangi, Tianyi Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient video human pose estimation must balance localisation accuracy, motion quality, and energy cost. We present SpikePose, a lightweight video pose estimator that pairs a frame-reset, single-step spiking encoder with motion-aligned heatmap memory (MAM). The encoder supplies per-frame spatial evidence, while MAM estimates joint displacement, aligns historical heatmaps, and adaptively fuses them with current predictions. By confining temporal reasoning to a compact, lightweight module outside the spiking backbone, SpikePose helps bridge the gap between spiking and classical Artificial Neural Networks (ANN) on large-scale, non-event-driven video tasks. We evaluate spatial accuracy, motion errors, and estimated arithmetic energy on MPII and a fixed NTU60 Cross-Subject subset. Against the architecture-matched ANN with MAM, SpikePose cuts estimated arithmetic energy by 91.4% at a cost of just 1.12 points in head-bone-normalised PCK at 0.5 threshold (PCK_HB(0.5)). Within SpikePose, adding MAM reduces velocity and acceleration errors by 28.13% and 31.46% while slightly improving localisation, at a cost of only 0.003M parameters and 0.0023 analytical GFLOPs per frame. Code will be released on GitHub upon acceptance.

---


### 190. [A trust layer for fast pedestal-stability surrogates: calibrated error bars, out-of-distribution alarms and few-shot recalibration](https://arxiv.org/abs/2611.06597)

**<font color=#1a73e8>作者：</font>** Amin Vakhshouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning surrogates of linear peeling-ballooning stability now run in milliseconds, but they are mostly deployed as point estimators: they do not say how wrong they may be, or when a query lies outside what they were trained on. For a fusion company designing a new device, every equilibrium of interest is outside the training data of existing surrogates, so this is the case that matters. We describe a model-agnostic trust layer for stability surrogates, made of conformal error bars, out-of-distribution alarms that route doubtful cases to the physics code, and recalibration from a few simulations of a new design, and we test it with pre-registered hypotheses. On a large public dataset of JET-like equilibria with ideal-MHD growth rates, the error bars hold their nominal coverage in distribution and fall short under a shift in plasma shape; a few dozen simulations of the new shape, or routing the cases the alarms flag, restore it. On resistive BOUT++ surrogates, the bars stay calibrated on held-out runs, the alarm flags tokamaks absent from training, and a scenario scan is screened in seconds instead of hours. Across equilibria from the SPARC library and the DIII-D coil set, a surrogate trained on our own graded BOUT++ labels beats the baseline on unseen equilibria, while a surrogate trained elsewhere ranks the same cases backwards and its alarm declines them. Building our own neural-operator surrogate, the harness exposed two input defects whose fix closed its gap to a simple network. For every surrogate tested, the trust layer keeps coverage near target, with a bar width set by that surrogate's own error. Not every pre-registered hypothesis held, and we report those results and the limits of all of them.

---


### 191. [Alternatives to Shallow Autoencoders for Collaborative Filtering](https://arxiv.org/abs/2611.06610)

**<font color=#1a73e8>作者：</font>** Mario Mallea, Angela Nebot, Francisco Mugica  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative filtering (CF) is a cornerstone of recommender systems and plays a relevant role in many modern applications. CF uses user-item interaction data to discover future preferences. Although deep learning models have shown promise in CF, Embarrassingly Shallow Autoencoders for Sparse Data (EASE) has gained attention for its outstanding ranking accuracy provided by its closed-form solution. EASE relies primarily on relationships among items to fit a full-rank high-dimensional linear mapping. We hypothesize that this design limits its capacity to capture similar but not equivalent fine-grained user relationships, consequently limiting its recommendation accuracy. This paper introduces an alternative formulation based on EASE that takes advantage of user-user information. Furthermore, we propose a hybrid model that combines both user-user and item-item adjacency distributions.
Our experiments reveal that the proposed models outperform EASE on well-known recommendation benchmarks, highlighting the significance of including the user alternative in shallow autoencoder studies for CF.

---


### 192. [From Reconstruction to Imputation: Test-Time Optimization for Missing Time-Series Channels](https://arxiv.org/abs/2611.06612)

**<font color=#1a73e8>作者：</font>** Björn Ludwig, Alexander Windmann, René Heesch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complete sensor-channel failures create a difficult form of time-series missingness: local interpolation is unavailable, and deploying a separately trained imputer for every failure pattern may be impractical. We ask whether a sequence reconstructor trained without artificial mask augmentation and then frozen can be converted into an imputer at inference time. Our method treats the missing entries of each test window as optimization variables, clamps all observations, and backpropagates through the frozen model to minimize reconstruction error only on observed coordinates. The resulting observed-self-consistency objective requires neither artificial mask augmentation nor full-channel dropout during reconstructor training. We characterize when this refinement is informative through the cross-Jacobian from missing inputs to observed residuals, and use an optional temporal-smoothness prior when that coupling is weak. Across five real-world datasets with exactly one channel synthetically masked per test window and four reconstruction architectures, no-prior test-time refinement reduces MAE relative to one-pass reconstruction in 19 of 20 dataset-backbone combinations. Compared with mask-aware imputers trained under either standard structured masks or matched full-channel dropout, the best refined reconstructor achieves the lowest MAE on two datasets and trails the strongest baseline on three. These gains require substantially more inference time and are sensitive to cross-channel coupling. Our results establish test-time self-consistency as a conditional inference-time adapter for frozen reconstruction models that complements mask-aware imputation without retraining the reconstructor.

---


### 193. [Dimension-Free Private Mean Estimation is Impossible Without the Covariance](https://arxiv.org/abs/2611.06615)

**<font color=#1a73e8>作者：</font>** Renaud Gaucher, Ephraim Linder, Adam Smith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the limits of differentially private Gaussian mean estimation when the covariance matrix is unknown. Prior work shows that when the covariance $\Sigma$ is known, the optimal sample complexity can depend only on its spectrum, rather than on the ambient dimension $d$. We establish new lower bounds for Gaussian mean estimation with Euclidean error which show that private estimators cannot achieve similar guarantees when the covariance is unknown. First, when the sample size $n$ is smaller than the effective dimension $\mathrm{trace}(\Sigma)/\|\Sigma\|_{\text{op}}$, the optimal error when the covariance is unknown can be larger than the optimal error when it is known by a factor of $\sqrt{d/n}$. Second, when the sample size is larger than the effective dimension, even for diagonal covariance matrices with effective dimension bounded by $\log d$, the optimal error when the covariance is unknown can be larger than the optimal error when it is known by a factor of $\sqrt{d}/n^{3/2}$. Together, these results show that in the unknown covariance setting, exploiting anisotropic structure under differential privacy can require a dimension-dependent error or sample complexity.

---


### 194. [Learning to Track Cells from Sparse Annotations in 3D Time-Lapse Microscopy](https://arxiv.org/abs/2611.06624)

**<font color=#1a73e8>作者：</font>** Yusuke Uchida  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing cell lineages from 3D time-lapse microscopy requires distinguishing cell motion from division and inferring temporally consistent connections. When only a subset of cells is annotated, however, training procedures that treat unannotated regions as background or incorrect correspondences can be problematic. We propose a cell tracking pipeline that integrates detection from sparse annotations, calibration of candidate connections using image features, and joint selection of lineage graph events. For detection, we combine the outputs of 2.5D and 3D models trained to suppress erroneous background supervision at unannotated cells. We then calibrate ordinary link and division probabilities using motion features from dense flow, correspondence features from a learned cell-matching model, and features from models that identify cells immediately before division, dividing parents, and daughters immediately after division. Ordinary links, divisions represented as daughter pairs, and node inclusion are selected jointly under a surrogate objective derived from the evaluation metric, followed by gap filling and temporal coordinate refinement. The pipeline achieves an overall score of 0.9762 in 5-fold cross-validation on 199 videos from 2 zebrafish embryos. With candidates and calibrated values held fixed, joint selection outperforms a sequential method that allows replacement of existing divisions and reoptimization of ordinary links by 0.0105. The improvement arises primarily from division recovery.

---


### 195. [Interactive World Simulation with Cosmos for Physical AI](https://arxiv.org/abs/2611.06627)

**<font color=#1a73e8>作者：</font>** NVIDIA, Anis Ahmad, Jon Allen 等 89 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a shared framework that adapts Cosmos world foundation models for real-time interactive world simulation in Physical AI. By streaming visual observations in response to actions and scene controls, the framework enables users and embodied agents to interact with evolving virtual environments. It supports both predicting the visual consequences of actions and generating observations from physical state maintained by an external simulator. We demonstrate this approach across camera navigation and robot manipulation, controllable video transfer, and multi-view autonomous vehicle (AV) simulation. These examples provide a shared foundation for developing interactive virtual environments for Physical AI training and evaluation. Our code and model checkpoints are available at this https URL and this https URL. The project website is available at this https URL.

---


### 196. [From Certified Pairs to a Certified Hub: Reasoner-Checked Crosswalks for the Information Exchange Standard](https://arxiv.org/abs/2611.06628)

**<font color=#1a73e8>作者：</font>** Fabio Rovai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A national digital twin was conceived as an ecosystem of twins connected through mappings to a common foundation, but the roadmap that promises to confirm those mappings are valid never says what valid means. We give the test a precise form, coherence and conservativity of the merged ontology, borrowed from logic-based alignment repair, and apply it to the Information Exchange Standard (IES), first pair by pair and then to whole hubs. Crosswalks from IES into thirteen ontologies across seven sector groups, anchored on the building ontologies BOT, Brick, and SAREF4BLDG, pass through separate stages of matching, human review, certification of each SKOS correspondence against the two class hierarchies, and reasoning with HermiT. Pair by pair, the stages catch different failures: certification alone removed all 526 conservativity violations of the raw crosswalks, review alone left 73, and together they made eleven of twelve overlapping pairs coherent and conservative. Pairwise certification does not compose. Merging the three certified building crosswalks into one hub made five Brick classes unsatisfiable, through a homonym between the IES and Brick notions of a floor that only BOT's disjointness axioms expose; rejecting that one row gave a coherent and conservative hub that entails 290 cross-ontology links nobody wrote down. The core hub is inconsistent before any crosswalk is added, because two published standards, the Open Energy Ontology and BFO 2020, contradict each other; with either one left out it is coherent and conservative. A hub, not a pair, is the unit an ecosystem of twins has to certify.

---


### 197. [Trick-or-Treat: Adversarial Evaluation of Multimodal Medical Reasoning with Synthetic Images](https://arxiv.org/abs/2611.06631)

**<font color=#1a73e8>作者：</font>** Oishi Banerjee, Eujin Lee, Sung Eun Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We used medical image synthesis to create a challenging multimodal evaluation framework that exposes hallucination behaviors in frontier models. Evaluating multimodal reasoning has historically been difficult because existing medical datasets rarely pair different image modalities, such as radiographs and external clinical photographs. To address this gap, we introduce Trick-or-Treat, an adversarial multimodal medical benchmark that pairs real chest radiographs with synthetic clinical photographs to challenge models' cross-modal reasoning. For each of a wide range of conditions, we created two pairs of images, where the pairs share a single chest radiograph but contain different external photographs. In matched pairs, the chest radiograph and photograph both contain findings suggesting the same disease (e.g., varicella pneumonia suggested by lung opacities and crusted skin lesions seen in chickenpox). In mismatched pairs, the photograph depicts an alternative clinical finding that would not lead to the same unifying diagnosis (e.g. replacing crusted skin lesions with ordinary acne). Synthetic photograph generation allows clinical findings to be varied while the person's features and photographic setting stay consistent, reducing confounding. In an investigation of three frontier models, we found that models hallucinated clinically significant photograph findings in 45-57.5% of mismatched pairs, up from 25-37.5% for the same photographs shown alone. When faced with mismatched pairs, models tended to ignore mismatches and instead hallucinated findings that better matched the radiograph (e.g. misreading acne as crusted skin lesions to justify diagnosing chickenpox). Trick-or-Treat both demonstrates concerning error pattern in frontier models' medical reasoning and provides a proof of concept for the use of synthetic images in adversarial multimodal evaluation.

---


### 198. [Uncertainty-Driven Efficient Communication for UAV-Based Collaborative Perception](https://arxiv.org/abs/2611.06635)

**<font color=#1a73e8>作者：</font>** Jiuwu Hao, Yuting Wan, Liguo Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV)-based collaborative perception enables multiple agents to share complementary perceptual information, overcoming limitations such as occlusion and limited sensing range. Communication efficiency is a critical bottleneck, as UAVs operate under stringent bandwidth and computational constraints. However, existing spatial selection methods focus predominantly on foreground regions to reduce missed detections, neglecting perceptually ambiguous regions and leaving false detections unresolved. We propose UCP, an uncertainty-driven framework that characterizes collaborative value through observational uncertainty, identifying sensor-limited regions, and discriminative uncertainty, capturing model-level ambiguity near the decision boundary. These estimates drive spatial request and supply maps for efficient inter-agent communication, and the received messages are aggregated via U-Fusion, an uncertainty-guided cross-attention module. Experiments on three benchmarks across 3D object detection and trajectory prediction demonstrate a superior performance-bandwidth trade-off with high interpretability and strong generalizability.

---


### 199. [Human Motion Prediction via Continual Prior Compensation](https://arxiv.org/abs/2611.06637)

**<font color=#1a73e8>作者：</font>** Jianwei Tang, Jian-Fang Hu, Tianming Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human Motion Prediction (HMP) aims to predict future human poses at different moments according to observed past motion sequences. Previous approaches mainly treated the prediction of different temporal moments as a single prediction task and learned the predictions of varied moments simultaneously, which would encounter a main limitation: the learning of short-term predictions (referring to ``near-future'' prediction) could be hindered by the predictions of long-term (referring to ``far-future'' prediction) motions. In this paper, we develop a novel temporal continual learning framework called Continual Prior Compensation (CPC) to progressively train HMP models, in which we divide the prediction task of motions corresponding to varied temporal moments into several subtasks and train the model in a multi-stage manner. To mitigate the prior information forgetting in the progressive training, we further introduce a learnable random variable Prior Compensation Factor (PCF) to explicitly measure the prior knowledge loss. We theoretically show that the PCF can be efficiently learned together with the model parameters by minimizing a reasonable upper bound of the objective function. The proposed CPC is further enhanced to estimate the prior information loss for each subtask and a new framework called Continual Prior Compensation++ (CPC++) with Fine-Grained Prior Compensation Factor (FGPCF) is finally developed. Our CPC and CPC++ frameworks are quite flexible and can be easily integrated with different HMP backbone models and adapted to various datasets and applications. Extensive experiments on three HMP benchmark datasets using multiple SOTA HMP backbones (PGBIG, siMLPe, MotionMixer, and LTD) demonstrate the effectiveness and flexibility of our frameworks.

---


### 200. [Dynamical State-Space Diffusion for Spatiotemporal Prediction](https://arxiv.org/abs/2611.06652)

**<font color=#1a73e8>作者：</font>** Woojun Lee, Hankyeol Kim, Pilsung Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models for temporal prediction typically corrupt each future frame with independent noise, leaving temporal dependence entirely to the denoiser. We propose Dynamical State-Space Diffusion (DSSD), which learns the temporal structure of the corruption process itself. DSSD builds a temporal kernel from the damped oscillatory modes of a stable diagonal state-space model, whose learned decay rates and frequencies let the corruption capture multiple timescales and oscillatory correlations, while the denoiser architecture remains unchanged. Running this model on a finite clip, however, requires the state before the first frame, which is unobserved; starting from a zero state leaves the early frames with less noise than the diffusion schedule prescribes. We avoid this by using the Cholesky factor of the model's stationary covariance as the temporal operator. We prove that this operator is causal, exactly invertible, keeps each frame's noise variance equal to that of standard diffusion, and reduces to the identity at the clean end of the process, and that it is exactly the Kalman innovations form of the state-space model. The denoiser is trained to predict the temporally correlated noise, and sampling removes and reapplies the temporal mixing at each step. On scientific-field and robot-video datasets, DSSD outperforms diffusion baselines that share its denoiser, and the evolution of its learned modes during training shows that the temporal operator adapts to each dataset.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
