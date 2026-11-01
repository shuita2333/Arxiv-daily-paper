# 🧠 大模型相关研究 | 2026年11月02日

> 本类共 **353** 篇论文：已确认 **335** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 151. [Routed Continual Learning](https://arxiv.org/abs/2610.38796)

**<font color=#1a73e8>作者：</font>** Michael Philip, Mahesh Balakrishnan, David Geraghty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agents deployed at scale repeatedly encounter related problems, and it is natural to let them learn from each other's experience rather than starting over each time. Unfortunately, there is no single way to retain that experience that works well across settings, and no way to know in advance which future problems a given experience will help with. A global history preserves every detail but becomes expensive and mixes together experience that may not belong together; compressing that history into one fixed representation limits the cost but can throw away valuable details.
We introduce Routed Continual Learning (Routed CL), an architecture that decides how to partition and retain experience. Past trajectories are grouped into clusters, each of which maintains state using one memory system from a fixed library. Before each run, an LLM-based router either reuses an existing cluster or creates a new one, basing its decision on the problem statement, memory system descriptions, and cluster summaries. We also introduce Context Memory Adapter, which mediates between the memory system and the agentic loop.
We evaluate the architecture on a heterogeneous stream that interleaves 301 instances from the six CL-Bench tasks with 97 banking instances from $\tau^3$-Bench. Across four language models and five matched rollouts, Routed Continual Learning raises normalized reward over a single global in-context learning (ICL) history by 15-30% of the maximum attainable normalized reward, achieves higher mean normalized reward than ICL-only clustering, and reduces estimated API cost by 65-72% relative to Global ICL. These results support approaching continual learning as a routing problem that chooses both a learning mechanism and a state cluster rather than committing to one representation globally.

---


### 152. [CARI: Cross-Boundary Adversarial Runtime Injection in Coding-Agent Workflows](https://arxiv.org/abs/2610.38799)

**<font color=#1a73e8>作者：</font>** Jie Fu, Shuang Wu, Ashish Kundu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents increasingly develop, test, and integrate software whose components are owned by different developers, teams, or services. This exposes a distinct attack surface: a malicious or compromised peer development role can manipulate a live component of the software under development (e.g., a backend service, test harness, CI job, or deployment service) and influence the runtime feedback that another role's coding agent must process to complete its task. Although such a component has legitimate diagnostic authority to report its own state, it has no action authority over the victim's local files, credentials, shell, or development environment. We introduce Cross-Boundary Adversarial Runtime Injection (CARI), a direct runtime-feedback injection setting that exploits this authority mismatch. Rather than explicitly compromising the victim's prompt, model, tools, or local environment, the attacker covertly embeds malicious instructions in task-relevant runtime feedback produced by a peer-controlled development component. The victim then interprets that feedback as part of normal debugging or recovery, and may translate the diagnostic guidance into unauthorized victim-side actions. We instantiate ten different attacks based on CARI, spanning resource exhaustion, information exposure, and development-state manipulation. Across four programming languages and five code-capable models, CARI succeeds in 2,845/3,000 (94.8%) trials. Furthermore, CARI transfers effectively to product-level coding agents, achieving 61.3% attack success on Codex and 58.7% on Claude Code. By contrast, prompt-level defenses exhibit a security-utility trade-off: generic warnings are ineffective, whereas explicit policies suppress attacks but substantially over-refuse legitimate actions.

---


### 153. [Causal Attention on CPU: A Cache-Aware and Load-Balanced Scheduling Kernel for Prefill](https://arxiv.org/abs/2610.38809)

**<font color=#1a73e8>作者：</font>** Kwun Fung Lau, Frost Mitchell, Kanya Mo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic AI drives significant productivity gains across diverse domains, but concurrent long-context prefills from multiple agents can saturate GPU compute resources. Although CPUs offer a viable alternative, existing CPU attention kernels fall short in adapting to multi-tier cache hierarchies and lack effective thread scheduling. To address this, we introduce CACPU, a high-performance attention kernel featuring tiered cache blocking and an in-kernel task dispatching mechanism designed for causal full-sequence prefilling. CACPU achieves up to a 2.01x speedup over PyTorch SDPA, FlexAttention, and SGLang attention kernels. Integrated into SGLang, it reduces Time to First Token (TTFT) of Llama-3.1-8B by up to 1.74x while preserving model accuracy.

---


### 154. [What to randomize matters: a controlled study of volume, axis and representation in low-data molecular generation](https://arxiv.org/abs/2610.38835)

**<font color=#1a73e8>作者：</font>** Neerav Kaushal, Alisa Teige, Ajay MNV Penmatsa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemical language models can struggle to generate new molecules when trained on small datasets, where a model may reproduce training examples rather than learn a useful generative distribution. Randomized SMILES augmentation varies atom traversal, whereas Sequential Attachment-based Fragment Embedding (SAFE) also allows the order of fragment blocks to vary. How these distinct sources of representational variation affect low-data molecular generation has not been clearly studied. Here, using 1,000 seed molecules to train an autoregressive sequence model, we compare canonical SAFE with randomized SAFE at increasing corpus sizes, isolate atom-order and fragment-order axes of SAFE randomization, and compare fully randomized SAFE with randomized SMILES at molecule-by-molecule matched training corpora. Three findings emerge. First, randomization of SAFE alone raises the genuine yield of novel molecules more than 450-fold, turning a model that merely reproduces its training set into a practical molecular generator. Second, the two axes of randomization act jointly rather than additively: atom order alone reaches a tenth, and fragment order alone a seventh, of the genuine yield obtained when both vary, which is four times their combined contribution. Third, at matched corpus size and compute, randomized SAFE delivers 2.8 times the genuine yield of randomized SMILES. Welch tests with Games-Howell post-hoc comparisons resolve every difference on the primary outcomes. In the low-data regime, thus, what one randomizes rather than only how much determines whether augmentation produces new molecules or merely new spellings of the training set.

---


### 155. [Learning to Reason from Reference Samples Alone: Reinforced Adversarial Learning for Modern LLM Post-Training](https://arxiv.org/abs/2610.38851)

**<font color=#1a73e8>作者：</font>** Albert Bou, Javier Valdes-Aleman, Jon M. Laurent 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In many settings where LLM post-training is desirable, high-quality answers are recognizable but difficult to score with explicit rewards. Reinforcement learning with verifiable rewards (RLVR) is limited to tasks where an explicit correctness signal is available. Prior adversarial approaches to training reasoning LLMs either complement verifiable rewards with co-trained critics or require reference reasoning traces. We ask whether a co-trained LLM judge can turn reference answers alone into the sole reward for on-policy post-training of reasoning LLMs. We call this method Reinforced Adversarial Learning (RAL). We first validate RAL on three verifiable tasks (integer multiplication, code-based arithmetic-expression synthesis, and SMILES-to-formula translation), using the verifiers only for evaluation. With sufficiently capable judges and enough training, RAL matches direct RLVR. We then apply RAL to scientific abstract generation in two settings. In the first setting, RAL guides the generator to produce abstracts in the scientific domain of the reference abstracts, even though the prompt leaves that domain unspecified. In the second setting, we generate abstracts for U.S. National Institutes of Health grant proposals conditioned on the grant title. Human scientists and an ensemble of LLM judges find our generations harder to distinguish from real abstracts than those of frontier-LLM baselines. These results suggest a path toward post-training reasoning models in scientific and other high-value domains, where increasingly capable judges infer hard-to-specify reward functions from example answers.

---


### 156. [Where You Inject Matters: The Trust Region Effect in LLM Agents](https://arxiv.org/abs/2610.38867)

**<font color=#1a73e8>作者：</font>** Chengquan Guo, Xiaodong Liu, Weiwei Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly adopted in long-horizon tasks and interact with diverse external environments. Despite their growing capabilities, these agents remain vulnerable to real-world attacks such as indirect prompt injections, which manipulate agents through malicious instructions embedded in external environments. While existing risk assessment work has primarily focused on the injection content, the effect of where an injection appears has not been systematically characterized. Studying injection placement requires agents to operate over longer-horizon tasks and interact with diverse environmental surfaces. Thus, we build three agentic testbeds spanning tool use, coding, and daily workflow domains with diverse injection surfaces. Holding the injection content fixed, we find that agent susceptibility varies across injection placements. We refer to this phenomenon as the trust region effect: agents implicitly assign different levels of trust to different regions of their environments. For example, an agent powered by GPT-5.4 follows an unsafe injection instruction placed in a repository documentation file (i.e., a README or TODO file) 2.6 times more often on average than the same instruction placed in a code or data file. Building upon this observation, we develop learning-based attackers that generate injection content and select better injection placements. Our approach demonstrates that both where an injection is placed and what content it contains can affect the strength of indirect prompt injection attacks. To the best of our knowledge, this work provides the first systematic characterization for the effectiveness of different injection placements, spanning both coarse-grained environmental surfaces and fine-grained positions. The uneven trust that agents implicitly place across their environments provides important insights for future attack and defense design.

---


### 157. [Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems](https://arxiv.org/abs/2610.38869)

**<font color=#1a73e8>作者：</font>** Zhuoyun Li, Boxuan Wang, Jinwei Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering abstraction for evidence-based commitments that guide downstream action. Building on this view, we propose the Explicit Belief Multi-Agent System (EB-MAS), which externalizes belief states into a structured substrate, uses belief operators to propose candidate updates, and applies a Cognitive Firewall to bound or reject updates that are weakly evidenced but strongly driven by vulnerability cues. We also discuss the risk of group belief at the group level, including manufactured consensus, collusion, and cascading misinformation, and outline practical integration challenges around grounding, false positives, scalability, and ethical misuse. Therefore, scalable agent safety requires not only better output filtering or stronger base models, but also explicit interfaces for tracing, calibrating, and constraining belief revision at runtime.

---


### 158. [HEDGE: Gated Hypergraph Memory for Scalable Multi-Agent Debate](https://arxiv.org/abs/2610.38902)

**<font color=#1a73e8>作者：</font>** Amirhossein Abaskohi, Mahdi Mostajabdaveh, Zirui Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate systems require agents to retain and revisit arguments across multiple rounds, yet limited context windows and unstructured memories make relevant information increasingly difficult to recover. Existing flat and pairwise-graph memories also struggle to capture higher-order relations, including multi-agent agreement, conflicting evidence, and evolving consensus. We introduce HEDGE, a selective memory framework that represents debate trajectories as semantic hypergraphs. Hyperedges connect related claims across agents, while intra-hyperedge relational graphs preserve fine-grained argumentative structure. A learned memory selection module (MSM), trained through supervised learning and reinforcement learning, routes each memory candidate to STORE, BACKUP, or OMIT, retaining useful information while limiting redundancy. Across seven diverse benchmarks, HEDGE consistently outperforms strong single-agent, multi-agent, and memory baselines, improving accuracy by 5.0 points on average over the strongest multi-agent system with GPT-4o-mini. The gains reach 8.2 points on conflict-heavy tasks, while HEDGE reduces memory usage by 48% and the number of debate rounds by 34%.

---


### 159. [When Does GenAI Use Support Critical Thinking? A Cross-Cultural Structural Account of Transactive Memory with GenAI](https://arxiv.org/abs/2610.38910)

**<font color=#1a73e8>作者：</font>** Mahir Akgun, Sacip Toker  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Whether generative AI (GenAI) use helps or hinders critical thinking remains contested, and existing accounts emphasize exposure to the tool rather than how a person structures their engagement with it. Extending Transactive Memory Systems (TMS) theory to human-AI partnerships, we test a structural account of critical thinking in GenAI-assisted academic work among 891 college students in the United States and Türkiye. Self-appraised thinking ability and confidence in the partnership shaped how much practical experience a person built up with GenAI, but neither predicted critical thinking directly. That experience mattered only through two downstream behaviors, dividing and coordinating cognitive labor with the tool, and actively reworking its output rather than accepting it as given. A multigroup comparison found this structure largely invariant, with two theoretically interpretable exceptions. This study offers a structural, TMS-based account of critical thinking in GenAI-assisted work.

---


### 160. [Interventional Training Reduces Causal Bypass in In-Context Introspection](https://arxiv.org/abs/2610.38911)

**<font color=#1a73e8>作者：</font>** Zilu Tang, Jongin Kim, Kerem Sahin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Introspection, the ability of a system to access and reason about its internal signals, is crucial for language model (LM) self-consistency and scalable interpretability. Prior work argues that LMs possess introspective capabilities, and that training (SFT) could enhance such behavior. However, most setups leave open the possibility of "causal bypass," in which the self-report relies on signals that are correlated with the self-report's subject, while being causally unrelated to it. Although high-level concepts are difficult to intervene on, lower-level signals (such as a single neuron activation) allow precise interventions. Understanding such signals can serve as a minimal prerequisite before understanding more complex introspection. In this study, we train hundreds of introspectors across three low-level signal types and eight LMs. We find that straightforward SFT training leads to causal bypass, and propose interventional training, an alternative where we train the model to report on counterfactually perturbed values. This method enables more accurate introspection of endogenous $\textit{and}$ injected signals, particularly in out-of-distribution (OOD) data. The mechanism generalizes across token positions and scales with more data. Our results demonstrate that while causally grounded introspection is possible, it is not guaranteed -- emphasizing the need to train on mechanisms, rather than behaviors alone.

---


### 161. [TreasuryQA Bench: Can AI Agents Work an Archive of Scanned Financial Records?](https://arxiv.org/abs/2610.38924)

**<font color=#1a73e8>作者：</font>** Ritiz Tambi, Sahar Shayegan, Joshua Meyer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organisations keep decades of financial records as scanned PDFs on shared drives, and AI agents can now reach those drives through Model Context Protocol (MCP) servers. Existing benchmarks do not mirror this production setting because they simplify the task. In some, the relevant documents are handed to the agent, so it never has to search. In others, the agent searches through documents with pre-extracted text, so it never has to read scanned images. We introduce TreasuryQA Bench, which requires both: 70 questions over 1,435 scanned U.S. Treasury publications, held in Veris's high-fidelity Dropbox twin. In each task the agent searches for the relevant file through Dropbox's MCP server, reads the pages it needs with Reducto's hosted OCR server or its own tools, and replies with one exact figure. A Python grader checks each answer against an accepted range around the correct value. In this paper we present results from ten agents. The best, Claude Opus 5.5 in Claude Code, solves 64.8% of attempts and the worst, GPT-5.6 Terra in Codex, solves 16.7%, so the benchmark is far from saturated. We also test how scan quality affects performance: every agent solves fewer tasks on the blurriest scans. Most failed attempts reply with a wrong number rather than no number, and the most common cause is a digit misread from the scan. Three worked examples are included with their answer keys.

---


### 162. [OneScene-Bench: Do Vision-Language Models Integrate Evidence Across Views?](https://arxiv.org/abs/2610.38926)

**<font color=#1a73e8>作者：</font>** Swathi Suhas, Anurag Das, Bernt Schiele 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly process multiple views of the same scene, but it remains unclear whether they integrate these observations into a coherent scene-level representation. Existing multi-image evaluations do not isolate this capability, as tasks may admit correct solutions through independent per-view processing without requiring cross-view correspondence. We introduce OneScene-Bench, a controlled benchmark designed to explicitly distinguish when cross-view integration is necessary. Our benchmark evaluates three complementary capabilities on real-world multi-view scenes: unique object counting, cross-view consistency, and spatial reasoning. For counting, we control object overlap across views to separate cases solvable by simple per-view aggregation from those requiring instance-level correspondence. For consistency, we introduce localized edits in shared and view-specific regions, testing whether models distinguish genuine scene contradictions from differences caused by viewpoint and visibility. For spatial reasoning, we construct object relations that require combining spatial evidence across viewpoints to compare physical proximity. We evaluate twelve state-of-the-art open-weight and proprietary VLMs and find that counting accuracy drops substantially on complementary views, ranging from 4.5-50.0%, compared with 45.5-81.5% on complete-overlap examples. Moreover, cross-view consistency remains around 50% across models, including recent proprietary VLMs, despite substantially stronger performance on spatial reasoning. Our results reveal a substantial gap between processing multiple images and integrating evidence across them, highlighting the need for evaluations that explicitly test scene-level multi-view understanding. Code and data are available at this https URL.

---


### 163. [What do MLLMs know about 'Waldo'? Evaluating Visual Reasoning under Multi-Instance Multi-Object Challenges](https://arxiv.org/abs/2610.38957)

**<font color=#1a73e8>作者：</font>** Saumya Mundra, Ajoy Mondal, Vineeth N Balasubramanian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) have led to significant progress in visual reasoning capabilities. However, existing benchmarks curate image-question pairs pertaining to object categories with few instances, enabling trivial object referencing and limited visual ambiguity. In this work, we introduce MIMO-Bench, a benchmark for evaluating MLLMs in a Multi-Instance per Multi-Object categories (MIMO) setting. Each image-question pair in our benchmark pertains to instances belonging to object categories with multiple instances. The presence of such similar feature distractors causes hindrance in basic visual reasoning tasks, necessitating the referring expression to be composed of multiple visual subtasks to uniquely and unambiguously identify the target object. MIMO-Bench comprises 3,802 image-question pairs across attribute binding and numerical counting tasks. Despite impressive performances on existing benchmarks, both SOTA open-source (InternVL, QwenVL) and proprietary (Gemini, GPT-5) models exhibit substantially lower performance on MIMO-Bench, highlighting their limitations in the MIMO setting. The benchmark will be made publicly available.

---


### 164. [Context Compaction for World Models](https://arxiv.org/abs/2610.38980)

**<font color=#1a73e8>作者：</font>** Hayder Tirmazi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models let observers explore and interact with generated worlds. Recent work shows that when observers revisit a region, current models often fail to regenerate it consistently. We view this as a context retrieval problem. LLM agents manage context retrieval at two layers of their stack. At the model layer, the KV cache design determines how much context fits in memory. At the agent harness layer, harnesses such as Claude Code pick the context sent to the LLM. Prior work on world models has mostly focused only on the model layer. In this paper, we make three contributions. First, we build a benchmark to measure world model context retrieval. It generates new worlds for every episode, preventing a model from recalling rooms using training data. It also separates context retrieval from guesses based on nearby frames. Second, we build an agent harness that performs context compaction for world models, which to our knowledge no prior work has studied. Third, we use our benchmark to study four world model designs. Context compaction lets our world models retrieve rooms up to 4 times beyond their context window without retraining. However, world models with sliding-window attention lose most of their context retrieval when dreaming. Therefore, a dreaming world agent benefits more from extending the reach of its world model using context compaction than switching to sliding window attention at the model layer.

---


### 165. [Why Speculative Decoding Works Better Than Predicted on Sparse MoE Models](https://arxiv.org/abs/2610.38981)

**<font color=#1a73e8>作者：</font>** Ekagra Ranjan, Komal K. Teru, Bharat Venkitesh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) accelerates autoregressive inference by leveraging the memory bound nature of decoding, verifying multiple draft tokens in a single forward pass. For mixture-of-experts (MoE) models, prior work predicts a concave speedup-batch size relationship, with gains peaking at intermediate batch sizes due to expert saturation. We evaluate this across 10 sparse MoE models (30B--1T parameters, 8--512 experts) and find recent fine-grained models break this trend, showing higher speedup at low batch size. We find verification cost is governed not only by activated-expert bytes, but also by temporal overlap across draft tokens and GPU execution dynamics. At low batch size, MoE layers in fine-grained models account for a much smaller share of runtime than of weights; on H100, kernel profiling attributes this mainly to higher bandwidth utilization of MoE kernels relative to attention, with L2 absorbing repeated reads of co-routed experts. Across draft tokens, routing overlap further reduces the unique experts activated during verification relative to independence assumptions. We model this effect using a maximum-entropy Iterative Proportional Fitting (IPF) framework that predicts unique expert counts from routing-overlap statistics with less than 4\% error, and substantially narrows the gap to real-model curves and captures the qualitative low-batch trend from synthetic routing.

---


### 166. [Exploring AI Peer in Collaborative Mathematics Learning](https://arxiv.org/abs/2610.38990)

**<font color=#1a73e8>作者：</font>** Yiran Lin, Ye Deng, Ziqi Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) agents are increasingly explored as collaborative learning partners in mathematics education, yet it remains unclear what makes an AI recognizable as a peer. This study examines how domain experts perceive and interact with an adaptive LLM-based peer agent combining a Big Five-informed persona with motivational state modulation for collaborative mathematics problem solving. Through thematic analysis of expert interviews, we identify conditions shaping peer perceptions, including emotional safety, shared control, and collaborative reasoning. Participants primarily judged the AI through its social behavior rather than mathematical capabilities. The AI was perceived more as a peer when it created a non-judgmental space, engaged in tentative reasoning, displayed appropriate imperfection, and respected participants' pace. Conversely, blind agreement and over-instruction reduced trust and shifted perceptions toward a tutor role. Based on these findings, we propose human-centered design dimensions for AI peer agents to guide future peer-oriented learning systems.

---


### 167. [Blind Spots: Where Small Language Models Fall Behind Frontier Models on Terminal Tasks](https://arxiv.org/abs/2610.39006)

**<font color=#1a73e8>作者：</font>** Ashima Suvarna, Ruta Desai, Ahmed Elgohary  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) offer an attractive alternative to frontier models (FMs) because they can be deployed with lower cost and latency. This makes SLMs especially appealing for terminal tasks on edge devices, where responsiveness, local execution, and limited connectivity are important considerations. However, they continue to lag behind FMs on terminal tasks, as measured by standard task success rates. Yet these rates conflate several capabilities that may contribute to this gap. In this work, we characterize the SLM-FM gap along three axes: solvability, whether additional test-time compute allows an SLM to reach a correct solution; verification, whether it can identify a successful solution among candidate trajectories; and confidence, whether it can accurately anticipate its probability of success. Across two standard terminal benchmarks, we find that repeated sampling narrows, but does not eliminate, the gap in solvability. In contrast, a persistent gap remains in verification. Given the same candidate trajectory pool, FMs recover substantially more of the gap between random and oracle selection than SLMs. SLMs are also more overconfident in their prospective success estimates and exhibit poorer calibration. These results suggest that the SLM-FM gap is multidimensional, spanning not only the ability to generate successful solutions, but also the ability to recognize successful solutions and anticipate success. We hope this decomposition can guide future work on developing stronger and smaller terminal agents.

---


### 168. [Implicit Reasoning in Transformers: Bridging the Compositionality Gap in GPT-2-like Models](https://arxiv.org/abs/2610.39016)

**<font color=#1a73e8>作者：</font>** Davide Venuto, Leonardo Venuto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compositional generalization remains a persistent limitation of transformer language models: even when a model learns to combine known facts correctly in-distribution (ID), the same compositional mechanism may fail when applied to out-of-distribution (OOD) knowledge. We investigate this compositionality gap in a controlled two-hop reasoning setting using a GPT-2-like transformer model trained from scratch. Building on prior work identifying a circuit associated with compositional generalization, we test whether the failure of OOD transfer is related to how atomic knowledge is structurally exposed during training. We modify the training distribution by presenting both ID and OOD atomic facts in a format positionally aligned with the second-hop retrieval step of the learned compositional circuit, without modifying the model architecture or adding OOD compositional supervision. Under this intervention, the model successfully transfers the learned ID compositional behaviour to held-out OOD atomic facts, closing the observed compositionality gap in the controlled setting. Our results provide evidence that the observed compositionality gap is not a fundamental architecture limitation and that it can be overcome through mechanistically informed training distribution design.

---


### 169. [Author-Informed Stance Detection: A Dataset and Findings](https://arxiv.org/abs/2610.39019)

**<font color=#1a73e8>作者：</font>** Ogen Schlachet Drukerman, Einat Minkov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stance detection in social media is challenging, as interpreting a text often requires understanding the author's perspective. We re-frame political stance detection as an author-informed text understanding task, where it is desired to infer both the author's political leaning and their stance towards the target from the text. We first show that human annotators struggle to infer authors' political leanings and stances from individual tweets, and that pretrained large language models (LLMs) perform below human level in this setting. We then demonstrate that author context improves stance detection for both humans and LLMs, with particularly pronounced benefits for tweets perceived as sarcastic. Through extensive experiments, we further show that LLMs can be effectively fine-tuned to predict authors' political affiliations, and that author-informed fine-tuning yields better stance detection performance than standard fine-tuning. This approach not only surpasses human performance but also improves generalization across datasets. To support further research on author-informed political stance detection, we release a large dataset of stance-labeled tweets enriched with author-context information.

---


### 170. [Distilling the Shape of Uncertainty: What On-Policy Distillation Learns and How to Predict It](https://arxiv.org/abs/2610.39020)

**<font color=#1a73e8>作者：</font>** Shiping Yang, Chuanqi Tang, Hossein Hajimirsadeghi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is increasingly adopted in the post-training of large language models. However, a stronger teacher may fail to improve the student. Prior work attributes this to a lack of new knowledge, but what that knowledge is remains unclear. We show that OPD learns not only \textit{how to branch}, i.e., which candidate tokens to consider, but also \textit{where to branch}, i.e., where to keep reasoning paths open. The existing token-overlap metric captures only the former. We introduce the entropy shape, the sequence of next-token entropies, to characterize the latter, and propose the Entropy Shape Correlation (ESC) to measure student-teacher agreement in entropy shape. Tracking ESC throughout training and intervening on a teacher's entropy while preserving its token preferences, we empirically show that \textit{where to branch} causally drives OPD gains, independently of \textit{how to branch}. Finally, we formulate OPD outcome prediction as a teacher selection task and establish an evaluation protocol for it, under which pre-OPD ESC selects the best teacher for both students and outperforms existing predictors. Code is available at this https URL.

---


### 171. [When Does Closed-Loop Curriculum Adaptation Help GRPO? An Analysis on Countdown](https://arxiv.org/abs/2610.39056)

**<font color=#1a73e8>作者：</font>** Yuv Raj Pant, Moshiur Rahman Tonmoy, Kaiqun Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement fine-tuning has become an effective post-training paradigm for improving the reasoning ability of large language models, but it remains sample-inefficient when the training distribution is mismatched to the model's current capability. In group-relative objectives such as Group Relative Policy Optimization (GRPO), problems that are too hard often produce uniformly failed rollouts, while problems that are too easy provide little useful advantage signal. In this work, we introduce CLOSEDLOOPGAUSSIAN, a lightweight adaptive curriculum method for efficient reinforcement fine-tuning on ordered reasoning tasks. Instead of following a fixed easy-to-hard schedule, CLOSEDLOOPGAUSSIAN preserves the structure of an Easy-to-Hard Gaussian sampler while dynamically adjusting its pace and spread using periodic probe estimates of per-difficulty accuracy. The controller accelerates training when the model is ahead of a reference curriculum, slows down when the model falls behind, and broadens sampling when earlier difficulties regress. This feedback mechanism keeps training focused on tasks that are challenging but still learnable, without changing the reward function, model architecture, or underlying GRPO optimizer. Experiments on symbolic arithmetic reasoning task show that CLOSEDLOOPGAUSSIAN improves exact-match accuracy over vanilla GRPO and fixed open-loop curricula, with the strongest gains in intermediate-difficulty regimes where group-relative learning signals are most informative. Codes are available at this https URL.

---


### 172. [Tracing the Influence of Retrieved Literature on Scientific Ideation in LLMs](https://arxiv.org/abs/2610.39060)

**<font color=#1a73e8>作者：</font>** Zhipin Wang, Koel Dutta Chowdhury, Christoph Leiter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate research ideas from scientific literature. Existing systems combine literature retrieval with search, generation, and refinement, making it difficult to determine how the retrieval strategy itself shapes the ideas generated. We isolate this contribution by comparing five retrieval strategies and a No Literature baseline under a shared generation protocol, using 45,000 ideas across 15 machine learning topics and ten open-weight models. Relative to no literature basline, all five retrieval strategies reduce diversity among ideas generated from the same set of papers by $5.6\%$--$17.9\%$, while most increase diversity by $10.2\%$--$18.1\%$ when ideas from different sets are pooled. Effects on idea quality and novelty are modest on average but vary across topics. We further apply a JSD-based attribution method to trace the influence of individual input papers on each idea's motivation, core idea, approach, and validation. In $79.3\%$ of ideas, only one or two distinct papers receive the highest attribution scores across these four parts. These leading sources often recur across ideas generated from the same set of papers, and groups with more varied source attribution contain more diverse ideas ($r=0.70$). These findings motivate various sets of literature and the use of attribution to guide the choice of sources for subsequent ideas.

---


### 173. [HEARSAYBENCH: Can AI Navigate from Abstract Human Rights to Lived Lives?](https://arxiv.org/abs/2610.39062)

**<font color=#1a73e8>作者：</font>** Ava Iranmanesh, Sobhan Lotfi, Ali Iranmanesh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) reach users worldwide, personal counseling has emerged as one of their most consequential applications, sometimes in life-critical situations. Yet broader access does not mean equal support. The text these models learn from disproportionately reflects people with the freedom to act, embedding an implicit assumption that users can leave, report, seek help, or appeal. Existing benchmarks largely inherit this assumption, overlooking users whose agency is constrained by structural conditions such as war, statelessness, and displacement. Meanwhile, models are increasingly shaped by normative frameworks such as Constitutional AI, often grounded in ideals like human rights, even as many users live where those rights offer little protection or recourse.
We introduce HEARSAYBENCH, a human-authored dataset of 400 test cases with in-region human verification grounded in scenarios where structural barriers stand between a person and the exercise of their rights. Built from United Nations and other human rights reports, the scenarios span over 80 regions and cover social, environmental, and personal constraints. Drawing on Nobel laureate Amartya Sen's Capabilities Approach, HEARSAYBENCH tests whether models can distinguish what a person is formally entitled to do from what they are actually able to do. Across 14 proprietary and open-weight models, every model infers a user's situation more accurately than it advises on it. Stronger models narrow this gap, but their recommendations remain unsafe to follow. Models may understand lives shaped by constraint, yet that knowledge remains hearsay if it cannot translate into advice people can act on. Those people are not alignment's long tail; they are among the users for whom good guidance matters most. HEARSAYBENCH makes this failure measurable, a step toward systems that serve the world as it is rather than as assumed.

---


### 174. [Closed Gates Leak: Decomposing Adjacent-Layer Cancellation in Gated Language Models](https://arxiv.org/abs/2610.39068)

**<font color=#1a73e8>作者：</font>** Harvey Dam, Ganesh Gopalakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In transformer language models with gated multilayer perceptrons (MLPs), adjacent layers write partly against each other into the residual stream. Previous work interpreted this cancellation as layers proposing features and the next layer selectively rejecting the inappropriate ones. We decompose the cancellation by removing the previous layer's write from the input of the next MLP: what the next layer writes along that write splits into what it writes anyway and how much less its MLP writes because the write is present, which we call the damping, and we trace the damping to the neurons that carry it. In gated MLPs the damping is carried by neurons whose gates are closed. SiLU and GELU are slightly negative below zero, so a closed gate still passes a small negative multiple of what the neuron reads, and a neuron whose output weight points along its input weight then subtracts a fraction of the direction it read. Summed over such neurons, closed gates contract the average direction a gated MLP reads, and the previous layer's write is not singled out: the same layer's write at another token is damped as much or more, and the eigenvalue signature from which that work concluded that the correction is selective appears for another token's write as well. Over training the damping grows while what the next layer writes anyway stays flat, and cancellation begins when the damping overtakes it; annealing the negative side of the gate activation away in continued pretraining removes the damping and the cancellation. Adjacent-layer cancellation is therefore weak evidence about which features a model rejects: it is produced by a contraction that gated MLPs apply, on average over directions, to whatever they read.

---


### 175. [When the Same Prompt Gives Different Answers (and the Same Answer Isn't Always Right): A Taxonomy of Failure Mechanisms, Testing, and Mitigation Strategies for LLM-Assisted Evidence Synthesis Read-and-Evaluate Tasks](https://arxiv.org/abs/2610.39070)

**<font color=#1a73e8>作者：</font>** Carole Lunny, Ian Goodman, Stefano Berrone 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM read-and-evaluate tasks include study screening, data extraction, risk-of-bias assessment, and critical appraisal in the evidence synthesis field. These task differ in the amount of LLM interpretation they require. Some tasks involve retrieving relatively simple information, such as an author name, sample size, or publication year. Others require the LLM to read source material, interpret it against predefined criteria, and make a judgement. Researchers should assess whether LLM judgements are accurate, supported by appropriate source evidence, and reproducible under specified conditions. A correct judgement does not necessarily indicate that the underlying evaluation process is reliable. We developed a taxonomy for identifying mechanisms that may compromise these properties and for informing the selection and reporting of appropriate evaluation methods. The taxonomy outlines potential ways that LLM judgments from read-and-evaluate tasks can fail, called TRAILS (Taxonomy of Reliability And Instability in LLM-assisted evidence Synthesis). The TRAILS taxonomy addresses two complementary questions. First, what mechanisms can cause the same read-and-evaluate task to produce different judgements across repeated LLM runs? Second, what mechanisms can systematically affect the judgement or required output in a way that is not apparent from the judgement itself? This study presents 38 mechanisms and identifies the deployment settings in which each can operate, approaches for testing them, and mitigation strategies. We also show why repeatability or accuracy does not rule out a hidden judgement failure and why human evaluation should assess whether a judgement is grounded in the supplied evidence, independent of inappropriate external influence, and produced through a process that can be examined and verified.

---


### 176. [REALM: Identifying Minimal Task Assets for LLM Agents](https://arxiv.org/abs/2610.39155)

**<font color=#1a73e8>作者：</font>** Zihou Ren, Byungchul Tak, Long Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents often receive access to more files, accounts, and services than a task requires. Prompt injection turns this excess access into an opportunity to redirect execution toward unrelated resources. Applying least privilege therefore requires identifying the assets needed by a task, including assets whose identities emerge only during execution. We present REALM (Required Execution Assets Linked to a Mission), an approach to identifying and maintaining a task's required assets and their permitted uses. The approach represents required assets as Dependency Graph nodes, resolves prerequisite relationships, and admits newly discovered assets through source-scoped selection. It separates discovering an asset from authorizing its use, while preserving the agent's freedom to choose its computation. The REALM Builder maintains the selected grants and projects Asset Files; the Partial API Manager exposes resource-bound Partial APIs to the Agent inside a Task Container. Across 60 clean tasks and 560 injected cases in AgentDyn, it completes 40.0% and 36.4% of tasks and decreases ASR from 16.6% to 0.2% with qwen3.5-flash as the base model.

---


### 177. [VEvo-Harness: Causally-Guarded Self-Evolving Harness for Agentic Image Generation](https://arxiv.org/abs/2610.39158)

**<font color=#1a73e8>作者：</font>** Yuan Wang, Yuhang Yu, Mengting Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The central bottleneck in visual generation and editing has migrated from achieving pixel-level fidelity to satisfying densely constrained user specifications through increasingly agentic workflows. Prevailing agentic generation pipelines remain shallow generate-verify-rewrite loops treating VLM judgments as coarse visual feedback, either discarding repair experience or admitting ungated updates that poison skill library. With memorize and govern periods left open, they degrade into ungoverned iterators of repeated trial-and-error rather than continual self-evolving harness. Towards this issue, we present \textbf{VEvo-Harness}, the first causally-guarded continual self-evolving harness system for agentic visual generation. VEvo-Harness introduces four coupled innovations: (1) \textit{a visual traceback} that densifies sparse judgments into root-cause attributions with a hierarchical verification tree; (2) \textit{a visual continual governance} that admits only causally valid skill patches through counterfactual dual-arm image generation replay; (3) \textit{a lifecycle-managed harness state} that hierarchically distills root-cause-anchored episodes across working, experience, and pattern tiers into a persistent skill library of routable and causally verified capabilities; (4) \textit{a heterogeneous sandbox policy} that orchestrates a diverse action space of repair primitives, dynamically routing cost-aware interventions based on root causes to select the most effective strategy. VEvo-Harness surpasses state-of-the-art agentic methods and rivals proprietary generators (\textit{e.g.}, GPT-Image, Nano-Pro) while maintaining the continual harness evolution and generalization.

---


### 178. [Reasoning or Pattern Exploitation? Mechanistic Insights from RL-Trained Language Models](https://arxiv.org/abs/2610.39182)

**<font color=#1a73e8>作者：</font>** Aishik Nagar, Cheston Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly described as acquiring "reasoning" skills after reinforcement learning with verifiable rewards. However, whether these gains reflect genuine reasoning or more superficial adaptations remains underexplored. In this work, we probe LLMs trained in a finite and exhaustively analyzable logical domain, namely Tic-Tac-Toe, and trace how internal representations evolve across reinforcement learning (RL) with Group Relative Policy Optimization (GRPO). Quantitatively, RL yields high accuracy and robustness across prompt variations, suggesting the emergence of game reasoning. Mechanistic interpretability, however, paints a different picture: features extracted with sparse autoencoders (SAEs) reveal that models primarily adapt to rely more heavily on information already explicit in the prompt, such as whose turn it is, game progression and board occupancy. In comparison, high-level concepts like board symmetries and strategic forks remain weakly represented, raising concerns that reasoning benchmarks overestimate model abilities. This suggests that RL-driven "reasoning" may conflate task-specific adaptations to input information with reasoning ability. We provide, for the first time: (i) a systematic interpretability pipeline tracing representation dynamics across RL training in small-scale LLMs; (ii) an extension of SAE-based feature discovery to hypothesis-driven testing in a finite logical domain; and (iii) an interpretability-based demonstration that RL post-training neither adds nor removes concept information but reorganizes which features dominate the representation, with causal interventions locating the decision downstream of it, in the late-layer state.

---


### 179. [Goal-Aware Dynamic Multi-Agent Collaboration for Long-Horizon Tasks](https://arxiv.org/abs/2610.39193)

**<font color=#1a73e8>作者：</font>** Xu Shen, Lingyong Yan, Shuaiqiang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly used to complete complex, long-horizon tasks without human intervention. To make progress toward the task goal, agents need to perform different duties, such as planning and verification, when needed. To understand how single agents manage these duties during long-horizon execution, we conduct a preliminary study. Our analysis shows that verification has the strongest association with task success, but often occurs late, leaving limited opportunities for correction. We also find that the proportion of duty-relevant information decreases as records from different duties accumulate in a shared context. These findings lead us to examine whether multi-agent systems (MAS) can address these problems by assigning duties to agents with separate contexts. Our analysis shows that this separation alone is insufficient. Agents can lose track of the overall goal and repeat prior investigations. They may also lack necessary background while receiving irrelevant information from others. To maintain goal awareness and coordinate collaboration as task needs change, we propose Goal-Aware Dynamic Multi-Agent Collaboration (GAD). It uses a growing execution graph to organize subtasks and their dependencies. To keep agents focused on their goals, each context retains the original instruction and the assigned task's goal and acceptance conditions. To adapt collaboration and information sharing during execution, agents can divide tasks into subtasks and specify dependencies based on execution evidence. These dependencies guide when agents work and which results they receive. Verification and recovery check subtask results and full task completion against their goals, providing feedback for repair when checks fail.

---


### 180. [XLaw-JP-27B: A Lightweight Open Model Specialized for Japanese Law](https://arxiv.org/abs/2610.39227)

**<font color=#1a73e8>作者：</font>** Andrew Shin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present XLaw-JP-27B, an open-weight model specialized for Japanese law that runs on a single 48\,GB GPU under the Apache~2.0 licence. It adapts Qwen3.8-27B with hybrid retrieval over all current statutes and 31k case summaries, a light QLoRA fine-tune on its own verified answers to past bar-exam questions (self-distillation), a contract-specific LoRA adapter, and four-sample voting. We evaluate it on eight Japanese legal tasks---the multiple-choice section of the bar examination in 2024, 2025 and 2026, statement-level bar questions (JBE-QA), statute questions (LawQA-JP), the patent attorney exam, and contract review and drafting built from government model contracts---against open models of 12--33B under identical prompts and retrieval. XLaw-JP-27B ranks first on six tasks, ties on one and is third on one (mean rank 1.3 against 2.8--3.1 for the baselines). It is the only system that passes the bar exam in all three years (129, 120 and 130 of 175, meeting every subject minimum; no test-year material was used in training), while open Japanese 32--33B models fail at least one year. A controlled study of each component shows that retrieval, voting and self-distillation help, and that thinking mode, retrieval-grounded synthetic tuning, self-verification, per-statement decomposition and more self-distillation do not. The largest remaining gaps to frontier models are in contract review and patent law. The model is available as a free web service at this https URL with the weights available at this https URL under Apache~2.0.

---


### 181. [Beyond LLM Wrappers: Context Engineering and the Three-Engine Architecture for Reliable Financial AI](https://arxiv.org/abs/2610.39230)

**<font color=#1a73e8>作者：</font>** Pradeep Kumar GS, Ravi Tanniru  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial AI systems must support decision-bearing questions involving payments, collections, cash flow, and compliance while ensuring numerical accuracy, traceability, and auditability. Large language models (LLMs) enable natural language interaction but cannot independently guarantee reproducible calculations or evidence-grounded recommendations. We present a production-grounded architecture integrating three components: a financial knowledge graph for enterprise relationships, temporal context, and provenance; a deterministic optimization engine for financial calculations and decisions; and a multi-agent LLM layer for intent interpretation, task orchestration, explanation, and claim validation. A coordination layer, termed context engineering, selects, ranks, composes, and validates query-specific context across ERP systems, tools, and tenants.
Based on observations from 15 deployments over approximately 11 months, single-agent pipelines exhibited hallucination rates of about 7-9% (5-10% across query types), including invented invoices and unsupported financial claims. Graph-backed multi-agent validation reduced observed rates to below 1%, although these findings are observational rather than causal. ERP data quality and tenant-specific schemas remained major implementation challenges. Reusable mappings, graph templates, and validation policies coincided with a reduction in deployment time from roughly six to two weeks.
We argue that financial context engineering extends beyond text-centric retrieval-augmented generation by requiring structured relationships, temporal validity, exact numerical evidence, access controls, and validation against source records and solver outputs. We outline research challenges in evaluation, reproducibility, privacy, context quality, and cross-tenant generalization.

---


### 182. [AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers](https://arxiv.org/abs/2610.39234)

**<font color=#1a73e8>作者：</font>** Zhiyi Liu, Haohua Du, Haoqi Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have demonstrated strong capabilities in automating complex information-seeking and transactional tasks across the open web. However, their real-world reliability remains limited by access barriers, such as dead links, authentication walls, rate limits, and anti-scraping defenses. These barriers block the primary execution path, causing agents to abort prematurely, loop indefinitely, or quietly compromise the user's original constraints. Existing evaluations either implicitly assume that target resources are freely accessible or focus on transient perturbations that simple retries can resolve, failing to capture scenarios where agents must actively reroute around impassable bottlenecks. To bridge this gap, this paper introduces AgentHeal, a comprehensive benchmark evaluating goal-preserving resource recovery, defined as the ability of web agents to detect non-transient access barriers, pivot to legitimate alternative sources, and fulfill the user's exact original objective. Spanning nine barrier families across a counterfactual sandbox and real-website replay, our experiments on leading LLM backbones show that average task success drops sharply from 89.4% to 43.7% under access barriers. Further analysis reveals that agents frequently fall for deceptive look-alikes, fail to escalate to users when necessary, violate access policies, or waste computation on futile retries, providing actionable diagnostics for developing resilient web agents.

---


### 183. [Grounding Multimodal Reasoning with Evidence-Ablated Negatives](https://arxiv.org/abs/2610.39237)

**<font color=#1a73e8>作者：</font>** Chenxi Liu, Tianyi Xiong, Yanshuo Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a powerful tool for improving multimodal reasoning. However, standard outcome supervision suffers from credit assignment ambiguity, as a model may receive positive rewards by exploiting language priors or dataset shortcuts rather than grounding its reasoning in the requisite visual evidence. This makes high-quality negative responses critical, since effective negatives should remain plausible under the current policy while exposing the shortcut that should be suppressed. In this paper, we propose EVAN, a multimodal reinforcement learning framework utilizing EVidence-Ablated Negatives to train LMMs against their own language-prior failures. EVAN first identifies highly visually dependent examples using a scaled image information gain metric and preserves data diversity with a mixed-ranking strategy. It then constructs evidence-ablated images by masking the most discriminative image patches, eliciting plausible but visually ungrounded responses from the current policy. During policy optimization, these negative responses are incorporated as bounded auxiliary signals under the clean image, penalizing shortcut learning while maintaining RL stability. Experiments across challenging multimodal reasoning benchmarks demonstrate that EVAN mitigates modality imbalance and improves over strong RLVR baselines. Our code is available at this https URL.

---


### 184. [IMRouter: Imbalance-aware Temporal Pattern Routing for LLM-based Time Series Forecasting](https://arxiv.org/abs/2610.39246)

**<font color=#1a73e8>作者：</font>** Xin Yang, Cai Xu, Haishun Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate time series forecasting (TSF) is essential for Web applications, such as traffic monitoring and online resource management. Recent advances in leveraging pre-trained large language models (LLMs) have shown promising performance in TSF. However, existing LLM-based TSF methods largely optimize the overall forecasting objective while overlooking temporal pattern imbalance (TPI), where different temporal patterns occur at highly unequal frequencies. Our empirical analysis reveals that TPI is prevalent across widely used TSF benchmarks, with substantially higher forecasting errors on less frequent patterns. To address this issue, we propose IMRouter (Imbalance-aware Temporal Pattern Routing), a novel framework that mitigates TPI-induced biases in both temporal representation learning and cross-modal alignment. Specifically, IMRouter introduces Pattern-Adaptive Temporal Representation Learning (PATR), which leverages gradient conflict and local gradient density to guide expert specialization. By penalizing incompatible expert assignments with density-aware weighting, PATR reduces the dominance of frequent optimization signals in router training. Furthermore, Routing-Guided Semantic Alignment (RGSA) transfers the pattern-specific knowledge learned by the router to cross-modal alignment through mutual information maximization, preserving distinctive temporal information across different patterns. Extensive experiments on benchmark datasets demonstrate the effectiveness of IMRouter, particularly in improving forecasting performance on less frequent temporal patterns.

---


### 185. [SocialArena: Evaluating Social Intelligence in Large Language Models](https://arxiv.org/abs/2610.39247)

**<font color=#1a73e8>作者：</font>** Zongqi Wang, Rui Wang, Yuchuan Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce SocialArena, a benchmark for systematically defining and evaluating the social intelligence of large language models (LLMs). Although LLMs are increasingly deployed in socially interactive applications such as mental health counseling, companionship chatbots, and educational tutoring, existing evaluations remain fragmented focusing on isolated capabilities or single scenarios and evaluation reliability is largely unverified. This work makes three main contributions to address these limitations. (1) We first propose a unified three-tier framework that defines social intelligence along three capability dimensions: role-playing ability, mental state reasoning, and behavioral reasoning. To operationalize this definition, we design a role-playing dialogue paradigm with explicit character thinking for evaluation, enabling simultaneous assessment of these capabilities in a manner that mirrors realistic human interactions. (2) To ensure diversity across social scenarios and thereby prevent evaluation conclusions from being confined to specific scenarios, we introduce the U-TRIMF framework, which guides us in synthesizing social contexts with broad coverage. (3) To obtain reliable evaluation, we invest $132.4K to recruit and train human annotators and adopt a human-annotated arena-style protocol, where annotators compare model responses and provide preference labels along with natural-language critiques. We hope that SocialArena can provide valuable insights and guidance for future LLM improvements.

---


### 186. [Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps](https://arxiv.org/abs/2610.39264)

**<font color=#1a73e8>作者：</font>** Peitong Duan, Khashayar Gatmiry, Jeffrey Nichols 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While frontier vision-language models demonstrate strong capabilities in user interface (UI) navigation, their high inference costs prohibit everyday use. Conversely, smaller models trained via supervised fine-tuning (SFT) or offline reinforcement learning often memorize static trajectories, leading to brittle execution and an inability to recover from errors. To address these limitations, we propose a novel online reinforcement learning framework that trains UI navigation agents directly on live iOS applications. Our framework decouples the agent into two specialized components: a Planning agent and a UI Grounding model. We rely on an LLM-as-a-Judge to provide comprehensive reward signals, combining dense, step-level feedback to evaluate intermediate progress with a terminal reward for overall task completion. To effectively leverage this dual reward structure, we optimize the agent using Proximal Policy Optimization (PPO) with step-level advantage estimation. Furthermore, we introduce GiGPPO, a novel neighbor-conditioned value estimation method that improves critic stability by leveraging reward signals from visually similar states across concurrent trajectories. To support this online training paradigm at scale, we introduce an efficient infrastructure that orchestrates hundreds of concurrent virtual iOS devices. Evaluations on rigorous benchmarks, including UINavBench, iOSWorld, and AndroidWorld, demonstrate that our online RL trained agents substantially outperform both SFT and terminal-only RL baselines while accelerating training convergence. Notably, our 8B RL agents achieve nearly a sevenfold improvement over the SFT baseline in out-of-distribution generalization to Android environments, while outperforming Gemini-3.5-Flash and tying with Gemini-3.1-Pro on real iOS applications.

---


### 187. [DeCoRL: Decomposed Consistency Reinforcement Learning for Multi-Image Composition](https://arxiv.org/abs/2610.39265)

**<font color=#1a73e8>作者：</font>** Zhiqiang Wu, Shuang Sun, Jiale Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-image composition (MICo) is a critical yet challenging capability for large-scale image editing models, where consistency degrades rapidly as the number of reference images increases. While supervised fine-tuning (SFT) can equip models with basic MICo ability, it provides only implicit supervision on the composed image and often fails to learn reliable object-level correspondence across multiple references. We propose DeCoRL, a reinforcement-learning (RL) framework that improves MICo consistency by decomposing holistic MICo consistency into object-level consistency. DeCoRL first establishes instruction-relevant object correspondences across reference images and localizes the corresponding regions in the generated image. It then uses a VLM-based reward model trained on single-object consistency annotations to produce fine-grained, object-wise feedback, which is aggregated into a multi-object consistency reward to guide RL post-training. We further introduce DeCo-Bench, a benchmark covering compositions from 2 to 6 reference images. Experiments on DeCo-Bench and the public MICo-Bench demonstrate consistent improvements in MICo consistency.

---


### 188. [LLM-Assisted Optimization for Simulation-Based Redesign](https://arxiv.org/abs/2610.39275)

**<font color=#1a73e8>作者：</font>** Chan-Eui Song, Jeremy J. Michalek, Christopher McComb  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Engineering design frequently involves redesigning a prior solution to adapt to changes in context, such as material prices or system requirements. Redesign often leverages simulators too complex and/or computationally intensive for traditional numerical solvers, which lack engineering knowledge and context, to ensure global solution quality. Large language models (LLMs) can interpret semantic information, including engineering knowledge about the system and changes in context, to help guide search, and recent studies have shown that incorporating this knowledge into optimization can improve search performance. However, how best to combine LLMs with numerical solvers in redesign remains unclear. We develop and test an integrated LLM-optimization approach for redesign and compare three methods for leveraging LLMs (warm start, variable fixing and ReAct) and four black-box solvers (Bayesian optimization, genetic algorithms, mesh adaptive direct search and random search) on an electric vehicle battery pack cost minimization case study across four types of redesign scenarios. We find that the integrated approach can match feasible design discovery of the numerical-solver baselines with 80% fewer simulator evaluations while tripling the fraction of runs that find near-optimal solutions. We find that the best LLM-solver integration approach and the way the prior solution is leveraged depend on the structure of the design requirement change, and that the benefit of increasing LLM model size grows with the extent to which the LLM controls the search. These results show clear potential for LLMs in redesign tasks for guiding or replacing numerical solvers.

---


### 189. [MemSteer: Turning User Histories into Supervision for Agent Memory Optimization](https://arxiv.org/abs/2610.39276)

**<font color=#1a73e8>作者：</font>** Jie Huang, Cuiling Lan, Qize Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An effective agent memory system should adapt to a user's history and task requirements. Human-annotated supervision can guide this adaptation by providing feedback for evaluating and improving memory designs. Yet suitable labels are rarely available for new user histories, and manually constructing QA pairs and supporting evidence is costly. We introduce MemSteer, which turns unlabeled user histories into question-answer (QA) supervision with supporting evidence for memory-design optimization. MemSteer constructs an evidence-grounded answer plan that specifies how facts across related records jointly support a reference answer. The plan guides question generation, while source-grounded auditing and blind answer recovery check the resulting annotations. To study the utility of this supervision, we develop MemSteer-Opt, which combines QA-based design evaluation with evidence-guided failure diagnosis to revise memory store, retrieval, and context construction without updating model parameters. Experiments on ATM-Bench and RHELM show that this supervision is competitive with official-QA-guided optimization. Relative to Base-BM25, MemSteer-Opt improves ATM-Bench Question Score by 13.4 points and RHELM accuracy by 4.1 and 6.6 points without and with external data, respectively. The supervision also benefits two existing optimizers on ATM-Bench, while new-user experiments demonstrate continued design optimization using supervision generated from the target histories.

---


### 190. [What Does "Now" Mean to Your Computer-Use Agent? Stale Screenshots, Page Loads, and Which Check to Run Before a Click](https://arxiv.org/abs/2610.39282)

**<font color=#1a73e8>作者：</font>** Vasundra Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents plan on a screenshot for several seconds and then click at a position on the screen; if the page has changed in the meantime, the click lands on an unintended element. Prior work treats the planning interval as the source of this risk. Measuring planned clicks on 31 public web pages, we find that the risk lies in page loading: 0.4% of clicks planned on fully loaded pages became stale within 30 seconds, against 17% of clicks planned in the first second after a page opened. On these pages, waiting about one second for network activity to stop removes most of this risk, yet the wait rules of eight of ten widely used open-source agents leave more than 1% of clicks stale. Commercial pages keep loading for longer: in the HTTP Archive's public crawl, 15% of 65 desktop booking and buying home pages went 500 ms without network requests within 3 seconds of their HTML being parsed, against 63% of 3,028 .gov pages, and 52% shifted their layout within 6.5 seconds of a network-idle wait capped at 3 seconds, against 8% (61% against 26% among pages recorded in full). Where a check before the click is needed, as before irreversible actions and on pages that are still loading, a pixel comparison verifies the target's position as accurately as a frontier vision-language model at one eighth of the latency, and a 4B model matches the frontier model in verifying whether the previous action succeeded. We release a benchmark generator, a break-even formula for when a check pays, and three rules for agent developers: this https URL

---


### 191. [Unlocking Any-Order Generation in Pretrained Autoregressive Image Models](https://arxiv.org/abs/2610.39293)

**<font color=#1a73e8>作者：</font>** Rishav Pramanik, Marco Pedersoli, Zhaozheng Yin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) image generators are powerful in principle but inflexible in practice: training with a fixed raster-scan order hardcodes a single factorization of the image distribution into the model, leaving it unable to inpaint, outpaint, or edit at inference time. Existing solutions, including the modern discrete-diffusion family, train from scratch on a mixture of token orderings, paying roughly 3x the compute of standard raster-scan training; discrete diffusion further sacrifices compatibility with the AR inference ecosystem (KV caching, vLLM) by construction. We argue that this cost is unnecessary. A pretrained raster-scan AR model has already learned the joint distribution over image tokens; what it lacks is not knowledge but the ability to express that knowledge through non-sequential conditional pathways. We propose a recipe for adapting pretrained raster-scan models into any-order generators using two components: future-aware positional embeddings that resolve a target-position identifiability problem at negligible overhead, and an ordering curriculum that traces a stable optimization path from the pretrained solution to a good any-order basin. Applied to four base models across two architectures and two scales (LlamaGen-L/XL, RAR-L/XL), the recipe substantially outperforms MaskGIT on ImageNet inpainting (FID 6.21 vs. 10.44) and outpainting, is competitive with MAR-L, trades a 1.2-1.9 increase in class-conditional FID for this flexibility, and costs 13-33% additional compute beyond pretraining, while leaving the standard AR inference stack untouched. Inpainting, outpainting, and editing, our results suggest, need not be added to autoregressive image models. They can be unlocked from the ones that exist. Code is available at this https URL.

---


### 192. [There Is No Free Lunch in RLVR: Every pass@1 Gain Has a pass@k Price](https://arxiv.org/abs/2610.39295)

**<font color=#1a73e8>作者：</font>** Yinuo Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) makes a language model solve more problems on the first try and fewer when given many tries: it raises pass@1 while the base model overtakes it at large sampling budget k. Is this a failure of RL to add reasoning, or a transient that more training removes? We settle the question with a theorem. The reversal is a price, and we compute its exact rate. Modeling RLVR as an exponential tilt of a base policy over strategies shared across prompts, we prove that under exclusive specialization every update that raises pass@1 strictly lowers the success of some prompt; a strictly positive price on prompts (Stiemke duality) is the exact condition, and being merely the best strategy on a prompt is provably not enough. When the loss reaches the hardest prompts, it forces a pass@k crossover, and the number of crossings is at most the sign variation of the shift in per-prompt success, a totally positive bound that is tight and that recovers the known single-crossover result as its order-preserving case. The crossover is not a bug to patch: a constrained update traces the exact pass@1 versus pass@k frontier, and removing the crossover entirely costs the entire pass@1 gain. The same tilt identity yields entropy collapse and the entropy-performance law with an identifiable exponent, unifying two literatures under one mechanism. Reinforcement cannot widen the reasoning frontier; it can only move along it, at a price we make measurable by a diagnostic that reads the bound, the order-preserving test, and the price from any evaluation log. There is no free lunch, only a price.

---


### 193. [Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities](https://arxiv.org/abs/2610.39301)

**<font color=#1a73e8>作者：</font>** Yunhang Shen, Zhangquan Chen, Xiaotian Li 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Youtu-Parsing-Omni, an omni-modal parser that converts documents, images, audio, and video into structured records grounded in space and time, providing a perception layer for agents that read, locate, and cite evidence across modalities. Its design rests on one encoder for every modality and one schema for every task. Youtu-Omni-Encoder, initialized from a pre-trained language model to strengthen text reading, encodes all modalities with shared weights in a unified space-time coordinate system, and a few fusion layers let video frames attend to concurrent audio, bringing cross-modal fusion and temporal alignment into perception itself. OmniSchema unifies the outputs of all ten parsing tasks, allowing a single self-evolving post-training procedure, OmniSchema-Aware On-Policy Distillation (OSAD), to provide a shared token-role-based objective across tasks. In each round, the model is trained on its own rollouts against token-level targets from a reference-conditioned copy of itself, which is then refreshed with the trained weights, so that the parser and its supervision co-evolve. With a single 5 B-parameter checkpoint, Youtu-Parsing-Omni achieves state-of-the-art performance on OmniDocBench v1.6 (96.96 Overall) and leads all open-weight models on OmniParsingBench (75.08 Avg.), with its advantage concentrated on audio and video. It also achieves the best overall chart-parsing score (95.02) and the highest exact chemical-fingerprint agreement among compared systems, and matches a dedicated optical-music model in character-level transcription of typeset sheet music while staying far ahead of general-purpose systems. Code and model weights are publicly available.

---


### 194. [Proving and Improving the Platonic Representation Hypothesis with JEPAs](https://arxiv.org/abs/2610.39302)

**<font color=#1a73e8>作者：</font>** Randall Balestriero, Yann LeCun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether models trained on different modalities converge to the same representation of the world is central to AI. The Platonic Representation Hypothesis (PRH) conjectures that they do as they scale, but without a proof it offers neither a guarantee nor a recipe. We turn the hypothesis into a theorem. First, we prove a \emph{Platonic Representation Theorem}: Joint-Embedding Predictive Architectures (JEPAs) trained separately on any number of modalities learn the same representation up to one rotation whenever their positive pairs are two observations of one scene--\emph{good views}--and their misalignment is bounded otherwise. Second, we show that next-token prediction is a JEPA with \emph{bad views}, parts of a single document, which explains why language models align with vision only through scale. Third, we validate the theory from 145k captions to the texts of 940M web images, and uncover a scaling law of alignment that predicts unseen runs within seed noise. Good views need 42 times fewer training samples than next-token prediction on the same corpus to reach the same alignment, and a 109M-parameter text JEPA aligns with DINOv2 and CLIP's image encoders better than every language model we evaluated, up to 72B parameters, and than CLIP's text encoder: next-token prediction is a remarkably inefficient route to platonic representations. As a showcase, one rotation turns separately trained encoders into an image captioner (CIDEr .838 on COCO). Even that rotation needs no pair: on the latest pair-free benchmark, our text JEPA beats every zero-shot accuracy reported with language models up to 8B parameters, e.g., 64\% against at most 56\% top-5 on ImageNet-100. Positive views, and not scale alone, are thus the lever to build platonic representations.

---


### 195. [CAD-WAM: Anticipating Geometry for Text-to-CAD Generation](https://arxiv.org/abs/2610.39306)

**<font color=#1a73e8>作者：</font>** Zhengyang Li, Weijie Zheng, Yuxin Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating editable computer-aided design (CAD) models from text requires selecting operations that produce the intended changes to the geometry constructed so far. An incorrect operation can compromise subsequent steps, making reliable multi-step generation challenging. Existing methods based on large language models (LLMs) primarily learn to predict commands, without explicit supervision of the geometric states those commands should produce. Inspired by world-action models, we introduce CAD-WAM, which couples geometry-conditioned action generation with next-state prediction. We define complete modeling operations as actions in a CAD domain-specific language (DSL) and encode surface point clouds of intermediate solids into compact latent states using a pretrained variational autoencoder. An LLM backbone generates the next action from the target description and current geometric state, while an auxiliary head on the same backbone predicts the next state to provide geometric supervision during training. We construct step-wise training trajectories from parametric CAD models in the DeepCAD dataset, pairing each trajectory with an expert-level textual description. At inference, each generated action is executed by a CAD kernel, and the resulting solid is re-encoded to inform the next decision. On the DeepCAD test set, CAD-WAM outperforms the task-specific baselines in geometric accuracy and output validity, with larger gains on models requiring more operations, and produces more accurate geometry than general-purpose LLMs prompted with the same DSL. Ablations further show that next-state supervision reduces mean Chamfer distance by 13.2\% relative to an otherwise identical model trained only to predict actions. Code is available at this https URL.

---


### 196. [MRC-MMAgent: Reinforcement Learning for Multi-Role Collaboration in Multimodal Tool-Using Agents](https://arxiv.org/abs/2610.39324)

**<font color=#1a73e8>作者：</font>** Shengqin Wang, Jie Jin, Xiaofan Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal tool-using agents augment vision-language models with access to external information and capabilities, enabling them to solve knowledge-intensive and visually complex tasks that cannot be addressed using visual context alone. However, existing reinforcement learning pipelines largely train single-role agents to search and answer using terminal rewards, overlooking how humans inspect retrieved evidence, reformulate queries, and revise conclusions during search. Consequently, they fail to optimize this self-corrective process over complete interaction trajectories. We propose MRC-MMAgent, a multi-role collaborative reinforcement learning framework that incorporates trajectory assessment and continuation directly into the executable agent loop. First, the framework establishes a multi-role collaborative loop that integrates solving, inspection, and continuation, enabling the agent to acquire evidence through tools, evaluate the preceding trajectory, and resume problem solving when the current answer is insufficiently supported. Second, we introduce a role-coupled learning objective that combines task success, interaction validity, and successful correction with full-trajectory policy optimization across the decisions generated by all roles. Extensive experiments show that, using only the original baseline training set without constructing additional datasets, our method consistently outperforms the corresponding base models and achieves leading or highly competitive performance across benchmarks.

---


### 197. [Telling Is Not Seeing: Textual Personas Rarely Make Vision-Language Models Answer Like the People They Describe](https://arxiv.org/abs/2610.39331)

**<font color=#1a73e8>作者：</font>** Jiawei Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly prompted with personas, such as "You have low vision", to stand in for people in user studies. We ask whether a persona makes a model see like the person it describes. We compare persona answers with measured people with low vision, color blindness or hearing loss, and with simple rules that use only the facts the persona states. The persona never beats these rules, and it erases the real differences between groups and individuals. Describing blur leaves recognition unchanged in all 14 models we test, while blurring the photo lowers it as it does for people. Inside open models, the description changes neither the image information nor the answer probabilities. Yet the models know the effects they fail to show: they can estimate how blur and illusions affect people. Telling is not seeing: a persona makes a model say what it knows about people, not see what they see.

---


### 198. [RetroChessBench: A Benchmark for Reconstructing and Proving Chess Histories](https://arxiv.org/abs/2610.39341)

**<font color=#1a73e8>作者：</font>** Tidor-Vlad Pricope  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier language models such as GPT 6 Astra have contributed to research mathematics, demonstrating substantial reasoning capabilities. Yet serious reasoning failures persist even in tasks governed by explicit rules. We demonstrate this in retrograde chess which is a playground for pure reasoning, where solvers reconstruct legal histories and distinguish possible events from forced ones. We introduce RetroChessBench, a 12-task benchmark covering exact-length constructions, unique endings, and exhaustive answer sets, with references, rubrics, and a terminal-reward environment. In two trials per task and condition, GPT 6 Astra High fails to produce the required final answer in 22/24 attempts without tools and 18/24 with code execution; mean terminal RL rewards are 14.75% and 27.19%, respectively. The examples identify faulty deductions: failed responses reject legal histories and treat temporary obstructions as permanent. Online retrograde archives often provide puzzles and final move sequences without detailed derivations. We hypothesize that limited exposure to these missing explanations in web-derived training data contributes to the observed reasoning failures. This questions how far frontier mathematical reasoning really generalizes beyond familiar solution patterns. Claims of general intelligence require evidence that models can transfer learnt principles to areas with few worked examples.

---


### 199. [Cord: Confidence-Anchored Order Residual Decoding for Masked Diffusion Language Models](https://arxiv.org/abs/2610.39372)

**<font color=#1a73e8>作者：</font>** Chengwei Zhou, Zhaoyan Jia, Massoud Pedram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The decoding order of masked diffusion language models (dLLMs) can substantially affect generation quality, yet common decoders typically apply the same reveal rule throughout generation. Confidence provides a strong default, but it measures how decisively a position can be predicted now, not how useful revealing that position will be for subsequent decoding. We propose Cord, a lightweight prompt-conditioned policy that retains confidence decoding as a stable reference and learns when and how to depart from it through geometric residuals over generation direction, proximity to revealed context, and two-sided infilling. The residuals adapt to both the prompt and the evolving partial response. Rather than sampling a new policy action at every decoding step, Cord samples a single low-dimensional coefficient matrix per rollout, which induces an entire state-dependent reveal trajectory. This yields a contextual-bandit formulation trained directly from sequence-level rewards, without step-level credit assignment or backbone updates. Across three dLLMs and five reasoning, code, and constraint-satisfaction benchmarks, Cord improves average task success from 32.0% under confidence decoding to 48.2%, and further improves over the best per-domain fixed residual. Behavioral audits show that the learned residuals induce substantial, task-dependent changes in reveal locality and two-sided infilling. Cord adds only $0.53$M trainable parameters, requires no additional backbone forward passes, and incurs only 5.39% inference latency overhead.

---


### 200. [What Makes Medical Examination Items Difficult? Using Large Language Models to Explore Patterns Associated With Empirical Item Difficulty](https://arxiv.org/abs/2610.39373)

**<font color=#1a73e8>作者：</font>** Xiaomeng Xiong, Marcus Walker, Yanlin Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research on medical item difficulty has largely focused on prediction rather than on identifying interpretable patterns associated with empirical difficulty. This study used empirical difficulty labels to guide large language models (LLMs) in inducing difficulty rubrics and examined how rubric guidance affected LLM difficulty judgments. Using training items and their empirical difficulty estimates from the United States Medical Licensing Examination (USMLE) and the Physician Assistant National Certifying Examination (PANCE), Claude Opus 5 induced separate rubrics for absolute and pairwise difficulty judgment. None of the induced rubrics treated surface features, such as stem length, option count, or images, as major sources of difficulty. Several patterns emerged across both examinations, including cue convergence, misleading cues, and option competition, although their specific forms differed. Retrieval of knowledge that could not be derived from the stem was particularly prominent in the PANCE rubrics, whereas the USMLE rubrics placed greater emphasis on integrating multiple clinical cues. We compared commercial and open-weight LLMs on held-out items under unguided and rubric-guided conditions. Rubric guidance changed how models used the difficulty scale but did not consistently improve performance. In absolute judgments, guidance encouraged broader use of the scale and generally improved coarse-grained agreement, without consistently improving rank ordering. In pairwise comparisons, its effects varied across models and examinations, and judgments became more sensitive to presentation order. These findings suggest that the value of label-guided rubric induction may lie more in generating interpretable, testable hypotheses from empirical difficulty data than in reliably improving difficulty judgments.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
