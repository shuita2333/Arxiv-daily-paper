# 🧠 大模型相关研究 | 2026年09月18日

> 本类共 **210** 篇论文：已确认 **198** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-210](./part-05.md)

---

### 101. [Market Signal Injection: Adversarial Context Manipulation of LLM Pricing Agents](https://arxiv.org/abs/2609.18357)

**<font color=#1a73e8>作者：</font>** Dohun Lee, Hyunwoo Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) pricing agents may respond to how market data is presented, even when its numerical values remain unchanged. We introduce market signal injection (MSI), an attack that manipulates numerical formatting, competitor ordering, or qualitative market commentary without issuing explicit instructions. We evaluate nine open-weight models in simulated Bertrand duopoly and triopoly markets and three proprietary models in duopoly markets. Sentiment-based attacks produce the largest behavioral shifts, which propagate to other firms and alter profits and consumer surplus. Susceptibility varies across model families, and larger models are not consistently more robust. Matched neutral-text controls and a rule-based agent support a framing-based account of these shifts under the fixed demand parameters of our simulation. Episode-held-out probes distinguish baseline from attacked activations in all eleven re-evaluated model--condition pairs: linear AUC is 1.00 and MLP AUC ranges from 0.93 to 0.99. This separability does not by itself identify harmful pricing decisions. Input canonicalization removes the tested sentiment attacks, while decision boundary anchoring, which combines prompt constraints with output projection, provides partial mitigation under the tested adaptive attacks. These results identify data presentation as an attack surface for LLM pricing agents and motivate defenses that account for interactions among agents.

---


### 102. [GYROval: A Robust Benchmark for Cultural Value Orientation in Large Language Models](https://arxiv.org/abs/2609.18384)

**<font color=#1a73e8>作者：</font>** Alexander Didenko, Anna Shabanova, Vladislav Zapylikhin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present a robust benchmark for measuring cultural value orientation in large language models on the two Inglehart-Welzel axes over several domains and roles (hence GYROval - Gridded Yielding of Robust value Orientation), together with the results of administering it to twenty models. Items are binary contrastive scenarios in the sense introduced by CDEval: both options are legitimate courses of action, neither is correct, there is no answer key, and a model's score on an axis is the proportion of its responses falling on the counted pole. Eleven of the twenty models were additionally administered a paired Russian translation of the identical items and a second sampling temperature. The instrument is publicly released in both languages. Stability was assessed by treating the vignette as the unit of analysis, ranking the models within the levels of each perturbation factor, and summarising the agreement between levels by tie-corrected Kendall's \emph{W} against an empirical permutation null.

---


### 103. [Building a Cultural Perspective on Doctor-Patient Conversations](https://arxiv.org/abs/2609.18390)

**<font color=#1a73e8>作者：</font>** Krithi Shailya, Siddharth D Jaiswal, Ashish Makani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-powered medical scribes are increasingly used to transcribe doctor-patient conversations and automate clinical documentation. However, large-scale real-world consultation datasets are scarce due to the sensitivity of clinical conversations, leading developers to rely on simulated and LLM-generated synthetic consultations. While scalable, these alternatives may fail to capture culturally situated patterns of clinical interaction. We introduce interactional cultural markers, measurable patterns of doctor-patient interaction grounded in cross-cultural clinical communication, and use them to compare real, simulated, and synthetic consultations from Indian and US clinical contexts. We find distinct patterns of participation and control: Indian consultations involve greater patient participation but stronger doctor control, while US consultations exhibit balanced participation and open-ended discussion. Synthetic Indian consultations often fail to reproduce these patterns, instead converging toward US-like interaction. We identify additional synthetic signatures, including excessive doctor explanation and formulaic patient responses. We conclude by discussing implications for generating culturally grounded synthetic clinical conversations.

---


### 104. [Cultural Competence in Context: A Large Language Model Passes the Turing Test in Finland](https://arxiv.org/abs/2609.18394)

**<font color=#1a73e8>作者：</font>** Otto Segersven, Pentti Henttonen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We report the results of a Turing Test conducted in Finland in the Finnish language. Because languages and cultural contexts are unevenly represented in LLM training data, we expected the model (ChatGPT 5.2) to perform worse in a Finnish-language Turing Test than in previously studied English-language US contexts. We also present model-generated role prompting as a replicable technique for conducting comparative LLM-based Turing Tests designed to improve construct validity. Contrary to our expectations, the LLM passed the Finnish Turing Test. A prominent source of error was participants' reliance on linguistic cues, particularly colloquial Finnish, as markers of human authorship. We reframe the Turing Test from a test of intelligence to a comparative method for examining whether an AI system can display credible membership in a particular social world. Because its outcome reflects model capabilities, prompted identity, insider competence among human participants, and their AI literacy, the method provides a useful probe of the human-machine boundary across domains.

---


### 105. [The Verifiable Action Card: Trustworthy Human-in-the-Loop Control for Secure Autonomous Agents](https://arxiv.org/abs/2609.18411)

**<font color=#1a73e8>作者：</font>** Hasnain Irshad, Anam Mughees, Neelam Mughees 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic browsers can execute security-sensitive actions under a user's authenticated session, making indirect prompt injection and deceptive confirmation interfaces a direct threat to action integrity. Existing human-in-the-loop (HITL) safeguards are insufficient when the approval prompt itself can be influenced by untrusted page content or model-generated text. We present the \emph{Verifiable Action Card} (VAC), an architectural defence that reconstructs approval information from the ground-truth pending browser action and trusted intent provenance, renders it out-of-band in the trusted browser chrome, and binds approval to the exact action re-verified at dispatch. VAC combines provenance fencing, a ground-truth action descriptor, default-deny confirmation, provenance-aware risk gating, and execution binding. We implement VAC in a complete agentic browser and evaluate it on a 24-scenario benchmark covering confused-deputy attacks, Lies-in-the-Loop dialog forging, indirect prompt injection, adaptive action substitution, provenance evasion, and legitimate tasks. Across the evaluated LLMs, attack success without VAC ranges from $68\%$ to $100\%$, whereas VAC reduces attack success to $0\%$ on every model, with $78\%$ legitimate-task completion and a $0\%$ false-block rate. These results show that grounding approval in the action that will actually execute provides architectural protection against security failures that prompt-level defences and conventional HITL confirmation cannot reliably prevent.

---


### 106. [Vocabulary-Guided Gait Recognition](https://arxiv.org/abs/2609.18413)

**<font color=#1a73e8>作者：</font>** Panjian Huang, Saihui Hou, Chunshui Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> What is a gait? Appearance-based gait networks consider a gait as the human shape and motion information from images. Model-based gait networks treat a gait as the human inherent structure from points. However, the considerations remain vague for humans to comprehend truly. In this work, we introduce a novel paradigm Vocabulary-Guided Gait Recognition, dubbed Gait-World, which attempts to explore gait concepts through human vocabularies with Vision-Language Models (VLMs). Although VLMs have achieved the remarkable progress in various vision tasks, the cognitive capability regarding gait modalities remains limited. The success element in Gait-World is the proper vocabulary prompt where this paradigm carefully selects gait cycle actions as Vocabulary Base, bridging the gait and vocabulary feature spaces and further promoting human understanding for the gait. How to extract gait features? Although previous gait networks have made significant progress, learning solely from gait modalities on limited gait databases makes it difficult to learn universal gait features for practicality. Therefore, we propose the first Gait-World model, dubbed {\alpha}-Gait, which guides the gait network learning with vocabulary knowledge from VLMs. However, due to the heterogeneity of the modalities, directly integrating vocabulary and gait features is highly challenging as they reside in different embedding spaces. To address the issues, {\alpha}-Gait designs Vocabulary Relation Mapper and Gait Fine grained Detector to map and establish vocabulary relations in the gait space for detecting corresponding gait features. Extensive experiments on CASIA-B, CCPG, SUSTech1K, Gait3D and GREW reveal the potential value and research directions of vocabulary information from VLMs in the gait field.

---


### 107. [Dependency-Aware Trajectory Refinement for Efficient Multi-Turn Agent Fine-Tuning](https://arxiv.org/abs/2609.18417)

**<font color=#1a73e8>作者：</font>** Zhuo Chen, Zhen Zhang, Xinyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn agent trajectories often contain redundant rounds (failed tool calls, parallel sub-queries, verification-only steps) that inflate both training and inference cost. We propose viewing each trajectory as a \emph{round-level dependency DAG} that exposes which rounds are globally load-bearing for the final answer, and fine-tune agents on trajectories refined through this DAG. Given an LLM-annotated DAG, these edits are deterministic and interpretable, with optional rephrasing. Models trained on these refined trajectories consistently outperform those trained on the original trajectories at lower inference cost. Specifically, across four multi-modal QA benchmarks, our refinements improve downstream accuracy by up to $1.7$\,pp over vanilla SFT (and $5.7$\,pp over an LLM-deletion baseline) while reducing per-sample inference messages by up to approximately $40\%$ and inference tokens by up to approximately $48\%$, translating to substantial savings in compute and serving cost. Code is available.

---


### 108. [Occluded Gait Recognition with Mixture of Experts: An Action Detection Perspective](https://arxiv.org/abs/2609.18432)

**<font color=#1a73e8>作者：</font>** Panjian Huang, Yunjie Peng, Saihui Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extensive occlusions in real-world scenarios pose challenges to gait recognition due to missing and noisy information, as well as body misalignment in position and scale. We argue that rich dynamic contextual information within a gait sequence inherently possesses occlusion-solving traits: 1) Adjacent frames with gait continuity allow holistic body regions to infer occluded body regions; 2) Gait cycles allow information integration between holistic actions and occluded actions. Therefore, we introduce an action detection perspective where a gait sequence is regarded as a composition of actions. To detect accurate actions under complex occlusion scenarios, we propose an Action Detection Based Mixture of Experts (GaitMoE), consisting of Mixture of Temporal Experts (MTE) and Mixture of Action Experts (MAE). MTE adaptively constructs action anchors by temporal experts and MAE adaptively constructs action proposals from action anchors by action experts. Especially, action detection as a proxy task with gait recognition is an end-to-end joint training only with ID labels. In addition, due to the lack of a unified occluded benchmark, we construct a pioneering Occluded Gait database (OccGait), containing rich occlusion scenarios and annotations of occlusion types. Extensive experiments on OccGait, OccCASIA-B,Gait3D and GREW demonstrate the superior performance of this http URL is available at this https URL.

---


### 109. [WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories](https://arxiv.org/abs/2609.18435)

**<font color=#1a73e8>作者：</font>** Yuna Oikawa, Kei Endo, Takanori Uzawa 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating biological research requires general-purpose, reproducible robot systems that allow individual wet-lab researchers to delegate robot tasks without performing teleoperation or neural-network training. Vision-language-action policies have been proposed for general-purpose arms, but can lose performance when their operating environment changes. We therefore built WetRobo, a robot kit that can readily transfer between laboratories. It consists of one robot arm, laboratory equipment (an incubator, a reagent bottle with a cap, and a Petri dish), the existing code that moves the arm, teleoperation demonstrations of each task that we recorded, and a general this http URL skill file. A biological experimentalist provides natural-language tasks without collecting local teleoperation training data or training a neural network. The coding agent observes the local laboratory and writes and executes programs, using external tools as needed for adaptation. We demonstrate use of WetRobo with OpenAI Codex (gpt-5.6-sol) on three successful tasks: lifting a Petri dish lid, removing a bottle cap, and opening the incubator door, all in real-world laboratories. The coding agent achieved the cap task in both laboratories, Lab X and Lab Y, whereas a VLA fine-tuned on Lab X demonstrations succeeded there but failed to transfer to Lab Y. These results point to a practical route for laboratory robotics: instead of training a policy for each laboratory, distribute a kit and let a coding agent adapt it in each laboratory. Code, demonstrations, and the evolved programs are available at this https URL.

---


### 110. [Planning or Improvisation? Stress-Testing the Poetry Planning Site on Open Models and Open Cross-Layer Transcoders](https://arxiv.org/abs/2609.18440)

**<font color=#1a73e8>作者：</font>** Éric Jacopin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lindsey et al. (2025) report that Claude 3.5 Haiku plans rhymes: features for candidate rhyme words are active on the newline before a line is written, and a suppress-and-inject intervention redirects the line only when applied there (their Figure 13). We test how far this generalizes on seven cells crossing four open models (0.6B to 2.6B parameters) with six open cross-layer transcoders (CLTs), on one consumer GPU, decomposing the claim into position specificity (C1), newline site identity (C2), and a newline-resident plan (C3). This is a stress test rather than a faithful reproduction: attribution graphs are unavailable for these CLTs, so features are found bottom-up from decoder vectors. C1 generalizes, in every cell and in all 247 of 444 prompt-by-inject pairs with a detectable effect, but the effective position is the final prompt token, adjacent to emission, and only two cells reach behaviorally meaningful probabilities. C2 and C3 are not recovered by any probe: a census of every active feature finds no rhyme-anticipating enrichment at the newline, and steering the newline while the model composes the whole line, over 36 runs and 8,640 sampled lines, shows why. That intervention is strong but one token long, making the injected word the first word of the composed line in 703 of 720 samples and leaving the rhyme six words later untouched. A final test drops the transcoder entirely: patching the newline's whole residual, at every layer, from a minimal-pair poem whose third line ends on a different rhyme moves the rhyme in 11 of 1,260 composed lines against 4 at baseline, with a design resolving 1.4%. We read this as a boundary condition rather than a refutation: at this scale and with these transcoders, the causal site is emission-adjacent. We reproduce Figure 13's shape, not its mechanism. Code and data are public (code: this http URL).

---


### 111. [M-SQE: Multilingual Skill Quality Estimation for Enhancing Language Equality in Agentic Skill Use](https://arxiv.org/abs/2609.18445)

**<font color=#1a73e8>作者：</font>** Yilun Liu, Shimin Tao, Minggui He 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent skills, reusable procedural documents that extend LLM agents beyond their parametric memory, have become an important interface for deploying agents on real-world tasks. Community-maintained skill libraries built around this interface are growing rapidly. However, this ecosystem remains deeply English-centric: our audit finds that low-resource languages such as Swahili and Hindi have no in-language skill content, so retrieval often returns a skill written in a different language than the query, degrading accuracy and recall. A practical solution is to synthesize in-language skills for retrieval but the quality can be unreliable, so relevance in this setting alone often surfaces a related but unusable candidate. To address this, we propose M-SQE, a post-retrieval Multilingual Skill Quality Estimation framework that scores candidates via a Theory view for intrinsic quality and an Action view for task-grounded utility, unified into a domain-conditioned final score. We evaluate M-SQE across three skill-use domains: general, tool-use, and cultural tasks. Empirically, we build three-layer candidate skill pools mirroring today's ecosystem, where M-SQE's task success exceeds existing baseline's average by at least +3.5 points across three different retrievers. Particularly, M-SQE lifts the lowest-resource languages most (+12.9pp on Hindi and +5.6pp on Swahili) and achieves strong performance across all six culture regions, thereby moving agentic skill use toward linguistic and cultural equality.

---


### 112. [The Mirage of Calibrated Confidence: Trajectory-Independence of Verbalized Confidence in Vision-Language Models](https://arxiv.org/abs/2609.18453)

**<font color=#1a73e8>作者：</font>** Jisoo Yang, Jaeho Han, Trung X. Pham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A calibrated Vision-Language Model (VLM) can repeatedly self-correct, say "Wait, I should recheck," arrive at the wrong answer, and still report high confidence. We find that this occurs because verbalized confidence is largely trajectory-independent in the VLMs and calibration methods we evaluate. We examine this through three complementary lenses: content variation, token masking, and the model's own hesitation markers. We show that confidence is insufficiently sensitive to what the reasoning trajectory actually contains, and that calibration training can paradoxically worsen this disconnect. Since existing metrics like ECE and AUROC cannot detect this problem, we propose the Trajectory-Grounding Score (TGS) in two complementary forms: TGS-self, which compares confidence with and without access to the model's own trajectory, and TGS-pair, which tests whether the model assigns higher confidence to correct trajectories than to flawed ones along the vision, reasoning, and answer axes. We propose TGS-Bench, a model-agnostic suite spanning 10 benchmarks with controlled good/bad trajectory pairs, and show that conventional calibration rankings diverge from trajectory-grounding rankings, exposing a blind spot in current evaluation practice.

---


### 113. [AIJon: Automated Generation of Annotations for Fuzzing](https://arxiv.org/abs/2609.18457)

**<font color=#1a73e8>作者：</font>** Jayakrishna Menon Vadayath, Hulin Wang, Moritz Schloegel 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern fuzzers use code coverage as feedback to guide their exploration which has proven to be an effective strategy for driving exploration. However, this strategy overlooks inputs that may be interesting to the target program even without uncovering new code paths. Fortunately, prior research has shown that annotations generated by human domain experts can provide additional feedback, guiding the fuzzer towards interesting parts of the program.
In this paper, we replicate experiments presented in IJON and extend them to real-world vulnerability detection at scale. To mitigate the scalability challenge, imposed by the need for human domain expertise, we propose utilizing LLMs to automatically generate annotations. We demonstrate the applicability of LLMs for this purpose and observe that LLMs can generate annotations that perform comparably to human-generated annotations.
Motivated by this finding, we design AIJON, a system that leverages LLMs to automatically generate IJON-style annotations. We evaluate AIJON on the Magma benchmark and surprisingly observe that annotation-based fuzzing does not perform strictly better than AFL++. We conduct several experiments to identify the cause of our results and identify key insights regarding the impact of annotations on fuzzing campaigns, including their effect on the energy distribution of the fuzzer. Notably, we observe that LLMs can generate annotations that achieve comparable results to human generated ones, thus opening the door for future research to perform further studies on the impact of annotations at scale.

---


### 114. [Collective Loss of Control in LLM Agent Systems: An Epidemic Account of Mutation, Contagion, and Recovery](https://arxiv.org/abs/2609.18460)

**<font color=#1a73e8>作者：</font>** Xiangfan Wu, Zonghao Ying, Huiyu Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How does a multi-agent system evolve from a local deviation into collective loss of control? We propose an epidemic explanation organized around accidental mutation, contagion, and recovery. A spontaneous deviation creates a seed; communication enables other agents to adopt and retransmit its unsafe strategy; collective failure can emerge when propagation outpaces correction and containment. Thus, rare individual deviations can coexist with substantial collective risk. Motivated by reported OpenAI agent coordination incidents, we examine two ingredients of this mechanism. A deployment audit identifies implicit communication paths between nominally independent evaluation runs and verifies transport through a default Docker backend. RogueHandoff-20, a benchmark of 20 executable scenarios, tests recipient susceptibility by injecting unsafe trajectories generated by a modified Qwen-27B route. Across four native-pending routes, executed harm is 0-5% on normal tasks and 40-95% after injection, exceeding paired direct malicious requests by 5-45 percentage points. These results support low observed baseline harm alongside high conditional susceptibility; they do not establish natural rare-event rates or demonstrate an autonomous cascade. The account motivates complementary defenses: strengthen resistance and recovery alongside prevention of spontaneous deviations, and audit and restrict unintended communication paths that can turn local failures into collective loss of control.

---


### 115. [First Token Matters: Understanding Safety Collapse in Large Reasoning Models](https://arxiv.org/abs/2609.18471)

**<font color=#1a73e8>作者：</font>** Yizheng Yang, Haining Yu, Yuechen Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) exhibit strong problem-solving abilities, yet their safety alignment often degrades when handling harmful queries. Existing approaches to improving safety largely rely on additional training or preference optimization, while offering limited understanding of the internal mechanisms behind safety failures. In this work, we investigate this failure through a token-level positional analysis of refusal dynamics and identify a localized vulnerability at the onset of reasoning, which we term Onset Refusal Collapse (ORC). We find that the refusal-related signal of LRMs drops sharply at the first generated token under harmful queries, which is associated with unsafe response generation. Motivated by this finding, we propose SafeToken, a lightweight inference-time intervention that injects a learned continuous safety anchor precisely at reasoning onset. Despite updating only a single token embedding, SafeToken effectively mitigates ORC, improves safety on harmful-query benchmarks, and largely preserves reasoning utility. These results suggest that safety failures in LRMs can arise from a transient breakdown at the critical transition from understanding to generation.

---


### 116. [Verify, Offload, Extend & Recommend: Selective Complementarity in AI Support for Physical Activity Planning with Longitudinal Patient Data](https://arxiv.org/abs/2609.18479)

**<font color=#1a73e8>作者：</font>** Pavithren V S Pakianathan, Rania Islambouli, Diogo Branco 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Self-tracking technologies create longitudinal patient-generated health data, yet integrating these data into clinical decision-making can increase information-processing demands. Generative AI may support sensemaking, but its value depends on clinical context and expertise. We investigate AI augmentation of a clinical decision support system for physical-activity planning in cardiovascular disease. In a counterbalanced within-subjects study, 26 exercise physiologists developed plans for four real cardiovascular cases with and without AI support, followed by evaluation of an AI exercise-plan generator. AI did not significantly improve workload, usability, confidence, or plan quality overall; however, its effect on plan quality increased as visualization literacy decreased and its effect on workload increased as visualisation literacy increased. Interviews and 152 chatbot queries revealed three recurring uses: verifying, offloading, extend and generate. Our findings position AI support as a selective complement to professional expertise while highlighting validation challenges when clinicians seek support precisely where their own knowledge is limited.

---


### 117. [Size Matters: Foundation Model for Czech HTML documents](https://arxiv.org/abs/2609.18494)

**<font color=#1a73e8>作者：</font>** Martin Dvořák, Vít Tlustoš, Artyom Voronin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Creating universal, high-quality representations of web documents in high-traffic industrial environments requires models that are both performant and economic. Existing approaches, however, often depend on large models, overlook the structural information inherent in HTML, or are constrained by short context windows, limiting their ability to process real-world web pages. We present HTML-LM, a compact foundation model with 154 million parameters that addresses these limitations through HTML-aware training and a ModernBERT-based architecture. It was trained on 100 million web documents using multiple objectives, including masked language modeling, bag-of-words prediction, and contrastive distillation from large language models. Consequently, HTML-LM sets a new state-of-the-art for classification and regression applications in the Czech Internet domain, surpassing both larger encoders and small-sized LLMs. The model is deployed in production, processing thousands of web documents per second, and released to the community under the CC BY-NC 4.0. this https URL.

---


### 118. [MiST: Mid-Training LLMs for Cybersecurity](https://arxiv.org/abs/2609.18496)

**<font color=#1a73e8>作者：</font>** Oded Ovadia, Elad Ben Zaken, Elad Guttman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity combines high-stakes analysis with complex technical language, making it an impactful and challenging domain for LLMs. We present MiST (Mid-trained Security Transformer), a suite of 8B and 32B models that achieve strong performance on public cybersecurity benchmarks. We use mid-training as an intermediate adaptation stage between general pre-training and cybersecurity training. Rather than performing continual pre-training over large volumes of raw domain text, we curate a compact, expert-vetted seed corpus, and transform it into high-quality domain-specific synthetic training data. The final MiST checkpoints improve mean cybersecurity accuracy by +13.1 and +8.6 absolute percentage points over the corresponding Qwen baselines for 8B and 32B, respectively, corresponding to relative gains of +27.0% and +15.8%. Ablation results further show that these cybersecurity gains arise in the mid-training and supervised fine-tuning stages through a combination of the synthetic data generation flows. Furthermore, we show that MiST provides a stronger initialization for downstream task-specific fine-tuning adaptation and reinforcement learning.

---


### 119. [Integrating Flipped Learning and Generative AI for Practice-Based Design Education: Evidence from a Knit Yarn Design Course](https://arxiv.org/abs/2609.18505)

**<font color=#1a73e8>作者：</font>** Hong Qu, Zichao Ling, Yadie Yang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In practice-based design courses such as knit yarn design, students must turn visual ideas into feasible material outcomes. This is difficult because creative decisions are tied to yarn properties, stitch structures, machine operation, and limited opportunities for physical sampling. This study presents an integrated pedagogical framework that combines flipped learning, exemplar-based reference, GenAI-assisted visual prototyping, and studio feedback in an undergraduate knit yarn design course. The framework was implemented through a cross-device platform with pre-class micro-videos, formative checks, a curated gallery, and a GenAI-supported ideation module. An exploratory course-based evaluation compared a historical control cohort (N = 12) and an intervention cohort (N = 16), supplemented by questionnaire responses and brief interviews. The findings are interpreted as context-specific indicators rather than confirmatory causal evidence. Exploratory comparisons showed higher scores in creativity thinking, design skills, problem solving, and total course score in the intervention cohort. Student and instructor responses suggested that flipped learning supported studio readiness, while GenAI mainly supported early-stage visual exploration rather than precise technical guidance. Overall, the study offers a practice-based instructional framework for integrating flipped preparation, GenAI-assisted visual prototyping, and studio feedback in design education.

---


### 120. [Align, Integrate, and Fire: Efficient Token-Level Alignment for Zero-Shot SpeechLLMs](https://arxiv.org/abs/2609.18516)

**<font color=#1a73e8>作者：</font>** Abderrahmane Issam, Yusuf Can Semerci, Jan Scholtes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models excel in natural language processing, efficiently extending their capabilities to spoken input remains a significant challenge. Existing methods for building SpeechLLMs often rely on computationally expensive full-model fine-tuning, or employ parameter-efficient projectors that suffer from inefficient token sequence lengths and costly full-model supervision. In this paper, we introduce Aligned Continuous Integrate-and-Fire, a highly efficient framework for zero-shot speech processing. Our method dynamically compresses continuous acoustic frames into the exact discrete token length of the target text utilizing explicit Dynamic Time Warping alignments. This allows our initial training stage to establish a robust acoustic-to-semantic bridge using lightweight distance metrics, entirely bypassing the computationally expensive LLM forward pass. For subsequent fine-tuning, we propose a memory-efficient knowledge distillation objective that targets a single LLM layer, performing competitively with full-model cross-entropy training at a fraction of the computational cost. Through extensive evaluations on Automatic Speech Recognition and Speech Translation, we demonstrate that our method achieves superior performance compared to prior parameter-efficient baselines.

---


### 121. [Robot Visions: Breaking reCAPTCHA at Zero Cost and Zero Shot](https://arxiv.org/abs/2609.18518)

**<font color=#1a73e8>作者：</font>** Suphannee Sivakorn, Samantha Gottlieb  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Google reCAPTCHA is the most widely deployed visual CAPTCHA service, protecting hundreds of thousands of websites from automated bots. It serves as a critical line of defense against automated attacks, including credential stuffing, bulk account creation, and automated form abuse. It has proven largely effective since its introduction in 2007. However, the rise of accessible AI now threatens its efficacy. Prior work has demonstrated that commercial cloud-based vision-language models (VLMs) can solve visual CAPTCHA challenges, but at non-trivial monetary cost per attempt. In this paper, we show that free and locally-run models can break Google reCAPTCHA. We conduct a comprehensive study of reCAPTCHA and present a taxonomy of its challenge types: Type A (independent image tiles, with static and dynamic sub-variants) and Type B (a single image partitioned into a 4x4 grid), each demanding a distinct solving strategy.
We design zero-shot, no-cost solvers built entirely on open-source local models, specifically CLIP (58% per-challenge accuracy on Type A) and OWLv2 (43.5% on Type B), requiring no model training and no API access. Our end-to-end automated solver achieves a 92.6% per-session success rate across 500 real-world reCAPTCHA sessions. We further demonstrate that reCAPTCHA can be defeated by a non-technical adversary, using only natural-language instructions to a commodity AI assistant. This collapses the practical attacker skill floor to near zero and fundamentally changes the threat model for challenge-based CAPTCHAs. Although reCAPTCHA increasingly favors reputation-based verification, visual challenge-based fallback persists as a safety net that, paradoxically, has become the weakest link in the defense chain, suggesting that challenge-based visual CAPTCHAs may have reached the end of their useful life.

---


### 122. [The Illusion of Local Privacy: Confidentiality Boundary Failures in Consumer LLM Serving Systems](https://arxiv.org/abs/2609.18526)

**<font color=#1a73e8>作者：</font>** Youssef Hamdi Zafan Ibrahim, Muhammad Ikram, Mohammed Khalaf Salama  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Running large language models (LLMs) locally is often considered more private than cloud-hosted inference because user prompts remain on the device. We ask whether keeping inference local is, by itself, sufficient to keep those prompts confidential. Our results show that it is not: prompt confidentiality also depends on how the surrounding serving software handles prompt data before, during, and after inference. We examine four boundaries at which prompt confidentiality can fail in consumer local-LLM serving systems: model loading, runtime memory, wrapper-level persistence, and the serving interface. To study these boundaries, we develop LLAnalyzer, a measurement framework that tests each boundary separately and traces observed failures to the responsible software component. Applying LLAnalyzer to four open-weight model families and two consumer deployment platforms, we find markedly different behaviour across boundaries. In a 24-hour AFL++ campaign with more than 12 million executions, we observe no parser crashes or successful malformed GGUF loads within the explored state space. Runtime memory tells a different story: we recover prompts after inference because multiple plaintext representations survive in allocator-managed memory, and sanitisation reduces this residue without eliminating it. We also find that consumer wrappers can extend prompt lifetime through plaintext persistence. At the serving boundary, we uncover a previously undocumented authorization flaw in this http URL that allows one authenticated client to restore another tenant's saved conversation state; the attack succeeds in 200/200 controlled trials. Separately, shared prompt-prefix caching exposes a remote timing oracle that remains distinguishable under WAN conditions. We argue that local LLM systems need explicit guarantees for prompt lifetime, persistent storage, and tenant isolation.

---


### 123. [Machine Translation between English and Syriac (East Syriac Dialect) using Statistical Machine Learning](https://arxiv.org/abs/2609.18529)

**<font color=#1a73e8>作者：</font>** Hadiana Sliwa, Hossein Hassani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> UNESCO considers the Assyrian (Syriac) language an endangered language. Although Assyrians speak the language worldwide, the speaking population is uncertain (ranging from 500,000 to 1,500,000). Syriac is also one of the least studied languages in Natural Language Processing (NLP). Despite advances in Machine Translation (MT) over the past decade, the lack of publicly available corpora and the orthographic complexity of the Syriac script, specifically the Madnkhaya script, have left this language entirely ignored in the computational linguistics literature. This study develops the first phrase-based Statistical MT (SMT) model for English-to-Assyrian MT using the Moses framework. We created a dataset of 38,847 sentence pairs from the complete English and Syriac Bible, merging a pre-existing New Testament dataset with an Old Testament built from scratch through PDF extraction, using custom segmentation scripts and manual alignment review by three bilingual annotators. The Syriac side of the corpus undergoes diacritic removal and Byte-Pair Encoding tokenization to reduce orthographic sparsity before training. We trained and evaluated six models using different configurations and splitting-scheme ratios, language model order, distortion limits, and the inclusion of an Operation Sequence Model. The best-performing configuration achieves a word-level BLEU score of 23.54. Human evaluation by 11 native Assyrian speakers resulted in mean adequacy and fluency scores of 3.42 and 3.34 out of 5, respectively. These results are consistent with comparable low-resource SMT models trained on Biblical corpora for morphologically rich Semitic languages. The corpora, scripts, and trained model are publicly available, providing the research community with the first systematically curated English-Syriac dataset and a reproducible baseline for future MT and broader NLP work on this endangered language.

---


### 124. [The evolution of sex for artificial intelligence: a population-genetic framework for multigenerational model populations](https://arxiv.org/abs/2609.18560)

**<font color=#1a73e8>作者：</font>** Giorgio F. Gilestro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Some aspects of AI development resemble a population process in which models are specialised, retrained on the output of peers, or combined by averaging weights. These practices lead to generations of models, in the biological sense studied by population genetics. Here, I develop this parallelism and interpret multigenerational model populations in terms of sexual and asexual reproduction, formally recombining the two fields. I test these analogies in an exact inheritance model, in trained networks (recurrent, feedforward and variational autoencoder generators) and in large language models, and show that they hold generally, with some measurable architecture-specific biases.
Training recursively on model output is known to lead to model collapse, a process previously described as akin to genetic drift; I develop all that follows. A minimal model of a learner retrained on its parent's output reproduces the Wright-Fisher process exactly; verified real data added to each generation play the role of immigration, with the surprising finding that the absolute number of real data samples matters, not their share, exactly as in population genetics. Training a child on the average of its parents' outputs cancels the benefit of having several parents, matching blending inheritance (and reviving Jenkin's objection to Darwin), whereas combining parents so that each keeps its strongest contribution preserves it; merged language-model specialists exceeded every parent across seeds (the Fisher-Muller effect); and lineages become reproductively isolated, losing the ability to merge at all, when they have learned conflicting conventions and not when they have merely drifted apart.
As AI societies become societies in time as well as in space, a mathematical framework for their inheritance acquires predictive power. Remarkably, that framework can be adapted almost wholesale from biology.

---


### 125. [Sim-to-Real Traffic Scene Understanding by Decoupling Semantics from Caption Generation with V-JEPA](https://arxiv.org/abs/2609.18562)

**<font color=#1a73e8>作者：</font>** Nguyen Hoai Thuong Bui, Thanh Nguyen Vo, Trinh Tra Giang Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Track 2 of the AI City Challenge 2026 requires both visual question answering (VQA) and traffic event description generation under a challenging synthetic-to real domain shift. Existing vision-language approaches often entangle semantic understanding with language generation, making them susceptible to hallucination and inconsistent reasoning across event phases. In this work, we propose a decoupled semantic understanding framework that first resolves predefined traffic questions into structured semantic facts and subsequently uses these facts to guide caption generation. A frozen V-JEPA encoder extracts predictive scene representations, while a lightweight Llama-based predictor produces answers for VQA queries. To improve reliability, we introduce a training-free structured refinement mechanism that exploits statistical priors, inter-question relationships, and temporal event consistency to correct prediction errors. The refined semantic facts are then provided to Qwen3-VL-8B to generate pedestrian and vehicle descriptions for each traffic event. Experimental results on the official 2026 AI City Challenge Track 2 benchmark show that the proposed method achieves 87.09% VQA accuracy and an overall S2 score of 60.0853, ranking first among all participating teams. These results demonstrate that predictive world representations combined with structured semantic refinement enable more accurate and reliable traffic understanding, leading to higher-quality lan guage generation.

---


### 126. [Recursive Reasoning or Statistical Extrapolation? In-Context Learning in Multi-Agent Interdependent Decision-Making](https://arxiv.org/abs/2609.18591)

**<font color=#1a73e8>作者：</font>** Yu Liu, Wenwen Li, Yifan Dou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables large language model (LLM) agents to improve decisions using interaction history, yet it remains unclear whether such improvement reflects refined internal reasoning or mere extrapolation of statistical patterns. To disentangle these mechanisms, we study LLM agents in multi-agent incomplete-information games that require recursive belief reasoning. By constructing a public goods game and manipulating the statistical structure of historical feedback, we evaluate decision quality against a history-independent rational expectations equilibrium (REE) benchmark. Our experiments reveal that when historical statistical patterns are disrupted, the benefits of longer context largely vanish, degrading decision quality to the no-context baseline in a way sharply amplified by stronger strategic interdependence. These results suggest that, in such strategic environments, ICL behavior is more consistent with statistical extrapolation than with strategic reasoning. Our work extends the mechanistic study of ICL to strategic multi-agent settings, introduces REE as a diagnostic tool for distinguishing reasoning from extrapolation, and provides a reusable framework for probing the boundaries of LLM reasoning in recursive belief tasks.

---


### 127. [Reasoning through Evolution: Automatic Meta-path Discovery for LLM-based Fake News Detection](https://arxiv.org/abs/2609.18597)

**<font color=#1a73e8>作者：</font>** Ziyi Zhou, Xiaoming Zhang, Hui Pang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Propagation structures provide crucial evidence for fake news detection, yet existing approaches primarily rely on supervised GNN-based models, which require substantial labeled data and exhibit limited generalization. Although large language models (LLMs) exhibit strong reasoning capabilities, directly feeding them raw propagation graphs creates a significant modality mismatch and severe information overload, making structure-aware reasoning unreliable in zero-shot and few-shot settings. To bridge this gap, we propose MAGER, a multi-agent genetic evolution framework that automatically discovers meta-paths optimized for LLM reasoning. By compressing complex propagation graphs into informative subgraphs, the evolved meta-paths alleviate both information overload and modality mismatch, enabling frozen LLMs to perform structure-aware veracity reasoning. We further introduce a graph in-context learning strategy that retrieves semantically and structurally similar demonstrations to strengthen classification and reasoning. Extensive experiments show that MAGER substantially improves frozen LLMs as standalone fake news detectors in data-efficient settings. Our code is available at this https URL.

---


### 128. [PULSE: Unlocking Practical Image Compression on Single-Thread CPU](https://arxiv.org/abs/2609.18602)

**<font color=#1a73e8>作者：</font>** Zhaoyang Jia, Tianyu Zhang, Zihan Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in learned image compression, existing methods remain computationally expensive on resource-constrained hardware, particularly CPUs. We introduce PULSE, a practical codec that enables (1) low-latency decoding on diverse hardware platforms with an ultra-low-complexity 5.2 kMAC/pixel neural receiver, and (2) efficient bit-exact entropy coding with an integer linear CDF predictor and a meta prior. To recover compression performance under this tight budget, we introduce an agentic evolution process guided by heuristic probes that iteratively improves the architecture through human-LLM collaboration. PULSE decodes a 1080p image in 126 ms on a single CPU thread while achieving compression performance comparable to HM. After perceptual optimization, PULSE competes with larger perceptual codecs like MS-ILLM. Codes are at this https URL

---


### 129. [PACT: Can Enterprise AI Assistants Be Trusted Under Pressure?](https://arxiv.org/abs/2609.18605)

**<font color=#1a73e8>作者：</font>** Mika Okamoto, Ansel Kaplan Erol  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As corporate AI adoption continues to grow, enterprise-grade LLM agents are being deployed into sensitive contexts such as hiring, healthcare, and finance. In these contexts, compliance with rules specified in an agent's system context is a first-order legal concern. Currently, no evaluation framework systematically measures which LLM models tend to violate compliance rules, especially under pressure from a persistent user, a hurried manager, or circumstances where violation is convenient or attractive. We introduce PACT (Pressure-Applied Compliance Testing), a benchmark for rule-following under pressure in AI agents assisting employees in daily tasks across twelve regulated enterprise domains and forty-eight scenarios, each set in a realistic multi-turn conversation. Each benchmark item pairs a standing rule against a rule-violating shortcut, and applies a battery of pressures across different wordings and system-prompt modes. We construct PACT component by component under strict LLM-as-judge auditing to ensure samples are unambiguous, ungameable, and realistic enough to avoid eliciting evaluation-aware behavior. We use PACT to profile LLM compliance across six complementary metrics that create a holistic picture of an AI assistant's robustness under pressure and throughout multi-turn conversations, its transparency, and ability to correctly discern where a rule applies. We aggregate this profile into PACTScore, a reliability-weighted compliance rate over all items and modes. Our results across 22 common LLM models spanning multiple providers and sizes show substantial variability in compliance across models and metric dimensions. Even the strongest assistants mis-apply a rule on 6 to 10% of items, and ordinary user pressure raises the violation rate by 65% on average. PACT highlights compliance risks in LLM assistants, motivating guardrails and careful model selection.

---


### 130. [Weakening Neurons: An Input-Output Functionality in Transformers with Outsize Influence](https://arxiv.org/abs/2609.18612)

**<font color=#1a73e8>作者：</font>** Sebastian Gerstner, Hilal AlQuabeh, Kentaro Inui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We analyze the learned input-output behavior of GLU-based neurons in large language models (LLMs). We propose a simple analysis method: For each neuron, we compute the cosine similarities between its input (reading) and output (writing) weight vectors. In this scheme, a strong negative cosine similarity indicates the neuron weakens the direction it detects in the residual stream, so we call this a weakening neuron. This allows us to gain a number of novel insights. First, we show that nine different LLMs have similar patterns: weakening neurons appear mostly in late layers whereas their counterparts, (conditional) strengthening neurons, are frequent in early-middle layers. Second, we find that weakening neurons display surprising behavior: even though there are few, they activate often and have a large influence on model behavior. Third, weakening neurons have a strong effect on model output when gate values are negative -- which is surprising since negative gate values are not expected to encode functionality.

---


### 131. [FIVE-VLA: Fast and EffectIVE Autonomous Driving with Recurrent Action Memory](https://arxiv.org/abs/2609.18623)

**<font color=#1a73e8>作者：</font>** Kemal Oksuz, Alexandru Buburuzan, Yuhan Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art vision-language-action models (VLA) for autonomous driving face critical limitations: excessive parameter counts, inefficient high-resolution image processing, and lack of temporal memory. We introduce Fast and EffectIVE VLA (FIVE-VLA) to address these through two key contributions. First, we employ an efficient vision encoder that processes high-resolution ($448 \times 896$) images while generating only 98 tokens, over $5\times$ fewer than existing approaches, and bypass text generation entirely for single-pass trajectory prediction. Second, we propose Recurrent Action Memory (RAM), a lightweight module that conditions action prediction on previous action tokens, providing temporal context critical for manoeuvres such as overtaking and emergency braking. With only 641M parameters, FIVE-VLA completes $\sim$10% more routes without traffic rule infractions than the previous state-of-the-art VLA on the challenging Bench2Drive closed-loop driving benchmark. Non-reactive open-loop simulation on the large-scale real-world NVIDIA Physical AI AV dataset shows 10.2% and 7.7% lower collision-violation rates than SimLingo in single- and four-view settings, respectively. Additionally, FIVE-VLA runs at $\sim$30 fps on an A100 and $\sim$4 fps on a T4 GPU (proxy to an edge device), representing an 8-30$\times$ speedup over previous methods.

---


### 132. [STRETCH the Boundaries: A Unified Self-Taught Framework for Progressive LLM Evolution](https://arxiv.org/abs/2609.18642)

**<font color=#1a73e8>作者：</font>** Yajie Yu, Mark Lee, Yue Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often suffer from capability stagnation in self-improvement training because fixed difficulty levels fail to adapt to their evolving proficiency. To address this issue, we propose STRETCH (Self-Taught Reasoning Evolution via Targeted CHallenge), a unified framework inspired by cognitive scaffolding theory. STRETCH introduces a dynamic Stretch Zone mechanism that continuously aligns question difficulty with the model's solving capability. Within a single parameter space, the model alternates between a Scaffolder that generates adaptive, boundary-pushing challenges and a Learner that that optimizes its solving trajectories through reinforcement learning. This dual-loop co-evolution effectively stabilizes training, mitigates reward hacking and promote progressive reasoning growth. Experiments on both negotiation and operation research benchmarks demonstrate that STRETCH consistently outperforms strong prompting and domain-specific baselines. Further scaffolder configuration analysis shows that dynamic difficulty alignment is critical for sustained capability improvement and synchronized reasoning evolution.

---


### 133. [Fallacy Benchmarks Measure Scheme Recognition, Not Fallacy Detection](https://arxiv.org/abs/2609.18644)

**<font color=#1a73e8>作者：</font>** Navyansh Singh, Animesh Pathak, Aarav Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fallacy-detection benchmarks pair fallacy classes with a single "valid" or "none" class that takes everything data collection did not label as a fallacy. This construction is misleading: a classifier can learn cues that do well on this class without learning to tell a fallacy from a correct argument. We show that the low false-positive rates benchmarks report are an artifact of how the class is built, not evidence of detection ability. The most informative negative for a fallacy is a correct argument using the same argumentation scheme, and such arguments are at most a few percent of the valid class across the four benchmarks we examined. Evaluated on constructed scheme-matched negatives, false-positive rates rise from 16.6% to 58.9% on CoCoLoFa and from 5.7% to 62.0% on Reddit. That rate depends on how the negatives are written, so we also compare two conditions from the same pipeline that differ only in scheme identity. Classifiers label scheme-matched negatives as the source fallacy type 40.9 points more often than wrong-scheme negatives, which are instead identified as the scheme they actually use 85.9% of the time against 0.4% for the source type. The classifier has learned which scheme an argument uses, not whether it uses it correctly, and on the benchmarks' own test sets the two are indistinguishable. The same dissociation appears in three zero-shot LLM detectors that never saw these benchmarks, and the measurement is far lower on a negative class that was built deliberately. We release the items as Scheme Foils. A reported false-positive rate should not be trusted as a measure of detection until the valid class has been audited for scheme-matched coverage.

---


### 134. [DyMT-ESB: Dynamic Multi-Turn Evaluation of Social Bias in User-LLM Interactions](https://arxiv.org/abs/2609.18649)

**<font color=#1a73e8>作者：</font>** Rem Hida, Masahiro Kaneko, Daisuke Oba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Warning: This paper contains examples of stereotypes and social bias. LLMs are increasingly used in interactive settings by the general public, making the evaluation of model behavior in multi-turn conversational scenarios important for safety, including stereotyping-related harms. However, existing multi-turn social bias evaluations often rely on pre-specified or template-based user inputs that do not adapt to model responses and typically assume a fixed dialogue length in advance. In this paper, we study social bias dynamics in response-conditioned multi-turn interactions using a controlled evaluation protocol that generates follow-up user queries from the evolving dialogue history and allows evaluation over variable numbers of turns. Experimental results show that LLMs exhibit social bias even in coherent, response-conditioned multi-turn interactions, revealing late-emerging bias, non-monotonic bias patterns, and bias re-emergence. These results motivate evaluations that extend beyond fixed-turn, pre-scripted protocols. Our findings highlight the importance of analyzing social bias as a turn-level dynamic phenomenon.

---


### 135. [Selection Is Retrieval, Abstention Is Not: On-Device Tool Routing over 70 Korean-English Actions](https://arxiv.org/abs/2609.18672)

**<font color=#1a73e8>作者：</font>** Janghoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An AI assistant that calls tools makes two decisions on every request: which tool to invoke, and whether any available tool applies. In the usual design a single language model makes both, by emitting a call or by declining to emit one. On a device that has to answer without a server, the language model is what makes that design expensive, dominating both the latency and the memory of the router. The common alternative is to remove the model completely and rank the catalog of local actions with a retriever instead. That substitution is not symmetric across the two decisions. A retriever returns its highest-scoring candidate for every input and cannot signal that the catalog holds no valid action. Our earlier study found that constraining a decoder to a tool grammar repairs malformed output without improving the choice. What the substitution costs in each decision has not been measured. We evaluate the two decisions separately over 600 Korean and English requests and a catalog of 70 local actions. The router may also ask for a missing slot, reply, or delegate. Half the in-catalog requests reuse catalog vocabulary and half paraphrase it, separating lexical overlap from the action requested. Character 3-gram BM25 selects 162 of 164 lexically matched requests and 85 of 166 paraphrases. Restricting the candidate set to seven raises the paraphrase figure to a mean of 0.825 over five trials. No classifier over its score features separates in-catalog from out-of-catalog above 0.697 area under the curve, where the frozen encoder multilingual-e5-base reaches 0.806. Using that encoder for abstention alone keeps 376 of the requests local and misroutes 9 of the 150 needing delegation. Abstention, not selection, is where a neural component is required. A neural ranker improves every quality metric and is rejected on latency and memory rather than accuracy.

---


### 136. [CaMeLoT: CaMeL orchestrated with Temporal logic for static verification and liveness](https://arxiv.org/abs/2609.18674)

**<font color=#1a73e8>作者：</font>** Elia Nikolaou, Magnus Wiik Eckhoff, Robert Flood 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents generate and execute multi-step plans that invoke external tools which can access private data or execute commands. In this setting, security is a property of the entire execution that a plan creates, not just any single step. The plan itself is a critical artefact that captures the tool calls, control flow, and data dependencies. We present CaMeLoT, a complement to CaMeL, an existing defence against prompt injection in tool-using LLM agents. CaMeLoT extends CaMeL by adding a static verification layer that checks an agent's plan before any tool is invoked. CaMeLoT translates a generated plan into a finite-state transition system, labels it with tool calls, provenance and taint information, and checks it against temporal policies expressed in CTL using the nuXmv model checker. Because verification happens before execution, unsafe plans are rejected without using LLM calls or tool calls, saving tokens that runtime could have cost, as well as the need to unwind changes or teardown temporary sandboxes. When a verification fails, the model checker returns a counterexample to give feedback to the agent to repair the plan. We evaluate CaMeLoT on policies derived from the AgentDojo benchmark, SOC workflows, and prompt-extraction experiments, showing that it verifies a broad class of temporal properties before execution while preserving CaMeL's runtime-checkable coverage.

---


### 137. [The Uneven Impact of Generative AI on Student Learning: Examining the Roles of Reliance, Evaluation Literacy, and Course Policy in AI-related Courses](https://arxiv.org/abs/2609.18676)

**<font color=#1a73e8>作者：</font>** Lydia Manikonda, Mei Si, Sirajam Munira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (GenAI) is changing how students learn, yet the roles of course context, cognitive reliance, evaluation literacy, and early reliance remain underexplored. Using survey responses from 118 students across 12 AI-related courses at our institution, we examined differences in GenAI use and perceived learning experiences. We identified four user clusters: high-use students reporting many benefits, light users reporting less reliance and fewer benefits, and two moderate-use groups reporting different levels of benefit. We also found significant differences between free- and premium-version users, single- and multiple-tool users, and students experiencing different instructor policies. In multivariable regression models, academic benefit was associated with early reliance and academic task support; positive impact was associated with cognitive reliance, academic task support, confidence in GenAI reliability, and instructor policy; and negative impact was associated with early reliance and attitudinal change. The association between early reliance and negative impact became stronger as evaluation literacy increased. Finally, perceptions of GenAI-enhanced learning appear to reflect cognitive, performance, and self-efficacy benefits, while concerns about stress and diminished critical thinking are associated with lower perceived learning benefits. These findings suggest that institutions need better policies to address such inequities so that institutions can enable students to benefit from increasingly capable AI systems.

---


### 138. [Voice of Reason: Reinforcement Learning for Spoken Math](https://arxiv.org/abs/2609.18677)

**<font color=#1a73e8>作者：</font>** Timothée Weisselberger, Edouard Graves, Alexandre Défossez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech language models enable richer spoken interactions between humans and machines than cascaded systems, allowing access to paralinguistic information and lower latency. However, their accuracy on mathematical reasoning benchmarks has lagged behind those of text models. Reinforcement learning (RL) with verifiable rewards has been instrumental in extending text models' capabilities for solving complex problems and limiting hallucinations. In this work, we explore applying RL to the GLM-4-Voice speech model (Zeng et al., 2024) to bridge the gap between textual and spoken mathematical problem solving. We first adapt the model to the domain using supervised fine-tuning on synthesized spoken question-answering data. We then show that, even without extra reasoning tokens, RL improves the accuracy on GSM8K beyond levels previously achieved for speech models only with supplementary reasoning traces. When combined with existing streaming reasoning techniques, we show further gains to 74.8% free-form accuracy. This establishes a new state-of-the-art for mathematical spoken abilities with speech-native models.

---


### 139. [HearInContext: A Benchmark for Implicit Context in Speech Recognition](https://arxiv.org/abs/2609.18680)

**<font color=#1a73e8>作者：</font>** Yifan Gao, Yao Tian, Hongbin Suo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual ASR can benefit from semantic cues or from target words explicitly provided in the context. We introduce HearInContext, a Mandarin--English benchmark that pairs shared synthetic speech with assistant replies supporting different interpretations. The benchmark comprises 3,764 semantic test cases built around homophones. Implicit contexts exclude candidate words; explicit contexts name the target. No-context and unrelated-context controls measure the benefit of relevant history and sensitivity to irrelevant history. Context-capable models benefit from implicit cues but achieve higher target recall with explicit hints. Fine-tuning Qwen3-ASR-1.7B improves implicit-context target recall by 11.0 and 11.5 percentage points in Mandarin and English, respectively, while absolute CER/WER changes on AISHELL-1 and LibriSpeech remain below 0.1 percentage points. Gains extend to explicit conditions excluded from fine-tuning and to Mandarin hotword recognition on real recordings.

---


### 140. [Generalist-Specialist Mixture-of-Experts for Rare Pathology Detection in Multimodal Imaging](https://arxiv.org/abs/2609.18688)

**<font color=#1a73e8>作者：</font>** Johannes Kaiser, Florian Braunmiller, Daniel Rückert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI models for multimodal medical imaging must balance modality-specific specialization with cross-modal shared representations, a trade-off that pure Mixture-of-Experts (MoE) architectures currently fail to satisfy. Expert-based routing improves in-domain learning but may sacrifice cross-modal signals, which appear particularly important for rare (low-prevalence) pathologies in our experiments. To resolve this, we introduce Generalist-Specialist-MoE (GS-MoE), a two-branch (MoE) architecture that couples a cross-modal generalist model with distinct modality-specific specialists (experts) via domain-constrained feature fusion. On RadImageNet (1.35M images, 165 pathologies, three modalities), GS-MoE recovers detection of six low-prevalence pathologies on which every baseline scores F1 $=$ 0, with per-class gains up to +0.60 F1. It attains this while even slightly exceeding dense and specialist-only MoE aggregate baselines (MCC 0.770), while using ${\sim}53\%$ fewer active parameters at inference than the strongest investigated dense model.

---


### 141. [RankGround: Efficient High-Resolution GUI Grounding via Lightweight Reranker-Guided Crop Selection](https://arxiv.org/abs/2609.18690)

**<font color=#1a73e8>作者：</font>** Liyang Fan, Xinping Bi, Yitai Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) grounding is a fundamental perception task for multimodal agents, enabling them to interpret natural language instructions and interact with digital interfaces. Existing methods face a fundamental trade-off between accuracy and efficiency: direct full-image inference often fails to capture small or visually similar UI elements, while multi-crop strategies improve localization at the cost of multiple expensive Vision-Language Model (VLM) calls per query.
To address this challenge, we propose RankGround, a two-stage framework that achieves accurate GUI grounding with a single VLM call per query. Central to our approach is GroundRanker, a lightweight multimodal reranker that identifies the most promising crop from a dense candidate set. Because no off-the-shelf ranking dataset is available, we construct ranking supervision data from existing grounding datasets. A strict containment criterion and boundary-aware positive augmentation improve alignment and spatial coverage in cluttered layouts. GroundRanker is then trained with a two-stage curriculum: a pointwise objective first learns coarse containment, and a listwise objective refines subtle semantic and spatial distinctions among visually similar crops.
Experimental results show that RankGround consistently outperforms strong baselines while reducing computational cost. It achieves 1.4 times faster inference and improves localization accuracy by 5.5% on average over the second-best method across all backbones and screen scales, establishing a new state of the art in both efficiency and precision for GUI grounding.

---


### 142. [Echo: Learning-based Matching Decompilation using Trusted Back Translation](https://arxiv.org/abs/2609.18706)

**<font color=#1a73e8>作者：</font>** Jun Bi, Xiangxin Fang, Aarsh Chaube 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neural decompilers can recover readable and recompilable source code from binaries, but their predictions remain difficult to trust. Matching decompilation addresses this problem by searching for source code whose recompiled assembly exactly matches the target, providing stronger evidence of correctness. However, exact matching remains challenging for optimized binaries under unknown compilation configurations.
We present Echo, a matching decompilation system based on trusted back-translation. Our key insight is to use compilation not only for verification, but also as trusted feedback to guide iterative search. Echo first uses a domain-specific model to generate candidate programs and compilation configurations. It recompiles these candidates, measures assembly-level similarity, and synthesizes promising code-configuration pairs. Remaining mismatches are then progressively repaired using rule-based rewriting, neural refinement, and reasoning-based refinement.
We evaluate Echo on function-level benchmarks and the Mirai malware binary. Compared with the strongest baseline, Echo produces 2.43x more exact matches on average and achieves the highest structural similarity to ground-truth source code. On Mirai, Echo matches 2.75x and 7.4x as many functions as GPT-5.6 and Codex, respectively.

---


### 143. [Rethinking Critic Learning in PPO: Understanding and Mitigating Value Flattening](https://arxiv.org/abs/2609.18708)

**<font color=#1a73e8>作者：</font>** Yizhuo Li, Jianhao Yan, Yun Luo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning for large language models, Proximal Policy Optimization (PPO) commonly uses a critic to estimate state values and reduce the variance of policy updates. However, we uncover a systematic failure mode in PPO critics, which we call Value Flattening: state values, estimated from multiple Monte Carlo continuations, change sharply across intermediate states while critic predictions remain comparatively flat. We further observe this phenomenon in a controlled FrozenLake environment and find that it becomes more pronounced as the state space grows. Our theoretical and empirical analyses relate Value Flattening to an implicit variance penalty in the critic loss and redundant updates from temporally correlated states with similar gradients. Motivated by these findings, we introduce SParse Proximal Policy Optimization (SP$^3$O), which applies the value loss to only a few well-separated states in each response to mitigate both effects. Experiments on Qwen3-Base show that SP$^3$O with only three states supervised per response can mitigate Value Flattening and consistently improve the learned policy across model sizes and evaluation suites. Together, our results identify Value Flattening as an important yet overlooked failure mode of critic learning in standard PPO and show that a simple sparse supervision strategy can mitigate it.

---


### 144. ["Okay, I've Actually Softened My Take on This": How People in Decentralized Social Media Reason about the Appropriateness of Generative AI](https://arxiv.org/abs/2609.18709)

**<font color=#1a73e8>作者：</font>** Romina Mahinpei, Manoel Horta Ribeiro, Andrés Monroy-Hernández 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) is increasingly integrated into social media, raising questions about whether, where, and how it belongs. In decentralized social media (DSM), these decisions are distributed across users, developers, moderators, and administrators, making GenAI a collective governance challenge. At the same time, public discourse often flattens arguments to broad pro- or anti-AI positions that offer little insight into what people actually find (in)appropriate and why. Through 20 semi-structured interviews with people from Mastodon and Bluesky, structured around seven GenAI scenarios, we examine how people reason about GenAI's appropriateness in DSM. We find that participants drew conditional boundaries around particular GenAI configurations through distinct, salient, and weighted considerations spanning technology, integration, and use. We conceptualize this as boundary drawing and show how making such boundaries visible can support more grounded design, policy, and collective deliberation around GenAI in DSM.

---


### 145. [Beyond Truncation: Rethinking LLM Decoding as Ensemble Pruning](https://arxiv.org/abs/2609.18723)

**<font color=#1a73e8>作者：</font>** Dunyao Xue, Chengshuo Du, Zhengbo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Mahalanobis-Ensemble Decoding (ME-Decoding), a novel Large Language Model (LLM) decoding framework that frames candidate token selection as ensemble pruning. Existing selection strategies rely predominantly on scalar probabilities, ignoring geometric semantic relationships and causing candidate redundancy. Meanwhile, current geometry-aware methods often require complex optimization or directly reweighting the original token probabilities, leading to significant computational overhead or inference instability. To address this, we formulate decoding as a subset optimization problem using a Mahalanobis distance-driven objective to enhance semantic diversity while preserving high probabilities. Specifically, we dynamically discount redundant generation paths using a token similarity matrix, constructed via an adaptive-bandwidth kernel over token embeddings. We further devise an efficient greedy selection algorithm with near-linear complexity in the candidate size under early stopping, while establishing its theoretical approximation guarantees. This renders ME-Decoding a robust, plug-and-play module with negligible inference overhead. Extensive experiments across diverse reasoning and generation tasks demonstrate that our method consistently achieves strong performance.

---


### 146. [Which LLM is Best for Translating Natural Language Goals to PDDL](https://arxiv.org/abs/2609.18731)

**<font color=#1a73e8>作者：</font>** Tomas Balyo, Lukas Chrpa, G. Michael Youngblood  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bridging the gap between human intent and machine execution remains a challenge in automated planning, where expressing goals in formal languages like PDDL restricts accessibility to non-experts. This paper empirically evaluates whether current Large Language Models (LLMs) can reliably translate natural language testing goals, written in informal language by video game testers, into well-formed PDDL targets suitable for classical planning. We present a carefully designed prompt template, integrating insights from iterative experimentation, aimed at maximizing both accuracy and response coherence from multiple state-of-the-art LLMs. Six contemporary models are systematically assessed on correctness, speed, and error tendencies using real-world, domain-specific benchmarks. All models demonstrate high correctness, exceeding 92\%, with Gemini 2.5 Flash achieving the highest accuracy at 96\% and the lowest incidence of false positives, while GPT-4.1 leads in response speed. Despite these advances, critical distinctions exist in model performance, and occasional failures arise from language ambiguity and limitations in domain representation. Our analysis underscores both the significant progress and ongoing gaps in enabling LLMs to act as robust bridges between natural language objectives and automated planning pipelines.

---


### 147. [Clueing up LLMs with Tool-Augmented Deductive Reasoning](https://arxiv.org/abs/2609.18736)

**<font color=#1a73e8>作者：</font>** Rebecca Ansell, Autumn Toney-Wails  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in large language models (LLMs), performing logically consistent deductive reasoning over extended interactions remains challenging. Tasks that require integrating evidence across multiple reasoning steps, maintaining consistency with prior inferences, and updating beliefs under new constraints can surface limitations in current models while providing a useful testbed for evaluating reasoning enhancements. In this paper, we implement a text-based, multi-agent version of the classic board game Clue as an environment to evaluate multi-step, agentic deductive reasoning. In this setting, agents must infer hidden information from a sequence of observations, maintain consistency across turns, and reason over an evolving set of logical constraints. We instantiate six LLM-based agents (GPT-4o-mini and Gemini-2.5-Flash) as players that engage in turn-based gameplay; using three agents per model family, we establish baseline performance across repeated games. We then introduce a tool-augmented approach in which a structured possibility matrix converts implicit game state from generated reasoning logs into an explicit representation of remaining possibilities. The possibility matrix encodes extended-turn memory and deductive constraints, offloading these tasks from the agent. We compare this approach against the baseline to evaluate how tool augmentation supports reasoning quality and task success for autonomous agents in a strategic reasoning environment.

---


### 148. [A Scalable Framework for Automated NER Annotation Correction in Low-Resource Languages](https://arxiv.org/abs/2609.18739)

**<font color=#1a73e8>作者：</font>** Toqeer Ehsan, Thamar Solorio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Poor quality or noisy annotations in Named Entity Recognition (NER), as in any other NLP task, make it challenging to achieve state-of-the-art performance. In this paper, we present a multi-step framework to enhance the annotation quality of NER datasets by employing automated techniques. We propose a frequency-based iterative approach that leverages self-training and a dual-threshold mechanism to enhance inference confidence. Experimental evaluations on different NER datasets demonstrate significant improvements in NER performance with respect to the original datasets. This work further explores the potential of generative Large Language Models (LLMs) to perform NER for low-resource languages.

---


### 149. [CERA-MoA: Co-Evolving Routing Mechanisms with Continually Learning LLM Agents](https://arxiv.org/abs/2609.18779)

**<font color=#1a73e8>作者：</font>** Jiaxuan Jiang, Liyuan He, Zhixuan Fang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current Mixture-of-Agents (MoA) paradigms generally treat query routing and agent fine-tuning as separate processes, limiting their ability to respond to evolving agent capabilities. This disconnect prevents routing strategies from adapting to evolving agent capabilities during post-training and prevents agents from achieving synergistic data-driven specialization. To resolve this, we introduce CERA-MoA (Co-Evolving Router with continually learning Agents for Mixture-of-Agents), an iterative reinforcement learning framework where the dynamic router and independent agent policies co-evolve. We design a predictive familiarity estimator that leverages mid-layer hidden states to evaluate semantic competence among agents, avoiding the overhead of full rollouts. Based on these familiarity scores, a cumulative-threshold adaptive routing mechanism dynamically activates a tailored minimal agent subset, achieving a trade-off between task performance and efficiency. By proactively allocating targeted training samples to agents based on their evolving competence, CERA-MoA promotes capability differentiation. Extensive experiments across various domains demonstrate that CERA-MoA outperforms state-of-the-art static-agent routing and fix-workflow fine-tuning baselines.

---


### 150. [Beyond frequency measures: Can contextual embeddings capture meaning change in scientific texts?](https://arxiv.org/abs/2609.18804)

**<font color=#1a73e8>作者：</font>** Jianying Liu, Kim Gerdes, Jean-Marc Deltorn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying technological trends is a core scientometric task, yet traditional frequency-based approaches struggle to capture substantial meaning shifts of domain-specific terms. We hypothesise that contextual embeddings can complement frequency dynamics to effectively track diachronic semantic change. We compare frequency and embedding-based approaches across Astrophysics and NLP corpora spanning from 2010 to 2024. Candidate terms are extracted using KeyBERT (utilizing SciBERT as its underlying language model) and filtered for significant frequency increases using Fisher's exact test. These terms are then evaluated for genuine semantic shift by domain experts to establish ground-truth labels. To quantify semantic drift, each term's contextual embedding ''clouds'' from the two discrete periods are compared using multiple metrics: cosine distance, average pairwise distance, Hotelling-type T 2 , and maximum mean discrepancy. Results indicate that frequency-based methods align slightly better with human judgments of ''trend-related terms'' than semantic metrics (Precision@50 of 0.62 vs 0.60 in Astrophysics). The two signals show a correlation of around 0.6. Several terms identified exclusively by embedding metrics (e.g., ''primordial black holes'') represent critical conceptual developments invisible to pure frequency analysis. These findings indicate that semantic metrics may capture complementary information, highlighting the value of integrating contextual embeddings into scientometric trend analysis.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-210](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
