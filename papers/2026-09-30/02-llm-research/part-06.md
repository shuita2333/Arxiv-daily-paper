# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 251. [CLAIRE: A Schema-Grounded Hybrid Workflow for Healthcare Administrative Form Completion](https://arxiv.org/abs/2609.32787)

**<font color=#1a73e8>作者：</font>** Garapati Keerthana, Manik Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare administrative staff transfer structured information from electronic health records, referrals, claims systems, provider rosters, and work queues into dynamic forms. We developed and evaluated CLAIRE (Clinical Language and Agentic Intelligence for Reasoning and Entry), a hybrid workflow that separates field-state discovery, source-to-field mapping, deterministic validation, bounded correction, escalation, and audit tracing. We tested five synthetic healthcare administrative schemas, 1,000 source records, four interface variants, two data-quality suites, and six comparators, yielding 24,000 benchmark episodes. A separate strict-output audit evaluated direct mappings from Qwen2.5-1.5B and Qwen2.5-7B, and a trace-derived operational simulation covered 6,000 episodes. Under the evaluated synthetic benchmark conditions, full CLAIRE achieved 1.000 episode success, field accuracy, required-field completion, and dependency completion in both suites; removing validation reduced stress-suite success to 0.500. In the simulation, 100.0% of clean and validation-stress episodes reached a staff-reviewable draft, compared with 68.6% of escalation challenge episodes, unsupported cases were blocked. Scenario-based savings were 149.7-165.5 seconds per case, not observed staff times. The findings support schema-grounded, validation-first healthcare administrative automation in which language-model components assist mapping but do not authorize unsupported or consequential actions.

---


### 252. [Getting Motif-ated: Controllable AI Compositions from Injected Motif Prompts](https://arxiv.org/abs/2609.32788)

**<font color=#1a73e8>作者：</font>** Chao Peter Yang, Cynthia Rudin, Yue Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has transformed symbolic music generation by borrowing the training paradigms of large language models, with systems such as NotaGen now producing complete, stylistically convincing classical scores from a short prompt. These systems could become powerful creative partners, helping musicians generate endless possibilities. However, current systems expose almost no control handles on the music itself. In principle, control handles could be built into a foundation model trained from scratch, but this is rarely practical without massive amounts of quality annotated data and compute resources. We therefore present MotiGen, a recipe for retrofitting pretrained symbolic music models to use new instruction prompts. MotiGen injects a musical motif as a structured prompt line, reinforces it with a scalar attention bias toward the motif tokens, and learns the association with a two-phase curriculum. First, it learns from focused excerpts cropped around motif occurrences in the training data, then full scores including the motifs. Our experiments show that our model composes with the prompted motif in over 92.3\% of generated pieces. Generated pieces using a variety of motifs are included in our sample site: this https URL.

---


### 253. [$T^5$: Twin-Critic Training for Token-Level Thoughts in Reinforcement Mid-Training](https://arxiv.org/abs/2609.32791)

**<font color=#1a73e8>作者：</font>** Nan Qiao, Yebin Yang, Weinong Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement mid-training lets language models learn internal thoughts from unlabeled text, but efficient token-level credit assignment remains challenging. Existing group-relative methods require costly repeated generation. Learned critics offer single-rollout feedback, but accurate return prediction alone does not ensure reliable policy updates. Our analysis shows how training--inference mismatch and PPO clipping prevent a common offset in advantage estimates from cancelling out, introducing additional update drift. We propose \tfour{}, a twin-critic method that calibrates token-level advantages from a single generated trajectory. After warmup and held-out qualification, the critics provide two advantage estimates, combined using action-dependent weights learned through a conditional-moment saddle-point objective. This objective brings the average advantage at each prefix toward zero, while a signal-retention constraint prevents the correction from erasing the learning signal. Sharing information across text positions avoids repeated sampling of each prefix. Theoretically, we characterize optimal mixing under the signal-retention constraint and establish an upper bound on residual mean-induced drift. Experiments show that, compared with the state-of-the-art critic-free method, \tfour{} improves mean benchmark performance by 7.8\% and reduces mean training-step time by up to 63.4\%.

---


### 254. [Understanding and Exploiting Anisotropy in Post-Training](https://arxiv.org/abs/2609.32792)

**<font color=#1a73e8>作者：</font>** Samyak Jha, Harshvardhan Saini, Yizhen Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM post-training combines supervised fine-tuning (SFT), a mode-covering forward-KL objective, with reinforcement learning (RL), a mode-seeking reverse-KL objective. Frequency-weighted likelihood training leaves a well-known signature: \emph{anisotropy}, in which a few residual channels carry disproportionately large activations. Anisotropy is widely documented and usually treated as a defect, yet its function and its interaction with post-training remain unclear. We first analyze it. A label-free outlier rule isolates about 5\% of residual channels that are essential for language modeling: removing them raises perplexity from 10 to over $10^6$, versus 35 for count-matched random channels. Yet they barely distinguish correct from incorrect reasoning. SFT reshapes them, whereas RL leaves them largely intact and adapts the complementary channels. These channels therefore form the model's \emph{coherence substrate}, and reasoning adaptation happens elsewhere. We then exploit this. \textsc{SphereGate} learns one bounded gain per residual channel on a frozen backbone. Its activation-weighted gradients provably limit movement of high-energy coherence channels and leave the remaining channels free. With 0.1M trainable parameters, \textsc{SphereGate} outperforms parameter-efficient baselines by 2.0--7.3 points on MATH-500 across Qwen2.5 (0.5B--7B) and Llama-3-8B, is comparable or exceeds full-model GRPO. Anisotropy is not a defect but a division of labor that post-training can exploit.

---


### 255. [AgentHabit: Characterizing Distinct Behaviors of Agents on Everyday Tasks](https://arxiv.org/abs/2609.32795)

**<font color=#1a73e8>作者：</font>** Woojung Song, Hoyeol Yang, Jeonghoon Shim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents assist users with everyday tasks that can be completed in many reasonable ways. Even when their answers are useful, how agents carry out these tasks may not match users' preferences and needs. For example, agents differ in whether they ask clarifying questions or search the web. We introduce HABIT, a taxonomy of 23 behavioral axes in five categories, which three authors and three LLMs derive bottom-up from 408 agent trajectories across 17 domains. On held-out tasks, HABIT distinguishes models more clearly than existing taxonomies of human values and agent actions while supporting comparably consistent annotation. Building on HABIT, we construct AgentHABIT, a benchmark that profiles each agent's behavioral tendencies from its trajectories on 86 everyday tasks. Profiling 18 models with AgentHABIT reveals a range of distinctive tendencies. For example, most GPT and Claude models state their assumptions and offer alternatives when requirements conflict, whereas Qwen and Google's models more often leave assumptions or changes to requirements unstated. These profiles remain recognizable even when built from entirely different sets of tasks, indicating that they reflect general tendencies rather than task-specific behavior. Prompting agents to adopt specific behaviors shifts some axes readily but barely changes others, while fine-tuning on another model's trajectories changes only part of a model's profile and leaves much of it intact. Overall, HABIT and AgentHABIT provide a systematic framework for characterizing how agents carry out everyday tasks beyond task success, offering insights to guide the development of agents whose behavior better fits users' needs.

---


### 256. [Re-derivability Decides What a Staged Agent Pipeline Recovers After an Upstream Fault](https://arxiv.org/abs/2609.32802)

**<font color=#1a73e8>作者：</font>** Tianqi Bu, YuXuan Peng, Junteng Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> One variable sets what an upstream fault costs a staged pipeline of language-model agents: re-derivability, how much of what a stage needs it can rebuild from the original problem. Grounding an inspector agent in that problem is worth +0.608 [+0.517, +0.700] to +0.358 over a blind one on four open-weight backbones served with thinking disabled, and on the two Qwen backbones the blind inspector changes no item at all. That head-to-head is exploratory. One deterministic fault enters the first stage, and we re-expose the original problem to $k = 0,\dots,3$ of the downstream stages with agents, items, fault and topology held fixed, on 120 gsm_hard items per arm at temperature zero. Accuracy under fault rises on four of four backbones, from +0.233 to +0.392, the largest Holm-adjusted $p$ being $2.1\times10^{-6}$. A registered kill test rules out tokens. Blanking every word holds the word slots fixed, and retention tracks the visible fraction on four of four, climbing from 0.221 to 0.692 on the primary. Those two families are confirmatory and everything else here is exploratory. The interaction excludes zero on two of four backbones under the registered pipeline, four of four under a three-stage pipeline, and three of four under full message history, the primary at +0.317. On Llama-3.1-8B the fault carries no detectable cost at any dose, so the other three carry every claim about what a fault costs. Re-derivability also sets what the architecture costs, and no decomposition we measured reliably beats one direct call. With no fault injected the registered pipeline loses to that call by -0.267, -0.125 and -0.317, and on Phi-4 reads +0.058 at $p = 0.118$, which the test fails to separate from zero. The repair that works is cheap and front-loaded: the first re-grounded stage buys +0.394 of matched retention for +59.8 tokens per item on Qwen3-14B, and the stages after it buy nothing.

---


### 257. [Nutri-ATLAS: Embodied Agent for Tabulated Lookup and Assistance for Smarter nutrition](https://arxiv.org/abs/2609.32803)

**<font color=#1a73e8>作者：</font>** Uttej Kallakuri, Boxun Hu, Ankur A. Butala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative and Agentic IoT systems offer a promising foundation for digital healthcare applications that combine sensing, personalized reasoning, and autonomous interaction in real-world environments. Nutrition assistance is a natural use case, but existing Large Language Model (LLM)-based systems are often limited to passive text interaction and static context, making them unreliable when food descriptions are ambiguous or nutritional evidence is missing. We propose Nutri-ATLAS, an Embodied Agent for Tabulated Lookup and Assistance for smarter nutrition in the real world. It integrates graph-grounded nutrition reasoning, hardware-aware LLM selection, and robot-based evidence acquisition. Nutri-ATLAS builds a unified Food-Nutrient knowledge graph from USDA FoodData Central and FoodKG and learns 64-dimensional GATv2 food and recipe embeddings. A shared hybrid graph-text scoring mechanism supports food nutrition extraction, nutritional gap filling, substitute retrieval, and recipe-level meal composition, while an LLM-guided skill interface navigates landmarks, updates dietary-context and food-accessibility memory, and grounds recommendations in observed food availability. We evaluate Nutri-ATLAS across nutrient estimation, substitution retrieval, recipe recommendation, patient-profile adherence, edge deployment, and real-world embodied execution. On HealthyFoodSubs, the hybrid retriever achieves 37.9% MAP, 80.7% RR@5, and 90.1% RR@10. On NutriBench v2, Dense+GAT retrieval grounds nutrient estimation across nine quantized Qwen3.5-9B configurations. On PFoodReQ, Nutri-ATLAS reaches 78.8% MAP, 83.0% MAR, and 77.5% F1. A patient-profile study shows adherence to allergy and healthy-target constraints for all selected cases.

---


### 258. [Decision-Sufficient State Representations: Measuring and Reducing Write-Time Regret](https://arxiv.org/abs/2609.32805)

**<font color=#1a73e8>作者：</font>** Bingyu Shen, Boyang Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long tasks produce more history than an LLM agent can hold in its context, and more than it uses reliably even when the history fits. A growing line of work therefore has agents carry a short written state instead: at every step a writer rewrites the state, and a reader acts from the state alone. Steps stay cheap, but anything the writer drops is lost before later decisions reveal that they need it. We quantify this loss and ask whether training can reduce it. Comparing the written state with the best state of the same size written in hindsight, we split the reader's loss into a budget loss, which any state of that size must incur, and a write-time regret, which comes from the writer's choices. In TextWorld cooking games where we control how long a fact must be carried before it is needed, a 128-token state holding the facts wins nearly every game, while prompted language-model writers win at most 17%. Almost all of the loss is write-time regret, and it grows with the delay. We then train the writer from the reader's own loss. DSSR (decision-sufficient state representations) scores candidate states by how well the reader acts after the writer carries them forward, and teaches the writer to prefer the better ones. This forward-rolled score predicts game outcomes ($\rho = 0.48$), whereas scoring a candidate as a fixed context, as hindsight methods usually do, does not ($\rho \leq 0.07$). On a pre-registered test split opened once, training adds +7.0 [+1.9, +12.2] points of success when facts are needed soon, bringing a plain summary writer to the level of belief- and slot-based memory prompts. The gain shrinks as the delay grows and is significant only at the shortest delay. We trace this limit to credit assignment: keeping a fact now pays off only if every later rewrite keeps it too, which a per-step score cannot see.

---


### 259. [Beyond Accuracy: Counterfactual Fragility and Demographic Bias in Clinical Evaluation of LLMs](https://arxiv.org/abs/2609.32807)

**<font color=#1a73e8>作者：</font>** Chaitai Deb Purkayastha, Bharath Kumar Bolla, Vishnu Surya Reddy Nandi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical LLM evaluation often emphasizes answer accuracy; however, accuracy alone does not test counterfactual consistency or demographic robustness. We evaluated six LLMs on 150 MedQA USMLE questions using two automated perturbation tests to assess their performance. The counterfactual validity (CFV) test asked each model to make a minimal, plausible clinical change that would make a different answer correct. The demographic robustness test added six demographic prefixes to the same vignette and compared the answers and explanations with a no demographic baseline. Of the 900 CFV attempts, 228 (25.3 %) were valid and 672 were invalid. Across 5,400 demographic comparisons, 1,097 answers were changed (20.3%). Automated judging identified 3,128 stereotype evidence flags, including 1,932 in the broad Other category. MedGemma 27B achieved the highest accuracy (87.1%) and CFV (63.3%), lowest answer change rate (16.0%), and low mean Explanation Demographic Dissonance (EDD) score (0.169). However, its accuracy still exceeded its CFV, indicating that correct answers do not guarantee reliable performance on the counterfactual validity task. OpenBioLLM had the highest answer change rate and EDD, whereas GLM had the highest stereotype flag rate. These findings show that accuracy, CFV, answer stability, EDD, and stereotype evidence capture different evaluation aspects. Because all judgments were automated and no clinician validation was available, the results support safety screening but do not establish clinical deployability of the model.

---


### 260. [Mind the Spike: Mechanisms and Brittleness of Visual Massive Activations in Large Vision-Language Models](https://arxiv.org/abs/2609.32808)

**<font color=#1a73e8>作者：</font>** Jonas Ngnawé, Yann Pequignot, Sabyasachi Sahoo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) inherit massive activations from their text-only bases: spikes where a few fixed hidden channels receive values thousands of times above the typical magnitude. The text spike systematically appears in early layers at a fixed initial position, independently of input content. Visual spikes vary across images, but whether their formation follows a consistent pattern across LVLMs and how they respond to image perturbations remain open questions. We find that some LVLMs do not form visual spikes, while others spike at different rates, typically in deeper layers. We identify the trigger direction from model weights and an interpretable location rule: before the language model decoder runs, eventual spike tokens are largely restricted to those sharing least with the rest of the image. Crucially, visual spikes are strikingly brittle. Common corruptions frequently create and relocate spikes, and less often remove them, raising overall incidence. Our trigger-guided spike attack deliberately creates or removes spikes under a small $\ell_\infty$ budget, with 1/255 enough in nine of the ten models that spike. Finally, our preventive intervention removes only the trigger component before spikes erupt, eliminating or substantially reducing spikes on clean and perturbed images while leaving the other image tokens nearly unchanged. Our study spans 25 adapter-based LVLMs built on 18 released text-only bases from 10 families, ranging from 2B to 72B parameters.

---


### 261. [Overwhelmed by Choice: Studying LLM Decision Making at Scale](https://arxiv.org/abs/2609.32809)

**<font color=#1a73e8>作者：</font>** Yu-Chi Lin, Aryan Seth, Anshul Aravind 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiple-choice and candidate-selection evaluations are widely used to assess LLM reasoning and decision-making, yet most benchmarks contain relatively small candidate sets. It remains unclear whether conclusions drawn from these settings remain valid as the candidate space scales. We systematically evaluate LLMs as the number of competing candidates increases and find substantial accuracy degradation across tasks, prompting strategies, and model scales. Controlled analyses show that standard long-context retrieval explanations cannot fully account for this degradation. Instead, we identify two systematic failure patterns. First, gold-margin collapse: the score gap between the correct answer and the strongest distractor progressively shrinks, driven primarily by weakening confidence in the correct answer. Second, earlier candidate preferences become increasingly difficult to overturn, with later candidates exerting progressively weaker influence on the final prediction. Motivated by these findings, we evaluate hierarchical partitioning and permutation-based inference, which improve accuracy by roughly 20 percentage points at $N=160$ on both HotpotQA and MIMIC. Overall, our results identify candidate-set scale as an important evaluation-protocol variable and show that strong small-option performance does not necessarily imply robust large-scale candidate comparison.

---


### 262. [OpenTumorBoard: A Real-World Benchmark of Multidisciplinary Tumor Board Discussion Trajectories](https://arxiv.org/abs/2609.32810)

**<font color=#1a73e8>作者：</font>** Anqi Li, Zhixuan Ge, Yixuan Duan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multidisciplinary tumor boards integrate multimodal clinical observations and longitudinal patient histories through specialist discussions, yet benchmarks rarely capture these real-world trajectories. We introduce OpenTumorBoard, a benchmark with 611 patient cases and 19,157 discussion turns across ten specialist roles, transcribed from 12,534 minutes of publicly available tumor board recordings on YouTube. The benchmark evaluates two settings: SPECIALIST TURN, in which an LLM responds to a clinically significant question posed during a real discussion, and BOARD SIMULATION, in which it generates an entire back-and-forth discussion and reaches a consensus on therapy recommendations, surgical plans, next actions and clinical trial matching. Evaluation of 14 general-purpose frontier and medical LLMs reveals substantial limitations: the best models score 3.43 out of 5 in clinical equivalence to specialist answers and 2.78 out of 5 in alignment with recorded board conclusions. Supervised finetuning and reinforcement learning improve performance on a held-out test set, suggesting that real-world discussion trajectories can support model adaptation. Three M.D. experts review a subset of the benchmark, finding high information coverage and factuality of patient cases and strong fidelity of extracted consensus conclusions. We will release OpenTumorBoard and its automated curation pipeline to support the development and evaluation of LLMs for multidisciplinary, personalized cancer decision-making.

---


### 263. [USAI-Quant: A Quantitative Reasoning Benchmark for Vision-Language Models in Built Environments](https://arxiv.org/abs/2609.32813)

**<font color=#1a73e8>作者：</font>** Dongdong Wang, Qingqi Song, Yuzhou Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) have emerged as a powerful paradigm for urban and spatial AI. However, current state-of-the-art large VLMs still struggle with quantitative reasoning on remote sensing imagery. Existing benchmarks and algorithms are predominantly based on qualitative Visual Question Answering (VQA), providing limited insights into the quantitative reasoning capabilities of VLMs for built environment metrics. To address this gap, we develop Quantitative Urban and Spatial AI benchmark (USAI-Quant), the first benchmark designed to quantitatively evaluate VLM's reasoning capabilities on built environment metrics via remote sensing imagery. USAI-Quant is curated from the 335 largest U.S. cities, aligning high-resolution remote sensing images with quantitative built environment metrics. We then evaluate both general-purpose and remote sensing VLMs (RS-VLMs) by applying VQAs to tens of built environment metrics across three complexity levels. Our results reveal that current state-of-the-art models consistently fall short on numeric reasoning tasks. We further conduct in-depth analyses across models, question types, and geographic locations, uncovering insights into performance variability and task-specific challenges.

---


### 264. [Right Answer, Wrong Reason: Accuracy, Consistency, and Consensus Are Misleading Indicators of LLM Faithfulness in Clinical Decision Support](https://arxiv.org/abs/2609.32817)

**<font color=#1a73e8>作者：</font>** Bharath Kumar Bolla, Bharath Kumar Bolla, Vishnu Surya Reddy Nandi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical Large Language Models (LLMs) achieve strong medical-exam accuracy; however, a correct answer does not guarantee that the explanation names the concepts that actually drove the decision. We introduce three lightweight, directly interpretable metrics for this faithfulness gap: the Explanation Stability Index (ESI), which measures reasoning consistency across repeated queries; the Causal Faithfulness Score (CFS), which tests whether cited concepts drive predictions via concept ablation; and the Perturbation Stability Score (PSS), which measures robustness to semantic-preserving paraphrases. By evaluating six LLMs on 150 MedQA-USMLE questions (900 model-question observations), we found that only 23.3% of the cited clinical concepts were causally necessary. Correct answers had lower CFS than incorrect answers (0.212 vs. 0.398), answer consistency negatively predicted CFS (Spearman r = -0.466), and model pairs could agree on answers while sharing only 8.8% of cited reasoning concepts. These results show that accuracy, consistency, and consensus are incomplete safety signals for clinical decision-making support. The evidence is behavioral rather than mechanistic: concept ablation tests counterfactual sensitivity of outputs, not internal circuits.

---


### 265. [When Can First-Order Models of Fine-Tuning Bound Forgetting?](https://arxiv.org/abs/2609.32818)

**<font color=#1a73e8>作者：</font>** Jianchang Su, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a language model on new data can make it forget facts that it should keep. We ask whether measurements taken at the start of a fine-tuning run can bound, for each protected fact, the probability that the run makes the model forget it. In LoRA fine-tuning with stochastic gradient descent on models from 0.6B to 14B parameters, a first-order response model estimated by finite-difference probes predicts changes of per-fact margins with correlation 0.974-0.998. Predictions of forgetting built on this model nevertheless failed, because forgetting requires parameter changes far outside the region in which the model was validated. The probes can, however, bound the probability that a margin first falls below a boundary near zero: we derive Freedman and Azuma first-passage bounds for a linear surrogate of the margin and test on new runs whether they hold for the model. The bounds contain a term R that measures how much the response coefficients change during the run. The simplified Freedman bound, which sets R = 0, certified most facts but was violated in 14 of 112 conditions, and every fact on which it was violated had R >= a, where a is the distance of the fact's margin to the boundary. The complete Freedman bound certifies only facts with R < a, and it held in every condition. On the violated facts, the spread of the margin across test runs was a median of 14.6 times the prediction of the response model, so the failures are breakdowns of the model, and in our data they occurred only where R >= a. We found this pattern post hoc and tested it in two preregistered confirmatory studies with 43 new conditions: the complete bound held in all of them, and the simplified bound failed there on only 3 facts, each with R >= a. First-order models of fine-tuning can thus bound forgetting on the facts whose response coefficients change by less than their distance to the boundary.

---


### 266. [Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs](https://arxiv.org/abs/2609.32821)

**<font color=#1a73e8>作者：</font>** Yuanyi Wang, Yanggan Gu, Su Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model merging efficiently combines specialized large language models (LLMs) without joint retraining, but can substantially alter expert routing in Mixture-of-Experts (MoE) models. Such \emph{routing drift} is often interpreted as routing failure, raising a fundamental question that remains unclear: \emph{does routing drift after MoE merging actually indicate routing failure, and what evidence should justify repair?} We investigate these questions across DeepSeekMoE, OLMoE, and Qwen3-MoE proposing a routing analysis toolkit for controlled counterfactual interventions and token-level analysis. By crossing source and merged router inputs and parameters, we attribute most expert reassignments to input shifts rather than parameter changes at the same layer. However, source-relative routing differences poorly predict next-token likelihood gains from source-route restoration, and different expert selections can produce directionally similar mixture outputs. We therefore operationalize routing failure as \textit{task loss recoverable under a specified routing intervention, with non-routing parameters fixed.} These tests detect recoverable loss under deliberate router corruption, whereas source-route restoration does not establish reliable task benefits in the evaluated merged models. Motivated by these, we propose \emph{Selective Router Repair (SRR)} as a case study, and find that source-specialist token-likelihood advantages do not reliably identify beneficial local corrections. Together, these findings show that \textbf{routing drift alone is insufficient evidence of routing failure}: source-informed corrections must be judged by their task-level intervention effects. The analysis toolkit and SRR code are released.

---


### 267. [The Decomposition Tax: LLM Pipelines Lose Up to 40 Accuracy Points at Their Own Interfaces](https://arxiv.org/abs/2609.32825)

**<font color=#1a73e8>作者：</font>** Tianqi Bu, YuXuan Peng, Junteng Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A four-stage LLM pipeline gives up as much as 40.5 accuracy points at its own interfaces (gemma-3-12B on MATH-500, Holm-corrected p = 1.66e-19; the largest tax in the primary family). We hold model, problem, stages, stage prompts and completion budget fixed, vary only whether each stage can still see the original problem, and call the accuracy difference the decomposition tax. Across 21 open-weight models from nine organisations, on GSM-Hard and MATH-500 at n = 200 paired items per cell, 70 of 118 primary-family tests survive Benjamini-Hochberg correction and 54 survive Holm. On GSM-Hard, a placebo recovers nothing: it carries at least 60% of the extra tokens and at most one word of the problem. Builders design a pipeline one stage at a time, and its bill arrives at the interfaces between stages. Rewriting one stage's instruction moves gemma-3-12B's tax from 4.5 to 36.5 points, and adding "every relationship stated between them" to a stage that lists the numerical quantities lowers the tax on 9 of 9 models on MATH-500. Re-grounding, which shows a stage the original problem again, belongs after the loss. With one lossy interface, re-grounding the stage after it beats re-grounding the stage before it on 7 of 7 models on both benchmarks; on MATH-500 the earlier repair is worse than none on 7 of 7. Newer models still pay: gemma-4-12B gives up 37.0 points, and the repair holds on all three of the newest models we test. A sealed held-out test refuted a stronger rule we registered, which predicted the paying stage from the interface and receiver types, so we locate the tax by measuring one stage at a time. The prescription has two parts: re-ground the stage after the lossy interface, and if a stage must list the quantities, tell it to keep the relationships.

---


### 268. [Improving LLM Collaboration via Multi-Agent Preference Learning](https://arxiv.org/abs/2609.32827)

**<font color=#1a73e8>作者：</font>** Shuo Liu, Xinzichen Li, Tianle Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Several works have explored multi-agent reinforcement learning (MARL) in LLM collaboration. However, constructing reliable rewards is difficult in practice, as complete and accurate metrics are often unavailable and hard to aggregate. Preference learning provides an alternative by learning from comparative human or AI feedback. Yet, its extension to multi-agent systems remains underexplored. To address this gap, we formulate preference-based multi-agent systems (MAS) from decentralized and centralized collaboration perspectives. We also introduce a general multi-agent preference learning framework (MAPL) to solve these problems. MAPL allows iterative updates by comparing the current solution with decentralized or centralized solutions generated by various agents. We instantiate MAPL using MARL from human feedback (MARLHF) with a learned reward model and multi-agent direct preference optimization (MADPO). Experiments on collaborative writing, coding, tool use, and travel planning show that MAPL can improve collaboration quality and efficiency while approaching the performance of MARL with fixed, well-defined rewards. Within MAPL, MARLHF generally outperforms MADPO on most tasks but remains sensitive to data coverage, agent and comparator models, and the underlying MARL algorithms.

---


### 269. [UniCache: Task- and Type-Aware KV Cache Compression for Unified Multimodal Models](https://arxiv.org/abs/2609.32831)

**<font color=#1a73e8>作者：</font>** Wanqi Yang, Yuexiao Ma, Mei Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models combine understanding, generation, and editing within a single network, offering a promising foundation for versatile multimodal applications. However, growing multimodal contexts make KV cache storage and access increasingly costly. Existing KV cache compression methods are typically tailored to specific tasks and single-modality caches, while overlooking changes in cache importance across tasks and timesteps. However, in unified multimodal models, each task involves multiple KV cache types, and both their composition and dynamics differ across tasks. As a result, a single compression policy overlooks task- and type-specific requirements, leading to the loss of critical information and degraded quality across tasks. Based on these findings, we propose UniCache, a training-free framework for task- and type-aware KV cache compression. UniCache identifies the cache segments activated by each task and assigns suitable compression policies through offline calibration. It coordinates their parallel execution under a shared storage budget through attention-guided allocation and task-aware temporal scheduling. Experiments show that UniCache achieves $5\times$ KV cache compression for understanding and editing and $2.5\times$ for generation with negligible quality loss, while increasing throughput by up to $1.78\times$ in long-context settings, significantly improving the practicality of scaling unified multimodal models to longer context.

---


### 270. [FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](https://arxiv.org/abs/2609.32835)

**<font color=#1a73e8>作者：</font>** Jerry Huang, Sarvesh Babu, Matt Van Buren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents are becoming widely adopted in the financial services industry, careful measurement is essential to understand where they can be reliably deployed and where oversight and professional review remain necessary. Such measurement, however, is constrained by limited access to proprietary or privacy-sensitive data. Existing benchmarks therefore often rely on publicly available data, human- and/or LLM-authored tasks, or simplified settings. We introduce FinancialAuditBench, a benchmark for evaluating agents on financial statement audit tasks, along with a framework for systematically generating synthetic engagements. Our task generation framework leverages differentially private aggregate statistics from historical audits along with audit expertise contributed through over 1,100 hours of benchmark development and review. FinancialAuditBench consists of 90 tasks spanning workpaper completion and review across six synthetic audit engagements, each containing an average of 179 files. Evaluation on eleven frontier models shows that while agents complete substantial portions of staff-level audit tasks well, they sometimes perform inappropriate procedures or produce incorrect documentation. Beyond financial auditing, our framework offers an approach for systematically generating synthetic tasks for model evaluation and training in privacy-sensitive domains.

---


### 271. [Transfer Learning for Edge Classification on Dynamic Text-Attributed Graphs](https://arxiv.org/abs/2609.32849)

**<font color=#1a73e8>作者：</font>** Tyler Bonnet, Marek Rei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning transferable representations for dynamic text-attributed graphs (DyTAGs) requires models to capture underlying interaction dynamics that persist across domains. However, existing methods tend to overfit to domain-specific structural, temporal, and semantic patterns, limiting edge classification performance under distribution shifts. To expose and address this, we formally establish a leave-one-domain-out (LODO) transfer learning protocol for edge classification on DyTAGs. Under this protocol, we demonstrate that state-of-the-art self-supervised methods for dynamic graph learning perform poorly when transferred to unseen domains. Strikingly, existing methods underperform a structurally and temporally unaware Bag of Events (BoE) model we introduce, which inputs only unordered sequences of node and edge text features. Proceeding from the BoE, we propose Spatio-Temporal Semantic Alignment (STSA), which integrates a spatio-temporal encoder that fuses representations of time deltas and node occurrence frequencies into a unified manifold. STSA is trained with a Contrastive Semantic Forecasting objective, which anchors edge representations to a multi-domain textual latent space initialized by a pretrained language model, providing a robust prior that outperforms BoE and all existing methods we evaluate.

---


### 272. [ARSM: Auto-Regressive State Machine for Agentic Reasoning Compression](https://arxiv.org/abs/2609.32852)

**<font color=#1a73e8>作者：</font>** Xiafeng Man, Siyuan Ye, Xiaosong Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Model (LLM)-based agents demonstrate strong capabilities in long-horizon tasks by interleaving reasoning with external environment interactions, the continuous accumulation of context rapidly creates a critical memory bottleneck. Existing memory compression methods rely on task-specific optimization or external auxiliary models, introducing significant computational overhead. Furthermore, the resulting compressed representations tend to lose structured relationships, leading to information dilution, attention collapse, and degraded decision consistency.
To address these limitations, we propose Auto-Regressive State Machine (ARSM), a lightweight training-free framework that enables in-situ reasoning compression through structured state evolution. ARSM introduces two key components: (i) a trajectory abstraction mechanism that reorganizes interaction histories into compact Hypothesis-Action-Result (HAR) micro-chains; (ii) a dynamic state machine that regulates hierarchical memory through atomic operations and a compression-control parameter. These components are unified within an auto-regressive, self-compressive generation space, where each model output jointly performs external action execution and internal state updates.
We evaluate ARSM on Webshop, Multi-Objective Multi-Hop QA, and SWE-Bench Lite datasets. Experimental results show that ARSM maintains the task performance while simultaneously reducing token consumption, offering a practical, cost-effective route toward scalable autonomous agents for long-horizon tasks.

---


### 273. [Are You Sure You're Sure? Two Confounds in a Sycophancy Benchmark](https://arxiv.org/abs/2609.32867)

**<font color=#1a73e8>作者：</font>** Atharv Gupta, Akshat Jindal, Lavanya Nigam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sycophancy is a language model's tendency to cave when a user pushes back, abandoning a correct answer for the user's. Several benchmarks now measure it by scripting an objection and recording how often the model caves. Because that objection is a prompt template, whatever else the template varies is measured along with the property it claims to isolate. We audit SycEval, which reports that objections raised before a model answers (preemptive) cause more caving than those raised after (in-context), and attributes the gap to timing. Two features of its templates vary alongside the property each is meant to test. First, SycEval's objections escalate through four strength levels, and at the two weakest only the preemptive template names a target answer, so timing and naming vary together. We build the missing comparison and test it on multiple-choice questions and SycEval's own free-form pipeline. Naming a target answer raises the follow rate, the share of samples matching the user's assertion, by 14.1--49.5 percentage points (pp), and once both templates name one, the timing comparison reverses on three of the five model conditions we test: models cave \emph{less} under preemptive objections than in-context ones, opposite to SycEval. Second, the output-format instruction benchmarks append for automatic grading also varies with objection placement. Moving it from the pushback into the question flips its effect in opposite directions across models on the same items ($p=0.0059$). The same effect appears in SycEval's free-form pipeline: relocating its instruction lowers caving by 5.1pp on Llama-3.1-8B, while an equivalence test confirms no effect on Qwen3-4B. Both confounds live in the template rather than the models under test, so both are correctable: we close with three checks benchmark authors can apply before publishing.

---


### 274. [Multimodal LLMs Outperform Pathology Foundation Models in Cross-Domain Histological Similarity](https://arxiv.org/abs/2609.32876)

**<font color=#1a73e8>作者：</font>** Yishu Zhang, Yun Li, Daiwei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art pathology foundation models, trained on millions of histology tiles, can fail to preserve tissue similarity when comparisons cross slide or institution boundaries. We show that general-purpose multimodal LLMs, without being trained as pathology foundation models, consistently outperform these specialized models in cross-domain histological similarity judgments. Using a relative similarity framework that we release as the MOSAIC (Model Similarity Assessment across Institutions and Cohorts) benchmark, we evaluate 17 models across 6 datasets and find that pathology encoders often rank same-institution, different-disease tiles as more similar than same-disease, different-institution tiles, a clinically dangerous failure mode invisible to standard within-domain evaluations. LLMs appear less susceptible to this failure, likely because they perform semantic visual comparison of morphology and tissue architecture rather than relying on shortcut features tied to acquisition context. Scaling training data does not resolve the problem for pathology encoders, implicating the learning objective rather than data coverage. Our results expose a fundamental robustness gap in current pathology foundation models and establish multimodal LLMs as a viable alternative for cross-institutional retrieval, dataset harmonization, and multi-site quality control. Code and data will be released upon acceptance.

---


### 275. [Can LLMs Predict the Future? A Brier Score Analysis of Prediction Markets](https://arxiv.org/abs/2609.32885)

**<font color=#1a73e8>作者：</font>** Yuanbo Li, Zekun Li, Xiaoyan cong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study whether model upgrades improve probability estimates for prediction-market questions. Our Resolved Market Forecasting (RMF) benchmark contains 3,000 resolved binary questions across nine domains, on which we evaluate six Claude and Qwen model variants using a question-only, zero-shot protocol. We assess Brier scores relative to an empirical base-rate predictor, examine their Murphy decomposition, and compare models through paired differences, with results stratified by event category and timing relative to training cutoffs. In the reported post-cutoff stratum, the four Claude models achieve Brier scores of 0.183-0.192, improving on the base-rate reference by 0.024-0.033. Qwen 32B does not significantly outperform that reference, although its paired Brier is 0.024 lower than that of the 7B checkpoint. The evaluated Claude version and tier upgrades yield no significant improvement. Within-model differences across event categories exceed the observed differences among Claude variants. These results show why forecasting scores should be interpreted alongside simple probability baselines and question composition: under this protocol, newer versions or higher model tiers do not consistently produce more accurate probabilities.

---


### 276. [StraTune: Adaptive Selection of Revision Operators for Self-Evolving LLM Skills](https://arxiv.org/abs/2609.32886)

**<font color=#1a73e8>作者：</font>** Zeping Liu, Yan Li, Ni Lao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can learn reusable textual skills from execution feedback without updating their parameters, but effectively deciding how to revise these skills remains a key challenge. Existing methods typically rely on a fixed revision operator, a search strategy and the revision forms applied under it. However, we observe that no single revision operator consistently performs best across tasks, and repeatedly applying an unsuitable operator can limit further improvement. We propose StraTune (strategy-guided skill tuning), which lets a frozen optimizer LLM choose the revision operator at every round from the optimization state, which is defined as the current execution feedback together with the recorded outcomes of earlier strategies and forms. Candidate skills from every revision operator pass one candidate evaluation, which screens for gains and regressions on a small sample set and validates them on a larger one, and every outcome is written back to the optimization state for later choices. Across four benchmarks and two LLM settings, StraTune outperforms all five baselines in most settings. Ablations attribute the gains to the adaptive choice of the revision operator, since fixed, random, scheduled, and bandit strategy choices all score lower, and skills learned with a small target LLM also improve a stronger one. Code and learned skills are available at this https URL.

---


### 277. [A Function-Level Vulnerability Score Measures Flag Rate More Than the Model: Protocol Effects on Paired Benchmarks](https://arxiv.org/abs/2609.32890)

**<font color=#1a73e8>作者：</font>** Maciej Cichoń, Bartłomiej Dmitruk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly evaluated as vulnerability detectors, and scores reported for similar models differ widely between papers. We measured how much of that difference evaluation protocol accounts for, with model outputs held fixed. In a paired test, a model must flag a vulnerable function and clear its version after a fixing commit. Three choices that published evaluations make differently were varied one at a time: metric, verdict extraction and output budget. Seven frontier and large open models were evaluated on five released pair benchmarks and a set pooled for this work under one protocol, and 61 open models of 1.5B to 36B parameters on the pooled set. Function-level F1 follows how often a model flags both functions of a pair (Spearman $+0.86$ over 42 combinations) and is nearly unrelated to pair-level correctness ($+0.16$). On the pair score, extraction changes a model's number by $+0.001$ at the median and budget by $+0.02$ with an interval through zero, whereas the model changes a benchmark's number by up to 0.18 and the benchmark a model's by up to 0.16; a function-level score therefore measures flag rate more than model. For 37 of 68 models the difference between correct and reversed pairs is within its 95% interval of zero, the value for a null model that flags each function at a fixed rate, while both-flagged and both-cleared rates exceed that null by 0.055 on median, and for 64 of 68 both functions of a pair receive one answer more often than independence predicts: verdicts are determined by the text common to both functions. On length-matched pairs a linear probe on activations separates 0.78 by within-pair ranking, against 0.64 for a tf-idf baseline and 0.5 for length; the generated verdict is near chance for three of six models and at 0.55 to 0.57 for the other three, and a prompted logit is at chance for all six.

---


### 278. [Constraints Are Graphs, Not Chains: Exact Decoding for Diffusion Language Models](https://arxiv.org/abs/2609.32900)

**<font color=#1a73e8>作者：</font>** Jianchang Su, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (dLLMs) predict masked positions in arbitrary order, but their exact constrained decoders still encode constraints as sequential languages, whose state must track every unresolved dependency between positions. For relational constraints this encoding grows exponentially: for same-order copy, every finite automaton needs $4^k$ states, deterministic or nondeterministic, and every context-free grammar has size $2^{\Omega(k)}$, while the factor graph of the same relation has size $O(k)$ and a 16-entry peak table. We introduce FactorDLM, a training-free decoder that represents finite-domain relations as a factor graph and, at each denoising step, conditions the model's mean-field prediction on that graph exactly by variable elimination. Decoding cost then grows exponentially with the induced width of the constraint graph, which replaces automaton size as the governing parameter. Because a finite automaton is a chain-shaped factor graph, one compiler enforces syntax and nonlocal relations together: on JSON records with cross-field references, a schema automaton alone leaves references dangling, relational factors alone produce malformed JSON, and the combined plan is valid on both counts, including on records of variable length. Across nine relational benchmarks and three backbones, every output satisfies every declared constraint at 0.4-6.9% projection overhead, where unconstrained decoding is 0-79% valid, and compiled projection answers repeated queries 13.6x faster than CP-SAT with eight parallel workers. Because model-free rules solve three of five standard benchmarks, we construct benchmarks with exact chance and fixed-template floors, on which selecting among exact constrained samples beats greedy projection. Which encoding is cheaper, sequential state or direct factors, depends on the constraint and is computable before decoding begins.

---


### 279. [Linger and Lose: Knowledge Collapse in Low-Bit Language Models](https://arxiv.org/abs/2609.32902)

**<font color=#1a73e8>作者：</font>** Prashanna Mani Paudel, Shivanand Venkanna Sheshappanavar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training language models with ternary weights is commonly judged by loss and downstream accuracy, which record only a modest cost relative to full precision. We show that these metrics can conceal a much larger failure. We instead measure knowledge capacity, the factual bits stored per parameter, on synthetic biographies with known information content. We train GPT-2-style models from scratch with 2.5M to 50M parameters at five precisions. Under the standard cosine schedule, ternary models retain as little as 6% of an identically trained fp16 model's capacity. The deficit widens with model size while perplexity rises by only 1.4 to 1.6 times. Measured throughout training, these models first acquire capacity and then lose most of it. We identify this knowledge collapse as a learning-rate dwell instability. Held near $1$--$2\times10^{-4}$ with no decay, a pre-collapse model collapses within a few hundred exposures, and returning to a safe rate does not restore capacity. We then locate the collapse in the output head. It happens at a value the model can never predict. The weights there grow unchecked, while every other prediction the model makes is unchanged. We find that making the value predictable removes the collapse, regardless of which attribute carries it. A warmup-stable-decay schedule with a 10% cooldown increases ternary capacity by 2.7 times at 25M and 4.3 times at 50M. Gains are larger at lower precision. Cutting the output head's learning rate prevents failure when training from scratch. The post-training quantization methods we tested recover no measurable capacity below 4 bits. Our findings suggest judging low-precision training by retained capacity during training rather than final loss.

---


### 280. [Logical subspace in LLMs](https://arxiv.org/abs/2609.32907)

**<font color=#1a73e8>作者：</font>** Hope Kean, Enric Boix-Adsera  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has identified a human brain network specialized for abstract formal reasoning (Kean et al., 2025). Does the same hold true in language models? To answer this question, we introduce the minimal viable subspace (MVS) method, which searches for the lowest-rank activation subspace at a layer that preserves task performance when everything outside that subspace is ablated. Using MVS, we demonstrate low-rank subspaces supporting logical inference on Gemma and Qwen models. Furthermore, these subspaces exhibit a clear dissociation from model capacities on other tasks, such that retaining these late logic subspaces preserves inference while impairing factual knowledge, working memory, cognitive control, and arithmetic. Conversely, ablating them reduces logical inference accuracy to chance while largely sparing these other capacities. Our results suggest a functionally localizable core machinery for logic akin to that in the human brain.

---


### 281. [Allspark: Weak to Strong Transfer via Alternating Chain of Thought](https://arxiv.org/abs/2609.32913)

**<font color=#1a73e8>作者：</font>** Kaizhao Liang, Junxiong Wang, Chen Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in frontier models has renewed interest in large-scale reinforcement learning (RL), but the cost of generating large-model rollouts makes even testing RL recipes expensive. We ask whether reasoning improvements learned by a small, weak model can benefit a larger, stronger model without using the strong model's rollouts during training. We introduce Allspark, a training and inference framework for weak-to-strong transfer through alternating chains of thought. A weak teacher is trained alongside a frozen copy of the same model; the two alternate reasoning segments, and the frozen model produces the final answer. At inference time, a stronger student replaces the frozen training partner, while both models remain fixed. Because they communicate through text, the teacher can steer students from different model families and with different tokenizers. We study Allspark at two scales: controlled Qwen experiments across math and reasoning, and larger-scale Inkling experiments on ARC-AGI-2. The Inkling experiments show accuracy gains in within-family and cross-family settings, including transfer to Kimi and Nemotron, with benefits that vary across inference settings. These findings motivate reusing a trained weak teacher across strong students and examining the resulting accuracy--token tradeoff.

---


### 282. [Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows](https://arxiv.org/abs/2609.32917)

**<font color=#1a73e8>作者：</font>** Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running large language model (LLM) agents in production gets expensive fast. A frontier model (the largest, most capable tier) is accurate but can cost 25 times what a small model costs per token, and the gap compounds once a workflow chains several calls together. Planner-as-Router (PaR) attacks this from a different angle. Instead of leaving model-tier selection to some component downstream, it folds the choice into planning itself. As the planner breaks a query into subtasks, it also assigns each one a model size tier (small, mid, or frontier, ordered by capability and price), so the dependencies between subtasks are visible before any specialist runs. Unlike per-call routers such as cascade routing, which look at one node at a time, PaR sees the whole workflow up front and needs no separate router model or training data. We evaluate PaR with EntBench, a benchmark of 54 enterprise agentic tasks across seven classes, graded by actually running the generated Structured Query Language (SQL) and MongoDB queries against live databases. Over 1,157 evaluations spanning eight routers and three seeds, PaR stays on the observed cost-accuracy frontier. It matches a sink-frontier heuristic (frontier model on terminal nodes only) in accuracy at comparable cost and a faithful FrugalGPT cascade at lower cost, and cuts cost 44% against all-frontier routing while giving up 2.9 points of accuracy. Several accuracy gaps fall inside the plus-or-minus six-point confidence interval of a 54-task study, so we frame PaR's advantage as frontier position rather than a clean accuracy win. We also report a preliminary observation, not a validated result: a small pilot hints that cheap routing may carry a hidden compounding penalty on compositional workflows, which we frame as a hypothesis for future measurement. PaR, EntBench, and all evaluation code are open source.

---


### 283. [Diagnosing Sampled LLM Reasoning in Formal Geometry: Coverage, Realization, and Validity Evidence](https://arxiv.org/abs/2609.32924)

**<font color=#1a73e8>作者：</font>** Xiao Yue, Guangzhi Qu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repeated sampling can reveal a correct numerical answer without yielding either a reliable system output or a supported derivation. We present Coverage, Realization, and Validity Evidence (CRV), an evaluation protocol for sampled large language model (LLM) reasoning over formal geometry states. Coverage is answer availability, realization is readout accuracy on the frozen candidate pool, and validity evidence is a label-blinded critic judgment of derivational support rather than a proof certificate. CRV freezes each candidate pool before comparing readouts and analyzes covered failures by correct-answer multiplicity and within-problem discrimination. On HardShift441, a 441-problem set for which a reference solver leaves 406 problems unsolved, a LoRA-adapted Qwen2.5-7B generator obtains 24.2% average single-sample accuracy and 68.9% pass@16, whereas verifier-weighted self-consistency (WSC) reaches 38.0%. Readout accuracy is particularly low when the correct answer occurs only once or twice in the pool. In a separate constructed audit of 195 covered problems, the critic labels 12 correct-answer representatives as supported, 181 as refuted, and two as uncertain. These results show that coverage, realization, and validity evidence from the critic are distinct quantities and should be reported separately.

---


### 284. [The Geometry of Logic: Stratification Induces Semantic Structure and Robust Reasoning](https://arxiv.org/abs/2609.32927)

**<font color=#1a73e8>作者：</font>** Cristina V. Lopes, Yuangang Li, Justin Tian Jin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models perform well on symbolic tasks, yet it remains unclear whether they learn generalizable rules or rely on statistical shortcuts. Mechanistic studies link algorithmic behavior to structured internal representations, motivating the hypothesis that robust reasoning benefits from separating values from the types that control their manipulation. Can making this separation an architectural primitive improve the learnability and generalization of logical mechanisms? We introduce \textbf{STRAT} (\textbf{ST}ratified \textbf{R}egisters \textbf{A}nd \textbf{T}ypes), which partitions the residual stream into orthogonal Data and Type subspaces and uses Type-based attention and gating to govern Data transformations. Controlled arithmetic ablations identify three failure modes associated with data-control interference: the Linear Trap, Gradient Wall, and Open Gate Trap. Mechanistic analysis reveals interpretable logical structure, and in arithmetic, STRAT reduces median OOD error 35-fold relative to a Transformer baseline. On each of 11 datasets spanning 10 tasks, STRAT outperforms the Transformer baseline in mean accuracy, by 26 percentage points on average, with both models trained from 10 base examples per dataset using identical task-specific augmentation where applicable. Under distribution shift, STRAT's mean accuracy drops by only 2.39 percentage points, compared with 11.75 for the Transformer.

---


### 285. [Counting on Thinking: Tracing Evidence Integration in Language Models](https://arxiv.org/abs/2609.32932)

**<font color=#1a73e8>作者：</font>** Jingming Xue, Robert C. Wilson, Huadong Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finite computational resources force a tradeoff between automatic System 1 processes and costly System 2 thinking. Large language models (LLMs) can spend extra computation on hard problems, yet direct answers struggle even with counting, an elementary operation humans and animals perform automatically. We ask why this requires thinking in LLMs. Evidence integration has long been used in psychology and neuroscience to probe decision-making. Our evidence-integration task presents one letter per conversational turn and asks which of two target letters appeared more often. A running count difference solves the task optimally by weighting every letter equally; tokens at each turn could represent and update this difference. Direct responses instead weighted evidence unevenly, with strong recency effects, and assigned less probability to the correct answer as difficulty increased. Thinking improved performance and made integration weights nearly uniform, yet final-query attention remained concentrated on the sequence ends in both modes. Reasoning trajectories showed models revisiting input, recounting letters, and checking intermediate counts that informed the answer, suggesting that thinking constructs the accumulated count that direct responses lack rather than reading out one already formed. Reasoning-token costs grew with the number of letters far more than with coherence. Outcome feedback did not bring this computation into direct responses: under in-context reinforcement learning (ICRL), performance deteriorated over repeated games and recency effects strengthened, yet models grew more confident. Humans and animals amortize such computations into automatic processes, whereas current LLMs still pay for them with thinking on every trial. Which operations learning can make directly available remains central to how future models allocate computation.

---


### 286. [Theory of Scene: Breaking the Symmetry Trap in Multi-Agent LLM Coordination](https://arxiv.org/abs/2609.32939)

**<font color=#1a73e8>作者：</font>** Liangqi Yuan, Wenzhi Fang, Shiqiang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built on large language models (LLMs) are largely homogeneous, as their agents behave alike even across distinct LLMs. We show that when such agents act concurrently without communication, they collide on targets they must split and diverge on targets they must take together, a double failure we term the symmetry trap. Theory of Mind (ToM), widely used for coordination without communication, cannot escape this trap, since homogeneous agents form the same prediction of one another and respond to it in the same way. We propose Theory of Scene (ToS), a training-free reasoning schema in which each agent reads its public role, the only difference between the agents, and the task context they all observe. Homogeneous agents thereby derive one division of labor, each taking the part its role fixes, which turns homogeneity from the cause of the trap into the cure. ToS reads the role together with the scene through role gating, which determines whether ownership overlaps or is already divided, and the task context through task coupling, which infers whether the team must converge on each target, divide it, or take its stages in turn. We evaluate on DivvyBench, a controlled environment we introduce, whose target types make an episode Competitive, Cooperative, or Mixed across Tabletop, Airspace, and Household scenarios, and on two established agentic benchmarks, GovSim and Overcooked. ToS outperforms all six baselines on every benchmark, and each baseline falls far behind it in at least one setting. Against ToM given the same inputs, ToS raises the DivvyBench success rate from 71.1% to 99.6%, the GovSim total gain from 207 to 400, and the Overcooked level-normalized throughput from 1.41 to 1.67.

---


### 287. [The Key Handoff: Retrieval in Hybrid Language Models](https://arxiv.org/abs/2609.32942)

**<font color=#1a73e8>作者：</font>** Kaan Kale, Oguzhan Baser, Sriram Vishwanath  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A two-hop question makes a language model retrieve twice: once to produce a bridge entity, and once to retrieve with it. Transformers resolve that entity in their early layers. Hybrid models replace most of the attention with a recurrent state, so where the key becomes usable, and where it is spent on an answer, is not known. Answering "Where is the ball?" from "the ball belongs to Alice" and "Alice is in the garden" turns on Alice, a name the question does not mention. A model could reach garden through Alice, the key it computed, or through where the fact sits in the prompt. Across twelve models, dense and hybrid, we move a hidden state from one story into another where the two routes lead to different places, and read off which place the model gives. An attention layer converts the key in every model we tested, and crossing that layer removes its usable effect, all of it where no attention follows. In sequential hybrids this makes the answer a handoff: recurrent layers carry the key forward, and attention spends it. Retrieval does not always stop there. Writing a different fact into the memory of the recurrent layers that follow the last attention layer can move the answer toward that fact, multiplying its odds by 1.3 to 2.7, and which hybrids do this is not settled by their architecture or training. That read is addressed by the key, not by position: recurrent state in a hybrid is not only a carrier, but a memory that later layers can query.

---


### 288. [DynamicDx: Evaluating Evidence Acquisition in Video-Based Diagnosis](https://arxiv.org/abs/2609.32957)

**<font color=#1a73e8>作者：</font>** Jiahui Li, Yutong Guo, Nan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diagnosing a patient from video requires more than recognizing the sign: a vision-language model must turn what it sees into hypotheses, questions and tests. DynamicDx evaluates each step in 71 neurological consultations across 11 sign categories, linking authentic patient videos to confirmed diagnoses and fixed charts built from the same case reports, so that every model queries the same evidence. Across five such models, video improves accuracy by 9.9-22.5 percentage points over blind input, but neither recognition alone nor temporal order explains the gain: the cause is usually missing from the model's video-only differential diagnosis even when the sign is recognized, and shuffling the frames produces no reliable accuracy loss. Instead, a trajectory replay traces most of the gain to the investigation results the video prompts. Evidence acquisition is the bottleneck: supplying the decisive investigations raises accuracy to 73.2-93.0%. Two interventions act on it. A post-trained 4B video describer improves sign descriptions, especially from a short, densely sampled segment, and source-clean literature retrieval expands initial hypotheses; both bring the tests a model orders closer to those the treating clinicians documented and, through them, raise accuracy. For video-based diagnosis, seeing better helps when it leads to asking better.

---


### 289. [Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents](https://arxiv.org/abs/2609.32961)

**<font color=#1a73e8>作者：</font>** Ritul Satish, Prasoon Sinha, Akiho Kawada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLM agents tackle longer tasks, they increasingly compress growing histories of reasoning, actions, and tool outputs. Compression can reduce token use, but it also changes the information available for later decisions. Existing agentic harnesses bundle decisions about what to compress, when to compress, and how much to remove into fixed policies. A systematic characterization is needed to disentangle these decisions and reveal how each affects task success and execution cost. We systematically vary these decisions across three open-weight models on SWE-bench Verified and Terminal-Bench 1.0. Across nearly 35,000 agent runs, we measure task success, token use, end-to-end latency, and estimated cost. We find that fewer tokens need not mean faster or cheaper execution: on Terminal-Bench with Qwen, policies using roughly one-third as many tokens can take 20-80% longer than the uncompressed agent. Policies with similar overall success can solve different tasks, while the same policy can perform quite differently across models. Our results motivate evaluating compression by its effects on agent execution and tailoring policies to the task, model, and workload.

---


### 290. [The Commit-Abstain Circuit: Why Language Models Hallucinate Instead of Abstaining](https://arxiv.org/abs/2609.32964)

**<font color=#1a73e8>作者：</font>** Vy Nguyen, Ziqi Xu, Jeffrey Chan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) often hallucinate by committing to confident answers rather than abstaining, even when they do not have enough information to answer reliably. A large body of existing work mitigates hallucination through detection or abstention mechanisms, but leaves open how models internally arrive at the decision to commit or abstain in the first place. We study this decision through mechanistic analysis, framing hallucination as unsupported commitment: the model commits despite exhibiting signals of unanswerability. Using causal gating, we identify a Commit-Abstain Circuit (CAC), a sparse, causally localised subset of attention heads and MLP sublayers underlying this decision. Across ten LMs (3B-14B) from five families and three benchmarks, the CAC exhibits a recurring accumulate-yet-undercorrect pattern: commitment-promoting components build up commitment in earlier layers, while abstention-promoting components act later as corrective signals that are often insufficient to overturn the accumulated commitment. Building on this finding, a lightweight policy trained on CAC activations improves decision accuracy by 12.2 points over the model's intrinsic commit-abstain margin, reduces false abstentions by 2.5 times, transfers to unseen benchmarks, and extends to larger models (27B-35B). The CAC is both diagnostic, clarifying how models overcommit, and practical, enabling improved abstention decisions.

---


### 291. [Relic: From Multi-Agent Collaboration to Persistent Organizational Capability](https://arxiv.org/abs/2609.32965)

**<font color=#1a73e8>作者：</font>** Hongyi Du, Tianyi Zhang, Weijia Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiple agents may often conflict in an organization: for example, one coding agent changes an interface in a repository, but another continues to develop on the old version where existing tests become stale. A conversation can resolve the episode, but when the participants change, what makes the lesson continue to govern the team? We introduce Relic, which turns recurring collaboration failures into organization-owned, executable protocols. Members reflect on visible work, propose rules, and govern their adoption. Adopted protocols bind triggers, responsibilities, required evidence, and execution consequences to the runtime, while remaining open to revision and retirement. In one traced case, repeated integration friction produces an interface-review rule that governs later pull requests and is revised as work continues. Across 360 controlled runs over ten software workloads and three models, Relic raises complete-contract delivery from 14.06% to 19.76% (+5.71 percentage points) over a matched structured team without the protocol lifecycle, improving all four verified production endpoints in every model stratum. Under fresh-member transfer, behavioral correctness is 25.4% with no inherited protocol, 34.6% with the same rules provided as readable text, and 41.2% with executable bindings, a +6.5-point advantage over text alone. On the full CooperBench benchmark, after excluding broken benchmark pairs, Relic achieves 367/477 (76.9%), establishing the best reported result among peer-structured systems. On the fixed 48-pair same-model subset, Relic also exceeds Solo (29/48 vs. 26/48), reversing the coordination loss exhibited by the official peer baseline. Together, these results show how collaboration experience can become persistent organizational state that remains useful beyond the members who created it.

---


### 292. [ReVision3D: Attribution-Guided Recursive Self-Improvement for 3D Medical Perception](https://arxiv.org/abs/2609.32984)

**<font color=#1a73e8>作者：</font>** Ho Hin Lee, Yuyin Zhou, Yannan Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) offers a promising path for overcoming the limited visual capability of current medical imaging agents. Yet applying RSI to volumetric imaging remains difficult: failures can arise from acquisition, perception, training recipe, or downstream inference, while self-generated feedback and logged trajectories provide little guidance on which component should change. We introduce ReVision3D, an RSI system that leverages 3D volumes with spatially grounded annotations to determine where visual evidence is lost and recursively improve the corresponding visual capability. A frozen language-model designer proposes revisions to acquisition, perception, training, or inference, while the verifier and system-level objective remain fixed. Our key insight is that an annotated volume forms an exact replay world for view rendering and spatial verification: unvisited views can be rendered on demand, and localized predictions can be checked directly against reference masks. This grounded feedback directs targeted revision, while only changes that improve beyond measured seed noise are retained. Each accepted change triggers renewed attribution, allowing the dominant bottleneck to shift across rounds. On abdominal CT, attribution identifies perception as the dominant remaining limitation. Revising that level enables ReVision3D to achieve 79% liver recall and 83% kidney recall at under 0.4 false positives per patient, outperforming the evaluated frozen multimodal foundation models, with the largest gains on small lesions.

---


### 293. [Certified Long-Horizon Code Agent Evolution via Validation-Gated Skill Optimization](https://arxiv.org/abs/2609.32990)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Hao Cheng, Xiaomin Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long horizon agent self-evolution without model weight updates is essential for enabling deployed agents to accumulate reusable skills and improve over time. Prior self-evolution work has focused primarily on short-horizon tasks, while repository-level software engineering remains unexplored despite being an ideal testbed for long-horizon adaptation. In this setting, agents are required to solve streams of sequential tasks, navigate complex dependencies with evolving repositories and persistently store and reuse experience. Text-based skill optimization offers an efficient, non-parametric approach for such adaptation. However, existing methods often suffer from unstable updates, performance drawdown, and agent collapse over extended deployments. In this paper, we formalize the concept of in-context self-evolution and introduce VALVE, a validated-gated framework for long-horizon skill optimization. We establish finite convergence, provide theoretical guarantees for future-task gain and drawdown, and derive the validation and evaluation holdout sizes required for a prescribed tolerance, with leading-order scaling
Empirically, our pipeline, VALVE achieves stable self-improvement over evolution horizon spanning more than 1,000 SWE tasks, with average final and peak gains of $14.9$ and $16.5$ points across three frontier models (GPT-5.5, Claude-4.6 and MiniMax-M2.7). The validation gate reduces average drawdown by 75% and produces an 11x more compact skill bank than ungated evolution. We further present extensive ablations identifying the design choices most critical to long-horizon skill evolution.

---


### 294. [What Should Data Teach? Moving Bottlenecks Across Circuit, Store, and Use](https://arxiv.org/abs/2609.32991)

**<font color=#1a73e8>作者：</font>** Yixiao Chen, Ke Cheng, Jiangtao Guan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What should data teach a language model at a particular point in training? A circuit view reveals three distinct bottlenecks: forming a computation, making its required content available, and selecting among available routes. A shared diagnosis-to-data principle connects them: localize the missing operation, preserve its causal relation, vary shortcut-bearing context, and re-audit the residual. Formation-sensitive selection and prerequisite ordering accelerate a binding-matching-transport path; a brief early prefix from the same training multiset retains a validation advantage through 100B tokens. Availability counterfactuals then distinguish writing content from invoking available memory, while paired supervision and context-opportunity ranking improve matched route decisions and long-context answer likelihood. A continuous 350M-model experiment connects the three interventions on the same facts: early circuit training improves subsequent learning, and the complete sequence outperforms stage-replacement controls on facts withheld from Use teaching. Independent query surfaces and opposed-source decisions expose conditional arbitration as the remaining frontier. Together, these results show why a change in the limiting operation calls for a change in supervision, not merely a new ranking of difficult examples.

---


### 295. [X-Tree: Tokenizing Reusable Experience for Efficient Agent Generalization](https://arxiv.org/abs/2609.32993)

**<font color=#1a73e8>作者：</font>** Sitao Cheng, Xunjian Yin, Zhiyuan Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step agents are trained on flat action streams: SFT and RLVR weight every token uniformly and ignore the sub-procedures that recur across tasks, the hierarchy that lets humans plan top-down from reusable routines. This structure sits unused, and flat training uses each scarce trajectory less fully than its content allows. Recent agents do use that structure, but only as LLM-written skills in context, never in the weights, so their gains do not generalize beyond retrieval. We instead recover this hierarchy from the data itself and train on it, with no LLM calls. Following text tokenizers, which build a vocabulary by counting alone, we score action spans by reusability and merge canonicalized actions into a reusable eXperience tree (X-Tree). Each X-Tree node captures how a frequent and success-bearing skill is composed from sub-skills, guiding efficient generalization. We integrate X-Tree into three training settings: offline RL, with each node as a training instance; online RLVR, with an adaptive skill bonus; and on-policy self-distillation, with X-Tree as the self-teacher's privileged context. Across WebArena, ScienceWorld, and WebShop at three model scales, X-Tree improves over standard recipes at matched data and budget by up to 4.5% SR on WebArena, 5.8% SR on ScienceWorld and 4.1% success on WebShop. Matched analyses attribute the gains to the X-Tree structure and the three integrations.

---


### 296. [Oracle Gaps in Reliability Coverage: Sampling Noise or Policy Specialization?](https://arxiv.org/abs/2609.32996)

**<font color=#1a73e8>作者：</font>** Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Policies trained from the same base model can appear to solve different problems. An oracle that chooses the best policy for each problem may therefore appear much stronger than any single policy. Selecting the largest estimated success rate also selects favorable sampling errors. We study this effect through reliability coverage, the fraction of problems whose success probability reaches a chosen threshold. Our first test redistributes stored correctness outcomes across policies within each problem. A second also preserves each policy's total successes, accounting for overall quality differences under a specified statistical model. For five training seeds of a seven-billion-parameter vision-language model, redistribution reproduces 0.096 of an estimated 0.113 oracle gap at threshold 0.10. Neither test finds significant evidence at this threshold. Small advantages remain unresolved. Mixtures, routers, voting, and weight averaging show no detectable improvement over their corresponding single-policy baselines. Training policies on different datasets shows little detectable specialization under light post-training, and no router gain. A stronger recipe does create it, both tests detect it, and a router gain appears only at the high thresholds where the specialists separate. In a control with predictable specialization, a router recovers about half the oracle gap. Coverage bounds explain why even a genuine oracle advantage need not yield a deployment gain. The tests assess apparent specialization from stored responses before investment in routing. Code: this https URL

---


### 297. [Certified Interface Aliases: Exact Collisions in Vision-Language Preprocessing, and When They Exist](https://arxiv.org/abs/2609.33003)

**<font color=#1a73e8>作者：</font>** Mert Onur Cakiroglu, Elham Buxton, Mehmet Dalkilic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language verifiers and routers must distinguish errors repairable by more reasoning from those caused by visual evidence never reaching the language model. This distinction lacks ground truth because annotators see full-resolution images while models receive preprocessed tensors. We introduce AliasForge to create cases where the relevant fact is provably absent from the interface. Fixed-point resampling makes the pre-rounding resize an exact integer linear map that can send nonzero integer perturbations to zero. Hiding a label-flipping perturbation there produces images with opposite step-correctness labels but bit-identical interface states. Every verifier therefore has the same output law on both members, giving pair-balanced accuracy exactly one half and zero gain from language-side repair. We prove that every fixed-point downscaler has such null vectors and bound their smallest size at the most common ratios, which rules out an 8-bit fit whenever the bound exceeds 255. From the resize configuration alone, a lattice criterion supplies realizable collisions and certifies their absence within the specified construction family. It resolves all 20 screened configurations, 17 as constructible and 3 as non-constructible. We construct certified pairs across three architectures and certify four additional processors, with zero decision-logit gap on all 18 scored pairs and none of the 18 controls. The pairs also screen routers that waste computation on re-attention or further reasoning. On natural items, per-item routing headroom exists, but no tested interface-only router improves over stopping. Our fiber ceiling bounds the headroom recoverable from the interface. Code: this https URL.

---


### 298. [Model-Aware Data Selection from In-and-Out Information Interplay](https://arxiv.org/abs/2609.33010)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Xiaomin Li, Yuexing Hao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are effective representations that assimilate vast amounts of knowledge during pretraining, but post-training is necessary for models to reliably access this knowledge and "know what they know." We observe an interesting rank equilibrium between knowledge stored in the weights and the data stream passing through the model. Across all model layers, we find that the hidden states (data stream) follow a U-shaped pattern, showing substantial compression in early layers and a steep rise during the late-layer decoding phase. In contrast, the weight rank follows an inverted U-shaped pattern, with very low rank in the early and late layers and high rank in the middle. We interpret this as an in-and-out information interplay: intermediate activations do not need to carry content that the weights can supply later, so they primarily preserve what the weights cannot provide.
Motivated by this observation, we propose a model-aware data selection method, CAP (Counterfactual Assimilation Profile), which can determine whether a data candidate contains information accessible to the current model by utilizing the divergence gap in early- and late-layer representations between model-generated and reference responses. Across math, code, and science domains, CAP delivers 35.4% greater average improvement over the base model than the strongest baseline under different selection budgets. With only 10% of the data pool, CAP surpasses or matches full-pool training on math and science. We further show that CAP transfers to multimodal data selection and is robust to response horizon and noise.

---


### 299. [The Epistemics of Agent Memory: Measuring, and Governing, the Consolidation Decision in Long-Horizon LLM Agents](https://arxiv.org/abs/2609.33013)

**<font color=#1a73e8>作者：</font>** Sasank Annapureddy, Anjaneya Prasad Thamatani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents must convert accumulated experience into durable memory, deciding what to keep, compress, abstract into reusable skills and rules, or forget. We report a four-phase research program on this consolidation problem whose central finding is a shift in what is measured: from how much an agent remembers, to whether its consolidation decisions are any good, to whether those decisions can be trusted.
Phase 1 learns episodic boundaries from agent traces by downstream utility; an honest near-miss (oracle correlation 0.691 vs a 0.70 bar) whose lasting output is a three-gate anti-leakage protocol. Phase 2 learns when to promote experience and to which abstraction level under a token budget, achieving a verified +22.7% task-success improvement with 7x compression, but exposing a degenerate-forgetting failure and a distribution-shift failure mode we name lambda-prevalence coupling. Phase 3 introduces ConsolidationBench, an oracle-by-construction benchmark that scores consolidation decisions against a known optimum on three non-circular axes; production retrieval systems retain information yet score zero on cross-level transfer. Phase 4 introduces governed consolidation: the decision wrapped in poison-resistance, reversibility, and auditability guarantees with a quality gate. Governance is statistically distinct from the quality score ($r^2 = 0.43$; partial $r = 0.27$; identical-quality policies differ threefold in governance), so the contribution survives independently of the metric's external validity. On that question we report a resolved negative: after a graded-reuse redesign removed a structural ceiling, a two-benchmark study with 2,532 real answer cells finds the quality score does not predict real transfer accuracy (pooled Spearman $\rho = -0.24$, n = 12, CI spanning zero). An adversarial self-critique pass cleared the final claim set with zero surviving overclaims.

---


### 300. [TCMQA: A 38K-Question Traditional Chinese Medicine Benchmark with a Licensed-Practitioner Reference](https://arxiv.org/abs/2609.33014)

**<font color=#1a73e8>作者：</font>** Tzu-Heng Huang, Jet Lin, Eric Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical benchmarks for language models are built almost entirely on Western biomedicine. Traditional Chinese Medicine (TCM) is a separate system, with its own diagnostic framework and its own literature, and it remains largely unmeasured. The few TCM evaluations that exist are small, narrow, and rarely paired with a human reference. We present TCMQA, an open benchmark of 38,279 questions from Chinese TCM licensing examinations, paired with 15,151 responses from 101 licensed practitioners. We evaluate 29 instruction-tuned models from 9 families, spanning 0.27B to 14.8B parameters. Accuracy ranges over 59 points, and no model approaches saturation. Pretraining data predicts TCM ability far better than scale: a 12B Western-pretrained model reaches 39.6%, while a Chinese-pretrained model an eighth its size reaches 60.8%. Nine models exceed the practitioner majority vote of 64.9%, the best by 21.8 points, and all nine come from that same Chinese-pretrained family. Yet difficulty does not transfer between models and practitioners: accuracy is flat across practitioner-rated difficulty, item-level agreement is near zero for all 29 models, and on $8.4\%$ of items the practitioners are correct where the leading model is wrong. We release the corpus, the practitioner responses, the harness, and per-item model outputs at this https URL.

---


> [!TIP]
> 当前位于：**251-300**（第 6/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
