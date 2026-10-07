# 📦 其他研究 | 2026年10月08日

> 本类共 **335** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-335](./part-07.md)

---

### 151. [Towards the Automatic Synthesis of Interpretable Chess Tactics](https://arxiv.org/abs/2610.07640)

**<font color=#1a73e8>作者：</font>** Abhijeet Krishnan, Chris Martens  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> State-of-the-art reinforcement learning agents are capable of outperforming human experts at games like chess, Go and StarCraft II. These agents do not simply take advantage of their digital hardware in being able to react and calculate faster than humans, but employ better strategies that lead to more victories. Interpreting these strategies would give human players valuable insight into how to improve their play. In this preliminary work, we propose a symbolic sub-policy model for playing chess. Inspired by chess tactics, our model attempts to incorporate domain knowledge to improve interpretability. We adapt patterns learned by an inductive logic programming system called PAL to derive our model. We contribute a divergence metric to evaluate our model against a random baseline, and find a set of tactics that is able to suggest moves of similar playing strength to a human beginner. Finally, we propose a computational evaluation scheme for the model by augmenting an off-the-shelf engine with it.

---


### 152. [Joint Workflow and Prompt Optimization for User Behavior Simulation](https://arxiv.org/abs/2610.07663)

**<font color=#1a73e8>作者：</font>** Nipun B Nair, Tongtong Wu, Hongzhi Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> User behavior simulation is the computational modeling of user interactions within information systems through the use of simulated agents in place of live users. It supports system testing and evaluation, decision-making and forecasting, and user experience design. Existing simulators rely on hand-crafted rules or domain expertise that transfers poorly across tasks. SWORD (Simulation-driven Workflow and Prompt Optimization with Role-based Design) is introduced as a framework that jointly optimizes multi-agent workflow topology and natural-language prompts. It is guided solely by a scalar task metric, without domain initialization or task-specific engineering. The experimental results demonstrate that SWORD achieves statistically significant gains over prompt-only, workflow-only, and staged-optimization baselines under a controlled, identical-backbone comparison. Against the strongest published domain-specific baseline, SWORD further improves accuracy while using a smaller backbone model, substantially less training data, and a very reasonable API cost (\$4--\$6 for each dataset). Beyond predictive performance, SWORD autonomously discovers domain-relevant signals, review-sentiment mapping rules and epidemiological decay priors, purely from scalar error feedback, establishing textual gradients as a mechanism for unsupervised feature-importance discovery in user behavior modeling.

---


### 153. [Evaluating human-AI workflows for field research in viticulture](https://arxiv.org/abs/2610.07669)

**<font color=#1a73e8>作者：</font>** Niko Carvajal Janke, Daoyuan Jin, Shivranjani Baruah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We assessed the value of two live human-AI interactions in a precision disease control project in California vineyards. The project tested whether 2021-2024 commercial scouting records and remote-sensing measurements across 140 hectares could support 2025 red-leaf symptom forecasting for prioritized scouting and virus testing. In Workflow 1, Aleks v1, a multi-agent research system, developed forecasting models with iterative human refinement. We applied Aleks's 2024 vine-scale model to updated 2025 predictors and evaluated red-leaf forecasts against independent 2025 scouting. In retrospective simulations surveying 45% of all vine positions, adding model-informed row prioritization to adaptive scouting increased the encountered proportion of newly recorded red-leaf observations from 85.8% to 94.1%. Within-block scouting comparisons suggested the model mainly improved scouting allocation among blocks. Despite unreliable internal 2024 performance estimates from synthetic oversampling before train/test splitting, Aleks developed an informative vine-scale model in 145 minutes, increasing throughput and answering our research questions. In Workflow 2, we assessed whether higher model-score vines had more frequent virus detection, and whether Aleks could infer this sampling goal from a general prompt with data and literature. Aleks's plan prioritized balanced vineyard and model score coverage, while our plan prioritized field efficiency and high-model-score oversampling. Aleks's and our plans yielded 41/50 (82%) and 97/100 (97%) sampled vines. Aleks's plan omitted instructions for replacing missing vines, limiting implementation and operational value. Five of 137 sampled vines tested positive for grapevine red blotch virus (model score ROC AUC 0.735). These findings support assessing AI interactions by how well they advance field research objectives under live, project-specific constraints.

---


### 154. [EIO-Agents: The Missing Semantic Layer for AI Agent Evaluation](https://arxiv.org/abs/2610.07675)

**<font color=#1a73e8>作者：</font>** Fouad Bousetouane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are entering production in increasingly consequential environments without a shared semantic standard for what their evaluations actually mean. Scores, traces, judge outputs, and multi juror findings are increasingly used to justify readiness and release decisions, yet they often do not specify what evidence supports a claim, what that evidence can establish, or how the claim leads to a decision. We introduce EIO-Agents, an open specification for interoperable AI agent evaluation built on two layers. The Evaluation Intelligence Ontology (EIO) provides the semantic layer through typed evidence, versioned behavioral predicates, evidence contracts, claims, witness rules, proof status, recurrence, and computable derivations for metrics, findings, controls, and PASS, REVIEW, or BLOCK decisions. The Portable Evaluation Record (PER) provides the system of record: a canonical, content addressed representation of one evaluation that preserves the evidence to decision chain and can be re derived, explained, and verified. Scores summarize, juries interpret, and traces record, but none of them define what the evidence means or what it can prove. EIO provides that missing semantic contract, while PER preserves the resulting evaluation as a portable and verifiable system of record. As AI agents assume greater operational responsibility, evaluation must become more than a collection of scores and verdicts; it must become an accountable artifact whose meaning, evidence, limitations, and decisions can be independently checked.

---


### 155. [Exact-Solution Volume and Length Generalization in Transformers](https://arxiv.org/abs/2610.07676)

**<font color=#1a73e8>作者：</font>** Yijia Jessica Zhu, David Chiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Research on transformer expressivity shows whether a transformer is capable of solving a given task, but gives little indication of whether the solution, if learned, is generalizable to longer input lengths. We study this question through normalized exact-solution volume (NESV): the fraction of a bounded parameter region that achieves an exact solution on every input of length $n$. For fixed-width, single-layer transformers with $\log n$-scaled attention, we establish asymptotic bounds on NESV for four tasks: FIRST ($\Theta(1)$), MAJORITY ($\Theta(1/(n\log n))$), INDEX ($\Theta(1/n^3)$), and PARITY ($0$). These results are consistent with previous empirical results: the faster the exact-solution volume decays with input length, the harder it is to length-generalize on that task. Looking deeper into INDEX, our volume analysis reveals two error sources that grow with $n$. Consequently, we study a transformer model that would structurally eliminate one of the terms, theoretically improving the NESV bound to $\Theta(n^{-1})$, and empirically achieving 85% accuracy when tested at $10\times$ the training length, compared with the 60% accuracy of the original model. We conclude that volume analysis may be a useful approach to identify concrete sources of length sensitivity and thus provide insights into task-specific model refinements.

---


### 156. [Adaptive Model Inversion Attacks Generalize a Privacy-Robustness Tradeoff](https://arxiv.org/abs/2610.07677)

**<font color=#1a73e8>作者：</font>** Shailen Smith, Rasmus Torp, Adam Breuer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we show that standard evaluations of high-resolution Model Inversion Attacks (MIAs) significantly underestimate training-data privacy leakage. State-of-the-art privacy defenses, standard training techniques such as MixUp and Adversarial Training, and undefended models all leak training images at rates 1.16 to 6.59 times higher on FaceScrub under simple adaptive changes to the attack, with the largest increases among defenses reporting the strongest privacy. We further show that measured leakage depends on the feature basis of the external classifier used to evaluate reconstructions: for the same reconstructed images, an adversarially trained Inception evaluator identifies the targeted identity at different rates than the standard Inception evaluator. Our results suggest that standard MIA evaluation can mistake optimization and measurement failures for privacy.
These underestimated leakage rates also concealed a broader relationship between privacy and adversarial robustness. Once we adapt the attack and vary the evaluator, reconstruction leakage closely tracks adversarial robustness across recent defenses and standard training regimes, suggesting that robustness provides an attack-agnostic proxy for reconstruction vulnerability that applies far more broadly than previously theorized. This raises an open question: can a practical defense reduce training-data reconstruction without paying a corresponding cost in adversarial robustness?

---


### 157. [Disentangling Dual Image References in Frequency Aware Diffusion Models for Personalized Generation](https://arxiv.org/abs/2610.07684)

**<font color=#1a73e8>作者：</font>** Haipeng Liu, Yang Wang, Meng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized image generation aims to synthesize text-driven images conditioned on reference images, while mainly casting the generation as image customization for foreground and style transfer for background. Previous arts of diffusion models suffers from the text misalignment with background for image customization and foreground for style transfer during the denoising process. Such facts, as we observed, rooted from the entanglement among hybrid frequency bands during the denoising process. To address such salient limitation, in this paper, we study personalized generation based on dual references - customization and color and style reference - and propose a paradigm to disentangle these Dual image references within Frequency-aware Diffusion Models, dubbed Dual-FDM, to simultaneously tackle two crucial personalized image generation tasks: customization style transfer and color style transfer, by disentangling different frequency bands via mask strategy within frequency domain. For customization style transfer, we replace the mid-frequency band of the background in the style reference with that from the foreground of the customized reference. For color style transfer, we substitute the low-frequency band of the background in the style reference with that from both the foreground and background of the color reference. Both the substituted frequency bands are used as the key and value to reconstruct the query foreground and background of the denoised personalized this http URL experiments validate the superiority of Dual-FDM over the state-of-the-art diffusion models for personalized image generation. Our code can be accessed from this https URL.

---


### 158. [BluffJAX: Adversarial Imperfect Information Games in JAX](https://arxiv.org/abs/2610.07686)

**<font color=#1a73e8>作者：</font>** Aryaman Reddi, Jan Peters, Carlo D'Eramo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce BluffJAX: an open-source suite of adversarial imperfect information games in JAX. We provide canonical implementations of games designed for high simulation throughputs and parallelization on GPU accelerators. Our suite consists of well-studied benchmarks such as Texas Hold'Em Poker and Kuhn Poker, as well as games that have not been previously studied in reinforcement learning research, such as Bluff, Stud Poker, and Kemps. We hope that implementing a variety of game mechanics and difficulties will introduce new challenges and foster novel research directions in game-theoretic methods for RL. We benchmark the throughput performance and memory usage of our environments in single and multi-GPU settings, demonstrating scaling of up to hundreds of millions of samples per second, and motivating the usage of BluffJAX over related GPU and CPU-based libraries. We benchmark reinforcement learning, tree search, and game-solving algorithms in JAX in order to provide users with baseline results and facilitate future comparisons.

---


### 159. [PerSpectron: Detecting Invariant Footprints of Microarchitectural Attacks with Perceptron](https://arxiv.org/abs/2610.07691)

**<font color=#1a73e8>作者：</font>** Samira Mirbagher-Ajorpaz, Gilles Pokam, Esmaeil Mohammadian-Koruyeh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting microarchitectural attacks is critical given their proliferation in recent years. Many of these attacks exhibit intrinsic behaviors essential to the nature of their operation, such as creating contention or misspeculation. This study systematically investigates the microarchitectural footprints of hardware-based attacks and shows how they can be detected and classified using an efficient hardware predictor. We present a methodology to use correlated microarchitectural statistics to design a hardware-based neural predictor capable of detecting and classifying microarchitectural attacks before data is leaked. Once a potential attack is detected, it can be proactively mitigated by triggering appropriate countermeasures. Our hardware-based detector, PerSpectron, uses perceptron learning to identify and classify attacks. Perceptron-based prediction has been successfully used in branch prediction and other hardware-based applications. PerSpectron has minimal performance overhead. The statistics being monitored have similar overhead to already existing performance monitoring counters. Additionally, PerSpectron operates outside the processor's critical paths, offering security without added computation delay. Our system achieves a usable detection rate for detecting attacks such as SpectreV1, SpectreV2, SpectreRSB, Meltdown, breakingKSLR, Flush+Flush, Flush+Reload, Prime+Probe as well as cache-attack calibration programs. We also believe that the large number of diverse microarchitectural features offers both evasion resilience and interpretability---features not present in previous hardware security detectors. We detect these attacks early enough to avoid any data leakage, unlike previous work that triggers countermeasures only after data has been exposed.

---


### 160. [RBMatch: Dual-Level Class Rebalancing for Semi-Supervised Building Footprint Extraction](https://arxiv.org/abs/2610.07698)

**<font color=#1a73e8>作者：</font>** Akil Ahmad Taki, Shaikh Anowarul Fattah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate building footprint extraction from high-resolution remote sensing imagery is essential for urban planning, disaster response, and environmental monitoring. However, obtaining dense pixel-level annotations is costly, motivating the use of semi-supervised learning (SSL) to leverage unlabeled imagery. In remote sensing, severe foreground--background imbalance poses a particular challenge for self-training, as it can bias pseudo-label generation and the resulting unsupervised optimization toward the majority background class. We show that addressing this imbalance at only one stage is insufficient: balancing pseudo-label selection alone does not prevent background bias from re-emerging during unsupervised loss optimization, a failure mode we term \emph{imbalance leak}. To address this issue, we propose \textbf{RBMatch}, a dual-level class-rebalancing framework that jointly regulates pseudo-label generation and unsupervised optimization. RBMatch combines a supervised learning pathway with a self-training module comprising three components: adaptive class-specific thresholding (ACT) for balanced pseudo-label selection, confidence-aware class-balanced reweighting (CACBR) for mitigating class bias in the unsupervised loss, and distribution alignment (DAL) for matching the predicted unlabeled-data distribution to the labeled-data prior. Experiments on the WHU, INRIA, and Massachusetts building footprint datasets across labeled ratios of 1%--10% show that RBMatch consistently achieves the best building IoU and F1-score among the evaluated methods. The improvement is most pronounced on the highly imbalanced Massachusetts dataset, where RBMatch improves IoU by 1.37 points over the strongest baseline at a 1% labeling ratio and is the only method to outperform the fully supervised baseline across all twelve dataset--ratio settings.

---


### 161. [On the Boundary of Admission Gates: An Injected-Truth Study of Falsification-First Selection in Quantitative Strategy Research](https://arxiv.org/abs/2610.07701)

**<font color=#1a73e8>作者：</font>** Tianlun Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Strategy research conflates two problems: finding a profitable rule, and establishing that the finding is not search luck. The latter calls for admission gates -- statistical criteria that must be satisfied before a conclusion is adopted -- yet whether gates work, and at what cost, remains untested. We introduce an injected-truth protocol with a random-admission control that adopts at the same rate as the gate; only if the gate beats this control does it carry information rather than merely raise a threshold. Across synthetic and real-calibrated panels, gates eliminate false discoveries in the weak-signal regime but cut adoption to 1--7%, and add nothing when signals are strong. Most importantly, criteria computed on absolute rather than excess returns silently reject every candidate, including true signals. Keywords: multiple testing, backtest overfitting, strategy admission, injected-truth validation, excess returns, false discovery rate

---


### 162. [Independent Multi-Agent Reinforcement Learning with Counterfactual Semantic-Social World Models](https://arxiv.org/abs/2610.07704)

**<font color=#1a73e8>作者：</font>** Fernando Martinez, Tao Li, Yingdong Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Fully decentralized multi-agent reinforcement learning (MARL), also referred to as independent learning, requires each agent to learn and act using only its local information and experience, without a centralized critic or inter-agent communication. Such a stringent information structure renders the conventional reward signal ambiguous. A poor return may result from an ineffective ego action, an incompatible teammate response, or an effective opponent response, yet scalar rewards alone do not reveal which explanation is responsible. We argue that agents can learn more effectively by prospectively comparing the consequences of candidate actions rather than diagnosing failures only from realized returns. We introduce CASTLE (Counterfactual Action-conditioned Semantic Tokens for Local Execution in Decentralized MARL), an offline-training, online-in-context guidance framework with two complementary world models. A Local Dynamics World Model, offline pre-trained over agents' local trajectories, summarizes the agent's local trajectory dynamics and partial observability, while a Semantic-Social World Model predicts compact short-horizon task and social consequences for each candidate ego action. The latter is trained from counterfactual simulator rollouts that expose plausible teammate and opponent responses to alternative actions taken from the same logged rollout state. During online learning and execution, both world models remain frozen and are queried by agents using only locally available information. Their prediction logits provide in-context guidance to an independent PPO policy. Across 30 matched seeds on Tag, Spread, and Adversary in the benchmark multi-particle environments, our proposed CASTLE achieves the highest mean final score among the evaluated methods, exceeding the strongest baseline on each task by 10.67, 6.46, and 0.33 normalized points, respectively.

---


### 163. [What Frame-Level Labels Can and Cannot Do for Small-UAV Point Detection in Thermal Video](https://arxiv.org/abs/2610.07705)

**<font color=#1a73e8>作者：</font>** Wonbin Son, Gyumum Choi, Junil Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing use of unmanned aerial vehicles (UAVs) has increased the importance of image-based UAV detection. Learning-based detectors are trained on imagery and annotations, with annotation type determining the information available during training. We focus on learning localization from frame-level target presence/absence labels when sensor or scene changes make spatial annotations for additional training burdensome. We analyze the detection capability, learning behavior, and potential applications of an existing architecture for point detection of small UAVs, trained with presence/absence labels and requiring no external detector. The architecture freezes spatial features learned through classification and trains a readout with the same frame labels to produce spatial score maps and point detections. On two thermal infrared datasets, CST Anti-UAV and Anti-UAV410, we evaluate localization hit rates and detection rates under false-alarm constraints, analyze the effects of training stages, label allocation, synthesis, and model configuration, and compare with bounding-box detectors. We also explore potential applications on Airborne Object Tracking (AOT) using its visible-light imagery and frame labels. Classification training strengthened target-related spatial responses, while readout training helped extract them consistently. Distributing similar label counts across more videos yielded higher localization hit rates, while synthesis effects varied by dataset and evaluation criterion. Higher localization hit rates did not always improve detection under false-alarm constraints, and failures remained when target signals were weak relative to background variation and under cross-dataset transfer. These findings provide guidance on label allocation, spatial representations and readouts, synthesis, and false-alarm control.

---


### 164. [AgentMemGate: Addressing Speculation Contamination in Conversational Assistant Memory](https://arxiv.org/abs/2610.07707)

**<font color=#1a73e8>作者：</font>** Chirag Sharma, Benjamin Fowlersmith, Karime Maamari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational AI assistants with long-term memory extract facts from user messages into a store consulted in later conversations. A stated plan can enter that store as fact: a user who might move to Seattle may be recorded as already living there. We call this speculation contamination. Final-state memory benchmarks miss this error because they do not probe intermediate state and include few unresolved speculations. We present AgentMemGate, a write-time gate for profile-store memory that classifies extracted statements as speculation, completed event, correction, or other. Speculations remain outside memory, with conditions governing later promotion or deletion. We also contribute a dataset of multi-session conversations in which plans are confirmed, abandoned, or left unresolved. On our 147-conversation held-out set, Mem0 and Graphiti assert unresolved plans as current state for 35.2% and 27.3% of pending plans. On the core benchmark, AgentMemGate eliminates all observed contamination relative to the identical ungated pipeline (87.5% to zero for the most exposed extraction style) and raises task accuracy from 65% to 95%. On the harder held-out set, gated contamination is 3.4% to 5.7% and task accuracy rises by 9 to 13 percentage points. Our analysis identifies field matching as the main remaining bottleneck: realistic speculations often match no profile field and never reach the gate. We release our datasets, prompts, and evaluation code.

---


### 165. [Comprehensive Evaluation and Fine-Tuning of Foundational Cell Nuclei Segmentation Models in Renal Pathology](https://arxiv.org/abs/2610.07711)

**<font color=#1a73e8>作者：</font>** Ruijie Wu, Junlin Guo, Ruining Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate nuclei instance segmentation is essential for quantitative renal pathology, yet general-purpose models often struggle with low contrast, dense nuclei, complex morphology, and strong background staining. In this work, we extended a human-in-the-loop framework by combining 5,901 foundation-model-generated pseudo-labels from well-segmented cases (Easy), 860 newly expert-annotated unresolved challenging cases (Medium), and 198 expert-annotated consensus failure cases (Hard). These annotations, spanning different levels of segmentation difficulty, enabled the systematic evaluation of seven single-source and mixed-source fine-tuning strategies across nine cell segmentation model configurations. Fine-tuning improved all models, with Medium data included in seven of the nine best-performing strategies. LSP-DETR achieved the highest F1 score of 0.8725 with Hard-only fine-tuning, while StarDist showed the largest improvement, increasing from 0.7380 to 0.8332 with Medium-only fine-tuning. These findings show that annotations spanning multiple difficulty levels support effective model adaptation, although the optimal annotation composition remains model dependent.

---


### 166. [Neuromotor Hierarchy Network: Physiological Inductive Biases for Robust Generalization in sEMG Decoding](https://arxiv.org/abs/2610.07713)

**<font color=#1a73e8>作者：</font>** He Wang, Hongyuan Qi, Zhaoxian Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surface electromyography (sEMG) provides a wearable, noninvasive interface to neuromuscular activity for movement decoding and human-computer interaction. Population-scale decoding remains difficult because the relationship between sEMG and neuromuscular activity varies across users and sessions, while task-relevant dynamics span channels and multiple timescales. Learning waveform-to-output mappings from task labels leaves the distinction between recording variability and coordinated motor activity implicit. We introduce the Neuromotor Hierarchy Network (NHN), which learns a compact latent neuromotor state from task supervision to represent task-relevant neuromuscular coordination. NHN constructs this latent state through a hierarchy inspired by neuromotor this http URL adapts recording statistics while preserving relative this http URL spatiotemporal encoder uses parameter-efficient channel interactions and modulates features with multi-timescale history. The resulting features yield candidate activations of learned motor primitives, which are temporally integrated and continuously weighted to form the state. Theoretical analysis characterizes the efficiency, temporal behavior, and optimization of NHN's core mechanisms. We evaluate the architecture for both continuous hand-pose estimation on emg2pose and touch-typing recognition on emg2qwerty. On emg2pose, NHN reduces user-averaged angular error by 0.52% to 2.84% across all three generalization splits in both Regression and Tracking relative to Hadidi et al.'s best task-specific variants, using 48.42% to 48.51% fewer parameters. On emg2qwerty, NHN reduces beam-search character error rate by 19.40% zero-shot and 30.42% after fine-tuning relative to SplashNet-Upscale, using 65.86% fewer parameters. Physiology-guided inference of a latent neuromotor state supports parameter-efficient sEMG decoding.

---


### 167. [RefRoute: Decoupling Conditioning Cost from References via Compact Residual Conditioning and Spatial Routing](https://arxiv.org/abs/2610.07720)

**<font color=#1a73e8>作者：</font>** Wanning He, Yuyao Zhang, Yu-Wing Tai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-reference image generation requires preserving the appearance of multiple subjects while composing them into a coherent scene. However, existing diffusion transformers commonly encode references as dense visual token grids and jointly process them with global attention, making conditioning increasingly expensive as the number and resolution of references grow. We present RefRoute, a framework that addresses both reference representation cost and attention overhead through two complementary mechanisms. Compact residual conditioning combines low-resolution latent tokens with lightweight residual features extracted from full-resolution pixels, reducing reference token counts while retaining fine-grained appearance cues. Condition routing and attention routing align reference tokens with their assigned target regions and restrict cross-reference interactions, while allowing selective reference access beyond region boundaries for scene integration. We further introduce RefRoute-Data for training many-reference generation models and ManyRef100, a benchmark spanning human, object, and mixed compositions with 10-17 references. After many-reference fine-tuning, RefRoute achieves an overall Weighted-Ref-VIEScore of 36.06 on ManyRef100, compared with 8.88 for FLUX.2-Klein-9B. Separate inference-cost evaluations show substantially slower latency growth as the reference count increases: at 16 references, our 50-step and 4-step configurations achieve $18.3\times$ and $14.2\times$ speedups over their corresponding FLUX baselines, respectively. These results establish compact reference representations and spatially routed attention as an effective approach to scalable many-reference image generation.

---


### 168. [PERSIST: Who-What-When Memory Across Sessions for Full-Duplex Spoken Dialogue](https://arxiv.org/abs/2610.07725)

**<font color=#1a73e8>作者：</font>** Achira Lin, Siyuan Hou, Wenyi Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern voice assistants may be shared by multiple users and should be able to answer questions about earlier conversations such as "When did I originally plan to leave?" or adapt their behavior to individual users based on past interactions. This requires more than retrieving a topically similar passage: the assistant must identify the current speaker, recover the relevant past state, and distinguish it from later revisions. We present PERSIST, a persistent memory system for multi-session, multi-speaker spoken dialogue that explicitly models Who, What, and When. PERSIST structures cross-session histories into readable event records and retrieves them with a 3W joint scoring mechanism that combines semantic content, acoustic speaker identity, and temporal state. For real-time full-duplex interaction, PERSIST further reuses intermediate representations from the dialogue backbone, avoiding query-audio re-encoding and reducing retrieval latency from 578.42 ms to 7.03 ms. We also introduce SpokenTrace, a diagnostic benchmark that factorizes evaluation along memory tasks and speaker-query types, exposing failures in recall, speaker attribution, and temporal-state tracking. On SpokenTrace, PERSIST achieves 85.08% end-to-end task accuracy and improves all-support EM@3 from 49.01% with BGE-large to 82.10%.

---


### 169. [Structure-aware Keypoint Localization for Videofluoroscopic Swallowing Study](https://arxiv.org/abs/2610.07726)

**<font color=#1a73e8>作者：</font>** Kai Zhou, Chuanshen Chen, Runhao Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Videofluoroscopic Swallowing Study (VFSS) is one of the gold standard for diagnosing swallowing disorders, providing dynamic X-ray imaging of the swallowing process. Automated kinematic analysis in VFSS relies fundamentally on precise anatomical keypoint localization. However, existing studies focus on limited keypoints (e.g., cervical vertebrae or the hyoid) and overlook critical regions such as the soft palate, while annotating only active swallowing segments and ignoring abundant non-swallowing data, resulting in poor data efficiency. Moreover, leveraging this unlabeled data via standard semi-supervised learning is suboptimal, as generic methods are prone to spatial bias. In medical X-rays with fixed layouts, models tend to memorize absolute coordinates rather than understanding anatomical structures. To tackle these challenges, we introduce VFSSKep, a novel dataset that extends annotations to the soft palate and incorporates large-scale unlabeled data. We further propose S$^3$KL, a Structure-aware Semi-Supervised Keypoint Localization framework designed to overcome spatial bias. It integrates a Structure-Aware Learning strategy to extract high-resolution structural cues for structure-aware representation learning, and a Structural Representation Consistency Learning strategy with block shuffling to enforce invariant structural recognition. Experiments show our method achieves state-of-the-art semi-supervised performance, even with unlabeled and 25% labeled data surpassing fully supervised learning with 100% labeled data. Code and data will be made publicly available at: this https URL.

---


### 170. [Later Is Better: Token Reduction for ViTs Under Distribution Shift](https://arxiv.org/abs/2610.07758)

**<font color=#1a73e8>作者：</font>** Hyeongheon Cha, Hyungjun Yoon, Sung-Ju Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free token reduction accelerates vision transformers by removing redundant tokens across layers, recovering most of the original accuracy at a fraction of the compute. These methods, however, are designed and evaluated primarily on clean data, and under real-world distribution shift their accuracy gap to the uncompressed model widens with the removal rate. We show that this gap is governed by the reduction schedule, the depth profile of removal, usually left fixed as an implementation detail. Concretely, we introduce a one-parameter late-concentrated power-law schedule that consistently improves out-of-distribution accuracy over flat at no extra inference cost. On ImageNet-C with DeiT-S, the late schedule closes 83% of that gap at a 26% compute reduction (+1.17pp), and 99% of it at a lighter 7% reduction (+0.26pp). The gain cannot be attributed to retaining more tokens or using extra compute: held to flat's compute, the late schedule removes more tokens in total and leaves fewer tokens at the end, yet still wins. Single-layer probes point to a mechanism: earlier reductions perturb features that pass through more remaining layers, front-loading reduction error in depth. The effect is broad, holding across five token-reduction methods (ToMe, EViT, ATS, ATC, PiToMe), nine backbones, all ImageNet-C corruption types, eight further shift suites, and two further modalities, video and vision-language QA. It is also specific to shift, still positive on clean and rising monotonically to ~4x that at the highest severity 5. The schedule keeps its gain under six test-time adaptation methods, and needs no per-input or per-domain tuning.

---


### 171. [What Response Marginals Miss: Adaptive Query Complexity of Functional Backdoor Recovery](https://arxiv.org/abs/2610.07771)

**<font color=#1a73e8>作者：</font>** Yunjae Hwang, Byoungjin Seok  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Functional backdoor recovery finds any trigger whose attack success rate is at least a given threshold rather than to recover the planted trigger. We study the minimum number of queries required for this task under label feedback which returns the predicted class label. We construct two finite families of victim models that have exactly the same attack success rate for every victim and trigger candidate. The distribution of returned labels for every query is also identical under a uniformly chosen victim. These families form an explicit counterexample that despite the matched quantities, their optimal adaptive query complexities are \(\Theta(\log H)\) and \(\Theta(H)\) where \(H\) is the number of possible victims. The difference arises because the same non-target labels are associated with different sets of victims, so successive queries eliminate possible victims at different rates. This separation disappears when the response is reduced to binary feedback, which reports only whether the target label is returned. The separation also persists for every fixed failure probability below one. Finally, we realize the same recovery problems with trained CIFAR-10 ResNet-18 classifiers and verify the predicted optimal query budgets. These results show that attack success rate and the distribution of returned labels for each query are insufficient to determine the query complexity of functional backdoor recovery.

---


### 172. [From Laboratory to Road: Evaluating Wearable Gaze Accuracy for Driving](https://arxiv.org/abs/2610.07783)

**<font color=#1a73e8>作者：</font>** William Engel, Fabian Flohr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird's-eye-view (BEV) representations have become a widely used interface between perception and planning in autonomous driving, but they encode what is in a scene, not what is behaviorally relevant to a human driver. Gaze offers a compelling behavioral signal for this gap, yet wearable eye trackers are routinely deployed as if their spatial output were ground truth, despite known sensitivity to head motion, illumination, and calibration drift. We present, to our knowledge, the first unified framework for quantifying wearable gaze accuracy under real driving conditions. Our on-road study contains 41 validated scenes in which one driver fixated a vehicle's license plate. Gaze error is measured as the angular difference between the plate center and the gaze direction estimated by the glasses. Separate indoor studies with the same driver and device systematically analyze how distance, illumination, head motion, target motion, and gaze eccentricity affect both systematic bias and gaze precision. The mean on-road error was 4.58 degrees. Applying an offset estimated from the indoor recordings reduced it to 1.10 degrees and improved all 41 scenes. Because this offset varied between sessions, reliable BEV supervision may require online recalibration and condition-dependent estimates of gaze uncertainty.

---


### 173. [Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied Agents](https://arxiv.org/abs/2610.07785)

**<font color=#1a73e8>作者：</font>** Gyusik Seo, Jaehong Yoon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central capability of embodied agents is to accomplish complex objectives through sequences of interdependent tasks. Yet existing visual goal-conditioned policies underlying these agents are typically evaluated on isolated interactions where the target is already visible, and thus do not capture the conditions that arise during continuous long-horizon task execution. In such settings, each task begins from the state left by the previous one: the agent may end at a different position and orientation, the world may have been modified, and the next interaction target may lie outside the current field of view. As a result, agents relying on such policies may struggle to proceed to the next task when they cannot ground their target in the current observation. To address this challenge, we propose Attacca, a new approach that trains visual goal-conditioned policies on complete search-to-interact trajectories using goal images decoupled from the execution environment. Attacca uses context-decoupled goal sampling to pair each demonstration with a class-compatible masked goal image from another world, removing direct scene and pose correspondence. It learns dense current-view grounding through a target-mask prediction head, providing auxiliary supervision beyond action imitation. We further introduce behavioral-phase conditioning that teaches the policy to distinguish Search, Approach, and Interact stages and adapt its control as execution progresses. We evaluate Attacca on multiple short- and long-horizon embodied tasks in Minecraft. Our method achieves 39.0-47.5% clean success, improving over the strongest baseline by 1.7-2.4x. On long-horizon tasks, it attains 54%, 30%, and 28% completion, yielding up to a 7x improvement.

---


### 174. [Extending Pathwise Gradients to Discrete Random Variables via Finite-Order Relaxation](https://arxiv.org/abs/2610.07786)

**<font color=#1a73e8>作者：</font>** Donghan He, Luhuan Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pathwise gradients are preferred for continuous random variables because they are unbiased, low variance, and work with a single sample. For discrete variables, however, the pathwise identity cannot generally be exact for every differentiable function. We propose a general framework to construct finite-order exact pathwise gradient estimators for a range of common discrete variables such as Poisson. The estimator is the least-norm solution among all solutions that are unbiased for polynomials of degree at most. The resulting estimators preserve the hard forward sample, require no temperature tuning, and can be implemented in a few lines of codes. Against other admissible solutions, our estimator is unique and minimizes weight variance; in contrast, prior works use categorical variables or augmented representations to approximate non-categorical variables that induces excess variance and computations. To understand approximation bias for functions beyond the prescribed class, we also derive a non-asymptotic bias bound. In experiments our low order methods match or improve tuned baselines across linear, nonlinear and hierarchical latent-variable models, while out-speeding competitors in every runtime benchmark.

---


### 175. [Image-Space Refraction Correction for Underwater 3D Reconstruction: Warping Flat-Port Views into Pinhole Perspective](https://arxiv.org/abs/2610.07788)

**<font color=#1a73e8>作者：</font>** Chelim Lim, Tobias Fischer, Emilio Olivastri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consumer-grade cameras in flat-port housings are widely used for underwater exploration and mapping of coral reefs and seafloor habitats due to their low cost and accessibility. However, refraction at flat-port interfaces causes bowl-shaped deformation in reconstructed scenes and camera trajectories, compromising the metric accuracy required for mapping and navigation. To remove the dominant refractive distortion before reconstruction, we introduce a physics-based refraction correction in image space. Our method is downstream-agnostic: the refraction-corrected images can be directly used as input to existing reconstruction and SLAM algorithms. We characterize the refractive distortion through ray-tracing simulations and validate our correction on two real underwater datasets with differing scene structures. Compared with conventional and refractive Structure-from-Motion (SfM), our approach removes reconstruction deformation while registering more frames and maintaining low reprojection error. The correction further generalizes across diverse reconstruction and VSLAM backends, demonstrating its broad applicability to downstream vision pipelines.

---


### 176. [Geometry-Constrained Bidirectional Point Cloud Registration for Thin, Sheet-Like Heritage Artifacts](https://arxiv.org/abs/2610.07793)

**<font color=#1a73e8>作者：</font>** Yuezhe Zhang, Lei Wei, Jingnan Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-contact three-dimensional reconstruction of thin, sheet-like heritage artifacts poses significant geometric and registration challenges. Due to their fragility, these artifacts cannot be suspended or equipped with artificial markers, necessitating independent acquisition of their front and back surfaces. Subsequent registration proves difficult due to the limited number of shared geometric features and the scarcity of explicit physical constraints, which may result in rotational ambiguity, instability, and structural collapse during iterative optimization. To address these challenges, we propose a geometry-constrained bidirectional point cloud registration method specifically tailored for thin, sheet-like heritage artifacts. The method integrates semantic-guided preprocessing, Principal Component Analysis (PCA)-based geometric normalization, and a thickness-aware registration strategy. The estimated physical thickness is incorporated as a geometric constraint to preserve structural integrity during registration. Rotational ambiguity is resolved by evaluating a finite set of global rotation hypotheses, each refined using the point-to-plane Iterative Closest Point (ICP) algorithm, with the optimal transformation selected via a geometry-aware fitness criterion consistent with the thickness scale. Experimental results show that the proposed method achieves competitive or improved performance in most cases, particularly in projected area consistency and physically plausible front-back alignment. In addition, the thickness-aware constraint and rotation hypothesis evaluation reduce the risk of degenerate configurations in which the two surfaces are incorrectly flipped while still yielding deceptively acceptable numerical scores, supporting reliable non-contact digitization of delicate and thin heritage artifacts. Implementation details are available at this https URL.

---


### 177. [Efficient Gaussian Splatting Sequence Compression with Standard Video Codecs](https://arxiv.org/abs/2610.07795)

**<font color=#1a73e8>作者：</font>** Qi Yang, Shuting Xia, Le Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel effective Gaussian Splatting (GS) sequence Compression method that utilizes the Video codec (GSCV). Existing video-based GS sequence compression relies on the Parallel Linear Assignment Sorting (PLAS) and tracked primitive information to convert GS into smooth 2D videos. However, tracked information is not available for most practical applications, and without it, using the vanilla PLAS can generate images exhibiting weak inter-frame correlation, due to its stochastic nature. GSCV incorporates a simple yet efficient Inter-PLAS method to produce close images between the I- and P-frames of GS, enhancing the inter-frame performance of video codec greatly. GSCV also realizes a new pipeline based on the state-of-the-art video codecs with high bit-depth GS images, achieving higher compressibility while simultaneously providing a higher quality upper bound. Experimental results show that the proposed GSCV exhibits obviously improved performance over MPEG video and point cloud-based anchors in GS sequence compression. The code is available at this https URL.

---


### 178. [The Geometry of Empowerment](https://arxiv.org/abs/2610.07796)

**<font color=#1a73e8>作者：</font>** Catherine Ji, Vivek Myers, Sergey Levine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Empowerment captures the capacity for an agent to actively control its environment. While conceptually appealing as an information-theoretic quantity, the connection between empowerment and structurally central states that provide broad access to future outcomes has remained an open question. In this work, we link empowerment maximization and skill-learning methods to provide new geometries for interpreting and analyzing empowerment. Our analyses answer longstanding open questions on the connections between empowerment and structural centrality. Our analyses also reveal distinctions between information and reward geometries, highlighting important theoretical implications to build scalable empowerment-maximization methods. Website and code can be found at this https URL.

---


### 179. [Novice Reliance Calibration in AI-Assisted Decision Making: The Role of Explanations and Self-Assessment](https://arxiv.org/abs/2610.07800)

**<font color=#1a73e8>作者：</font>** Eun Jeong Kang, Peter, Duan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) tools are widely used to support decision making in tasks and domains where no immediate performance feedback is available. In these settings, users cannot learn to adjust their reliance behavior over time through trial and error. However, little is known about how novice users calibrate reliance on AI when external feedback is unavailable, or whether AI explanations can support calibration in its absence. We introduce reliance calibration as an organizing construct for studying how novice users dynamically adjust reliance behavior, and examine how AI explanations and meta-cognitive self-assessment shape it. Through a between-subjects study with 110 participants completing a clinical entity extraction task with AI assistance and limited performance feedback, we observe that novice users exhibit systematic drift toward over-reliance in the presence of explanations, while higher self-reported task understanding is associated with more selective reliance behavior. These results extend reliance calibration research into human-AI collaboration contexts without real-time performance signals and present actionable guidelines on designing AI tools that must support appropriate reliance in these settings.

---


### 180. [Towards benchmarking Western Bluebird detection in the wild](https://arxiv.org/abs/2610.07802)

**<font color=#1a73e8>作者：</font>** Estela Monserrat Arriaga Santana, Julian Rosas Scull, Ibeth P. Alarcón 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird monitoring in natural environments is challenging due to the small size of some species of birds relative to the scene, background clutter, variability in illumination, and the observers' viewpoint. Progress is further limited by the scarcity of large-scale, realistic datasets, which are essential for understanding behavioral patterns. To address this gap, we introduce a new benchmark dataset for the detection and segmentation of Western bluebirds (Sialia Mexicana), comprising over 6,000 labeled images from 41 recording sessions. The dataset features high-resolution (4K) in-the-wild images in which birds occupy only a small fraction of the image. We evaluated supervised detectors, open-vocabulary models under zero-shot and fine-tuned settings, and segmentation approaches. Supervised detectors remain the most reliable overall, with Faster R-CNN achieving the highest detection mAP and RT-DETR offering the best precision-recall trade-off. Open-vocabulary models perform poorly in zero-shot settings; however, fine-tuning substantially improves their performance, with YOLO-World becoming competitive with supervised methods and achieving the highest precision, F1-score, and mAP@0.5. For segmentation, supervised methods significantly outperform Grounded-SAM and SAM 3: Mask R-CNN achieves the highest mask mAP, while YOLOv8-Seg provides the best precision and fastest inference. A diagnostic analysis further shows that failures are not explained by object size alone, but by a combination of apparent scale, brightness, contrast, clutter, blur, crowding, and recording-session variation. Overall, our findings highlight the difficulty of zero-shot bird detection in cluttered ecological scenes and underscore the importance of domain adaptation in small-object settings.

---


### 181. [SIFT: Search Intent-to-Filter Transformer for Multi-Task Personalized Filter Ranking at Airbnb](https://arxiv.org/abs/2610.07810)

**<font color=#1a73e8>作者：</font>** Shashank Dabriwal, Tanya Piplani, Hao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Search filters help guests navigate vast catalogs in two-sided marketplaces like Airbnb, and recommending the right filters can meaningfully lift booking conversion. Many such production filter-ranking systems, however, represent the guest through hand-engineered, pre-aggregated features generated by ETL pipelines. This makes it expensive to maintain and difficult to extend for new filter types or contextual dimensions (trip length, group size). We present SIFT (Search Intent-to-Filter Transformer), a ranking model built on transformers that learns guest preferences directly from raw behavioral sequences. SIFT replaces manual feature engineering with a unified guest representation that feeds multiple prediction tasks, including booking likelihood, filter engagement, and ordinal capacity thresholds (e.g., 2+ bedrooms) -- a general framework for filter ranking in two-sided marketplaces that accommodates both boolean and numeric-range filter types. Extending SIFT to new filters requires only adding a new head, not a new feature pipeline. To keep serving fast, this guest representation is computed offline on a daily cadence rather than at request time. Offline, SIFT improves booking and amenity-engagement PR-AUC by +51.9% and +62.8% respectively over the production baseline. In online A/B testing, SIFT increased engagement with recommended filters by +20.0%, overall filter usage among searchers by +0.72%, and usage of the newly-supported bedroom, bathroom, and bed filters by +3.9%, +10.7%, and +0.52% respectively. Demonstrating the system's extensibility, we rapidly integrated a novel hotel-intent filter using the same shared representation, driving a +3.8% lift in uncancelled hotel bookings and a +0.76% lift in overall marketplace bookings. SIFT is now fully deployed in production, serving scalable personalization to millions of guests.

---


### 182. [Efficient and Implementation-Hardened RBLWE on Commodity Cortex-M Microcontrollers](https://arxiv.org/abs/2610.07820)

**<font color=#1a73e8>作者：</font>** Muhammad Asim Javaid, Muhammad Adeel Pasha, Muhammad Ali Siddiqi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Efficient post-quantum cryptography on resource-constrained Internet-of-Things (IoT) devices requires implementations that exploit the target processor architecture while resisting practical implementation attacks. This paper presents an ISA-accelerated and implementation-hardened realization of Ring Binary Learning with Errors (RBLWE) encryption on a commodity ARM Cortex-M33 microcontroller. Packing four 8-bit polynomial coefficients into the byte lanes of a 32-bit register and processing them with SIMD-style instructions, together with a packed message codec, accelerates encryption and decryption, while a buffered hardware-TRNG entropy source drawn from the on-die Secure Element drives the key-generation gain. Together these give same-core cold-start speedups of $4.06\times$, $3.35\times$, and $3.01\times$ for key generation, encryption, and decryption over a scalar baseline, and $3.52\times$/$3.18\times$ lower encryption/decryption cycle counts than a reference Cortex-M0 implementation. On top of this accelerated core, we add four staged countermeasures: constant-time execution, fault hardening against zeroing, random-corruption, and instruction-skip faults, a Fujisaki-Okamoto (FO)-style CCA2 transform, and first-order shared (masked) CPA decryption, reporting each layer's cost individually. Binary-level inspection confirms these countermeasures survive compilation and identifies a compiler-induced masking flaw resolved with a hand-written assembly replacement. Dudect-style timing tests, debugger-assisted fault-injection campaigns, and component-level TVLA then provide implementation-level evidence for the staged protections. The results demonstrate a practical acceleration-security tradeoff for RBLWE on off-the-shelf microcontrollers and reusable architecture-aware techniques for lightweight post-quantum implementations.

---


### 183. [Nucleus Speculative Decoding: Plausibility-Aware Verification Beyond Exact Distribution](https://arxiv.org/abs/2610.07822)

**<font color=#1a73e8>作者：</font>** Shuhao Li, Fanghua Ye, Wanyu Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive generation by using a lightweight draft model to propose multiple tokens that are verified by a target model in parallel. However, the standard acceptance rule focuses on exact distribution correction and rejects tokens that remain highly plausible under the target model when the draft model assigns excess probability. This conservative verification limits the number of draft tokens retained after each verification forward pass. We introduce Nucleus Speculative Decoding (NSD), a relaxed verification method that incorporates target-model plausibility into speculative decoding. NSD accepts a draft token if it satisfies the standard acceptance rule or belongs to the target model's nucleus. We theoretically characterize the distributional deviation introduced by our method and show that the single-step error is exactly determined by the draft model's excess probability within the target nucleus. We further derive sequence-level fidelity bounds that quantify how local deviations accumulate over autoregressive decoding. Experiments across multiple target models and proposal mechanisms demonstrate that NSD consistently improves speculative decoding efficiency while maintaining competitive task performance. Our method achieves throughput speedups of up to $5.16\times$ over autoregressive decoding and up to $3.15\times$ over standard speculative decoding. These improvements coincide with longer accepted lengths, allowing more output tokens to share the cost of each target verification pass. Analysis shows that plausibility-aware verification provides an effective approach for relaxed verification and speculative decoding efficiency. Our code is available at this https URL.

---


### 184. [TTNet: Multi-Task Deep Learning for Table Tennis Player Analysis with Smart Racket](https://arxiv.org/abs/2610.07823)

**<font color=#1a73e8>作者：</font>** Ko-Hsun Chen, Xiang-Wei Ke, Hsien-Cheng Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The AI CUP 2025 Precise Analysis of Table Tennis Smart Racket Data Competition introduced smart table tennis rackets that collect extensive player swing data, enabling research on table tennis big data. These data support in-depth analysis of players' return techniques and swing-force consistency, improving the accuracy of player skill assessment. This study focuses on six-axis sensor data collected by smart table tennis rackets and proposes TTNet, a novel deep learning model with multitask learning capabilities, to advance table tennis data analysis and related applications. TTNet combines convolutional neural networks (CNNs), residual networks (ResNet), and self-attention mechanisms to simultaneously predict four player attributes: gender, playing hand, years of experience, and skill level. We adopt a two-stage training strategy that incorporates data augmentation and task-specific loss functions to improve generalization on imbalanced data. Our approach achieved second place on the official competition leaderboard.

---


### 185. [CANDLE: Cortical Null-Space Decomposition for Noninvasive Brain Source Imaging](https://arxiv.org/abs/2610.07824)

**<font color=#1a73e8>作者：</font>** Shuntaro Suzuki, Yuiga Wada, Komei Sugiura  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrophysiological source imaging (ESI) aims to estimate cortical source activity from noninvasive electrophysiological measurements such as electroencephalogram (EEG). However, ESI is fundamentally ill-posed because source activity is substantially higher-dimensional than sensor observations, resulting in non-unique solutions. Recent learning-based approaches address this ambiguity by learning data-driven source priors, yet they often struggle to generalize across subject-specific cortical geometries. To address this, we propose CANDLE, a learning-based ESI model that estimates source activity on subject-specific cortical geometries. CANDLE learns a prior over the null space induced by the source-to-sensor mapping derived from T1-weighted MRI, restricting learning to unobservable source components while preserving geometric constraints. To train CANDLE, we develop a whole-brain simulator spanning over 1,100 subject-specific cortical geometries with source configurations derived from over 26,000 statistical brain maps. Trained exclusively on simulated data, CANDLE outperformed prior ESI methods on simulated source activity estimation and generalized to two empirical tasks: (i) intracranial stimulation localization from simultaneously recorded scalp EEG and (ii) epileptogenic zone estimation from presurgical interictal EEG. Our project page is available at this https URL}{this https URL.

---


### 186. [Agentic Semantic Sensing for Resource-Adaptive AI-RAN](https://arxiv.org/abs/2610.07829)

**<font color=#1a73e8>作者：</font>** Zhongqin Wang, Xiaoqi Zhang, Nan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic sensing (SemS) acquires task-relevant information rather than reconstructing complete physical information. Existing SemS formulations typically operate open loop: sensing configurations and observation schedules are fixed before inference and cannot respond to evolving task-level evidence. We propose Agentic SemS, a closed-loop framework for AI-enabled radio access networks (AI-RANs) that controls sensing within a communication-feasible profile set. A profile-conditioned causal Transformer updates the semantic belief from streaming observations, while key-value caching enables efficient state updates across profile changes without repeatedly processing the complete history. A semantic utility network estimates the task-level benefit of acquiring the next observation block under each feasible profile after accounting for sensing cost. The resulting continuation utilities jointly support next-profile selection and semantic early exit, adapting sensing configuration and duration to evolving evidence. The expected semantic gain is further related to conditional mutual information, providing a value-of-information interpretation of continued online sensing. Experiments on Widar3.0 with six emulated sensing profiles show that, in comparison with full-sequence High, the resource-efficient Agentic setting reduces normalized cumulative sensing cost by 25.33% while achieving 85.79% Macro-F1. At the same utility checkpoint, semantic early exit provides a further 12.35% cost reduction over adaptive sensing without early exit, with a 0.97-percentage-point Macro-F1 decrease.

---


### 187. [Retrieval Is Not Enough: Refreshing Memory for Frozen Time-Series Forecasters](https://arxiv.org/abs/2610.07834)

**<font color=#1a73e8>作者：</font>** Chao He, Jianyu Xu, Xinyi Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented time-series forecasting uses the continuations of historical segments similar to the current context as references for a forecaster. Most existing methods build the retrieval memory once from the training segment, leaving observations revealed after deployment unavailable as references, and generally do not calibrate how much the retrieved information should influence a frozen forecaster. We identify two key determinants of retrieval utility for a frozen forecaster: whether the history still reflects the current state, and whether the correction it induces aligns with the forecaster's residual errors, an alignment that can shift between validation and deployment when the memory becomes stale. We propose FreshCast, a plug-in retrieval framework that keeps the forecaster frozen, continuously updates a non-parametric memory with new observations, forms a memory forecast through relational kernel regression, and calibrates its weight in closed form on the validation segment. Under a simplified generative model, we characterize the optimal combination gain through the second-order relation between forecaster error and memory correction, and show that a sufficiently long look-back can make periodic memory information redundant. Across seven benchmarks and ten forecasting architectures, FreshCast reduces average MSE for every evaluated forecaster and input length, by 14.6% and 5.6% at input lengths 96 and 720, and achieves lower MSE than the evaluated retrieval-augmented and online baselines in their comparison settings. Ablations show that freezing the memory at the end of training removes most of the gain, identifying post-training observations as a primary source of improvement. For a frozen forecaster, useful historical references must remain timely and provide information that helps correct its remaining errors.

---


### 188. [CHARTER: Auditing Reference Substitution in Hierarchical Compact-Evidence Evaluation for Computational Pathology](https://arxiv.org/abs/2610.07843)

**<font color=#1a73e8>作者：</font>** Hyun Do Jung, Jungwon Choi, Soojung Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In digital pathology, compact evidence is often used to explain or audit predictions made by whole-slide image multiple instance learning models. In hierarchical compact-evidence pipelines, candidate filtering introduces a strategy-specific candidate-conditioned prediction alongside the original full-bag prediction. If the evaluation reference changes while the intended target remains the original full-bag prediction, however, not only can the measured fidelity of the same compact evidence change, but comparisons between competing candidate strategies can also change. To make this dependence explicit, we introduce CHARTER, a reference-aware evaluation charter that asks researchers to DECLARE the intended target and reference, QUANTIFY candidate-induced prediction shift, and AUDIT the stability of comparative conclusions. Across the 15 comparisons in our main five-seed Random-K audit, 4 showed determinate reversals; in a matched native-ranking stress test, the ACMIL comparison changed from REVERSED to PRESERVED. CHARTER turns otherwise implicit candidate-filtering and reference choices into an auditable evaluation specification, helping distinguish genuine preservation of the intended prediction from apparent gains induced by changing the prediction being explained.

---


### 189. [Lifecycle-Based Design and Evaluation of Real-Time Backup Triggers for Ransomware Damage Mitigation](https://arxiv.org/abs/2610.07854)

**<font color=#1a73e8>作者：</font>** Kosuke Higuchi, Ryotaro Kobayashi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware continues to encrypt files during the interval between attack onset and detection. Real-time backups can mitigate this damage by preserving files before they are modified. The previously proposed Real-Time Open-File Backup System (ROFBS) triggers backups primarily on file-open events. However, the file lifecycle offers several candidate trigger points, including open, read, write, and rename operations. Triggering backups too early may create unnecessary backup files, whereas triggering them too late may allow ransomware writes to race with backup creation and prevent the preservation of clean file contents. Consequently, it remains unclear which trigger timing best balances recoverability and the number of backups created. In this study, we design and evaluate real-time backup triggers for mitigating ransomware damage from a file-lifecycle perspective. Specifically, we compare four strategies: Open-time backup, Read-time backup, Write-time backup, and Rename-time backup. We implement these strategies in an ROFBS-style prototype on XFS and evaluate them using five ransomware samples: Conti, Sodinokibi, AvosLocker, REvil, and HelloKitty. Our results clarify how trigger timing affects both damage mitigation and the number of backups created, providing design guidance for selecting effective triggers in real-time backup systems against ransomware.

---


### 190. [A Decision-Focused Neural Optimization Framework for Personalized Route Reproduction from Vehicle Trajectories](https://arxiv.org/abs/2610.07857)

**<font color=#1a73e8>作者：</font>** Gyeongjun Kim, Yeseul Kang, Keemin Sohn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study formulates individual route reproduction as a shortest-path problem over learned driver-specific latent link costs. The central idea is that, once such latent costs are inferred from contextual information, observed routes can be reproduced without enumerating alternative route sets. We propose a neural pipeline that includes a perception model that embeds context covariates, which comprises individual characteristics, trip-specific attributes, and network-level traffic states, into the personalized link costs. A constrained optimization (CO) layer, which determines the shortest path (SP) based on these estimated costs, follows the perception encoder. To enable end-to-end training, we employ decision-focused learning to align the predicted shortest paths with observed routes. The implicit maximum likelihood estimation (iMLE) provides an approximate gradient of the loss function that contains the non-differentiable CO layer. Furthermore, a regularization term anchors the latent cost distribution to the empirical scale of observed link travel times, mitigating the scale ambiguity inherent in shortest-path supervision. Empirical evaluations demonstrate that the proposed framework outperforms baseline route choice models in path reproduction. The learned latent costs, interpreted as proxies for perceived travel costs, provide plausible explanations for heterogeneous route choices.

---


### 191. [Tram-FL: Reducing Communication and Computation Costs through Sequential Model Circulation in Decentralized Federated Learning](https://arxiv.org/abs/2610.07859)

**<font color=#1a73e8>作者：</font>** Kota Maejima, Takayuki Nishio, Asato Yamazaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional decentralized federated learning (DFL) often focuses on clients, with each client maintaining a model copy, performing updates individually, and undertaking model exchange and integration. While fully leveraging computational resources can shorten training times, it can also lead to significant computational and communication waste. This is especially pronounced with non-independent and identically distributed (non-IID) data, where achieving high model accuracy demands extra resources. This research shifts focus to the model itself, aiming to realize DFL with minimal computation and communication costs. To this end, we propose Tram-FL (Traveling Model Training Mechanism for Decentralized Federated Learning), a mechanism designed to efficiently address these challenges. It sequentially trains a single model by circulating it among nodes. We address the training scheduling problem in model circulation-based training, specifically determining which nodes should update the model and the number of updates to perform. This is approached by considering the model's circulation route and update iteration allocation, for which we propose simple yet effective methods. Additionally, with quantized momentum, Tram-FL achieves high accuracy with fewer model circulations while controlling communication load per transmission. Experimental results show that the proposed algorithm, even with non-IID data, converges to a global model with reduced communication and computation.

---


### 192. [The Amplifier Effect: Human-Factor Risks of AI-Suggested Correlation and Auto-Propagation in Multi-Framework GRC Self-Assessment](https://arxiv.org/abs/2610.07866)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Michael Ioannou, Marina Korgiala-Karyda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-framework Governance, Risk and Compliance (GRC) platforms increasingly automate the link between an organisation's self-assessment answer and the compliance obligations that answer is said to satisfy. Cross-framework control mapping, AI-suggested question correlation, and automatic propagation of answers and evidence across correlated questions all serve the legitimate efficiency goal of reducing duplicate work for small and medium-sized enterprises under the EU Cyber Resilience Act, NIS2 and GDPR. The same mechanisms, however, amplify the consequences of any human-factor bias in a single answer: one optimistically-graded control, one rubber-stamped attestation, or one AI-drafted answer can be silently replicated as evidence of compliance with many obligations across multiple frameworks. We call this the amplifier effect: a platform-design property (coarse-grained attestation and un-gated propagation) rather than a failing of individual users. Using two EU-funded SME-facing GRC platforms, CYBERFORT and CYBER-BRIDGE, as examples, we (i) describe the amplification mechanism in concrete data-model terms, (ii) propose a six-dimension scoring framework for evaluating any GRC tool's exposure to the effect, (iii) instantiate the framework on a thirteen-tool comparison covering enterprise IRM, mid-market platforms, compliance-automation tools, and the two EU SME projects, and (iv) outline a measurement protocol that a consortium with access to production self-assessment data can run. The thirteen-tool comparison is a structured design assessment, not an empirical measurement of user behaviour. The EU SME platforms score lowest on the amplifier dimensions because their burden-reduction design deliberately trades sign-off granularity for throughput; we report this as a design trade-off, not a verdict on the platforms. Our contribution is the framing and the measurement protocol.

---


### 193. [Plug-and-Play Quantum-Resistant BLE Pairing for Medical Implants via NFC Out-of-Band](https://arxiv.org/abs/2610.07870)

**<font color=#1a73e8>作者：</font>** Muhammad Asim Javaid, Muhammad Shafay Tanveer Hassan, Faaiz Umer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bluetooth Low Energy (BLE) pairing establishes the cryptographic foundation for secure device communication. However, mainstream man-in-the-middle (MITM)-resistant pairing methods, such as Numeric Comparison and Passkey Entry, require user interfaces that implantable medical devices (IMDs) inherently lack, making Near-Field Communication (NFC)-assisted Out-of-Band (OOB) pairing an attractive alternative. Existing NFC-assisted OOB schemes authenticate a classical BLE key exchange that remains vulnerable to quantum attacks, while the NFC channel itself is susceptible to eavesdropping and active injection under stronger threat models. To address these limitations, we propose a lightweight, plug-and-play NFC-based OOB pairing protocol that performs a post-quantum key encapsulation mechanism (KEM) entirely over the NFC channel, ensuring that no shared secret is transmitted over NFC while reducing long-range radio-frequency (RF) exposure during pairing. The proposed protocol requires no modifications to the BLE stack and inherently resists RF battery-depletion attacks. Evaluation on an IMD-class proof-of-concept testbed demonstrates that post-quantum OOB pairing is practical on resource-constrained devices, reducing projected battery life by less than 0.57\% for Kyber-1024 and 0.56\% for FireSABER under an operational usage model relative to the MITM-vulnerable Just Works method.

---


### 194. [Don't Let One Lie Survive A Hundred Truths: A Selective Bayesian Trust Estimator for Collaborative Perception](https://arxiv.org/abs/2610.07875)

**<font color=#1a73e8>作者：</font>** Yutong Liu, Chenyi Wang, Ming F. Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Collaborative perception (CP) enables connected vehicles to see beyond their own sensors but makes them dependent on messages they cannot independently verify. A compromised collaborator can surgically conceal a single safety-critical object or inject a non-existing one while correctly reporting many others. Existing Bayesian trust mechanisms pool agreement across objects, which, while effective against blatant untargeted attacks, either incurs high false-positive rates (FPR), or allows unrelated correct reports to dilute persistent attack evidence for stealthy single-object attackers. To address this problem, we propose SABER, a selective two-tier Bayesian trust estimator. The first tier maintains broad agent and object trust, preserving the ability to downweight benign but low-quality contributors. Cumulative-sum screening selects agent--object pairs with persistent omissions or unsupported reports for focused Bayesian assessment. The second tier checks these pairs against other agents' evidence and maintains a separate, reference-weighted Beta state for each. The lowest pair score constrains agent trust, preventing unrelated reports from diluting a targeted attack. We establish sufficient conditions for stronger attacker-side trust reductions with bounded additional benign false alarms at fixed thresholds. Compared with state-of-the-art CP defenses, SABER improves attack detection while reducing benign FPRs. On OPV2V, SABER improves defense ROC-AUC over MATE by up to 0.427 in late fusion and 0.337 in intermediate fusion. Against advanced intermediate-fusion data fabrication attacks, it increases detection rates over ROBOSAC and LUCIA by up to 96.40 and 67.07 percentage points, respectively, while reducing FPRs.

---


### 195. [Self-Referenced Social Preferences: Cooperation without Observing Others Rewards](https://arxiv.org/abs/2610.07881)

**<font color=#1a73e8>作者：</font>** Mohamed Ayman Mohamed, Harshil Kotamreddy, Marcos Menon Jose  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social preferences can promote cooperation in multi-agent reinforcement learning, but existing approaches often require agents to observe the rewards of their peers. In many real-world interactions, however, an agent can, as humans do, observe others' behavior and outcomes without access to their private reward signals. We introduce self-referenced social preferences, in which each agent learns a model of its own reward, applies it to other agents' observed transitions to assess their outcomes from its own perspective, and feeds these self-referenced assessments into standard social preferences. We study two ways to incorporate these assessments: modifying the learning reward, or using them to weight policy updates. We evaluate the approach on three sequential social dilemmas, Escape Room, Clean Up, and Commons Harvest, which require volunteering, public-good contribution, and resource restraint, respectively. Across all three environments, agents learn cooperative behavior without observing others' rewards, including in settings where independent learners fail to cooperate, and frequently achieve more equitable divisions of jointly produced returns than agents with access to true rewards. The effective integration point depends on the social preference: inequity aversion works best in the reward together with a value look-ahead, whereas a purely benevolent preference benefits from policy-update weighting. Under partial observability, the policy-update approach continues to support cooperation. These results show that explicit access to other agents' reward signals is not necessary for learning cooperative behavior: social preferences can instead be grounded in self-referenced assessments of others' outcomes derived from their observed behavior.

---


### 196. [Revar3r: gauge-aware perturbation uncertainty for feed-forward 3d reconstruction](https://arxiv.org/abs/2610.07883)

**<font color=#1a73e8>作者：</font>** Sammam Mahdi, Fariha Binta Salim, Rakin Bin Rabbani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A correctly reconstructed distant point appears uncertain even when a frozen 3D model processes equivalent inputs because its output frame rotates fractionally. This exposes a weakness of trainingfree perturbation uncertainty: when outputs contain an unobserved symmetry, run-to-run variation potentially reflects symmetry rather than error. Existing alternatives have trade-offs: built-in confidence is outperformed in most evaluated conditions, while trained evidential heads require modelspecific supervision. For point maps, this research derives a closed-form, error-independent variance term that grows with scene extent and potentially overwhelms the desired signal. Simulation reproduces the effect; all 30 real VGGT view-sets tested exhibit its predicted $\|x_p\|^2$ signature. ReVar3R robustly registers predictions to a common similarity frame before computing per-point variance, without retraining or modifying the frozen model. Optional calibration and fusion use a held-out split. Across VGGT, {\pi}3, and MASt3R on six datasets, the same estimator on every backbone lowers AUSE below built-in confidence in 15 of 18 conditions. The staged evaluation yields 11 of 18 wins for the label-free core, 12/18 for label-free equal-weight fusion, 14/18 with held-out weights, and 15/18 when the built-in signal is included. Against a trained evidential head, the result is a trade-off: the head calibrates magnitude better and leads in its training domain, whereas ReVar3R transfers across backbones without adaptation. Its ranking improves point filtering, but it does not detect stable systematic bias, aid novel-view synthesis, or transfer calibration across domains.

---


### 197. [Label-Efficient Deep Learning for ECG Delineation: A Multi-Dataset Benchmark against Widely Used Delineation Tools](https://arxiv.org/abs/2610.07885)

**<font color=#1a73e8>作者：</font>** Jeonghwa Lim, Minje Park, Yeongyeon Na 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) delineation, the identification of waveform boundaries, is a foundational step that translates raw ECG signals into clinically interpretable measurements. Deep learning has advanced this task but remains dependent on costly expert annotations. Label-efficient strategies such as self-supervised pretraining and semi-supervised learning are expected to ease this burden, yet it remains unclear whether they yield reliable delineation and whether the deep models they produce outperform the delineation tools used in practice. We address this in two stages. First, comparing self-supervised objectives with supervised or semi-supervised fine-tuning across one internal and four external datasets, we find that pretraining helps but the objective matters, and that the value of semi-supervised fine-tuning depends on the pretraining objective. Second, we benchmark the selected deep learning model against widely used open-source (NeuroKit2, Prominence, ECGdeli) and commercial (CalECG) tools using three complementary metrics. The model ranks best on every metric and dataset, outperforming the strongest tool by a clear margin on the rhythm-diverse set (mIoU 71.3 vs. 54.8%; averaged point-wise sensitivity 92.6 vs. 76.4%), and degrades the least from sinus to arrhythmia. A rhythm-stratified and point-wise analysis further characterizes the distinctive behavior of each tool, yielding practical guidance for tool selection. These results provide systematic, multi-dataset evidence that self-supervised pretraining is effective for ECG delineation and enables a label-efficiently trained deep learning model to outperform widely used delineation tools by leveraging abundant unlabeled data. This supports adopting such models in diverse, real-world clinical settings.

---


### 198. [Visual Abstention in Unified Multimodal Models](https://arxiv.org/abs/2610.07887)

**<font color=#1a73e8>作者：</font>** Chufan Shi, Cheng Yang, Tiannuo Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) integrate understanding and generation, yet their generative behavior is rarely governed by what they understand about the task. We formalize visual abstention: when a requested visual transformation is impossible under the task's rules, the model should recognize that no valid solution exists, state this, and decline to generate. We introduce Draw-or-Decline (DoD), a benchmark of 1,050 feasible-infeasible request pairs across 7 task categories that jointly measures editing success and the refusal of infeasible requests. Evaluating 8 UMMs, we find that editing ability and abstention are distinct capabilities: even the strongest editor, at 68.4% editing accuracy, refuses only 0.4% of infeasible requests under ordinary instructions. Their reasoning shows why: the models rarely notice the conflict, and instead plan the edit as if the request were possible, often describing objects that are not in the image, or quietly change the request into one they can complete. Explicitly prompting these UMMs to report infeasibility increases textual refusals but reduces editing accuracy. We propose VisTA (Visual Transformation and Abstention), a training method that pairs feasible and infeasible examples so that a model judges feasibility before deciding whether to generate. We train VisTA-BAGEL to perform feasible edits and decline infeasible requests. Without any reminder, it refuses 93.0% of infeasible requests, up from 0.4% for the strongest editor, while falsely refusing only 0.8% of feasible ones. Unlike a reminder, this does not cost editing accuracy: VisTA-BAGEL completes 74.3% of feasible edits, more than any of the 8 evaluated UMMs.

---


### 199. [Variance-Averse $n$-Step Offline Reinforcement Learning for Sparse Long-Horizon Environments](https://arxiv.org/abs/2610.07899)

**<font color=#1a73e8>作者：</font>** Guhyeon Kang, Minhae Kwon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative actors are transforming offline reinforcement learning (RL) by enabling expressive policy classes that model complex action distributions. However, this expressiveness also exposes a key challenge in heterogeneous datasets: generative policies can reproduce unreliable action modes whose return distributions exhibit high variance, occasionally yielding high returns by chance but lacking consistency. Consequently, maximizing the expected $Q$-value alone is insufficient for identifying reliable actions. We propose VAN-Flow (Variance-Averse $n$-step Flow), a framework that promotes reliable actions in generative offline RL. VAN-Flow combines (i) a categorical distributional critic, (ii) a variance-averse expectation operator that smoothly reweights atom probabilities to favor actions with both high returns and low dispersion, and (iii) a flow-matching generative actor guided via rejection sampling. Unlike CVaR or mean-variance objectives, the operator redistributes probability mass over the categorical return distribution without hard truncation or auxiliary penalty terms. Across more than 40 tasks from D4RL and OGBench, VAN-Flow consistently outperforms strong baselines, with the largest gains in long-horizon and high-variance regimes where reliable action selection becomes critical.

---


### 200. [ARIA: Audio-Driven Melody-Tone Relation Modeling for Cantonese Lyric Authoring](https://arxiv.org/abs/2610.07902)

**<font color=#1a73e8>作者：</font>** Shengyu Li, Jinting Wang, Li Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cantonese lyric writing requires close alignment between lexical tones and melodic pitch. Existing melody-guided lyric generation methods typically rely on symbolic melody to generate lyrics. However, in real songwriting scenarios, melodies are often expressed as raw singing audio or hummed recordings, where pitch is implicit, noisy, and unstructured, making these methods difficult to apply directly. To address this limitation, we propose ARIA, a two-stage audio-driven melody-tone relation modeling framework for Cantonese lyric authoring that generates Cantonese lyrics from singing recordings with provided character-level timestamps. Specifically, we first design a Tri-Stream Relation-Aware Tone Estimator (TRATE) to predict 0243 sequences from timestamped singing audio by modeling multi-stream acoustic cues and relational tonal structure. We then propose a Decoupled Retrieval-Augmented Tone-Conditioned Lyric Generator (DRA-TCLG) to generate fluent lyrics conditioned on predicted tonal plans with retrieval-enhanced lexical guidance. Moreover, we construct a large-scale aligned audio-Jyutping-0243 dataset from real Cantonese singing recordings to support this new task. Experimental results demonstrate that ARIA achieves strong performance in both 0243 prediction and tone-consistent lyric generation, validating the effectiveness of the proposed framework.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-335](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
