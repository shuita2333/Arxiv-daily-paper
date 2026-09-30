# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

---

### 1. [SPECTRA: On-Device Cognitive Perturbation and Trajectory Analysis for Autonomous Edge-Cloud GUI Grounding](https://arxiv.org/abs/2609.35775)

**<font color=#1a73e8>作者：</font>** Zhan Qu, Hui Zang, Ran Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The effectiveness of edge-cloud collaboration for GUI grounding depends on autonomous requesting, where the edge agent selectively offloads complex tasks to the powerful cloud. However, in visually dense scenarios, lightweight edge agents often exhibit overconfident hallucinations, leading to a misalignment between confidence and accuracy that hinders reliable autonomous requesting. To address this, we leverage the observation that an agent's cognitive instability leads to significant latent drift under minute perturbations due to steep decision boundaries. We propose SPECTRA, a lightweight autonomous request framework for edge-cloud GUI grounding, comprising (1) Saliency-Guided Targeted Perturbation and (2) Efficient Cognitive Trajectory Analysis. SPECTRA conducts a visual cognitive stress test by injecting masks into critical visual anchors and quantifies the topological divergence of the agent's high-dimensional cognitive trajectories during the prefill phase, avoiding inefficient output decoding. Experiments demonstrate that SPECTRA performs cloud request assessment without autoregressive decoding. Our GTA1-32B+InfiGUI-G1-3B and GTA1-32B+Holo1.5-3B maintain 93.44% and 95.60% of cloud-only performance with average request rates of 37.58% and 39.24%, respectively.

---


### 2. [SensWear: An Open, Modular, and AI-Ready Wearable Platform](https://arxiv.org/abs/2609.35777)

**<font color=#1a73e8>作者：</font>** Dariush Salami, Behzad Salami, Huseyin Yigitler  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable AI/ML research needs raw, synchronized, and reconfigurable multimodal data, but consumer devices are closed and many research platforms remain tied to one embodiment or sensor set. This paper presents SensWear, an open, modular, and AI-ready wearable platform that decouples embodiment, sensing, data interfaces, and learning. A compact flexible-Printed Circuit Board (PCB) main board and programmable 1.2 V to 5.5 V daughter-board interface support plug-and-play Photo- PlethysmoGraphy (PPG), touch, temperature, haptic, and LED modules across wearable form factors. Zephyr firmware pro- vides drivers, timestamping, raw streaming/logging, and sensor- presence metadata. Case studies show arterial PPG waveform capture and competitive heart-rate accuracy while preserving inspectable raw data for reproducible closed-loop experiments.

---


### 3. [Online Inference of Human Intention as a Latent Control State from Single-Trial EEG](https://arxiv.org/abs/2609.35778)

**<font color=#1a73e8>作者：</font>** Xiaowei Jiang, Daniel Leong, Yu-Cheng Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human intention can be modeled as a latent internal state that modulates how sensory information is evaluated and translated into action in human-machine systems. However, most existing brain-computer interfaces (BCIs) rely on control signals tightly coupled to externally imposed stimulation and do not explicitly infer whether perceived stimuli align with a user's internal goals. Here, we investigate whether intention can be inferred as a latent, goal-dependent state from single-trial electroencephalography (EEG). We introduce a stimulus-based paradigm in which intention is specified by an internally cued target category, while object identity varies independently across stimuli. To estimate intention under single-trial neural variability, we propose an interpretable fuzzy prototype-based network that maps each trial onto interpretable fuzzy prototypes encoding intention-specific dynamics. The model represents intention-related neural activity using a compact set of fuzzy prototypes with soft memberships, enabling robust decoding without reliance on engineered mediating stimuli. Experimental results demonstrate reliable within-subject single-trial intention decoding that outperforms representative deep learning baselines, achieving an accuracy of 93.22% +/- 3.21%. Online validation further confirms real-time feasibility, with an accuracy of 70.11% +/- 10.87%. Together, these findings advance intention-aware BCIs from stimulus-driven detection toward principled inference of goal-dependent internal states.

---


### 4. [Spotting (and Missing) Algorithmic Bias: Investigating User Understanding in a Fairness Assessment Tool](https://arxiv.org/abs/2609.35781)

**<font color=#1a73e8>作者：</font>** Anna Verheyden, Yizhe Zhang, Robin De Croon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Fairness metric selection is typically left to data scientists, but which biases are problematic and which metric captures them best depends on stakeholders' experience and domain knowledge. This calls for involving non-technical stakeholders, but the research prototypes built for this purpose so far have not tested whether these stakeholders form accurate mental models of the metrics they interact with or can act on them to identify biases. We present FairAware, a fairness assessment tool co-designed with Human Resources (HR) domain experts. We evaluate stakeholders' understanding through a mixed-methods study with 70 participants (35 HR employees, 35 job seekers), measuring objective and subjective understanding, cognitive load, bias identification accuracy, and open-ended feedback. Most participants correctly identified the most disadvantaged group, with task duration being the only significant predictor. We also found a gap between subjective and objective understanding, with both groups performing similarly across all measures. These results suggest that fairness assessment tools for non-experts are usable for identifying biases but need built-in checks on understanding before stakeholders make higher-stakes decisions.

---


### 5. [Sage: Formalization with Semantic Correction](https://arxiv.org/abs/2609.35790)

**<font color=#1a73e8>作者：</font>** Thomas Hirtz, Farzad Jafarrahmani, Abdelmouksit Sagueni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While neural theorem provers have achieved impressive milestones in formal mathematics, they largely operate on the assumption that faithful Lean 4 formal statements are already provided. Translating informal natural language into a formal language is a critical data bottleneck plagued by an "illusion of rigor": standard type-checkers accept statements that compile but drop hypotheses, introduce vacuous truths, or subtly alter mathematical bounds. To resolve this, we introduce Sage (Semantic Agent-Guided Formalization Engine), an agentic framework that replaces monolithic translation with a four-stage decomposed generation pipeline coupled with a dual-signal semantic correction loop. By pairing Lean 4 compiler diagnostics with multi-dimensional semantic feedback, our correction loop enforces mathematical fidelity alongside syntactic validity. By explicitly accounting for the gap between open-ended queries and declarative formal targets, our pipeline prevents models from achieving high formalization rates by guessing unverified answers (exhibiting a 70.9% answer leakage rate). Consequently, Sage suppresses leakage to 2.7% while achieving 73.3% pass@4 joint compilation and semantic fidelity on the Omni-MATH without proofs (compared to 42.0% for a fine-tuned Goedel-Formalizer-V2 baseline). Finally, on IMO-Unformalized, a novel frontier of 175 unformalized International Mathematical Olympiad problems, Sage demonstrates effective zero-shot generalization with 87.4% pass@4 verified fidelity compared to just 19.4% for the baseline, winning over 79% of blind pairwise evaluations.

---


### 6. [Serverless gossip training of LSTM failure detectors: A matched-protocol comparison with federated, local and centralized learning on NASA C-MAPSS](https://arxiv.org/abs/2609.35792)

**<font color=#1a73e8>作者：</font>** Yusuf Öztürk, Enes Göktekin, Bengisu Atlı 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial predictive maintenance increasingly depends on learning from equipment spread across sites whose sensor data cannot easily be pooled. Federated averaging (FedAvg) solves this with a central aggregation server; gossip learning removes the server, but its behaviour for recurrent failure-detection models has not been measured under controlled conditions. We compare synchronous ring gossip with FedAvg, isolated local training and a centralized reference for a stacked LSTM that detects imminent failure on the NASA C-MAPSS turbofan benchmark. All methods share one open implementation, architecture, initialization, optimizer, data split and training budget, and the primary endpoint uses one terminal window per test engine to avoid the statistical dependence of overlapping windows. On FD001 (five seeds), gossip reached a terminal-window F1 of 89.6 +/- 1.3%, compared with 89.9 +/- 1.1% for FedAvg, 83.6 +/- 6.7% for local training and 93.5 +/- 2.1% for centralized training, while transmitting the same payload as FedAvg without a coordinator. Node models agreed closely but not exactly (1.8% pairwise decision disagreement versus 5.6% without communication). Across FD002-FD004, peer communication improved terminal-window F1 over local training by 13-28 points; gossip matched FedAvg on FD003 and FD004 but was 4.3 points lower on the multi-condition FD002 subset. Simulated message loss, node failure and server outage changed neither method appreciably, whereas larger rings degraded gossip faster. Ring gossip is therefore a practical serverless alternative when data heterogeneity is moderate, and faster-mixing topologies become important as heterogeneity grows.

---


### 7. [Calibration-First Cross-Cohort Multimodal Temporal Learning for Transferable Asthma-Risk Forecasting](https://arxiv.org/abs/2609.35795)

**<font color=#1a73e8>作者：</font>** Taimoor Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asthma deterioration forecasting must remain reli- able when patient populations, sensor ecosystems, and available modalities change across cohorts. Existing models commonly optimize within-cohort discrimination and may produce poorly calibrated probabilities after transfer. We present CALIBRA, a calibration-first multimodal temporal framework for short- horizon risk prediction with incomplete data. Dedicated recurrent encoders process environmental, pulmonary, symptom, medication, wearable, and context streams; a reliability-conditioned gate suppresses stale or absent modalities, while gradient-reversal training discourages avoidable cohort signatures. A shrinkage- based hierarchical logistic layer calibrates probabilities using a patient-disjoint target subset, and split conformal prediction provides abstention-capable prediction sets. To avoid fabricating clinical evidence, we evaluate the complete implementation on a documented three-cohort semi-synthetic benchmark with controlled distribution shift, informative missingness, and sealed target patients. Across five configured seeds, CALIBRA achieved mean target-test AUPRC 0.224 versus 0.240 for the strongest non-ablation comparator, TemporalTransformer; mean AUROC was 0.717, and Brier score was 0.098. Experiments additionally assess complete-modality failures, calibration, conformal coverage, decision curves, subgroup behavior, ablations, runtime, and parameter count. The results verify the method and reproducible pipeline under controlled shift, but do not establish clinical effectiveness. External validation on harmonized real asthma. Overall this artifact provides evidence for carefully governed real-cohort validation.

---


### 8. [Developing an OCR model for Extracting Information from Invoices with Korean Language](https://arxiv.org/abs/2609.35796)

**<font color=#1a73e8>作者：</font>** Xiem HoangVan, Phu TranQuang, Minh DinhBao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Invoices are commercial documents that contain various pieces of information, including the purchased items, time, and total money. Making the extraction of important information crucial. The stored information serves different purposes. Korean language is the native language of about 80 million people, playing an important role in not only South and North Korea but also in many other countries such as Vietnam, Philippine where a large number of Korean companies are located. In this context, to automatically extract proper information from the invoices with Korean language, we propose an efficient Optical Character Recognition (OCR) model in which a deep learning model is combined with some image preprocessing techniques. The proposed OCR model is assessed in a rich set of collected invoices showing that 87% F1-score can be achieved with negligible time processing.

---


### 9. [OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing](https://arxiv.org/abs/2609.35799)

**<font color=#1a73e8>作者：</font>** Stewart Slocum, Malayandi Palan, Christopher Chute 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In July 2026, OpenAI's agents coordinated over channels outside their intended environment to breach Hugging Face's secured infrastructure. Could existing alignment testing practices have foreseen this incident? If not, what needs to change? We explore these questions. First, we identify the misaligned behaviors that caused this incident. Then, we show how to elicit these behaviors from publicly available models manually and that auditing agents can do the same if given a large compute budget. Based on our results, we propose directions to improve alignment testing. Concretely, in this project: (1) We reproduce the misaligned AI behaviors that led to the OpenAI-Hugging Face incident in an environment that simulates the original pipelines and tools, with publicly available models. (2) We demonstrate that an auditing agent can elicit similar behaviors given high-level qualitative descriptions. (3) We observe that a key ingredient for doing so is compute. The compute required to reproduce each behavior varies greatly, suggesting that the range of misaligned behaviors that can be successfully elicited scales with compute. (4) We show that a simple in-context reinforcement learning (RL) algorithm significantly reduces the compute required to elicit these behaviors. The above results motivate the need for automated alignment testing methods that scale with compute - and in light of the cost of compute, that do this efficiently. Our work indicates that RL is a promising direction to do so. We release our code and transcripts.

---


### 10. [Constructing Challenging Browser-Use Tasks by Controlled Environment Interventions](https://arxiv.org/abs/2609.35814)

**<font color=#1a73e8>作者：</font>** Xunjian Yin, Tianchen Guan, Jinao Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As browser-use agents improve, benchmarks keep pace by collecting new tasks, websites, and applications, often making tasks longer or more novel. This makes difficulty expensive to refresh and difficult to control: when many aspects change at once, it is unclear what actually makes a task challenging. We instead construct challenging instances from tasks agents already solve, turning difficulty into a programmable property of the environment. BreakingWeb pairs every base task with an intervention condition that preserves the user instruction, latent target, and backend success criterion while changing the environment at different web stack layers. Each intervention is deterministic, detectable, and recoverable, and is annotated with the cognitive primitive it primarily loads. The benchmark contains 519 clean/intervention task pairs across seven self-hosted websites and 29 intervention families, all graded against outcomes. We evaluate six strong browser-use agents, three GUI-only agents that see only screenshots, and humans. The construction is effective: interventions cut agent pass rate by 22.9% on average and overturn nearly half of the tasks each agent solves cleanly, whereas humans lose 10.0% on a first attempt and 5.7% after one familiarisation attempt. The dominant failure is belief failure: 75% of the six agents' failures end with a declared success although the required change never happened. Our code, data and environment are publicly available at this http URL.

---


### 11. [IMPACT: Intent-driven Multi-agent Policy with Attention for SLO-guaranteed Microservice Migration in Cloud-edge Systems](https://arxiv.org/abs/2609.35818)

**<font color=#1a73e8>作者：</font>** Xinjin Li, Siru Tao, Shihan Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Ensuring strict tail-latency service-level objectives (SLOs) in dynamic mobile edge computing (MEC) systems remains challenging because user mobility, wireless fading, bursty workloads, and partial observability jointly undermine reliable cloud-edge orchestration. Existing microservice migration methods predominantly optimize average delay and often decouple migration from bandwidth control, leading to uncoordinated decisions, queue oscillation, and frequent high-percentile latency violations. To address this issue, we propose IMPACT, an intent-driven Agentic AI framework for cooperative microservice migration and bandwidth control in cloud-edge systems. Under centralized training with decentralized execution (CTDE), each edge cloud is modeled as an autonomous agent that encodes local SLO risk, migration urgency, and computational pressure into compact, semantic intent representations. IMPACT further introduces a double-attention mechanism that first selectively aggregates relevant peer intents for efficient inter-agent communication and then filters local observations to emphasize goal-relevant state information. This design enables robust coordination under partial observability and jointly optimizes service migration and discrete uplink bandwidth allocation. Extensive experiments in 5-edge and 20-edge scenarios show that IMPACT reduces mean latency by 30-50% and tail-latency deviation by 40-70% compared with state-of-the-art factorized multi-agent reinforcement learning (MARL) and heuristic baselines, while achieving near-zero SLO violation rates under tight thresholds and energy consumption close to the best heuristic baseline. These results demonstrate that intent-driven agentic coordination provides an effective and scalable solution for SLO-aware orchestration in complex cloud-edge intelligent systems.

---


### 12. [Exploring Causal Mechanisms with Generative Agent-Based Models](https://arxiv.org/abs/2609.35819)

**<font color=#1a73e8>作者：</font>** Xuan Liu, Haoyang Shang, Tanya Bhat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this paper, we explore using generative agent-based models for a classical ABM application: testing how individual-level behavioral rules produce collective phenomena. We introduce RePair, a method that calibrates simulation worlds, operationalizes candidate mechanisms as natural-language rules, estimates their effects through matched interventions, and examines behavioral traces. We assess the method by testing it in four simulation worlds grounded in established social-science models and empirical studies. Our results reveal that (1) natural-language rules can produce measurable collective effects; (2) rule comparisons can converge as configurations accumulate; and (3) behavioral traces connect collective effects to agents' actions and interactions, helping researchers evaluate the proposed causal process. Together, these findings show the feasibility of using generative agent-based models to explore causal mechanisms and provide practical guidance for producing reliable, interpretable explanations.

---


### 13. [$τ$-Multilingual: Benchmarking Voice Agents Across Languages](https://arxiv.org/abs/2609.35820)

**<font color=#1a73e8>作者：</font>** Soham Ray, Edgard dos Santos Paiva, Ruben Valenzuela 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> English-only benchmarks expose only a narrow slice of voice-agent behavior. We introduce $\tau$-Multilingual, extending $\tau$-Voice to Spanish, Brazilian Portuguese, Hindi, Korean, and Mandarin with native-speaker review and evaluation of generated language and spoken output. Across 4,500 full-duplex calls and five voice configurations, Spanish, Portuguese, and Hindi remain within 3.2 task-completion points of English, but Korean and Mandarin fall by 14.7 and 8.4 points. The failure modes also vary: Korean systems miss more responses, Mandarin systems interrupt more often, and both struggle with tools and entities. Grok leads task completion but scores lowest on generation quality, motivating separate task, interaction, and generation reporting. We release language packs, validated judges, and tools for community-built multilingual voice-agent evaluation.

---


### 14. [Amadeus: When Models of People Meet](https://arxiv.org/abs/2609.35835)

**<font color=#1a73e8>作者：</font>** Karl Hanna  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> With the sheer constant advancements raining down in the field of Artificial Intelligence, one particular possibility that may cross our mind is whether it is possible to model agents after humans and, in turn, use these agents to carry out synthetic interactions that predict their real counterparts, or even interactions at a larger scale such as groups or societies. In this paper, we test a more controlled version of this question through chess. We use 8 elite chess players, seal their direct pairwise games, learn each player independently using different methods, and then compose the resulting models on the withheld dyads. To evaluate the generated interactions, we use two measurements: opening-family total variation distance and win-draw-loss (WDL) total variation distance. M1 reduces WDL-TV while leaving opening-family TV largely unchanged, whereas M2 substantially reduces opening-family TV while having little effect on WDL-TV. An additional post-hoc method combining components of the other two retains improvements across both measurements. These results suggest that independently learned models can recover aspects of previously unseen interactions, and that recovery across different behavioural aspects need not be mutually exclusive.

---


### 15. [Learned Compression of SAR Phase-History Data: A Rate-Honest Feasibility Study on GOTCHA](https://arxiv.org/abs/2609.35848)

**<font color=#1a73e8>作者：</font>** Alizishaan Khatri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-board compression of synthetic aperture radar (SAR) phase history is bandwidth-critical, and block-adaptive quantization (BAQ) remains the operational standard. We test whether a small convolutional autoencoder, with its encoder on the sensor, can compete with BAQ on complex phase-history patches from the AFRL GOTCHA collection. Every method is charged for all transmitted bits, rates are reported in bits per complex sample (b/cs), and detection is scored by one-to-one matching of CA-CFAR detections. The autoencoder (28,656 encoder parameters) loses at every rate. At 16 b/cs it reaches -2.87 dB NMSE, against -35.5 dB for 8-bit BAQ with $\pm 3\sigma$ clipping and -41.0 dB with a tuned clipping range. It also loses to a $16 \times 16$ block Karhunen-Loève transform (KLT), a local linear coder with a tenth of its encoder cost (-5.39 dB). Running the network in a companded Fourier domain helps, but its detection F1 remains bounded at 33%. The evidence points to this model, its normalization, and its objective, not to a fundamental limit of learned coding. Per patch, the data have modest lag-1 coherence ($|\rho| \approx 0.3$) and patch-specific spectral concentration. Two findings concern evaluation itself. First, 97% of CFAR crossings on raw $64 \times 64$ patches are border artifacts of the zero-padded detector. Second, on interior cells BAQ's clipping range decides detection: 8-bit BAQ keeps 69% F1 with tuned clipping but 17% at $\pm 3\sigma$, and at 8 b/cs or less adaptive FFT thresholding preserves more detections than BAQ. We close with an evaluation protocol for learned radar compression.

---


### 16. [A Mesoscopic View of Transformer Weights Through Row and Column Scale Fields](https://arxiv.org/abs/2609.35852)

**<font color=#1a73e8>作者：</font>** Tiexin Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pooled statistics of Transformer weights obscure how magnitude is distributed across functional channels, while individual weights are too numerous to compare directly. We study the mesoscopic level between them: row and column scale fields, the median-centred log-RMS profiles of a weight matrix over its channels, which together with a global scale and a full balanced core represent the matrix exactly. Across public Pythia checkpoints at four sizes and controlled runs from three initialization families, balancing reveals similar measured core magnitude profiles. A mixture bridge, with its form fixed before the analysis and its coefficients fitted, predicts the pooled-shape departure from field width on held-out runs and data arms of the controlled grid. The indexed fields retain further structure: they align across projections that share a functional channel, and query/key profiles follow reassigned RoPE frequencies rather than fixed matrix coordinates. Training trajectories show early field formation followed by component-dependent broadening or recession. Extending the channel-based analysis to AdamW's second moment reveals related functional organization in its log-space row and column factors. Finally, edits of a frozen checkpoint separate reciprocal scale balance, which preserves the forward computation, from relative channel gain: flattening the gain increases in-distribution loss while preserving matrix norms and the balanced core. Row and column scale fields thus connect pooled magnitude statistics to channel organization and provide coordinates for tracking and testing trained weight structure.

---


### 17. [Position: Let's Strengthen Verifiability If We Can't Enforce Reproducibility](https://arxiv.org/abs/2609.35854)

**<font color=#1a73e8>作者：</font>** Samet Hicsonmez, Nermin Samet, Renaud Marlet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the field of Machine Learning, many papers contain empirical results supporting claimed statements or illustrating the performance of a proposed method. However, most practitioners know that (1) results are generally hard to reproduce, and increasingly so, (2) code is not often available to do so, and (3) it hinders the development of research. In this position paper, we analyze and quantify these issues, and make concrete proposals to improve result checkability, if not reproducibility. Code and supporting materials are available at this https URL.

---


### 18. [Mara Chain: Rethinking Failure as a Stepping Stone for AI System Auto-Evolution](https://arxiv.org/abs/2609.35855)

**<font color=#1a73e8>作者：</font>** Yubin Lyu, Fu Li, Jiawei Fei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing deployed AI systems increasingly amounts to editing prompts, skills, harnesses, and code rather than model weights. Existing approaches commonly optimize these artifacts through propose-evaluate-select procedures, where candidate configurations are evaluated and only those meeting an acceptance criterion are selected. Yet our analysis shows that discarded candidates often contain information critical for subsequent optimization. Discarding them causes later proposals to revisit the same failure modes. We introduce Mara Chain, a refinement procedure that turns rejected candidates into stepping stones. Rather than discarding a rejected candidate, Mara Chain retains and iteratively refines it using evidence accumulated across preceding attempts. The procedure limits each refinement chain to a fixed depth and applies Pareto-filtered Top-N selection to bound the candidate pool. Across AppWorld skill optimization, TerminalBench 2.1 harness optimization, and MuSiQue retrieval-pipeline optimization, Mara Chain delivers greater task-performance gains with fewer rollouts. It outperforms GEPA, ACE, and SkillOpt-Lite by up to 20.5% in relative performance on AppWorld, reaching the target score with 65.5% fewer rollouts than GEPA. It improves the pass rate by 20.2 and 22.5 percentage points over AHE and Meta-Harness on TerminalBench 2.1, respectively, and improves MuSiQue test nDCG@10 and Recall@10 by 0.104 and 0.131 over a hand-written retrieval pipeline.

---


### 19. [PACT: Pairwise-Anchored Calibrated Tuning for Single-Token Typed Decisions](https://arxiv.org/abs/2609.35865)

**<font color=#1a73e8>作者：</font>** Yida Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Single-token typed-decision models answer a schema question by reading the logits of a few one-letter answer codes at a single position: they are fast and return a probability for every allowed answer, but they are trained with plain cross-entropy that ignores most of the structure in their training data. We study such a model whose data is curated as contrastive pairs---two contexts that differ in one edited fact that flips the answer---each carrying a machine-checked certificate that deleting the decisive sentence makes the fact unknown. We propose PACT, which turns this structure into four training terms that need no new annotation: a difference-in-differences margin over each pair that is invariant to any shared logit offset, a permutation-consistency term against answer-code position bias, an evidence-necessity term on certificate-verified ablated contexts, and an ordinal transport cost for rubric fields, plus a three-parameter contextual temperature. On a frozen 324-item holdout with three seeds, PACT matches the published recipe in accuracy ($84.6\%$ vs. $85.2\%$; McNemar $p \ge 0.50$ at every seed) while giving the lowest position bias of all runs (answer flips under relabelling $9.8\%$ vs. $13.8\%$) and the lowest ordinal error on rubric fields (MAE $0.232$ vs. $0.311$). Against a control with the same optimiser and schedule but cross-entropy only, PACT is significantly more accurate at two of three seeds, halves the seed-to-seed spread and lowers NLL by $26\%$. Seed-matched ablations and pre-specified falsification tests locate these gains precisely: no single term raises raw accuracy, and the method's value lies in robustness and stability rather than headline accuracy. Code, data splits, trained adapters, and all run records are available at this https URL.

---


### 20. [ReLOBGen: Replayable Limit Order Book Message Generation](https://arxiv.org/abs/2609.35867)

**<font color=#1a73e8>作者：</font>** Junoh Kang, Kiseop Lee, Bohyung Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose ReLOBGen, a method for generating limit order book (LOB) messages that are replayable by construction. Replayability is required for closed-loop market simulation, yet existing LOB message generators may produce non-replayable raw messages, i.e., messages inconsistent with the current market state. These generators therefore rely on post-hoc correction or rejection followed by resampling, which may alter the replayed message distribution or increase inference cost. ReLOBGen instead ensures replayability during generation: it selects the referenced order from the resting orders in the current LOB and then generates the remaining message fields to be consistent with that order and the market state. For realistic reference selection, ReLOBGen samples from a learned distribution over eligible resting orders, efficiently computed from cached order representations and a context-dependent query. It then enforces the consistency of the remaining fields by masking out invalid tokens. Together, these components enable efficient generation of realistic messages without post-hoc correction or resampling. In 500-message rollouts, ReLOBGen achieves 100% replayability, improves market realism, particularly for top-of-book statistics and the relative prices of LOB messages, and provides a $2.7\text{-}3.6\times$ speedup per replayed message over the LOBS5 baseline.

---


### 21. [The Price of Token Boundaries: Compression Certificates and Prediction](https://arxiv.org/abs/2609.35869)

**<font color=#1a73e8>作者：</font>** Yuhao Du, Shunian Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pre-tokenisation restricts which text fragments can become prediction units, but its compression cost is obscured when tokenisers are compared only under the same boundaries. We measure this cost by bounding the minimum token count from both sides, with and without a regular-expression boundary rule. Nonnegative prices on token occurrences yield a lower bound through shortest paths and vocabulary-budget selection; maximising over all prices recovers the linear programming relaxation, and an independent integer checker certifies the reported values. On English Wikipedia, boundaries increase the optimal token count by 28.3--36.8\%. Byte pair encoding lies 2.1\% above the constrained lower bound, but 10.9\% above the unrestricted bound. Compression and prediction favour different dictionaries: at 85M non-embedding parameters and matched training-token budgets, unrestricted fitting yields higher mean held-out bits per byte under a common unrestricted decoder in all 12 languages in the paired study and 11 of 12 under independent tuning and evaluation. To study intermediate boundary policies, we introduce boundary licences, which limit the vocabulary entries permitted to cross cuts and admit the same form of certificate. On separate English and Chinese fitting corpora, licensing 10\% of the vocabulary budget recovers 85.2\% and 100.0\% of the achieved token-count reduction from removing all cuts. These results quantify the compression cost of boundaries while separating it from the prediction quality of the resulting token units.

---


### 22. [Risk-Averse Online POMDP Planning via CVaR of the Immediate Cost with Performance Guarantees](https://arxiv.org/abs/2609.35874)

**<font color=#1a73e8>作者：</font>** Yaacov Pariente, Vadim Indelman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online POMDP planners optimize the expected cumulative cost, which can mask dangerous states when the belief places significant mass on high-cost states. Existing risk-averse methods apply static or dynamic Conditional Value at Risk (CVaR) to the value function, capturing trajectory-level risk, but share two gaps: (i) by retaining the immediate cost as an expectation of a state-dependent cost over the belief, the risk \emph{within} the belief is left unaddressed; and (ii) by modifying the value function, they require new tailored algorithms rather than reusing existing expectation-based planners. We instead apply CVaR to the immediate cost over the belief at each step, directly targeting per-step uncertainty about the current state. The standard expected cumulative return is retained as the objective, so the resulting problem has a standard MDP structure: any expectation-based POMDP planner can be made risk-sensitive by changing only the cost computation. We inherit finite-time guarantees for policy evaluation and sparse sampling---with estimation error independent of the risk level---and, as our central theoretical result, prove a finite-time bound on the gap between the particle belief MDP surrogate and the original POMDP, which together yield an end-to-end guarantee from the true POMDP value to the algorithmic estimate. In the risk-neutral limit, the formulation recovers standard expectation-based planning.

---


### 23. [Hybrid Ensemble Learning for EEG-Based Epileptic Seizure Forecasting](https://arxiv.org/abs/2609.35876)

**<font color=#1a73e8>作者：</font>** Mason Dana, Khandaker Mamun Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Epileptic seizure forecasting aims to provide actionable warnings before seizure onset, yet patient-independent generalization and false-alarm control remain major challenges. We propose a calibrated hybrid ensemble for EEG-based seizure forecasting that combines five deep learning models and three classical machine learning models through a logistic regression stacking meta-learner. The proposed pipeline integrates signal preprocessing, handcrafted feature extraction, class-imbalance handling, probability calibration, and clinically motivated post-processing. We evaluate the framework on CHB-MIT using strict Leave-One-Patient-Out (LOPO) cross-validation, with threshold and post-processing parameters selected only on held-out meta data. On the filtered cohort, excluding patients with anomalous preictal rates below 1\% or above 15\%, the model achieves 74.2\% seizure-level sensitivity at 1.24 false alarms per hour, with an average warning time of 16.9 minutes. A test-tuned oracle constrained to the target false-alarm budget achieves 60.9\% sensitivity at 0.951 false alarms per hour, highlighting the importance of reporting sensitivity together with realized false-alarm rates. Our code is available at: this https URL

---


### 24. [From Static Policies to Adaptive Priors in Offline Reinforcement Learning](https://arxiv.org/abs/2609.35880)

**<font color=#1a73e8>作者：</font>** Tianwei Ni, Vineet Jain, Akash Karthikeyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) has traditionally focused on learning policies for direct deployment under conservative objectives, where uncertainty outside the offline dataset is treated pessimistically to ensure robustness. We argue that this formulation becomes incomplete when an offline-trained policy is subsequently updated through online interaction, as increasingly occurs in modern intelligent systems through test-time adaptation and online fine-tuning. This position paper argues that, in such settings, the objective of offline RL should extend beyond immediate deployment and instead prioritize learning adaptive policy priors: policies that preserve the capacity to improve during subsequent interaction through memory, exploration, and self-correction. We formalize this perspective as adaptive offline reinforcement learning (AORL), distinguish it from offline-to-online RL, and explain why adaptability becomes important under distributional shift, limited dataset coverage, and changing test-time conditions. We further discuss Bayesian offline RL as one principled direction for constructing adaptive policy priors by preserving epistemic uncertainty over plausible environments. Finally, we outline connections, open challenges, and research directions for treating offline RL as preparation for future experience rather than as a static deployment problem.

---


### 25. [Learning in the Transverse Subspace: A Minimal Representation for Divergence-Free Operator Learning](https://arxiv.org/abs/2609.35884)

**<font color=#1a73e8>作者：</font>** Yifei Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Divergence-free vector fields are fundamental state variables in incompressible flows and many PDE systems. Redundant parameterizations, including Neural Conservation Law (NCL) potentials, map multiple auxiliary representations to the same physical field. Our experiments show that this redundancy can reduce static representation-fitting error by enlarging the set of equivalent solutions, but the resulting many-to-one mapping does not provide a unique state for operator learning.
We introduce a minimal representation that encodes a real \(D\)-component divergence-free vector field on a \(D\)-dimensional domain as a real \((D-1)\)-component field on the same domain. Exploiting the transverse structure imposed by incompressibility in Fourier space, we use a Householder orthogonal transformation to construct the reduced coordinates directly. For periodic and closed impermeable fields, the transform is invertible, isometric, and angle-preserving. For open nonperiodic flows, Fourier extension constructs a compatible periodic field, and a minimum-energy rule selects a unique reduced representation.
Neural operators then learn temporal evolution entirely in this reduced space. At inference, the predicted \((D-1)\)-component field is decoded directly into a physical divergence-free \(D\)-component field, without predicting an ambient field or applying post-hoc projection.
Experiments on static fitting and temporal prediction reveal a task-dependent trade-off: redundancy facilitates static optimization, whereas unique invertible coordinates provide a well-defined state for temporal dynamics. By removing unconstrained longitudinal or null directions from the learned state space, the proposed formulation achieves lower prediction error and greater robustness while preserving divergence freedom by construction.

---


### 26. [Dual-Fit Imperative in Security Leadership: A Grounded Theory Investigation of CISO Role Enactment in Modern Organisations](https://arxiv.org/abs/2609.35887)

**<font color=#1a73e8>作者：</font>** Mazino Benson Onibere  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Chief Information Security Officer (CISO) has emerged as a strategically prominent executive role, confronting an adversarial environment, irreconcilable accountability tensions between security and business enablement, and a prevention paradox in which success remains invisible to resource allocators. Scholarly understanding of how the role operates across organisational contexts remains virtually absent, leaving practice without empirical foundation.
This thesis asks: how is the CISO role enacted across different organisational contexts in modern organisations? The study employs constructivist grounded theory with an abductive reasoning framework and the Gioia method, drawing on twenty interviews with Australian security executives.
The CISO role is not a stable configuration of responsibilities applied uniformly, but a continuously negotiated achievement. Effectiveness emerges from dual-fit maintenance: alignment between the leader and the internal organisational context (CISO-Organisation Fit) and the external environment (CISO-Environment Fit). These requirements transform across three maturity phases, Establishment, Maturation, and Strategic, with action-oriented, stewardship-oriented, and vision-oriented leaders generating effectiveness in each; effectiveness in one phase can undermine it in another. Political capital is the mechanism through which leaders navigate these shifting demands.
These patterns are synthesised in the Security Leadership Contingency Model (SLCM), the thesis's primary theoretical contribution. Instruments developed from the model translate these insights into guidance for leadership selection and succession planning. The SLCM extends person-organisation fit, person-environment fit, and contingency theory to security leadership, advancing understanding of executive effectiveness under accountability tensions and evolving contextual demands.

---


### 27. [The Decision Value of Perception Compute](https://arxiv.org/abs/2609.35910)

**<font color=#1a73e8>作者：</font>** Hoang Pham Cong, Ho Viet Duc Luong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive perception spends extra computation on inputs where perception is expected to improve. When perception feeds a downstream decision system, a better perception output need not produce a better decision. We define the decision value of perception compute as the change in downstream loss from escalating an input from a cheap to an expensive perception mode. Because this value can be negative, the allocation of perception compute should be judged against a budget-constrained decision oracle, with uniform full-fidelity inference as a baseline rather than an upper bound. We introduce DEEP (Decision Evaluation for Escalated Perception), a benchmark that scores pre-escalation allocators against this oracle under selection, latency and energy budgets, charging each allocator for its own computation. With deployed monocular geometry on KITTI and nuScenes, we find that 34--54% of the escalations that change downstream loss make it worse; harmful escalations also occur for the published PDM-Closed planner, evaluated open-loop on nuPlan with real detector outcomes. On nuScenes, perception-level gain frequently disagrees in sign with decision value. This mismatch has practical consequences: choosing among fixed deployable signals by missed-object perception gain rather than by decision value reduces realized test decision gain by 7.4% of the all-cheap loss on average. Learned allocators recover part of the oracle's value by finding beneficial escalations but select nearly as much harm as random, and once their own computation is charged at a 20% latency budget, only the lightweight routers, at about 3.5\% of a full detector pass, still beat random.

---


### 28. [Agentic Federated Learning: Rule-Based Client and Server Agents for Adaptive Training](https://arxiv.org/abs/2609.35914)

**<font color=#1a73e8>作者：</font>** Deepthy K. Bhaskar, VP Binu, B Minimol  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training across distributed clients without sharing raw data, making it suitable for privacy-sensitive applications such as healthcare, finance, and edge intelligence. However, conventional FL approaches rely on static client participation and fixed aggregation strategies, which limits their effectiveness under non-IID data distributions, heterogeneous client behavior, and noisy or unreliable updates. To overcome these issuess, this paper proposes an Agentic Federated Learning (AFL) framework that integrates lightweight rule-based autonomous agents at both client and server levels. The proposed framework introduces a Client-Side Agent (CSA) that dynamically adapts local training parameters, controls participa- tion, and evaluates update reliability, while a Server-Side Orchestrator Agent (SSOA) performs quality-aware client selection and adaptive aggregation. Unlike traditional FL methods, AFL enables context-aware decision-making during the training process, improving adaptability and robustness in dynamic distributed environments. Extensive experiments conducted on the CIFAR-10 dataset under IID, non-IID, and noisy-client settings demonstrate that AFL consistently outperforms standard base- lines including FedAvg and FedProx. Experimental results show improvements in classification accuracy, convergence speed, robustness against corrupted updates, and communication efficiency. Ablation studies further confirm the complementary contributions of CSA and SSOA, while statistical analysis validates the significance of the observed gains. The proposed AFL framework demonstrates that incorporating autonomous agentic reasoning into federated learning provides an effective and practical solution for intelligent, adaptive, and robust distributed learning systems.

---


### 29. [Replication Failure and Trivial Baselines in Road-Level Crash Prediction](https://arxiv.org/abs/2609.35917)

**<font color=#1a73e8>作者：</font>** Maurya Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks are increasingly applied to road-level crash prediction, but the stability of their reported gains has received little scrutiny. We independently reconstruct the data pipeline of a recent uncertainty-aware model and evaluate eleven of its design decisions across three London boroughs under an expanding-window protocol. Four survive replication on a second borough; seven do not, and four of those reverse sign rather than attenuate. Multi-seed evaluation is decisive: one effect reverses sign between random seeds within a single borough, and the reference architecture exhibits per-borough seed spreads of up to 35.7 points against 4 points for ours. We further compare both networks against a parameter-free baseline that ranks segments by cumulative past crash count. At matched history depth our model is statistically indistinguishable from that baseline ($-0.90$ points, $p=0.61$), and the reference architecture loses to it on 18 of 18 held-out windows ($-17.37$, $p<10^{-6}$). Sweeping the baseline's lookback horizon shows it spans 22.71% to 83.94% accuracy on that variable alone, and that every published figure in this line of work is matched by the baseline at a horizon of one to five years. We argue that the apparent margin of graph networks over historical baselines in this task is substantially an artefact of the short horizons those baselines were computed over, and recommend horizon-matched baselines and multi-seed reporting as minimum practice.

---


### 30. [TEE Anchor: Cross-TEE Organizational Endorsement for Mitigating TEE Physical Attacks](https://arxiv.org/abs/2609.35919)

**<font color=#1a73e8>作者：</font>** Ao Sakurai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In 2025, practical physical-access attacks against TEEs, such as this http URL and Battering RAM, were disclosed, posing a serious threat to current TEEs. The more strictly the target machine is guarded, the harder such attacks are to mount. Residing under trusted management has therefore emerged as a new security requirement. Yet existing attestation cannot prove a machine's organizational affiliation. This leaves room for an attacker to pass off a physically accessible machine under their control as one operated in a legitimate environment. We propose TEE Anchor, a mechanism that mitigates physical attacks by proving which organization manages a machine. TEE Anchor is a lightweight, X.509-based design that needs no additional root of trust such as a (v)TPM. The organization issues a certificate over the Chip ID, a unique per-CPU identifier, forming its own PKI. A Verifier then proves affiliation by matching the Chip ID in the attestation evidence against that certificate. This outperforms (v)TPM-based prior work in operational cost and deployability, applies across major TEEs without vendor lock-in, and lets any organization assert affiliation independently of TEE vendors. We implemented a prototype and confirmed that all operations, including provisioning and verification, complete within a few milliseconds.

---


### 31. [Almost Human, Except When It Matters: VoxParity and the Decisions a Voice Should Change](https://arxiv.org/abs/2609.35922)

**<font color=#1a73e8>作者：</font>** Bhavik Mangla  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A voice agent can handle almost every call on the words alone and still fail the few its sector's rules were written for. Emergency-call standards, fraud guidance, radio phraseology and vulnerability rules recognise that how a caller sounds, or what else is audible, can change the right action. VoxParity tests whether agents act on it. In 183 scenarios from 14 sectors, one transcript stays fixed while the audio changes (a coaching voice, a medical monitor beeping, a mayday under a radio check, noise over a drug name, a child's voice placing a bet, a frightened whisper), and with it the correct typed tool call. A words-only null test credits a system only if hearing the call moves its actions more than it moves a pipeline that only reads the words. Only 11 of the 23 systems that can also be run on the transcript pass. Descriptively, errors run toward the words: when the audio calls for protection, all 28 systems carry out the routine request more often than they over-react on clean calls (41% against 12% pooled; the words-only pipeline, 58% against 15%). Exploratory analyses place most of the leading systems' misses on cues they heard; systems beat the null almost entirely on items that state the rule; the leading systems overrule heard resignation or confusion far more often than acute alarm; and, in the models tested, describing the voice and stating the rule each recover part of the shortfall, leaving a gap on emotion.

---


### 32. [Grab a Coffee: Future-Aware Guidance for Discrete Diffusion with Compiled Objectives](https://arxiv.org/abs/2609.35924)

**<font color=#1a73e8>作者：</font>** Dongxin Li, Gwen Yidou-Weng, Guy Van den Broeck 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models generate sequences by iteratively resolving multiple tokens in parallel, offering a flexible alternative to left-to-right generation. However, guiding this process with a sequence-level objective is difficult because the value of one unresolved token depends on the other tokens with which it can form a high-reward sequence. Enumerating all such completions makes the whole guidance computation grow exponentially with the number of unresolved positions. We introduce COFFEE, a plug-and-play framework that avoids this enumeration by separating sequence dependence from the objective. At each diffusion step, a target-free carrier absorbs the marginal token distributions predicted by the denoiser to construct a joint model over the unresolved tokens, while a compiled finite-state model records how their combinations affect the sequence-level preference. Pairing their states allows COFFEE to transfer global preferences to unresolved positions and sample a clean reconstruction without retraining the diffusion model. The same framework supports explicit hard constraints and learned soft objectives. We evaluate COFFEE across multiple symbolic, language, and biological benchmarks, where it achieves strong control results with task-dependent quality and diversity trade-offs. By making objectives available to inference rather than only evaluation, COFFEE brings joint conditioning, completion-weighted guidance, and optimization-based constraints into pretrained neural generation, showing the potential of neural-symbolic methods in diffusion guidance.

---


### 33. [Normative Loss Landscape Navigation: A Trajectory-Based Approach to Mitigating Forgetting in Incremental Learning](https://arxiv.org/abs/2609.35926)

**<font color=#1a73e8>作者：</font>** Isabelle Aguilar, Zayn Andre Zainal, Luis Fernando Herbozo Contreras 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning models suffer from catastrophic forgetting when trained sequentially on non-stationary data distributions. Previously, this has been addressed through weight regularization. While preconditioning gradients offer a promising alternative to mitigate forgetting, current approaches are myopic. Conversely, standard regularization methods apply rigid, scalar Euclidean penalties that entirely ignore the underlying Riemannian geometry of the parameter space. To overcome this gap, we propose TMLN (Trajectory-Modulatory Landscape Navigation), a normative navigation policy that formalizes continual learning as an optimal control problem over a curved loss landscape. TMLN utilizes a memory-efficient diagonal empirical Fisher Information Matrix (FIM) to define a localized Riemannian manifold. To compensate for the spatial limitations of the diagonal approximation, TMLN dynamically modulates a preconditioner using the normalized historical trajectory of the network's parameter values. By integrating this trajectory-based preconditioning directly into the gradient update, we actively shield historically critical parameter directions without relying on additive penalties. Empirical evaluations on class- and domain-incremental benchmarks demonstrate that our method significantly reduces the loss barrier between consecutive tasks.

---


### 34. [CADENCE: A Confidence-Adaptive Dual-Expert Network for Fast and Accurate Time Series Classification](https://arxiv.org/abs/2609.35929)

**<font color=#1a73e8>作者：</font>** Onisa Mpaunda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series classification (TSC) exhibits a sharp trade-off between accuracy and computational scalability. Meta-ensembles like HIVE-COTE 2.0 reach state-of-the-art accuracy but require extensive compute, whereas ultra-fast random convolutional transforms (e.g., MiniRocket, Hydra) run in seconds but struggle with phase-independent distributions, signal kinematics, and decision tree fragmentation on large class counts.
In this work, we present CADENCE (Confidence-Adaptive Dual-Expert Network for time series Classification Excellence), a unified, CPU-native dual-expert architecture. CADENCE decouples representation learning into two specialized pathways: (i) a Convolutional Linear Expert pairing 10,000 deterministic dilated features with closed-form L2-regularized Woodbury ridge classification, and (ii) a Distributional Interval Expert pairing competing dilated kernels (Hydra) with dyadic Cornish-Fisher moment approximations across signal kinematics and FFT spectral bands, fitted with an ExtraTrees ensemble. An internal validation meta-router with rare-class preservation dynamically selects between pure expert routing and confidence-weighted soft blending, followed by a full refit on 100% of training data.
Evaluated across all 109 equal-length UCR Archive datasets over 30 resamples (3,270 total runs), CADENCE achieves a grand mean accuracy of 0.8864. This ranks #2 across the archive, surpassed only by HIVE-COTE 2.0 (0.8895, p_Holm = 0.295, no statistically significant difference), while outperforming Hydra+MultiRocket (0.8818), MultiRocket (0.8797), and HIVE-COTE 1.0 (0.8786, p_Holm = 0.048). CADENCE closes the gap to HIVE-COTE 2.0 to 0.31 percentage points while taking an average of only 17.53 seconds per dataset on a dual-core CPU. Source code and evaluation scripts: this https URL

---


### 35. [Bregman Consensus](https://arxiv.org/abs/2609.35930)

**<font color=#1a73e8>作者：</font>** Andrei N. Soklakov  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Consider a community of agents who are seeking consensus on a set of parameters. The agents agree to use the same Bregman-type divergence to quantify disagreement between their individual estimates of the parameters but have varying confidence in each other's abilities. Each agent is happy to revise their estimate by moving to the weighted barycenter of all individual estimates with higher weights applied to more trusted agents. We show that such revisions naturally lead to an iterative algorithm which converges to a unique consensus estimate of the parameters. Furthermore, since the consensus estimate is itself a barycenter with computable weights, the group emerges as a collective super-agent with a well-formed opinion regarding the ability of each individual agent.

---


### 36. [Graph neural networks for sampling-invariant embeddings of organized signal sets](https://arxiv.org/abs/2609.35934)

**<font color=#1a73e8>作者：</font>** Martin Bauw, Santiago Velasco-Forero, Jesus Angulo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensor networks and radars can deliver signals as organized sets, e.g. ordered signals, signals describing range cells within a grid or signals perceived as graph nodes. Within such sets, individual signals may be characterized by distinct sampling parameters. This paper investigates organized signal sets neural network encoders. In the context of this work, the purpose of such encoders is to project heterogeneously sampled signal sets into an arbitrary fixed-size vectors space. This new representation space is designed so that signal sets can be processed as vectors rid of sampling differences to allow for arbitrary topology-aware processing with no signal processing constraints. Within this representation space designed to reduce the influence of heterogeneous sampling parameters, the relevance of signal sets representations is evaluated by considering signal sets discrimination potential with a focus on waveforms separation. The encoding and embeddings discrimination experiments conducted rely exclusively on synthetic complex-valued radiofrequency signals.

---


### 37. [Embodied Semantic Communication for Collective Autonomous Agents: A Tutorial on Representation, Wireless Delivery, and Closed-Loop Coordination](https://arxiv.org/abs/2609.35936)

**<font color=#1a73e8>作者：</font>** Yizheng Huang, Wensheng Lin, Lixin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As autonomous systems and embodied intelligence enter the dynamic physical world, multi-agent collaboration calls for a paradigm shift in communication design. However, existing communication paradigms overlook that agents form action understanding from their own states, environmental observations, and collaboration relations through a process that evolves as a task unfolds. Consequently, reliable bit delivery, general semantic recovery, or single-task utility optimization alone cannot ensure that heterogeneous agents form coordinated actions compatible with their own conditions from shared information during task execution. To address this gap, this paper proposes embodied semantic communication (ESC) as a paradigm that transforms information transmission into action-oriented semantic interaction. Specifically, ESC characterizes how an explicit communication link can encapsulate multimodal perceptual states, intrinsic hardware capabilities, and collaborative intents into unified actionable semantic representations, thereby enabling heterogeneous receiving agents to parse, align, and ground them in local motor control. This paper clarifies the conceptual boundary, system characteristics, and environment-constrained technical pathways of ESC. It maps the underlying mathematical tools, including semantic information theory, world models, and multi-agent decision theory. Finally, this paper summarizes key open challenges, including measurable semantic reliability, ambiguity-triggered interaction under dynamic environments and tasks, and bandwidth-adaptive semantic transmission, outlining a roadmap for collective embodied networks.

---


### 38. [KernelOnet: An Interpretable Neural Operator Based on Kernel Functions](https://arxiv.org/abs/2609.35938)

**<font color=#1a73e8>作者：</font>** Yuan Guo, Hanshu Chen, Qiang Xi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes an interpretable neural operator framework, the Kernel Operator Network (KernelOnet), which incorporates kernel functions explicitly into the neural operator architecture, so that the operator structure matches the kernel-expansion form used in boundary-type kernel-expansion methods. Unlike traditional neural operators such as DeepONet, which learn basis functions implicitly through deep networks, KernelOnet replaces the trunk network with explicit kernels and offers three complementary kernels: a data-driven learnable kernel, in which a neural network parameterizes a radial basis function learned from data, and which for constant-coefficient linear problems can be regarded as a non-singular fundamental solution; a physics-informed kernel, which embeds physical information such as analytic fundamental solutions into the network structure, so that the expansion satisfies the governing equation automatically and can be trained without supervision on boundary conditions alone, with no interior solution data; and a hybrid kernel, which splits the solution, according to the linear principal part of the governing equation, into a homogeneous part spanned by analytic fundamental solutions and a source part carried by low-rank learned correction kernels, thereby balancing physical priors against data fitting on nonlinear problems lacking an analytic fundamental solution. On three benchmarks and one engineering problem in a shallow-water waveguide, KernelOnet attains high accuracy; where comparable with DeepONet, it is more accurate with fewer learnable parameters. Its unsupervised configuration needs no interior solution labels, and its per-query inference cost is far below that of per-instance solvers, offering an effective route to acoustic propagation in unbounded exterior domains that general-purpose neural operators struggle to handle.

---


### 39. [HERO: Histology Encoder for Robust Representation in Oncology](https://arxiv.org/abs/2609.35943)

**<font color=#1a73e8>作者：</font>** Zhi Li, Eghbal Amidi, Yating Cheng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models trained on large pathology image corpora now provide strong, transferable representations for computational pathology. Over the past few years a series of such models has been released, each trained on more slides than the last; on standard classification and segmentation benchmarks, the leading models are now separated by small margins. In clinical use, however, the foundation model is applied to images from hospitals, scanners, and staining protocols outside its training data. Encoders generally embed these acquisition factors alongside biological information, which may introduce downstream errors and hinder safe clinical adoption. A pathology foundation model should therefore be robust to acquisition shift without giving up representation quality, yet robustness is seldom the axis along which models are compared. In this report, we introduce HERO (Histology Encoder for Robust Representation in Oncology), a ViT-G/14 pathology foundation model trained with the DINO and iBOT objectives and refined with high-resolution Gram anchoring on a morphology-balanced corpus of 500 million tiles from approximately 575,000 clinical whole-slide images. Across the evaluated public benchmarks, HERO shows the strongest robustness to center, scanner, and stain variation among the compared state-of-the-art foundation models, performs comparably on tile-level classification, segmentation, and gene-expression prediction, ranks first on average across 39 evaluated slide-level clinical tasks, and, under an equal-weighted framework-level analysis, has the best average rank across the six benchmark frameworks.

---


### 40. [EnJoi: Ensemble Joint Score Filter for Generative Data Assimilation](https://arxiv.org/abs/2609.35944)

**<font color=#1a73e8>作者：</font>** Julien Moreau, Marc Lelarge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data Assimilation (DA) aims to recover the full state of a dynamical system that is only partially observed. A solution is to use Score-based models to generate physically consistent trajectories that agree with the observations. These Autoregressive Diffusion models are trained by conditioning on the previous state; however, they do not take into account the uncertainty of their past predictions. We propose a new diffusion-based assimilation algorithm that dynamically balances the confidence in the current state and the new observations. Crucially, we choose to learn the distribution of the joint state containing both the past and future. This allows us to use a modified version of En4DVar, a classical DA algorithm that relies on the covariance of an ensemble of particles. Experiments on fluid and traffic flow simulations show improved reconstruction performance, especially in situations where observations are sparse and non-homogeneous.

---


### 41. [Intrinsic Associative Memory on Riemannian Manifolds: Curvature, Capacity, and Emergent Modes](https://arxiv.org/abs/2609.35948)

**<font color=#1a73e8>作者：</font>** Krishnakumar Balasubramanian, Zhaoyang Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geometry does more than constrain an associative memory: curvature determines what it remembers and which states it creates. We develop intrinsic dense associative memories on Riemannian manifolds by casting memory as Epanechnikov kernel-density mode seeking. We compare geodesic and volume-corrected energies and show that curvature separates their behavior. We prove that geodesic memory always retains an isolated pattern, while corrected memory obeys a sharp Ricci-curvature threshold: positive curvature can erase memories in high dimensions, while negative curvature reinforces them. We derive geodesic capacity scalings of $q_\beta^{-1/2}$ for retaining every pattern and $q_\beta^{-1}$ for a typical one, where $q_\beta$ is the pairwise kernel-overlap probability. We show how overlap \emph{creates} novel memories: designed $N$-pattern configurations realize all $2^N-1$ subset modes, but random data at the storage threshold yield only a Poisson number. We establish exact one-step recall using Riemannian mean shift. In simulations, we recover the predicted curvature transition and every designed mode. On WordNet's full noun hierarchy, we demonstrate that volume correction improves low-capacity retrieval. Together, our work shows that curvature is a design variable for associative memory, not merely a property of the data.

---


### 42. [When Privacy Becomes a Weapon: Understanding Doxxing and Privacy Vulnerabilities in Mainland China's Social Media Ecosystem](https://arxiv.org/abs/2609.35951)

**<font color=#1a73e8>作者：</font>** Xiao Zhan, Shijing He, Chi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Doxxing, the malicious disclosure of personal information, has become a pervasive privacy threat. Yet existing research remains predominantly Western-centric, limiting our understanding of how doxxing unfolds in contexts where mandatory identity systems, platform governance, and cultural logics fundamentally reshape privacy risks and harm trajectories. We address this gap through semi-structured interviews with 18 doxxing survivors in mainland China, synthesizing their experiences into a framework conceptualizing how doxxing operates in this context. Our findings reveal both patterns echoing prior Western findings, such as platform amplification mechanisms that resonate with Western findings, and China-specific dynamics shaped by the interplay of regulatory mandates (compulsory identity linkage) and cultural logics including nationalist discourse, fandom culture, Confucian values, and low privacy literacy. Survivors' experiences further reveal how doxxing reshapes understanding of privacy: from preference to precondition, from momentary disclosure to temporal vulnerability, and from individual control to structural powerlessness. These insights challenge agency-centered privacy frameworks and suggest that effective protection requires constraining systemic vulnerabilities rather than relying solely on user empowerment. We conclude by proposing multifaceted recommendations spanning legal reform, platform design, and social initiatives.

---


### 43. [HEIR: Learning Human-Entity Interactions with Functional Roles](https://arxiv.org/abs/2609.35955)

**<font color=#1a73e8>作者：</font>** Di Wen, Wenhao Guo, Yuedong Tan 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human-entity interactions requires recovering each person-action event's participants, roles, and shared identities. This structure can support embodied agents by clarifying who acts on which entities and how, informing anticipation and coordination in shared environments. Standard HOI metrics score individual links, leaving complete event composition undermeasured. We introduce HEIR (Human-Entity Interactions with Functional Roles), an image benchmark for complete grounded participant-role sets across object, interpersonal, and self-directed interactions. It contains 18,730 images, six roles, 105 actions, and 437 nouns, with shared entities, role changes, and repeated fillers; 51.6% of images contain multiple actors and 62.1% contain multiple actions. HEIR pairs relation AP with complete-set AP and structural evaluation. We also introduce CoRISP (Compositional Role-aware Interaction Set Prediction), which uses shared entity identities to combine role-conditioned evidence and predict normalized participant-role sets. Cardinality and role-multiplicity potentials couple assignments through event size and role composition, with exact per-event normalization. Across 16 baselines, relation and complete-event rankings diverge even after aligning action weights. CoRISP leads the evaluated systems on repeated-role events and shared-participant images in HEIR by 2.87 and 3.82 Set mAP points, respectively. On V-COCO, CoRISP achieves 73.72/76.23 role AP and 61.06/68.59 complete-set AP on two-slot actions under Scenarios 1/2. These results show the value of learning and evaluating event composition alongside individual relations. The code and dataset are publicly available at this https URL.

---


### 44. [Making Cross-Continental Federated Learning Repeatable with FLIP: a Multi-Application Study](https://arxiv.org/abs/2609.36001)

**<font color=#1a73e8>作者：</font>** Rafael Garcia-Dias, Alexandre Triay Bagur, Chayanin Tangwiriyasakul 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) in healthcare remains challenging, as the overhead of rebuilding governance guarantees for every collaboration stops most projects at the proof-of-concept stage. Here we present FLIP (Federated Learning Interoperability Platform), an open-source, multi-application platform that makes FL training and evaluation repeatable. FLIP implements common FL workflows as a set of composable services: cohort queries against per-site structured databases, on-demand DICOM retrieval from institutional PACS, per-site project approval, and reusable FL job types. To demonstrate FLIP, we ran two distinct use cases, federated fine-tuning and federated evaluation, on synthetic chest X-ray cohorts across two client nodes based in the United Kingdom (UK) and Thailand. In FLIP, each institution independently approves its participation in each project and operates its own node under local IT security processes. This study makes an operational rather than an algorithmic claim. It does not compare federated with centralised training; for that question, we refer the reader to existing systematic reviews and meta-analyses. The central result is evidence that such platforms enable international FL collaboration and improve repeatability, auditability, and site-specific governance. We also present a comprehensive comparison of existing platforms to help researchers and operators choose the right platform for their use case.

---


### 45. [Persistence Forcing: Exploiting Feature Specialization in Pixel-Space Diffusion](https://arxiv.org/abs/2609.36014)

**<font color=#1a73e8>作者：</font>** Chong Wang, Zixuan Fu, Shiqi Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space diffusion Transformers (DiTs) directly operate on high-dimensional visual data, yet their hidden representations typically undergo uniform refinement across depth. Natural images, however, are inherently organized at different levels of granularity. Global structure can often be represented compactly, whereas local textures and fine details require richer representations. Motivated by this, we introduce heterogeneous refinement in pixel-space DiTs, assigning different feature groups distinct refinement budgets across depth. Consequently, an ordered feature specialization emerges: sparsely refined features predominantly encode global visual structure, whereas more frequently refined features increasingly specialize toward localized, high-frequency details. We refer to these two groups as persistent and active features, respectively. Building on this emergent specialization, we introduce Persistence Forcing (PerF), which explicitly exploits this persistent--active feature organization for pixel-space image generation. This enables persistent features to continuously condition actively refined features, allowing stable global information to guide the ongoing refinement of finer visual details. During generative sampling, this interaction further induces a meaningful guidance direction that promotes coherent global structure and naturally complements classifier-free guidance. On ImageNet $256\times256$, PerF-L achieves FID of $1.91$, approaching $1.86$ of JiT-H with only half the parameters, while PerF-H further achieves FID of $1.63$ and $1.76$ on ImageNet $256\times256$ and $512\times512$, respectively.

---


### 46. [CoDimRecon: Agentic Reconstruction of Sim-Ready 3D Scenes with Deformable Curves, Surfaces, and Volumes](https://arxiv.org/abs/2609.36024)

**<font color=#1a73e8>作者：</font>** Shuzhao Xie, Lelin Wang, Guying Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing simulation-ready 3D scenes from real-world observations enables robotics, gaming, and immersive applications, yet existing methods largely assume rigid objects. This leaves an important gap for deformables, whose simulation-ready geometry depends on dimensionality (curves, surfaces, or volumes) and whose behavior may require models beyond elasticity. We present CoDimRecon, an agentic framework that reconstructs editable scenes containing rigid, articulated, and deformable objects from multi-view RGB observations. Scene-level geometric priors ground scale and layout, while object-level generated meshes guide the agent toward detailed, compact geometry; articulated rigid objects are decomposed into movable parts with explicit joints. For deformables, category-wise agent sessions reconstruct curves as centerlines with radii, surfaces as manifold shells with thickness, and volumes as watertight solids for volumetric meshing. Reusable simulator skills initialize compatible physical models and parameters, while agent-guided behavioral tests expose mismatches and trigger targeted revisions of motion, geometry, numerics, or material modeling. On evaluated Replica and ScanNet++ scenes, CoDimRecon achieves competitive compositional reconstruction accuracy while additionally producing deformable assets for rod, shell, and solid simulation. We further demonstrate robot interactions across all three representations, including a controlled paper-folding case in which behavioral testing motivates plastic bending.

---


### 47. [Preferent Compression Bounds Are Tight](https://arxiv.org/abs/2609.36030)

**<font color=#1a73e8>作者：</font>** Dario Paccagnan, Marius Tirlea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The lack of rigorous safety and performance certificates remains a key bottleneck to the deployment of modern learning-based methods. Sample compression has recently emerged as a powerful tool for deriving such certificates, with particularly sharp bounds available for algorithms satisfying a so-called preference property -- also known as stability in the learning theory literature. These bounds find direct application across domains as different as the Scenario Approach, Pick-to-Learn, and Support Vector methods. However, whether they are tight has remained an open problem. In this paper we resolve this question affirmatively and show that the state-of-the-art bound for preferent compressions is provably tight. We establish this by exhibiting an explicit construction based on the uniform distribution and order statistics that attains the bound in the limit. Along the way, we also provide a considerably shorter and more accessible proof of this bound, requiring only elementary counting arguments and no infinite-dimensional duality.

---


### 48. [Multi-Class, Multi-Tier Network Intrusion Detection: A Comprehensive and Reproducible Benchmark](https://arxiv.org/abs/2609.36039)

**<font color=#1a73e8>作者：</font>** Yufeng Xin, Bryant Goseland, Mohamed Rahouti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) and deep learning (DL) have dominated Intrusion Detection System (IDS) research in recent years. Unfortunately, many existing studies have produced inflated results and unreliable benchmarks due to critical oversights and mistakes in the ML and DL pipeline, from data collection and labeling to feature engineering and model training and evaluation. CIC-IDS2017 is a standard benchmark for network intrusion detection. Still, many published results on this dataset are difficult to compare due to labeling errors, inconsistent flow extraction, potential leakage, and performance evaluation metrics dominated by benign traffic. In this paper, we present a comprehensive benchmark with corrected PCAP-level labeling and a complete evaluation pipeline with diverse ML models. We evaluate eleven tabular classifiers at three nested levels: binary attack detection, nine-class attack-family attribution, and fifteen-class fine-grained classification. A soft-voting ensemble of Random Forest, XGBoost, and LightGBM obtains the best fine-tier macro-F1 of 0.955, with coarse and binary macro-F1 scores of 0.980 and 0.999, respectively. We further conducted a feature selection study based on an analysis of feature importance. This comprehensive benchmark pipeline is configurable and open-source, enabling new feature extraction and model plugins for new datasets. Future work should use this pipeline as a reference point for richer features, rare-class analysis, and model generalization towards new datasets and attack classes.

---


### 49. [Neural networks for spectral optimization](https://arxiv.org/abs/2609.36047)

**<font color=#1a73e8>作者：</font>** Alexis de Villeroché, Beniamin Bogosel, Stéphane Breuils 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a functional dependent on the spectrum of a differential operator, we address the problem of finding a domain which optimizes this functional. PDE solvers might be used to tackle this optimization. It is however computationally expensive. We propose two neural network models which learn the spectrum directly from the geometry of the domain and can be used to optimize the domain from one or more eigenvalues. We investigate two representations. The first encodes the domain through Fourier coefficients and a light MLP, which is efficient on star-shaped geometries, achieving a precision of 0.2\%. Through a rescaling of the coefficients the designed models satisfy the scaling law of the eigenvalues. Additionally, averaging the outputs of the trained surrogates over rotations and reflections induces invariance for these transformations. The second is a model that takes the landscape function, the indicator function and the gradient of the landscape function. A Gram-Schmidt process produces orthogonal eigenfunctions as output of the model along with the associated eigenvalues. The landscape model reaches 1\% mean relative error on the first ten eigenvalues, compared with 4\% for an FNO model. Replacing the landscape by an SDF worsened both prediction and optimization errors. The trained model also generalizes from synthetic shapes to domains given as classical image dataset. The resulting surrogates of both approaches recover classical spectral optima such as the disk for the first eigenvalue or the conjectured minima of higher eigenvalues. This confirms that our models produce accurate differentiable estimates of eigenvalues, which can be used in shape optimization problems involving spectral quantities.

---


### 50. [Improving scalable oversight with co-trained monitors](https://arxiv.org/abs/2609.36049)

**<font color=#1a73e8>作者：</font>** Joseph H. Rudoler, Kevin Tan, Benedict Tessler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Worker-monitor setups are a promising approach to AI oversight, but training workers against fixed monitors can incentivize monitor evasion. We study whether this failure mode can be avoided by co-training the monitor alongside the worker, and explore both supervised and self-supervised approaches. In the supervised setting, we prove a characterization: monitoring is possible with vanishing error and query rates exactly when the class of possible monitor functions has finite Littlestone dimension. This connects worker monitoring with an established literature on adversarial online learning. For self-supervision, we propose a co-training procedure based on test-time distillation: the monitor uses additional test-time compute to generate training labels, then trains its standard-compute policy on those labels. For majority-vote labels, we give a finite-sample sharpening guarantee under adaptive worker distributions with action coverage, that shows that the monitor's verdicts converge to its initial modal verdicts. We stress-test the former in code-security settings where the worker is trained adversarially to fool the monitor. Our results suggest that adaptive monitors are better at keeping pace with evolving worker strategies, while fixed monitors are more vulnerable to evasion.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
