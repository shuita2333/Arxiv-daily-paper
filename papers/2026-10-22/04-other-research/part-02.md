# 📦 其他研究 | 2026年10月22日

> 本类共 **288** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

---

### 51. [Model Exposure on One Device Endangers Others: Rethinking Edge Neural Network Security across Devices](https://arxiv.org/abs/2610.27152)

**<font color=#1a73e8>作者：</font>** Yuyang Zhang, Kangjie Chen, Yihui Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neural networks (NNs) are increasingly deployed on edge devices such as mobile and IoT platforms, offering low latency and improved privacy compared to cloud-based deployment. However, on-device models embedded in mobile applications can be unpacked and exposed to adversaries, enabling cross-node attacks in centrally distributed ecosystems, where adversarial examples crafted on one compromised device transfer effectively to other nodes sharing the same models. To address this threat, we propose VeilNN, a defense framework that reduces adversarial transferability across on-device models via model obfuscation. The core idea of VeilNN is to introduce controlled model diversity while preserving original task functionality. Specifically, VeilNN applies stealthy and irreversible obfuscation at both the architectural and parameter levels through network cell obfuscation and layer assembling, and is applicable to diverse NN architectures, including MLPs, CNNs, and Vision Transformers. Extensive experiments demonstrate that VeilNN effectively defends against cross-node attacks, achieving an average defense success of 49.19% and up to 81.19% across four adversarial attack types, with more than 33.16% improvement over existing defenses.

---


### 52. [A Hybrid TFT-NBEATS Framework for Robust Multi-Horizon Photovoltaic Power Forecasting](https://arxiv.org/abs/2610.27155)

**<font color=#1a73e8>作者：</font>** Shafi Bin Sultan, Sabik Bin Sultan, Mohammad Tajrian Arafat Alvi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate multi-horizon photovoltaic (PV) power forecasting is essential for grid stability, energy scheduling, and the efficient operation of PVbatterygrid systems. However, existing models often fail to jointly capture short-term variability and long-term temporal patterns, while lacking unified multi-horizon capability and interpretability. To address these limitations, this study proposes a novel hybrid deep learning framework that integrates a Temporal Fusion Transformer (TFT) and N-BEATS within an attention-based fusion architecture. The proposed model leverages TFT to learn short-term temporal dependencies and dynamic feature importance, while N-BEATS captures long-term trend and seasonal components through interpretable basis decomposition. An adaptive attention mechanism dynamically fuses both branches, enabling balanced multi-scale learning. The framework simultaneously generates forecasts for 30-minute, 2-hour, 6-hour, 12-hour, and 24-hour horizons within a single unified pipeline. The model is evaluated using multi-year real-world datasets from the Desert Knowledge Australia Solar Centre (DKASC). Experimental results demonstrate superior performance over statistical, machine learning, and deep learning baselines. The proposed model achieves RMSE values of 42.35, 46.27, 52.29, and 48.11 across the 20162017, 2023, 2024, and 20252026 datasets, respectively, corresponding to a 3540% reduction compared to the best baseline (TFT). Additionally, MAPE remains below 5% across all datasets, indicating high predictive accuracy and stability. The model also provides interpretability through attention visualization and trendseasonality decomposition, and is deployed on a cloud-based platform for real-time forecasting. These results demonstrate that the proposed framework is robust, interpretable, and suitable for practical renewable energy applications.

---


### 53. [MoSAIK: Motion Search with Artificial Intelligence in K-space](https://arxiv.org/abs/2610.27156)

**<font color=#1a73e8>作者：</font>** Oscar Dabrowski, Abijith Jagannath, Frédéric Grouiller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Object:
Motion artefacts remain a major limitation of routine two-dimensional T2-weighted turbo spin-echo (TSE) brain MRI, reducing diagnostic confidence and often necessitating repeated acquisitions. MoSAIK (Motion Search with AI in K-space) retrospectively estimates in-plane rigid-body motion directly from standard multi-coil TSE k-space. Without a motion-free reference, external navigators, or additional acquisitions, MoSAIK infers motion from k-space self-consistency violations and incorporates predicted parameters into model-based, motion-aware reconstruction rather than synthesizing corrected images.
Materials and Methods:
Selected complex coil data were represented as log-magnitude and phase channels. A decoupled convolutional embedding and Transformer encoder estimated phase-encoding-line-indexed rotation and two-dimensional translations. Training used motion-free clinical acquisitions with simulated motion; four held-out subjects were evaluated. Component-wise errors assessed estimation; SSIM and PSNR in silico and entropy focus criterion (EFC) in vivo assessed reconstruction.
Results:
Motion estimation errors were low for both rotation (MSE $<$ 0.2 deg$^2$) and translation (MSE $<$ 0.2 pixels$^2$), with Pearson correlations of approximately 0.96 and 0.94, respectively. In every in-vivo acquisition, more than 75% of slices showed information gain relative to uncorrected reconstructions. MoSAIK reduced visible artefacts while preserving anatomical detail.
Discussion:
Transformer-based k-space motion-trajectory estimation enables fast retrospective correction of standard clinical TSE brain MRI.

---


### 54. [Learned Control Variates for Rare Grid-Outage Estimation at Electric Vehicle Charging Stations](https://arxiv.org/abs/2610.27159)

**<font color=#1a73e8>作者：</font>** Sulyman Iyanda, Mansur Arief  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public charging of electric vehicles (EVs) adds a large and synchronized load to the distribution feeders. In most networks, it is rare to overload a feeder at the same time. When it does happen, the consequences can be severe: an overloaded feeder stresses its transformers and can trigger cascading outages across a city. Planners who design for high reliability therefore need to estimate very small outage probabilities. To that end, plain Monte Carlo estimation with an expensive grid simulator can require a prohibitively large number of runs for this task. To reduce the number of runs, we propose a control variate (CV) built from a learned classifier of the outage, trained on cheap observable features such as temperature and load forecasts. We show that for any binary learner, the variance reduction is an explicit function of its recall and false-positive rate. Furthermore, we show that control variate based on a Gaussian proxy of the load loses its effect as outages become rarer, while a learner with non-vanishing precision keeps removing a fixed fraction of the variance even in the extreme rare-event regime. We verify these results in numerical experiments using a feeder-overload simulator across three orders of magnitude of outage probability and obtain that even weak learner with a single feature can remove a quarter of the variance, while a boosted-tree learner is able to remove about 60%. We then apply the estimator to the feeder network of Surabaya, Indonesia, in which the Gaussian load model leaves every feeder three to seven times the one-day-in-ten-years blackout target. At the same simulation budget, planning the reserve with the learned CV and a 95% confidence limit reduces the city-wide blackout days by a third compared with Monte Carlo. These results show that learned control variates can help planners design distribution grids that stay reliable against rare outages.

---


### 55. [Too Long to Watch, Too Short to Leave: Designing for Agent Micro-Waits](https://arxiv.org/abs/2610.27170)

**<font color=#1a73e8>作者：</font>** Kevin Pu, Anh Truong, Michael Terry 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly carry out complex work, where a single turn routinely runs for minutes. This produces a micro-wait that is too long to watch and too short to leave. In a formative study with 12 daily agent users, we found that staying felt like wasted time, while switching away fragmented attention and forfeited the context needed to re-engage. We introduce Sidecar, a parallel assistant situated in the same interface as the agent, which reads the run and surfaces implicit decisions the agent made, along with task directions worth exploring. In a within-subjects study (N=16), Sidecar helped participants stay focused on their main task, freely workshop unfinished ideas without fear of unwanted action, and recognize under-specification in their own prompts. Together, these findings contribute to designs that help users stay context-aware and engaged during agent micro-waits.

---


### 56. [CanvasObs: Structured Spatial Observation for Agent Editing on 2D Infinite Canvases](https://arxiv.org/abs/2610.27176)

**<font color=#1a73e8>作者：</font>** Jiahao Xu, Haohui Wang, Rebecca Faust 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Editing agents on 2D infinite canvases must reason about application state that pixels may not reveal. Targets may be offscreen or covered, while visual containment and touching arrows may disagree with recorded frame membership or connector bindings. We ask how a structured observation layer can support accurate object selection during agentic editing on 2D infinite canvases. We present CanvasObs, which augments visual context with a structured payload and guidance for reading four components: Identity & State, Visibility & Structure, Relations, and Offscreen Object bounds in action coordinates. A Remote Team Handoff case study illustrates retrieving an editable offscreen copy, choosing a covered chart by color, separating cards by frame membership, and preserving an evidence connection. We turn these cases into ten controlled configurations and compare CanvasObs with the baseline agent in 1,200 browser trials across three models. CanvasObs improves Correct target for every model. Combined across models, it raises Correct target from 16.5% to 48.3%, an increase of 31.8 percentage points (95% confidence interval [29.0, 34.7]), and Full task success from 4.3% to 25.0%. These results show that compact structured observation can improve object choice on 2D infinite canvases without redesigning the editing pipeline.

---


### 57. [SITO: Sifting a Commercial Text-Safety API for Missed Harm and False Flags in English, Ukrainian and Surzhyk](https://arxiv.org/abs/2610.27178)

**<font color=#1a73e8>作者：</font>** Andrii Tuzhykov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Platforms that host young users screen messages with commercial text-safety APIs, but independent evidence on how often such systems miss harm or flag harmless text is scarce, especially outside English, and the documentation of the one studied here leaves its false-positive rate unquantified. We evaluated one such API, Tuteliq Detect as deployed under the release identifier tuteliq-detect-v5.20261011 (not the separately published v6 model), on six harm categories: authorised push-payment fraud, money-mule recruitment, social engineering, romance scams, gambling harm and bullying. We built SITO (Synthetic Independent Text-safety benchmark with Overflagging tests; sito is Ukrainian for 'sieve'), 2,332 synthetic cases in English, Ukrainian and mixed Ukrainian, with each harmful case matched by hard harmless ones: same-topic messages, minimal-edit contrasts, warnings and retrospective accounts. On English text the system flagged 84.9-94.1% of harmful cases and 0-4.3% of harmless ones per category. It missed third-party reports of ongoing harm far more often than perpetrators' messages (63.6% against 95.1% recall, all languages), when sent without the settings the API offers for reports of harm. Ukrainian and mixed-language input was detected at least as often as English, recall was lower on text from a held-out generator family, so headline recall may be optimistic, and 3.2% of cases received a different decision in repeated runs. A platform should measure false positives on its own traffic and check how bystander reports are handled. The datasets, generation prompts and code are released.

---


### 58. [Meta-iLaD: Identifiable Latent Dynamics via Meta-Learning of Dynamics Environments](https://arxiv.org/abs/2610.27180)

**<font color=#1a73e8>作者：</font>** Yubo Ye, Sweekar Piya, Xiajun Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning latent dynamics is central to assessing the current states and forecasting the future trajectories of high-dimensional time series. For locally-stationary latent dynamics $\mathcal{F}(\mathbf{z}_{<t}; \mathbf{c})$ with latent dynamics state $\mathbf{z}_t$ and environment variable $\mathbf{c}$, prior identifiability results have largely focused on $\mathbf{z}_t$ when conditioned on predefined label $u$ of dynamics environments. This leaves two limitations: reliance on predefined labels that hinder generalization to unseen environments, and a limited understanding of the identifiability of $\mathcal{F}$ and $\mathbf{c}$ which -- although offering important structural properties for the identifiability of $\mathbf{z}_t$ -- are learned jointly with $\mathbf{z}_t$. We address these limitations with Meta-iLaD, a novel identifiable latent dynamics framework attained by meta-learning across dynamics environments. Meta-iLaD introduces a novel conditional prior of $\mathbf{c}$, modeled as a feedforward meta-learner to rapidly extract $\mathbf{c}$ from few-shot examples. Meta-iLaD further establishes identifiability for $\mathbf{z}_t$, $\mathbf{c}$, and $\mathcal{F}$ simultaneously, for a general formulation of $\mathcal{F}(\mathbf{z}_{< t};\mathbf{c})$ without restricting the dimension of $\mathbf{c}$ or how it modulates $\mathcal{F}$. On synthetic and real data, we provide strong empirical evidence that 1) conditioning on few-shot examples enables generalization to out-of-distribution environments, and 2) identifiability for $\mathbf{c}$ and $\mathcal{F}$ is critical for accurate forecasting beyond reconstructing observed trajectories. Code is available at this https URL.

---


### 59. [LSA-PAST: Layer-Specific Adaptation and Prototype Transport for Compositional Incremental Learning](https://arxiv.org/abs/2610.27203)

**<font color=#1a73e8>作者：</font>** Kyle Stein, Andrew Arash Mahyari, Guillermo Francia III 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Learning (CIL) enables models to recognize new classes over time while retaining prior knowledge, but many real-world problems are compositional, where visual concepts arise from combinations of primitives such as states (i.e., red, shiny) and objects (i.e., shoe, car). Standard CIL methods treat each composition as an independent class, ignoring shared primitives and providing no mechanism to stabilize their representations as new compositions arrive. This causes parameter updates to entangle primitives and induce drift that degrades performance on earlier compositions. Compositional Incremental Learning (composition-IL) formalizes this setting by introducing new state-object compositions across tasks. In this paper, we propose Layer-Specific Adaptation with Prototype-Anchored Adapter-Space Transport (LSA-PAST), a parameter-efficient method tailored to composition-IL. LSA integrates Low-Rank Adaptation (LoRA) into a frozen ViT with depth-specialized adapters for states, objects, and compositions. PAST then maps past, anchored prototypes into the current adapter space through a rehearsal-free affine transform fit on current-task data, enabling old prototypes to remain compatible with new adapters. Extensive experiments demonstrate that LSA-PAST achieves state-of-the-art (SOA) accuracy-forgetting trade-off performance for composition-IL.

---


### 60. [A Combined Streaming FPGA Architecture for Client-Side CKKS Encoding and Encryption](https://arxiv.org/abs/2610.27204)

**<font color=#1a73e8>作者：</font>** Joseph Kurina, Bogdan Pasca, Suleyman Demirsoy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Homomorphic encryption allows a computing service to process encrypted data, but the client must first encode and encrypt its inputs. Sharing hardware between floating-point encoding and modular encryption reduces area but requires those transform roles to execute at different times. We present a streaming FPGA architecture for CKKS encoding and encryption that computes the shared floating-point encoding transform once and performs the integer transforms for six residue moduli in parallel. Dedicated transform pipelines exchange intermediate results on chip rather than through off-chip memory. DSP Builder generates the transform RTL, and Altera HLS IP Gen compiler compiles the surrounding SYCL pipeline into IP integrated with DMA and control logic in an accelerator functional unit. At polynomial degree N = 8192, the Altera Agilex 7 implementation delivers 5,143 complete ciphertexts per second at 471 MHz. One SEAL-Embedded CPU worker on the same workstation delivers 113 ciphertexts per second for real-valued inputs using all 4,096 slots. Measurements cover prepared-input computation through complete ciphertext construction, including FPGA submission and output delivery.

---


### 61. [LoWAgent: A Low-Resource Multilingual Benchmark for Web Agents](https://arxiv.org/abs/2610.27205)

**<font color=#1a73e8>作者：</font>** Ocean Monjur, Daud Ahmad Nisar, Shahriar Kabir Nahin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents are typically evaluated on English-language interfaces, leaving their ability to operate across the world's multilingual websites largely unexplored. This gap is especially significant for low-resource languages, where standardized resources for evaluating web agents remain limited. To address this gap, we introduce Low-Resource Web Agent Benchmark (LoWAgent), a benchmark for evaluating web agents across different low-resource languages (LRLs) in comparison to the default, English. LoWAgent evaluates web agents across English and four LRLs: Hindi, Bengali, Urdu, and Amharic. The benchmark comprises of six fully localized websites, instantiated across five languages to yield 3,000 task instances. We evaluate three closed-source and five open-source models across all five languages on all six websites. Our findings show that both closed-source and open-source models experience performance degradation for LRLs compared to English, with substantially greater performance drops observed among the open-source model agents. We further evaluate the robustness of the models on realistic interface disruptions, such as cookie notices and advertisement pop-ups, and find that these further degrade agentic performance. Finally, we show that post-training on a small subset of LoWAgent traces can significantly improve low-resource language agentic task performance, demonstrating the usefulness of our benchmark.

---


### 62. [Deep catastrophic-risk-aware reinforcement learning](https://arxiv.org/abs/2610.27214)

**<font color=#1a73e8>作者：</font>** Carlos Pérez Octavio Mendoza, Frédéric Godin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating extreme risk in reinforcement learning becomes increasingly difficult as the confidence level increases, since only a small number of observations contribute to empirical estimates of Conditional Value-at-Risk (CVaR). In this paper, we extend an Extreme Value Theory (EVT) approach for CVaR optimization to high-dimensional neural-network policies. Using a peaks-over-threshold representation and method-of-moments estimation, we obtain a differentiable tail-risk objective and show that, conditional on the selected threshold, its finite-sample gradient can be computed directly through automatic differentiation. We first validate the approach in a controlled experiment with a known optimal solution and then investigate its performance in a deep-hedging problem with rare extreme market movements. Our results show similar hedging behavior for EVT- and empirical-CVaR-trained policies under normal conditions, while EVT-trained policies exhibit lower hedging losses under the extreme-scenario evaluation across the training sample sizes considered. These results suggest that EVT can provide a practical alternative for training neural policies when the observations relevant to extreme risk are scarce.

---


### 63. [MMedAgent-Plus: Scaling Multimodal Medical Agents across Modalities, Tasks and Workflows](https://arxiv.org/abs/2610.27233)

**<font color=#1a73e8>作者：</font>** Ruoxin Wang, Yuanting Pan, Binxu Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical workflows often require multiple interdependent analyses, but existing specialist and generalist AI models are not designed to coordinate them. We introduce MMedAgent-Plus, a multimodal medical tool-use agent that combines a vision-language planner with 18 leading specialist models spanning 12 tasks and 8 modalities. Through a unified tool interface, the planner selects specialists, executes them in sequence, and synthesizes responses grounded in their outputs. The planner is instruction-tuned on 208,928 samples from 32 public medical benchmarks, covering single- and multi-tool interactions across single and multiple rounds. We separately evaluate tool orchestration, response synthesis, and end-to-end execution on held-out samples. MMedAgent-Plus achieves tool-call accuracies of 91.0%, 98.1%, and 80.7% in single-tool multi-round, multi-tool multi-round, and multi-tool single-round settings, respectively. Given correct tool outputs, MMedAgent-Plus achieves scores of 14.4-14.8 out of 15 for faithfulness, completeness, and conciseness across 600 evaluation samples. In end-to-end execution without pre-supplied tool outputs, MMedAgent-Plus correctly invokes the required specialist in 90.6% of 350 evaluation cases spanning seven tasks. Its final-answer accuracy reaches 0.98, matching the dedicated leading specialist and exceeding the strongest baseline (0.28).

---


### 64. [CEFR-oriented Russian Text Simplification Using Reinforcement Learning](https://arxiv.org/abs/2610.27237)

**<font color=#1a73e8>作者：</font>** Kristina Mustakova, Alexey Sorokin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a study on controlled automatic simplification of Russian texts using preference-based optimization algorithms with a focus on adapting texts to the A1, A2 and B1 proficiency levels. We fine-tune YandexGPT using Rejection Sampling and Direct Preference Optimization (DPO) methods to improve control over the complexity of the generated text. We compare several training configurations that differ in dataset composition, text type and the strategy used to construct preference pairs for DPO. For automatic evaluation we train a regression model based on ruRoBERTa-large to predict continuous complexity scores corresponding to CEFR levels. We also consider semantic similarity, lexical coverage and quantitative readability metrics. Human evaluation assesses simplicity, fluency and adequacy. Our best model achieves 87.15\% target level accuracy, an MAE of 0.35 CEFR levels and a target interval MAE of 0.11. Manual assessment shows that 75% of the evaluated simplifications match the target morphological and syntactic level, and fluency and adequacy scores are especially high for A2 and B1. Although A1 remains the most challenging level, the model significantly reduces the proportion of vocabulary and grammatical constructions beyond the target level while generally preserving meaning. Our model is freely available on $\href{this https URL}{HuggingFace}$.

---


### 65. ["It Wouldn't Have Been So Apparent to Me": Evaluating How Thought-Level Progress Tracking Supports Psychosocial Goals](https://arxiv.org/abs/2610.27238)

**<font color=#1a73e8>作者：</font>** Shiyu Xu, Ruishi Zou, Anna R. Van Meter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We pursue psychosocial goals every day, from coping with anxiety, to pursuing personal growth. While prior research has designed systems for tracking progress towards behavioral goals, fewer studies have focused on progress towards psychosocial goals - and the thinking changes people make to address them. As a first step, we present Thought-GPS, a system that visualizes potential markers of such thought-level progress in-the-moment as users interact with an AI-supported cognitive restructuring intervention. We evaluated Thought-GPS through a mixed-methods single-session study with 30 participants, comparing Thought-GPS with an active control condition without progress markers. We found preliminary evidence that participants using Thought-GPS reported greater clarity about how they might change to pursue their goals, stronger motivation to reflect on goal progress, and greater engagement in that reflection. Participants also reported that progress markers made subtle progress visible, helped them engage in deeper reflection, and connect conversational insights to their personal goals.

---


### 66. [AutoRedClaw: Automated Red-Teaming for Claw-Style Agents](https://arxiv.org/abs/2610.27244)

**<font color=#1a73e8>作者：</font>** Hao Li, Tongyan Hu, Weidi Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw. These claw-style agents maintain configuration files (e.g., this http URL), long-term memory, and reusable skills. Once poisoned, this persistent state is repeatedly reloaded into the agent's context, creating persistent threats across tasks and sessions. Existing security evaluation systems struggle to evaluate these complex claw-style systems since they rely heavily on manually constructed test cases and environments, which limits their scale and coverage; in addition, these manually designed cases quickly become outdated as agents evolve, and their evaluation settings leave a gap with how claw-style agents are deployed in practice. To address this, we introduce AutoRedClaw, an automated red-teaming framework that generates end-to-end attacks together with the environments needed to execute them. AutoRedClaw combines a strict quality-checking protocol with execution-based validation to ensure the correctness, realism, and effectiveness of generated samples, and adopts task-driven environment construction to keep costs low. To achieve broad coverage, it organizes generation along risk categories, attack strategies, attack stages, and attack surfaces, and uses experience-guided exploration to steer generation toward under-explored regions. AutoRedClaw achieves an effective attack rate above 30% at less than $0.10 per successful sample. From its outputs, we construct RedClaw-Bench, a 330-case benchmark that yields substantially higher attack success rates (ASRs) than AgentDojo, AgentDyn, and DTap. Across seven harnesses and four frontier models, most agent systems exceed 50% ASR, showing that our red-teaming pipeline provides a strong evaluation signal even for the most advanced agent systems. Our code and benchmark are released at this https URL.

---


### 67. [When Pebbles Are Not Atomic: A Polynomial Separation Between Pure and Entangled Pebbling](https://arxiv.org/abs/2610.27249)

**<font color=#1a73e8>作者：</font>** Piotr Marszalik  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph pebbling is the model in which the memory cost of memory-hard functions and proofs of space is measured, and pebbling lower bounds are the main way to argue that such constructions are secure. It has long seemed that the model is faithful to reality. It is known that it is not exact: an adversary who stores encoded information instead of whole values can do better, but so far only by small factors: a factor of 1.5 in the work that introduced entangled pebbling (Alwen, Chen, Kamath, Kolmogorov, Pietrzak and Tessaro) and, recently, a factor of about log n/log log n (de Rezende, Engström and Reyzin). One could still hope that pebbling is right up to such small factors.
In pure pebbling, memory consists of whole labels; entangled pebbling also allows encoded state, such as XORs of labels. We show that the two models can differ polynomially. We study the setting in which proofs of space and data-dependent memory-hard functions are used: a state is prepared in advance, a random challenge has to be answered from it, and memory is paid for as long as it is held. Our graphs are explicit and have indegree two, and on them a pure adversary can do no better, up to a constant factor, than storing every possible answer in advance. Still, an adversary who keeps XORs instead of labels pays polynomially less. This ends the hope that pure pebbling is a faithful model of memory up to small factors.
The heart of the paper is a simple combinatorial game, together with a special class of graphs found by Alon, Moitra and Sudakov.

---


### 68. [The Differential Effects of AI Abstention on Advice Acceptance](https://arxiv.org/abs/2610.27258)

**<font color=#1a73e8>作者：</font>** Nicholas Wolczynski, Yotam Liel, Maytal Saar-Tsechansky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI advising systems are typically designed to always provide a response. Recent work has focused on developing systems that withhold advice in some instances, such as when advice quality is questionable, to improve the overall quality of guidance when it is given; a design paradigm we refer to as AI abstention. While substantial work has focused on optimizing when models should abstain, little is known about how users respond to systems that abstain. In a preregistered experiment, participants made repeated financial decisions, assisted by one of two advising regimes: an AI that advises selectively or one that advises on every decision. We find that the same AI abstention regime produces differential effects depending on the user: it increases advice acceptance among users with high perceived expertise and tends to decrease it among users with low perceived expertise. This differential effect is accounted for by the cognitive burden users face when repeatedly reconciling AI recommendations with their own judgment; AI abstention appears to relieve this burden among users with high perceived expertise, and in doing so increases their receptivity to advice. Further, AI abstention mitigates the decline in advice acceptance observed among expert users over repeated interactions. Exploratory evidence also suggests it increases appropriate acceptance where advice would improve the decision, increasing the downstream accuracy of perceived experts. The AI abstention regime is thus a first-order design property of AI advisory systems, and one that must be calibrated to the users a system serves.

---


### 69. [Solving the Ho--Nguyen Conjecture for Gaussian Mixtures: Applications to Mixtures of Experts](https://arxiv.org/abs/2610.27265)

**<font color=#1a73e8>作者：</font>** Yuyang Zhang, Qihuang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over-fitted Gaussian mixtures can contain many parameter configurations with nearly the same density, making the order of density cancellation central to their parameter-learning rates. Ho and Nguyen encoded these cancellations in a polynomial system and conjectured its exact order as a function of cluster size. The key to resolving the conjecture is a common positive-variance shift that turns the coefficient equations into Gaussian moment matching. For every cluster size $\Mhn\ge2$, we prove that the real, nonzero-weight system has order $2\Mhn$: a sharp sign-change bound forces rigidity at that order, while positive Gauss--Hermite quadrature constructs a non-trivial solution through order $2\Mhn-1$. Population-density calculations at 110-digit working precision recover the predicted leading term for two to six components; finite multistart searches recover the same observed powers for two to five components, with smaller finite-scale constants for three to five components. For parameter learning, the exact order gives an explicit pointwise maximum-likelihood exponent and an exact local minimax order on specified shrinking neighbourhoods of a fixed known mixing measure. The same coefficient viewpoint separates high-order cancellation from exact parameter symmetries in mixtures of experts. Synchronized replication preserves the conditional density while keeping the corresponding parameter losses positive in two broad standard-softmax classes, showing why statistical rate arguments must account for exact parameter symmetries.

---


### 70. [A latent control model for realistic rodent motion](https://arxiv.org/abs/2610.27279)

**<font color=#1a73e8>作者：</font>** Aidan Sirbu, Charles Y. Zhang, Yuanjia Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The development of embodied models of animal behavior is a major goal of the neuro-AI community. Embodied models will enhance our ability to make direct comparisons between biological and artificial agents. To make such comparisons effective, though, we need embodied models that actually move like animals. Previous work has developed virtual animal bodies and techniques for training realistic motion through imitation. However, to date, there is no system for embodied animal modeling that produces natural movements both during trained goal-directed behavior, and during exploration driven by random generation. Here, we introduce Simulated Control via Augmented Motor Priors for Embodied Reinforcement learning (SCAMPER), a system for training an embodied virtual rat model, enabling natural movements during both goal-directed behavior and random exploration. SCAMPER uses a variational architecture with two distinct priors, a motion prior for control and a behavior prior for exploration. We show that combining both of these priors allows SCAMPER to generate realistic behavior during exploration and exploit the task structure effectively. SCAMPER can also learn from sparse rewards as a result of the diverse movements induced by the behavior prior, allowing the system to model realistic sparse-reward tasks from experimental neuroscience. Altogether, SCAMPER provides the neuro-AI community with an effective new system for training embodied models of rodents on realistic tasks.

---


### 71. [VPFlow: Value-Predictive Planning with Imperfect World Models for Offline Goal Reaching](https://arxiv.org/abs/2610.27280)

**<font color=#1a73e8>作者：</font>** Yunzhe Hu, Dong Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline goal-conditioned reinforcement learning enables skill acquisition by reaching any goal from any state without dense rewards. Model-based methods allow for planning by scaling test-time compute to solve complex tasks. Combining both holds appealing promise for pre-training on suboptimal demonstrations and zero-shot adaptation via goal specification and planning. Yet existing methods assume effective planning requires accurate next-state prediction in pixel or latent space. In this work, we show that value prediction is more useful for planning, whereas accurate state prediction is often unnecessary. Our key insight is that offline goal reaching naturally admits a closed-form Monte Carlo return, enabling value regression to replace temporal-difference bootstrapping. We use this return as the sole supervision for latent world models: imagined latents are trained to predict goal-reaching value rather than match future states, implicitly preventing representation collapse. These planning-oriented representations let imperfect world models imagine on the level sets of value field beyond dataset transitions. We then present VPFlow, a value-predictive planner that pairs the world models with a one-step flow policy and plans in its noise space via evolutionary search. It enables policy improvement with imagined generalized advantage and reduces out-of-distribution queries common in action-space planning. On 30 state and pixel OGBench datasets, VPFlow surpasses model-free baselines by at least 30.3 and 10.1 percentage points in success rate, respectively, and outperforms latent planners LeWorldModel, PLDM, and TD-MPC2. It achieves this despite a latent prediction error orders of magnitude larger than with state prediction, while minimizing this error lowers success rate. This demonstrates that value-predictive representations, not exact state prediction, are what offline planning requires.

---


### 72. [When Does Hate Transfer? A Large-Scale Study of Cross-Lingual Hate Speech Detection](https://arxiv.org/abs/2610.27285)

**<font color=#1a73e8>作者：</font>** Zahra Bokaei, Walid Magdy, Bonnie Webber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective detection of hate content is essential for maintaining healthy online communities, yet performance can vary substantially across languages. This work investigates a core practical question: Can training data from one language support hate-speech detection in another language with comparable performance? To answer this question, we conduct a large-scale study across 14 languages. \change{We observe consistent patterns in which certain language pairs transfer more effectively than others. Among the factors we measure, linguistic similarity is the strongest predictor of these patterns, with temporal overlap and dataset-size difference playing smaller roles. These measurable factors do not fully explain the observed patterns; a complementary qualitative analysis suggests that shared cultural cues and communicative norms may be associated with some of the remaining cases, particularly within several clusters. We present this cultural interpretation as a hypothesis from qualitative inspection rather than a measured cause.}{} Our analysis includes low-resource languages, offering practical insights into when cross-lingual transfer can support them and where its limitations emerge. These findings inform the design of more reliable multilingual hate-detection systems.

---


### 73. [Vulnerability Analysis for Safe Multi-Agent Reinforcement](https://arxiv.org/abs/2610.27293)

**<font color=#1a73e8>作者：</font>** Taozheng Zhu, Shixiong Jiang, Fanxin Kong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safe Multi-Agent Reinforcement Learning (SMARL) aims to learn cooperative control policies under prescribed safety constraints. Al- though existing SMARL methods focus on enforcing safety during policy optimization, their vulnerability remains largely unexplored. This paper investigates inference-time observation attacks against SMARL, where an adversary perturbs the observations of a subset of agents, thereby altering the actions produced by their policies. We propose MinMax Attack, an attack framework that jointly selects adversarial target actions for compromised agents while accounting for the Cooperative Resistance of benign agents. We further derive a bound on the induced safety cost and characterize its relation- ship with the Compromised-Agent Budget and the Perturbation Budget. Experiments across multiple safety-critical multi-agent benchmarks and representative state-of-the-art SMARL algorithms show that MinMax Attack induces substantially higher safety costs than existing attack baselines while preserving task reward, thereby reducing its detectability and achieving both attack effectiveness and stealthiness.

---


### 74. [Generalizing Multimodal Foundational Models in Context-Driven Class Incremental Learning](https://arxiv.org/abs/2610.27298)

**<font color=#1a73e8>作者：</font>** Avi Gupta, Nilotpal Sinha, Vishnu Raj 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Learning (CIL) aims to learn new classes continuously without forgetting the previously learned ones. Recent works in CIL have significantly advanced across various modalities; however, at the intersection of audio-visual modality, this problem remains underexplored. While representations from multimodal foundational models (MFMs) encapsulate rich static priors, our preliminary analysis shows that these representations struggle in incremental settings. Motivated by this, we propose a framework that generalizes frozen MFMs to audio-visual CIL. Specifically, we leverage their dense audio and visual representations and employ an attention-based contextual guidance module, in which the audio representations serve as task-stable contextual guidance for the visual representations, enabling effective class recognition in the incremental setting. To further mitigate catastrophic forgetting and preserve stability across tasks, we employ feature- and logit-level distillation, which are primarily responsible for the reduced forgetting. Extensive evaluations across various audio-visual CIL benchmarks demonstrate that our approach consistently outperforms state-of-the-art methods. Code is available at this https URL.

---


### 75. [When Does an Added Planning Capability Create Operational Value? An Observable Evidence Standard](https://arxiv.org/abs/2610.27305)

**<font color=#1a73e8>作者：</font>** Yihua Xu, Yan Lyu, Jize Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial artificial intelligence (AI) planning systems combine predictive models, optimization logic, controls, and governance rules, but improvement in the complete policy does not show whether one addition made an independent contribution or whether that contribution justifies its burden. We address this attribution problem with an observable evidence standard that separates opportunity to act, executed-plan change, operational consequence, equivalence, uncertainty, and operating scope. Using forecast-to-plan replay on Favorita, M5, and Walmart data, we apply the standard to heterogeneous planning additions. Three limits of single-indicator evaluation emerge. First, a composite policy can conceal negligible component contribution: one control changed only 15 of 681 executed plans. Second, changing execution does not guarantee stable benefit: the evaluated multi-period capability helped in several long-lead settings but was 7.6% more costly under tight capacity. Third, indirect evidence can prioritize review but cannot complete attribution. Independent runs produced different paths in 19 of 599 cases that a rule-based check predicted would be unchanged. Although a lower-cost diagnostic matched the full-evaluation winner in only 55.0% of cases, it selected an option within the $10^{-6}$ cost-equivalence tolerance in 79.5%; the remaining cases prevented the proxy from authorizing acceptance. These experiments establish capability-level contribution evidence; the organization completes the value decision by weighing it against implementation and sustaining burden. The resulting capability evidence record links the observations to validation, deployment scope, fallback, monitoring, redesign, and retirement decisions.

---


### 76. [What Not to Erase: Saliency-Constrained Augmentation for Low-Resource Handwritten Character Recognition](https://arxiv.org/abs/2610.27309)

**<font color=#1a73e8>作者：</font>** Paraskevi Platanou, John Pavlopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) and handwritten character recognition (HCR) in low-resource historical material collections often rely on data augmentation, yet augmentation strategies are typically evaluated almost exclusively through predictive accuracy. This leaves open whether a model's improved performance is accompanied by saliency stability. This question is important in low-resource historical HCR, where recognition is performed on variable and partially degraded letterforms and two models with similar predictive performance may differ in how consistently their saliency patterns respond to such variation. We therefore study saliency-guided augmentation as an explanation-aware strategy for low-resource HCR. Rather than treating saliency maps only as post-hoc interpretations, we use them to define augmentation variants that perturb, preserve, or constrain visually informative regions of character images. We compare classical document-style transformations, random lacunae, and several saliency-constrained lacuna variants. To evaluate the effect of augmentation beyond accuracy, we introduce the Explainability Consistency Index (ECI), a metric that quantifies the stability of saliency patterns under controlled perturbations. We find that saliency-constrained augmentation can improve recognition over classical augmentation, but no single saliency strategy is consistently best. The preferred form of the constraint varies with both architecture and corpus, indicating that saliency is better treated as a mechanism for controlling augmentation than as a fixed augmentation strategy. In some settings, saliency-constrained training improves explanation consistency even when predictive performance is similar. This shows that predictive metrics alone can obscure differences in model sensitivity under perturbation, motivating explanation consistency as a complementary evaluation dimension.

---


### 77. [Scrambled Multiply-with-Carry Pseudorandom Number Generators](https://arxiv.org/abs/2610.27313)

**<font color=#1a73e8>作者：</font>** Sebastiano Vigna  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multiply-with-carry (MWC) generators are very fast pseudorandom number generators whose quality depends on the choice of a multiplier, and is usually assessed by applying the spectral test to an associated multiplicative congruential generator. We show that the special form of the modulus imposes structural limitations on the lattice structure of every MWC generator, which the generalized MWC generators of Goresky and Klapper mitigate; in our tests, xoring each output with its carry removes them. Since these limitations make the usual worst-case criterion useless, we rank candidates by a weighted geometric mean of their figures of merit, which does not depend on their normalization, and suggest multipliers for generators with 64 to 256 bits of state. Along the way, we correct some errors in the literature. In the end, we propose MWC192X, a 64-bit generator with 192 bits of state that passes all tests we are aware of, and emits an output in half a nanosecond.

---


### 78. [Quantum-Seeded Distributed Post-Quantum Group Signatures for 5G V2X Communications](https://arxiv.org/abs/2610.27316)

**<font color=#1a73e8>作者：</font>** P. Blanco-Casal, P. Rejo-Iglesias, D. Cajaraville-Aboy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vehicle-to-Everything (V2X) communications rely on elliptic-curve signatures that a quantum adversary breaks and on pseudonym certificates whose anonymity rests on rotation rate, not cryptography. This work presents qDGSP, a post-quantum V2X infrastructure: a hash-based dynamic group signature scheme (DGSP, over SPHINCS+ and WOTS+) distributed between a central controller and roadside verifiers. Group keys derive deterministically from quantum key distribution (QKD) seeds served over the ETSI GS QKD 014 interface, so no group-signature secret crosses the classical channel. qDGSP-EA (Ephemeral Association) binds an ephemeral ML-DSA-65 key to one group signature per 5G cell: messages remain unlinkable across cells, linkable within one. On a testbed with emulated 5G links, median end-to-end latency stayed within the 100ms ETSI budget for every variant. The qDGSP-EA intra-cell DENM matched the NIST ML-DSA-65 baseline on the wire, and under load EA mode raised delivery from roughly 78% to 93%.

---


### 79. [VampPrior Unleashed](https://arxiv.org/abs/2610.27322)

**<font color=#1a73e8>作者：</font>** Andrew A. Stirn, Abhejit Rajagopal, David A. Knowles 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep latent variable models (DLVMs) underpin many modern analysis pipelines, for example in single-cell genomics, yet their prior distributions have received markedly little attention. The VampPrior approximates the optimal prior (the aggregate posterior) and often attains high model evidence. Here, we identify two key limitations of the VampPrior: it ties prior and posterior uncertainty to a single amortized covariance and clusters poorly due to its fixed uniform mixture weights. We unleash the VampPrior by decoupling its prior and posterior covariances, resolving the conflict of generating high prior and low posterior entropy with the same shared parameters and substantially improving model evidence. We then replace the uniform mixture with a Dirichlet process. When combined, our proposals provide higher model evidence than the VampPrior and robust non-parametric clustering. Augmenting single cell Variational Inference (scVI) with our prior improves single-cell integration and clustering across six atlases while significantly raising model evidence. Our approach changes only the prior and thus can be applied to any DLVM with a continuous latent space.

---


### 80. [Orchestrating Key Scarcity: Global Capacity Allocation in Hybrid QKD-PQC Networks](https://arxiv.org/abs/2610.27332)

**<font color=#1a73e8>作者：</font>** Pablo P. Rejo, Manuel Fernández-Veiga, Ana Fernández-Vilas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This article presents a Distributed Key Management System (DKMS) that provisions quantum-safe symmetric encryption keys to applications across a network. To overcome the distance and rate limitations inherent to Quantum Key Distribution (QKD), the architecture adopts a hybrid design: it utilizes multi-hop trusted relays for physical key transport, while applying an end-to-end Post-Quantum Cryptography (PQC) layer to ensure the relayed key material remains strictly protected from intermediate nodes. Because QKD transforms key generation into a scarce physical resource, managing unpredictable application demands poses a critical capacity allocation problem. The core contribution of this work is an SDN-driven control plane that globally orchestrates the network. Rather than relying on vulnerable hop-by-hop capacity reservations, a central controller simultaneously computes optimal filling rates and multipath routing for all per-peer key buffers. This global orchestration ensures that no application is starved and that all key buffers synchronize their filling processes. Evaluated on a Kubernetes-based digital twin across five distinct network topologies, the controller successfully filled all key buffers to capacity in under six minutes. Furthermore, under deliberately excessive demand, the network demonstrated graceful degradation, safely rejecting excess requests through controlled rate-limiting rather than experiencing catastrophic failure.

---


### 81. [Automated Brick Schema Knowledge Graph Completion Across Buildings](https://arxiv.org/abs/2610.27339)

**<font color=#1a73e8>作者：</font>** Daniel Ma, Jalil Huseynov, Xinyi Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Brick schema represents building equipment, sensors, spaces, and the relationships between them as typed, multi-relational graphs, providing machine-readable metadata that supports generalizable control applications. Current methods for producing complete Brick models require extensive manual examination of building schematics and point lists. We observe that as Brick models are knowledge graphs, inferring missing relations is naturally posed as a knowledge graph completion problem. To the best of our knowledge, this is the first application of knowledge graph completion to Brick model generation. We compare three methods, gradient-boosted trees, Pairwise Brick Relation Ranking, and CompGCN, on the relations feeds, hasPart, and hasPoint, which account for the majority of the schematic-reading work in building a Brick model by hand. Models are evaluated on held-out MORTAR buildings and out-of-distribution Kaggle and Building Time Series data. Although CompGCN is the strongest performer on held-out buildings under metrics resistant to class imbalance, leading macro-F1 and AUPRC, no method generalizes uniformly across datasets or relations.

---


### 82. [LiBRA: Logit Fingerprints for Byzantine-Robust Client Selection in Federated Learning](https://arxiv.org/abs/2610.27357)

**<font color=#1a73e8>作者：</font>** Saheed A. Tijani, Frank Jiang, Ming Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Byzantine-robust aggregation shields federated learning from malicious updates, but the rules that filter out suspect updates do so by comparing clients' parameter vectors. That comparison requires access to every client's update, which secure aggregation exists to withhold, costs $O(n^2 d)$ in the parameter dimension $d$, and is defined only between clients that share an architecture. We propose LiBRA, which compares clients on what their models compute rather than on the parameters that compute them, using a fingerprint of $C^2$ values for $C$ classes, the class-conditional logit response of each client's model to pseudo-patterns optimised against it. We instantiate LiBRA as variants of Krum, Multi-Krum and Bulyan that change only what the dissimilarity score is computed on. On Fashion-MNIST and CIFAR-10 with three architectures and four backdoor and label-manipulation attacks under i.i.d. partitions, each variant holds every attack its parent holds, and on identical client updates under a backdoor attack the fingerprint ranks malicious clients within 0.006 AUC of the full parameter vector. The variants thus match the robustness of the rules they extend, while their trust decision reads no client parameter, compares up to 49,090 times fewer values, and can by construction compare clients whose architectures differ, at the cost of one pattern optimisation per client per round.

---


### 83. [Predictive Closure: A Set-Level Characterization of JEPA's Feature Selection](https://arxiv.org/abs/2610.27364)

**<font color=#1a73e8>作者：</font>** Mosh Levy, Aly Lidayan, Yoav Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In joint-embedding predictive architectures (JEPA), an encoder and a predictor are trained together to produce a representation that minimizes the error in predicting the representation of the next observation. Because the representations of both the current and the next observation are learned, it is unclear which features they will include. Earlier characterizations describe the features JEPA selects in terms of their individual predictability, raising the concern that unpredictable features, like a traffic light, will not be encoded into the representation. However, the prediction error is also affected by the relationships between features, e.g., the light's color helps predict whether the traffic will stop. We propose the predictive closure characterization, which accounts for these relationships. Based on a reformulation of the JEPA training objective, we show that selection depends on properties of feature sets. This view agrees with earlier works when features evolve independently, but makes new predictions when they do not, for instance that a feature like the traffic light can still be retained. We test this characterization in controlled experiments, which show that unpredictable features can become better represented when they help predict other features, and that changing one feature's predictive relationships can affect how well others are represented. We also demonstrate implications for steering feature selection: targeting one feature with an auxiliary objective, or supplying it to the predictor as side information, can strengthen the representation of another feature whose future values it helps predict, so steering can be indirect.

---


### 84. [Trail-Weighted Influence Scores for Approximate Outcome Prediction in Bayesian Networks](https://arxiv.org/abs/2610.27366)

**<font color=#1a73e8>作者：</font>** Sahil Kumar Rajput, Randhir Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study trail-weighted pruning of evidence for Bayesian-network prediction. A traversal enumerates the active trails from each evidence node to the outcome, scores each trail by the product of its edge strengths, and drops evidence whose score falls below a threshold. For collider-free networks (chains and forks) over binary variables, we show that the trail score equals the exact correlation between a trail's endpoints, that a chain and a fork with equal edge strengths have identical joint distributions, and that the pruned posterior is within a computable sum of per-trail terms of the exact posterior when each dropped trail lies in its own branch of the outcome node. We prove this bound, check it exhaustively on all small trees, and show that it fails when dropped trails share a branch. In simulations on random trees, thresholding trail scores gives 1.4 to 13 times lower error than random pruning of the same size. We also apply the score, as an unproven heuristic, to seven bnlearn networks with colliders and loops. Keeping the top half of the active evidence by trail score gives lower error than random pruning on all seven, but it is not clearly better than a mutual-information ranking, and scoring costs more than the inference it saves on six of the seven, so we show no speedup. Models trained on trail, graph and information features and tested on networks they never saw do not beat the trail score or mutual information, but trail features carry most of what they use and clearly outperform generic graph features. A bound for general networks is left to future work.

---


### 85. [PerQ: Inverse Generative Modeling for Neural Image Compression via Quantization Error Compensation](https://arxiv.org/abs/2610.27374)

**<font color=#1a73e8>作者：</font>** Tianhao Peng, Ho Man Kwan, Fan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural image codecs face a fundamental trade-off between pixel fidelity and perceptual quality. Distortion-optimized codecs preserve pixel-wise fidelity but produce blurred reconstructions at low bitrates, whereas generative codecs leverage learned priors to improve perceptual quality but tend to exhibit saturating PSNR at higher bitrates and require separate models for different bitrate targets. We propose PerQ, which reframes perceptual reconstruction as inverse generative modeling with bounded support. Specifically, we define the quantization cell as the set of latents that yield the same transmitted symbols and derive a transport bound showing that reconstructions from this cell remain within a rate-determined radius of the codec output. This motivates performing generative reconstruction within the codec-induced quantization cell, rather than sampling from an unconstrained image prior. PerQ implements this principle by attaching a rate-conditioned flow-matching compensator to a frozen, multi-rate distortion-optimized backbone, enabling perceptual enhancement while preserving the backbone's coding performance. Experiments on Kodak and CLIC2020 show that PerQ achieves perceptual performance comparable to generative codecs such as MS-ILLM in LPIPS and FID, while maintaining competitive PSNR relative to distortion-optimized codecs such as ELIC. A single model checkpoint supports a wide bitrate range with fast decoding, and the compensator provides consistent gains across three different backbones. The implementation is available at this https URL.

---


### 86. [Sample-efficient learning with Dense Associative Memories](https://arxiv.org/abs/2610.27384)

**<font color=#1a73e8>作者：</font>** Andrew Lucas, Dmitry Krotov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We analytically study the evolution of the energy function of Dense Associative Memories (DenseAMs) as they train on randomly sampled codewords of random expander low-density parity-check codes (a.k.a. solutions of random XORSAT problems). We identify two distinct regimes and a transition between them, reminiscent of grokking in neural networks. A regime of small training set size is where the model memorizes a few training examples but cannot discover the underlying rules of the entire codeword dictionary generative process. The opposite regime, corresponding to a larger training set size, is where the model has uncovered the sparse constraints that generated the entire data set after seeing only polynomially many patterns. We also design a novel class of DenseAMs with a thresholding learning rule, and show that any amount of thresholding enables the model to perform simplified sparse Hamiltonian learning, which exponentially reduces the number of training examples needed to learn the true underlying data set. In this regime, the model learns how to discover $\exp[\mathrm{O}(n)]$ solutions from only $\mathrm{O}(\log n)$ training samples, which is asymptotically optimal for any learning algorithm. When training on codewords of certain random codes, the model can even learn the underlying code when a small O(1) fraction of bits are latent variables. These latent variables are not shown to the model during learning, but will be discovered by sparsifying observed higher-order correlations. For certain random codes, we show that a simple and conservative algorithm learns a minimal latent representation for the data set. This provides a transparent, physics-motivated, and analytically tractable toy model for how deep latent representations emerge in an associative memory training.

---


### 87. [Fixed-Size Active Statistical Inference](https://arxiv.org/abs/2610.27389)

**<font color=#1a73e8>作者：</font>** Erik Skalnes, Michael Oberst  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variance reduction techniques improve the efficiency of drawing conclusions from data. Recent proposals for variance-reduction use two complementary techniques to reduce variance: incorporating machine learning predictions into estimators and weighted sampling. A popular weighted sampling algorithm is Poisson Sampling (PS), which independently flips a biased coin at each unit and includes all heads in the sample. A fundamental flaw with PS is that it has a random sample size, which presents practical challenges and introduces variance into the estimator. We show that a fixed-size alternative, known in survey sampling as Conditional Poisson Sampling (CPS), is a drop-in replacement for PS on general multivariate Z-estimation problems, which include convex M-estimation considered in prior work. Notably, we show that the asymptotic variance of CPS is no worse than that of PS, and can be substantially better in realistic scenarios where predictions are imperfect. We illustrate these advantages on both synthetic and real datasets, and release a Python package implementing CPS. In light of our contributions, there is no need to suffer a variable sample size.

---


### 88. [When PTQ Calibration Helps or Hurts: Dose-Driven Collapse and Validation-Gated Abstention in Quantized Text Embedders](https://arxiv.org/abs/2610.27397)

**<font color=#1a73e8>作者：</font>** Hyojung Han, Ryangkyung Kang, Youngeun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned post-training quantization (PTQ) calibration fits quantizer parameters on a small calibration set, and for a text embedder the natural supervision is retrieval relevance. We ask two questions that are usually conflated: how far to calibrate, and whether to calibrate at all. Across three embedders (e5-base-v2, BGE-M3, EmbeddingGemma-300m) at 4-bit weight quantization, 161 calibration runs, the outcome of a fixed procedure ranges from a gain to catastrophic degradation, and the driver is the dose of the update, measured as the functional displacement D_func of the quantized model from its uncalibrated start. On EmbeddingGemma the same learning-rate grid gives +1.47 to -71.53 points of in-domain NDCG@10 change; a label-free cosine objective collapses at the same dose (-69.52 vs -71.63), so the collapse is a property of learnable calibration rather than of retrieval supervision. Objective sensitivity is heterogeneous: on e5, ranking calibration is substantially more robust than cosine at matched displacement (+14.16 +/- 4.34 pp, 95% t-CI [+3.37, +24.96], three paired slates), whereas on BGE-M3 the ordering is directionally opposite but unresolved ([-5.18, +2.38]). Dose is the main axis but not a sufficient statistic: equal D_func reached along different paths differs by up to 1.61 pp. We therefore treat calibration as an optional intervention. A pre-registered rule that accepts a checkpoint only when a per-query paired confidence interval on a 25% calibration-validation split clears the uncalibrated baseline was run on 6 independent slates and five arms. It never selected a checkpoint below its slate's baseline (0 harmful selections in 30 decisions), retained 8 of 11 beneficial updates, and paid a mean oracle regret of 1.52 pp with one abstention that forfeited 11.13 pp, a safety-opportunity trade-off, not a free improvement. We report what remains open, including label efficiency.

---


### 89. [Unified Sharp Bounds on Probabilities of Causation](https://arxiv.org/abs/2610.27398)

**<font color=#1a73e8>作者：</font>** Xin Shu, Ang Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilities of causation (PoCs) have developed steadily, from the binary measures first introduced by Pearl to the non-binary setting recently studied by Shu et al. As the theory has matured, PoCs have found applications in a growing range of areas, including personalized medicine, marketing and legal attribution. Shu et al. proposed closed-form bounds for multi-valued treatments and outcomes and proved them valid, but left their sharpness in high dimensions open. We close this gap with a mathematical proof. We further show that $\PNS$, $\PSub$, $\PRep$ and $\PN$ are all special cases of a single, more general formula. Combined with their equivalence classes, this settles the question of sharp bounds for discrete PoCs from experimental and observational data: in every dimension, they are given in closed form by a single theorem.

---


### 90. [Test-time Adaptation for Point Cloud Denoising under Unseen Noise](https://arxiv.org/abs/2610.27410)

**<font color=#1a73e8>作者：</font>** Kun Jiang, Shida Fu, Fanhao Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although deep learning-based point cloud denoising methods have demonstrated impressive results in recent years, their effectiveness usually degrades substantially in real-world scenarios where the noise distribution of test point clouds deviates from that of the training set. To address this challenge, we propose a test-time adaptive denoising (TTAD) framework that enables existing denoising approaches to adapt to unknown noise patterns at test time without relying on additional supervision or retraining from source data. Taking a pre-trained denoising model and a test noisy point cloud as input, TTAD first employs a residual-driven noise modeling (RDNM) module to estimate the sample-specific noise distribution through analyzing the deviation between the noisy input and its pseudo-clean version denoised by the initial model. Then, a noise-aware contrastive adaptation (NACA) module is designed to build sample-specific noisy-noisier test-time training pair from the denoised point cloud, and update the model parameters over a few adaptation steps per sample at test time through contrastive learning. Furthermore, TTAD naturally extends to a continual TTAD (CTTAD) setting, facilitating efficient progressive refinement across sequential test samples with consistent noise distributions, while reducing the computational cost per sample. Extensive experiments on both synthetic and real-world datasets demonstrate that our approach significantly improves the generalization ability of existing denoising models under unseen noise, achieving superior performance across multiple evaluation metrics.

---


### 91. [TokenFlow: Latent Token Rectified Flow Matching for 3D Point Cloud Generation](https://arxiv.org/abs/2610.27418)

**<font color=#1a73e8>作者：</font>** Linhao Wang, Dongjin Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D point clouds generation requires capturing both part-level layout and surface detail while preserving permutation equivariance. Existing latent generative models often encode an entire shape into a single vector, which limits their ability to retain part-level structure. We propose TokenFlow, a hierarchical flow matching framework that represents each shape as a set of latent tokens and couples a rectified flow over these tokens with a conditional flow over points. A bottleneck of $M \ll N$ learnable tokens aggregates global context through cross-attention at $O(NM)$ cost. On ShapeNet, TokenFlow achieves the best MMD and coverage across airplane, car, and chair, while obtaining 1-NNA comparable to the strongest baselines. On ModelNet, its learned latent set reaches the best reported linear-evaluation accuracy on ModelNet10. These results show that representing a shape as a set of latent tokens, aggregated at $O(NM)$ cost, provides an effective representation for 3D point cloud generation.

---


### 92. [Relational Complexity: Making Sense of Social Companion AI Use](https://arxiv.org/abs/2610.27419)

**<font color=#1a73e8>作者：</font>** Sophie Elizabeth Klitgaard, Grace X. Wang, Daniel M. T. Fessler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The adoption of social companion AI (SCAI) is often framed in terms of the positive features it offers users, including its nonjudgemental nature, agreeableness, and availability. Here, we argue the appeal of these features primarily arises from the difficulties inherent in human sociality. SCAI reduces what we term relational complexity, or the demands and risks inherent in human relationships. Drawing insights from studies of human cognition, communication, and human-computer interaction, we identify six distinct sites of relational complexity that we posit are integral to understanding SCAI adoption. These include: (i) relationship formation and dissolution; (ii) achieving mutual understanding; (iii) interpersonal motives and strategic uncertainty; (iv) social partner evaluation and self-presentation; (v) social embeddedness and information flow; and (vi) reciprocity and relationship maintenance. By attenuating relational complexity, SCAI offers users some of the experiences associated with companionship while reducing the demands intrinsic to obtaining such experiences from another person. However, the lower interpersonal risk and diminished cognitive load that attracts users to SCAI may contribute to myriad negative impacts, including relationship displacement, social demotivation, social deskilling, and risks to privacy. The concept of relational complexity thus provides a framework for studying both the appeal of artificial companionship and its implications for human wellbeing.

---


### 93. [Learning-Theoretic Foundation for General Coded Computing: The Adversarial Setting](https://arxiv.org/abs/2610.27440)

**<font color=#1a73e8>作者：</font>** Parsa Moradi, Hanzaleh Akbarinodehi, Mohammad Ali Maddah-Ali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial workers pose a severe challenge in distributed computing systems by returning corrupted outputs that can substantially distort the recovered computations. Coded computing addresses this threat by introducing redundancy across worker assignments. Existing exact and approximate coded-computing methods typically handle adversarial outputs by explicitly locating and correcting or removing erroneous evaluations, which adds significant computational overhead at the master node. Moreover, existing analyses do not characterize how the recovery error scales with the number of workers and the adversarial budget.
In this paper, we develop an adversarially robust extension of general coded computing (GCC), a learning-theoretic approximate coded-computing framework that designs the encoder and decoder by minimizing an upper bound on the end-to-end recovery error. Rather than identifying corrupted workers, the proposed method uses smoothness regularization to limit the influence of their outputs. The resulting encoder and decoder can be implemented using smoothing splines with linear master-side complexity. We derive a non-asymptotic bound on the worst-case end-to-end approximation error by decomposing it into three components: (1) the encoder approximation error, (2) the decoder reconstruction error under fully honest results, and (3) the adversarial perturbation error. For maximum of $q\geq 1$ adversarial workers among $N$ workers results in a worst-case error of order $\mathcal{O}((q/N)^{6/5})$ with appropriate selection of smoothness parameter, demonstrating that the approximation error vanishes asymptotically whenever the number of adversaries grows sublinearly with the network size. Experiments on scalar computation and neural-network inference are consistent with the predicted convergence behavior.

---


### 94. [Privacy-Preserving Robustness-Guided Testing](https://arxiv.org/abs/2610.27441)

**<font color=#1a73e8>作者：</font>** Charles Koll, Houssam Abbas, Mike Rosulek  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In industries like semi-conductors and aerospace, it is common for the design company to contract out part of the testing process to a Testing-as-a-Service (TaaS) company. In such a setup, both parties want to keep their intellectual property private (i.e. unknown to the other party): namely the design and its output traces for the designer, and the detailed correctness specifications for the tester. We demonstrate a practical way for conducting provably private TaaS using a cryptographically secure multi-party computation protocol. We do so for the common setup where the specification is in Signal Temporal Logic, and testing is done using robustness-guided falsification. Our implementation carefully separates the steps of falsification, and manages to be $\textit{maximally secure}$, in the sense that the parties learn the absolutely minimum necessary for falsification. For up to a 100-dimensional input search space, the generation of one test takes less than 80 msec, and the overhead of the privacy-preserving protocol is less than 6x. These numbers mean that privacy-preserving TaaS is practical, thus enabling TaaS in security-sensitive industries.

---


### 95. [Using Set Learning to Improve Set-Valued Classifiers on Long-tailed Data](https://arxiv.org/abs/2610.27443)

**<font color=#1a73e8>作者：</font>** Kevin Kasa, Scott C. Lowe, Graham W. Taylor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Set-valued classification (SVC) offers a practical approach to communicating uncertainty while maintaining accuracy by predicting variable-sized sets per input rather than fixed-sized sets (e.g. top-1 or top-5). However, set-valued classifiers (SVCs) exhibit significantly degraded performance on long-tailed and imbalanced datasets, a setting for which they are ostensibly well-suited. This becomes apparent under macro-average evaluation, which weighs all classes equally. SVCs are typically formed during a post-hoc calibration stage, so little is known about how training dynamics affect their behaviour. In this work, we investigate how different neural network training strategies and loss functions impact downstream SVC performance on highly imbalanced data. In addition to methods such as label smoothing and class-balancing, we investigate whether loss functions that operate over sets of examples in a batch, rather than treating all examples as independent, lead to better downstream SVCs. We adapt the recently proposed odd-K-out (OKO) loss function, which learns from sets of training samples, improving its sample efficiency whilst introducing algorithmic modifications that reduce its computational overhead from 3.2x to just 1.36x that of standard cross-entropy training. Experiments on highly long-tailed datasets demonstrate our modified OKO approach significantly improves macro-accuracy across multiple SVC methods - including top-k, average-k, and conformal prediction - while maintaining competitive micro-accuracy. This improved performance on minority classes occurs without substantially increasing prediction set sizes, suggesting that carefully constructed set-based training can produce networks better suited to imbalanced data.

---


### 96. [LoRASpace: A Pool-Wide Shared Substrate for Static and Dynamic Multi-LoRA Composition](https://arxiv.org/abs/2610.27444)

**<font color=#1a73e8>作者：</font>** Thamirawaran Sathiyalogeswaran, Navindu De Silva, Chamikara Siriwardane 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) attaches small low-rank matrices to a frozen backbone, and public repositories host many LoRAs per backbone, each for a different concept or task. Combining several LoRAs in one generation forces a trade-off. Merging their weights into one update needs a single forward pass, but LoRAs trained for different concepts interfere and quality drops. Running each LoRA in its own forward pass (composite) preserves quality, but inference time grows linearly with the number of active LoRAs. We study a property of LoRA pools overlooked by prior multi-LoRA work. In real LoRA pools, the stacked low-rank factors need far fewer directions than their summed ranks. Using singular value decomposition, we find the minimal subspace that keeps 99% of the factor energy. On three diffusion pools, only 46% to 57% of the summed LoRA ranks is needed, and the subspace grows sub-linearly with pool size. A 48-LoRA sub-pool of LoRA-Hub on FLAN-T5 tasks shows comparable overlap (62%), while the diversity-curated LoRA-Retriever benchmark sits near the no-overlap baseline (96%), so pool composition rather than modality predicts where compression is large. We build on this overlap with LoRASpace, a training-free method that computes the subspace once per pool and reuses it in two inference modes, a static mode at merge cost and a dynamic mode for input-dependent routing. On the diffusion pools, static LoRASpace matches composite quality at merge cost, and dynamic LoRASpace is more than 6x faster than composite with six active LoRAs on a 17-LoRA pool, mainly because it runs one backbone pass instead of six. In an ablation, static variants at the same rank match LoRASpace, so the quality gain does not depend on the pool-wide basis. On the near-orthogonal LoRA-Retriever benchmark, compression is small and gains come from coupling with external retrieval.

---


### 97. [SRE: Accelerating Zero-Knowledge Proofs via Scalar Redundancy Elimination in Multi-Scalar Multiplication](https://arxiv.org/abs/2610.27452)

**<font color=#1a73e8>作者：</font>** Jonathan Ku, Guanglei Zhou, Jiawen Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-Scalar Multiplication (MSM) is a fundamental cryptographic operation used in Elliptic Curve Cryptography (ECC) across a wide range of applications. Its computation involves intensive elliptic curve point additions (PADD). MSM plays a critical role in cryptographic primitives such as polynomial commitments and zero-knowledge proofs (ZKPs), where it often becomes the runtime bottleneck. Consequently, optimizing MSM is an active area of research focused on reducing computational complexity and accelerating performance. The current state-of-the-art algorithm for large-scale MSM is Pippenger's bucket method, which consists of three main steps: point merging, bucket aggregation, and window aggregation. Among these, the point merging step is the primary performance bottleneck. Our work targets this major computational bottleneck. To reduce operations for practical applications, we propose a novel Scalar Redundancy Elimination (SRE) algorithm with three approaches: a vanilla array-based approach, a list-based greedy approach, and a list-based exhaustive approach, all incorporating an early stopping technique. Depending on the use case, these strategies can be integrated into our modified MSM algorithm, which is based on Pippenger's bucket method. As a result, our proposed MSM algorithm, enhanced with the SRE technique, incurs less than $3\%$ additional search time, while reducing the number of operations by $25\%$, leading to a $30\%$ speedup in runtime compared to the standard Pippenger's bucket method. This translates to a $10 \sim 20\%$ runtime reduction in various ZKP systems that rely heavily on MSM.

---


### 98. [Privacy-Preserving Personalized Federated Learning (PPP-FL) for Medical Imaging](https://arxiv.org/abs/2610.27470)

**<font color=#1a73e8>作者：</font>** Md Morshedul Islam, Hossain Shahriar, Alfredo Cuzzocrea  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a distributed machine learning paradigm that reduces transmission costs, mitigates cross-border data sharing restrictions, and enhances privacy by keeping raw data on local devices. Clients in FL systems train local models and share only updates, which are aggregated by a central server. While this setup limits direct data exposure, FL remains vulnerable to privacy attacks. Existing attack and defense strategies have largely been developed for centralized systems, and adapting them to FL introduces new challenges due to its unique architecture and training workflow. In this work, we first propose a model inversion attack on FL systems using Deep Convolutional Generative Adversarial Networks (DCGANs) in the context of large-scale medical imaging. Our method operates under realistic assumptions about the attacker's knowledge and capabilities. We then examine the effect of client-side differential privacy (DP) in mitigating privacy leakage and incorporate personalized FL to improve model performance under DP settings. Experiments on the Brain MRI ND-5 dataset show that DCGAN-based attacks can reconstruct semantically meaningful synthetic images, revealing significant risks to the privacy of training data. Applying DP reduces attack success but introduces an accuracy trade-off, which is further overcome by personalized FL at each client side. We also evaluate how different aggregation algorithms affect both attack vulnerability and defense effectiveness, underscoring the critical role of aggregation strategies. The proposed attack-and-defense framework is model-agnostic and applicable to a wide range of FL-based systems.

---


### 99. [When Parameter Gradient Flows Close in Representation Space](https://arxiv.org/abs/2610.27474)

**<font color=#1a73e8>作者：</font>** Shengye Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The represented gradient flow of a parameterized model depends on a mobility that can retain hidden parameter information. We study when one entire represented mobility map works for every autonomous loss from one fixed initialization. For two-factor matrix representations wider than both output dimensions, with individually full-row-rank factors, we classify all admissible joint ranks: closure occurs precisely at effective scalar-balanced minimal joint rank or a two-value signed spectral family at full joint rank. All intermediate ranks are excluded; positive represented flows belong to known square-root families. For general representations with constant ambient representation and gradient-Lie ranks, ordinary closure is equivalent to a local invariant-level metric in the analytic case and specified smooth regimes. An endpoint section forces the initially unrestricted mobility map to admit a locally smooth representative on the represented image. We also separate testing families: linear losses locally admit closure at every submersion, whereas one fixed translated strongly convex quadratic family fails it on a delayed-bracket example. A fixed output readout gives an ordinary squared-loss witness. These supporting results do not characterize quadratic-only closure in general. We retain the unresolved smooth output-rank-two case with Lie rank at least four. A frozen deterministic experiment checks a separate engineered-loss construction; it is distinguished from the squared-loss proof, universal theorems and empirical learning performance.

---


### 100. [Securing Agentic Commerce Through Behavior-Aware Fraud Detection and Cybersecurity for Trusted AI-Agent Payment Authorization](https://arxiv.org/abs/2610.27483)

**<font color=#1a73e8>作者：</font>** Kayode L. Ogunsusi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing use of autonomous artificial intelligence agents in digital commerce creates new security concerns involving agent impersonation, unauthorized payments, compromised agents, and misuse of delegated authority. This research introduces the Autonomous Commerce Agent Guard System (ACAGS), a cybersecurity framework combining supervised machine learning, behavioral analytics, agent-specific authorization controls, and explainable AI. The framework was evaluated using synthetic financial transaction data augmented with simulated agent characteristics and five adversarial scenarios. XGBoost was selected following comparisons with alternative classifiers. Across ten experimental runs, behavioral features improved mean F1-score from 52.12% to 67.49%, with agent-specific features increasing performance to 69.46%. The framework achieved detection rates of 99.77% for abnormal agent behavior, 99.73% for impersonation, and 100% for malicious delegation and authorization-scope violations. Compromised-agent detection reached 72.27%. ACAGS also supported APPROVE, REVIEW, and REJECT authorization outcomes, with SHAP explanations providing model interpretability. The results demonstrate the potential of combining behavioral intelligence and delegated authorization controls to strengthen simulated agentic-commerce payment security, while highlighting the need for validation using real-world transactions.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
