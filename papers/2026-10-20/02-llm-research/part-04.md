# 🧠 大模型相关研究 | 2026年10月20日

> 本类共 **258** 篇论文：已确认 **247** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-258](./part-06.md)

---

### 151. [Chinese Decision: A Family of Language Models for Single-Pass Probabilistic Decision-Making](https://arxiv.org/abs/2610.23170)

**<font color=#1a73e8>作者：</font>** Qiang Yan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many language-based applications require probabilities over a finite set of decisions rather than open-ended responses. We present Chinese Decision, a family of Chinese-language models for single-pass probabilistic decision-making. Given context, an instruction, and candidate descriptions, the model extracts final-position candidate-letter logits in one forward pass and normalizes them over valid options, without autoregressive answer generation. A shared interface supports Boolean judgments, categorical choices, and ordinal scores. We report a completed 0.8B model trained with distribution cross-entropy on 13.048 million decisions and preliminary 2B checkpoints trained with an additional RLCD objective. On the full CJ-Bench of 307,900 decisions, the uncalibrated 0.8B model achieves 72.24% general-domain accuracy and 76.98% average accuracy across medicine, law, and finance using a single checkpoint, with 1.07% overall expected calibration error. The 2B model reaches 72.56% general-domain accuracy after 40.13% of one epoch but has not surpassed the completed 0.8B model on the professional-domain average. We further evaluate a validation-temperature-scaled deployment model and its Q8 quantization, finding close aggregate performance while documenting individual prediction changes. We release the training, evaluation, and deployment pipeline. The current results establish a reproducible approach to Chinese probabilistic decisions but do not isolate the effect of model scale.

---


### 152. [Knowledge-Guided Distributional Prompt Learning with Visual Hierarchy for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2610.23172)

**<font color=#1a73e8>作者：</font>** Jiyul Ham, Seongho Yoon, Yonggon Jung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot anomaly detection (ZSAD) aims to detect anomalies in previously unseen classes using auxiliary images, with applications such as industrial visual inspection and medical imaging. Recent vision-language-model-based approaches improve ZSAD by aligning textual and visual representations, while distributional prompting further models prompt variability for unseen categories. However, existing methods do not explicitly combine normality-referenced distributional modeling with hierarchy-specific prompt specialization, limiting their ability to model anomalous semantics relative to normality while addressing both image-level detection and fine-grained localization. We propose Hierarchical Knowledge-Guided Distributional Prompt Learning (HiDist), a normality-referenced hierarchical distributional prompt framework for ZSAD. HiDist models each prompt token with a diagonal Gaussian distribution and generates stochastic prompt variations through Monte Carlo sampling. Rather than learning normal and anomalous distributions independently, anomalous prompt distributions are parameterized as deviations from learned normal references, explicitly encoding their dependency. The resulting distributions are specialized into global and local representations for image-level detection and pixel-level localization, respectively, while an adapted global visual representation guides hierarchical alignment. Experiments on seven industrial and medical datasets demonstrate strong cross-dataset performance across anomaly detection and localization tasks. Extensive ablation and representation analyses further support the effectiveness of the proposed distributional modeling and hierarchy-specific representation learning.

---


### 153. [Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2610.23181)

**<font color=#1a73e8>作者：</font>** Heming Zou, Qi Wang, Yixiu Mao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has become a scalable post-training paradigm for large language models. However, training agents over long-horizon interactions presents two challenges: using only terminal rewards makes turn-level credit assignment sparse and high-variance, while sequential mini-batch updates on a fixed rollout batch introduce policy staleness as the current policy drifts from the behavior policy. Existing approaches obtain denser credit via learned critics, process reward models, or on-policy distillation, but they rely on a value network, step-level annotations, or a stronger external teacher that increase training complexity. Meanwhile, importance sampling and clipping mitigate policy drift, but they do not specify a finite target that stops sequential updates from overshooting. In this work, we introduce TreeOPSD, a critic-free, tree-aware posterior self-distillation framework for long-horizon agentic reinforcement learning. Treating each interaction turn as a tree node, TreeOPSD branches alternative continuations from shared prefixes and recursively backs up terminal rewards into implicit turn-level credit. It then maps each credit to a closed-form, bounded teacher distribution parameterized by the likelihood ratio relative to the frozen behavior policy. Minimizing the divergence between this teacher and the student policy recovers the policy-gradient direction as the tangent at the behavior policy while bounding updates toward a finite target across sequential mini-batches. Empirically, TreeOPSD improves agentic capabilities across several competitive benchmarks and model scales, especially for long-horizon tasks, e.g., raising the average accuracy of Qwen3-30B-A3B-Thinking-2507 by 4.97 points over GRPO on the Deep Research setting.

---


### 154. [What LLMs Do in the Shadows: Reading Context Reliance from the Unembedding Dark Space](https://arxiv.org/abs/2610.23182)

**<font color=#1a73e8>作者：</font>** Alexandra Kuleshova, Andrey Volodichev, Daria Kotova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting faithfulness hallucinations in large language models (LLMs) is crucial for their safe deployment in high-stakes domains. Recent approaches address this by contrasting contextual against parametric knowledge utilization, yet measuring context reliance typically demands noticeable overhead, such as materializing attention maps, running additional forward passes, or training auxiliary probes. In this work, we show that context reliance can be estimated by projecting hidden states onto the dark space - directions that compose weakly with the unembedding matrix. Beyond its recognized function as an initial-token attention sink, we show that this subspace actively mediates context processing, and that its share of hidden-state norm - termed the Dark Matter Ratio (DMR) - provides a direct score of context utilization. Pairing DMR with a parametric knowledge score yields DarkLens, a lightweight faithfulness detector operating strictly within a single forward pass. Evaluated across three QA and summarization benchmarks on six open-weight LLMs (4B-13B parameters), DarkLens matches or outperforms a wide range of baselines without requiring extra forward passes or probe training.

---


### 155. [A Stronger Teacher Within: Strengthening MoE Models via On-Policy Bidirectional Distillation](https://arxiv.org/abs/2610.23185)

**<font color=#1a73e8>作者：</font>** Haoyu Chen, Jun Bai, Yang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has substantially improved Mixture-of-Experts (MoE) LLMs, but its outcome-level rewards provide only sparse supervision. On-Policy Distillation offers dense token-level feedback, yet requires a stronger compatible teacher, while on-policy self-distillation relies on hand-designed privileged information. We observe that the MoE architecture itself offers a way to resolve this dilemma, as increasing the activation budget per token exposes latent expert capacity and yields a potentially stronger teacher within the model. However, naive expansion degrades performance because newly co-activated experts are not optimized to work together. We therefore propose MoEvolve, a bidirectional distillation framework following a recovery-then-improvement strategy: we first restore the activation-expanded high-$k$ model and further strengthen it by exploiting its additional active capacity, then reverse the direction of distillation to transfer the enhanced capabilities back into the original low-$k$ configuration, retaining its inference-time activation budget. Across diverse MoE models and benchmarks, MoEvolve improves the initial models by up to $22.2$ domain-average points and outperforms same-budget RLVR baselines by up to $6.5$ points. Notably, the final low-$k$ models often surpass their activation-expanded teachers.

---


### 156. [LangNCO: Compiling Natural-Language Constraints into Inference-Time Interventions for Neural Combinatorial Optimization](https://arxiv.org/abs/2610.23190)

**<font color=#1a73e8>作者：</font>** Hironori Ohigashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural combinatorial optimization (NCO) rapidly produces high-quality solutions for problem structures encountered during training, but operational requirements may change after deployment and be communicated in natural language. We propose LangNCO, a framework that compiles instance-specific requirements into structured inference-time interventions for a frozen NCO solver, without changing the pretrained policy's architecture, learned input representation, or parameters. A pretrained LLM serves as a replaceable semantic front end, translating each requirement into a schema-validated domain-specific language (DSL) rule set. A deterministic Rule Executor applies the rules as nonexpansive hard action masks. Because local masking prevents immediate violations but does not ensure that a complete feasible continuation remains reachable, Critical-Offset Decoding extracts rule-referenced critical nodes and reallocates part of a fixed rollout budget to multi-strength biased rollouts. Using controlled task-specific language to isolate solver adaptation from open-ended language robustness, we evaluate a CVRP policy on road closures, time windows, vehicle assignments, visit-order requirements, all pairwise combinations, and twelve additional constraint types. LangNCO achieves 100% feasibility on the four primary datasets with mean reference gaps of 1.63--3.26%, 97.33--100% feasibility when separately generated rules are composed for pairwise constraints, and 98.67% feasibility across the additional constraints. These results demonstrate modular post-training adaptation of a frozen NCO solver through inspectable language-derived rules, without retraining.

---


### 157. [OfficeTown: Generative Organizations for Evolving Agent Intelligence](https://arxiv.org/abs/2610.23194)

**<font color=#1a73e8>作者：</font>** Hongchen Wei, Daohong Ying, Zhi Hong 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly use files and software tools to produce professional deliverables. Such work draws on materials, decisions, and feedback accumulated across assignments. We introduce OfficeTown, a generative simulation framework for professional organizations in which tasks and their context arise from continuing organizational work. From a natural-language description of an organization's purpose and activities, OfficeTown initializes an organization whose members coordinate work, delegate bounded assignments to assistant agents, and review their deliverables. Artifacts, decisions, and unresolved matters persist and shape subsequent work, while responsibilities and permissions determine what each member can see and do. We curate work requests, their context, and review feedback into executable resources for evaluation and learning. We construct OfficeTown Bench with 406 tasks and 4,836 evaluation criteria from 23 simulated organizations across eight professional domains, incorporating domain-expert feedback. Frontier-model evaluations reveal substantial remaining headroom. Supervised fine-tuning and on-policy distillation on OfficeTown data substantially improve Qwen3.5-9B on external professional-work benchmarks, including GDPval. Supplementary evaluations show that the principal--assistant harness achieves higher scores than the single- and multi-agent baselines tested. These results highlight the value of organizational simulation in generating work-grounded data and environments for the continued development of generalist agents.

---


### 158. [MAS-Bai: Linguistically Informed Adaptive Multi-Agent Translation for Bowen-Script Bai](https://arxiv.org/abs/2610.23205)

**<font color=#1a73e8>作者：</font>** Jingting Zheng, Hong Ren, Yuehan Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) remain unreliable for extremely low-resource languages whose writing systems conflict with high-resource pretraining priors. We study Bai-Chinese translation in the Bowen script, where Chinese characters are frequently borrowed phonetically rather than semantically, causing severe literal-translation hallucinations. We propose MAS-Bai, a linguistically informed adaptive multi-agent framework for Bowen-script Bai-Chinese translation. MAS-Bai routes each input through either a lightweight retrieval-translation path or a deeper philological path with etymological and syntactic agents, and uses cycle-consistency with a lightweight reverse translator as an inference-time reliability signal. We construct a 6,536-sentence Bai-Chinese corpus and evaluate on a 1,536-sentence test set. MAS-Bai achieves 16.23 BLEU and 62.15 COMET, improving over Standard RAG by 8.11 BLEU and 6.85 COMET. Forward LoRA, expert ablations and controlled routing experiments distinguish the roles of supervised adaptation, Bai-specific expertise and conditional routing. The largest gains occur on Bowen phonetic loans and divergent Bai word order, while human evaluation and reverse-verifier analyses support the automatic results.

---


### 159. [Not All Test-Time Compute Is Evidence: Model-Specific Bias in LLM Reasoning](https://arxiv.org/abs/2610.23213)

**<font color=#1a73e8>作者：</font>** Ming Shen, Tianjun Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling methods implicitly assume that additional computation from the same model provides independent evidence. We show that this assumption fails within a single reasoning model: errors are correlated across repeated samples, across reasoning depth, and in the model's own self-evaluation, so more compute from the same model is not more evidence. We introduce DIA (Disagreement-triggered Independent Arbitration), which treats disagreement between an intermediate-stage and the final-stage prediction as a per-question signal of reasoning instability and resolves it by asking a small panel of heterogeneous models to solve the question independently, without seeing either candidate, and aggregating their answers directly. Across seven benchmarks and two base models, DIA outperforms full chain-of-thought in 12 of 14 settings, including a 7.00% gain on MuSiQue, while activating on only $\sim 17\%$ of examples and using up to 47.2% fewer tokens than a multi-agent baseline. Ablations show that both independent solving and solver heterogeneity are necessary for these gains.

---


### 160. [MLLM Frame Subset Ensembling for Audio-Visual Video QA and MLLM-based Reranking for Ad-hoc Video Search in TRECVID 2025](https://arxiv.org/abs/2610.23214)

**<font color=#1a73e8>作者：</font>** Andreas Goulas, Damianos Galanopoulos, Ioannis Patras 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the overview of the runs related to the Ad-hoc Video Search (AVS) and Video Question Answering (VQA) tracks of TRECVID 2025 on behalf of the CERTH-ITI team. For the AVS track, we introduce a two-stage framework built on foundation models. In the first stage, multiple vision-language models (VLMs) encode both the input query, augmented through LLM-generated rephrasings, and the candidate video shots, producing weighted similarity scores for initial retrieval. In the second stage, we utilize a Multimodal-LLM(MLLM)-based reranking module that evaluates the semantic alignment between each shot among the top-N highest-ranked ones and the original query, generating updated relevance scores for reordering these shots. This MLLM-driven reranking significantly improves contextual matching and produces more accurate final rankings without requiring any model training. Regarding the VQA track, we fine-tune an audio-visual MLLM model on the provided TRECVID training dataset and we implement an inference-time scaling technique to enhance the multimodal understanding capabilities of the MLLM. For the open-ended Answer Generation (AG) task, we aggregate multiple model responses per question via a majority vote. The responses are generated with greedy sampling from different random frame subsets of the video and they are ranked based on the number of votes. For the Multiple-Choice (MC) task, instead of voting, we use mean pooling on the logits assigned by the fine-tuned model to each candidate response. Through the combination of fine-tuning and frame subset ensembling we achieve the highest score across 3 metrics in the VQA AG task and the second highest in the VQA MC task.

---


### 161. [Process Reward Modeling with Reliability- and Conservatism-Aware Bayesian Belief](https://arxiv.org/abs/2610.23223)

**<font color=#1a73e8>作者：</font>** Zhongjian Qiao, Zhixiang Zhou, Jiafei Lyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process Reward Models (PRMs) play a central role in test-time scaling for large language model (LLM) reasoning. However, PRMs may provide inaccurate process rewards for test-time scaling, which we identify as arising from two sources of uncertainty: (1) \textit{PRM uncertainty} that arises from insufficient supervision data and imperfect PRM training; and (2) \textit{policy uncertainty} that results from the mismatch between the policy to collect supervision data and the policy for test-time scaling, leading to systematic reward overestimation. Previous studies fail to jointly consider both uncertainties. To bridge this gap, we propose BayesianPRM, which treats the process reward as a random variable within a reward hypothesis space and maintains a Bayesian belief over it. Since exact Bayesian inference over the continuous hypothesis space is generally intractable, we discretize the reward hypothesis space with a reward ensemble and introduce two complementary belief updates, each targeting one source of uncertainty: (1) to address PRM uncertainty, we introduce \textit{reliability-aware belief updating} that measures how well each ensemble member explains the supervision data and updates the belief with an amortized belief network optimized by the evidence lower bound (ELBO); and (2) to tackle policy uncertainty, we propose \textit{conservatism-aware belief calibration} which further reweights the belief toward lower rewards to suppress overestimation. These two updates yield a reliability- and conservatism-aware Bayesian belief, whose expectation determines the process reward. Experiments on multimodal reasoning benchmarks indicate that BayesianPRM consistently yields more accurate process reward estimates while enhancing test-time scaling performance.

---


### 162. [ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling](https://arxiv.org/abs/2610.23225)

**<font color=#1a73e8>作者：</font>** Yuki Otsuka, Daisuke Oba, Naoaki Okazaki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Drifting Models generate a sample with a single function evaluation, making them attractive for fast parallel language generation, but their one-step formulation does not support iterative refinement. We propose Recurrent Language Generation via Drifting (ReLaDrift), which uses a shared Drifting Model to generate an initial draft from noise and iteratively refine it in a continuous latent space. We train this recurrence by sampling the number of rounds and applying the drifting loss only at the final round, stopping gradients through preceding rounds so that only one round requires backpropagation. Unlike the one-step Drifting Model, whose accuracy does not improve when iterated, ReLaDrift enables a trade-off between test-time computation and generation quality, as diffusion and flow language models do. On Sudoku Hard and GSM8K, it achieves competitive or superior performance compared with these iterative-generation approaches across a range of inference budgets. Our code is available at this https URL

---


### 163. [Characterising and Analysing Retrieval-Augmented Generation Techniques](https://arxiv.org/abs/2610.23226)

**<font color=#1a73e8>作者：</font>** Emmanuel Igbekele, Olawande Daramola  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The advent of Large Language Models (LLMs) across many application domains has increased the need for Retrieval-Augmented Generation (RAG) to reduce hallucinations and improve LLM performance. Thus far, several RAG techniques with impressive features and capabilities have been proposed in the literature, making it a herculean task to select the most appropriate RAG techniques for specific problem scenarios. Thus, we propose a conceptual framework comprising main dimensions and sub-dimensions for characterising (defining "what it is") and analysing (defining "how well it does") existing RAG techniques. The conceptual framework was developed through a qualitative analysis of the attributes of RAG techniques reported in the literature. It can serve as a pre-empirical filtering mechanism for researchers and practitioners in selecting the highest-fit RAG candidates that meet specific user and task requirements before empirical benchmarking of RAG techniques, which can be computationally and financially expensive.

---


### 164. [RAP: A Dataset for Paper-to-Poster Generation via Declarative Markup from Human-Crafted Exemplars](https://arxiv.org/abs/2610.23230)

**<font color=#1a73e8>作者：</font>** Haonan Han, Yukang Lin, Minliang Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Making a conference poster is visual coding in miniature: an entire paper must be compressed onto a single page, which exercises summarization, visual design, and code implementation at once, using nothing beyond the paper itself. Yet benchmarks for this task in the context of visual coding remain scarce: existing resources are small and annotated only with layout boxes, so evaluation must fall back on VLM-as-judge or human checklists rather than objective render-and-compare, and the generation methods they support design layouts from scratch, leaving human-crafted posters unusable as either a retrievable design library or as verified supervision. We introduce RAP (Reconstruct A Poster), a dataset and benchmark for paper-to-poster generation as a visual coding task. RAP contains 25K+ verified paper-poster pairs from various machine learning conferences held between 2022 and 2026, annotated with a three-level content taxonomy, plus a held-out benchmark of 150 test papers each paired with its human poster. A fully automated derendering pipeline turns each poster into styled HTML/CSS of typed, refillable slots, so every sample is a paper-poster-markup triplet verifiable by rendering against the source poster. The corpus serves both inference and training: PosterRAG, a training-free multi-agent pipeline, retrieves an exemplar and refills its slots without touching layout or styling, while an SFT+RL recipe trains a dedicated model from the same triplets. An online demo is available at this https URL.

---


### 165. [AgentLoupe: Kernel-Resident Semantic Causal Labels for AI Agent Observability](https://arxiv.org/abs/2610.23233)

**<font color=#1a73e8>作者：</font>** Yifei Bao, Ting Liu, Yuxin Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents translate user intents into system actions via tool invocations. Accurately attributing these actions to their originating LLM interactions is essential for security auditing, yet existing methods, such as AgentSight, fail for delayed execution and cross-process-lineage behaviors. We present AgentLoupe, an application-transparent eBPF-based observability tool. The core insight of AgentLoupe is to embed causal identity into kernel this http URL employs eBPF to capture TLS plaintext to interpret LLM interactions, and assigns each a kernel-resident semantic this http URL maintains labels in eBPF maps, then propagates this label across processes and threads, associates it with kernel resources such as files and sockets. When a persistent resource carries context to an independent process outside the original lineage, this design preserves the delayed causal this http URL show that the average observation overhead of AgentLoupe is below 8%, and case studies confirm AgentLoupe traces cross-lineage persistent attacks back to their originating LLM interactions.

---


### 166. [MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation](https://arxiv.org/abs/2610.23234)

**<font color=#1a73e8>作者：</font>** Yuhan Sun, Jiaxin Zhao, Yongdong Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In a hierarchical multi-agent system, a Leader assigns tasks and subagents carry them out. Jointly training the Leader and the subagents is difficult because a final answer gives only indirect feedback to the subagents. An LLM judge can score the performance of the subagents, but these scores depend on the judge's own assessment of the quality of subagents' responses. We present MultiAgent-OPD, which combines on-policy distillation with reinforcement learning to jointly train a shared-parameter Leader-Searcher-Answerer team end to end. We first train a Teacher in a Searcher-Answerer workflow using answer correctness. During team training, the frozen Teacher scores student-generated search and summary tokens to provide local process supervision for the Searchers, while the Leader learns from team success and the Answerer from candidate correctness. Across seven datasets, the trained system reaches 38.68% macro avg@4, exceeding Prompted Critic by 4.06 percentage points and C-MAS + RL, the trained cascaded multiagent system, by 2.61 percentage points. The team also solves more questions within four attempts.

---


### 167. [Response-Informed Value Estimation for Cost-Aware Multi-Turn LLM Routing](https://arxiv.org/abs/2610.23239)

**<font color=#1a73e8>作者：</font>** Haotian Yan, Jiaqi Liu, Bingyi Jing 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn LLM routing selects a model at every turn before its response is available, yet task success is revealed only when the interaction ends, leaving each intermediate choice without a label of its own. Logged trajectories, however, retain the response each call produced, which exposes what each turn required and how well the chosen model served it, evidence that outcomes alone hide. We introduce RIVET (Response-Informed Value Estimation for Turn-Level Routing), which exploits this post-call evidence during training while keeping routing strictly pre-call at deployment. RIVET jointly trains two value estimators over a shared state-model representation: a deployable Routing Value Estimator that scores candidate models from pre-call information, and a training-only Response-Informed Value Estimator that additionally observes the realized response. Conditioning on the response turns response-induced return variation from residual noise into an observed covariate, and we show that this reduces the leading asymptotic estimation error of the shared representation. On the MINT benchmark, RIVET solves more held-out tasks than the strongest multi-turn baseline while using 74.7% less total call cost.

---


### 168. [MGE-PO: Entropy-Aware Credit Assignment for Mathematical Reasoning](https://arxiv.org/abs/2610.23245)

**<font color=#1a73e8>作者：</font>** Jihao Huang, Guangjia Chai, Zhirui Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GRPO assigns the same group-relative advantage to equally rewarded responses within a question, leaving their generation uncertainty unused. We introduce MGE-PO, centered on four-quadrant (4Q) advantage shaping that combines verified correctness with rollout generation entropy. Correctness determines the sign of an additional correction, while entropy controls its magnitude: lower-entropy successes receive larger bonuses and higher-entropy failures receive larger penalties. An online entropy-based question curriculum supports this credit rule using cached rollout measurements. At the final checkpoint after eight training epochs on Qwen3-8B-Base, adding 4Q across three policy optimization settings yields absolute gains of 3.23-3.69% in six-benchmark macro avg@32 and 4.24-11.06% in macro pass@32. On Qwen2.5-7B-Base, the complete configuration raises four-benchmark macro avg@32 from 41.5% to 45.4%.

---


### 169. [Who Pays for Efficient Inference? Confidence-Based Small-to-Large LLM Routing Across Tasks and Languages](https://arxiv.org/abs/2610.23249)

**<font color=#1a73e8>作者：</font>** Md Sabbir Hossen, Anichur Rahman, Pabon Shaha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small-to-large language model routing can reduce inference cost by escalating difficult inputs while retaining easier ones on a smaller model. Its success, however, depends on identifying examples that benefit from escalation, and the reliability of confidence across multilingual tasks remains unclear. We present a systematic evaluation of confidence-based routing across three model families, four languages, and three task types, covering 72 model, dataset, language, and scale configurations and 42,288 predictions. We compare global confidence routing with random routing, equal-quota confidence routing, and an oracle upper bound. Confidence identifies beneficial escalations on the Belebele reading comprehension and SIB-200 topic classification datasets, with mean correction-detection AUCs of 0.612 and 0.705. At 50% escalation, it improves over random routing by 1.40--4.67 percentage points on Belebele and 2.54--5.63 points on SIB-200. In contrast, the mean AUC on the MMLU-ProX-Lite knowledge and reasoning dataset is only 0.510, and routing provides no consistent improvement over random selection because small models often remain highly confident while incorrect. Global confidence routing also creates language escalation gaps up to 30.33 percentage points, whereas equal-quota routing removes this disparity with little aggregate accuracy cost. These results show that confidence routing is task-dependent and can allocate computation unevenly across languages. Code is available at this https URL

---


### 170. [FLARE: Physics-Grounded Evaluation of Language-Model Agents for Feeder Restoration with Degraded Observations](https://arxiv.org/abs/2610.23251)

**<font color=#1a73e8>作者：</font>** BHVSP Subrahmanyam, Neeraj Choudhary  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Restoring service after distribution-grid faults requires decisions from incomplete and conflicting information while respecting electrical constraints. Addressing this need, we introduce FLARE (Feeder-Level Agent Restoration Evaluation), a physics-grounded benchmark for post-isolation feeder restoration. FLARE con- tains 800 AC-feasible cases across five observation settings and allows agents to gather evidence, evaluate switches, and perform restoration actions under fixed operational limits. We evaluate five instruction-tuned models over 78,750 episodes, including topology, distributed-generation, and loading shifts. Mean normalized regret ranges from 0.082 to 0.148. Although every model has zero median regret, P95 regret ranges from 0.814 to 1.000, revealing an important failure tail. Shadow replay shows that 96.4% of 15,706 guard-rejected actions would have caused a physical violation. FLARE enables reproducible evaluation of language-model based restoration support while emphasizing the need for external safety checks.

---


### 171. [Sample, Mix, or Verify? Allocating Test-Time Compute under Imperfect Verifiers](https://arxiv.org/abs/2610.23255)

**<font color=#1a73e8>作者：</font>** Srinivasan Iyengar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A common way to make language models and agents more accurate is to spend more compute at inference time: generate many candidate solutions and submit the one a verifier prefers. Success then requires that some candidate is correct and that the verifier picks it. The first grows predictably with the number of samples; the second does not, because real verifiers (unit tests, majority votes, LLM judges, reward models) accept wrong answers, reject right ones, and make correlated mistakes. With a fixed budget, a practitioner must decide how many samples to draw, which models to draw them from, and how much to spend on verification, and today these choices are made by rules of thumb. We introduce SPLIT, which makes them from a small labelled pilot. It rests on an exact formula for the probability of submitting a correct answer under accept/reject and top-score selection that accounts for varying task difficulty, blind spots shared across models, and correlated repeated verifier calls. SPLIT fits the formula by empirical Bayes and uses it to plan budgets on unseen tasks. Across seven benchmarks spanning math, science QA, code and software-engineering agents, 26 models, 175 agent systems and six kinds of real verifiers, all from public releases, SPLIT lands within 0.02-0.8 percentage points of the best allocation in hindsight, while every fixed rule we test loses at least 2.5 points in some setting. Regret depends only on how well SPLIT ranks configurations, and it stays near-optimal under compute, price and latency costs and online. The formula also explains when asking more LLM judges lowers precision. As a forecaster far beyond the pilot, SPLIT beats power-law fitting when the verifier caps success, and we report where it loses.

---


### 172. [Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To](https://arxiv.org/abs/2610.23257)

**<font color=#1a73e8>作者：</font>** Uriel Dolev, Idan Schwartz, Yoav Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) controllability, the ability of reasoning models to control properties of their CoT, is consequential for both their usefulness and reliable oversight. Recent work evaluates this capability by measuring whether models follow CoT constraints given in the user prompt, and reports very low controllability across models. We argue that this low controllability may not reflect an inherent inability of reasoning models to control their CoT, but instead result from naively specifying constraints in the user prompt. To test this, we introduce Self-Instructed CoT Controllability: a complementary evaluation that places the constraint as a self-instruction inside the model's CoT and measures its ability to follow it. We show that, under self-instruction, models achieve significantly higher controllability than with standard user instructions. Even a generic reminder to follow the user's constraint substantially improves controllability. Moreover, effective self-instructions can be bootstrapped into the reasoning through a simple instruction in the user prompt, enabling improved control even without access to the reasoning channel. Finally, using self-instruction, we demonstrate in a realistic monitoring setup that CoT controllability can be leveraged for monitor evasion, posing a risk to CoT monitorability.

---


### 173. [Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents](https://arxiv.org/abs/2610.23266)

**<font color=#1a73e8>作者：</font>** BHVSP Subrahmanyam, Neeraj Choudhary  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-agent memory selection often uses retrieval rankings based on record relevance or individual influence. Such rankings cannot identify sufficient subsets under redundant or jointly necessary evidence. We study per-decision memory sufficiency: selecting a small subset that preserves full-memory behavior. To separate search error from model error, we introduce JointCoreBench, a benchmark with nine interaction families, six workflow domains, natural-language decisions, and exact sufficient-set oracles, and JointCore, a relevance cost-ordered group-deletion baseline that tests blocks before individual records. On 6,912 exact conditions, cost-ordered JointCore recovers a minimum-cost sufficient set in 100.0% of cases, reduces subset evaluations from 30.00 to 11.13 (62.9%), and achieves 87.8% active-memory savings. Across four 12B-70B model families and 432 tasks per model, its unweighted mean is 10.28 versus 16.00 model queries and 50.6% versus 43.1% minimum-cost recovery relative to cost aware singleton deletion. Both methods preserve full-memory behavior under the deterministic primary interface. Tests with physical deletion, UNKNOWN masks, PENDING sentinels, counterfactual values, and alternative labels identify interface dependent behavior. JointCore is an efficient benchmark baseline; the study does not establish deployment-ready memory compression.

---


### 174. [Verbalising Model's Computation for Chain-of-Thought Faithfulness Detection](https://arxiv.org/abs/2610.23275)

**<font color=#1a73e8>作者：</font>** Yujing Wang, Yulan He, Wenya Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current Chain-of-Thought (CoT) verification methods detect reasoning faithfulness from model outputs or static activations, but are limited in explaining how unfaithfulness develops during generation. We introduce VERITAS to verbalise the model's computation: how different reasoning anchors emerge, transfer across layers, and surface in the output. VERITAS adopts the layer-wise Jacobian projection to produce a verbalised account of the model's internal reasoning evolution at each generated CoT token. By training a classifier on the extracted features along the traces, we show that these structured features provide insightful perspectives on how and where reasoning diverges toward unfaithfulness. Experiments on four datasets from FaithCoT-Bench and BonaFide show that VERITAS achieves a significant performance gain over LLM-as-Judge, with a 28.4% gain in balanced accuracy, and an average improvement of 16.0% over activation probing. Further analysis shows VERITAS can be generalised to different datasets and model architectures. Our work shows that verbalising model computation provides a richer and more interpretable lens on CoT faithfulness, moving beyond detection toward a mechanistic understanding of how reasoning fails.

---


### 175. [Xiaomi-Lens-0 Technical Report](https://arxiv.org/abs/2610.23279)

**<font color=#1a73e8>作者：</font>** Pei Fu, Yike Liu, Yue Sun 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) answer questions about whole images well, yet they still struggle with fine-grained region understanding. A key reason is that text-only supervision never specifies which regions support an answer. To close this gap, we present Xiaomi-Lens-0, a 4B MLLM built on Qwen3.5 that predicts masks from its own visual representations. Specifically, a lightweight decoder combines vision-encoder patch features with visual latents, the language model's mask-token states, so mask supervision reaches the shared backbone without an additional segmentation encoder. Because each latent decodes to a mask, the model can interleave reasoning with region-specific latents and thus think with visual latents, while grounded reasoning traces supervise the regions it visits during chain-of-thought. As a result, across all eight RefCOCO, RefCOCO+, and RefCOCOg splits, Xiaomi-Lens-0 gains 5.6 points on average over Qwen3.5 in referring comprehension and achieves the highest segmentation cIoU among compared models. Moreover, it surpasses Qwen3.5 across all perception benchmarks. Homepage: \href{this https URL}{this https URL}

---


### 176. [Annotrace: A Workbench for Step-Level Annotation of Agent Traces](https://arxiv.org/abs/2610.23284)

**<font color=#1a73e8>作者：</font>** Arun Josephraj Arokiaraj, Chenyi Huang, Sahan Bulathwela 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every study of why LLM agents fail begins by labelling traces by hand, and every such study builds its own throwaway tool. Observability platforms record agent traces but offer no structured labelling; annotation tools label text but have no notion of a step, a delegation or a tool call, leaving it unclear what the smallest unit of execution to label should be. Annotrace reads six trace formats, including OpenTelemetry GenAI, LangSmith and Langfuse, and turns each run into an ordered, nested list of steps. The annotator writes their own labelling codebook; a frontier model proposes a starting set from a sample of their own traces, answers first, and is asked exactly the questions the human is asked, making annotation a joint human-AI process. Annotrace measures agreement between any two annotators, human or AI. On a multi-agent question-answering corpus it reproduces a previous manual effort's 235 annotation units exactly, and two models labelling the same traces agree 91% of the time at $\kappa = 0.82$.

---


### 177. [CoTA++: Understanding the Repeat Curse in dMLLMs from an Information Flow Perspective](https://arxiv.org/abs/2610.23290)

**<font color=#1a73e8>作者：</font>** Qiyan Zhao, Xiaofeng Zhang, Xu-Yao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion-based multimodal large language models (dMLLMs) decode by iterative denoising with bidirectional attention, which precludes the standard autoregressive key--value cache. Practical deployments therefore rely on approximate caching that reuses intermediate states across denoising steps. Such caching, however, often makes a response repeat one token at adjacent positions in a run that breaks the sentence, a failure we term the \emph{Repeat Curse}. Tracing the context-token information flow reveals three disruptions. Within a step, caching disperses the attention that anchors a position on nearby context tokens. Across steps, similarity-based refresh is not staleness-aware, so some positions are decoded against stale key--value states. Across layers, the deep-layer entropy of the context fails to converge where repetition arises. We accordingly propose CoTA++, a training-free, plug-and-play framework that counteracts each disruption where it originates: Context-Token Attention Re-anchoring re-forms the attention routing against the current context, Decode-Aware Refresh reserves part of the cache's refresh budget for the positions about to be committed, and Context-Token Entropy-Guided Voting discounts the confidence of a position by the deep-layer entropy of its context, which reorders the unmasking. The three components act at non-overlapping stages of a decoding step and compose freely with existing dMLLMs and caches. Across three dMLLMs and two caching backends, CoTA++ reduces the sample repetition rate of long responses from up to 99.6\% to at most 17.0\%, recovers most of the accuracy lost to caching on nine benchmarks, and keeps the speedup of caching at under 15\% overhead, making approximate caching reliable for dMLLMs.

---


### 178. [Optimist Deep Research: An Iterative, State-Centric Agent for Autonomous Literature Research](https://arxiv.org/abs/2610.23299)

**<font color=#1a73e8>作者：</font>** Gihan Panapitiya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most retrieval-augmented systems treat literature search as a single retrieval step followed by summarization. Real literature research works differently: the investigator's understanding of the question changes as they read, new subquestions appear, and evidence is weighed, not just collected. We present Optimist Deep Research, an open-source agent that runs literature research as an iterative evidence-acquisition process over an explicit, mutable research state. A research question is broken into a tree of subquestions, each served by search intents that are translated into source-specific queries over arXiv, OpenAlex, Crossref, PubMed, Semantic Scholar and the web. Results are merged into a canonical, provenance-preserving document registry through a conservative four-tier deduplication hierarchy. The registry is expanded by citation snowballing until a saturation criterion is met, and then screened, ranked and allocated to subquestions round-robin. Documents are read in parallel into a structured evidence store of claims with support, location, type and strength. A critic reviews the state along eight dimensions and returns research actions rather than a binary verdict: it can add, split, rephrase, deprioritize or close subquestions, so the research plan is an output of the investigation as well as an input. The final report is written section by section from the evidence store, and every citation resolves to a retrieved document. We describe the design, the deterministic machinery that keeps a language-model pipeline auditable, and a case study that read 28 of 237 retrieved documents in about three and a half minutes. We also report weaknesses the case study exposed.

---


### 179. [Look, Reason, Draw a Region: Recursive Refinement for Spatial Context Prediction](https://arxiv.org/abs/2610.23302)

**<font color=#1a73e8>作者：</font>** Wajeeha Tahir, Anna Tegon, Lionnus Kesting 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial context prediction requires visual grounding and spatial reasoning to identify vacant regions relative to objects in a scene. Spatial relationships and physical constraints remain challenging for large vision-language models (VLMs). Recursive reasoning has demonstrated strong performance on discrete and abstract reasoning tasks, motivating its use for improving spatial context prediction in natural images. Weight sharing enables higher accuracy with a small trainable parameter count. We introduce Spatial-TRM, a compact recursive model with frozen vision-language features, a convex region decoder, and just 11.2M trainable parameters. This weight-tied reasoner supports six spatial relationships, three reference frames, and open-vocabulary anchor objects. On the RoboSpatial-Home benchmark, Spatial-TRM achieves 29.51% context accuracy, a gain of 9.02 percentage points (44.0% relative) over a separately trained single-step model with the same parameter count. Including the frozen encoders, the model has 877.8M total parameters, approximately $15\times$ fewer than the reported 13B size of RoboPoint. These results show that repeated refinement improves spatial context prediction from pretrained vision-language features at a fixed trainable parameter count on this benchmark.

---


### 180. [Designing for Imperfect Prompts: A Simulation-Based Evaluation of an LLM-Based Enterprise Data Assistant Using Knowledge Graphs](https://arxiv.org/abs/2610.23304)

**<font color=#1a73e8>作者：</font>** Niklas Wagner, Alexander Mädche  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Enterprise data assistants using large language models (LLMs) promise democratized data access in organizations. Yet in our real-world deployment within the CFO unit's data lake at an industry partner, we observed that business users frequently pose imperfect prompts that include domain-specific vocabulary and lack schema references or structural information. This Design Science Research study examines automatic resolution using a semantic mediation layer. We design and evaluate two design variants: schema-based mediation via semantic similarity, and knowledge graph-based mediation leveraging an automatically constructed knowledge graph from the data lake. Our simulation-based evaluation using real-world data, supported by LLM-as-a-Judge assessments and human validation, shows that knowledge graph-based mediation outperforms the schema-based approach in Precision, Recall, F1, and preserving user intent. We propose a design principle for knowledge graph-based mediation, demonstrating that structured knowledge representation bridges user intent and database structure and guides the design of enterprise data assistants across skill levels.

---


### 181. [SimOPD: Relational Knowledge Transfer for On-Policy Distillation](https://arxiv.org/abs/2610.23306)

**<font color=#1a73e8>作者：</font>** Kai Tang, Xing Zheng, Haobo Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A key challenge in on-policy distillation (OPD) is extracting effective supervision from teacher knowledge. Supervision from token probabilities may underutilize internal knowledge, while direct hidden-state matching forces the student to shift to the teacher's feature space and complicates cross-architecture transfer. Inspired by contrastive learning's use of relationships between instances, we propose \textbf{SimOPD} to transfer teacher internal knowledge through response similarities. Specifically, SimOPD uses paired memory banks of student-generated responses to extract supervision from the teacher's internal representations as similarity distributions. The student then matches these distributions within its own representation space, retaining representational freedom and removing the need for cross-model projection. Extensive experiments show that SimOPD improves the overall average over the strongest baselines by up to 2.6 and 3.1 percentage points in same- and cross-architecture settings.

---


### 182. [MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection](https://arxiv.org/abs/2610.23307)

**<font color=#1a73e8>作者：</font>** Songping Wang, Peiyang Li, Yi Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal large language model (MLLM)-based mobile agents are rapidly evolving from conversational assistants into autonomous systems that perceive, reason over, and act on smartphone environments. This capability also exposes a new security risk: adversaries can embed malicious objectives in cross-application mobile content and steer agent behavior through indirect multimodal injection. Although prompt injection has been studied in desktop and web settings, its cross-modal properties in mobile ecosystems remain poorly understood, and existing security analyses are still limited. To close this gap, we introduce MobileInject, the first benchmark for evaluating mobile agents against multimodal injection attacks and reasoning-to-action security risks. MobileInject provides a high-fidelity interactive mobile evaluation framework covering 11 scenarios, 9 security-risk categories, and 108 executable risk instances. It further introduces Cross-Modal Consistency Injection to exploit corroboration across modalities, two enhanced attack methods, Multi-Role Collaborative Deception and Reasoning-Camouflage Injection, to intensify trust manipulation and reasoning hijacking, and a Reasoning Security Diagnosis Framework for fine-grained failure analysis. Systematic experiments show that mobile agents are broadly vulnerable to multimodal injection, and that many failures stem from reasoning hijacking at early stages. These findings establish MobileInject as a systematic cross-modal benchmark for studying and improving the security of mobile agents. Code release details are provided in the Appendix Open Science section.

---


### 183. [Inferring L1 Backgrounds from L2 English with LLM Token Probabilities](https://arxiv.org/abs/2610.23309)

**<font color=#1a73e8>作者：</font>** Ahmet Yavuz Uluslu, Mark Gales, Kate Knill 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Native language identification (NLI) infers a non-native speaker's first language (L1) from their second language (L2) production. We investigate a token probability approach that scores each text sample as a continuation of a prompt prefix specifying a candidate L1, then predicts the candidate with the highest score. We evaluate our approach using Llama 3.1 8B and 70B on three datasets: TOEFL9, Write and Improve 2024, and BULATS-L1. We compare its performance with previous prompting-based classification approaches. Token-probability scoring substantially improves on direct classification, particularly with the 8B model, while the 70B model achieves state-of-the-art performance across all datasets. Our results indicate that pretrained LLMs' token probabilities contain information useful for distinguishing L1 backgrounds from L2 English production.

---


### 184. [Self-Reflective Chain-of-Thought (SRCoT): Evidence-Based Text Generation via a Closed-Loop Retrieve--Reflect--Revise Pipeline on Edge LLMs](https://arxiv.org/abs/2610.23311)

**<font color=#1a73e8>作者：</font>** Fabian Broszio, Michael Hoffmann, Adrian Paschke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate fluent outputs that lack source support or conflict with local operational constraints. We introduce Self-Reflective Chain-of-Thought (SRCoT), a modular architecture that organizes generation as a closed Retrieve--Reflect--Revise loop. SRCoT separates environment state, persistent knowledge, accumulated experience, and short-term memory into provenance-labeled stores. BM25 retrieval supplies local context; subsequent passes expose intermediate drafts, missing-information markers, follow-up queries, and optional claim--evidence mappings. These artifacts inform retrieval, revision, clarification, or abstention decisions. We examine the architecture through qualitative, trace-based case studies in two fully synthetic settings: emergency medical services and Munich-Sim, an emergency-operations simulation. Local prototype runs on an Apple M4-family laptop with 128 GB memory illustrate source-labeled documentation, explicit gap marking, and structured dispatch-style outputs. The traces also reveal provenance-assignment errors, incomplete evidence coverage, and unsafe assumptions that remain possible despite prompting constraints. These cases demonstrate report-level inspectability and local execution, not comparative superiority, hallucination reduction, clinical validity, or operational safety. The architecture separates retrieval and control from the model interface, but behavior across different models remains to be evaluated. SRCoT is a research proof of concept requiring human review, with its principal contribution lying in an inspectable control procedure rather than a new model.

---


### 185. [From Memory Hits to Answerable Evidence: Query-Conditioned Memory Compilation for Long-Term Agent Memory](https://arxiv.org/abs/2610.23313)

**<font color=#1a73e8>作者：</font>** Shangze Li, Yanyu Yao, Derong Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term agent memory requires recovering answer-relevant evidence dispersed across turns and sessions. Existing systems increasingly use structured memories and adaptive retrieval, yet often pass retrieved or expanded units directly to the reader, coupling memory addressing with evidence presentation and leaving the final context redundant or incomplete. To address this gap, we propose MemCompile, a query-conditioned evidence compilation framework for long-term conversational memory. Given a query, the Address Plane locates relevant support through compact source-linked descriptors and capacity-aware Cells, while a normalization boundary resolves heterogeneous retrieval hits to stable SourcePacket identities. Its Evidence Plane then allocates a bounded evidence budget across complementary packets, admits limited additional support, and renders the retained claims associated with each selected packet into an answer-ready context. MemCompile achieves 80.52% Judge Accuracy on LoCoMo and extends the empirical quality-cost Pareto frontier to a higher-quality regime. Its strong performance on LongMemEval-S further suggests that the benefits of query-conditioned compilation generalize across long-term conversational-memory benchmarks.

---


### 186. [AgentOnto: Ontology-Guided LLM Agents for Enterprise Data Analytics](https://arxiv.org/abs/2610.23317)

**<font color=#1a73e8>作者：</font>** Dayan Pan, Bincheng Zuo, Xiaojian Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise data analysis requires agents to connect analytical requests with knowledge distributed across databases, business documents, and existing example tasks. Without an explicit representation of this knowledge, an agent may produce incorrect analytical results and cannot reliably incorporate feedback. We present AgentOnto, an ontology-guided LLM agent for enterprise data analytics. AgentOnto organizes heterogeneous enterprise knowledge into an ontology that directly guides analysis and incorporates confirmed feedback. Iterative Ontology Preparation further improves the ontology through self-generated analysis tasks. We evaluate AgentOnto on two public data sources. AgentOnto substantially outperforms representative methods, while module-level evaluations confirm the effectiveness of ontology construction, analysis, and updating. A real-world deployment further demonstrates its practical value in enterprise analytics. These results demonstrate that explicitly constructing, using, and updating enterprise knowledge supports reliable and adaptable data analysis.

---


### 187. [CatchUp: Depth-Aware Re-Admission of Visual Tokens for Efficient Large Vision-Language Models](https://arxiv.org/abs/2610.23324)

**<font color=#1a73e8>作者：</font>** Eunju Park, Uiwon Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) repeatedly process hundreds of visual tokens across decoder layers, incurring substantial computation and memory costs. Existing inference-time visual token pruning methods often irreversibly remove low-ranked tokens, although the set of visual tokens receiving high query-conditioned attention can change across decoder depth. Recoverable routing preserves skipped tokens for later reconsideration, but re-admits them with stale representations after bypassing intermediate transformations. We further find that replacing stale re-admitted states with their current-depth oracle states from a full-token reference trajectory substantially improves grounding performance. We therefore propose CatchUp, a training-free framework for depth-aware visual-token re-admission. CatchUp repeatedly re-evaluates query-conditioned visual relevance, processes only selected visual tokens through each decoder interval, and preserves deferred tokens for later re-admission. Upon re-admission, CatchUp approximates missed representation evolution using reference-to-current transition signals from semantically and spatially related visual tokens. Across three referring-expression grounding datasets and six multimodal benchmarks, CatchUp achieves the highest average relative retention in both benchmark groups at 64-, 128-, and 192-token budgets. At a 64-token budget with 88.9% fewer active visual tokens, CatchUp retains 92.17% of the full model's performance on average across six multimodal benchmarks while reducing end-to-end latency by 8.0%. Code is available at this https URL

---


### 188. [Wait for It: A Component-Level Analysis of Latency Feedback Mechanisms for LLM Agents in VR](https://arxiv.org/abs/2610.23336)

**<font color=#1a73e8>作者：</font>** Pratham Arora, Abhinav Lodha, Siddharth Siddharth  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Delays in AI responses pose a significant challenge to immersive Virtual Reality experiences. While previous research demonstrates that feedback can reduce the perception of waiting, we lack understanding of which types work best and why. We conducted a within-subjects study with 18 participants to systematically compare three isolated feedback approaches during VR agent interactions: verbal fillers (e.g., um..., hmm...), visual indicators (loading spinners), and embodied gestures (thinking animations). Our results revealed that embodied gestures significantly outperformed visual loading indicators across multiple dimensions, making agents feel more lifelike and socially present. Interestingly, explicit visual feedback like loading spinners actually degraded perceived humanness and broke immersion by forcing users to shift from social to technical mental models. These findings suggest that natural, behavior-based feedback maintains the illusion of conversing with a thinking entity, while technical indicators expose the computational substrate. We present empirically-grounded design guidelines for creating more engaging AI-powered VR agents.

---


### 189. [Minimax-optimal Scaling Laws in Ridge Regression via Transfer Learning](https://arxiv.org/abs/2610.23337)

**<font color=#1a73e8>作者：</font>** Yalda Shabanzadeh, Diyuan Wu, Marco Mondelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained models are often reused across downstream tasks, motivating the question of whether this transfer learning procedure can provide a substantial performance improvement, namely, in terms of the scaling law. We address this question in the prototypical setting of high-dimensional regression, where (i) a pretrained \emph{source} model is trained via ridge regression, and (ii) a fine-tuned \emph{target} model is regularized via the $L_2$ distance from the source estimator. First, we establish a deterministic equivalent for the risk of this two-step procedure under both model and covariance shift. Next, by specializing the deterministic equivalent to a shared regression function and commuting power-law covariance spectra, we identify a regime where the resulting scaling law achieves the minimax-optimal exponent. Notably, in this regime, the optimal source regularization depends on source data only, indicating its universality across all targets. Furthermore, we show that the same optimal rate is achieved by performing the fine-tuning step via one-pass stochastic gradient descent. We support our theoretical analysis via experiments on both synthetic settings and language models.

---


### 190. [Robust Function Calling for LLM Agents Under Interface Drift](https://arxiv.org/abs/2610.23342)

**<font color=#1a73e8>作者：</font>** Aniruddha Chattopadhyay, Kanishka Halder, Partha Sarathi Roy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented language-model agents rely on interface text: tool descriptions, argument schemas, and the candidate tool list shown at inference time. These interfaces often change after deployment even when the underlying tool semantics remain fixed, creating a practical reliability problem for function-calling systems. We study this failure mode as interface drift and evaluate whether a lightweight, training-free repair layer can recover robustness without retraining the base model. Our method, SchemaShield-Lite, combines schema validation, candidate-set retry for missing tool names, and one-shot constrained repair. On Qwen3.5-9B, it raises DICE-300 accuracy from 0.717 to 0.813 and BFCL-200 accuracy from 0.580 to 0.805, recovering 19/22 and 33/45 drift-induced failures with no observed repair harms. Naive retry does not explain the gains. Ablations show that candidate-set drift, especially distractor tools, accounts for most observed damage, while description and schema edits alone are less harmful. The results position validation-and-repair as a practical robustness layer for deployed LLM-agent tool use.

---


### 191. [Language Models Learn to Improve Language Models](https://arxiv.org/abs/2610.23344)

**<font color=#1a73e8>作者：</font>** Minhua Lin, Zijun Wang, Zewen Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to automate AI research, including language-model (LM) development, offering a potential path toward recursive self-improvement. However, turning experimental feedback into a learned ability to propose effective improvements across models faces two challenges. First, training such an ability with real feedback is expensive: reinforcement learning (RL) requires evaluating tens of thousands of proposals, each potentially requiring a full model-training run. Even at ten GPU-hours per run, reward collection alone would consume hundreds of thousands of GPU-hours, motivating a cheaper surrogate. Second, surrogate feedback can become unreliable as policy optimization favors overestimated proposals when the proposal distribution shifts. To address these challenges, we propose LM2LM, which trains LLMs with RL to generate effective LM improvement proposals. To provide scalable feedback, we use a research world model (RWM), a frozen LLM that predicts proposal gains from real experimental records provided in context, as the reward model for RL. To maintain feedback reliability, we periodically execute current-policy proposals ranked highly by the RWM and add their measured outcomes to its context. Across eight autoregressive and diffusion LM development environments, real-execution evaluations on held-out tasks show that LM2LM enables Qwen3.8-27B to outperform GPT-6-sol, even when GPT-6-sol is given 300 real experimental records in context, while requiring 33% lower data-generation cost. LM2LM also generalizes to a model family unseen during training.

---


### 192. [FloodVLM-Pix: Language-Guided Pixel-Level Flood Understanding](https://arxiv.org/abs/2610.23377)

**<font color=#1a73e8>作者：</font>** Chengyang Zhang, Zhihao Wang, Zhiyu Long 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As climate change intensifies, floods are becoming more frequent and destructive, making accurate flood understanding an urgent priority. However, existing vision-language models perform poorly on flood-related tasks, suffering from attentional bias and inaccurate descriptions of flood magnitude. To bridge this gap, we construct the first large-scale remote sensing flood multi-modal benchmark that supports language-level flood understanding and pixel-level flood segmentation. The benchmark contains 131,200 flood image patches and corresponding 443,100 textual descriptions for flood severity and evolution. Based on this benchmark, we propose FloodVLM-Pix, a language-guided pixel-level flood understanding model that includes a flood prior module and a multi-temporal flood pixel decoder to achieve accurate flood understanding. The flood prior module automatically distills sub-region flood spatial priors and inputs priors into FloodVLM-Pix, solving the attentional bias problem in flood language understanding. The flood pixel decoder introduces a novel general-specific feature fusion mechanism to address performance degradation caused by interference (e.g., clouds or mountain shadows) during flood segmentation. Experiments on FloodVL-Pix demonstrate that FloodVLM-Pix improves both flood description quality and pixel-level flood segmentation performance compared with state-of-the-art VLMs and flood segmentation models. Our code and data will be released at this https URL.

---


### 193. [On the Tip of the Tongue: First-Token Cueing as a Behavioral Probe of Recall Failures in LLMs](https://arxiv.org/abs/2610.23400)

**<font color=#1a73e8>作者：</font>** Jaewon Sok, Jewon Yeom, Seonghyeon Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often answer factual questions incorrectly in closed-book settings, and such errors are usually attributed to missing knowledge. Yet models often encode answers they fail to produce. We show that many closed-book errors are first-token recall failures: the model commits to a wrong first token, but once given the right one it completes the answer and often recognizes it as correct. We study this with First-Token Cueing, a behavioral probe that prefills the response with the first token of the gold answer. Model uncertainty peaks at the first answer token, where it already predicts correctness, and among gold prefixes of any length the first token alone accounts for the largest share of recovered errors. Across 16 open models, this one token corrects between a fifth and a half of the errors on multi-token answers in English QA and improves accuracy in all seven languages of a multilingual benchmark. Most of the errors it corrects are also solved by the model's own sampled reasoning, a criterion for encoded knowledge, and models recognize correct starts they do not produce: they continue a correct start more confidently than an incorrect start of the same answer type and prior probability, yet rarely find it without the gold answer. These results locate a recoverable class of factual errors at the first decoding step, where inference-time methods may gain the most.

---


### 194. [GeoReason: Bridging Logical Reasoning and Spatial Fidelity in Remote Sensing Segmentation](https://arxiv.org/abs/2610.23416)

**<font color=#1a73e8>作者：</font>** Cheng Fan, Han Wu, Tingzhang Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have significantly advanced instruction-driven perception through the "Embedding-as-Mask" paradigm. However, extending this capability to Remote Sensing (RS) reasoning segmentation remains exceptionally challenging under cluttered geographical contexts and extreme scale variations, often leading to Spatial Fidelity Degradation and Target Misidentification. We identify a critical yet underexplored bottleneck: the sequential alienation of the segmentation token [SEG] from its initial visual grounding within the autoregressive generation paradigm. Produced only at the end of long reasoning chains, [SEG] relies on visual evidence that has been progressively diluted by linguistic abstraction and autoregressive noise. This information decay is particularly catastrophic for RS targets with minuscule pixel footprints, where even marginal fidelity loss leads to localization failure. To address these bottlenecks, we propose GeoReason, a novel framework designed to fortify logical deduction and preserve spatial integrity. First, we introduce an Anticipatory Prior mechanism that injects the [SEG] token directly into the initial user query, shifting it from a terminal output to a primary condition. This paradigm shift transforms the token into a persistent spatial anchor, preventing information decay during long-form linguistic inference. Second, we enhance visual reasoning via a Location-aware Chain-of-Thought (CoT) that enforces coarse-to-fine localization using bounding boxes, coupled with a Latent Patch-to-Token Alignment (PTA) Loss that explicitly aligns the latent segmentation token with physical RS textures. Extensive experiments demonstrate that GeoReason consistently outperforms state-of-the-art methods on the Earthreason and RRSIS-D benchmarks. Code is available at this https URL.

---


### 195. [mmPencil: Toward Writing-Style-Independent In-Air Handwriting Recognition via mmWave Radar and Large Vision-Language Model](https://arxiv.org/abs/2610.23419)

**<font color=#1a73e8>作者：</font>** Yifan Guo, Zhu Wang, Qian Qin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In-air handwriting recognition based on radio frequency (RF) signals offers a promising solution for human-computer interaction, yet existing methods are often limited by predefined writing planes, constrained writing styles, and small recognition vocabularies. To address these limitations, we propose m^2VLMs, a modality mapping architecture that bridges millimeter-wave (mmWave) radar sensing and large vision-language models (VLMs), and develop mmPencil, a 3D in-air handwriting word recognition system. mmPencil reconstructs 3D handwriting trajectories from mmWave signals using a multi-stage spatial trajectory reconstruction algorithm and maps them into visual representations through a spatial-to-visual mapping algorithm, enabling VLMs to recognize handwriting while reducing sensitivity to writing styles and environmental factors.
We collect and release a 3D mmWave handwriting dataset containing 7,664 samples of 200 words from 12 users across 22 writing scenarios. Extensive experiments demonstrate that mmPencil achieves robust word recognition under variations in writing position, range, angle, speed, size, direction, and user movement. It achieves 97.60% accuracy on 200 word classes for seen users and 92.50% zero-shot accuracy on 50 word classes for unseen users, outperforming state-of-the-art baselines.

---


### 196. [Generative Policy Improvement from Observational Data](https://arxiv.org/abs/2610.23436)

**<font color=#1a73e8>作者：</font>** Jonas Schweisthal, Dennis Frauen, Stefan Feuerriegel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how to improve decision policies from observational data to generate better actions when actions are complex, structured objects, such as text messages or images. This task is subject to two major challenges: (i) action-level overlap is often too weak for reliable off-policy evaluation and improvement, and (ii) generating new structured actions often requires expensive training or fine-tuning (e.g., of an LLM) and can be ill-defined due to information loss in action representations. To address both, we propose PolicyLift, a three-stage framework for generative policy improvement with structured actions from observational data. In Stage 1, PolicyLift learns a small set of discrete action codes that capture high-level strategies in the observed action space and are tailored to support policy improvement under limited overlap. In Stage 2, it learns a context-dependent policy over these action codes. At deployment time, Stage 3 "lifts" the learned code-level policy back to the original action space by generating actions from the historical behavior system in a code-conditioned way. We show theoretically that improving the policy over action codes guarantees improvement of the induced policy in the original action space. We demonstrate PolicyLift across experiments in synthetic and real-world text generation tasks with consistent policy improvements over the behavior policy.

---


### 197. [ScoutRoute: Efficient Mixture-of-Experts Routing Using Internal Language Model Signals](https://arxiv.org/abs/2610.23443)

**<font color=#1a73e8>作者：</font>** Rajdeep Pandhare, Delzaan Bharucha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient expert routing is a fundamental challenge in Mixture-of-Experts (MoE) systems, particularly for heterogeneous collections of independently trained Large Language Mod els (LLMs). Existing routing approaches typically rely on jointly trained gating networks, prompt-based predictors, or computationally expensive multi-model inference, limiting their flexibility and efficiency. This paper presents ScoutRoute, a lightweight post-hoc routing framework that predicts expert competence using internal language model signals extracted from a single forward pass through an inexpensive scout model. Hidden-state representations are used to estimate cross-model competence through lightweight logistic probes, while logit-derived confidence measures are incorporated within a domain-aware routing strategy for efficient expert selec tion without modifying the underlying language models. ScoutRoute isevaluatedon fiveopen-weightlanguagemodels across fourbenchmark datasets covering mathematical reasoning, code generation, commonsense reasoning, and multidis ciplinary knowledge. Experimental results show that ScoutRoute consistently outperforms individual routing signals while requiring only a single scout-model inference. The proposed competence probes also achieve superior calibration compared with conventional confidence measures, demonstrating that internal language model representations provide transferable information for accurate and efficient expert routing across heterogeneous language models

---


### 198. [GatewayBench: Unified Capability and Security Evaluation Platform for MCP Gateways](https://arxiv.org/abs/2610.23449)

**<font color=#1a73e8>作者：</font>** Yitian Zheng, Zhaorun Chen, Haoyu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents have increasingly interacted with external environments by invoking tools, with Model Context Protocol (MCP) emerging as a standard interface for connecting agents to heterogeneous tools and services. As organizations deploy agents at scale, MCP gateways have become a critical middleware layer for aggregating, governing, and shaping the tool surface exposed to agents. Despite the growing importance of MCP gateways in agentic systems, no prior work has systematically studied how gateway design affects agent capability, efficiency, and security. To address this gap, we introduce GatewayBench, the first unified evaluation framework and benchmark for MCP gateways. We characterize gateway architectures into two major paradigms: flattened gateways and hierarchical gateways. GatewayBench comprises 524 tasks across six domains, together with a pool of 11,118 real-world tools from 251 authentic MCP servers. To emulate large-scale deployments, we systematically inject task-irrelevant tools sampled from this pool into each agent environment, enabling controlled evaluation as the accessible tool surface scales. Based on GatewayBench, we conduct extensive experiments across seven widely deployed MCP gateways and diverse agent configurations, covering both benign and adversarial tasks. Our results reveal substantial differences across gateway designs in task completion, tool-use efficiency, and resilience to attacks, and further demonstrate that these effects interact strongly with the underlying model and agent harness. These findings highlight the MCP gateway as a consequential yet underexplored component of the agentic AI stack. By enabling controlled evaluation of gateway architectures under realistic tool ecosystems, GatewayBench provides both practical guidance for MCP gateway design and a rigorous testbed for developing more capable, efficient, and secure agentic systems.

---


### 199. [HydraLLM: Adaptive Width Slicing for Elastic Text and Vision-Language Models](https://arxiv.org/abs/2610.23455)

**<font color=#1a73e8>作者：</font>** Oscar Kemme, Janek Haberer, Ali Hojjat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs and LVLMs are increasingly deployed across heterogeneous hardware, ranging from data-center GPUs to resource-constrained edge devices. Their fixed-size architectures limit the ability to reuse a single model across deployment settings with different compute, latency, and model-size targets. We introduce HydraLLM, an elastic MQA-based architecture. Its number of active attention heads determines the effective widths of the embeddings, attention projections, feed-forward layers, and the output head, forming a nested family of subnetworks within a single parameter set. We introduce a static-to-elastic conversion pipeline that, starting from a pre-trained model checkpoint, includes importance-driven weight reordering and stochastic subnetwork training with knowledge distillation. We extend this principle to multimodal inference through an elastic projection module whose output width follows the active text width. HydraLLM covers a wider range of active parameter configurations than FFN-only elastic architectures. With 75% of heads active, HydraLLM achieves 2.2 percentage points higher TriviaQA accuracy than a state-of-the-art nested baseline configuration which has 17.25% more parameters. With 50% of heads active, our multimodal model achieves a CLIPScore comparable to that of the 7$\times$ larger Gemma 3 4B model. With only 25% of heads active, HydraLLM increases token-generation throughput by 75.3% over the full-width configuration.

---


### 200. [S-GAP: Stealthy Graph Attack Primitives for Graph Large Language Models](https://arxiv.org/abs/2610.23465)

**<font color=#1a73e8>作者：</font>** Wenda Li, Tongya Zheng, Shunyu Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Large Language Models (GraphLLMs) enable powerful semantic understanding and reasoning over Text-Attributed Graphs (TAGs), while their semantic reasoning may exhibit vulnerabilities to perturbations in node text and graph structure under adversarial attack evaluation. Existing attacks typically construct textual and structural perturbations in separate stages guided by distinct realization intents. However, this separation results in attack-intent fragmentation, causing semantic incoherence between the two perturbation types, thereby undermining attack stealth and making them easier for GraphLLMs to identify and disregard, ultimately weakening attack effectiveness. To avoid attack-intent fragmentation, we propose the Graph Attack Primitive (GAP), an atomic semantic representation that unifies textual and structural perturbations under a coherent attack intent. By carefully calibrating the semantic composition of a GAP, we can achieve strong attack effectiveness while maintaining sufficient attack stealth. Furthermore, we introduce S-GAP (Stealthy GAP), a multi-agent framework that iteratively refines the semantic content of the GAP. The framework unifies GAP planning and realization and continuously refines this process through surrogate evaluation and textual feedback. Extensive experiments across four datasets, three GraphLLMs, and two attack settings show that S-GAP improves ASR over the strongest baselines by 7.02% on average while producing more relationally plausible perturbations, exposing critical vulnerabilities in current GraphLLMs and motivating more robust defenses.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-258](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
