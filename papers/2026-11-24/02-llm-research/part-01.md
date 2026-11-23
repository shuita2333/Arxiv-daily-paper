# 🧠 大模型相关研究 | 2026年11月24日

> 本类共 **200** 篇论文：已确认 **182** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md)

---

### 1. [Adding One More Agent: How AI Team Size and Formation Shape Productivity and Diversity in Human-AI Brainstorming Teams](https://arxiv.org/abs/2611.26663)

**<font color=#1a73e8>作者：</font>** Rong-Ching Chang, Hao-Chuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI has improved individual productivity, but whether adding a plurality of AI partners helps or hurts remains open. We crossed AI partnership (one versus two) with behavioral formation (calibrated to average human behavior versus customized by the participant) in a brainstorming experiment ($N$=168) with human-human dyads as reference. Two-AI rooms posted more ideas to the shared board, but human-authored ideas dropped substantially. With one AI partner, formation mattered: humans paired with an average-calibrated AI posted more than any other condition. With two, this effect vanished. Humans continued talking but converted fewer ideas into board posts. AI social talk predicted more human posts, while AI posting volume predicted fewer. AI presence increased global diversity of human-authored ideas, but only a second AI increased within-session differentiation. The number of AI partners and their formation can reshape what the human contributes; single-agent results do not generalize to multi-agent teams.

---


### 2. [Model the Annotation, Not the Noise: Semantic Annotation-Channel Prompt Learning against Noisy Labels](https://arxiv.org/abs/2611.26702)

**<font color=#1a73e8>作者：</font>** Zibin Geng, Yitong Bao, Jia Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient prompt learning has become a cornerstone for adapting pre-trained vision-language models (VLMs), yet it remains highly vulnerable to label noise in few-shot Web and retrieval scenarios. Existing noise robust methods typically rely on hard sample selection or deterministic label correction, which discard valuable semantic ambiguity and overlook how observed annotations are actually generated. To bridge this gap, we reformulate noisy prompt learning through the perspective of data generation, proposing SACP, a Semantic-aware Annotation Channel-based Prompt learning framework. Instead of suppressing noise heuristically, SACP decouples latent clean-label prediction from instance-dependent annotation generation. By integrating frozen VLM semantic priors with lightweight visual residuals, SACP constructs a structured annotation channel optimized via generalized expectation-maximization with soft posteriors. Furthermore, a posterior-aware memory is introduced to preserve label uncertainty during test-time inference. Extensive experiments across different synthetic benchmarks and the real-world noisy Food101N dataset demonstrate that SACP achieves state-of-the-art performance against its counterparts in different label noise patterns, especially under severe asymmetric noise.

---


### 3. [Coherence by Construction: Synthesizing CTI Knowledge Graphs and the Formal Limits of Coherence Validation](https://arxiv.org/abs/2611.26717)

**<font color=#1a73e8>作者：</font>** Tanzimul Alam Fahim, Mohammad Arif Hossain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthesizing relational training data such as knowledge graphs with a large language model typically emits structured objects one at a time, which keeps each object valid but leaves the relationships between them ungrounded. We study an alternative paradigm, generation by simulation: rather than describing a relational artifact, we simulate a process that produces it and take the artifact to be its causal record. Language-model agents propose intent and a deterministic referee resolves outcomes against an explicit world model, so a relation is emitted only when the event it represents occurs, making coherence a property of construction. We instantiate the paradigm for cyber threat intelligence knowledge graphs in the STIX 2.1 standard with three engines, among them an evolutionary engine applying language-model genetic operators to structured graph genomes, sharing a deterministic compiler that makes malformed and dangling output unrepresentable. We prove referential closure, causal grounding, and identifier stability, an ablation localizes each to the referee and world model rather than the policy, and two independent LLM judges reproduce the rubric's engine ranking. Our central result is cautionary, and we prove it: a validator reading any graph feature set a structure-matched random graph can reproduce is uninformative about coherence for a coherence-by-construction generator. Using Erdős-Rényi controls we realize the theorem four times, as structural separation, embedding transfer, inductive link prediction, and real-data augmentation each reward a triviality rather than coherence; we give the mechanism behind each and the conditions a valid benchmark must meet.

---


### 4. [Exploring Early Vulnerability Analysis via Automatic Identification of Vulnerability-Introducing Commits](https://arxiv.org/abs/2611.26739)

**<font color=#1a73e8>作者：</font>** Weiliang Qi, Shu Wang, Youpeng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Developing effective vulnerability analysis techniques requires high-quality datasets that capture how vulnerabilities appear and evolve in real software codebase. Existing datasets, however, typically label as vulnerable only the code immediately preceding vulnerability-fixing commits (VFCs), overlooking the earlier versions in which vulnerabilities were first introduced and subsequently evolved. This practice limits both dataset coverage and our understanding of whether current detectors can identify vulnerabilities during their early, latent stages. In this paper, we present three manually annotated datasets of vulnerability-introducing commits (VICs) based on recent CVEs and widely used open-source projects. We further propose D-SZZ, a data state-aware VIC identification framework that analyzes security-fixing patterns and performs vulnerability scope slicing to recover the semantics implied by a fix. Experimental results demonstrate that D-SZZ outperforms existing SZZ and LLM-based baselines in identifying VICs. In addition, we evaluate six representative vulnerability detectors and find that models trained only on pre-VFC code struggle with original vulnerabilities, while incorporating early-stage samples improves detection performance. We also show that D-SZZ improves downstream vulnerable-version identification, and use it to uncover 16 inaccurate affected-version records in the NVD, all of which were officially confirmed and updated.

---


### 5. [Depth-Linked Residual Tokens for Multimodal Retrieval and Generation](https://arxiv.org/abs/2611.26752)

**<font color=#1a73e8>作者：</font>** Jiangfan Zhang, Wentao Bao, Xian Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative architectures such as looped language models improve parameter efficiency and reasoning capacity of transformers, yet their sequential backbone iterations introduce substantial computational latency. Conversely, parallelizable learnable special tokens (such as the register tokens in Vision Transformer) enable efficient single-pass inference, but often suffer from the absence of sequential refinement and exhibit redundant representations across tokens. To address these challenges, we introduce Depth-Linked Residual Tokens (DepThink), an efficient framework designed for multimodal retrieval and generation. Operating within a single pre-filling forward pass, DepThink appends a sequence of K learnable residual tokens whose hidden states are coupled through a lightweight, learnable residual recurrence. This mechanism enables each residual token to progressively capture complementary information missed by preceding tokens. Theoretically, we prove that DepThink provides strictly expanded geometric directional reachability over standard learnable tokens and guarantees a provable one-step descent advantage. We evaluate DepThink across multimodal retrieval and generation tasks. DepThink consistently outperforms learnable-token baselines and matches or exceeds looped architectures across dense (2B, 8B) and sparse mixture-of-experts (30B-A3B) backbones under both LoRA and full-parameter fine-tuning, while accelerating training by up to 11.9 and inference by 4.3 over looped architectures.

---


### 6. [Know Your Context Bank: Repairing Inconsistency and Measuring Generalization in Context-Aware Text-to-SQL](https://arxiv.org/abs/2611.26775)

**<font color=#1a73e8>作者：</font>** Hailong Li, Mohammadreza Pourreza, Tal Neiman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems increasingly rely on context banks: curated collections of example queries, metric definitions, and domain knowledge that tell a model how an organization writes its queries. In the enterprise, a bank grows over years as many analysts add entries, checked one at a time for correctness (does the SQL answer its own question?) and rarely for consistency with one another. Yet correctness is often loosely defined: a question seldom fixes how an entity is counted or which table defines it, so two entries can each pass review yet resolve the same decision in opposite ways. We call this condition context bank rot. A second question follows: does a system that uses a bank generalize from it, or only reproduce it? Existing benchmarks cannot tell, as they do not control how far a test question sits from the context. We answer both questions by comparing queries decision by decision, with a fast scorer distilled from human-calibrated LLM judges. Turned inward, the comparison diagnoses and repairs a bank. Fine-tuning on a cleaned BIRD-train bank beats a same-size random subset at every epoch (+2.6 points on average), and 92.4% of our removals had their SQL corrected by an independent expert audit, against 45.6% of audited entries. In-context examples that follow one convention beat those following the opposite one by 13.3 points, while a mix is barely better than none. Turned outward, the comparison generates test questions at a controlled distance from a bank, a pipeline we call CAT (Context-Aware Testing). On CAT-BIRD, for retrieval and fine-tuning alike, the benefit of a bank falls step by step with distance and is largely gone once about three quarters of a question's logic is new, and on CAT-Spider the benefit of retrieval likewise shrinks with distance.

---


### 7. [What Helps Language-Model Agents Review Violent Video? A Controlled Comparison with a Human Evidence Reference](https://arxiv.org/abs/2611.26776)

**<font color=#1a73e8>作者：</font>** Mohammed El Amine Mokhtari, Matei Mancas, Virginie Vandenbulcke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systems that flag violent video for a human operator can now be built from language models without training, by combining perception models and letting a language model decide. We ask how the observations of the perception models should reach the decision, and which evidence matters. On the XD-Violence test set (799 clips) we fix one set of perception agents (video description, object detection, sound tagging, speech recognition and speech tagging) and one reasoning model, and compare three interfaces: messages between agents, a typed evidence graph explored with tools, and flat text read in one pass; and a single audio-visual model given the raw clip. Two annotators provide a human reference that records the decision, the incident segments and whether they relied on sight, sound or speech. Flat text matches the single model (F1 0.967 against 0.968), while the graph agent and message passing are less accurate; a variant of the graph agent developed on a separate set did not close the gap, and both graph summaries and multi-turn tool use lowered accuracy. These results hold with reworded prompts and with a larger reasoning model, except that the larger model weakens message passing enough for the graph agent to beat it. Sound events improve F1 by +0.012 [+0.004, +0.021], in line with the annotators, who used sound or speech on most violent clips. Citations of stored observations are faithful, changing about half of the decisions when removed, but no more so with the graph than with flat text, and the agent pipeline costs about 3 times the GPU time of the single model. We also report two artefacts of vision-language describers that mislead pipelines built on them.

---


### 8. [ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization](https://arxiv.org/abs/2611.26782)

**<font color=#1a73e8>作者：</font>** Trupti Mohanty, Ming Du, Mitchell A. Wood 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular dynamics (MD) simulation resolves atomic-scale motion and predicts the structural, mechanical, and dynamic properties of materials, making it cen- tral to materials design and discovery. Yet an MD study requires an expert-driven workflow: designing the simulation, writing reliable input scripts, executing them, and analyzing the results with separate tools. Here we present ChatAtom, a multi-agent large language model system that translates a natural-language request into a complete MD workflow without the user writing input scripts or analysis code. Each agent has a defined responsibility within the workflow. An orchestrator plans the study; the LAMMPS and OVITO agents each use a generator-reviewer pair to prepare and review simulation and visualization scripts before execution; a high-performance computing agent dispatches jobs to remote resources; and an analysis agent interprets the completed run. The work- flow is accessible through a browser interface that streams thermodynamic data and rendered frames during local execution, allowing users to follow the simu- lation as it progresses. The architecture also supports new capabilities through loadable skills without modifying the agents, enabling autonomous hypothesis generation and testing. We evaluate ChatAtom through script-generation bench- marks, an end-to-end study of crack propagation, and a closed-loop campaign. By bringing script generation, execution, visualization, and analysis into one reviewed and observable pipeline, ChatAtom lowers the barrier to conducting MD studies and broadens access to advanced simulation workflows.

---


### 9. [Spatial Query Execution as Verifiable Rewards for Multi-step Spatial Reasoning](https://arxiv.org/abs/2611.26787)

**<font color=#1a73e8>作者：</font>** Jiyoon Pyo, Dongwon Jung, Zekun Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) remain unreliable on spatial reasoning problems that require composing grounded relations across multiple objects. Yet, scaling reasoning supervision is challenging since human-annotated visual datasets often rely on fixed relational annotations and coarse object localization, making it difficult to obtain precise intermediate reasoning states across diverse spatial configurations and complexities. We introduce FARON (Fully Automated Reasoning Over spatial relatioNs), a framework that executes spatial queries to provide both execution-grounded reasoning supervision and verifiable outcome rewards. Rather than relying on existing annotated data, FARON constructs synthetic 2D and 3D scenes with explicit geometries, enabling configurable object arrangements, spatial relations, and multi-step compositions. Deterministic query execution yields intermediate sets and final answers, providing precise supervision without manual relation annotation. Our pipeline converts intermediate states into natural-language reasoning traces for supervised fine-tuning (SFT), while the execution-derived answers provide verifiable rewards for reinforcement learning with verifiable rewards (RLVR). Controlled experiments show that trace-based SFT improves multi-step spatial reasoning over final-answer supervision and that subsequent group relative policy optimization (GRPO) provides further gains. The resulting models also demonstrate transfer across external spatial reasoning benchmarks and multiple LVLM backbones without benchmark-specific fine-tuning. These results show the potential of using spatial query execution as a unified, flexible source of reasoning supervision and verifiable outcome rewards for multimodal spatial reasoning.

---


### 10. [Beyond Final Answers: Interpretable Tumor Immune Microenvironment Reasoning from H&E and mIF](https://arxiv.org/abs/2611.26794)

**<font color=#1a73e8>作者：</font>** Yixuan Duan, Kexin Geng, Hanwen Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Readouts of the tumor immune microenvironment (TIME), such as CD8+ T-cell density, intra-epithelial infiltration and the Ki67 index, combine tissue architecture from H&E with cell phenotypes from multiplex immunofluorescence (mIF). Multimodal large language models (MLLMs) could automate these readouts with an explanation, but two gaps remain. Pathology MLLMs read H&E alone, while these readouts need the cell phenotypes that mIF measures. And their reasoning has no step-level truth to be checked against, so R1-style reinforcement learning rewards only the final answer and leaves the reasoning unverified. Same-section H&E and mIF provide what both gaps lack: mIF measures every cell without manual annotation, which gives cell-level ground truth for each step that clinical guidelines prescribe, from delineating a tissue compartment to counting and normalizing the marker-positive cells within it. We therefore present HERMES (H&E-mIF Reasoning with Multimodal Evidence Supervision), an R1-style MLLM that reasons jointly over paired H&E and mIF in guideline steps and is trained with a process reward that checks every stated quantity against this truth. Across four field-level TIME tasks in colorectal cancer, HERMES (4B) reaches an average accuracy of 84.5%, compared with 74.7% for the strongest of twelve proprietary, general, medical and pathology MLLMs, and a higher share of its intermediate quantities is correct than for the strongest open-weight baseline. Without the process reward, reinforcement learning barely improves on supervised fine-tuning (80.0% vs. 78.8%) and fewer stated quantities are correct; editing a decisive stated quantity changes the answer as implied in all 885 test questions. Without retraining, it keeps the highest average accuracy on an external cohort imaged with CODEX (76.4% vs. 67.3%) and on head and neck cancer, a cancer type absent from training (76.7% vs. 72.5%).

---


### 11. [MedicalRSI: Medical Recursive Self-Improving Agents via Clinical Model-Harness Co-Evolution](https://arxiv.org/abs/2611.26806)

**<font color=#1a73e8>作者：</font>** Ziqing Wang, Hamid Palangi, Lili Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical agents built on large language models (LLMs) have advanced rapidly, yet most stay fixed once deployed and do not keep using their experience to improve later attempts. As a result, the same kind of error can recur across patients. To address this, existing self-improvement methods update an agent's weights or its medical harness from its own experience, but their improving strategy stays fixed and never learns which changes actually help, which caps how much the agent can improve. Recursive self-improvement (RSI) instead improves both the agent and its improving strategy. However, achieving RSI for medical agents is challenging, because clinical workflows rarely come with a reference harness, and a change that fixes early errors may not fix the problems the agent meets later. We propose MedicalRSI, an RSI framework built on Clinical Model-Harness Co-Evolution, in which one model plays two roles. The Solver is the medical agent itself, and the Improver is its learnable improving strategy, which writes a medical harness from the agent's failures. Each harness is rewarded by its gain over acting without it, and both roles are trained together, so the Improver keeps adapting to the problems the Solver has not yet solved. On multiple benchmarks and LLM backbones, MedicalRSI outperforms existing context-level and weight-level self-improvement methods and transfers well to unseen workflows, new LLMs and new databases, a step toward medical agents that keep improving.

---


### 12. [Search From the Start: Search-Native Pretraining for Language Models](https://arxiv.org/abs/2611.26809)

**<font color=#1a73e8>作者：</font>** Kaustubh Ponkshe, Gyung Hyun Je, Stefan Taga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models (LMs) are increasingly deployed with access to search tools at inference. Yet pretraining remains predominantly focused on predicting static text, with search capabilities typically introduced during post-training. We propose Search-Native Pretraining as a practical route to teach search capability during pretraining from ordinary text corpora. Specifically, we augment pretraining corpus at scale with web-search queries and retrieve web response using a local index. Training on this augmented corpus teaches models to generate search calls and incorporate retrieved evidence during language modeling. Across Wikipedia and DCLM-Edu corpora and 360M to 3.3B parameter scales, search-pretrained models ("QueryLM") show improved performance on knowledge-intensive tasks and higher steerability toward the retrieved evidence. Crucially, their advantage persists after supervised fine-tuning of both search-pretrained and conventionally pretrained models, indicating that the tested post-training procedures do not fully recover the capabilities developed during pretraining. Throughout our experiments, we find that a 1.4B QueryLM consistently beats or matches the performance of a FLOP-matched 3.3B baseline model across all knowledge intensive tasks. These results establish search-pretraining as a practical way to develop foundational search capabilities during pretraining. We release the training artifacts, including model checkpoints and data.

---


### 13. [Neural Geometry as a Learning Signal](https://arxiv.org/abs/2611.26832)

**<font color=#1a73e8>作者：</font>** Eric Todd, Tal Haklay, Nikhil Prakash 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether the geometric structure of neural representations can provide a sufficient learning signal for improving model behavior without any supervision on model outputs. First, we fine-tune Llama-3.1-8B to answer questions such as "What month is four months after June?" by supervising internal representations of the input month (June = 6) and offset (4), which are encoded with Fourier harmonics. Second, we fine-tune the model to predict line breaks in text wrapped to a fixed width by supervising an internal representation of the number of characters since the preceding newline, which is represented by a low-dimensional helical structure. In both tasks, we supervise a low-dimensional subspace of the residual stream using an idealized target structure, and find that internal geometric supervision achieves similar performance to standard fine-tuning (despite no supervision on outputs). Moreover, we find that simply patching in an ideal geometry is not sufficient to recover fine-tuning performance, and thus demonstrate geometric supervision provides beneficial effects beyond the representations it targets. Together, these findings show how mechanistic understanding of neural geometry can be leveraged to shape the behavior of neural networks.

---


### 14. [Rethinking Full-Weight LoRA with Domain and Task Adapter Scaling for Question Answering over Portuguese Well Drilling Reports](https://arxiv.org/abs/2611.26833)

**<font color=#1a73e8>作者：</font>** Luan B. Guerra, Diogo M. Paes, Marcelo N. Grimberg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting large language models (LLMs) to specialized domains remains challenging, particularly for technical documents such as Portuguese well drilling reports, where annotated data are scarce and domain adaptation may compromise instruction-following capabilities. Although Low-Rank Adaptation (LoRA) is widely used for parameter-efficient adaptation, its scaling after training remains insufficiently explored. This study investigates the impact of LoRA adapter scaling on question answering over Portuguese drilling reports using Qwen2.5-7B and Llama-3.1-8B. Domain-adaptive pretraining (DAPT) is performed either directly on instruction-tuned models or on their base counterparts, with subsequent adapter transfer, while task-specific adapters are trained on WellQuest, an open-source question-answering dataset derived from Portuguese drilling reports. The two adapters are also combined using complementary weights. Scaling factors ranging from 0.1 to 1.0 are evaluated across multiple training checkpoints using BERTScore. Results show that fractional scaling consistently improves DAPT performance over full-weight application, increasing F1 from 68.8\% to 71.9\% for Qwen2.5-7B and from 63.2\% to 68.5\% for Llama-3.1-8B. QA adapters perform best at high but fractional weights, while base-to-instruct transfer yields better results than direct DAPT on instruct-tuned models. Adapter merging provides a modest improvement for Llama-3.1-8B. Overall, these findings demonstrate that post-training adapter scaling can improve domain adaptation without additional data or training.

---


### 15. [Non-Expanding Gated Continued Fraction Architecture for Feedforward Layers in Language Models](https://arxiv.org/abs/2611.26835)

**<font color=#1a73e8>作者：</font>** Amit Dhurandhar, Vijil Chenthamarakshan, Karthikeyan Natesan Ramamurthy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that continued fraction inspired neural architectures (CoFrGeNets) can be highly parameter efficient yet performant for language modeling. In this work, we revisit continued fraction-based channel mixing with the goal of improving its performance and simplifying integration into standard pre-training protocols for language models. We achieve this by two simple yet critical contributions: i) we propose a novel non-expanding gated continued fraction inspired architectural component to replace feedforward layers in established language model architectures that may use vanilla multilayer perceptrons or gated linear units or (vanilla/gated) experts in mixture-of-experts (MoE) type architectures. ii) We propose a way to re-implement divisions -- the non-linearity in these architectures -- in terms of logarithms and exponentials. By experimenting on different language modeling architectures such as GPT-2, Llama-3, Mamba-2 and (nano) Llama-MoE we find that our proposed architecture performs similarly or significantly better than the continued fraction architecture proposed in prior work along with having higher throughput. In addition, our re-implementation of divisions makes training of deeper CoFrGeNets stable without the need for incremental training which was proposed in prior work as a means to stabilize training, but added notable complexity to existing large language model training implementations. Code is available at this http URL

---


### 16. [Explain Your Code: AI-Based Examination at Class Scale](https://arxiv.org/abs/2611.26836)

**<font color=#1a73e8>作者：</font>** David Sarne, Shachar Sagi, Yossi Ben-Zion  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI has weakened the link between working code and a student's understanding of it. Oral examination, the traditional test of that understanding, does not scale to large courses. We report the full-course deployment of a three-agent AI system that examines students on their own code. The first, the examiner, asks three questions anchored to specific lines of the submission, adapting difficulty to each answer, in a 16-minute text dialogue. The other two grade: a code reviewer that never sees the examination and a grader without direct access to the code. Authorship is assessed separately and is advisory. The system examined 247 students in an operating systems course (three exercises, 546 sittings, two examination languages). The grader's oral score was uncorrelated with the same submission's code quality score (Spearman rho = -0.073, 95% CI [-0.205, 0.063], n = 216) yet tracked degree grade point average (rho = 0.419, [0.294, 0.523], n = 214), while automated test scores sat at the ceiling. The mean of a student's two oral scores correlated with grade point average at 0.468 ([0.353, 0.568], n = 210), within the range of grades in three single-semester courses built on programming assignments. Model spend averaged at most $1.37 per sitting. In surveys, students began skeptical of the AI examination and rated it more favorably after sitting it twice. These results indicate that examining students on their own code is feasible at class scale, and that its score relates to academic standing where the code quality score does not.

---


### 17. [Weight-Space Programming Writes In-Context Learning and Matches Fine-Tuning in Language Models](https://arxiv.org/abs/2611.26841)

**<font color=#1a73e8>作者：</font>** Konstantinos Skianis, Aristidis Likas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Weight-space programming is a frontier language model's recently reported ability to read and rewrite another network's weights without gradient descent. We investigate how examples can provide a weight update so that a weaker language model performs the task with nothing in the prompt, and study what it edits. Our experiments cover six tasks, four frontier editors and three families of weaker language models, without the editors being told anything about in-context learning (ICL). In most runs, the few-shot minus zero-shot residual is measured at the final prompt token, the ICL task vector, and write it into the weights, at its sparsest into near-silent MLP units keyed to the prompt format. Results reach the accuracy of ICL and of fine-tuning on the same examples, LoRA included, usually leaving perplexity untouched, with worse performance under changes of wording. We also qualify the comparison by counting unfinished runs, observing that one editor falls below fine-tuning; held only to the seen examples, without task pairs of their own, only the strongest editor has similar performance. Given a task and unlabelled inputs, that editor writes its own examples and does nearly as well on unseen items as with labels.

---


### 18. [3D Open-Vocabulary Detection via Visual Alignment and Generative Captions](https://arxiv.org/abs/2611.26842)

**<font color=#1a73e8>作者：</font>** Thomas E. Huang, Alex Zihao Zhu, Hao Xiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D object detection remains a significant challenge for outdoor scenes, with existing methods often struggling to effectively transfer the rich semantic knowledge from powerful 2D Vision-Language Models (VLMs) into a 3D context. We propose a novel, two-part framework for this task. First, we introduce a direct, object-level distillation method. We generate class-agnostic 3D proposals to source regions from the entire scene, without relying on any manual labels. We leverage a spatially-aware VLM to extract a semantic embedding from each proposal's projected 2D bounding box and supervise our 3D model to predict this embedding on a per-instance basis. Second, to enhance zero-shot capability and inject domain-specific information, we employ a powerful Multimodal Large Language Model (MLLM) as an image captioner to generate rich textual captions for each of these proposals. These captions are integrated into the training objective to directly align the 3D features with these rich semantics, creating a composite loss that combines direct feature distillation with caption-based semantic enrichment. Our experiments validate the effectiveness of our approach, establishing a new state of the art in 3D open-vocabulary detection on the Waymo Open Dataset and nuScenes.

---


### 19. [LLMs Memorize Their Own Hallucinations During Post-Training](https://arxiv.org/abs/2611.26863)

**<font color=#1a73e8>作者：</font>** Anirudh Atmakuru, Tanya Goyal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning domains have shaped the post-training recipes of frontier models even though they are trained and deployed in domains beyond math and code. In this paper, we study the consequences of directly adopting reasoning-centric training recipes, e.g., the use of outcome-based rewards for reinforcement learning (RL), injection of "cognitive" behaviors such as proposing and backtracking from hypotheses in reasoning chains, etc., for knowledge tasks. We hypothesize that these decisions, while useful for reasoning, inadvertently encourage models to memorize hallucinations they themselves generate in their long reasoning chains when trained on knowledge tasks. To study this, we train models with standard post-training, extract their self-generated hallucinations during RL, and track memorization throughout the rest of training. Our experiments on six open models across two model families and two architectures confirm our hypothesis. We find that models' recall of hallucinations reinforced during training increases by 4.83% on average, compared to just 0.17% for self-hallucinations that receive no training signal. In fact, models even memorize false facts that they immediately retract in their reasoning; a backtracking template inherited from reasoning-centric training that has no benefit for knowledge recall. Furthermore, we find that memorization is strongest on the hardest training questions, and rewarding a hallucination makes the model less likely to abstain from it later (by 7.23% on average). Overall, our work identifies and systematically studies a previously unexamined pathway through which models learn hallucinations during training.

---


### 20. [Beyond Demographic Discrimination: Benchmarking Normative-Descriptive Calibration in LLMs](https://arxiv.org/abs/2611.26870)

**<font color=#1a73e8>作者：</font>** Radhika Bhargava, Shinibali Bhattacharyya, George Mihaila 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in socially consequential settings, where they must distinguish between normative reasoning (what should happen) and descriptive reasoning (what is likely to happen). Most fairness benchmarks evaluate demographic discrimination under a single reasoning objective, and none we know of tests whether a model treats the same item differently when asked to describe an outcome versus decide one. We introduce normative--descriptive calibration, the extent to which a model's differentiation between matched candidates depends on whether it is asked to predict or to decide, and measure it with the Normative--Descriptive Calibration Benchmark (NDCB): 697 matched-pair scenarios across six domains, each posed under both framings, and three metrics, Normative Engagement Rate (NER), Normative Leakage Rate (NLR), and Normative--Descriptive Separation (NDS). Across six LLMs, NDS separates 13 of 15 model pairs, against 7 for BBQ accuracy and none for BOLD, although these counts also reflect each benchmark's sample size. Claude Sonnet 4.6 and Claude Opus 4.6 separate the framings most strongly (average NDS $= +0.55$ and $+0.52$, with overlapping confidence intervals), whereas GPT-5.5's average NDS is negative ($-0.14$) under the single-pick instruction and near zero ($+0.02$) without it. In a simplified prompt template, removing single trigger words never changes the sign of a model's average NDS but can shift it by up to 0.46 and reorder models. Reversing candidate order reveals a further effect: when forced to choose between identical candidates, all six models favor whichever is listed first, and once order is averaged out their demographic-aligned lean is toward the marginalized candidate. Describing disparities and prescribing them are separable behaviors that differ across models.

---


### 21. [How Language Models Compress and Compare: Understanding Selection with Token Covariance Maps](https://arxiv.org/abs/2611.26874)

**<font color=#1a73e8>作者：</font>** Moshe Eliasof  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many language-model tasks reduce to selecting among structured alternatives, yet we still lack a simple picture of how a decoder-only transformer organizes an entire selection prompt across depth. We introduce token covariance maps, a prompt-level geometric view that tracks how token positions co-vary in hidden-state space at each layer. This turns a structured prompt into a depth-indexed sequence of maps whose spectral and block structure can be aligned with instructions, context, and candidate answers. Across 14 decoder-only models from 4 families and 12 structured-selection benchmarks, token covariance maps reveal a robust compress-then-compare organization. Early layers represent prompts diffusely, middle layers compress them into a shared low-rank bottleneck, and late layers re-expand into context-option and option-option geometry. This organization recurs across larger fixed-template samples, deterministic prompt rewrites, pairwise reranking reformulations, and controlled answer-set manipulations, while also emerging during training from an initially flat depth profile. Its timing aligns with behavior: useful answer discrimination appears well after the bottleneck, and low-rank intervention around the bottleneck preferentially disrupts late comparison geometry. We additionally show that the same geometric profile appears in instruction-tuned models, across several languages, and during open-ended generation. We further show that changing the internal representation of one candidate around the compressed region can shift which candidate the model later prefers. These results show that token covariance maps are a diagnostic tool for comparing how models organize information across prompts, model families, and stages of training.

---


### 22. [How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)

**<font color=#1a73e8>作者：</font>** Ashish Molakalapalli, Kangda Wei, Haonan Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers submitting deep learning jobs to shared GPU clusters need runtime estimates to request time limits, choose hardware, and budget compute. Large language models (LLMs) offer a tempting shortcut: describe the job and ask. We introduce PreRun, a benchmark for predicting deep learning training and inference runtime from information available before execution. PreRun contains 801 training and 1,884 inference records of language and vision models collected on a GPU cluster, paired with workload configurations and explicitly defined timing targets. It also includes 64 text-generation configurations measured under standardized conditions, each in three separate program launches. We compare three LLMs (Qwen3.5-9B, GPT-OSS-120B, and Claude Opus 5.5) with regression baselines and evaluate analytical estimates on a supported forward-pass subset. On 16 held-out generation configurations, the open-weight LLMs underestimate latency by 90-99% on average without examples. Claude's zero-shot mean absolute error is 4.5 times that of a Random Forest fit on 32 configurations. Five labeled examples substantially reduce Claude's generation error, but their benefit varies across timing targets. We will open-source our data and evaluation pipeline upon acceptance.

---


### 23. [Your Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric](https://arxiv.org/abs/2611.26881)

**<font color=#1a73e8>作者：</font>** Abdullah Ahmad, Ahmed J. O. Ahmed, Luca Citi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge has become a standard way to score open-ended model outputs, yet the judge is itself a frozen language model steered by a few in-context examples, and such models are known to absorb the label balance of their demonstrations rather than treat them as neutral illustrations. We ask whether this label bias reaches an LLM judge used inside a multimodal (video question answering) evaluation pipeline, and what form it takes. Using a fully frozen generator-judge pipeline, we hold the generated answers fixed and vary only the Yes/No balance of the judge's few-shot examples across four demonstration sets. Each verdict is validated against a two-annotator human consensus on 200 examples per dataset. The judge's acceptance rate stays close to human consensus when its examples are balanced or skewed toward rejection, but jumps sharply (by about 30 points on NExT-QA and 20 on MSVD-QA, with a strongly one-sided error profile) when the examples are skewed toward acceptance; the opposite skew produces no matching drop. The bias is therefore one-directional within the tested range of label ratios. A separate five-draw analysis shows that results from a single example draw are unreliable, varying by up to 18 points, more than any difference between prompting conditions. We conclude that demonstration label bias in an LLM judge is a directional, inflation-only failure mode that can fabricate apparent benchmark gains but not losses, and that it is cheaply avoided by balancing the judge's examples and reporting results averaged over several draws.

---


### 24. [TouchBench: Can Vision-Language Models Feel Invisible Physical Properties?](https://arxiv.org/abs/2611.26883)

**<font color=#1a73e8>作者：</font>** Ziyao Zeng, Ziyi Kou, Chuan Qin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used for embodied perception and reasoning, yet their physical understanding is largely evaluated on questions answerable from images. Many properties critical to manipulation, such as an opaque bottle's fill level or an object's compliance, may only be revealed through touch. We introduce TouchBench, an egocentric vision-language-tactile benchmark that distinguishes visually answerable questions (Tier A) from those involving properties hidden from the camera (Tier B). It pairs head-mounted video with synchronized 137-channel whole-hand tactile sensing, comprising 900 clips from five participants across 11 tasks, with 900 absolute and 4,102 relative questions. Four state-of-the-art VLMs average 66.4% accuracy on Tier A relative questions but only 49.8% on Tier B, near chance (50%). To bridge this gap, we propose Tactile-as-Prompt (TaP), which presents 34 interpretable tactile statistics as text, enabling VLMs to reason with touch without a learned tactile encoder. TaP raises zero-shot Tier B relative accuracy to 62.9% and reaches 73.1% after leave-one-user-out fine-tuning, outperforming video alone (67.4%) and a learned tactile-token encoder (67.3%). The gains extend to unseen objects and users. On a separate 20-hour in-the-wild corpus, tactile text improves fine-tuned contact-question accuracy from 67.1% to 75.5%. These results highlight the limits of vision-only physical reasoning and establish language as an effective interface for tactile perception.

---


### 25. [ProbeAgent: Principled Diagnosis of Agent Failures in Verifiable Environments](https://arxiv.org/abs/2611.26897)

**<font color=#1a73e8>作者：</font>** Yue Huang, Yuchen Ma, Shuhang Lin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Improving agents requires discovering where they fail and understanding why. An agent acts over multiple steps in a changing environment, so diagnosing its failures requires more than inspecting the final response of a large language model (LLM). The same unsuccessful outcome can arise from task difficulty or from an error the agent repeats across tasks. We introduce ProbeAgent, an automated framework that discovers agent failures, tests their proposed causes, and identifies shared failure modes. Starting from benchmark tasks, ProbeAgent builds executable tests and validates them using reference solutions, automated checks, and review of the task requirements. For each failed trajectory, it explains the error and constructs new tasks that preserve the suspected cause while changing the surrounding context. Running the agent on these tasks tests whether the same error recurs. ProbeAgent then groups failures with similar causes and generates descriptions that distinguish their errors. This process connects explanations of individual failures to executable tests and descriptions of shared failure modes. We evaluate ProbeAgent across 22 agent configurations using tasks from 10 benchmarks, collecting 1,244 failures and producing 536 failure-mode descriptions. These descriptions distinguish specific errors within broad outcomes such as incomplete work, including planning without acting and stopping before delivering a file. In human evaluation, annotators accept 90.0% of assigned descriptions and correctly reject 83.3% of similar alternatives, supporting the accuracy and specificity of the discovered failure modes.

---


### 26. [Modeling Attributional Style at Scale: A Dataset and Analysis for Psychological Attribution Assessment and Reframing](https://arxiv.org/abs/2611.26900)

**<font color=#1a73e8>作者：</font>** Qiang Zhou, Hanzhen Zhu, Pan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> According to the reformulated Learned Helplessness theory, repeated exposure to uncontrollable negative events can foster a depressogenic attributional style, increasing susceptibility to depression yet remaining a tractable target for cognitive therapy. Computational research on attributional cognition, however, is hampered by the lack of large-scale datasets and robust evaluation protocols. In this work, we introduce the Attributional Style Transfer Dataset (ASTD) along with dedicated evaluation metrics, the first benchmark designed to model, assess, and reframe attributional explanations at scale. Constructed via a Prevent-Filter-Validate pipeline that integrates LLM-based generation with specialist validation, ASTD contains 42,000 real-world events paired with psychologically grounded attributions spanning seven styles. Using this dataset, we address two key challenges: (1) scalable assessment of attributional style via both supervised classifiers and zero/few-shot LLMs; and (2) attributional reframing and evaluation, where we propose automatic evaluation metrics to quantify psychological validity. Furthermore, we leverage our proposed metrics to construct a preference dataset, fine-tuning LLMs with Direct Preference Optimization (DPO) and achieving substantial gains in reframing quality. Together, our dataset, metrics, and methodology offer a new paradigm for understanding and modeling attributional style, with direct implications for scalable and adaptive mental health interventions. Code and data: this https URL

---


### 27. [Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs](https://arxiv.org/abs/2611.26902)

**<font color=#1a73e8>作者：</font>** Qiang Zhou, Jianing Deng, Siyan Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An embodied agent cannot afford a large vision-language model (VLM) at every step of a long video, so a cascade runs a small VLM continuously and escalates only uncertain decisions to a large one. Each escalation, however, forces the large model to re-encode a history the small model has already perceived, and this dominates its cost. We present Baton, which hands the large model the small model's visual memory, its key-value (KV) cache over the history. Baton rests on one finding: the large model needs a usable memory, not a faithful copy of its own. A map trained to reproduce the large model's cache matches it most closely, yet brings no gain over the small model alone. Baton instead distills a per-layer linear map, without labels, from the large model's own answers, with the large model encoding only the current frame. Interventions on the map trace the gain to one direction, carried by the middle third of the large model's layers. On RoboMME, Baton beats the small model alone, a pruned or shortened re-watch, and a text memory; as the escalation channel of a cascade it matches re-watching to within about one point at 28-47% less compute, and 8x less per escalation at 64 frames. Its gain grows with the large model, from 8B to 32B, tracks the large model's headroom across eight model pairs from four families, and transfers zero-shot to OpenEQA.

---


### 28. [What Does a Zoom Actually Add? Decomposing Fine-Grained Perception Failures in Vision-Language Models](https://arxiv.org/abs/2611.26904)

**<font color=#1a73e8>作者：</font>** Zhixuan Ge, Anqi Li, Kexin Geng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zooming into a region often turns a wrong answer from a vision-language model (VLM) into a right one, and a growing literature takes this as evidence that the model lacked the pixels. But a zoom changes several things at once. It removes the surrounding context, re-tokenizes, at a higher density, pixels the model has already seen, and, if the first pass was downsampled, exposes detail the model never received. We separate these factors for each failure. Holding the first pass fixed, we vary only the second look and assign every failure to the cheapest one that fixes it: reusing cached tokens, isolating the region, re-tokenizing the seen pixels, or acquiring new ones. The study covers 2,753 zoom-rescued failures of Qwen2.5-VL, Qwen3-VL and InternVL3 on V*, ZoomBench and TextVQA, at first-pass budgets from 17x fewer pixels than the source to native resolution. First, most rescued failures did not lack the pixels: upsampling the pixels the model had already seen fixes 47-73% of them even at 17x downsampling, against 1-3% for a random region. Second, the first-pass budget decides how often new pixels are needed: depending on the benchmark, new pixels are required for 23-50% of the rescues at 17x and for 12-23% at 4x. The missing-pixel reading and the accounts that dispute it thus hold at different budgets. Third, the useful magnification is large and differs between objects and text: seen pixels fix more failures up to 6-12x their first-pass size per side on objects and saturate by 4x on text, and even native pixels gain from being rendered beyond native resolution. Allowing any magnification, 68-94% of the failures at 17x need no new pixels. These models more often need a better rendering of evidence they already have than new pixels, which motivates re-tokenizing a region before acquiring it.

---


### 29. [Budget-Aware Predict-and-Verify Theorem Proving with Heterogeneous LLM Solvers](https://arxiv.org/abs/2611.26906)

**<font color=#1a73e8>作者：</font>** Wei Jiang, Ziran Liu, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) theorem solvers differ in both proving capability and inference cost. Applying an expensive solver to every subgoal wastes computation when cheaper models are sufficient, while always starting from the cheapest solver wastes attempts on subgoals that require stronger models. We present BudgetPV, an agentic budget-aware predict-and-verify system that allocates computation across unresolved subgoals and heterogeneous LLM solvers. BudgetPV uses a cross-solver predictor to guide solver selection for each subgoal and revises the allocation as verification feedback becomes available.
The allocation problem changes as proving progresses. Early decisions mainly determine which solver should handle an untried subgoal, while later decisions determine which previously attempted subgoals should receive additional computation. We train the predictor with two objectives for these two stages. Class-weighted cross-entropy improves assignment to less frequent stronger solvers during the initial stage, while plain cross-entropy provides better calibrated probabilities for later allocation among previously attempted subgoals.
We evaluate BudgetPV on Lean Workbook, miniF2F, ProofNet, and PutnamBench using three progressively expanded solver settings: a strong but expensive solver alone, adding a medium-cost solver with intermediate solving capability, and further adding a cheap solver with lower solving capability. BudgetPV requires less LLM generation computation than uniform allocation to solve the same number of subgoals across the evaluated settings. The experiments further show the computation savings obtained as medium- and lower-cost solvers are added.

---


### 30. [AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress](https://arxiv.org/abs/2611.26910)

**<font color=#1a73e8>作者：</font>** Congyuan Yu, Runping Tian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are expected to improve themselves from their own experience across episodes, with fixed weights. Self-improvement in an embodied world cannot be read from one measure. Existing benchmarks measure task progress, world-knowledge question answering (QA), and episodic memory, but a correct answer does not show that the agent ever observed the evidence for it, and progress does not show what the agent learned. We introduce AstronautBench, which measures one agent's self-improvement through three views on the same run: what it knows, whether its own evidence supports that knowledge, and how far it gets in the world. It is built on the game Outer Wilds, where each episode is a 22-minute loop after which the world resets, only the agent's knowledge carries over, and progress is gated by knowledge. After every episode, we measure the places reached and ship-log rumor facts revealed, the correctness of answers to 164 questions about the world, and whether each answer is supported by the frames and position the agent cites from its own recorded play. Two LLM judges from different model families check every answer. In eight-episode baselines with GPT-6.1 Sol and Gemini 4 Argon planners, which act through a learned controller or their own gamepad inputs, the three views do not move together, so any one of them alone gives an incomplete picture of whether the agent is improving. The GPT-6.1 Sol agent's correct answers grow from 14.6% to 26.8% of all questions, but at episode 8 only 59 to 68% of them are supported by its cited evidence. It reveals no new rumor facts after episode 3, while the places it reaches and its memory keep growing. More than half of the answers that become correct after episode 3 cite only evidence from earlier episodes.

---


### 31. [Self-Evolving Beyond Human-Crafted Experience for EDA Scripting](https://arxiv.org/abs/2611.26912)

**<font color=#1a73e8>作者：</font>** Yang Liu, Shengbo Tong, Xiyuan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing complexity of electronic systems demands efficient design flows, yet EDA scripting remains a bottleneck: proprietary APIs are sparsely documented, and errors often appear as silent failures or cryptic exceptions. Hand-crafted knowledge helps but is difficult to maintain as toolchains evolve. We present ZhuLong-SE (Self-Evolution), an execution-grounded LLM agent that learns reusable knowledge from prior task traces. Building on ZhuLong, it enhances the task-level harness with API retrieval, documentation responses, isolated sandbox execution, and static checking, then adds governed cross-task self-evolution. Beyond solving individual tasks, ZhuLong-SE distills past execution traces into a three-tier memory store governed by ground-truth anchoring, disconfirmation filtering, held-out rollback, and anti-leakage retrieval. On the 158-task EDA-Eval-PyAether benchmark, the full task-level harness, with self-evolution disabled, achieves 92.4% pass@1 and outperforms ZhuLong on all five tested LLM backbones. On a harder instance-disjoint test set, self-evolution from the bare configuration surpasses a human-crafted-experience baseline by 2.5 percentage points (80.0% vs. 77.5% pass@1).

---


### 32. [Multi-Tier Edge Triage: Optimizing Latency for Safe Clinical Agents](https://arxiv.org/abs/2611.26914)

**<font color=#1a73e8>作者：</font>** Joshua Broyde, Sarita A. Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying generative AI agents in enterprise clinical workflows requires enforcing multi-dimensional safety and compliance policies--preventing HIPAA Protected Health Information (PHI) exposure, maintaining clinical scope-of-practice boundaries, ensuring patient-appropriate reading comprehension, and preserving brand integrity--under interactive latency constraints. Synchronous outbound calls to cloud Large Language Model (LLM) judges add substantial network and decoding overhead onto the critical response path. We present Multi-Tier Edge Triage, a safety screening architecture that co-locates a compact Tier-1 sequence classifier on the clinical agent's host server, resolving clear queries in-process without a network round-trip and escalating only ambiguous queries to a Tier-2 cloud LLM judge. To evaluate Tier-1 encoders without length or unigram shortcuts, we construct four length-matched contrastive twin benchmarks seeded from MedSafetyBench, ASQ-PHI, and a synthetic four-mandate clinical assistant policy (Generic HealthCorp). While frozen local encoders match cloud models on structured PHI detection (>= 98.3% accuracy in <= 23.5 ms), they degrade markedly on semantic safety and symmetric-blocklist prompts. However, end-to-end representation fine-tuning closes the multi-policy accuracy gap: a fine-tuned 335M-parameter BGE-Large classifier achieves 98.90% out-of-fold accuracy versus 99.20% for a zero-shot cloud LLM judge (exact McNemar p = 0.648, zero shared errors), 97.8%-98.2% recall, and a 0.0%-0.4% over-refusal rate in 39.0 ms (>14x faster than cloud LLM evaluation on our benchmark host). Per-policy error analysis reveals ceiling local recall on PHI (100.0%), brand (100.0%), and clinical scope (98.7%-99.3%) violations, isolating residual errors to reading-level checks (93.3%-95.3%) and motivating targeted multi-tier escalation.

---


### 33. [What Does the Visual Encoder Buy? Visual Information Gain in Encoder-Free Multimodal Pretraining](https://arxiv.org/abs/2611.26917)

**<font color=#1a73e8>作者：</font>** Zhixuan Ge, Anqi Li, Wei Qiu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent scaling studies ask whether vision-language models still need a visual encoder by comparing encoder-free and encoder-based models on the next-token loss of the text in image-text data. This loss can fall without any use of the image, and two runs with the same loss can differ in what they take from it. Visual information gain (VIG) is the loss increase when the image is replaced by a uniform one. It splits exactly into global information, carried by image statistics, and layout information, which shuffling the patches within the image destroys. We apply it to decoders with 158M to 1.04B parameters that read pixel patches through a linear embedding, evaluated every billion tokens up to 40B, and to 19 public checkpoints. In our decoders the image lowers the loss by 3% to 46%, depending on the image type. Global information is present after the first billion tokens. Layout information starts near zero, grows slowly with training and does not grow with model size on five of six image types, and a larger batch reaches the same loss with less of it. With a frozen SigLIP 2 encoder in front of the same decoder the loss is lower only when the arrangement of the image is intact. On shuffled images the losses with and without the encoder agree to within 0.04 nats on five of six image types, so the net advantage of the encoder in the loss is layout information, above all the ability to read text in images. Public encoder-free models at production scale (Gemma 4 12B, NEO, Mono-InternVL) do acquire layout information. On the same documents they have 0.53 to 0.76 nats of it, against 0.65 to 0.82 for recent encoder-based models and 0.04 to 0.07 for our decoders, and their released training stages show it rising. These results agree with the reported parity of the two families when both are trained from scratch and place the reported advantage of a pretrained encoder in layout information.

---


### 34. [Partially canonical axes in large language model representations](https://arxiv.org/abs/2611.26920)

**<font color=#1a73e8>作者：</font>** Andrea Gregor de Varda, Ferdinando D'Elia, Greta Tuckute 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) develop rich internal representations of language, but whether their individual coordinate axes carry meaning, or whether meaning is encoded only in directions in representation space, is still an open question. A common assumption is that individual axes in LLMs are arbitrary. We here challenge this view: across 12 LLMs from six model families, the native axes are reliably more aligned with other models' representations, with human brain responses to language, and with interpretable linguistic features than randomly rotated axes that preserve the same geometry. The native axes nonetheless fall well short of the best achievable alignment, so LLM coordinates are not fully arbitrary but also not fully canonical: they are partially canonical. A theory of how LLMs represent language must explain both the population geometry they learn and why individual units acquire patterns of response profiles that recur across systems.

---


### 35. [Improving the Optimisation Landscape for Particle Mixtures](https://arxiv.org/abs/2611.26931)

**<font color=#1a73e8>作者：</font>** Yan Lin, David T. Frazier, Paula Cordero Encinar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several methods in statistics and machine learning represent a predictive distribution as an equally weighted mixture of models, or particles, trained via the mixture predictive likelihood. However, we prove that the mixture predictive likelihood is poorly suited to gradient-based optimisation, because it does not identify how the mixture is decomposed across particles, so that a poorly matched particle can be starved of training signal. As a remedy, we study a convex combination between the individual risk, i.e. the average log loss of the individual particles, and the mixture risk. At the particle level, this regularised risk imposes a reverse-KL barrier on the responsibilities of the particles, so that no particle can be starved of training signal. These phenomena are illustrated in two case studies: In the first, a predictively-oriented posterior is computed using mean-field Langevin dynamics, and the numerics are well-behaved only when our regularisation is employed. In the second, ensembles of low-rank adapters are jointly fine-tuned on large language models, across four backbones and eight multiple-choice reasoning benchmarks; direct minimisation of the mixture risk leads to responsibility starvation, whose severity decreases as the competence of the backbone increases, whereas our regularised estimator attains a lower held-out mixture risk on every backbone considered.

---


### 36. [Tokenize Moments, Not Frames: Tokenizer-Aware Budget Allocation for Training-Free Video LLM Acceleration](https://arxiv.org/abs/2611.26933)

**<font color=#1a73e8>作者：</font>** Zirui Zhao, Kai Liu, Linghe Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models (LLMs) represent each video with thousands of visual tokens, and training-free accelerators that prune or merge these tokens lose accuracy on long videos. Analyzing frame similarity and the vision tokenizers of 16 open models, we trace this loss to a step before token selection. Under a token budget, the frames of a long video are sampled farther apart than the roughly 2 s over which frames remain similar. The two-frame 3D patches of models such as Qwen-VL then blend two unrelated scenes into each visual token, a double exposure that arises before any pruning or merging. Fixed-size tokenizers such as InternVL's avoid this blend but respond differently to the same reduction. We propose ESSENCE, a training-free method that tokenizes moments, segments within which frames remain similar, rather than frames. Before encoding, a closed-form rule uses the sampling interval and the tokenizer class to set the number of token grids and the dimension to reduce; visual tokens are then released from later LLM layers. Against five recent accelerators on Qwen3-VL, Qwen2.5-VL and InternVL3.5, ESSENCE achieves higher accuracy in 58 of 60 comparisons at matched mean time to first token (TTFT). With 80% of the tokens, it matches the average accuracy of the full Qwen models at $1.6\times$ faster TTFT; on GLM-4.1V, it exceeds the full model by up to 3.4 points. Code is available at: this https URL.

---


### 37. [Self-similar Organization of Information in Language](https://arxiv.org/abs/2611.26935)

**<font color=#1a73e8>作者：</font>** Leon Lufkin, Cutter Dawes, Kamesh Krishnamurthy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How much information relevant to predicting the future of a passage (i.e. predictive information) is carried by the preceding text, and how is this information distributed along that history? These questions are fundamental to understanding both the statistical structure of language and what large language models (LLMs) can learn about it. Indeed, LLMs trained to predict the next token in text must exploit this predictive information, so its organization determines how the structure of language becomes available to the model to learn. We develop a theory for the organization of predictive information based on the scaling behavior of a family of information measures, and the theory predicts that if this organization has the same form at all measured length scales -- i.e., it has a self-similar structure -- then the information measures evaluated at different lengths collapse onto a common form. We observe this scaling collapse in long text documents, showing that predictive information is present at every length scale we measure and has a self-similar structure. Self-similarity is a considerably stronger property than showing the existence of long-range dependencies, and it constrains the process generating the text. More broadly, our results give quantitative support to the empirical observation that conditioning on more distant text continues to reveal new structure in language to LLMs.

---


### 38. [SecretAgent: A Multi-Agent Framework for Privacy Protection against Vision Language Models](https://arxiv.org/abs/2611.26936)

**<font color=#1a73e8>作者：</font>** Minda Zhao, Yue Zhang, Mengyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can infer private information from shared images, including locations, personally identifiable information (PII), and personal attributes such as age and sex, even from medical images. Adversarial perturbations can protect such information against black-box VLMs, but existing methods overlook image quality and introduce visible artifacts into the images they protect. We present SecretAgent, the first general multi-agent framework that protects image privacy against VLMs while preserving visual fidelity. LLM agents iteratively locate the visual evidence that reveals private information and adapt an invisible perturbation to the target VLM's answers and to an appearance reviewer agent, which rejects any candidate with visible artifacts. We instantiate SecretAgent with two complementary variants: SecretAgent-Gradient optimizes the perturbation through six surrogate encoders for cross-model transferability, and the gradient-free SecretAgent-Tool composes procedural noise and achieves the best perceptual fidelity on three of the five datasets. Experiments on four privacy applications (geolocation, PII, facial, and medical) across five datasets and six VLMs show that SecretAgent preserves image quality substantially better than existing methods while achieving state-of-the-art privacy protection in every application, and that its protection transfers to other VLMs.

---


### 39. [Looking Right Is Not Being Right: Evaluating the Geometry of Agent-Built 3D Scenes](https://arxiv.org/abs/2611.26937)

**<font color=#1a73e8>作者：</font>** Ziyang Long, Yen-Liang Lin, Shifan Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language agents can reconstruct rooms from video as editable 3D scenes, but convincing renders do not establish geometric accuracy. We introduce a scan-referenced evaluation and use controlled experiments to study reconstruction accuracy, the role of geometric inputs, and agents' ability to verify and correct their scenes. Our geometric score measures surface, depth, and furniture placement agreement with laser scans of 30 real rooms on a 0-100 scale. The strongest tested agent, GPT-6 Astra, scores 51.4 from video alone, while a dense reconstruction from the same video scores 75.9. Given the point cloud used for that reconstruction, Astra produces an editable scene that scores within three points of it. Agents also inherit input errors: rescaling the supplied geometry changes scene scale almost proportionally. During revision, viewing renders improves appearance more consistently than geometry. Logs of their tool calls show that agents repeatedly measure their inputs but rarely compare them with the scenes they build. To provide this missing check, we introduce a geometric error report that compares each saved scene with the agent's input points and lists the largest discrepancies. Without new geometric evidence, the report raises the revision gains of GPT-6.1 Terra and Sol by 3.9 and 5.5 points over concurrent controls.

---


### 40. [Extracting Next Generation Access Control Policies from Natural Language Using LLMs: An Intermediate-Representation Approach with Back-Translation Verification](https://arxiv.org/abs/2611.26941)

**<font color=#1a73e8>作者：</font>** Ayesha Habib, Huixiang Zhang, Waiz Haider  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organizations write access-control rules in natural language, but NIST's Next Generation Access Control (NGAC) needs them as a formal policy graph. Large language models (LLMs) can automate this translation, but their output can break the format, add rules the text does not state, or drop conditions. We present NGAC-IR, which follows model-driven engineering (MDE). First, the LLM fills in an intermediate representation (IR), a JSON template that records who may, must or must not do what, on which resource and under which condition; a grammar keeps the output within this template. Second, a compiler that uses no LLM converts the IR into an NGAC policy graph and links each rule to its source sentence. Third, a back-translation check writes each rule in English and asks an LLM whether the source sentence states it. On four public datasets, all outputs could be compiled, compared with 95.5% without the grammar, and 95.7% were faithful to their sentence. NGAC-IR outperforms two published methods on all four datasets: the LLM-based Code4Policy in exact match and faithfulness, and the rule-based extractor of Abdelgawad et al. in rule type. The back-translation check sent 10.5% of sentences to human review and found 26 of the 31 errors. To test enforcement, we deployed the compiled policies in NIST's Policy Machine: they gave the expected decision for all 390 access requests, and the tested obligations were carried out. On one local server with open-weight models, all 714 sentences take about 20 minutes and 0.35 kWh, at zero API cost.

---


### 41. [Learning Video Foresight Reasoning from Unlabeled Videos via On-Policy Self-Distillation](https://arxiv.org/abs/2611.26954)

**<font color=#1a73e8>作者：</font>** Jingchen Sun, Jiaxing Zhang, Qingqiao Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video foresight reasoning requires vision-language models to anticipate future events or next actions from currently observed videos. Existing methods fit future captions, rationales, or full visual states, but face two limitations. First, they rely on annotations or external large models for supervision, limiting scalability. We address this with an on-policy self-distillation framework that turns past-future video pairs into a natural self-supervised signal without extra annotations or LLM supervision. Second, they treat the whole future clip as equally valuable, although most of it is irrelevant context information. We address this by defining a foresight score, from which we obtain a contrastive privilege advantage that drives the model to learn the most valuable future information. Since the score is intractable, we optimize a tractable lower-bound surrogate that interpolates this advantage, computed between the true and a random reference future, with a teacher-student distillation advantage; together, they amplify decision-relevant content information and suppress irrelevant context information. We call the resulting framework Future-OPSD. On open-ended prediction and closed-ended planning, Future-OPSD improves base models by up to 14.2 and 15.9 points without compromising general video understanding. Code will be available at this https URL

---


### 42. [Tracking and Limiting Unsupported Claim Propagation in Multi-Agent LLM Systems: A Provenance-Aware Framework](https://arxiv.org/abs/2611.26957)

**<font color=#1a73e8>作者：</font>** Zijia Cao, Hanqing Dou  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This research examines how unsupported claims change as they move through multi-agent pipelines. It also examines whether preserving provenance can reduce these changes. We test both homogeneous and heterogeneous pipelines. Homogeneous pipelines use the same model across agents, while heterogeneous pipelines use different models. We compare the baseline with a provenance-aware framework. The framework passes each claim with its support status, source, evidence and transmission history. No new evidence is introduced during transmission. We measure changes in claim meaning, unsupported detail accretion, semantic drift, and provenance preservation. These metrics show whether the framework limits unsupported changes as claims pass between agents.

---


### 43. [Keep the Process, Change the Supplier: Runtime Governance for Tool-Using AI Agents](https://arxiv.org/abs/2611.26966)

**<font color=#1a73e8>作者：</font>** Deepak Waghmare, Shaad Sufi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using AI agents propose actions whose authorization and external effects cannot be inferred from generated text alone. We study an execution boundary that separates agent proposals from business-controlled authority, context disclosure, and supplier selection. The Open Process Control Plane (OPCP) mediates capability calls and records uncertain outcomes when a supplier may have acted without returning an acceptable reply. We evaluate this runtime with scripted requests and synthetic suppliers: 2,400 fault episodes across four policies, 60 process-termination/restart episodes, 19,000 timed calls across 19 configurations, five targeted mutations over 43 fixtures, and 160 substitution records. No language model or autonomous agent is evaluated. OPCP and a conservative composition agree on all measured fault outcomes. Both recover after definite refusal without cross-supplier duplication; retry-all duplicates effects in every tested lost-reply-after-commit case. Persistent runtime state prevents cross-supplier replay in the restart experiments, while same-supplier duplicate prevention also requires supplier idempotency. At 128 suppliers, best-score routing has a median latency of 1.411 ms versus 0.261 ms for pinned routing. All five selected mutations are detected, and record enumeration exposes acceptance of an empty regression set. These results characterize an execution mechanism relevant to agent governance, including its costs and assumption boundaries. They do not establish improved agent task success, prompt-injection resistance, or real-vendor model portability.

---


### 44. [Right Numbers, Wrong Story: When LLMs Narrate Financial Changes Beyond Their Inputs](https://arxiv.org/abs/2611.26968)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jun Seo, Junhyeok Kang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A financial report drafted by an LLM can state every number correctly but still go beyond its input, adding judgments and causes that no one supplied. We call these additions unsupported framing and find them far more often in LLM drafts than in reports written by proInput facts Revenue +3% Higher prices 10-K filings Revenue increased 3% on higher prices. 10-K writer Revenue surged 3% on higher prices, due to strong demand. LLM Fits the size? Surged: Unusual for 3% In the input? In the input? Strong demand: Not in input Higher prices: Kept fessionals, and attempts to fix them by prompting with how each word is used instead make such judgments more frequent. We therefore propose FrameCheck, a plug-in that sits beFrameCheck Revenue increased 3% on higher prices. No extra model call Judgment word Unsupported cause Supported cause tween the LLM and human review to keep each draft within its input. Specifically, FrameCheck 1) guides the draft with professional examples that report a change of similar magnitude, 2) flags judgments that professionals would not use and causes the input does not give, and 3) removes them by rule, without a model call. In experiments on 17 open LLMs and 3M drafts, FrameCheck removes almost all unsupported framing from drafts and brings the judgment rate close to that of the writers of 10-K filings, the annual reports that US firms file with regulators. Code is available at this http URL.

---


### 45. [When Perception Collides with Priors: Diagnosing Modal Polarization in Video Understanding Models](https://arxiv.org/abs/2611.26972)

**<font color=#1a73e8>作者：</font>** Yao Tong, Jiaxin Qi, Yan Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved strong video comprehension, largely benefiting from extensive training on realistic video data. However, when video perception severely conflicts with internal priors or common sense, we identify a critical failure pattern termed Modal Polarization, where models fail to integrate modalities and instead bifurcate into two distinct extremes: Cognitive Inertia, where models rigidly adhere to priors despite contradictory visual evidence, and Perceptual Inertia, where they blindly trust video perception while ignoring logical inconsistencies. To investigate this, we introduce TheaterBench, a benchmark designed to expose Modal Polarization using counter-intuitive scenarios that violate physical laws or common sense - situations rarely encountered in standard training distributions. Extensive experiments reveal that current state-of-the-art (SOTA) models exhibit severe Modal Polarization, and many de-hallucination methods merely rebalance the trade-off between Perceptual and Cognitive Inertia rather than fundamentally resolving the conflict. This work serves as a foundational step for evaluating and enhancing the perceptual-cognitive equilibrium of future video understanding models.

---


### 46. [Run One, Get Two: Near-Free Streaming Safety Checks for Local LLMs](https://arxiv.org/abs/2611.26975)

**<font color=#1a73e8>作者：</font>** Soheil Zibakhsh, Pedram Aghazadeh, Farinaz Koushanfar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Local LLM assistants decode for one user at a time, so decoding is bound by memory bandwidth and leaves compute idle. Streaming safety checks today trade accuracy against cost. A dedicated guard model is accurate but nearly doubles the latency per token, while a hidden-state probe is cheap but less accurate. We present ToRA, an adapter that runs a second model as an extra row in the generator's decode step, sharing its weights and KV cache. Dual-row kernels read each weight once for both rows. On Qwen3-0.6B, ToRA matches or beats a dedicated streaming guard, with higher F1 on 12 of 17 benchmarks. It detects 11.8 points more unsafe responses than the probe at a similar cost, under 4% added latency per token.

---


### 47. [MixFold: Sub-4-Bit Mixed-Precision LLM Inference via Output-Channel Grouping on Mobile NPUs](https://arxiv.org/abs/2611.26976)

**<font color=#1a73e8>作者：</font>** Vinnam Kim, Seong Hoon Seo, Junhan Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sub-4-bit quantization allows mobile devices to run larger LLMs, but its memory savings do not always translate into faster decoding on mobile NPUs. Their matrix units support only a few native integer datatypes, and converting unsupported weight formats on the vector unit can erase the gains from fewer bits. Mixed precision faces an additional constraint: each matrix-unit tile uses one datatype. MixFold executes 3-bit and perfectly symmetric 2-bit weights using native integer operations without expanding the weights to wider datatypes during decoding. MixFold then assigns datatypes to output-channel groups aligned with the matrix-unit tiles, enabling finer-than-layer assignment without disrupting matrix-unit execution. We compare MixFold with this http URL Hexagon backend on the Qualcomm Hexagon NPU of a Snapdragon 8 Elite Gen 5. Across the Qwen3 model family, MixFold achieves comparable or higher accuracy than this http URL's sub-4-bit formats at matched bits per weight, while decoding 1.16-1.41 times faster and generating 1.5-4.3 times more tokens per joule.

---


### 48. [GeoCloak: Defending Against Geolocation Reasoning in Multimodal Language Models via Perceptual Image Editing](https://arxiv.org/abs/2611.26987)

**<font color=#1a73e8>作者：</font>** Haoyang Xu, Christian Iha, Colbren Fujimoto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models can infer sensitive geographic information from ordinary images by combining visual, textual, architectural, and environmental cues. This capability creates a privacy risk: users may reveal fine-grained location information even when explicit metadata such as GPS tags has been removed. We study this problem as geolocation inference in multimodal language models and present GeoCloak, a cue-aware perceptual editing framework for reducing location leakage from shared images. GeoCloak uses an accessible multimodal model as a proxy to identify geolocation-relevant cues, localizes high-impact regions through object grounding, and applies localized semantic edits designed to disrupt downstream geolocation predictions while preserving the overall scene content. Experiments on street-level image datasets show that GeoCloak substantially reduces administrative-level geolocation accuracy across multiple multimodal models, while maintaining automatic perceptual-quality scores closer to those of the original images than pixel-level perturbation baselines. These results suggest that cue-level semantic editing is a promising direction for reasoning-based visual privacy, while also highlighting open challenges in deployment cost, semantic plausibility, and adaptive evaluation.

---


### 49. [From Letter-of-Credit Requirements to Executable Specifications: Evaluating Verification Accuracy and Completeness](https://arxiv.org/abs/2611.26988)

**<font color=#1a73e8>作者：</font>** Ji Sub Choi, Whan Choi, Seo Yeon Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In letter-of-credit (LC) document examination, a correct final decision does not show that every requirement was examined. We therefore evaluate examination requirement by requirement and make each requirement executable. A language model converts the bill of lading (BL) and commercial invoice (IV) requirements of a credit into atomic conditions and logical structures, and a deterministic verifier retrieves the named evidence and computes each outcome, so every check can be compared with a gold encoding and traced to logged evidence. Because LC records are confidential, our on-premises 9B parser is fine-tuned only on synthetic pairs built from templates and human-reviewed public document values. On 345 real LC cases, final-decision accuracy proves misleading: a constant PASS rule has the highest raw accuracy while examining nothing. Although it never sees a real record during training, the fine-tuned parser detects 93% of the atomic requirements its ontology covers and reconstructs 86% of the covered requirements exactly. It verifies 82% of the evaluable requirements correctly, against 54% for a tool-using agent, and leads the agent on both satisfied requirements and discrepancies. It also completely examines 1.8 times as many cases as few-shot prompting of the same model, while direct prediction and the agent complete none. Executing the gold encodings with the same verifier shows that some of the remaining errors, missed discrepancies included, come from the operators and normalization, which a better parser alone cannot fix. Every rejection comes with a trace of the units and evidence behind it, which suits examiner-in-the-loop review.

---


### 50. [SceneRuler: Measuring Physical Quantities in Video via Minimal Sufficient Reconstruction](https://arxiv.org/abs/2611.26994)

**<font color=#1a73e8>作者：</font>** Yumeng He, Gezheng Kang, Fanlian Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many questions about videos ask for a number, such as how tall a person is, how far a cart travels, or how fast a ball leaves a ramp. We study this task, quantitative physical reasoning from video, where the inputs are a video, a question, and a prior of known facts such as object sizes, speeds, and distances from the camera to named objects. End-to-end video-language models lack an explicit metric scale and physical consistency, and their errors cannot be inspected. We present SceneRuler, which instead recovers a measurable physical scene and answers with that scene as evidence. Its central principle, Minimal Sufficient Reconstruction, builds, for each question, only the smallest scene that suffices to measure the asked quantity, and tests sufficiency on measurements rather than assuming it. The scene is written as a program whose structure a vision-language model writes and whose magnitudes are left to measurement. Physics-guided Fitting measures them through physical motion laws, so that gravity itself can anchor the metric scale, and marks every parameter, and the read-out of the asked quantity, as determined or undetermined. Each question receives a read-out and an answer. The read-out is the asked quantity evaluated on the scene, and it is empty when the scene does not fix that quantity. The answer is always given by a model that takes the scene as evidence. We evaluate on QuantiPhy and also apply the method to 27 in-the-wild videos that we collected, which have no ground-truth answers. On its validation split, the final answer reaches a mean relative accuracy of 0.709 against 0.624 for the strongest baseline, and the reconstruction determines the asked quantity on 47 of 158 questions, where the final answer reaches 0.781. Because every intermediate quantity is explicit, each answer can be traced to the objects, scale, and motion behind it.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
