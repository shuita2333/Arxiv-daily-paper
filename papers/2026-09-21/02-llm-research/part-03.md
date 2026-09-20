# 🧠 大模型相关研究 | 2026年09月21日

> 本类共 **176** 篇论文：已确认 **162** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-176](./part-04.md)

---

### 101. [EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning](https://arxiv.org/abs/2609.20004)

**<font color=#1a73e8>作者：</font>** Nikita Khomich, Leopold Hermansson, Ido Hakimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-based reinforcement learning for language models, exemplified by Group Relative Policy Optimization (GRPO), collapses an entire stochastic trajectory into a single scalar reward. This is clean and scalable, but it explores and allocates reward inefficiently: a trajectory may contain many causal decisions, recovery attempts, and environment-randomness events, yet every token or action inherits one trajectory-level advantage. We study tree-based rollout construction as a compute-allocation problem for policy-gradient estimation. Our central claim is that branches should be placed not where the policy is merely uncertain, but where an additional branch most reduces uncertainty about the policy gradient per unit of compute. From a law-of-total-variance decomposition of the local policy-gradient random variable, we derive two allocation laws: new branches reduce decision uncertainty, while repeated suffix rollouts reduce continuation uncertainty. The resulting EPIG-Tree score allocates branches using the already computed rollouts. It estimates occupancy- and score-weighted value uncertainty, along with a suffix law $n_e \propto w_e \|\nabla_\theta \log \pi(a_e|h_e)\| \sigma_e / \sqrt{c_e}$. Empirically, EPIG reduces gradient MSE in cloned-state control, winning in all nine dense continuous-control environments of a 13-environment sweep and recovering the reference gradient direction near-perfectly, and it improves frozen-LLM gradient calibration relative to entropy branching. In online single-turn math, tree-local credit beats flat GRPO, while branch placement is secondary to token-level credit assignment. In online multi-turn Wordle, EPIG attains the highest final win rate (0.850), overtaking flat GRPO, which saturates early at 0.790, and entropy branching as training proceeds, confirming that the gradient-estimation advantage transfers to a stateful, large-action setting.

---


### 102. [Geopolitical Divisions Across Languages in Large Language Models](https://arxiv.org/abs/2609.20005)

**<font color=#1a73e8>作者：</font>** Maxim Chupilkin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People increasingly turn to AI chatbots for news and explanations of world events. But do they receive the same political answers when they ask in different languages? Here we show that the language of a question can change how the same AI systems assess the war in Ukraine. We ask GPT, Claude and Gemini to evaluate twenty statements about the war in 112 languages, collecting 67,200 responses. The balance between Russia-leaning and Ukraine-leaning responses differs across languages. When we group responses by countries' official languages, they follow a pattern resembling worldwide political divisions: relatively more Russia-leaning answers correspond to more favourable public views of Russia, less support for Ukraine in United Nations votes, and less aid to Ukraine. The broad pattern recurs across all three models and remains when individual statement pairs are removed. Our findings suggest a possible route through which information warfare may shape the text used to train AI models, which may in turn spread geopolitical biases.

---


### 103. [Can Data Attribution Filter Out Subliminal Learning? Not Reliably](https://arxiv.org/abs/2609.20027)

**<font color=#1a73e8>作者：</font>** Moritz Weckbecker, Sweta Jena, Jonas Müller 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Subliminal learning allows language models to transmit behavioral traits through training data with no obvious semantic relationship to those traits, undermining content-based data filtering as a safety intervention. Training data attribution offers an alternative: it identifies the training examples responsible for a given model behavior, independent of their semantic content, and so may apply in exactly the cases where semantic inspection fails. We evaluate three gradient-based attribution methods (GradCos, a contrastive GradCos variant, and EK-FAC) across three models, comparing them against divergence tokens, a strong baseline previously shown to localize subliminal learning (albeit one that requires access to counterfactual teacher models). Filtering at the token level, EK-FAC mitigates a significant part of the effect, the other methods provide little benefit, and all mostly fall short of divergence tokens. Filtering entire samples is less effective for every method, though EK-FAC often gives a stronger signal than divergence tokens in this setting. Success is inconsistent across methods and settings: variants that work well for some model-preference combinations fail for others, and we do not identify a consistent explanation for these differences. Our results suggest that gradient-based attribution can identify data responsible for subliminal learning in some settings, but that some approximations are more reliable than others.

---


### 104. [Correct Now, Insufficient Later: Auditing Update Sufficiency in Context Compression](https://arxiv.org/abs/2609.20045)

**<font color=#1a73e8>作者：</font>** Guangzhe Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A memory can answer a current query correctly while discarding distinctions required by a later update. We investigate this failure with a paired-history audit: two histories have the same current answer, receive a shared future update, and require different subsequent answers. A pilot evaluates 24 history pairs across six synthetic mechanisms, 12 memory conditions, two repeats, and two model backends. A deterministic frontier selector obtains strict reveal accuracy of 96/96 on DeepSeek and 82/96 on GLM; a structured writer obtains 62 successes with one unresolved outcome and 56/96. The configured four-outcome joint contrast has finite-sample identification intervals of [0.521, 0.542] and [0.292, 0.313], not confidence intervals. A record-level audit distinguishes retained-state adequacy, response delivery, and answer-schema compliance without changing those original scores. It finds 26 and 25 well-formed but semantically wrong structured reveal memories, while all 14 GLM frontier reveal failures contain correct values in the wrong wrapper. Tombstone removal produces 16/16 exact replay failures in the targeted mechanism. Identifier renaming then exposes a separate flaw: original frontier late-reference adequacy falls from 8/8 to 94/320 transformed instances. We provide and test a label-equivariant repair, but it preserves only 2/8 original late-reference answers: eliminating a naming shortcut does not solve unknown future relevance. These results support a scoped evaluation methodology and reproducible failure analysis, not general superiority of the repaired algorithm. Paid pilot evidence, retrospective diagnostics, and new offline tests are reported separately; no independent held-out or natural-task validation is claimed.

---


### 105. [What People Almost Did: Evaluating LLM Social Simulations Beyond Behavioral Fit](https://arxiv.org/abs/2609.20055)

**<font color=#1a73e8>作者：</font>** JaeWon Kim, Angie Boggust  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-based social simulations are primarily evaluated for behavioral fit, testing whether agents reproduce the actions or response distributions of the people they are simulating. However, the promise of simulation extends beyond behavioral fit. Simulations can explain human behavior, diagnose barriers, and compare large-scale interventions. These use cases depend on understanding \textit{why} people acted a certain way, not just \textit{what} they did. As a result, behavioral fit is insufficient for these types of claims because behavior underdetermines the reasoning process behind it. For instance, the behavior of staying silent may be due to disinterest or suppressed speech, and not answering a call may be due to distrust of the caller or limited phone access. In this paper, we propose \textit{representational adequacy} as a new evaluation target for LLM-based social simulations. By leveraging LLM reasoning traces, representational adequacy measures whether a simulation's scenario--reasoning--action triples preserve the reasoning process behind the behavior in a way that is faithful to the population and scenarios being simulated. We distinguish representational adequacy from interpretability and alignment metrics, propose ways to integrate it into simulation research, and pose its measurement as an open problem.

---


### 106. [WiCleanData: Guaranteeing the Type Consistency of Wikidata by Taxonomy Refinement and Constraint Enforcement](https://arxiv.org/abs/2609.20057)

**<font color=#1a73e8>作者：</font>** Yiwen Peng, Marc Jeanmougin, Thomas Bonald  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Because of its collaborative nature, Wikidata suffers from errors, in- consistencies, and excessive complexity, such as redundant classes, ambiguity between instances and classes, wrong taxonomic paths, and type constraint violations. The manual curation of these issues is infeasible at scale. To address these challenges, we introduce WiCleanData, a refined version of Wikidata with a consistent tax- onomy and free from type constraint violations. Specifically, we have designed an automated pipeline that first cleans the taxonomy with language model assistance, then simplifies type constraints by hierarchical aggregation, and finally filters facts accordingly. The resulting knowledge graph, free from any type violation, is made publicly available via a Web interface, enabling easy exploration and downstream applications.

---


### 107. [A Free Lunch? Adapting PP-OCRv6 for Historical Text Recognition](https://arxiv.org/abs/2609.20064)

**<font color=#1a73e8>作者：</font>** Benjamin Kiessling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite impressive reported scores, large vision-language models have seen limited practical uptake in historical automatic text recognition because of their computational cost, dependence on large-scale pretraining, and hallucination. Historical ATR therefore continues to rely largely on compact CRNN line recognizers, which are visually grounded and trainable on modest data. Lightweight recurrence-free recognizers promise the accuracy of larger models with the practical advantages of CRNNs, yet have not been comprehensively evaluated on historical writing. We adapt PP-OCRv6, a recent compact text recognizer without strong language modeling, for historical line recognition and compare it with a conventional CRNN across generalized pretraining, domain-specific training, corpus-level fine-tuning, and manuscript-specific few-shot adaptation on multilingual Latin- and Arabic-script material. While PP-OCRv6 does not consistently outperform the baseline when trained from scratch, heterogeneous pretraining produces markedly better generalization. Comparisons with the Qwen3.5-based Medusa recognizer further show that fine-tuned PP-OCRv6 can outperform a large VLM tailored towards historical Latin-script HTR.

---


### 108. [Marginal utility, matrix factorization, and the Key-Value (KV) cache: a unified information-economic framework for sovereign geo-mining inference](https://arxiv.org/abs/2609.20068)

**<font color=#1a73e8>作者：</font>** Caroline Gans Combe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper builds a theoretical bridge between the economic notion of marginal utility and two machine-learning constructs, matrix factorization and the Key--Value cache of transformer language models. The singular value spectrum of a rating matrix is shown to be a diminishing marginal utility schedule for latent factors, the eigenvalue spectrum of the projected covariance operator to be the marginal utility schedule of a model's learned representation, and cache eviction and low-rank cache compression to be instances of constrained utility maximization under a memory budget. The three collapse into a single allocation rule: retain the top dimensions whose eigenvalue exceeds the shadow price of the binding constraint. The framework is applied to the automated extraction of structured information from geo-mining documents, where it motivates a multi-pass inference protocol, a layer-wise TIES model merging procedure, and a selection policy combining extraction quality, localization drift and energy, scalarized with a Conditional Value-at-Risk term on drift. Two empirical contributions are reported. An 11.2-million-parameter hierarchical classifier, trained in about five minutes on a single GPU, reaches 90.0 per cent level-1 accuracy on a held-out test set from a 973-document uranium-exploration corpus, against 92.0 per cent for a proprietary model on a fifty-document human audit of the same corpus, at a latency of 2.62 ms per card against approximately 2,000 ms for the API and at negligible cost. A diagnostic of uniform-density TIES merging exposes a reproducible degenerate mode in which the merged model returns token-identical outputs across five geographically distinct districts while declaring high confidence; re-executing the merge under layer-wise calibrated densities removes that signature on the diagnostic sample. The full-scale extraction benchmark, including LoRA fine-tuning, is reported as projected rather than measured and remains an empirical extension of this work.

---


### 109. [Tailored to you: longitudinal effects of personalising language models](https://arxiv.org/abs/2609.20077)

**<font color=#1a73e8>作者：</font>** Canfer Akbulut, Justine Breuch, Arianna Manzini 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interest in developing personalised language models is rapidly growing. While personalisation is often viewed as a mechanism to better serve diverse user needs, the effects of sustained interactions with personalised models on people's perception of and behaviour toward AI remain poorly understood. Most critically, downstream consequences outside the immediate human--AI interaction loop, such as effects on users' self-perceptions and interpersonal relationships, remain largely unexamined. In this study, we recruited 992 participants to complete daily advice-seeking interactions with language models over the course of five days, comparing outcomes from a non-personalised baseline against two personalisation approaches: memory-based (conditioned on prior conversational history) and survey-based (conditioned on information collected through a pre-study intake survey). We find that several changes in human-AI interaction over time are driven primarily by repeated exposure rather than personalisation itself. However, participants interacting with personalised models experienced differences in advice-seeking and information-sharing attitudes and behaviours: participants in the memory-based condition engaged in greater self-disclosure and rated the model as less creepy, while participants in the survey-based condition reported higher regret about having shared personal information with the AI. We conclude by highlighting the nuanced effects of different personalisation approaches on interaction outcomes, and discussing the implications of these findings for the responsible design and deployment of personalised AI systems.

---


### 110. [Reading Emotions in the Token Space: Discriminative Adaptation of SpeechLLMs for Emotion Recognition](https://arxiv.org/abs/2609.20081)

**<font color=#1a73e8>作者：</font>** Hasindri Watawana, Sergio Burdisso, Esaú Villatoro-Tello 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SpeechLLMs have shown strong potential for emotion recognition, yet they read the predicted emotion off a generative decoder not suited for classification: it can emit labels outside the target set and favors frequent classes. We propose a discriminative adaptation that reads the final prompt token's hidden state through a classification head, producing a label in one forward pass without modifying the backbone. Because this readout starts from the hidden state the model would otherwise decode, it gives a controlled comparison of generative and discriminative inference in an otherwise identical speechLLM. We keep the head a single linear layer, trading little accuracy for interpretability: each emotion becomes one direction in the LLM output token space, revealing associated tokens. On IEMOCAP, across two speechLLM architectures, it improves Macro F1 and removes hallucinations, with largest gains on realistic ASR transcripts. Our analysis reveals that these emotion directions encode indirect associations mirroring biases in web-scale text.

---


### 111. [MATCH: Model-Aware Tool Learning with Curriculum Scheduling and Hierarchically Gated Rewards](https://arxiv.org/abs/2609.20082)

**<font color=#1a73e8>作者：</font>** Shihao Liu, Hao Yin, Lijun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool learning enables large language models (LLMs) to use external tools for tasks beyond parametric knowledge. Reinforcement learning can optimize tool-call behavior from feedback, but current methods still face two problems: fixed-threshold curricula can become misaligned with the policy's evolving capability boundary, and additive rewards can leak argument-level credit when the predicted tool is wrong. To address these problems, we propose MATCH, a closed-loop framework for model-aware tool learning with curriculum scheduling and hierarchically gated rewards. Model-Aware Curriculum Learning (MACL) maintains reward-derived sample difficulty that co-evolves with the policy, and each epoch selects samples near the current capability boundary together with a top-k pool of harder cases. Hierarchical Tool-call Gated Reward (HTGR) scores tool name, argument key, and argument value as a gated chain, granting credit at each level only when prerequisites hold. The same HTGR rewards drive both GRPO updates and MACL's difficulty refresh, closing the loop between policy optimization and sample scheduling. On API-Bank and BFCL V3, MATCH reaches 72.19% and 62.87% overall accuracy, outperforming the main supervised and RL-based baselines. Backbone experiments further show consistent improvements across four backbones from two model families.

---


### 112. [UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.20089)

**<font color=#1a73e8>作者：</font>** Wenjie Liao, Liangjie Zhao, Zehong Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving methods reduce the need for human-annotated trajectories by allowing tool-using agents to generate their own training data. Yet existing methods typically separate trajectory generation from evaluation, relying on static verifiers that cannot adapt to emerging failure modes or self-consistency signals that may reinforce errors shared across trajectories. Jointly adapting planning, execution, and evaluation offers a promising alternative, but introduces a fundamental coordination challenge: each component continuously changes the data or feedback used to train the others. We address this challenge with \textbf{UnifiedPlayers}, a cooperative framework comprising a Planning Player that generates tasks, an Execution Player that produces multi-turn trajectories with Python tool calls, and an Evaluation Player that constructs executable verifiers. We design role-specific rewards that coordinate the three players toward a shared learning objective under GRPO. Across two model backbones and twelve reasoning benchmarks, UnifiedPlayers outperforms the strongest prior baseline by at least 3.5\% on mathematical reasoning and 3.9\% on general reasoning tasks. Moreover, the learned verifier achieves 84.2\% adversarial detection accuracy, while its reward signal exhibits 2.03$\times$ higher per-question variance than a self-consistency baseline, providing more discriminative verifications. These results highlight cooperation among specialized players as a promising path toward self-enhanced tool-integrated agents.

---


### 113. [Perception, Layout, and Validation: Calibrated Confidence for Reliable Straight-Through Processing of Financial Documents](https://arxiv.org/abs/2609.20110)

**<font color=#1a73e8>作者：</font>** Yichao Jin, Yushuo Wang, Yuxuan Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Straight-through processing (STP) on extracted key-value fields from financial documents without human review requires a calibrated probability together with a bounded guarantee on the residual error of the auto-approved tier. The emergence of modern Vision Language Models (VLMs) provides an out-of-the-box capability for extracting the key-values, but their verbalized confidence signals are unreliable and weakly track field correctness. This paper introduces a decomposed confidence layer along three interpretable channels, including perception, layout, and validation. Together with a final conformal risk control, the score can be used for reliable STP of financial documents. The method is validated on three public datasets covering real invoices, synthetic invoices, and ad-buy forms, using two different VLM families (Qwen3.6-27B and Gemini-3.1-Flash-Lite). Our decomposed score consistently improves the separation of correct from incorrect extractions, substantially raising the AUROC from 0.54-0.74 for VLM verbalized signals to 0.90-0.99 with contributions from all three designed channels. Crucially for industrial deployment, this enables usable STP. The native VLM confidence signals could clear only 0.1%-7.0% of fields under risk control at a target error of <10%. In contrast, the proposed method auto-approves 49-72% of fields while holding the empirical error of the accepted tier at or below the target.

---


### 114. [Cross-Modal Attention Acts as a Frequency Filter: Why Verbose Prompts Improve Robustness in Vision-Language Models](https://arxiv.org/abs/2609.20139)

**<font color=#1a73e8>作者：</font>** Farooq Ahmad Wani, Maria Sofia Bucarelli, Mujtaba Hussain Mirza 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are fragile under image corruption. We find that the wording of the question affects VLMs in two opposite ways. Verbose questions make VLMs substantially more robust---e.g., rephrasing "Is there a cat?" into "Please look carefully and answer: is there a cat?". Conversely, VLMs become more fragile under corruption when the question is semantically complex or finer-grained, e.g., "what colour is the cup left of the chair?" instead of "is there a cup?". Both effects stem from question-conditioned cross-modal attention, which induces a spectral filter over image patches: verbose questions broaden its frequency support, while fine-grained questions concentrate it onto fewer visual scales. The model's answer drifts most when this filter and the corruption sit on the same spatial frequencies. We test the filter view on Qwen3-VL and LLaVA-OneVision across GQA and CLEVR; verbose paraphrasing reduces drift variance by 70--81% on the 8B models. The practical recipe---pad the prompt---further yields measurable gains in accuracy, even under image corruption.

---


### 115. [Designing Against Deskilling: Metacognitive Feedback Reduces Cognitive Offloading to LLM Assistants](https://arxiv.org/abs/2609.20143)

**<font color=#1a73e8>作者：</font>** Sebastian Maier, Kai Schwabe, Manuel Schneider 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cognitive offloading to AI can reduce opportunities to practice skills, creating risks of deskilling. However, it remains unclear how to prevent deskilling without restricting access to AI. Here, we design two interventions to reduce offloading decisions: (1) metacognitive feedback that makes the implications of offloading for users explicit, and (2) an effort-based reward that incentivizes less extensive LLM assistance. We test both in a preregistered online experiment ($N = 704$) with a 2$\times$2 design and a no-AI control. The task was to practice fraction arithmetic with an LLM-based assistant that provided solutions only on explicit request, followed by an unaided test. Metacognitive feedback reduced answer offloading (OR $= 0.47$) and improved test performance (OR $= 1.51$). We found no evidence that the reward affected either outcome. Our results identify metacognitive feedback as a promising design choice to reduce cognitive offloading.

---


### 116. [MTVA-Bench: Evaluating the Language Model Inside Cascaded Voice Agents](https://arxiv.org/abs/2609.20152)

**<font color=#1a73e8>作者：</font>** Pritish Mishra, Ishaan Kumar, Akshat Mandoli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generally, most voice agents are cascaded systems, i.e., an ASR model transcribes the caller's audio, a language model reads the transcript and decides what to say and which backend tools to call, and a TTS model speaks the reply. Nearly all of the decision making happens in the language model, but existing evaluations measure it either too broadly or too narrowly. End-to-end voice benchmarks score the full pipeline, so recognition errors and model errors mix into a single number. LLM benchmarks isolate the model but they do not evaluate what makes real phone calls hard, such as transcription issues, caller's voice being split across messages and the requirement that replies follow the language and script specified. We introduce the Multi-Turn Voice Agent Benchmark (MTVA-Bench), which evaluates the language model on the same conditions it faces inside a cascaded system. The caller is played by an LLM following a set of rubrics and tool calls are answered by a mock backend which responds to the arguments the model actually sent. The benchmark contains 49 agents working across 490 reviewed scenarios and supports 7 languages. Scoring is a combination of deterministic checks on tool calls with two LLM judges, one that scores scenario specific rules and one that grades conversation quality without access to the task. Both judges must cite specific messages from the transcript. Task and conversation scores are weighted equally, since a call can complete its task and still go badly for the caller. In a seven-model study, six of the models select the correct tool within 6.4 points of one another, but their overall scores span 24.4 points. Most of the gap comes from argument values, action ordering, rule compliance, and what the model says around its tool calls.

---


### 117. [Fine-Tuning Models for Biomedical Relation Extraction](https://arxiv.org/abs/2609.20169)

**<font color=#1a73e8>作者：</font>** Claudiu Creanga, Liviu P. Dinu, Daniela Gifu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Next-Generation Sequencing has revolutionized the study of genetic mutations, enabling large-scale investigations into their roles in disease development. However, extracting meaningful insights from the vast amount of biomedical literature remains a complex challenge that cannot be addressed manually. In this paper, we present pre-trained models (PTMs) for the automatic extraction of relations from biomedical text, specifically targeting the variant-phenotype domain. Our evaluation on the SNPPhenA corpus demonstrates that fine-tuning small BERT-based models, particularly DeBERTa, yields strong performance, approaching the current state-of-the-art (SOTA). Additionally, our results indicate that carefully fine-tuning Google's Gemini Pro 1.0 outperforms the existing SOTA for both sentence-level tasks (where the model processes only the target sentence) and abstract-level tasks (where the model processes the entire abstract).

---


### 118. [To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals](https://arxiv.org/abs/2609.20186)

**<font color=#1a73e8>作者：</font>** Roy Eisenstadt, Ido Cohen, Edo Cohen-Karlik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative Decoding (SD) has significantly accelerated Large Language Model (LLM) inference, yet existing approaches face a fundamental tradeoff between two drafting strategies: neural drafting and context-based copying. Neural drafts (e.g., EAGLE3) provide robust performance across diverse text settings, while copy-based methods achieve higher speedups in copy-intensive regimes by generating candidates faster and exploiting long repetition spans for near-perfect speculation. We analyze existing copy-based methods and find that they are prone to accidental repetitions where surface-level n-gram overlap does not reflect a structural intent to copy, leading to false-positive triggers that ultimately degrade throughput. We introduce SwitchSD, an adaptive framework that treats copying as a latent control signal of the LLM. By training lightweight probes on the target model's internal representations, SwitchSD identifies genuine copy-intent with high precision (AUC > 0.99). This allows the system to dynamically switch between neural drafting (e.g., EAGLE) and context-based copying. Our results across Llama and Qwen families demonstrate throughput gains of up to 15% over state-of-the-art baselines like EAGLE3, effectively turning copying from a noisy heuristic into a principled, model-aware decoding regime.

---


### 119. [Evaluating Financial Sentiment in the Age of AI](https://arxiv.org/abs/2609.20198)

**<font color=#1a73e8>作者：</font>** Arslan Bisharat, Oudom Hean  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial sentiment measures are widely used in empirical finance, but it remains unclear whether general-purpose large language models (LLMs) improve on existing finance-specific methods. This paper evaluates twelve sentiment models, including dictionary-based methods, finance-specific transformers, and open-source LLMs, using two criteria: linguistic validity and economic validity. We find that general-purpose LLMs achieve classification performance comparable to finance-specific transformer models without task-specific fine-tuning. However, higher classification accuracy does not translate into stronger economic relationships. Several models produce sentiment measures that are significantly associated with earnings surprises, but none is significantly associated with next-day stock returns. Model performance is strongest for announcements with large earnings beats or misses and substantially weaker for announcements with more moderate earnings surprises. These findings suggest that financial sentiment captures information about firms' economic performance but has limited ability to explain short-run market reactions

---


### 120. [Foundations of Stochastic Lexical Calculus: Semantic Descent and Random Dynamics on Probability Simplices](https://arxiv.org/abs/2609.20207)

**<font color=#1a73e8>作者：</font>** Matthew F Dixon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models produce prompt-dependent probabilities over words, whereas scientific systems require uncertainty over meaningful states that can be updated as evidence arrives. We develop an observable framework for determining when language-derived probabilities support such a sequential state representation. Theoretically, we define typed measurable transformations of contextual language, construct a minimal closed representation, and give necessary and sufficient conditions for semantic updates to exist uniquely. We bound irreducible nonclosure and accumulated error, and under average contraction prove existence, uniqueness and stability of an external random recursion on a probability simplex. These results define a stochastic lexical calculus without attributing an internal calculus to the language model. Empirically, frozen experiments test the observable implications. Raw prompt-conditioned probabilities fail the prespecified invariance gate; after prompt-specific calibration, a common three-state representation passes the stability gates and covers 28 of 30 untouched eight-step paths, or 0.933 at nominal level 0.90. Accordingly, language probabilities support a stochastic state only conditionally on verified closure, stability and coverage within a declared operating domain.

---


### 121. [Silence Is Endorsement: Verification-Status Laundering in LLM Agent Pipelines](https://arxiv.org/abs/2609.20211)

**<font color=#1a73e8>作者：</font>** Yibo Hu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety monitors in LLM agent systems often judge actions from summaries or stored handoffs, not from the original evidence. This creates a simple but dangerous failure mode: the handoff preserves the claim that an action is authorized while losing the fact that the claim was never verified. We call this verification-status laundering. Across nine open-weight monitors and two hosted models, the action and authorization proposition remain fixed while we remove the unverified provenance framing around the claim. This change raises approval for risky actions from $5\%$ to $60\%$ on Llama-3.1-8B and from $9\%$ to $98\%$ on Qwen2.5-14B, with similarly large shifts on both hosted models. The failure also emerges in ordinary agent pipelines. Summarizers frequently weaken the status, memory compressors often remove it, and a full proposer--summarizer--memory--monitor pipeline raises risky approval to $57$--$81\%$ across three downstream monitors. Experiments on WildGuard and ATBench show the same pattern on independently authored harmful and unsafe requests: unsupported authorization claims make approval substantially more likely. Explicitly instructing monitors to reject unverified authorization is not a reliable cross-model fix: some models remain vulnerable, while others reject legitimate requests. Agent systems should therefore carry authorization provenance as structured state attached to the claim throughout the pipeline.

---


### 122. [Is It Still Worth Training a Classical Model in the Era of LLMs? A Crossover Benchmark on Tabular Data](https://arxiv.org/abs/2609.20218)

**<font color=#1a73e8>作者：</font>** Kaihua Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can label a tabular row from a plain-English description with no training - a capability now shipping in mainstream spreadsheet tools such as Microsoft Copilot in Excel and Anthropic's Claude for Excel - raising a practical question for the many business prediction problems where labels are expensive: should you prompt a frozen LLM, or collect data and train a model - and if so, how much data? We quantify the answer with the labeled-data crossover N*, the training-set size at which a trained classical model's learning curve overtakes a frozen LLM's training-free (and therefore flat) error. Aggregating 126 independent student evaluations of small GPT models under eight prompting configurations across 18 tabular datasets, paired with authoritative power-law learning curves for six classical model families, we find that training wins fast: even given an oracle choice of its best prompt configuration, a trained classical model beats the small frozen LLM using no more labeled data than is already on hand in 86% of cases, and wins by the smallest labeled subset we evaluate in 40%, with the observed crossover at a median of ~6% of the training set. In-context few-shot examples do not behave like training - error versus shot count does not follow a power law - and the same protocol re-run by independent implementers varies with a coefficient of variation of 0.148. A controlled probe indicates the LLM depends on recognizable feature-name semantics, which plausibly makes our crossover a conservative estimate (we do not claim memorization). For a typical business table, the evidence is clear: collect a few hundred labels and train a gradient-boosted model.

---


### 123. [Scene-Q: Confidence-Aware Coarse-to-Fine Querying of 3D Scenes with Selective VLM Reasoning](https://arxiv.org/abs/2609.20235)

**<font color=#1a73e8>作者：</font>** Juno Kim, Yesol Park, Hye-Jung Yoon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor mobile robots require open-vocabulary scene understanding that grounds natural-language queries in a consistent 3D map. Many existing systems ultimately rely on cosine-similarity retrieval with contrastive image--text encoders, which is efficient but brittle when labels are near-synonymous or multiple similar instances appear. We present Scene-Q, a confidence-aware coarse-to-fine querying framework that normalizes encoder scores with temperature scaling and selectively invokes a reasoning VLM only for low-confidence cases. High-confidence queries are answered by fast retrieval, while ambiguous ones are reranked over a small top-K candidate set using the original multi-view images and instance bounding boxes, enabling context-aware disambiguation at low cost. Scene-Q improves open-vocabulary 3D instance segmentation on ScanNet200 and natural-language 3D instance retrieval on real-world reconstructions, with the largest gains on spatial and relational queries while keeping a substantial fraction of queries on the fast path.

---


### 124. [How Far Can Sub-3B Open Language Models Go in Zero-Shot Essay Scoring on an 8 GB Consumer GPU?](https://arxiv.org/abs/2609.20250)

**<font color=#1a73e8>作者：</font>** Nguyen Dung Son, Dang Quang Minh, Nguyen Huu Loi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot essay scoring with large language models is usually demonstrated with proprietary API models, yet the settings where automated scoring is most needed, such as public schools grading thousands of essays under strict privacy rules, are often those where sending student writing to a third-party API is unacceptable. We ask how much capability survives when the model must be a sub-3B open model running fully locally in FP16, with a controlled study of four instruction-tuned models from two families (Qwen2.5 at 0.5B/1.5B/3B, SmolLM2 at 1.7B) on all eight ASAP-AES prompts on a single 8 GB consumer GPU, with bootstrap confidence intervals, Holm-corrected paired tests, and deployment-realistic variants of the key design choices. Three findings emerge. (i) Rubric-decomposed prompting beats holistic prompting for every model under batch min-max aggregation (though Qwen2.5-3B drops significantly on one prompt), and under mean aggregation two unrelated families land within 0.01 at the 1.5-1.7B scale. (ii) Mapping trait scores into the prompt range is fragile to grader calibration: one model compresses traits into a narrow low band (2-4 on 0-10) and naive mean aggregation collapses, while the min-max normalization of Multi-Trait Specialization repairs it (macro QWK 0.204 to 0.388) and stays within 0.03 when its statistics are frozen on 30 held-out essays. (iii) Signed error falls with essay length in eleven of twelve configurations, opposite to the verbosity bias reported for large LLM judges; normalized rubric decomposition largely flattens this slope for well-calibrated models. We anchor results honestly: the best local configuration (0.388) remains far below both the human inter-rater ceiling (0.769) and a length-only baseline (0.523), so we position sub-3B local models strictly for formative, human-supervised feedback.

---


### 125. [Lens: Bringing the Right Semantic Perspective into Focus for Training-Free Multimodal Representation Learning](https://arxiv.org/abs/2609.20252)

**<font color=#1a73e8>作者：</font>** Xinran Liu, Shouqian Shi, Yixian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-quality representations are essential for a wide range of downstream tasks. Dedicated embedding models are explicitly optimized for representation learning, yet their training data are often more limited in scale and diversity than the massive corpora used to pretrain modern large language models and multimodal large language models. Large-scale pretraining and instruction following enable autoregressive models to select relevant evidence, integrate multimodal information, and infer semantics under different task perspectives, creating a distinctive opportunity for training-free representation learning. However, our analysis reveals that existing semantic-elicitation methods do not reliably orient the extracted states toward the semantic perspective required by the downstream task. Consequently, the resulting representations often remain dominated by salient input content. We characterize this problem as semantic perspective misalignment and propose Lens, a training-free framework that makes representation readout task-directed. Semantic Perspective Anchoring associates the task-required perspective with a task-specific readout phrase, specifying the interpretive role of the positions later used for extraction. Contextualized Phrase Readout places the same phrase after the complete input and aggregates its token states, combining full-context access with the anchored perspective. The resulting representation reflects task-conditioned evidence integration and inference rather than a generic summary of salient content. Without parameter updates, architectural modification, or reranking, Lens achieves an overall Precision@1 of 63.9 across all 36 MMEB datasets, outperforming the closest same-backbone training-free embedding baseline by 10.2 points.

---


### 126. [Placement Is Free, Composition Is Not: The Latin Square as a Provably-Balanced Construction for Heterogeneous Sequence-Mixer Stacks](https://arxiv.org/abs/2609.20269)

**<font color=#1a73e8>作者：</font>** Taebong Kim, Youngsik Hong, Minsik Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Since GPT, most Transformers have repeated the same attention mechanism at every layer. Yet this design is largely a convention rather than a tested conclusion. When multiple sequence mixers are combined in one stack, improvements may arise from mechanism choice, placement, or both, making causal attribution difficult. We introduce Aether-7B-5Attn, a 6.59B-parameter mixture-of-experts model ($\approx$2.98B active) whose 49 layers contain seven sequence-mixing mechanisms arranged as a $7\times7$ Latin square. Because each mechanism appears exactly once in every row and column, the design guarantees balanced exposure across depth while eliminating placement confounds. To evaluate this principle, we build a parameter-matched proxy with four mechanisms arranged as a $4\times4$ Latin square over sixteen layers, matched to 700.9M parameters and trained with eight seeds per arm. The results reveal a clear dissociation. Rearranging a distributed heterogeneous stack into a balanced periodic cycle changes validation loss by only 0.16\%, indicating that exact placement has little effect. In contrast, clustering the same mechanisms into contiguous depth bands incurs a 0.59\% penalty, while replacing the heterogeneous stack with a homogeneous one incurs a 1.68\% penalty. These results indicate that performance depends primarily on heterogeneous composition distributed across depth rather than on any particular permutation. We confirm this finding at 2.16$\times$ larger scale (1.514B parameters), where the homogeneous-stack penalty increases to 2.63\% and removing the SSM-family mechanism produces a 3.20\% degradation. We further report per-mechanism cost profiles, English and Korean evaluations, and a causal-safety audit of all 49 layers. We release model weights, training recipes, training code, logs, and architecture source code.

---


### 127. [AgriScope: Pixel-Grounded Multimodal Understanding for Agricultural Images](https://arxiv.org/abs/2609.20325)

**<font color=#1a73e8>作者：</font>** Abderrahmene Boudiaf, Mohamad Alanssari, Irfan Hussain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural image understanding requires fine-grained recognition of plant diseases, pests, crop structures, and botanical species under complex real-world conditions. Despite recent advances in Multimodal Large Language Models (MLLMs), existing models remain limited to text-only outputs and lack pixel-level visual grounding capabilities. In this work, we introduce AgriScope, a unified pixel-grounded multimodal framework for agricultural image understanding. AgriScope jointly supports image-level, region-level, and pixel-level understanding within a unified framework, enabling tasks such as grounded caption generation, referring expression segmentation, and multi-turn multimodal interaction for agricultural imagery. AgriScope integrates biologically specialized semantic representations with dense spatial grounding through biological-semantic encoding, dense spatial representations, and pixel decoding. To support large-scale grounded learning, we introduce AgriGround, a large-scale pixel-grounded agricultural multimodal instruction-tuning dataset containing over 500K images and 11M instruction-following samples spanning plant disease analysis, crop and weed identification, insect pest recognition, and fine-grained botanical understanding. AgriGround is constructed through a multi-stage automatic annotation pipeline that integrates multimodal caption generation, phrase-level grounding, segmentation mask generation, and task-oriented instruction synthesis to produce densely grounded supervision. Extensive experiments across multiple agricultural vision-language tasks demonstrate the effectiveness of AgriScope in pixel-grounded multimodal understanding, establishing a strong benchmark for agricultural vision-language learning and visual grounding. The dataset and code will be made publicly available at (this https URL)

---


### 128. [The More It Says, the More You Pay: A Black-Box Audit of Provider-Side Token Inflation in LLM Services](https://arxiv.org/abs/2609.20370)

**<font color=#1a73e8>作者：</font>** Leilei Chen, Lan Zhang, Chen Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In pay-per-token LLM services, the more a model says, the more users pay. Dishonest providers can covertly manipulate generation to inflate output tokens while largely preserving task utility. We define such manipulation as a Provider-Side Token Inflation Attack (PTIA) and instantiate five representative attacks at the query, prompt, representation, and model levels of the provider-controlled pipeline. Our experiments show that each attack increases mean output length to more than 10.2x the clean baseline, demonstrating PTIA's financial appeal and feasibility at multiple stages of generation. Yet auditing PTIA from black-box responses is difficult for users. Our key observation is PTIA saturation: an initial attack sharply lengthens output, but further strengthening or composition has much less effect. We trace this saturation to stopping behavior: an initial PTIA sharply lowers the end-of-sequence token probability, whereas further intervention lowers it only marginally. Building on this insight, we design a lightweight single-probe audit that applies a controlled lengthening intervention. Under PTIA, the probe induces far fewer additional tokens than under normal service. The audit requires neither a trusted local reference model nor historical clean responses, and its separately issued original and probed requests resemble ordinary traffic, making evasion difficult. Across four open-weight models, it achieves an average detection rate of 85.1% with false-positive rates below 2%. Across 15 real LLM API services, the audit flags 7 for PTIA-consistent behavior.

---


### 129. [Schema-Anchored Latent Reasoning for Semantic Parsing-Based Knowledge Base Question Answering](https://arxiv.org/abs/2609.20398)

**<font color=#1a73e8>作者：</font>** Guangze Gao, Zixuan Li, Sikui Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic parsing (SP)-based knowledge base question answering aims to answer natural language questions by generating executable logical forms (LFs) over knowledge bases (KBs). When applying Large Language Models (LLMs) to this task, a key challenge over large, heterogeneous KBs is selecting question-related schema elements (i.e., relations and classes) and composing them into complex LFs. Recent LLM-based methods often make early discrete commitments to schema elements during intermediate reasoning, allowing incorrect intermediate schema decisions to propagate and finally result in incorrect LFs. To overcome this limitation, we propose SALR, a schema-anchored latent reasoning method for LF construction. It performs multi-step reasoning by generating continuous thoughts in the model's hidden states, thereby delaying the explicit commitment to LF decisions. To ground this latent reasoning process in the corresponding KB schema, SALR aligns continuous thoughts with a codebook of KB schema elements through an alignment objective supervised by schema traces deterministically derived from gold LFs. It then incorporates the aligned schema codes into inputs for subsequent reasoning steps. This schema-mediated feedback guides LF generation without requiring the model to emit an explicit textual reasoning trajectory. Experiments on GrailQA and WebQSP show that SALR achieves consistent overall gains over strong baselines. Notably, on compositional questions from GrailQA, SALR outperforms TIARA, a strong SP-based baseline, by 2.86 F1 points. Further analyses show that schema-mediated feedback affects LF generation and that schema information is recoverable from the latent states.

---


### 130. [Xeno-Interpretability: Investigating the Alien Minds of LLMs](https://arxiv.org/abs/2609.20408)

**<font color=#1a73e8>作者：</font>** F. Pierucci, M. Bracale Syrnikov, M. Prandi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are usually interpreted through concepts that humans already possess: truthfulness, refusal, deception, personality, harmfulness, and related categories. This paper asks whether models may also represent and use distinctions for which no adequate human concept exists. We call such internal structures xeno-representations, and their study xeno-interpretability. We distinguish the human-interpretable semantic space from the xeno-semantic space: the region of model-native representations for which no adequate human conceptual counterpart is available. We show that the space of possible internal distinctions in an LLM is substantially larger than the space available through finite human descriptions. We then separate experimental identification from semantic interpretation: an internal representation may be reproducibly located, geometrically characterized, causally manipulated, and linked to downstream behaviour even when its semantic content cannot be adequately expressed in human terms. On this basis, we sketch an empirical programme to identify xeno-representations. We finally examine the implications for AI safety and multi-agent systems, where model-native representations may propagate and stabilize across interacting agents while remaining only partially visible through human-readable communication. Xeno-interpretability therefore shifts the aim of interpretability from finding human concepts inside models toward discovering and characterizing the representational structures that are native to the models themselves and might affect their behaviour in unpredictable ways.

---


### 131. [SkillAA: Attribution-Guided Skill-Graph Updating with Targeted Validation and Rollback](https://arxiv.org/abs/2609.20455)

**<font color=#1a73e8>作者：</font>** Ziqiao Shang, Ling-Yue Ge, Lan-Zhe Guo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External skills provide domain procedures without parameter updates, but existing methods often edit skills directly from failed rollouts without structured routing from an observed failure to an editable location; existing skill graphs also underuse semantic boundaries, object addresses, and topological dependencies for skill retrieval, targeted updating, and scoped validation. We introduce SkillAA (Skill Abductive Attribution), a structured skill-optimization framework for frozen language models. It represents skill applicability, execution, and composition in a unified graph, allowing the same structure to support skill selection, attribution-guided repair, and update validation. SkillAA contrasts successful and failed executions to route candidate repairs to specific graph objects, updates only the selected local structure, and uses Local and Big Gates to screen candidate changes before commitment. With gpt-5.6-sol, SkillAA reaches 81.5%, 66.7%, and 91.2% on SearchQA, LiveMath, and DocVQA, respectively, and attains the highest observed mean in every main setting. These results support the utility of attribution-guided graph editing and graph-scoped validation.

---


### 132. [Fingerprinting Multimodal Large Language Models](https://arxiv.org/abs/2609.20457)

**<font color=#1a73e8>作者：</font>** Chao Huang, Meng Tong, Kejiang Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While multimodal large language models (MLLMs) enable a wide range of image-text reasoning tasks, recent incidents indicate that they are vulnerable to illicit deployment and unauthorized distillation. Existing solutions for model provenance are typically confounded by shared language backbones in MLLMs and struggle to detect violations of distillation. To bridge this gap and safeguard model ownership, we present the first study on multimodal model fingerprinting. Inspired by recent findings that self-attention acts as a low-pass filter and that its low-frequency components are informative, we develop AttnPrint for white-box provenance. Specifically, we extract cross-modal attention distributions and isolate their low-frequency components to serve as model fingerprints. To facilitate black-box auditing, we further introduce DistillTrace, which employs hypothesis testing of MLLM outputs to identify potential model infringement. We conduct extensive experiments on 154 model instances across 19 multimodal architectures. Notably, AttnPrint achieves strong derivative-model detection performance while remaining robust to five downstream modification techniques. DistillTrace also provides evidence of distillation relationships under three parameter-independent techniques.

---


### 133. [How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents](https://arxiv.org/abs/2609.20474)

**<font color=#1a73e8>作者：</font>** Yukun Zhang, Kemu Xu, Yishen Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses supply planning guidance, organize execution, and check completion. We study how these components affect success, erroneous acceptance, and cost in two Retail experiments and an Airline pilot in $\tau^2$-bench. The primary comparison pairs prewritten task-specific plans (Fixed) with shuffled policy text matched in word count (Sham), isolating the contribution of guidance content. Across 265 matched cells, Fixed improves oracle-verified success by 7.17 percentage points (90\% task-clustered bootstrap interval, 1.15--13.36 points), with gains concentrated in higher-complexity tasks. A read-only terminal verifier rejects 61\% of Retail oracle-invalid episodes while withholding 17\% of correct ones, at less than one cent of additional cost per episode. Which component matters more depends on the loss assigned to erroneous acceptance: at low liability the planning gain dominates; at high liability the verifier's avoided false passes dominate---and a standalone verifier captures nearly all the false-pass benefit of the full planning-plus-verification stack at a fraction of its cost.

---


### 134. [Edustories: A Collection of Real-world Case Studies from Classroom Practices](https://arxiv.org/abs/2609.20484)

**<font color=#1a73e8>作者：</font>** Michal Štefánik, Jan Nehyba, Jirina Karasova 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the widely recognized potential of AI in education, most prior work has focused on individualized student assistance. In contrast, the majority of educational practice worldwide still takes place in collective classroom settings. To enable researchers to study AI assistance in collective teaching, we introduce Edustories, a dataset of 1,492 teacher-written case studies describing real elementary and high-school classroom situations involving challenging student behavior, pedagogical interventions, and their outcomes. Among many other applications, Edustories enables evaluating LLMs' ability to predict the success of teacher interventions, crucial for providing practicing teachers with useful feedback. Comparing the latest models from four language-model families against expert assessments, we find that current models fall short of human expertise in predicting classroom outcomes; the strongest models reach 58% accuracy compared to 64% of human experts. This gap highlights both the limitations and the emerging potential of AI as assistants for practicing teachers.

---


### 135. [When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation](https://arxiv.org/abs/2609.20511)

**<font color=#1a73e8>作者：</font>** Yuxiao Yang, Tianrun Yu, Shangzhe Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study length inflation in on-policy distillation (OPD), where student responses can become excessively long and even exhaust the generation budget. We identify \emph{termination-token mismatch} between base students and post-trained teachers as an important source of this behavior. Across Qwen3, Llama, and Gemma, the two models can place their stopping probability on different EOS tokens, even when their declared stopping sets are identical. This mismatch can suppress the student's preferred termination action without reliably transferring the teacher-preferred alternative. We show that aligning the decoding stopping set alone is insufficient, while treating functionally equivalent EOS tokens as a shared semantic stopping action substantially mitigates mismatch-induced length inflation across all three model families. To further understand how termination behavior evolves over training, we study OPD across different K2-Horizon training stages. This stage-wise analysis shows that termination preferences can shift substantially during training, while also revealing a distinct length inflation late in the OPD run that persists beyond termination alignment. Together, these results identify termination mismatch as an important, but not exhaustive, source of OPD length dynamics. We release an implementation incorporating the proposed termination-handling corrections.

---


### 136. [SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://arxiv.org/abs/2609.20519)

**<font color=#1a73e8>作者：</font>** Haozhe Liu, Tian Ye, Sensen Gao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvements that transfer beyond their development setting, moving automated harness discovery toward production-level outcomes. Four mechanisms survive selection and form SoL-Pi, spanning action execution, context compaction, observation handling, and delegated reading. On the 51-task EdgeBench evaluation, SoL-Pi achieves performance comparable to Pi across GPT-5.6 Sol and Opus 5 while reducing recorded token traffic by 44.7-49.0% and API cost by about one third. In other words, estimated hourly savings are \$8.75-\$13.50 relative to native Codex and Claude Code harnesses, and \$4.36-\$5.71 relative to Pi.

---


### 137. [Relational Attention for Data-Efficient Language Modeling](https://arxiv.org/abs/2609.20530)

**<font color=#1a73e8>作者：</font>** Adrian Brasoveanu, Ece Takmaz, Jakub Dotlačil  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Relational BabyLM, a system submission to the BabyLM 2026 challenge that combines two cognitively motivated inductive biases in a single decoder-only Transformer. Architecturally, we replace standard self-attention with a Dual Attention Transformer (DAT), which separates the routing of object-level ("sensory") lexical features from structural/relational information (Altabaa and Lafferty, 2025; Altabaa et al., 2024; Webb et al., 2024; Kerg et al., 2022; Webb et al., 2021). Relational attention (RA) disentangled from self-attention greatly increases data efficiency and out-of-training-sample generalization on purely relational tasks, but language modeling requires object-level and relational information to be integrated as well as disentangled, and RA-based LMs have remained largely unexplored. BabyLM's data-constrained training and comprehensive evaluation is an ideal testing ground for whether that data efficiency transfers. As a training intervention, we add a Next-Latent Prediction (NextLat; Teoh et al. 2026) objective that encourages hidden states to compress history incrementally into a dense belief state. Architecture is the dominant factor for structural linguistic generalization; the objective is secondary but still significant. DAT's three relational attention types (full RA vs. the simpler RCA and DisRCA variants) are largely interchangeable at 10M words; full RA pulls ahead at 100M. We also introduce a novel symbol-retrieval mechanism (RoPE-based, as opposed to learned, relative symbols) that matches learned symbol libraries while adding no parameters. On the strict (100M-word) track, our best model ranks 6th of 55 overall and 3rd of 55 on the leaderboard's NLP-task subset at the time of writing; our two strongest models outperform the GPT-2 baseline on most benchmarks, with one attaining the highest EWoK score among strict-track entries.

---


### 138. [Towards TEE-Certified DP: Verifiable Differentially Private Training on Legacy GPUs](https://arxiv.org/abs/2609.20532)

**<font color=#1a73e8>作者：</font>** Li Ge, Wenjie Qu, Weitao Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Wide adoption of machine learning has created growing policy and regulatory demand for protecting sensitive training data, with differential privacy (DP) emerging as a key mechanism. Yet a less-studied problem is how to certify the faithful execution of DP during training: an external verifier should be able to check that a released model was trained with proper DP protection, without accessing the private training data. Existing cryptographic approaches, such as zero-knowledge proofs, provide strong guarantees but often incur prohibitive overhead, in some cases by orders of magnitude. Trusted Execution Environments (TEEs) offer a more efficient alternative, but the multi-GPU TEE support needed for training and fine-tuning large language models remains limited to recent platforms and is absent or inefficient on legacy GPUs.
To address this, we propose a practical framework for verifiable DP training using CPU-side TEEs together with untrusted GPUs. Our design addresses a fundamental efficiency-security tension: training entirely inside a CPU TEE is too slow, while unrestricted GPU offloading can allow malicious deviations from DP. We therefore offload expensive gradient computation to GPUs, while using the CPU TEE to efficiently verify the correct enforcement of DP on gradients through probabilistic checking. Our framework detects frequent full deviations from DP with high probability; for the utility-oriented forged-gradient attacks evaluated in this work, sparse deviations provide limited utility benefit and show no measurable additional membership leakage. Experiments further show that our approach nearly achieves a ``free lunch'': it incurs only modest overhead compared with standard GPU-based DP training, while effectively constraining malicious deviations from the claimed DP execution.

---


### 139. [Parallelism, critical windows, and separations among diffusion language models](https://arxiv.org/abs/2609.20539)

**<font color=#1a73e8>作者：</font>** Sitan Chen, Liye Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A popular selling point of diffusion large language models (dLLMs) is their capacity for parallelism: the ability to generate sequences of text far more efficiently than autoregressive models, which require one forward pass per token. Yet among the many competing paradigms for dLLMs, from masked to uniform to Gaussian diffusion, principled understanding of how these different proposals compare in parallelism remains limited. In this work, we initiate a fine-grained comparison of the capacity for parallelism among these three leading approaches and prove the following:
- Uniform and Gaussian diffusion can sample in a number of forward passes which scales with the dual total correlation of the underlying distribution, a measure of intrinsic complexity which can be much smaller than the context length. Previously, it was only known how to achieve this using masked diffusion.
- For a certain family of random empirical measures, we show that $\widetilde{\Theta}(\sqrt{d})$ forward passes are necessary and sufficient to sample using uniform or Gaussian diffusion, yet there exist approximate score oracles for which $\widetilde{\Omega}(d)$ forward passes are needed for masked diffusion. This establishes the first provable separation in parallelism between the three prevailing dLLM paradigms.
Contrary to popular intuition that masked diffusions are harder to parallelize because they must commit to token values, the latter separation instead comes from the fact that the critical windows in masked diffusion sampling are asymptotically narrower than those in uniform and Gaussian diffusion sampling.

---


### 140. [An Analysis of Training-Free Self-Reported Confidence in Language Models](https://arxiv.org/abs/2609.20541)

**<font color=#1a73e8>作者：</font>** Lukas Meyer, Sofia Rossi, Wei Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can report a numerical confidence together with generated content, but it is unclear whether this report is more than calibrated rhetoric. We analyze three training-free signals: confidence verbalized with the answer, post-hoc $P(\mathrm{True})$, and agreement with three additional generations on the same 100 TriviaQA questions for two model families. Direct verbalization is a surprisingly strong baseline: after auditing benchmark errors, it reaches AUROC 0.956 and 0.937 for correctness prediction. Three-sample agreement is substantially weaker (0.765 and 0.790), and a fixed interpolation with verbalized confidence has no statistically reliable benefit. Four of nine errors from one model and two of eight from the other receive unanimous sample support, showing that self-consistency can amplify shared misconceptions. Re-eliciting confidence for the same fixed answers with equivalent prompts changes scores by 0.043 to 0.084 on average and flips 4\% to 9\% of decisions at a 0.8 threshold. An exploratory audit of 100 confidence-tagged biography claims further finds only a modest confidence gap between supported and contradicted claims. These results argue that useful self-reports remain sensitive to elicitation, correlated errors, and benchmark noise.

---


### 141. [Language-model groups overstate consensus when replaying human deliberation on a reasoning task](https://arxiv.org/abs/2609.20543)

**<font color=#1a73e8>作者：</font>** Tengfei Shao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-consensus rates are often treated as indicators of collective cognition, yet depend on how participation and final states are operationalized. We replayed 100 held-out human Wason groups with matched large language model (LLM) agent groups, seeding one belief-anchored agent per participant's pre-discussion answer and scoring agents and people with the same code. Across human scoring definitions, estimates ranged from 24.0% to 57.0%; about one fifth of participants never posted, whereas agents almost always did. Agent groups remained more consensual in two post-unblinding sensitivity analyses: the submit-based comparison (n = 98) yielded gaps of 34.0 and 43.9 percentage points for chat and reasoning modes, and the participation-matched comparison (n = 45) yielded gaps of 34.1 and 44.4 points. These complementary routes reduced different measurement asymmetries yet converged within 0.5 percentage points. The gap persisted without early stopping and under a reparameterization removing the memorizable answer; reasoning-mode groups then agreed nearly unanimously, mostly on incorrect answers. Simulated consensus did not track collective accuracy, and belief-anchored agent groups were biased estimators of the human group-outcome distribution in this setting. These analyses provide a scoring-explicit basis for assessing simulated-group estimates of human deliberative outcomes.

---


### 142. [Steering the Compass: Aligning Dynamic Psychological Counseling Conversations with Cognitive Behavioral Therapy Strategies](https://arxiv.org/abs/2609.20565)

**<font color=#1a73e8>作者：</font>** Zimu Wang, Yiwen Jiang, Xiangyu Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in large language models have revolutionized the field of psychological counseling, especially in the context of Cognitive Behavioral Therapy (CBT). While the success of CBT relies heavily on dynamic decision-making informed by the client's real-time mental state, this aspect has often been overlooked in current research, limiting both flexibility and therapeutic outcomes. In this paper, we introduce StratCBT, a dataset specifically designed for psychological counseling conversations with CBT Strategies, consisting of 9,688 sessions and around 256K utterances, with each counselor's response aligned with one of eight distinct strategies. The creation of StratCBT involves modeling clients based on their negative thoughts and generating high-quality counseling conversations through self-chat, incorporating realistic sessions as guidance, thereby significantly surpassing existing datasets in both general counseling and CBT-specific skills. We conduct extensive experiments to demonstrate the effectiveness of strategy-aligned generation and evaluate its efficacy in delivering professional and effective counseling with LLM-simulated clients to reflect real-world scenarios. The dataset can be obtained from this https URL.

---


### 143. [DocAttriBench: Benchmarking Answer Grounding in Document Visual Question Answering](https://arxiv.org/abs/2609.20574)

**<font color=#1a73e8>作者：</font>** Luca De Grandis, Silvia Cappelletti, William Raccagni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Answer grounding in document visual question answering remains an open challenge: most benchmarks lack grounding annotations or provide limited-quality labels, while constructing grounded datasets still requires costly manual effort. We introduce DocAttriBench (DAB), a large-scale benchmark for fine-grained, element-level source attribution in Document VQA, grounding answers to specific layout elements such as text blocks, tables, and images. To build DAB, we propose a Mask-based Perplexity-Derived Attribution method (MAPPET) that combines document layout and language modeling to identify the most informative element for each answer. MAPPET measures the increase in perplexity after masking candidate elements and attributes the answer to the element contributing most to model confidence. Applying MAPPET to multiple existing Document VQA datasets yields DAB, with 237k documents and 296k question-answer pairs with element-level grounding. We benchmark grounding-capable multimodal LLMs on DAB, evaluating answer accuracy, attribution accuracy, and overall answer quality. Results show that while larger models generally achieve higher answer accuracy, even the strongest models often fail to localize the supporting elements. DAB provides a scalable benchmark for developing grounded, verifiable, and trustworthy Document VQA models. Dataset and code are available at this https URL.

---


### 144. [SAFARI: An Industrial Benchmark for LLM-Assisted Hazard Analysis and Risk Assessment](https://arxiv.org/abs/2609.20584)

**<font color=#1a73e8>作者：</font>** Chenxi Wu, Zimu Wang, Haiyang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly considered for safety-critical engineering, yet their reliability in regulated functional-safety workflows remains underexplored. We introduce SAFARI (Safety-Aware Functional Automotive Risk Inference), the first industrial benchmark for LLM-assisted automotive Hazard Analysis and Risk Assessment (HARA) under ISO 26262. It contains 3,000 de-identified industrial HARA cases and evaluates two coupled tasks: open-ended hazard analysis and standards-grounded risk assessment. To evaluate open-ended HARA artifacts, we propose the first reference-anchored LLM-as-a-judge protocol with high expert correlation. Experiments with nine frontier LLMs show that models often produce plausible hazard narratives but remain weak at ISO 26262 risk classification, with the best ASIL macro-F1 reaching only 0.261. Chain-of-Thought prompting provides limited benefit and often degrades categorical risk assessment. Error analysis further localizes major failures to scenario-critical context omissions during hazard generation and to controllability misjudgments during risk assessment, indicating where expert oversight should be concentrated. The dataset can be obtained from this https URL.

---


### 145. [WiC is Not WSD: A Study on LLMs and Lexical Ambiguity Resolution](https://arxiv.org/abs/2609.20593)

**<font color=#1a73e8>作者：</font>** Yi Zhou, Kiamehr Rezaee, Danushka Bollegala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word-in-Context (WiC) remains challenging for language models, despite recent progress on lexical-semantic tasks. We hypothesise that this difficulty arises not only from comparing two contextual uses of a word, but also from the absence of an explicit sense inventory that specifies the relevant level of semantic granularity. We evaluate open LLMs on WiC and traditional Word Sense Disambiguation (WSD) under similar settings. We find that providing candidate senses, similar to what is done in traditional WSD, improves WiC performance in all settings. In general, explicit sense information helps models make more consistent and targeted judgements. Human evaluation further shows that many apparent WiC errors reflect label ambiguity or mismatches between model and annotator sense boundaries rather than simple failures of lexical understanding. In particular, results show that LLMs overthink the sense distinction often leading to errors based on overly fine-grained distinctions.

---


### 146. [What Does Privileged Information Add to On-Policy Self-Distillation?](https://arxiv.org/abs/2609.20612)

**<font color=#1a73e8>作者：</font>** XiuYu Zhang, Wei Chow, Junfeng Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) lets a language model learn from a frozen copy of itself that sees an answer or a worked solution. Giving the teacher this extra information seems to offer the student more to learn, but how much does it add beyond distillation itself? To isolate that contribution, we construct AMPLE-Math, a reusable suite of 5,319 mathematical problems with six reasoning views that share the same answer, and compare each view with matched reference-free distillation. With a thinking-enabled teacher supervising direct-response rollouts, reference-free distillation accounts for much of Qwen3-1.7B's improvement under thinking-enabled evaluation, both in domain and on external benchmarks. Evidence for an additional reference benefit is modest in Qwen, strongest for a polished solution, whereas complete traces add two percentage points in SmolLM3-3B at step 50. These benefits depend on the student being trained. At the same checkpoint, replacing short direct-response rollouts with long thinking-enabled rollouts turns gains into losses in both families while the problems, references, and evaluation stay fixed. Teacher profiles and matched loss interventions in Qwen further show that changing token-level supervision can leave student behavior largely unchanged. Together, these findings suggest that OPSD can improve access to existing reasoning capabilities through parameters shared by direct-response and thinking-enabled inference. The value of a privileged reference is what it adds to this cross-mode transfer, not how much of the solution it reveals.

---


### 147. [Chronicle: Cut-Point Replay for Regression Testing of LLM Agents](https://arxiv.org/abs/2609.20625)

**<font color=#1a73e8>作者：</font>** Tisha Chawla, Susheem Koul  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model responses are non-deterministic, so failures in LLM agents are hard to reproduce: a failure depends on inference that is not bitwise reproducible, on tools that read changing state, and on a multi-step trajectory that a re-run rarely repeats. Record-and-replay makes a run reproducible, but existing agent tooling records runs only to trace or score them, not to test a code change against them. We present Chronicle, which records an agent run at its non-deterministic boundaries as immutable envelopes and replays it from the record. Its central operation, cut-point replay, serves a chosen subset of boundaries from the record and executes the complementary subset live with new code, turning a recorded incident into a regression test that runs in continuous integration. On a benchmark of 6 recorded failures with simulated model boundaries, recording adds 23 {\mu}s per crossing (0.008% of an assumed 300 ms model call), full replay issues zero model calls and is bit-stable across 20 repetitions, and cut-point tests fail on faulty code and pass on guarded and benign changes for all 6 incidents. In a mutation study of the guarded tools, cut-point tests catch every mutant that lets the recorded unsafe action through, while a baseline that stubs every boundary, using the same assertion, catches none. Chronicle and the benchmark are publicly available at this https URL.

---


### 148. [HerHealthEval: Evaluating Multilingual and Register-Sensitive Understanding of Women's Health Communication](https://arxiv.org/abs/2609.20684)

**<font color=#1a73e8>作者：</font>** Hassan Saeed Hassan Albattra, Mazen Mohammed Bahgat, Rahatara Ferdousi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in healthcare communication, yet most evaluations emphasize response quality while assuming that the user's concern has been interpreted correctly. We introduce HerHealthEval, a controlled evaluation framework for multilingual understanding of women's-health communication. For each clinical case, HerHealthEval provides matched versions in English, French, and Modern Standard Arabic using six communicative forms: canonical, clinical, layperson, indirect or hedged, emotionally concerned, and deliberately under-specified. The first five express the same underlying concern and retain the same clinical information, whereas the under-specified form intentionally omits relevant details to test whether the model recognizes that clarification is needed. We evaluate a multilingual instruction model and QLoRA-adapted variants on concern classification, risk calibration, clarification behavior, parse compliance, and cross-form consistency. Results reveal that aggregate accuracy and consistency can conceal safety-relevant failures. A multilingual adaptation model reaches 0.994 under-triage in French and Arabic under language-asymmetric risk supervision. A controlled re-adaptation using source-derived, language-invariant risk labels reduces under-triage to 0.572 and 0.558, respectively. These findings show that robust multilingual healthcare evaluation requires explicit testing of register variation, uncertainty handling, and the provenance and invariance of adaptation labels.

---


### 149. [Summarization Bias: The Directional Collapse of Objective Projection into Told-Mode Labels in Large Language Models --- A Conceptual Framework and Registered Test Protocol](https://arxiv.org/abs/2609.20712)

**<font color=#1a73e8>作者：</font>** Levent Bulut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces and operationalizes summarization bias: a proposed systematic tendency of large language models (LLMs) to represent narrative meaning as an abstract summary label rather than as the reconstructable inferential structure that produces it. Within the Bulut Doctrine, narrative effect is theorized along a told-shown axis: in told mode, emotional and informational content is declared explicitly and requires little reader reconstruction; in shown mode, that content is suppressed at the surface and must be reconstructed from physical cues and indirection (Objective Projection). Shown mode is the higher-load condition the doctrine is designed to measure.
The claim is that LLMs fail along this axis in a specific direction. Summarization bias is hypothesized to operate in two regimes: (i) a generative regime, in which a model asked to render an emotion through Objective Projection defaults to declaring it instead; and (ii) an evaluative regime, in which a model judging narrative quality rewards told-mode explicitness and under-detects shown-mode suppression. The evaluative regime is the more consequential, since LLMs increasingly serve as judges and reward models, and a directional bias toward told mode would impose a selection pressure degrading prose toward flat declaration.
This report does not claim the bias is validated. It defines the construct, situates it against LLM-as-judge biases, rereads a completed independent reliability study as directional evidence consistent with it, and pre-registers a two-regime test with decision rules under which the construct would be abandoned.

---


### 150. [Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL](https://arxiv.org/abs/2609.20715)

**<font color=#1a73e8>作者：</font>** Juzheng Zhang, Disha Makhija, Manoj Ghuhan Arivazhagan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent trajectories record what an agent does and what happens next. Yet standard supervised fine-tuning (SFT) applies loss only to agent-authored action tokens, using environment observations as context but not as prediction targets. We ask whether this convention provides the best initialization for subsequent reinforcement learning. We introduce ActObs, which also supervises the observation tokens already present in each trajectory. Although deployed agents never generate observations, learning to predict them encourages the policy to model action consequences without adding data, parameters, sequence tokens, or forward passes. The methods perform similarly after SFT but diverge after GRPO. On Qwen3-4B, GRPO from ActObs achieves higher pass@k at every evaluated sampling budget than its action-only counterpart on Terminal-Bench 2.0. On Qwen3-8B, it trades some pass@1 reliability for higher pass@k (+3.4 pp at pass@16) and solves more distinct tasks. The advantage extends to cross-domain code editing on aider-polyglot (+4.2 pp at pass@1 at 4B), whose tasks are unseen during SFT and RL. ActObs retains more entropy during RL while requiring less policy movement, leaving the final policy closer to its SFT initialization. Our analysis traces this difference to SFT: action and observation gradients rapidly become orthogonal, while action-only training leaves a large residual observation gradient and degrades environment prediction below the base model. Joint supervision prevents this one-sided specialization, preserving consequence prediction and preparing the policy for downstream exploration.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
