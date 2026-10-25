# 🧠 大模型相关研究 | 2026年10月26日

> 本类共 **241** 篇论文：已确认 **225** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-241**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-241**

---

### 201. [Jev-DLC: Decision-Level Continual Learning from Typed Feedback](https://arxiv.org/abs/2610.31521)

**<font color=#1a73e8>作者：</font>** Yangyang Feng, Jianle Gan, Zhuoyan Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Individual preferences often become visible only after deployment, when a user accepts one decision or revokes it in favor of another. Jev-style typed interfaces make this feedback explicit by identifying the selected action and, under revocation, the decision it replaces. We study how these consequences persist across requests as Decision-Level Continual Learning from Typed Feedback (Jev-DLC). Jev-DLC treats each correction as both evidence about a recurring action identity and a directed relation between the preferred and rejected choices. It preserves these signals in complementary bounded channels above a frozen scorer and combines their scores to shape the next decision. The method retains no raw interaction history, adds no scorer call, and performs no runtime language-model backward pass. We also introduce TCPA-Bench, a chronological suite that credits a correction only through its effect on later decisions. On TCPA-Repeat, Jev-DLC reaches 44.83% user-macro accuracy overall, 2.43 points above Recent-4 history replay. After at least two earlier feedback events, it reaches 56.07%, a 7.54-point margin over the strongest reported comparison at this depth. These results show how explicit typed corrections can become compact causal state for continual personalization.

---


### 202. [An Empirical Study of Recent Large Language Models for Knowledge Graph to Text Generation on Standard Benchmarks](https://arxiv.org/abs/2610.31529)

**<font color=#1a73e8>作者：</font>** Priyanka, Renaud Delbru, Souhail Bakkali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph-to-text (KG-to-text) generation verbalizes a set of knowledge graph triples into fluent natural language. While fine-tuned encoder-decoder models have long been the standard approach, recent LLMs are becoming increasingly competitive. We benchmark recent LLMs against fine-tuned encoder-decoder models, using reference-based metrics and graph-grounded reference-free LLM-based evaluation validated against human annotations. We observed that recent LLMs substantially narrow, and in several settings close, the gap with fine-tuned models on reference-based metrics, while performing better on graph-grounded metrics. LLM-based evaluation scores show limited correlation with reference-based metrics, suggesting that the two approaches capture different aspects of generation quality. Graph-grounded evaluation reveals that prompted models produce fewer contradictions and triple omissions than fine-tuned models, and these errors increase more rapidly with graph size for fine-tuned models, highlighting differences between the two approaches that reference-based metrics may not fully capture.

---


### 203. [Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.31544)

**<font color=#1a73e8>作者：</font>** Zeropy Surio, Tobias Engel, Mei-Lin Chou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning rewards a complete episode, yet the policy needs credit for every decision inside it. Counterfactual branching estimates this credit by re-running the episode after an alternative decision, but the branch draws its sampling noise independently of the factual episode, so the outcome difference mixes the effect of the decision with the luck of everything that follows. We observe that in agentic search the retriever, the corpus, and the grader are deterministic, so an episode is a deterministic function of the policy's decisions and its sampling noise. Twin worlds are therefore realizable: the same noise, a different decision. We introduce TWICE (TWIn-world Credit Estimation), which keys the Gumbel noise of every token by turn and line, rolls out counterfactual twins that inherit the factual episode's downstream noise, and turns their paired outcome differences into turn-level advantages for policy-gradient updates on actor-sampled trajectories; only the actor is deployed. Twin credit is unbiased for any coupling quality, its variance is that of an independent counterfactual scaled by $1-\rho$, where $\rho$ is the twins' outcome correlation, and under coupling the number of rollouts needed to resolve an advantage of size $\Delta$ falls from $\Theta(\Delta^{-2})$ to $\Theta(\Delta^{-1})$. A square-root rule spends the twin budget where outcomes are predicted to disagree per unit cost. On seven question-answering benchmarks, TWICE improves the average exact match of GRPO by 5.3 and 4.5 points on Qwen2.5-3B and 7B, outperforms tree-search and counterfactual-branching baselines, and uses 68% fewer auxiliary tokens than VinePPO.

---


### 204. [Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems](https://arxiv.org/abs/2610.31553)

**<font color=#1a73e8>作者：</font>** Humza Akhtar, Brian Freeman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications, and inspection reports. Governance programs often manage these sources separately. Classifying, linking, and documenting them depends on a small group of employees with deep domain knowledge. Agents built on large language models can propose metadata, cite documents, and flag quality issues, but unreviewed proposals can spread errors into downstream systems. A perfunctory approval leaves no record of what a reviewer checked. We present contestable governance: specialist agents produce scored, cited arguments for disputed metadata decisions; a steward can accept, reject, modify, or add arguments before commit; and a governance record retains the evidence, interventions, and outcome. A versioned domain glossary supplies model-specific terms and acronym definitions to the agents. We describe the workflow, a triage path that reserves full argumentation for uncertain proposals while preserving review before commit, the scoring and record models, and a gate that controls which verified decisions become precedent. Two HVAC use cases illustrate the pattern: point classification using Brick Schema class labels, supported by an open reference implementation, and an illustrative warranty failure-mode decision linking claim fields and telemetry to service notes and revisioned bulletins.

---


### 205. [Diffusion Language Models for Perplexity-Aware Black-Box Attacks](https://arxiv.org/abs/2610.31558)

**<font color=#1a73e8>作者：</font>** Ali Al-Lawati, Elsayed Eshra, Dongwon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> \emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned from language, its prompts can be highly unnatural, and as such easily detectable through input guardrails, and the risk estimates they yield are not grounded in natural prompts. In this paper, we demonstrate that the same continuous latent-space framework can be coupled directly to a learned generative distribution over language, a continuous diffusion language model (dLLM), which removes the artificial random mapping while preserving the standard-Gaussian latent formulation and the downstream sampling or optimization procedure. We evaluate this approach under two settings: sampling-based estimation using \emph{RareTrap} and optimization-based search using \emph{ThinkTrap}. We find that character-level perplexity drops from $10^3$--$10^7$ to 3--5 in RareTrap and from 20--28 to 4.3--5.4 in ThinkTrap. We also find that model risk estimates can differ by an order of magnitude across the two mappings.

---


### 206. [When to Follow the Teacher: Advantage-Based On-Policy Distillation](https://arxiv.org/abs/2610.31563)

**<font color=#1a73e8>作者：</font>** Mahdi Sabbaghi, George Pappas, Hamed Hassani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online Policy Distillation (OPD) often outperforms offline methods such as Supervised Fine-Tuning (SFT) by training on trajectories sampled directly from the student. However, standard OPD trains the student to follow the teacher at every state of the trajectory, assuming that teacher guidance is always beneficial. We instead distinguish between what the teacher prefers and what actually helps the current student succeed. We introduce Advantage-Based On-Policy Distillation (AOPD), which weights teacher actions by their counterfactual advantage under the student. Teacher actions that improve the student's expected outcome are reinforced, while those that do not are downweighted.
Directly computing these advantages requires trying alternative teacher actions at each step and running new rollouts from each. Instead, we show that the AOPD objective can be estimated using only standard student rollouts and their terminal rewards. Our estimator uses teacher importance weights on the student-sampled actions to provide unbiased advantage-weighted supervision, without any additional rollouts or reward evaluations. This allows AOPD to focus teacher supervision on actions that help the current student while preserving the rollout efficiency of standard OPD. Experiments on math, coding, and Medqa show gains over distillation and RL baselines in both external-teacher and self-distillation settings.

---


### 207. [CellTrack-Bench: Microscopic Cell Tracking Benchmark for Vision-Language Models](https://arxiv.org/abs/2610.31566)

**<font color=#1a73e8>作者：</font>** Ilan Theodoro, Jordão Bragantini, Loïc A. Royer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models have shown outstanding performance on text-first tasks such as coding, math, and writing. Recent efforts are shifting models' training to include scientific problems that often live in highly specialized domains beyond text, such as protein structure and biological images. However, in these scenarios, their general-purpose accuracy compared with specialized algorithms remains in question. One such domain is cell tracking, which requires spatiotemporal awareness of cell dynamics. To evaluate this, we created a new benchmark, CellTrack-Bench, which assesses Vision-Language Models' (VLMs) cell-tracking-related performance against specialized trackers. The full benchmark draws from 15 standard cell-tracking datasets across four imaging modalities and comprises 1,537 problems corresponding to 9,041 cell-linking decisions. We selected a hard subset requiring greater reasoning effort by identifying failures shared across distinct algorithmic trackers. With this proposed dataset, we: (i) evaluated different environment harnesses for VLMs; (ii) benchmarked 9 frontier closed-source models and 13 open-weight models; and (iii) provided a detailed analysis of their failure modes. Code, the stored model outputs, and a pipeline that regenerates the benchmark from the source datasets are available at this https URL.

---


### 208. [On the Token Collapse Phenomenon in Textual Graph Soft Prompting](https://arxiv.org/abs/2610.31572)

**<font color=#1a73e8>作者：</font>** Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent methods for injecting graph structure into LLM prompts include graph soft prompting, in which a graph neural network (GNN) learns graph-specific tokens that capture relational information among entities in textual prompts. G-Retriever combines graph soft prompts with a verbalized description of the same graph to strengthen the textual prompt signal. We conduct an in-depth analysis of G-Retriever and uncover a pathological behavior we term token collapse. Across three benchmarks, three graph encoders, two LLM families, and both frozen and LoRA-adapted models, G-Retriever's graph tokens become almost indistinguishable across inputs. We provide evidence that the same failure is inherited by subsequent methods, even with multi-token pooling. Under the standard setup, swapping a token with the dataset mean, a token from another example, or one derived from a corrupted graph produces no resolved answer-level effect in accuracy. Moreover, a learned constant prompt that never accesses the graph matches or surpasses G-Retriever on all three benchmarks. These findings indicate that, rather than conveying graph content as intended, the collapsed token functions primarily as a generic soft prompt. We also examine conditions linked to this collapse and propose a two-stage procedure that yields non-collapsed tokens while maintaining competitive performance in most cases. However, token variability alone does not prove that the model uses graph information: via interventions and decoding probes, we show that depending on the configuration, a token can reflect the question, an answer prior, or graph-derived content that the LLM may or may not use. Overall, our results offer a practical approach to evaluating graph-token alignment rather than inferring it from task accuracy alone. Code to reproduce our experiments is available at this https URL.

---


### 209. [Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure](https://arxiv.org/abs/2610.31573)

**<font color=#1a73e8>作者：</font>** Pellegrino Casoria, Simon Pietro Romano  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it. As these practices become routine, exposure to social engineering attacks becomes an operational certainty, demanding a shared framework for assessment and mitigation.
We make this exposure measurable by quantifying how accurately a target can be profiled, and how far that profile enables social engineering attacks. Because no existing model fully spans this continuum, we unify Social Media Intelligence (SOCMINT) and Cyber Human Intelligence (Cyber-HUMINT), two individual-focused disciplines that evolved separately, into a single doctrine-grounded taxonomy of 38 capabilities across the Cyber Threat Intelligence lifecycle, where user profiling bridges passive collection and active engagement. Domain experts validated the taxonomy (Fleiss' $\kappa$ = 0.92).
We operationalize its core path (extraction, inference, and susceptibility assessment) as an LLM-augmented multi-agent pipeline, evaluated on real participants' public data. Susceptibility is assessed indirectly: the pipeline predicts how each target would rank personalized engagement options, matching their actual choices significantly above chance. This ranking capacity captures the personalization on which tailored attacks depend. The underlying profiles are accurate: extraction reaches F1 = 97.3%, and inferred attributes score 4.73/5, both far above rule-based and NER-based baselines at negligible cost. The framework augments security analysts' tradecraft rather than replacing it and enables defenders to gauge their own exposure before an adversary does.

---


### 210. [Rethinking Sequence Compression with Test-time Regression](https://arxiv.org/abs/2610.31574)

**<font color=#1a73e8>作者：</font>** Sihan Yang, Jie Huang, Hanxuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequence compression is a fundamental operation and a critical information bottleneck in efficient language and multimodal models, and yet prevailing approaches based on pooling or learned projections remain underperforming. We revisit sequence compression through the lens of test-time regression: input tokens define a regression problem whose fitted coefficients form the compressed representation. Importantly, the regression problem is learned end-to-end via backpropagation, while its coefficients are computed efficiently in closed form during the forward pass. This leads to TTR-Compressor, a general alternative to conventional pooling and projection-based compression. We evaluate TTR-Compressor as the compressor for block-wise sparse attention and the visual token merger for multimodal large language models. On block-wise sparse attention, TTR-Compressor improves RULER performance over attention-based compressors by a large margin. For visual token merging, it consistently outperforms the standard MLP merger and matches its performance with 55.6% fewer visual tokens. These results establish test-time regression as an effective primitive for sequence compression in efficient language and multimodal models.

---


### 211. [What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models](https://arxiv.org/abs/2610.31576)

**<font color=#1a73e8>作者：</font>** Jinya Sakurai, Xun Xu, Jaehong Yoon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models generate tokens in parallel, but their efficiency depends on which predictions are committed. Learned unmasking policies improve the speed--accuracy trade-off, yet differ in supervision, inputs, and capacity, obscuring which choices matter. We view supervised policies as distilling a decoding procedure through a teacher and examine independently what the teacher labels as committable, on which states the policy imitates it, what the policy observes, and how much the number of function evaluations (NFE) must decrease to offset policy overhead. We find that labeling predictions matching the final output is overly permissive at low NFE, and hidden states are weak alone but can complement confidence. About a 10% NFE reduction suffices to offset policy overhead for policies up to 7.5M parameters across tested settings. We therefore train a policy on trajectory-contraction targets, which accept only commitments staying on a reference trajectory, using confidence and hidden states. On LLaDA-8B-Instruct, the resulting 856K-parameter policy achieves the best accuracy--NFE frontier and highest throughput on GSM8K, is competitive at moderate targets on MATH-500 and HumanEval, and largely transfers to Dream-7B-Instruct.

---


### 212. [Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration](https://arxiv.org/abs/2610.31579)

**<font color=#1a73e8>作者：</font>** Deepthika S, Pawni Yadav, B. Sankar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend towards it? In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five assistants built on the same model (GPT-5-mini). Unknown to participants, each assistant's briefing had 0, 25, 50, 75, or 100% of its facts replaced by plausible falsehoods, and every assistant spoke with full confidence. A surprise quiz after each topic offered the correct fact, the planted falsehood, and two distractors, with a confidence rating for every answer. Across 104 quizzes and 1,040 answers, scores fell from 7.4 to 2.9 out of 10, and the planted option was chosen on 60% of falsified items against 11% of correctly taught ones (odds ratio 12.5). Transcript coding showed that whenever the assistant stated a falsehood, it was adopted about 65% of the time at every falsification level. Absorbed falsehoods were held with high confidence (8.4/10), the modeled confidence advantage of right over wrong answers vanished, and the discrimination of confidence for correctness fell from an AUROC of 0.70 to chance, while post-task trust ratings barely moved. Participants tended to return to the chat more when the assistant was worse, but returning went with more absorption, not less, and 30% of all turns pasted quiz questions back to the source being checked. The assistant itself was almost never sycophantic and never conceded under pushback. We introduce a baseline-corrected Human Deference Index to quantify this human-side sycophancy and argue that trustworthiness is a property of the human-AI pair, that sycophancy evaluations should measure both directions, and that learning interfaces must make reliability legible claim by claim.

---


### 213. [Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination](https://arxiv.org/abs/2610.31586)

**<font color=#1a73e8>作者：</font>** Miguel Fernandez-de-Retana, Unai Zulaika, Ruben Sanchez-Corcuera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accuracy on medical examinations is common evidence offered for the clinical use of language models, yet a health system that intends to run an open model on its own hardware needs to know considerably more: whether the model recognizes when it is likely to be wrong, whether medical fine-tuning improves this ability, whether its correct answers rest on sound clinical reasoning, or whether it actually uses the images it is given. We examine these questions for four open models of 8 to 27 billion parameters on the Spanish MIR residency examination, scoring 1,552 questions from eight editions under the exam's own rules. Answering every question, the three larger models would rank among roughly the first 600 to 3,000 candidates, with 41 to 43 specialties still open to them. Abstention, however, never pays, because even their least confident answers are right more often than the 25% break-even. Medical fine-tuning reduced overconfidence at the cost of accuracy, without improving how well confidence separates right from wrong answers. Moreover, 13-38% of correct answers rejected a distractor for a clinically unsound reason that confidence did not reflect, and removing or swapping the provided contextual images left accuracy unchanged.

---


### 214. [Simulated Control Evals](https://arxiv.org/abs/2610.31593)

**<font color=#1a73e8>作者：</font>** Jeffrey Olmo, David Zhang, Tyler Tracy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Control evaluations measure whether safeguards can prevent an AI model from causing undesired outcomes even when it is intentionally trying to do so. These evaluations typically use purpose-built control settings and extrapolate their results to a model's deployment. However, the effectiveness of safeguards in deployment can depend on features of environments and tasks that control settings do not represent. To broaden where control evaluations can be run, we introduce simulated control evaluations (SCEs), which use a language model to simulate tool responses in place of an environment. We evaluate SCEs on LinuxArena, where execution provides ground-truth outcomes. We compare SCE prediction errors with those from a separate control setting, BashArena, and with variation in control metrics within LinuxArena. For independently sampled evaluation and deployment task sets, SCEs predict safety with a root mean squared error of 3.6 percentage points across five monitors at a 5% audit budget, compared with 10.1 for BashArena. SCEs closely reproduce distributions of attack strategies, attacker reasoning, and monitor reasoning, with over tenfold lower KL divergence from execution than BashArena. SCEs explain 78-85% of the between-environment variance in attack success, monitor scores, and safety. This accuracy is sample efficient: SCEs predict safety with less error than BashArena using fewer than 5% as many task-pair draws as the deployment task set. Strategies discovered through simulation also improve monitor performance on held-out LinuxArena attacks, outperforming BashArena and approximately matching improvement from executed strategies. These results suggest that deployment-specific SCEs can be more predictive than control evaluations executed in separate control settings.

---


### 215. [How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions](https://arxiv.org/abs/2610.31606)

**<font color=#1a73e8>作者：</font>** Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an 18-query development benchmark, with one Yes/No or WH-question per document, were used. Retrieval combined dense embeddings, BM25, and cross-encoder reranking. Chunk sizes of 128 to 1024 tokens, overlaps of 0 to 20%, and four retriever configurations were evaluated. Relevance was defined by evidence spans mapped to all containing chunks, treating overlapping chunks with equivalent evidence as relevant. Retrieval was evaluated using R-Precision, Recall@K, MRR, and nDCG@K. Separately, generation was assessed on a 512-token index at K=1 to 5 using DeepEval claim-level metrics, with deepseek-v4-pro as the LLM judge, and BLEU/ROUGE metrics. Results: The selected hybrid retriever, using 384-token chunks and 20% overlap, retrieved accepted evidence in the top three results for 17 of 18 queries. Recall@3, R-Precision, MRR@3, and nDCG@3 each reached 0.94. Ground-truth curation increased evidence spans from 25 to 37 and accepted chunk targets from 36 to 51 without changing retrieval rankings. Conclusion: Cross-encoder reranking achieved the highest retrieval scores. Expanded relevance annotations increased recognized evidence without changing rankings, highlighting annotation sensitivity. The small development set and retrieval-informed curation require independent validation, including radiologist assessment of evidence sufficiency.

---


### 216. [Bilingual Language Models Capture Cross-Linguistic Influence in Second-Language Reading](https://arxiv.org/abs/2610.31620)

**<font color=#1a73e8>作者：</font>** Abderrahmane Issam, Irene E. Winther, Stefan L. Frank  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While monolingual language model (LM) surprisal is widely established as a predictor of reading times, it cannot capture the non-native (L2) reading dynamics that are shaped by the reader's first language (L1). In this work, we investigate whether the cross-lingual transfer within bilingual models aligns with human L1-driven biases during L2 reading. We evaluate bilingual models on eye-tracking data of readers from 12 diverse L1 backgrounds reading English texts. To isolate L1-specific transfer, we compare bilingual models trained on an L1 that matches the readers' L1 background to both a monolingual English baseline and bilingual models trained on other L1s. We demonstrate that matching the readers' L1 improves the prediction of L2 reading times. This predictive advantage is concentrated in late-stage eye-tracking measures, modulated by L1-L2 script overlap, and peaks among intermediate-proficiency readers. These findings provide evidence that bilingual LMs capture aspects of cross-linguistic influence, and that such influence is present in L2 reading behavior.

---


### 217. [Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3](https://arxiv.org/abs/2610.31624)

**<font color=#1a73e8>作者：</font>** Barış Alparslan, Sandy Tanwisuth, Caleb Petterson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforcement learning with verifiable rewards (RLVR) make a model more likely to express instrumental-convergence behavior, or does this depend on the training regime, evaluation frame, and stage of post-training? We study this question as a checkpoint-conditioned behavioral trajectory rather than as a single before/after safety score. Using InstrumentalEval, we evaluate OLMo-3-7B-Think across SFT, DPO, 13 intermediate RLVR checkpoints, and the final RLVR model. The trajectory is nonmonotonic: instrumental rate rises from 25.0% at SFT to 46.1% near RLVR step 200, then falls to 11.8% at the final checkpoint. Paired item-level tests and step-wise regression support the final SFT-to-RLVR reduction. Prompt framing does not explain this pattern: a harmful-prompt indicator combined with other framing effects explains only 15% of within-checkpoint score variance on average, and Iterative Null-space Projection (INLP) removes a detectable framing direction without changing the SFT-to-final-RLVR gap. Together with preliminary 32B endpoint results (35.53% SFT to 22.37% RLVR final), these findings indicate that RLVR does not monotonically increase instrumental behavior in this setting: the rate rises early, then falls below the SFT baseline. The result is specific to this model family and benchmark, and judge agreement is moderate, so absolute rates should be read cautiously.

---


### 218. [Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2](https://arxiv.org/abs/2610.31636)

**<font color=#1a73e8>作者：</font>** Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, budgeted API and compiles each finding into an executable test, which a native speaker then validates. On the 26.5M-document Slovak portion of FineWeb2, three runs costing \$2.21-\$2.84 each found seven findings over four phenomena. The largest is a machine-generated content farm of 1,408,437 documents (5.32%) that passed the pipeline's filters, 86.6% of it passing even stricter thresholds. Blinded labels support 6 of the 7 findings (defect rates .53-1.00 against .08 in a random control) and do not support one. The compiled suite scans the full corpus in 0.7 s of wall-clock time without a GPU, against \$12k-\$90k per LLM classification pass. The best static sampling baseline validates more selectors than any agent run, at under half the cost. The agent contributes exact prevalence, a precision estimate checked against sampled documents, an account of why the pipeline missed each slice, and a reusable test. We release the framework, Slovak test suite, validation data and agent trajectories.

---


### 219. [Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation](https://arxiv.org/abs/2610.31639)

**<font color=#1a73e8>作者：</font>** Gabriele Dominici, Teague McMillan, Fazl Barez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregressive generation, dense attention allows each reasoning step to attend to the full context, enabling the model to derive answers through direct lookup while generating plausible-sounding but post-hoc justifications. We introduce CausalCoT, an inference framework that enforces causal transparency by decomposing problems into a directed acyclic graph of atomic sub-questions, evaluating each node in an isolated context containing only its direct causal parents. This Markovian structure removes attention pathways to non-parent content, making downstream predictions sensitive to local reasoning rather than global context leakage. Across a diverse suite of reasoning benchmarks, CausalCoT preserves competitive predictive performance while improving explanation faithfulness, increasing causal sensitivity of intermediate reasoning steps by an average of 12 and up to 21 percentage points over the strongest baseline. The structured dependency graph additionally enables test-time interventions in which local corrections propagate predictably through downstream reasoning.

---


### 220. [Low-Bit N-Gram Embeddings for Language Models](https://arxiv.org/abs/2610.31646)

**<font color=#1a73e8>作者：</font>** Stephen Chung, Wenyu Du  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many recent open-weight language models use n-gram embedding tables to improve performance. These tables store learned representations of short token sequences, such as pairs or triples of consecutive tokens, which the model retrieves during processing. However, they can require substantial memory: DeepSeek-V4.1-Flash, for example, allocates 196 billion parameters to its Engram n-gram memory. We therefore investigate whether this memory cost can be reduced while preserving the performance improvement that the tables provide. We propose storing n-gram embeddings at low precision and systematically investigate different quantization methods and bit allocations across tables. Across nanochat-, Llama-, and GPT-2-family models trained from scratch, four-bit tables save approximately 75% of table memory while preserving more than 99% of the validation-loss improvement from adding the tables. Using fewer bits leads to a larger drop in performance, although we find that a short fine-tuning phase recovers a significant part of this loss. In addition, reinvesting the saved memory in larger tables can improve performance beyond that of the original full-precision tables while still using less memory. These table memory savings also extend to large existing models: on DeepSeek-V4.1-Flash and Qwen3.8-Flash-Next, low-bit tables save 47-55% of table memory, with perplexity increases of less than 1.2% and largely preserved downstream task performance. These findings establish low-bit precision as a practical way to reduce the memory requirements of n-gram embeddings and use the saved capacity to improve model performance.

---


### 221. [Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation](https://arxiv.org/abs/2610.31649)

**<font color=#1a73e8>作者：</font>** Xiaolin Li, Zihao Huang, Fanpeng Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image 3D generation has achieved high fidelity on curated benchmarks, yet degrades sharply on real-world images with uneven illumination, blur, and occlusions. Purifying such inputs requires deciding when to intervene and preserving the visual cues needed for 3D generation, while leaving clean inputs unchanged. We introduce Gate3DGen, a selective pre-processing model that gates image inputs to existing 3D generators without retraining them. A degradation-aware router bypasses inputs classified as clean and extracts features to guide purification of the remaining inputs. Conditioned on these features, a 3D-oriented one-step purifier purifies degraded inputs with spatial losses that encourage preservation of object identity, contours, and textural cues. To provide paired supervision, we construct a synthetic data engine that renders clean views of 3D assets and synthesises composite degradations. On the synthetic benchmark, the purifier improves image fidelity and downstream 3D geometry in only 2.3s on average, reducing TRELLIS.2 mesh distance by 61.5% relative to degraded inputs. VLM evaluation and human preferences on real photographs further support identity preservation and degradation correction. More demos and code are available at this https URL.

---


### 222. [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650)

**<font color=#1a73e8>作者：</font>** Qijin Zhang, Hanzhen Wang, Yuehan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. By systematically suppressing critical facts, the benchmark measures unsafe execution under critical evidence omission and determines the minimum observed failure cardinality, including failures with full evidence and cases with no observed failure after exhaustive testing. An independent audit tool tests whether agents seek missing facts and then withhold prohibited actions while completing permissible tasks. The benchmark reveals substantial variation across the ten models in omission robustness, evidence acquisition, and appropriate action. Resistance to missing evidence does not necessarily translate into useful recovery. Recovery access reduces unsafe execution for all ten models, but agents differ in whether they actively obtain the missing facts and use them to act appropriately in both worlds.

---


### 223. [BrickWright: Agentic Creation of Physically Feasible Brick Builds](https://arxiv.org/abs/2610.31651)

**<font color=#1a73e8>作者：</font>** Ava Pun, Kevin Dai, Sally Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frontier coding agents are becoming increasingly adept at 3D modeling. Yet, they still face challenges when building objects meant to be assembled in the physical world, often creating invalid assemblies with floating, colliding, or disconnected parts. We argue that providing agents with tools for assembling builds and verifying their physical feasibility is sufficient for them to produce physically valid assemblies that still adhere to input prompts. Focusing on the domain of LEGO brick builds, we present BrickWright, a framework for generating physically feasible brick builds from text or image prompts using pre-trained agents, where a build is physically feasible if it uses only real parts, has no colliding or floating parts, and forms a connected structure if possible. BrickWright guides agents to create builds by writing code with BrickLayer, a Python toolkit with two main components: an ergonomic brick assembly API that halves inference cost compared to working in raw LDraw, and a validator that provides feedback on physical feasibility. Whereas baseline agents achieve physical validity rates ranging from only 9% (GPT-6 Luna) to 69% (GPT-6 Astra), BrickWright-guided agents achieve 100% validity on a sample of 512 prompts, while improving prompt adherence for lightweight agents and maintaining it for stronger agents. Additionally, they outperform specialized models on the text-to-brick task. Code is available on our project page: this https URL

---


### 224. [Cost-Aware Abstention for LLM-Based IT Ticket Classification](https://arxiv.org/abs/2610.31657)

**<font color=#1a73e8>作者：</font>** Sachin Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_triage, c_wrong) = (0, 1, 5), TF-IDF with logistic regression and a threshold of 0.60 selected on calibration reduces test cost from 0.763 to 0.472, a 38.1% relative reduction (paired ratio-bootstrap 95% CI [35.7%, 40.4%]), while lowering wrong routes from 15.3% to 3.5%. Frozen calibration-selected policies also beat both always-route and always-defer on held-out test data in 14 of 16 settings in a post-hoc cost-parameter analysis. The strongest prompted configuration reaches 0.477 accuracy on a stratified 1,000-ticket test subset, versus 0.879 for fine-tuned DistilBERT on the same tickets. Isotonic lowers expected calibration error without reliably improving discrimination: GPT-4o-mini few-shot has one confidence value before and after recalibration and correctness AUROC 0.500. We therefore report correctness AUROC and tie-aware risk-coverage area alongside ECE. At the analytically derived break-even probability 0.80, seven prompted configurations defer all tickets; Haiku few-shot routes only 19/1,000. An LLM-only agreement control and margin/entropy rejection baselines further separate calibration from discrimination. The findings are scoped to this dataset, prompt design, model endpoints, and illustrative costs; the work is an evaluation framework, not a new abstention algorithm or universal deployment certification.

---


### 225. [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670)

**<font color=#1a73e8>作者：</font>** Yunfei Xie, Howard H. Qian, Shiyi Lan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the structure of physical motion? To examine this, we propose Sensorimotor Alignment ($S^2$), a training-free offline metric that measures how well a model's sensory representation aligns with the geometry of physical motion. We find that $S^2$ correlates positively with downstream robot task success across embodied model families, making it a low-cost offline proxy for prioritizing models before closed-loop evaluation. $S^2$ can also identify promising vision-language model (VLM) backbones even before costly fine-tuning into vision-language-action models (VLAs). Beyond this correlation, $S^2$ offers representation-level explanations for phenomena observed in VLAs and world action models (WAMs). With $S^2$, we extend PRH to embodied models and make sensorimotor alignment empirically measurable, offering insight into why an embodied model succeeds beyond its closed-loop success rate.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 226. [Protection Is Not One Event: A Survey of RAG Protection Research by Measured Endpoint](https://arxiv.org/abs/2610.30193)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Peiyang Liu, Xi Wang, Di Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems face security, privacy, and copyright risks including content leakage, source reconstruction, unauthorized access, data poisoning, and prompt injection. Yet RAG protection studies use incompatible evaluation metrics, datasets, and threat models. We present a systematic survey and human-coded evidence map of 118 full-text-confirmed RAG defense papers, organized by measured endpoint rather than claimed goal or defense mechanism. Our seven-family taxonomy covers content disclosure, formal privacy proxies, access control and suppression, corpus-use detection, and pipeline integrity and attribution. Thirty-two annotators double-coded the papers kappa=0.867. The survey identifies three gaps. First, retrieval reranking and context rewriting each span five or six endpoint families, so mechanisms do not identify protection outcomes. Second, only 17.8% of studies use content disclosure or reconstruction as their primary endpoint; under the frozen copyright/ownership relation label, 73.3% of records have corpus-use detection as their primary endpoint, and none have an emitted-expression primary endpoint. Third, most evaluations use general-purpose question-answering datasets and non-adaptive attacks rather than sensitive data and adaptive, multi-turn extraction. Our controlled RAG testbed shows that preventing verbatim copying does not prevent private-fact recovery: a normalized 8-gram guard reduces 20-token copying to 0.0%, but a three-query adaptive attacker recovers 48.3% of hidden facts on Qwen3-8B. We release the taxonomy, dataset, coding protocols, and testbed to enable comparable, claim-aligned RAG security evaluation.

---


### 227. [Diagnosing Personalization Failures in Mobile GUI Agents](https://arxiv.org/abs/2610.30573)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhixin Lin, Dongliang Xu, Jungang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unlike conventional GUI agents, personalized GUI agents require user preferences to guide sequential execution over changing GUI states. This raises two challenges: determining HOW each preference should alter execution strategy and WHEN it should take effect along the interaction trajectory. Existing benchmarks primarily evaluate overall task success, offering limited insight into these questions. We introduce PrefDiag-Bench with two components: (1) a categorization of preferences into five types, characterizing HOW they affect execution; and (2) a stage-wise diagnostic framework with 1,664 probes, tracing WHEN preferences should take effect and where failures occur. We evaluate eleven GUI agent systems, including end-to-end agents and agentic workflows, under two forms of user context: explicit user profiles and behavioral memory logs. Although existing agents achieve relatively high completion rates on non-personalized tasks, performance is substantially lower on preference-personalized tasks. Even the best-performing model, Seed-2.0-Pro, achieves only 47.17% on Process preferences under explicit user profiles. Agents struggle particularly with Ranking and Process preferences. Further analysis reveals two key capability bottlenecks: selecting relevant evidence from user history and recognizing when preferences should take effect during execution. Controlled interventions that explicitly provide relevant evidence improve end-to-end task success by up to 7.06%. PrefDiag-Bench offers a more systematic evaluation of GUI agents' personalization capabilities beyond overall task success. Code and data are available at this https URL.

---


### 228. [Anticipating Social Consequences with Distributional World Models](https://arxiv.org/abs/2610.30657)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Viet-Thanh Pham, Thuy-Trang Vu, Zhuang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social world models predict how interactions develop after an action, helping agents negotiate, cooperate and mediate. In these situations, one action can lead to several plausible futures, hence predicting only one future can overlook consequential alternatives, while exploring them through repeated simulations increases inference cost. We propose DSWM, a Distributional Social World Model that predicts alternative responses, their probabilities and immediate and final outcome values in one output per candidate action. We train a 4B model on repeated simulations using supervised fine-tuning and GRPO. At inference time, the actor uses these possible consequences to choose an action. Across three seen and two unseen environments, with interaction backbones absent from training collection, DSWM achieves the best average performance on 13 of 15 metrics. Ablations show that retaining multiple futures and their predicted probabilities improves outcomes in all five environments.

---


### 229. [UniGuard: Multi-View Guardrail Learning for Cross-Interface Safety Generalization](https://arxiv.org/abs/2610.30742)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Viet-Thanh Pham, Thuy-Trang Vu, Junae Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Guardrail models are increasingly used as safety layers for LLMs and agentic systems, but most are trained on fixed prompt or response interfaces and become unreliable when the same safety case appears as a conversation, agent trajectory, multi-agent trace, or policy-conditioned input. We propose UniGuard, a training framework that learns interface-invariant safety representations from multiple semantically aligned views of the same safety case. We also construct the UniGuard-FT dataset by transforming 1,000 public safety cases into prompt, response, multi-turn conversation, agent-trace, and multi-agent-trace views, and train UniGuard-0.6B with classification, supervised contrastive learning, and asymmetric confidence calibration losses. Across unseen-interface benchmarks ATBench, PolicyGuardBench, and DynaBench, UniGuard-0.6B improves over its pretrained guardrail by 45.12 F1 points on average and reduces expected calibration error by 35.41 points, while remaining competitive with much larger guardrails such as Claude-Sonnet-4.5 and GPT-5.2 - despite being a 0.6B model and trained only with synthetic data.

---


### 230. [Random Remasking Scales Masked Diffusion Inference](https://arxiv.org/abs/2610.30744)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhaoyi Zhou, Frank Wu, Andrea Zanette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) generate sequences by progressively unmasking tokens, but errors introduced during decoding are typically irreversible. Recent work has shown that iterative correction can improve sample quality, yet existing theory fails to explain this given a learned, imperfect denoiser model. We re-formulate MDM inference as a Markov chain on the clean sequence space, defined by a remask-denoise kernel that randomly re-introduces masks and then denoises. This helps us analyze the actual denoising trajectory towards the data distribution. The analysis motivates Random Remask-Denoise (R$^2$D) inference, a purely test-time, finetuning-free, reward-free procedure. To further improve performance, we propose Trajectory Correction Training (TCT), a denoiser-training procedure that exposes the model to its own errors along the generation trajectory. On logical tasks, our approach exhibits a striking near-log-linear test-time scaling, achieving over 97% accuracy on hard Sudoku puzzles and over 99% accuracy on 3-SAT. Our approach also applies to pretrained models on actual language tasks, beating iterative correction baselines and the official Q-mode accuracy of LLaDA2.1-mini on HumanEval+.

---


### 231. [Synthetic-to-Real Code-Switched ASR: A Spontaneous Nepali-English Podcast Benchmark](https://arxiv.org/abs/2610.30860)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Firoj Paudel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nepali-English code-switched conversational speech presents severe challenges for automatic speech recognition (ASR), chiefly through script confusion (inappropriate mixing of Devanagari and Latin orthography) and elevated error rates at language switch points. Supervised fine-tuning (SFT) can adapt multilingual foundation models, but human code-switched audio is expensive to collect and annotate. We curate a new benchmark of 13,044 spontaneous podcast utterances (15.45 h total; 10,214 test, 2,830 dev), audited and verified to eliminate machine translation leakages and acoustic loops. We investigate a two-stage synthetic-to-real adaptation framework: Stage 1 applies SFT on 0.95 h of speech synthesized via a multi-speaker, dual-engine TTS pipeline; Stage 2 explores Group Relative Policy Optimization (GRPO) with transcription and script rewards. We find that synthetic SFT provides the primary cross-domain transfer to spontaneous human speech, reducing Mixed Error Rate (MER) from 23.40% to 21.52% (-1.88 pp) and switch-point error rate (SPER) from 35.89% to 28.77% (-7.12 pp). Subsequent GRPO yields small, statistically significant adjustments on 173 test utterances (1.69%), driving English script confusion (SCR_en) from 6.45% to 6.36% (p <= 0.001) and SPER to 28.70% (p = 0.022 clustered). Crucially, ablation reveals that in this SFT-converged encoder-decoder setting, an auxiliary script reward term yields performance identical to MER-only optimization because rollout candidate groups exhibit near-zero script variance on synthetic data. On monolingual benchmarks, SFT improves Nepali MER by 2.71 pp (stabilizing at 18.42% after GRPO, a 2.38 pp gain over baseline) while preserving English lexical WER (3.38% vs. 3.33%). Verified transcripts, timestamps, episode metadata, and reconstruction scripts are publicly released.

---


### 232. [MOER: Mix-Policy Optimization under Expert Prefix Guidance with Selective Rollback](https://arxiv.org/abs/2610.30873)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuyang Zhong, Jiuding Yang, Yiwen Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mix-policy optimization incorporates off-policy expert data into the reinforcement learning (RL) loop to transcend the capability boundary of on-policy RL. However, existing methods either provide static full-trace guidance that suppresses self-exploration, or adopt expert prefix guidance without correctness guarantees, leading to suboptimal performance or even training collapse. In this paper, we propose MOER, a mix-policy optimization framework that harmonizes expert guidance with self-exploration. MOER injects a decaying expert chain-of-thought prefix into the prompt and lets the model complete the remaining reasoning, with the prefix length progressively annealed to encourage self-exploration. A selective rollback mechanism replaces failed completions with the original full expert trace, guaranteeing the correctness of every off-policy trajectory. Furthermore, a harmonized mix-policy objective optimizes on-policy tokens with a GRPO loss while supervising both expert prefix and completion tokens with a trust-region SFT loss, substantially stabilizing training. Extensive experiments show that MOER achieves the highest average scores in mathematical and general domain reasoning tasks, outperforming all basic and mix-policy baselines, and generalizes consistently across diverse tasks, model scales, and base model categories. Codes are available at this https URL.

---


### 233. [Random Initialization as a Baseline for Time Series Foundation Models](https://arxiv.org/abs/2610.30950)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pinar Sungu Isiacik, Georgiana Ifrim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) use self-supervised pretraining to learn reusable representations for downstream tasks such as multivariate time series classification (MTSC). We examine how much pretrained weights contribute beyond the architecture itself by comparing seven publicly released instances from four TSFM families with architecture-matched randomly initialized counterparts on the UEA MTSC archive. For each instance, five random initializations are evaluated using four classifiers on frozen representations: ridge classification, logistic regression, RBF SVM, and random forest. After model-specific exclusions due to computational constraints, the study comprises 183 paired dataset-level comparisons. Pretraining improves mean accuracy for all seven instances, but the gains are modest, ranging from 1.43 to 5.19 percentage points, with an overall average improvement of 2.58 points. Three of seven per-instance Wilcoxon signed-rank tests have raw $p$-values below 0.05, but only NuTime remains significant after Holm correction. A secondary pooled test across all 183 pairs gives $p < 0.001$, while the corrected per-instance tests remain the primary evidence. We also compare with ROCKET, Hydra, and Quant, which remain competitive without requiring large-scale pretraining. These findings suggest that MTSC evaluations should distinguish the effect of pretrained weights from that of the underlying architecture and should include both architecture-matched random initialization and strong non-pretrained baselines.

---


### 234. [Zero-Shot Forecasting of In-Situ Soil Moisture and Temperature with a Time-Series Foundation Model](https://arxiv.org/abs/2610.30971)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mohammad Talaei, Mohammad Goudarzi, Maille Todd 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Soil moisture and temperature govern plant-water availability and microbial activity, making them key indicators for evaluating land-restoration efforts on degraded landscapes. However, the physical and data-driven models normally used to forecast them both need information that a newly instrumented restoration site does not yet have: hydraulic parameters for the former and months of per-site training data for the latter. We evaluate TimesFM 1, a 500M-parameter time-series foundation model, zero-shot on 15-minute telemetry from 27 sensor stations across three land-management regimes (Control, Treatment, Scald) at a semi-arid restoration site, forecasting 5 cm and 30 cm soil moisture and enclosure temperature at seven lead times from 1 h to 168 h. Using gap-aware rolling-origin evaluation across sensors, we find that TimesFM beats the best rule-based statistical forecasting baselines (persistence, seasonal-naive, or 7-day climatology) by 21-76% at sub-daily lead times but loses by 6-79% beyond a day, a pattern explained by a diurnal-alignment mechanism that holds for both soil-moisture depths and temperature. A CatBoost baseline trained walk-forward on the same origins with full history and weather covariates never wins overall, and we show that its weakness is partly a cold-start effect specific to short deployments. We additionally quantify the inference cost of zero-shot forecasting on commodity CPU hardware. Our results highlight a practical trade-off between zero-shot forecasting capability, predictive performance, and computational efficiency.

---


### 235. [Transformers with CoT Discover Heavy-Ball Acceleration Through Training](https://arxiv.org/abs/2610.31089)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxuan Cai, Yuan Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern transformers often solve complex tasks by generating and refining intermediate reasoning steps. To develop a theoretical understanding of chain-of-thought (CoT) reasoning, a notable recent study by Huang et al. (2025) viewed transformers as algorithm executors, and showed that when transformers' CoT steps are supervised by a gradient-descent teacher, they can learn to implement gradient descent for in-context weight prediction in linear regression. In this paper, we study the same in-context weight prediction task but ask whether CoT reasoning can go beyond merely imitating the teacher algorithm. We show that, after initial supervision from a gradient-descent teacher, further trajectory-level supervision using the true regression weights leads the model to implement the Heavy-Ball method, thereby achieving acceleration over the original teacher. Notably, this accelerated algorithm emerges without supervision from any Heavy-Ball teacher. Our results provide a concrete theoretical example in which transformer reasoning can discover new algorithms through training, rather than merely imitate the algorithm used for supervision.

---


### 236. [MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model](https://arxiv.org/abs/2610.31321)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinyang Lu, Shengzhe Wei, Sheng Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Local feature matching is typically formulated for image pairs, although structure-from-motion and visual localization commonly match one reference image against many retrieved or covisible neighbours. Applying a pairwise matcher independently to these centre-neighbour edges duplicates reference-side computation and prevents the matcher from exploiting complementary multi-view geometric evidence from the remaining observations. To address these limitations, we introduce MVLoMa, a sparse star-graph matcher that extends LoMa from image pairs to multiple views. MVLoMa first uses a frozen multi-view geometry model to jointly describe all images in a star, then injects the resulting cross-view geometric context into local descriptors. It then matches the centre image to all neighbours in a single forward pass through per-view self-attention and bidirectional centre-neighbour cross-attention. For supervision, we derive positive correspondences only from depth-valid, mutually visible dense warps and explicitly penalize high-confidence matches that violate epipolar geometry. On 25-view star graphs from HyperSim, ScanNet++, Mip-NeRF 360, and Tanks and Temples, MVLoMa obtains the best macro-average relative-pose AUC among the compared methods at all three thresholds (58.65/85.41/90.99). Its matcher is 2.20 times faster than sequential evaluation of the 24 centre-neighbour edges. The same design supports four tested frozen geometry encoders -- DA3, $\pi^3$, VGGT, and VGGT-$\Omega$ -- with DA3-Giant performing best on all reported encoder-ablation metrics. Controlled ablations further isolate the effects of geometry-aware descriptors, visibility filtering, geometric negative supervision, and joint multi-view inference.

---


### 237. [HERD: Harness-Evolving Recursive Distillation for Continual Learning](https://arxiv.org/abs/2610.31401)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual learning requires a model to keep acquiring new skills and knowledge without compromising its existing capabilities. Parametric methods suffer from catastrophic forgetting and loss of plasticity. Non-parametric methods, such as prompts, skills, and harnesses, leverage in-context learning but are limited by context length and lossy plain-text compression. To effectively combine their complementary strengths, we propose HERD (Harness-Evolving Recursive Distillation), a hybrid continual learning framework that learns efficiently in the harness and internalizes experience into cumulative capabilities via distillation. On the harness side, HERD continually refines its skills to capture reusable patterns, while retaining high-residual examples that the skills fail to capture in a bounded memory. On the parameter side, HERD performs drift-constrained distillation with dual anchors, substantially reducing forgetting over long recursive runs. On the 25-stage task stream of TRACE+17, under fixed memory and compute budgets, HERD matches the strongest parametric baseline in new-task acquisition while exhibiting the least forgetting and the strongest retention of general capabilities.

---


### 238. [OP-Print: Tracing Membership Imprints in On-Policy Self-Distillation](https://arxiv.org/abs/2610.31616)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qi Li, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation has been widely adopted for alleviating the distribution mismatch of off-policy distillation. Self-distillation further removes the need for an external teacher by using the student's own outputs, enhanced with extra context or demonstrations, as supervision. This teacher-free design makes on-policy self-distillation practical, yet its privacy risks remain largely unexplored. In particular, using two coupled views of the same training example may strengthen its memorization. Motivated by this, we present the first study of membership inference attacks against on-policy self-distillation. We investigate both gray-box and black-box threat models and propose a unified attack framework, named OP-Print. OP-Print builds on our finding that the supervision imprint in on-policy self-distillation is sparse and structured, concentrating on uncertainty-sensitive correction sites rather than across the entire rollout. Exploiting this property, we construct attack signals tailored to the two access levels: in the gray-box setting, OP-Print directly aggregates the privileged teacher-student residual correction along the same rollout; in the black-box setting, it measures restart-based output-basin stability as an observable surrogate for the hidden correction process. Across diverse models and distillation schemes, all baseline attacks remain essentially at random guessing even under gray-box access, whereas OP-Print is broadly validated to be effective in both gray-box and black-box settings.

---


### 239. [F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation](https://arxiv.org/abs/2610.31623)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jinyu Zhang, Haitao Lin, Jiashu Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies category-level RGB-D object pose estimation, which recovers an object's 3D rotation and translation without instance-specific CAD models or reference views. This task is highly ambiguous due to intra-class variations, symmetries, and partial observations. Current solutions struggle to balance reliability and efficiency: methods based on intermediate structures are prone to error propagation, while diffusion models suffer from high inference latency and complex post-hoc candidate extraction. To address this, we present F2G-Pose, a real-time direct, single-pass framework that predicts category-level pose, metric size, and camera-frame completed shape from a single RGB-D observation in one feed-forward pass. F2G-Pose lifts dense visual foundation features to partial point clouds, encodes local geometry with DGCNN tokenization, and integrates object-level structure with a Mixture-of-Experts Transformer. Joint size prediction and camera-frame shape completion encourage metric consistency through dense geometric supervision. With its task-specific network trained only on pose-annotated synthetic SOPE data and its frozen RADIO backbone externally pretrained, F2G-Pose achieves state-of-the-art accuracy on SOPE and ROPE while running at 28 FPS for pose-only inference, and further demonstrates strong camera-frame geometry on HouseCat6D and real-object transfer on HANDAL. Analyses of latency, robustness, shape completion, and GenPose++ candidate behavior further demonstrate the efficiency and reliability of F2G-Pose, with real-world manipulation experiments demonstrating deployment potential under segmented RGB-D inputs. The project page, code, and pretrained models are made available at this https URL.

---


### 240. [BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing](https://arxiv.org/abs/2610.31633)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hayden Prairie, Jacob M. Ryan, Taylor Berg-Kirkpatrick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped architectures scale quality while keeping parameter count fixed by repeatedly passing activations through the same block of layers. During inference, each recurrence generates independent KV-caches, causing memory to grow linearly. To address this challenge, prior work has proposed KV-sharing (i.e., sharing KV-caches across depth), finding that, in some cases, the KV-cache of the final recurrence can be shared with the earlier recurrences without quality loss, a property we denote as KV-shareability. However, the mechanisms underlying KV-shareability remain poorly understood, with even identically trained looped architectures not consistently exhibiting it. In this paper, we study how KV-shareability can be enabled in looped models. We propose a two-stage method: in the first stage, we use stochastic depth during pretraining, which induces contractive residual dynamics that drive representations toward a common limit across recurrences. In the second stage, we propose BeNice!, a post-training method that broadcasts the final recurrence's KV-cache into the first recurrence, training it to produce compatible residuals while preserving the original model's quality. As a result, BeNice! enables KV-shareability while matching standard finetuning's unshared validation perplexity. Using BeNice!, we show that KV-sharing is complementary to alternative KV-compression methods, composing with memory-efficient sequence mixers (e.g., multi-latent attention, Kimi delta attention) and low-precision KV-cache quantization (e.g., fp8, mxfp8, nvfp4). Finally, in simulated low-memory, long-context inference, KV-sharing improves cache hit rates by up to 31.4%, increases throughput by up to 23.6%, and reduces p90 time-to-first-token by up to 83.6%.

---


### 241. [Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](https://arxiv.org/abs/2610.31667)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mahdi Salmani, Adel Javanmard, Devansh Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool after generating only a short prefix, committing further computation only to the surviving candidates. Existing pruning strategies divide broadly into two categories: Quality-based methods assign a score to each partial solution and discard those predicted to ultimately lead to an incorrect final solution, while diversity-based methods select partial solutions that follow different reasoning trajectories and are therefore likely to cover different final solutions. The tension between these two objectives is an instance of exploration versus exploitation, yet little to no prior work on pruning exposes this trade-off directly, let alone optimizes it. In this paper, we introduce a pruning procedure that addresses this trade-off directly by optimizing pass@$k$ over the selected solution pool. In particular, it chooses the pool to maximize the probability that at least one of its partial solutions, when continued to completion, yields a correct answer. Because this objective simultaneously rewards high-quality partial solutions and penalizes redundancy among them, quality and diversity are naturally balanced by the criterion itself rather than through separate ad-hoc design choices. On eight open-weight reasoning models, our method outperforms existing quality-based and diversity-based pruning strategies. The gains are particularly pronounced when the pruning procedure keeps a moderate number of partial solutions for continued generation, highlighting the value of directly balancing quality and diversity during pruning.

---


> [!TIP]
> 当前位于：**201-241**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-241**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
