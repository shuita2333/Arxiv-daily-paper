# 🧠 大模型相关研究 | 2026年06月26日

> 本类共 **112** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-112**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-112**

---

### 101. [InvestPhilBench: A Multi-Layer Dynamic Benchmark for Evaluating Large Language Model Procedural Reasoning in Expert Investment Philosophy](https://arxiv.org/abs/2606.25984)

**<font color=#1a73e8>作者：</font>** Mingguang Chen, Bo Qu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as investment research assistants, yet no benchmark tests whether they can accurately reconstruct and apply the specific procedural decision frameworks of expert investors. We introduce InvestPhilBench, a multi-layer dynamic benchmark spanning eight cognitive tiers, from principle identification (L1) to novel framework extrapolation (L8). The v0.6 release comprises 118 primary-source-verified investment principle cards, 25 decision framework cards with explicit topology metadata, and 243 QA questions (197 dev / 46 held-out test). For reproducible scoring at scale we introduce the Benchmark Automated Scoring Pipeline (BASP) -- five algorithmic metrics (OGRS, KCCS, SAP@k, IVP, CKCA) -- the Failure Mode Detection Protocol (FMDP) with computable rules for six failure modes, and Gate Reconstruction Accuracy (GRA), a per-gate metric for questions with gold reasoning programs. In this release, InvestPhilBench is primarily a benchmark-and-methodology contribution. A four-model sanity wave on the 188-question development split shows a sharp provider-tier split (BASP 0.906 vs. 0.438); these mixed-judge numbers are confounded upper bounds. The central finding: the BASP composite saturates at the frontier (Claude L4 = 0.932) while GRA still exposes a procedural deficit (frontier L4 GRA approx. 0.77, L7 GRA 0.57-0.62) -- composite scoring rewards fluent prose and hides the procedural gap. v0.6 implements a unified judge and true model-in-the-loop retrieval/oracle conditions; the de-confounded multi-model leaderboard and full three-condition run are v1.0 deliverables. On a 100-item expert-annotated gold set the automated BASP composite tracks the human reference at Pearson r = 0.72 (MAE = 0.10), with attribution (SAP@3) the weakest sub-metric and the failure-mode detector running sensitive-but-over-flagging.

---


### 102. [Weave of Formal Thought](https://arxiv.org/abs/2606.25987)

**<font color=#1a73e8>作者：</font>** Alexandre Bouayad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) attain remarkable surface fluency on code, yet they neither formally guarantee the syntactic validity of their output nor leverage the hierarchical structure defining the target language. While existing constrained-decoding frameworks address the former, they operate under rigid assumptions that preclude critical lexical mechanisms -- including context-sensitive lexing, maximal-munch tokenization, and keyword extraction -- and only approximate vocabulary masking, sacrificing completeness. For the latter, code LLMs typically inject grammatical structure via predetermined policies rather than learning which structural information to expose. In this work, we introduce Weave of Formal Thought (WoFT), a paradigm uniting rigorous syntactic validation with learned structural representations. First, we present a formal engine and constrained decoder that is sound and complete with respect to the full Tree-sitter specification. By augmenting generalized LR (GLR) parsing with a speculative-lexing construction that maintains concurrent lexer-state hypotheses synchronized with a GLR graph-structured stack, our decoder admits every subword token extending to a valid program prefix and rejects all others. Second, we present a latent-variable fine-tuning method training the language model to interleave non-terminal grammar symbols directly into generation. Utilizing the reweighted wake-sleep (RWS) algorithm to optimize the importance-weighted evidence lower bound (IW-ELBO) of the surface text, the model learns to selectively retain formal derivations as an adaptive structural scratchpad. For Python, fine-tuning StarCoder2-3B with our RWS objective reduces per-token cross-entropy by 14.3% relative to a text-only SFT baseline, demonstrating that discretionary latent syntax recovers critical structural information that flat autoregressive training discards.

---


### 103. [Autodata: An agentic data scientist to create high quality synthetic data](https://arxiv.org/abs/2606.25996)

**<font color=#1a73e8>作者：</font>** Ilia Kulikov, Chenxi Whitehouse, Tianhao Wu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Autodata, a general method that enables AI agents to act as data scientists who build high quality training and evaluation data. We show how to train (meta-optimize) such a data scientist agent, so that it learns to create even stronger data. We describe the overall formulation, and a specific practical implementation, Agentic Self-Instruct. We conduct experiments on computer science research tasks, legal reasoning tasks and reasoning with mathematical objects, where we obtain improved results compared to classical synthetic dataset creation methods. Further, meta-optimizing the data scientist agent itself delivers an even larger performance uplift. Agentic data creation provides a way to convert increased inference compute into higher quality model training. Overall, we believe this direction has the potential to change the way we build AI data.

---


### 104. [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It](https://arxiv.org/abs/2606.26027)

**<font color=#1a73e8>作者：</font>** Yupu Hao, Zhuoran Jin, Huanxuan Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities. However, RL alone often leads to instability or limited gains in tool-use tasks. In our experiments, some models exhibit catastrophic collapse, where performance abruptly drops and tool-invocation structures fail. The analysis reveals that these failures stem from unexpected probability spikes in specific control tokens, disrupting structured execution, yet the underlying tool-use capability remains intact, merely obscured by specific formats. To address this, we systematically investigate a diverse set of supervisory signals, including off-policy supervision, hint-based guidance, erroneous example supervision, and others, applied under both synchronous and interleaved training schemes. We find that interleaving supervised fine-tuning (SFT) with RL substantially improves stability, but exhibits degraded performance under format and content out-of-distribution (OOD) evaluation. We also analyze the impact of learning rates and generalization across settings. These results highlight the importance of understanding RL failures and demonstrate how diverse supervisory signals can guide exploratory learning, enabling robust training of LLMs for complex, multi-step tool-use tasks. Our Code is available at this https URL.

---


### 105. [TriViewBench: Controlled Complexity Scaling for Multi-View Structural Reasoning in MLLMs](https://arxiv.org/abs/2606.26029)

**<font color=#1a73e8>作者：</font>** Yu-Yang Chen, Lan-Zhe Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) demonstrate strong performance on standard visual question answering benchmarks, yet their scalability under controlled structural complexity remains poorly understood. We introduce TriViewBench, a controlled three-view visual reasoning benchmark constructed from synthetic 3D scenes with explicitly parameterized object count and occlusion. The benchmark contains 1,923 scenes and over 14K Question-Answer (QA) pairs organized into four complexity levels and three reasoning categories: Local Decision, Object Counting, and Global Recovery. We evaluate 18 open- and closed-source MLLMs under a unified prompting protocol. All 18 models exhibit an identical capability hierarchy without exception (Local Decision > Object Counting > Global Recovery), and performance degrades monotonically with complexity: Local Decision tasks decline modestly (12.11% relative drop), while Object Counting degrades substantially (59.14%) and Global Recovery collapses severely (80.02%). Error analysis on Object Counting reveals two mechanistically independent failure modes: single-view tasks are dominated by undercounting due to occlusion blindness, whereas the multi-view task reverses to overcounting due to cross-view identity confusion. Chain-of-Thought (CoT) prompting yields near-zero overall benefit ($\Delta = -0.16\%$) and its effect on Global Recovery is strongly capability-gated, suggesting that the bottleneck lies in cross-view spatial representation rather than reasoning strategy. These findings reveal fundamental scalability limitations in current MLLMs and position TriViewBench as a controlled diagnostic framework for analyzing structural reasoning failures.

---


### 106. [Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning](https://arxiv.org/abs/2606.26036)

**<font color=#1a73e8>作者：</font>** Poojitha Thota, Shirin Nilizadeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.

---


### 107. [AI translation of literary texts is "fine", but readers still prefer human translations](https://arxiv.org/abs/2606.26040)

**<font color=#1a73e8>作者：</font>** Yves Ferstler, Adam Podoxin, Ty Brassington 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.

---


### 108. [How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations](https://arxiv.org/abs/2606.26041)

**<font color=#1a73e8>作者：</font>** Yuxing Cheng, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong performance on OCR-based benchmarks and increasingly focused on text-rich understanding, but their robustness under controlled visual degradation remains insufficiently understood. This gap is critical for OCR reasoning, where visual corruption can induce OCR errors and structural distortions, thereby introducing uncertainty into the reasoning task. To systematically study this problem, we introduce OCR-Robust, a benchmark designed for evaluating OCR reasoning robustness under visual perturbations. It contains 812 samples across two complementary subsets: OCR1.0, covering documents, scene text, receipts, handwriting, and mathematical content, and OCR2.0, focusing on charts, geometry diagrams, and tables. To enable efficient yet informative evaluation, we conduct a pilot study over 18 candidate perturbations and select 5 representative types at 3 severity levels each based on their impact and cross-model discriminability. We evaluate robustness using clean accuracy, Relative Corruption Retention (RCR), Worst-Case Retention (WCR), and a composite Corruption Robustness Index (CRI), and benchmark 18 models spanning proprietary systems, open-source VLMs, and OCR+LLM pipelines. Our results show that higher clean accuracy does not necessarily imply stronger robustness, and that models can suffer pronounced degradation in the worst case on OCR tasks that are sensitive to structure, and charts and tables are substantially more fragile than document-like inputs under perturbation.

---


### 109. [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/abs/2606.26057)

**<font color=#1a73e8>作者：</font>** Seth Dobrin, Łukasz Chmiel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems.
We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment.
We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.

---


### 110. [Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment](https://arxiv.org/abs/2606.26071)

**<font color=#1a73e8>作者：</font>** Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.

---


### 111. [Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models](https://arxiv.org/abs/2606.26079)

**<font color=#1a73e8>作者：</font>** Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.

---


### 112. [Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents](https://arxiv.org/abs/2606.26080)

**<font color=#1a73e8>作者：</font>** Changdae Oh, Wendi Li, Seongheon Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.

---


> [!TIP]
> 当前位于：**101-112**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-112**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
