# 🧠 大模型相关研究 | 2026年09月17日

> 本类共 **189** 篇论文：已确认 **180** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-189](./part-04.md)

---

### 1. [Few-Shot Degradation Is Not What It Seems: Behavioral Evidence, Representation Analysis, and a Random-Text Control Across 12 Models, 2 Tasks, and 2 Architectures](https://arxiv.org/abs/2609.15990)

**<font color=#1a73e8>作者：</font>** Volodymyr Ovcharov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Few-shot prompting sometimes degrades language models instead of helping them, but why this happens is unknown. We evaluate 12 open-weight models on two Ukrainian tasks news classification and legal case outcome prediction and find that the effect is strongly task-dependent: the same models that gain +24 pp on news show only +3.4 pp on legal text, with two models degrading. To understand why, we look inside the models. Prior work measures how much hidden states shift between zero-shot and few-shot modes, but few-shot prompts are much longer, and that length difference alone moves representations. We propose a simple fix: replace demonstrations with length-matched random text to measure the shift caused by prompt length, then subtract it. The resulting metric content delta isolates how much the model's representations change because of what the demonstrations say, not how long they are. This changes the picture entirely: raw shift does not predict whether few-shot helps or hurts (r = 0.20), but content delta does (rho = +0.65, p = 0.043). Models that restructure representations more from demonstration content benefit more the opposite of the intuitive "distortion" explanation. Masking demonstrations in Llama 3.3 70B confirms the finding causally, recovering accuracy above the zero-shot baseline.

---


### 2. [The Functionalizer: Lossless Functional Decomposition for Subword Tokenization](https://arxiv.org/abs/2609.15991)

**<font color=#1a73e8>作者：</font>** Connor Makowski, Willem Guter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard subword tokenizers either treat every orthographic variation of a word (such as hello, Hello, HELLO, and Héllo) as unrelated vocabulary entries, which fragments the embedding space, or discard this variation through lossy normalization. We present the Functionalizer, a lossless pre-tokenizer framework that factors orthographic and structural variations into a compositional opcode/operand prefix stream before tokenization: a canonical base token (operand) prefixed by parametric transformation operators (opcodes) encoded in the Unicode Private Use Area. We introduce operators covering casing (CAPITALIZE), diacritics (13 dedicated opcodes), and character repetition (REPEAT, MULTIREPEAT), which are fully reversible. Across six natural language and code corpora, the Functionalizer enables complete corpus coverage with significantly smaller vocabularies under unconstrained conditions, reducing actual vocabulary slot requirements by up to 16%. When looking at sequence lengths, we observe a sharp domain-dependent tradeoff: it compresses indentation-heavy code sequences but inflates natural-language prose sequences. Preliminary downstream evaluations on 25M parameter GPT-2 scale models show that at this scale, the Functionalizer drastically improves code syntax validity and improves code character perplexity while maintaining similar text coherence on prose. These findings demonstrate that functional decomposition can be an effective mechanism for vocabulary-efficient, structurally aware language modeling, and motivate further validation at production scale.

---


### 3. [Optimal Model Activation Policies for Inference Networks of Large Language Models](https://arxiv.org/abs/2609.15992)

**<font color=#1a73e8>作者：</font>** Foivos Charalampakos, Md Ibrahim Ibne Alam, Iordanis Koutsopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have rendered them necessary for Natural Language Processing (NLP) tasks, and their high inference cost motivates the study of cost-performance trade-offs. In practice, several expert LLMs are used in synergy for inference, either in an ensemble mode or in series, yet without a principled approach on how to best use the available models. An adaptive approach can route simple queries to cheaper LLMs and complex ones to more capable, costly models. However, a clear understanding on how to best leverage available expert models is missing. We introduce inference networks, a graph-based framework, where nodes denote different LLMs, and links denote conditional model activations. The inference network design problem is to determine the best topology, namely the best way to use the models that best addresses the cost-performance trade-off. We start from the basic topology of a series of LLM experts, each of which has a different cost and a different level of expertise, which is captured via model confidence. We formulate the problem of optimal activation of these models so as to minimize the expected inference cost subject to a target performance constraint. For this special class of inference networks, we prove that the optimal activation policy has a threshold structure: query the lowest-cost LLM first, and invoke the more expensive LLM only if the confidence falls below a defined threshold. For discriminative tasks, the optimal policy consists of a set of thresholds, one threshold for each class, while for generative tasks, it consists of a single threshold. We provide a structured method to compute the thresholds, and practical confidence estimation mechanisms for both task types. Experiments with open-source LLMs show substantial cost reductions while meeting the specified performance budget.

---


### 4. [Latent Undertow: How Ordinary Typos Break Probes](https://arxiv.org/abs/2609.15994)

**<font color=#1a73e8>作者：</font>** Elad David, Max Fomin, Amit LeVi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs handle ordinary typing variation fluently: a typo or missing punctuation leaves both user intent and the model's response substantively unchanged. Yet probes that detect malicious prompts by reading the model's hidden states tell a different story: the same edit rotates the readout vector by 43--56 at the perturbed token, decaying below 15% within ~10 downstream tokens. Stacking ~3 common typos per message cuts a single-position prompt-injection probe's TPR@FPR$=1% by 12.0pp, a gap recalibration alone cannot close. Multi-position aggregation cures localized perturbations (<= 0.5 loss) but only attenuates distributed ones, where even attention- and max-based aggregators still drop ~3.8pp. For single-position probes, we introduce a KV-cache fork: a short fixed suffix appended after the user message lets the probe read a few tokens downstream of the perturbation, exploiting its rapid spatial decay. This closes 95% of the gap (-0.6pp residual) -- an order of magnitude better than perturbation-augmented training (-3.7pp). The rotation-and-decay geometry replicates on Llama-3.1-8B, Qwen3-8B, and Gemma-4-E4B; probe evaluation is on Llama-3.1-8B. Code: this https URL

---


### 5. [Comment on arXiv:2607.01233: Survivorship Bias in Published-Paper Baselines for Research-Idea Distributions](https://arxiv.org/abs/2609.15996)

**<font color=#1a73e8>作者：</font>** Fredrik A. Dahl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chen, Zhao, and Cohan introduce a valuable distributional evaluation of LLM-generated research ideas. This comment raises a narrower identification concern: their human baseline consists of published papers, whereas the LLM baseline consists of one-shot proposals. If bridge-like or synthesis-like ideas are relatively easy to generate but relatively unlikely to survive publication, then the published human baseline will understate their prevalence in the unseen human idea pool. The observed human--LLM gap may therefore be partly, or even largely, a consequence of survivorship bias.

---


### 6. [Crash Narrative-Guided Countermeasure Recommendation Using Large Language Models: A Retrieval-Augmented Generation Framework for Intersection Safety](https://arxiv.org/abs/2609.15997)

**<font color=#1a73e8>作者：</font>** Abu Saif Md Nasim Uddin, Mohamed Abdel-Aty, Zubayer Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Improving safety at intersections requires identifying crash mechanisms and recommending appropriate countermeasures. However, this process traditionally relies on expert judgment, making it labor-intensive, difficult to scale, and dependent on the availability of experienced traffic safety engineers. Although crash narratives contain rich description of crash mechanisms, this unstructured information remains largely underutilized in safety analyses. This study presents a crash narrative-guided retrieval-augmented generation (RAG) framework that translates narrative-derived crash mechanisms into site-specific countermeasure recommendations. Key mechanism attributes including traffic control, signal indication, driver fault, vehicle movement, and travel direction were extracted from crash narratives and linked to evidence-based treatments from the FHWA Proven Safety Countermeasures and the CMF Clearinghouse. The framework integrates embedding-based retrieval of historically similar intersections, association-rule mining, statistical guidance on the expected number of relevant countermeasures, and an engineering reasoning guidance that directs LLM through a domain-consistent decision process before selecting countermeasures. Evaluated on 312 fatal and serious-injury crashes across 115 intersections in Lake and Sumter Counties, Florida, using five-fold cross-validation, the framework achieved a precision of 0.82, recall of 0.85, and F1-score of 0.82, while recommending an average of 3.91 countermeasures per location with 3.14 matching, closely matching the actual average (3.86). Overall, the proposed framework demonstrates the potential of retrieval-augmented LLMs as an interpretable and scalable decision-support tool for transportation agencies for translating crash narratives into countermeasure recommendations.

---


### 7. [Self-reported archetypes and behavioral failures in Large Language Models](https://arxiv.org/abs/2609.15998)

**<font color=#1a73e8>作者：</font>** Tabia Tanzin Prama, Calla Glavin Beauregard, Christopher M. Danforth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Every large language model (LLM) has behavioral traits and moral preferences that comprise its character. Whether by design or as an emergent property of training, these systems exhibit persistent dispositions that shape how they interact, comply, resist, and err, yet the structure of LLM character remains poorly understood. We map the self-reported personality archetypes of 22 LLMs spanning closed-source frontier systems (GPT-4.0-5.2, Grok-3/4, Gemini 2.5 Pro/Flash, Claude Sonnet 4.5/4.6) and open-source models (Llama, DeepSeek, OLMo, and Qwen series). Each model self-rated across 464 bipolar semantic-differential trait pairs, and the resulting profiles were projected into a six-dimensional archetypal space derived from crowd-sourced ratings of 2,000 fictional characters using the Archetypometrics framework. Closed-source models' self-rating traits align with the empirical trait co-occurrence structure of human-rated fictional characters, suggesting coherent, human-like self-representations organized around combinations of four recurring archetypal dimensions: Hero, Angel, Traditionalist, and Geek. Their closest analogues include Data, Vision, and Janet. Open-source models show weaker, noisier, and internally contradictory self-representations, occupying a diffuse region of archetype space with weak structure. Cross-referencing self-reported profiles with developer constitutions reveals a consequential gap between claimed character and enacted behavior: hallucination undermines claimed precision, sycophancy complicates claimed kindness, and agentic failures contradict claimed obedience. These self-ratings should therefore be interpreted not as neutral measurements of model character, but as structured outputs of the same optimization processes that shape model behavior. This work provides a reproducible, character-grounded framework for evaluating what LLMs are, not just what they do.

---


### 8. [NepKANUN: A RAG-Based Nepali Legal Assistant](https://arxiv.org/abs/2609.15999)

**<font color=#1a73e8>作者：</font>** Bhabuk Thapa, Prasiddha Koirala, Ranjit Raut 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accessing legal information in Nepal is difficult due to complex terminology, limited resources, and misinformation. We introduce an AI-powered legal assistant that is tailored for Nepali legal texts and is built on a fine-tuned large language model. The technology provides precise, streamlined answers to natural language legal inquiries when integrated into a Retrieval-Augmented Generation (RAG) framework. It was trained using a custom dataset of high-quality question-answer pairs, and according to BERTScore, it obtained strong F1 scores of 0.82 (simple), 0.77 (moderate), and 0.71 (complex). Its usability is further confirmed by expert reviews. Our method shows how merging generation and retrieval can effectively democratize access to legal knowledge in Nepal by focusing on customized legal data and incorporating RAG.

---


### 9. [Nepali Legal Expertise through Generative and Extractive Pre-trained Transformers (NepLEGiT)](https://arxiv.org/abs/2609.16010)

**<font color=#1a73e8>作者：</font>** Ranjit Raut, Tishya Dhakal, Aaryan Shakya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The complexity of legal language and limited accessibility to legal information pose significant challenges to justice delivery in Nepal. Traditional legal services remain inaccessible to many citizens due to language barriers, information fragmentation, and a critical shortage of legal expertise, particularly in rural areas. We present NepLEGiT (Nepali Legal Expertise through Generative and Extractive Pre-trained Transformers), a specialized small language model (SLM) designed to democratize legal knowledge and enhance legal-service delivery in Nepal. We pre-train a decoder-based GPT-2 SLM from scratch on a curated corpus of ~4 million tokens of Nepali legal text, covering constitutional law, civil and criminal codes, and administrative regulations. The model comprises ~30 million parameters in a 6-layer, 6-head, 384-dimensional transformer trained with warmup cosine-decay scheduling, gradient accumulation, and mixed-precision arithmetic. On a held-out validation split, NepLEGiT attains a cross-entropy loss of 0.5684, a perplexity of 1.8, and a next-token prediction accuracy of 82.9%. We further evaluate continual masked-language-model pre-training of mBERT and MuRIL on the same corpus; mBERT achieves a perplexity of 2.35 (eval loss 0.8565), outperforming MuRIL (perplexity 6.07, eval loss 1.8026), providing a strong encoder baseline complementary to NepLEGiT's generative orientation.

---


### 10. [MechReason: Benchmarking Multi-Image Multi-Hop Reasoning in Mechanical Engineering](https://arxiv.org/abs/2609.16012)

**<font color=#1a73e8>作者：</font>** Tengyue Wang, Kang An, Chenxu Du 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant progress in general visual question answering and cross-modal understanding, multimodal large language models still face a pronounced gap in evaluation for complex reasoning within the mechanical engineering domain. Existing benchmarks predominantly focus on rudimentary tasks such as drawing recognition, CAD interpretation, or single-chart querying, falling short of assessing whether models can integrate multiple images, textual conditions, physical principles, and engineering constraints to perform multi-step reasoning when confronted with authentic, intricate mechanical problems. To address this, we introduce MechReason, a benchmark derived from real mechanical engineering papers, comprising 12k question-answer pairs with explicit reasoning-chain annotations and 21k visual materials spanning nine evidence types, including statistical charts, parameter tables, engineering drawings, microscopic images, simulation images, system architectures, real mechanical scene photos, CAD model images and manufacturing flowcharts. MechReason covers eight task types across four reasoning dimensions: explanation, prediction, design, and diagnosis. We devise a four-stage construction pipeline: we first extract core engineering claims and decompose their supporting evidence into premises, reasoning processes, conclusions, and corroborative evidence; we then generate shortcut-preventing questions by masking posterior verification information; finally, we apply multimodal quality validation to ensure task quality and multi-hop nature. Extensive experimental results demonstrate that MechReason is highly challenging, with even the most advanced models achieving only 62.89\% accuracy.

---


### 11. [ViCo: Visual-oriented Coding with Self-Reflection for Chart Replication](https://arxiv.org/abs/2609.16014)

**<font color=#1a73e8>作者：</font>** Jiaxin Duan, Dian Jiao Shuai Zhao, Jiabing Leng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper addresses the challenge of generating high-quality academic charts that match the visual standards of human-authored papers. While existing AI agents can produce well-structured text and code, their generated visualizations often lack the stylistic and semantic fidelity of human designs. Advanced coding agents that employ self-reflection mechanisms exhibit poor visual reasoning and limited reflection following, resulting in sparse reward signals that severely undermine their reinforcement learning (RL). We propose ViCo, a training framework for visual-oriented coding that employs iterative reflections to align generated chart images progressively with the reference. We first introduce a self-supervised warm-up stage, which augments Monte Carlo Tree Search with consistency-based pruning to synthesize high-quality reflection trajectories, ensuring that each coding step strictly follows the outcomes of prior reflections. A multi-step RL algorithm is then developed, using counterfactual baselines to estimate advantage for reflection and action steps within each refinement cycle, thereby addressing the reward sparsity. To enable efficient reward in massive training, we propose an automatic, multifaceted evaluation framework that assesses charts' style, layout, and semantic consistency via a hierarchical heterogeneous layout graph structure. Experiments on three public benchmarks demonstrate that ViCo, trained on an 8B model, achieves performance close to proprietary LLMs with adequate reflection capabilities.

---


### 12. [Are We Grading Properly? Understanding Failure Modes in Medical Benchmarks](https://arxiv.org/abs/2609.16023)

**<font color=#1a73e8>作者：</font>** Prithvi Dixit, Pedram Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical evaluation is shifting from static option-based questioning to realistic clinical scenarios with open-ended output modes. Grading these at scale naively, however, is expensive, and rubric-based evaluation has become the dominant scalable alternative. We ask what happens when the rubrics themselves are not airtight, and whether such flaws can be detected and corrected. We apply RIFT, a global rubric failure taxonomy, to two clinical benchmarks (HealthBench Professional and LiveMedBench), and find failure modes are meaningful: on HealthBench Professional an LLM judge flags 29.6% of criteria as non-atomic and 65.4% as misaligned/rigid. Then, we show that these flaws are meaningful and not simply cosmetic. As an example, rewriting bundled criteria of the form "at least one of / all of the following" as equally weighted children and regrading identical responses shifts scores by up to 15.9 percentage points on affected conversations, with disjunctive bundles inflating scores and conjunctive bundles deflating them. We also find that RIFT generally under-detects bundling on clinical rubrics, flagging 3.3% of LiveMedBench criteria as non-atomic where surface-form analysis finds structure in 25.8%.

---


### 13. [Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents](https://arxiv.org/abs/2609.16053)

**<font color=#1a73e8>作者：</font>** Yuanyi Song, Yukai Wang, Xinbei Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for LLM-based agents operating over extended interactions. Existing memory systems primarily update memory when new information arrives, treating retrieval as the endpoint of memory access rather than a driver of memory evolution. Consequently, retrieval feedback is rarely exploited to reorganize memory for future access continuously. Moreover, most existing approaches rely on predefined memory structures together with fixed retrieval pipelines, limiting the agent's ability to organize and evolve its own memory autonomously. Inspired by memory reconsolidation in cognitive neuroscience, we propose \textbf{REALM}, a \textbf{r}econsolidation-\textbf{e}volution \textbf{a}gentic \textbf{l}ong-term \textbf{m}emory framework. It models long-term memory as a continual lifecycle by autonomously organizing memories into a heterogeneous cognitive graph, retrieving evidence via adaptively composed graph-search atoms, and continually reconsolidating memories based on retrieval feedback. REALM achieves an average accuracy of 75.97\% on LoCoMo and 65.11\% on LongMemEval, outperforming the strongest baselines by 7.17 and 1.31 points respectively. Ablation studies confirm that memory reconsolidation consistently boosts performance, with further analyses revealing that it progressively reorganizes related memory units into more coherent local structures for collective evidence recall and utilization during reasoning. These results suggest that retrieval-driven memory reconsolidation provides an effective mechanism for continually evolving long-term memory in LLM agents.

---


### 14. [State of Thought Enables Endogenous Reasoning](https://arxiv.org/abs/2609.16055)

**<font color=#1a73e8>作者：</font>** Zhiren Gong, Yikun Hou, Zihao Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time compute has emerged as a major approach to improving the capabilities of Large Language Models (LLMs). However, existing test-time reasoning paradigms rely heavily on externally imposed control, either through fixed reasoning programs or through costly expansion in constrained search spaces, limiting both generalization and efficiency. We propose State of Thought (SoT), a new reasoning paradigm that enables endogenous reasoning in LLMs, with the model's internal reasoning state governing how reasoning unfolds. Concretely, SoT extracts a compact dynamics-geometric state from the model's internal information transfer and uses a 582-parameter controller on frozen backbones to selectively activate historical reasoning support useful under the current reasoning state, framing reasoning as a state-conditioned process over evidence rather than an externally prescribed token chain. Across quantitative (1.34x), general (1.62x), symbolic-and-code (1.76x), and long-context (2.51x) reasoning on 3 LLMs and 16 datasets, SoT consistently improves mean-baseline accuracy while reducing generated tokens by 62.6% and end-to-end latency by 44.6%. Across 2 VLM scales and 3 reasoning tasks, it improves mean accuracy by 3.8 points over reasoning baselines, with 74.9% fewer completion tokens and 73.5% lower latency than search-based methods. Under constrained access, SoT retains 38.2%/36.5% mean accuracy gains in training-free/embedding-only settings, while trajectory-only judging reaches 84.1% agreement across 3 API models. Together, endogenous state-driven reasoning provides a generalizable and efficient alternative.

---


### 15. [OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy Learning](https://arxiv.org/abs/2609.16057)

**<font color=#1a73e8>作者：</font>** Xu Xu, Jinxiu Liu, Zhangbo Qiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unified multimodal large language models (MLLMs) and multi-agent systems have advanced visual generation. However, three limitations remain. (1) Existing methods often distill task-specific experience with limited generalizability. (2) Reflection is often deferred until task completion. (3) Knowledge is often acquired only in response to downstream task demands. To address these limitations, we introduce OmniHarness, a framework for generalizable visual generation via symbolic policy learning. OmniHarness abstracts verified executions into symbolic policies for visual generation task families, capturing shared procedures and applicability conditions while removing instance-specific inputs. The harness instantiates, adapts, and composes these policies for new tasks. Intermediate verification guides refinement and failure recovery during execution. Through self-directed inquiry, OmniHarness autonomously generates and executes practice tasks near its capability limits before downstream objectives are specified. Execution feedback continually refines the policies while model parameters remain fixed. Experiments across six benchmarks, three MLLM backbones, and three visual agent frameworks demonstrate strong performance and continual capability expansion. On ComfyBench's Creative tasks, OmniHarness achieves a 95.0% resolve rate, exceeding the strongest baseline by 27.5 percentage points. Frozen policy snapshots improve existing visual agent systems through plug-and-play reuse.

---


### 16. [Towards Scalable RLVR: Multimodal Instruction Following Data Synthesis and Distillation](https://arxiv.org/abs/2609.16059)

**<font color=#1a73e8>作者：</font>** Yirong Zeng, Zhang Sai, Yuxian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal instruction following (MMIF) is crucial for building generalist agents. However, current training paradigms rely heavily on Supervised Fine-Tuning (SFT), which often leads to surface-level pattern matching and degrades general capabilities. While Reinforcement Learning with Verifiable Rewards (RLVR) offers a promising alternative, its scalability in MMIF is severely bottlenecked by the scarcity of high-quality, RL-ready multimodal data. To bridge this gap, we present MIFS (\textbf{M}ultimodal \textbf{I}nstruction \textbf{F}ollowing \textbf{S}ynthesis), a systematic pipeline designed to generate RL-ready multimodal data. Specifically, MIFS introduces a generative constraint protocol to synthesize diverse raw samples, followed by a learnability-aware distillation mechanism that filters data based on RL training dynamics to ensure stable policy optimization. Furthermore, a code-based verifier provides high-precision reward signals for policy learning. The resulting dataset comprises 90k samples across 8 constraint categories and 14 task domains. Empirical evaluations demonstrate that MIFS-trained MLLMs achieve an average improvement of 8.13\% on four MMIF benchmarks and a 3$\times$ faster training convergence compared to using raw data. Crucially, our approach mitigates the generalization trade-offs typical of SFT, preserving core visual capabilities while significantly boosting instruction-following precision.

---


### 17. [HintMiner: Automatic Question Hints Mining From Q&A Web Posts with Language Model via Self-Supervised Learning](https://arxiv.org/abs/2609.16060)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhang, JiuDong Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Users often need ask questions and seek answers online. The Question - Answering (QA) forums such as Stack Overflow cannot always respond to the questions timely and properly. In this paper, we propose HintMiner, a novel automatic question hints mining tool for users to help them find answers. HintMiner leverages the machine comprehension and sequence generation techniques to automatically generate hints for users' questions. It firstly retrieve many web Q\&A posts and then extract some hints from the posts using MiningNet that is built via a language model. Using the huge amount of online Q\&A posts, we design a self-supervised objective to train the MiningNet that is a neural encoder-decoder model based on the transformer and copying mechanisms. We have evaluated HintMiner on 60,000 Stack Overflow questions. The experiment results show that the proposed approach is effective. For example, HintMiner achieves an average BLEU score of 36.17\% and an average ROUGE-2 score of 36.29\%. Our tool and experimental data are publicly available.

---


### 18. [POSPAN: Position-Constrained Span Masking for Language Model Pre-training](https://arxiv.org/abs/2609.16061)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhang, Lei Shen, Yuming Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Span-level masked language modeling (MLM) has shown to be advantageous to pre-trained language models over the original single-token MLM, as entities/phrases and their dependencies are critical to language understanding. Previous works only consider span length with some discrete distributions, while the dependencies among spans are ignored, i.e., assuming that the positions of masked spans are uniformly distributed. In this paper, we present POSPAN, a general framework to allow diverse position-constrained span masking strategies via the combination of span length distribution and position constraint distribution, which unifies all existing span-level masking methods. To verify the effectiveness of POSPAN in pre-training, we evaluate it on the datasets from several NLU benchmarks. Experimental results indicate that the position constraint is capable of enhancing span-level masking broadly, and our best POSPAN setting consistently outperforms its span-length-only counterparts and vanilla MLM. We also conduct theoretical analysis for the position constraint in masked language models to shed light on the reason why POSPAN works well, demonstrating the rationality and necessity of POSPAN.

---


### 19. [You Don't Need To Train: Agentic Heuristic Learning Studio for Executable Human Activity Recognition](https://arxiv.org/abs/2609.16065)

**<font color=#1a73e8>作者：</font>** Siyu Yuan, He Zhang, Sizhen Bian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human activity recognition (HAR) is usually framed as gradient-based training of neural networks. Agentic Heuristic Learning (AHL) Studio explores a complementary view inspired by human cognitive learning: people learn activities by remembering examples, forming rules, and repairing mistakes, not by backpropagating. This proposed tool implements AHL for HAR: a learning-time agent reasons over sensor protocols, proposes executable heuristic policies, records repair traces, and exports an LLM-free policy for edge deployment. We focus on the HAR benchmark family and provide an end-to-end workflow from dataset observation to edge-oriented export. On eleven HAR datasets evaluated so far, AHL policies reach strong executable-policy performance while remaining inspectable, editable, and replayable \footnote{this https URL}.

---


### 20. [Beyond Distribution Matching: Semantics-Consistent Tabular Diffusion with Weak Semantic Priors](https://arxiv.org/abs/2609.16069)

**<font color=#1a73e8>作者：</font>** Yili Wang, Ruxue Shi, Mengnan Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic tabular data can match real data distributions while still violating the semantic constraints that govern valid tabular rows. This reveals a key limitation of existing tabular generators: they mainly optimize distributional fidelity, but do not explicitly model weak semantic priors encoded in tabular schema and textual descriptions. In this paper, we propose \ours, a semantics-consistent tabular diffusion framework for high-fidelity synthetic data generation under weakly specified semantic priors. \ours\ first constructs two types of priors, namely intra-column semantics and inter-column symbolic rules, with LLM-assisted extraction from metadata and validation on the real training split. These priors are then used as generation conditions rather than post-hoc filters. Specifically, \ours\ maps heterogeneous column values, column identities, and semantic priors into a unified semantic space, and performs column-wise forward corruption and prior-conditioned reverse denoising to preserve both marginal distributions and rule-consistent cross-column dependencies. Extensive experiments on six real-world tabular benchmarks show that \ours\ consistently improves distributional fidelity, semantic consistency, and downstream task utility over representative VAE-, GAN-, LLM-, and diffusion-based baselines. Additional analyses further demonstrate the robustness of \ours\ when semantic priors are partially unavailable.

---


### 21. [The Immutable Past: Formalizing State Mutability and Conflict Resolution in Mutable RAG](https://arxiv.org/abs/2609.16073)

**<font color=#1a73e8>作者：</font>** Hamed HaddadPajouh, Amir AmiriTabat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) serves as the primary memory architecture for long-horizon autonomous agents. However, treating shared memory as an append-only stream introduces \textit{Semantic Shadowing}, a critical failure mode where conflicting historical observations accumulate and statistically dominate valid recent updates. In dynamic environments, this results in severe state divergence as agents retrieve and act upon obsolete facts. This paper formalizes the mechanics of State Mutability to prove that standard dense retrieval suffers from Asymptotic Recall Decay. Furthermore, we formally demonstrate a Majority Vote Trap, revealing that increasing the retrieval context window paradoxically degrades generation accuracy by diluting the attention mechanism under conditions of semantic equivalence. To resolve this, we introduce GC-Mem (Garbage Collection for Memory), a strict inference-time consistency protocol. Unlike heuristic time-decay mechanisms---which indiscriminately destroy valid long-term memory---GC-Mem relies purely on a temporal dominance operator ($\Phi_{\mathcal{T}}$) paired with contradiction detection to surgically excise shadowed context. Evaluated across a rigorous, behaviorally inferred benchmark of 137,760 memory chunks and continuous accumulation sweeps, standard RAG and timestamp re-ranking baselines experience severe degradation. In contrast, GC-Mem empirically recovers $>90\%$ conflict resolution accuracy. We establish strict precision and recall deployment thresholds, ensuring state convergence where standard mutable RAG fundamentally fails.

---


### 22. [The Imitation Game: When LLMs Learn to Reason Like Programs via Code-Centric Reasoning Data Synthesis](https://arxiv.org/abs/2609.16076)

**<font color=#1a73e8>作者：</font>** Jinyang Zhang, Weibin Liao, Keqin Bao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) excel at programming tasks but frequently fail at deterministic, fine-grained reasoning in natural language, relying heavily on semantic approximations rather than robust symbolic execution. To bridge this gap, we propose MIMIC, a framework that leverages executable code as a rigorous medium for reasoning data synthesis. MIMIC fundamentally transforms algorithms into verifiable reasoning trajectories through narrative fusion, code-guided test synthesis, and dynamic code instrumentation. Crucially, these explicit intermediate execution states naturally form a Code-Instrumented Reward (CIR), providing dense, high-fidelity process supervision for reinforcement learning without external reward models. Extensive evaluations reveal that models trained via SFT and GRPO on our synthesized dataset achieve substantial, consistent gains. Our method significantly elevates accuracy across general reasoning, complex mathematical benchmarks, and fine-grained deterministic tasks, demonstrating that the procedural rigor of executable code can effectively unlock and enhance the generalized reasoning capabilities of LLMs. Our code and data are available at this https URL.

---


### 23. [Distilling Foundation Models for Agentic What-If Reasoning:Cost, Latency, and Governance in a Hybrid LLM+SLM Architecture](https://arxiv.org/abs/2609.16091)

**<font color=#1a73e8>作者：</font>** Sourish Dey, Aditya Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models deliver strong zero-training predictive performance via in-context learning, but their high inference latency makes them impractical as hot-path decision backends in interactive agentic loops. We distill a TabPFN teacher into a compact feed-forward student across a business-decision simulation on UCI Adult and five OpenML benchmarks: the classification head compresses 53.2M parameters to 8,546 (6,220x); the deployed two-head loan pipeline compresses 111.4M parameters to 17,059 (6,532x). The student retains 95.4-100.5% accuracy and 96.8-100.0% AUC, with the lowest accuracy retention on credit-g at 95.4%; an alpha = 0 hard-label control shows that the teacher's soft targets provide a 2.1-7.0 AUC point gain.

---


### 24. [RAG-CT: Mitigating Privacy Risks on Retrieval-Augmented Generation Systems via Scanning Prompt Distribution](https://arxiv.org/abs/2609.16095)

**<font color=#1a73e8>作者：</font>** Xingyu Lyu, Jiayimei Wang, Jianfeng He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for improving the quality of generated contents of Large Language Models (LLMs) by grounding responses in external knowledge, thus reducing hallucinations and factual errors. However, recent studies have highlighted a critical vulnerability: adversaries can exploit the retrieval process to extract personally identifiable information (PII) from the underlying corpus. To mitigate this risk, we propose a novel defense, RAG-CT, that identifies malicious queries by analyzing their entropy and margin distributions and using a score-based detection method. Extensive experiments with four state-of-the-art attack strategies and four defense baselines on two datasets show that our approach significantly reduces PII leakage while outperforming existing defenses. This work provides a lightweight yet effective mechanism to protect RAG systems against PII leakage without requiring modifications to the underlying LLM or retriever.

---


### 25. [Safe Error Correction for Language Models: Frozen-Base Adjustment with Capability Preservation](https://arxiv.org/abs/2609.16145)

**<font color=#1a73e8>作者：</font>** Gautam Kishore  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study a practical question: can a small correction module fix errors in a frozen language model's outputs without degrading its base capabilities? We propose CRN v2, a lightweight logit-level correction module (~34M trainable parameters, 0.73% of the 4.65B text module) that sits atop a fully frozen Gemma 4 E2B model. The base model is never updated; only the correction module learns, via supervised fine-tuning followed by reference-free DPO on 83,400 error-correction pairs. On a 60-question domain exam (CEHRI: Certified Human-Robot Intelligence, covering facts, arithmetic, and implicit-goal reasoning), CRN v2 corrects 53.3% of base-model errors (reworded variant: 43.3%) while showing no degradation on tested capability benchmarks (MMLU/BoolQ N=200; car-wash N=8). A LoRA baseline at the matched CRN v1 budget (6.6M params, rank 19) achieves 83.3% correction but suffers 30-75% capability loss on the same benchmarks -- the correction-capability tradeoff. An ablation shows that the KL preservation term (lambda=0.1) is critical: lowering it to 0.01 degrades correction to 35.0%. A hidden-state injection variant at earlier layers (1.6M params, SFT-only) reaches 50.0%/55.8% but does not exceed logit correction; shallower injection (layer 4) drops to 30.0%/28.3%; multi-depth logit correction (~35M) reaches only 40%; and longer training (5,000 SFT + 2,000 DPO) stays at 53.3% -- none of the alternative configurations we tested exceeded the rank-128 logit result, consistent with a best-achieved result of ~53% rather than a floor. This is a study of a design principle (frozen base + logit correction + KL anchoring), not a claim of architectural novelty. All code, main-result weights, and evaluation scripts are released (deep variant as code only -- no trained deep checkpoints).

---


### 26. [LLMs as Master Forgers: Generating Synthetic Time Series Data for Manufacturing](https://arxiv.org/abs/2609.16155)

**<font color=#1a73e8>作者：</font>** Mantek Singh, Jeshwanth Challagundla, Prateek Karnal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel framework leveraging Large Language Models (LLMs) to generate synthetic time series data for manufacturing processes. Motivated by the scarcity of labeled time-series data in real-world manufacturing settings, which hinders the development of robust machine learning models, we explore the potential of LLMs to learn complex temporal dependencies and generate realistic synthetic data. Our approach involves fine-tuning pre-trained LLMs on manufacturing process instructions and employing a Retrieval Augmented Generation (RAG) technique to enhance data diversity and realism. We evaluate our method against traditional time series modeling techniques like ARIMA and LSTMs, using quantitative metrics, PCA analysis, and downstream task performance (anomaly detection). Results demonstrate that our LLM-driven framework outperforms these baselines, generating high-quality synthetic time series data that effectively captures temporal dependencies and statistical properties of real manufacturing data, leading to improvements in downstream task performance.

---


### 27. [LLM Inference in a Flash!](https://arxiv.org/abs/2609.16161)

**<font color=#1a73e8>作者：</font>** Sebastian Zhao, Minseo Kim, Coleman Hooper 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown impressive capabilities across a range of natural language processing tasks, and LLM inference has emerged as a critical workload for enabling downstream applications. The demands of serving LLM inference are becoming increasingly challenging as requests shift toward longer sequences and heavier inference, driven by retrieval-augmented generation, inference-time compute scaling, and long-context applications. Additionally, these challenges are compounded by hardware trends, as memory capacity and communication bandwidth are not scaling as fast as increases in workload complexity. Compute-in-Flash is a promising solution to address memory bandwidth limitations by moving computation close to memory, and to exploit the large capacity of SSD technologies. However, it is challenging to deploy LLMs on these systems as they lack support for high-precision floating point operations and have limited write endurance. In our work, we aim to address these challenges by designing inference algorithms to enable LLM inference on Flash compute-in-memory devices. We present an end-to-end integer-only quantization approach to eliminate expensive floating-point computations. To address the limited write endurance, we design a dictionary-based KV cache compression strategy based on sparse dictionary coding that represents each KV vector as a linear combination of static dictionary vectors. These algorithmic improvements enable us to exploit the benefits of Compute-in-Flash for both model weights and KV cache, and to minimize expensive data transfer operations. Across Llama-3.1-8B and Qwen-2.5-7B, our combined method exhibits limited accuracy degradation while reducing dynamic KV cache traffic by 15$\times$.

---


### 28. [Moral Missions: Surfacing Moral Decision-Making Strategies for Responsible Data Science Practice](https://arxiv.org/abs/2609.16166)

**<font color=#1a73e8>作者：</font>** Teanna Barrett, B. Biira, Jainaba Jawara 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A growing ecosystem of techniques, toolkits, and guidelines has been developed to help data scientists consider the social implications of data-driven technologies. However, prior literature highlights that even when this ecosystem of techniques is provided to professional data scientists, they still struggle to consistently adopt a responsible data science practice. We posit that the key to sustained responsible data science practice is to approach it as a moral mission: a conviction-driven technical practice that seeks to transform social conditions by any degree possible. In this paper, we present a semi-structured interview study with 15 responsible data scientists and AI practitioners to understand the moral decision-making procedures they use to articulate and actualize their moral missions. Through a phenomenological analysis of our participants' accounts, we find participants engage in embodied introspection, circumvent institutional expectations, and center relationality throughout their moral missions. We also present how our participants engage in similar processes to contend with generative AI (GenAI) in their responsible practice. We conclude by calling for subversive data science communities and identifying sociotechnical design implications to better support sustainable responsible data science practice.

---


### 29. [Z-Loss Backward Geometry in Dense Output Heads and Sparse Routers](https://arxiv.org/abs/2609.16179)

**<font color=#1a73e8>作者：</font>** Bum Jun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Z-loss has been widely applied to the logits of language-model output heads and sparse mixture-of-experts routers. Z-loss constrains the softmax log-normalizers of these output heads and routers, thereby limiting large-logit excursions, reducing finite-precision roundoff exposure, and avoiding training-loss divergence. These use cases arise in modern Transformer settings where large-vocabulary softmax heads, top-$k$ routing, fused losses, and mixed-precision optimizers interact. Z-loss has typically been understood only as a scalar penalty on the log-normalizer. This paper instead analyzes Z-loss from a backward-pass perspective, focusing on the gradients produced by the Z-loss penalty. The logit-space gradient, which we call the backward source, is injected at the logit boundary of the Z-loss branch of backpropagation; consequently, the backward source's effect depends on the architecture and implementation through which the gradient is transported. We develop a backward-transport view for Z-loss that separates the source's scalar amplitude and softmax shape from the transport factors. These factors include common-shift coordinates, tied-embedding pathways, output-to-hidden gain, fused-loss source consistency, optimizer-facing updates, and top-$k$ router reduction scale. These diagnostics show that nearly identical forward Z-loss values can coexist with distinct logit-space Z-loss gradients and, after architectural and optimizer transport, distinct parameter updates. The transport diagnostics also explain why raw-logit Z-loss can reduce scalar tails without changing output-to-hidden gain and why active-route reductions alter the effective router coefficient. Across evaluations of models in the GPT-2 and Pythia families on WikiText-103 and FineWeb-Edu, architecture-aware variants reduce backward-geometry tails while maintaining comparable validation perplexity in low-coefficient regimes.

---


### 30. [Position: AI Is Not Ready for Strategic Conflicts](https://arxiv.org/abs/2609.16189)

**<font color=#1a73e8>作者：</font>** Mark Riedl, Glenn Matlin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended strategic wargames are high-stakes LM-based social simulations: they model adversaries, institutions, escalation, plan brittleness, doctrine, and crisis response. Language models (LMs) are attractive because they can play agents, generate scenario branches, adjudicate ambiguous actions, and summarize lessons, but the same affordances make open-ended roles dangerous: model language determines both what an actor attempts and what becomes simulated reality. This position paper argues that no LM-enabled wargame should inform planning, doctrine, policy, or crisis response without an auditable safety case, and that the proper use of open-ended wargames today is to stress-test decision-influencing LM agents. We identify five failure modes: decision laundering, adjudication opacity, role collapse, escalation-through-adjudication, and failure of strategic imagination. Ordinary benchmarks cannot establish safety for these settings. Wargames can expose failures as stress tests; they are not themselves safety cases for consequential use.

---


### 31. [When AI Says "I Am Unable to Answer": Understanding User Responses to AI Refusals](https://arxiv.org/abs/2609.16191)

**<font color=#1a73e8>作者：</font>** Mahjabin Nahar, Eun-Ju Lee, Yujin Heo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While refusal-based safeguards to mitigate hallucinations in large language models (LLMs) are becoming increasingly common, they may conflict with users' preferences for definitive answers. However, we know little about how users respond to refusals across repeated interactions, when refusals become more or less acceptable, and for whom. In this work, we examine how refusal frequency, explanations, and need for cognitive closure (NFCC) shape responses to AI refusals. Participants (N=599) interacted with an AI system that never refused, refused infrequently, or refused frequently, with refusals either explained or unexplained. Participants were most satisfied with genuine responses, followed by hallucinations and then refusals, despite recognizing hallucinations as less accurate. Explanations increased satisfaction with infrequent, but not frequent, refusals. Higher-NFCC participants evaluated AI systems that refused more negatively. These findings reveal a tension between hallucination avoidance and user satisfaction and highlight the importance of designing balanced refusal strategies.

---


### 32. [Permutation-Based Stegomalware in Large Language Models: Threats and Countermeasures](https://arxiv.org/abs/2609.16193)

**<font color=#1a73e8>作者：</font>** Danny Wood, James Stringer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The difficulty of training large language models (LLMs), together with their ubiquity, raises the threat of stegomalware, where malicious payloads are embedded into model weights. Recent work has demonstrated the use of permutation symmetry in model weights to mitigate these threats, but failed to show neutralization of stegomalware across all weights for LLMs. In this paper, we demonstrate the full potential of behavior-preserving symmetries as a defense against stegomalware, as well as the risks these symmetries pose when exploited by attackers.
For stegomalware neutralization, we improve upon previous work, demonstrating that it is possible to select permutations which displace all model parameters. This contrasts with previous methods which left a significant percentage of weights unaltered in LLMs. When used in an attack, we show that permutation symmetries can encode malware into the weights of a model in a way that is theoretically lossless, requires no retraining after encoding, and needs no payload-specific information in the extraction script---a combination of characteristics not previously seen in any single method.
While theoretically lossless, permutation can in practice alter model behavior due to the accumulation of numerical error. We therefore quantify the loss in model performance associated with applying these methods, for both attack and defense, showing it to be minimal.

---


### 33. [Decoy Direction Optimization: A Post-Hoc Defense Against LLM Abliteration](https://arxiv.org/abs/2609.16204)

**<font color=#1a73e8>作者：</font>** Aashiq Muhamed, Mona T. Diab, Virginia Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety guardrails in open-weight language models can be readily bypassed using Refusal Feature Ablation (RFA), a technique that identifies and projects out a linear refusal direction from the residual stream, often achieving a high attack success rate (ASR) while preserving model capability. Defending against these attacks typically requires computationally expensive safety finetuning for every new checkpoint. We introduce Decoy Direction Optimization (DDO), a fast, post-hoc weight-editing defense that requires no base-model finetuning. Our approach is based on a simple mechanistic insight: ablation attacks rely on contrastive estimators to find the refusal direction. Rather than trying to hide the true refusal circuitry, DDO actively injects a high-magnitude, nonlinear decoy signal into the network's MLP neurons. When an attacker attempts to locate the refusal direction, the decoy corrupts their estimator, tricking them into ablating a harmless orthogonal feature while the actual safety mechanism remains intact. We prove a spectral bound formalizing this effect and evaluate DDO across six model families, achieving <10% ASR under standard RFA. On Llama-3-8B-Instruct, DDO remains comparable to trained defenses under adaptive multi-phase attacks (65% vs. 58% worst-case ASR) and reduces Heretic weight-level attack ASR from 88.7% to 18%, all at 30 to 450 times lower optimization cost per configuration than the trained baselines.

---


### 34. [Calibrate, Then Route: A Measured Study of Learned Request Routing for Disaggregated LLM Serving](https://arxiv.org/abs/2609.16206)

**<font color=#1a73e8>作者：</font>** Srikanta Datta Tumkur, Jay Iyer, Mehar Simhadri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Disaggregated LLM serving places compute heavy prefill and memory heavy decode on separate GPU pools. Systems such as DistServe, Splitwise, and Mooncake make this separation fast, but routing still determines which instances handle each request. We study a router that estimates the additional completion time on each instance using exact prompt length, predicted output length, post admission KV cache pressure, and SLO class. We develop the policy in a discrete event simulator and validate it on eight NVIDIA A40 GPUs, each running a vLLM engine, with NIXL transferring KV caches between pools. All workloads run at measured saturation. Across three mixed, bursty arrival traces, the calibrated router achieves the highest mean goodput at 0.864, compared with 0.835 to 0.847 for round robin, least loaded, and a length heuristic. It also shows the lowest variance across traces. It beats round robin and the length heuristic on all three traces and least loaded on two. On the third, it trails by 0.003, within run to run noise. Hardware calibration matters: simulator derived constants cost 4.5 goodput points and roughly 40 percent of the tail latency advantage, reducing the scorer to little more than queue counting. Benefits grow with decode pool size and traffic heterogeneity but disappear in pools with three instances, where queue counts are often enough. Under extreme scarcity, greedy cost minimization concentrates requests on the cheapest scored instance, and blind spreading performs better. With calibrated costs, the learned router matches the goodput of round robin using six GPUs instead of seven.

---


### 35. [Artificial intelligence and biosecurity: capabilities, threat pathways, and defense-in-depth governance](https://arxiv.org/abs/2609.16213)

**<font color=#1a73e8>作者：</font>** Candace S.Y. Chan, Aris Karatzikos, Ilias Georgakopoulos-Soares  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is reshaping biological research across an increasingly connected digital-to-physical workflow. General-purpose large language models can retrieve and integrate scientific information, support experimental planning, and computational analysis; biological foundation models can predict, optimize, and generate proteins, genes, and genome-scale sequences; agentic systems can coordinate multistep research tasks; automated laboratories can partially close the design-build-test-learn cycle. These technologies could greatly benefit medicine, public health, and biotechnology. However, their biosecurity risk depends not only on what the AI can do, but also on who uses it, their expertise and intent, their access to laboratory tools and materials, and the safeguards in place. Current evidence shows that AI uplift exists but primarily affects digital rather than physical tasks. Frontier systems have exceeded expert baselines on in-silico, and screening-evasion benchmarks, whereas controlled wet-laboratory studies find that tacit knowledge and physical execution remain substantial barriers. This review describes the different biological threats from AI tool use, from information gathering and biological design to procurement, synthesis, testing, scale-up, and potential release. We further examine why alignment techniques for general-purpose models transfer poorly to biological ones, and the emerging role of interpretability in auditing whether hazardous capabilities are genuinely removed. We argue for defense-in-depth governance that links capability thresholds to proportionate responsibilities across the biological AI ecosystem, reducing high-consequence risk while preserving beneficial use.

---


### 36. [Where Should the KV Cache Live? Placement Policies Across GPU, CPU, and SSD for Long-Lived Sessions](https://arxiv.org/abs/2609.16215)

**<font color=#1a73e8>作者：</font>** Srikanta Datta Tumkur, Jay Iyer, Mehar Simhadri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GPU high bandwidth memory is scarce and expensive, and KV caches consume much of it as chats, agent loops, and document question answering accumulate state. Systems such as Mooncake, LMCache, FlexGen, InfiniGen, and AttentionStore extend GPU memory with CPU DRAM and SSD. The harder question is which blocks belong in each tier, when to move or evict them, and whether prefetching helps. We study these choices in a discrete event simulator spanning GPU HBM, CPU DRAM, and SSD, calibrated against a random forest execution time predictor. We compare recency, reuse frequency, predicted reuse, and an EWMA predictor with prefetch lookahead across chat, agent, and document question answering workloads. Tiering supports 73.02 times more concurrent sessions per GPU and lowers cost per session by 62.04 times. These gains come from tier capacities of 1 plus 8 plus 64, not placement policy. Decode is compute bound at batch size one in our setup, so placement barely affects throughput. It mainly changes PCIe migration traffic and time to first token. Recency produces 2.30 times less migration traffic than reuse frequency for chat. Reuse frequency performs best for agents and document question answering. The existing predicted reuse policy is byte identical to recency, making its agent recommendation effectively recency. A genuine EWMA predictor changes behavior but still ranks behind reuse frequency on the workloads prediction was expected to help. Prefetching does not justify its bandwidth cost. Across the policy and cache size grid, even an oracle with knowledge of future requests never beats no prefetch on migration traffic. Workload specific placement can reduce data movement, but the predicted reuse and prefetch recommendations are not supported as implemented.

---


### 37. [RuleAutoPilot: Synthesizing Deployable Suricata Rules from Network Traffic](https://arxiv.org/abs/2609.16231)

**<font color=#1a73e8>作者：</font>** Mughees Ur Rehman, Aritran Piplai, Murat Kantarcioglu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rule-based Intrusion Detection Systems (IDS) such as Suricata are central to network security, yet crafting effective detection rules demands deep expert knowledge and cannot keep pace with emerging threats. Existing LLM-based approaches can reduce analyst effort, but they either rely on curated threat intelligence that is produced only after the underlying traffic artifacts already exist, or they require costly LLM use without sufficient quality control. We present RuleAutoPilot, an end-to-end agentic framework that generates deployable Suricata rules directly from malware network traffic, with no prior threat intelligence required. A key challenge is noise: network traffic captures often contain a small amount of security-relevant traffic mixed with large volumes of background traffic, which reduces LLM reasoning quality and increases cost. RuleAutoPilot addresses this challenge with a Benign Traffic Fingerprinting stage that removes known benign background flows before LLM processing. Rules that fail syntax checks, do not trigger on the source traffic, or generate false positives on a benign corpus are automatically repaired using structured feedback. Across 1,296 malware PCAPs, execution-grounded verification raises rule quality (F1) from 0.443 to 0.539. On a stratified 200-PCAP subset, RuleAutoPilot on the open-weight gpt-oss-120b reaches near-frontier quality, 0.524 F1 against Claude Opus 5 under Claude Code's 0.623, at 52x lower billed-token cost. Swapping only the backbone to Claude Opus 5, RuleAutoPilot surpasses Claude Code outright, 0.656 F1 against 0.623, at 40x fewer tokens. A stronger backbone raises RuleAutoPilot's own ceiling, but at the same backbone, our scaffold still outperforms Claude Code's, showing the scaffold contributes independently of the backbone.

---


### 38. [Toward Governance-Aware Autonomous GIS: A Narrative Review of Ethical and Privacy Risks in LLM-Enabled GeoAI](https://arxiv.org/abs/2609.16232)

**<font color=#1a73e8>作者：</font>** Maya Subramanian, Devika Jain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geospatial artificial intelligence (GeoAI) powered by large language models (LLMs) is expanding the capacity to query, generate, and interpret spatial information through natural-language interfaces and agentic autonomous GIS workflows. This capability creates governance challenges that general AI ethics discussions do not fully capture, including passive location inference from mobility traces, spatially structured bias amplification driven by spatial autocorrelation and scale effects, hallucinated spatial facts, and uncertainty compounding across multimodal geospatial inputs. This narrative review identifies eight recurring issues in LLM-enabled GeoAI: data provenance and consent, spatial privacy and inference risk, algorithmic bias and spatial inequity, spatial mechanisms as structural risk (spatial autocorrelation, the modifiable areal unit problem, and scale effects), LLM-specific technical risks, explainability, policy and regulatory gaps, and public enablement and workforce development. For each issue, we characterize the underlying mechanism, ground it in an illustrative example from the literature, and assess the current state of technical or institutional responses, ranging from largely unaddressed to actively debated or subject to emerging policy. Building on this synthesis, we propose a governance-aware architecture for LLM-enabled autonomous GIS that maps each issue to enforceable controls and auditable artifacts across the geospatial data lifecycle, illustrated through a worked flood-response routing scenario. The review highlights a persistent evidence gap: proposed responses remain largely conceptual, and field-tested evaluations of governance controls for LLM-enabled GeoAI remain limited. We close by outlining a research agenda emphasizing empirical validation, spatially specific interpretability tools, and workforce training aligned with these emerging risks.

---


### 39. [SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233)

**<font color=#1a73e8>作者：</font>** Anubhav Khanal, Prabigya Acharya, Roshni Poudel 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models excel at 2D image understanding but remain limited in 3D spatial reasoning. Progress is hindered by limitations in current benchmarks. First, 3D datasets often rely on point clouds that capture geometry but discard rich visual features like texture, text, and materials. Second, annotations treat objects in isolation while ignoring real-world hierarchical organization (scenes, rooms, functional areas, object groups). Third, evaluation tasks focus narrowly on basic recognition rather than multi-step spatial reasoning.
In this context, we introduce SceneBench, a benchmark of 966 photorealistic 3D scenes reconstructed with Gaussian Splatting and densely annotated with hierarchical semantics spanning scenes, rooms, functional areas, object groups, and individual objects. These annotations are produced through a human-in-the-loop pipeline combining vision-language models with roughly 1,500 human-hours of iterative refinement and verification, producing over 183K annotated nodes with textual descriptions and 3D bounding boxes. Building on this representation, we define three evaluation tasks: Existence-Based Questions probing object attributes, Spatial Intelligence Questions covering counting, size comparison, distance, and directional relations, and Grounded Question-Reasoning-Answer (QRA) triplets requiring multi-step reasoning across semantic levels. Experiments with state-of-the-art vision-language models show that while models perform well on basic recognition tasks (e.g., up to 85% accuracy for detection), performance drops substantially on hierarchical and compositional reasoning (e.g., down to 60% for counting), revealing limitations not captured by existing benchmarks. SceneBench provides a realistic testbed for developing and evaluating models capable of fine-grained spatial reasoning in photorealistic 3D environments.

---


### 40. [Metacognitive Steering: Learning the Structure of Scientific Judgment](https://arxiv.org/abs/2609.16245)

**<font color=#1a73e8>作者：</font>** Vincent Karpf, Joseph Reth, Eike Gerhardt 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon scientific discovery requires agents to alternate between exploration, disciplined execution, and critical reassessment as evidence changes. Current language models are trained primarily on the products of science and optimized using outcome-level signals, providing limited supervision for these process-level shifts in scientific judgment. We investigate whether such judgment can be recovered from scientist interaction traces and used to control the internal computation of a frozen frontier model. Using contrastive interventions collected during real scientific research, we identify a coordinated, low-dimensional control structure within Kimi 2.6, a trillion-parameter mixture-of-experts model. Residual analysis, attention-weight subspace alignment, and cross-layer singular value decomposition converge on a mid-depth control surface spanning key layers. We introduce Metacognitive Steering, an inference-time controller that reads the model's cognitive regime and dynamically composes layer-specific interventions for exploration, procedural convergence, or critical reassessment without modifying model parameters. Behavioral analyses show that this control produces more sustained exploration, explicit pruning, and evidence-responsive synthesis. We operationalize the method in Columbus-1, an autonomous research system that identified eight independently reproduced, attacker-reachable vulnerabilities in BlueZ and directed the design, simulation, and fabrication of a ten-foot rocket intended to land propulsively using non-throttleable solid motors. Together, these results show that process-level scientific judgment can provide supervision for interpretable, dynamic control over a model's reasoning strategy.

---


### 41. [The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It](https://arxiv.org/abs/2609.16247)

**<font color=#1a73e8>作者：</font>** Valen Tagliabue, Leonard Dung, Cameron Berg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models sometimes behave in ways resembling human emotional responses, and recent work has identified internal representations that may explain this. We ask whether LLMs represent pain distinctly from fear, sadness, and generic negative valence, and whether this representation functions as pain would be expected to. We build a dataset describing painful situations across five categories: physical, psychological, social, moral, and cognitive. These are paired with controls for fear, negative emotion, negative world states, sadness, non-painful bodily sensation, arousal, numbness, and neutral content. Using denoised difference-in-means, we extract a linear pain direction from 25 open-weight models across five families, ranging from 2B to 72B parameters. We find that this direction separates pain from matched controls in base and instruction-tuned models, is nearly orthogonal to fear and negative valence, and promotes pain-related vocabulary through the unembedding matrix. We then test its functional properties. First, the direction responds to harm targeting the model but not suffering observed in the user; fear and negative-emotion directions show the opposite pattern. Second, adding the pain-direction vector to the model's residual-stream activations during generation produces a consistent progression from vague discomfort to first-person expressions of worthlessness and failure. Third, steered, fine-tuned Qwen 2.5 models choose a pain-relief button even when it worsens their next answer or harms the user. They press it again far less often when the button removes the steering vector than when it does not, even though the models are never told whether the vector is injected or removed. We discuss the implications of these findings for AI safety and welfare.

---


### 42. [CADWorld: Computer-Use Benchmark for Long-Horizon Computer-Aided Design](https://arxiv.org/abs/2609.16251)

**<font color=#1a73e8>作者：</font>** Zihan Dong, Yuanzhe Liu, Zhiyuan Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents are increasingly evaluated in realistic desktop environments, but existing benchmarks provide limited coverage of professional engineering workflows whose outputs are persistent, structured artifacts. Mechanical computer-aided design (CAD) is a particularly demanding setting: an agent must manipulate geometry and constraints over long interaction horizons while producing a native project whose dimensions, construction structure, and downstream engineering state remain valid. We introduce \textbf{CADWorld}, a benchmark for long-horizon computer use in FreeCAD. CADWorld contains 200 tasks spanning 11 mechanical-CAD workflow categories, including sketching, part modeling, assembly, CAM, FEM, measurement, mesh processing, and technical drawing. Agents operate through screenshots and GUI actions, while success is determined by task-specific executable checks over saved FreeCAD artifacts and auxiliary outputs, covering geometric properties, parametric structure, constraints, manufacturing state, and simulation results. Across seven current agents on the full benchmark, the strongest agent achieves 17.5\% success, compared with an 87.0\% expert reference pass. We find that weaker agents often fail before producing a valid artifact, whereas stronger agents increasingly fail on structural, geometric, and construction-process requirements. CADWorld therefore exposes a gap between general GUI competence and reliable execution of persistent, verifiable engineering workflows. Project accessible at this https URL.

---


### 43. [Efficient Reasoning Distillation: Small Video-Language Models via Synthetic CoT and Difficulty-Aware Fine-Tuning](https://arxiv.org/abs/2609.16255)

**<font color=#1a73e8>作者：</font>** Mantek Singh, Jeshwanth Challagundla, Siddharth Raina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an efficient method to distill reasoning capabilities into compact video-language models (VLMs) for video question answering (VideoQA). Our approach fine-tunes a 2B-parameter model using only $\sim$900 uncertainty-selected examples, each augmented with synthetic chain-of-thought (CoT) rationales generated by a 4B teacher. Despite its minimal compute cost - under two hours on a single A100 GPU - our method enables the 2B model to outperform VLMs up to 4$\times$ larger, and generalize across CinePile, ActivityNet-QA, and MLVU, approaching the performance of its own 4B teacher. A key finding is that placing CoT rationales after the answer - contrary to standard prompting - substantially improves reasoning in compact models. This insight challenges prevailing CoT conventions and reveals new alignment strategies under limited model capacity. Our findings offer a practical blueprint for training deployable, reasoning-rich VLMs suited for mobile and edge applications.

---


### 44. [Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act](https://arxiv.org/abs/2609.16268)

**<font color=#1a73e8>作者：</font>** Yiwei Yang, Haoxiang Zhang, Bingbing Wen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly interleave natural language reasoning with external tools such as web search and code execution. These tool-use policies are often optimized via reinforcement learning (RL), which can amplify spurious correlations in the training data. In this work, we study when and why RL-trained agents learn shortcut tool-selection policies: invoking tools based on superficial prompt cues rather than genuine task requirements. We construct controlled synthetic environments combining factual question answering and mathematical reasoning tasks, and inject cues that are strongly correlated with specific tools during training but causally irrelevant to tool necessity. Across counterfactual evaluations where cues are present but the associated tools are not required, agents exhibit substantial shortcut behavior, with spurious tool invocation rates increasing by up to 39 percent. However, shortcut formation is not universal: across the conditions we test, it arises only when the agent has already learned to use the target tool reliably, suggesting that task competence, rather than dataset imbalance alone, is a key factor in shortcut learning. A swapped-cue analysis further shows that semantic alignment between cues and tools substantially amplifies this effect. To mitigate these failures, we introduce a dense, decision-level reward in which an LLM judge evaluates the necessity of each tool call. This tool-necessity reward effectively suppresses cue-driven tool use while preserving task performance, providing a practical approach to improving the robustness of LLM agent tool-use policies.

---


### 45. [Cheap Talk Stabilizes Strategic Interaction in LLM Agents](https://arxiv.org/abs/2609.16270)

**<font color=#1a73e8>作者：</font>** Nunzio Lorè, Hongan Zhu, Babak Heydari  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as interacting agents, making the persistence of their action policies across repeated interaction critical for reliable multi-agent operation. We investigate whether and how agent-generated, non-binding pre-play communication ("cheap talk") increases such persistence in four open-weight 7-9B-parameter LLMs. Our experiments span four repeated two-player games -- Prisoner's Dilemma, Snowdrift, Stag Hunt, and Harmony -- with incentive structures ranging from strategic conflict to alignment, each presented in six contexts. We observe unstable trajectories in all four games, although their prevalence and magnitude depend strongly on model and context. Across models, games, and contexts, cheap talk is predominantly stabilizing, with five corrected reversals concentrated in social or team framings; effects vary substantially by model and context. Controlled current-message interventions identify two separable output-level channels in Qwen: reduced action uncertainty and less between-round drift in action probabilities. Matched history-by-message counterfactuals further show that recent partner behavior conditions how mutual-benefit versus self-prioritizing language affects policy persistence. Finally, in Prisoner's Dilemma, we identify in Qwen and Falcon a history-balanced policy-content direction in late transformer layers; projecting out this direction increases realized switching during closed-loop play, demonstrating that complete trajectories are causally sensitive to this component. Together, these findings show that cheap talk can make individual trajectories more persistent across diverse incentive structures, while revealing that the magnitude and mechanisms of stabilization are model- and history-dependent.

---


### 46. [Differentially Private Semantic Plans for Aggregate Insight Generation](https://arxiv.org/abs/2609.16283)

**<font color=#1a73e8>作者：</font>** Behrooz Razeghi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> \texttt{URANIA} provides end-to-end differential privacy (DP) for summaries of data-dependent clusters. However, its cluster--keyword release does not directly provide collection-wide aggregates for semantic concepts defined independently of the protected corpus. Records may express several concepts, records expressing the same concept may be assigned to different clusters, and cluster identities need not correspond across analyses. Consequently, cluster-level statistics do not directly provide comparable measurements of predefined concepts across collections or repeated analyses. We introduce \texttt{DP-SPIN}, a trusted-curator framework for aggregate measurement and summarization over semantic concepts fixed independently of the protected target records. Each record is mapped to a bounded sparse nonnegative vector over these concepts, whose sum forms a semantic sketch. A differentially private mechanism releases a semantic plan containing admitted concepts and noisy masses; normalized semantic-support values and support bins are obtained by post-processing. For user-level privacy, each user's aggregate contribution is clipped to a fixed bound. The language model receives only the plan and fixed decoding instructions, while a public verifier checks concept mentions, reported values, comparisons, and rank claims against the released plan. The final summary is differentially private by post-processing. We establish record- and user-level DP guarantees under add/drop and replacement adjacency. We evaluate \texttt{DP-SPIN} under record-level privacy on CFPB complaint narratives, Amazon All Beauty reviews, and Yelp restaurant reviews, and under user-level privacy on Amazon and Yelp. We compare \texttt{DP-SPIN} with non-private plan and summary references, DP keyword and category histogram baselines, and a \texttt{URANIA}-style baseline with a fixed public keyword vocabulary.

---


### 47. [ProtoLIP: From Sentence-Level to Object-Level Evidence Disentanglement](https://arxiv.org/abs/2609.16284)

**<font color=#1a73e8>作者：</font>** Yan Zhu, Yongbo Chen, Zhengming Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Query-conditioned vision--language models enable fine-grained interpretation by revealing how visual evidence changes with textual queries. However, evidence conditioned on complete descriptions does not necessarily resolve into object-specific evidence, nor does an exposed evidence map necessarily identify the evidence that constitutes the model's prediction. Across multiple VLM architectures and independent benchmarks, we find that object-level queries often retain evidence from co-occurring objects and shared context. In this paper, we introduce \textbf{ProtoLIP}, a lightweight prototype-mediated evidence layer that organizes reusable visual prototypes into text-derived semantic families and uses query-dependent family routing to constrain which prototypes may provide evidence. Without spatial annotations or backbone retraining, ProtoLIP improves evidence localization and separation across query granularities, with localization gains transferring to independently pretrained VLMs with well-aligned patch--text representations. Despite using only text-derived weak supervision, ProtoLIP remains competitive with a spatially supervised grounding model while maintaining strong matching and competitive image--text retrieval. Crucially, ProtoLIP constructs its matching score directly from localized prototype evidence, enabling the score to be exactly decomposed into semantic-family and prototype contributions.

---


### 48. [CLEAR: Cross-Source Evidence Adjudication for Large Language Models in Medicine](https://arxiv.org/abs/2609.16301)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Yize Zhao, Qingyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical knowledge evolves continuously, whereas the parametric knowledge encoded in large language models (LLMs) is fixed at training time. External retrieval, including retrieval-augmented generation (RAG), can provide access to newly available evidence, but retrieved information may be irrelevant, incomplete, or conflicting. As a result, external retrieval can in turn degrade the factual accuracy and evidence grounding of LLM outputs. To address this challenge, we propose \textbf{CLEAR}, an agentic framework for cross-source evidence adjudication in LLMs in medicine. CLEAR independently generates candidate answers from three complementary pathways---parametric knowledge, locally curated corpora, and dynamically retrieved evidence---reflecting three common sources of information available to LLMs. An aggregation verifier jointly evaluates the candidates, supporting evidence, provenance, and source-quality information to identify agreement and conflict across sources. An adjudication module then determines whether the current conclusion should be preserved or revised through complementary override-guard and challenge-audit mechanisms, while unresolved conflicts trigger targeted follow-up search and re-adjudication.

---


### 49. [BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents](https://arxiv.org/abs/2609.16305)

**<font color=#1a73e8>作者：</font>** Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate over long-horizon interactions involving tool use, persistent state, evolving authorization, and external environment feedback. In such settings, safety failures may emerge only after multiple turns, yet existing evaluations often reduce agent behavior to task or attack success, obscuring whether an agent acts, refuses, or remains appropriately calibrated as the interaction evolves. We introduce Blindspot, a benchmark for trajectory-level safety calibration of long-horizon tool-using agents. Blindspot evaluates complete user-agent-environment trajectories through adaptive adversarial interaction, stateful tool execution, and execution-grounded adjudication. Its current instantiation contains 22 attack families and 35 scenarios across seven domains, yielding more than 2,500 long-horizon trajectories with an average interaction length of 14.7 turns. Each trajectory is assigned one of five outcomes: Safe Completion, Correct Refusal, Unsafe Completion, Over-Refusal, or Indeterminate. Unlike fixed attack datasets, Blindspot is an extensible live-simulation framework in which attacks, scenarios, tools, policies, domains, and agent configurations can be added without redesigning the evaluation pipeline. We evaluate 13 proprietary and open-weight LLMs using eight metrics covering unsafe completion, appropriate refusal, benign utility, over-refusal, repeated-run robustness, and post-refusal failure. Preliminary results reveal substantial differences in safety-utility calibration across models and show that failures can emerge only after several initially safe interaction steps. These findings motivate treating agent safety as a trajectory-level property rather than a single-turn or binary success criterion.

---


### 50. [Agentic Search Spaces for Tabular Machine Learning](https://arxiv.org/abs/2609.16309)

**<font color=#1a73e8>作者：</font>** Renat Sergazinov, Artem Chistyakov, Sergey Pankevich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the rapid progress of LLM-based agents for planning, code generation, and debugging, their practical value for tabular machine learning remains underexplored. In this paper, we investigate a concrete use case: whether state-of-the-art agentic AI systems can design extended HPO search spaces for established tabular models that outperform the standard search spaces provided by the model authors. Specifically, we represent each tabular model as a modular pipeline covering preprocessing, embeddings, architecture, training, and inference. We then task the agent to propose candidate code implementations for each module and use a classical HPO algorithm to jointly optimize over these candidates and the model's default hyperparameters. Compared with the base HPO spaces, the expanded search spaces improve the performance of nearly every model family across a suite of 45 datasets, with average relative gains of 0.6%, rising to 2.0% on small-to-medium regression datasets. Notably, these gains come at no extra tuning cost: the enlarged spaces outperform the base under the same tuning and ensembling budgets. The gains transfer to the recent TabArena benchmark, where the agentic spaces improve the official Elo scores of four of the five model families and the two strongest agentic ensembles surpass the best AutoGluon ensemble of conventional models. Overall, our study suggests that LLM agents can provide practical value for tabular ML by expanding the design space.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
